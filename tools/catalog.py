"""Build navigation and bounded retrieval from maintained reference metadata."""
import collections, hashlib, json, os, re, sqlite3
from pathlib import Path
from urllib.parse import unquote
import kb

def records(root):
 for base in [root/'shared/reference',root/'domains']:
  if not base.exists():continue
  for p in sorted(base.rglob('*.md')):
   m,t=kb.metadata(p)
   if not m or m.get('template') is True:continue
   title=next((line[2:] for line in t.splitlines() if line.startswith('# ')),p.stem)
   yield {'path':p.relative_to(root).as_posix(),'title':title,**m}
def generate_navigation(root,ss,selection=None):
 canonical,canonical_conflicts=kb.canonical_schemas(root,ss)
 allowed=None
 if selection:
  import refresh
  selected=refresh.selection_sources(root,selection)
  allowed={s['set_path'] for s in selected}
  allowed.update(m['set_path'] for s in selected for m in s.get('memberships',[]) if m.get('set_path'))
  for item in selection.get('affected',[]):
   match=re.match(r'(.*/reference/(?:message-sets|code-sets)/[^/]+/[^/]+)/',item['path'])
   if match:allowed.add(match.group(1))
 canonical_pages={}
 for pattern in ['shared/reference/messages/*/index.md','domains/*/reference/messages/*/index.md']:
  for cp in root.glob(pattern):
   cm,_=kb.metadata(cp)
   if cm.get('document_kind')=='message-index' and cm.get('message_id'):canonical_pages[cm['message_id']]={'path':cp,'metadata':cm}
 workbook_manifest=root/'work/workbook-results.json'
 workbook_outputs={x['source_id']:x['output'] for x in json.loads(workbook_manifest.read_text(encoding='utf-8'))} if workbook_manifest.exists() else {}
 sets=collections.defaultdict(list)
 for source in ss:
  sets[source['set_path']].append(source)
  for membership in source.get('memberships',[]):
   if membership.get('set_path') and membership['set_path']!=source['set_path']:
    view={**source,**membership}
    if not any(x['source_id']==source['source_id'] for x in sets[membership['set_path']]):sets[membership['set_path']].append(view)
 output=[]
 for setpath,group in sets.items():
  folder=root/setpath;page=folder/'index.md'
  if allowed is not None and setpath not in allowed:
   if page.exists():
    m,_=kb.metadata(page)
    inferred='code-publication' if '/code-sets/' in setpath else 't2s-aggregation' if group[0]['set_slug']=='t2s' else 'message-set'
    output.append({'path':setpath+'/index.md','collection_kind':inferred,**m})
   continue
  first=group[0];ids=sorted(set(m for s in group for m in s.get('message_ids',[])))
  ids=sorted(set(ids)|{mid for mid,cp in canonical_pages.items() if first['set_slug'] in cp['metadata'].get('message_sets',[]) and set(cp['metadata'].get('source_ids',[]))&{s['source_id'] for s in group}})
  if first['set_slug']=='t2s':ids=sorted(set(ids+[m for s in ss if s['collection']=='target2securities_t2s' and s['format']=='xsd' for m in s['message_ids']]))
  editions=sorted(set(s['source_edition'] for s in group if s.get('source_edition')))
  schema_only=all(s['format']=='xsd' for s in group)
  limitations=['All source tables and figures require recorded visual reconciliation before this set can be reviewed.']
  if schema_only:limitations.append('No MDR narrative documentation is supplied for this collection; business purpose, participants and flows cannot be established from XSD alone.')
  meta={'template':False,'document_kind':'message-set-index','review_status':'needs-review','domain':first['domain'],'message_set':first['set_title'],'set_slug':first['set_slug'],'source_ids':[s['source_id'] for s in group],'source_editions':editions,'message_ids':ids,'limitations':limitations}
  if '/code-sets/' in setpath:meta['document_kind']='code-set-index'
  meta['collection_kind']='code-publication' if '/code-sets/' in setpath else ('t2s-aggregation' if first['set_slug']=='t2s' else 'message-set')
  text=kb.front(meta)+'# '+first['set_title']+'\n\n'
  text+='This reference groups the supplied collection while retaining each publication edition in its source metadata. Message versions and MDR editions are separate. Business-area prefixes do not determine domain ownership.\n\n'
  text+='## Supplied sources\n\n'+kb.table(['Source','Format','Publication label / evidence','Content identity / occurrences'],[[kb.source_link(root,page,s),s['format'],s.get('source_edition') or 'Unknown; see source metadata',s['sha256']+'; '+str(len(s['occurrences']))] for s in group])
  membership=[]
  for m in ids:
   cs=canonical.get(m)
   evidence=', '.join(s['source_id'] for s in group if m in s.get('message_ids',[]))
   cp=canonical_pages.get(m)
   if not evidence and cp:evidence=', '.join(cp['metadata'].get('source_ids',[]))
   membership.append([m.rsplit('.',2)[0],kb.link(page,cp['path'],m) if cp else kb.link(page,root/kb.area(cs['domain'])/'reference/messages'/m/'index.md',m) if cs else m+' (schema not supplied)',evidence or 'Supplied T2S schema/archive member',cs['source_id'] if cs else 'Not supplied; documentation-only evidence'])
  text+='## Canonical message definitions\n\n'+kb.table(['Family','Exact definition','Membership evidence','Schema source'],membership)
  docs=[]
  for child in ['documents','workbooks']:
   for p in sorted((folder/child).glob('*/index.md')):docs.append([kb.link(page,p,p.parent.name),child,'needs-review'])
  for p in sorted(folder.glob('*.md')):
   if p.name not in ['index.md','coverage.md']:docs.append([kb.link(page,p,p.stem),'curated context','see page'])
  for child in ['flows','diagrams']:
   p=folder/child/'index.md'
   if p.exists():docs.append([kb.link(page,p,child.title()),'curated context','see page'])
   for p in sorted((folder/child).glob('*/index.md')):docs.append([kb.link(page,p,p.parent.name),'focused '+child,'see page'])
  if first['set_slug']=='t2s':
   for target,subgroup in sets.items():
    if target!=setpath and subgroup[0]['collection']=='target2securities_t2s':docs.append([kb.link(page,root/target/'index.md',subgroup[0]['set_title']),'separate archive message set','needs-review'])
  # Preserve externally curated code-publication landing pages.
  if '/code-sets/' not in setpath or not page.exists():
   oldmeta,oldbody=kb.metadata(page) if page.exists() else ({},'')
   extra=re.search(r'\n<!-- [^\n]+ -->',oldbody)
   retained=oldbody[extra.start():] if extra else ''
   if oldmeta.get('manual_curated') or (selection is not None and page.exists()):
    oldmeta.update(message_ids=ids,source_ids=meta['source_ids'],source_editions=editions)
    if selection is not None:
     oldbody=re.sub(r'\n<!-- REFRESH-NAV-START -->.*?<!-- REFRESH-NAV-END -->\n?','\n',oldbody,flags=re.S)
     oldbody+='\n<!-- REFRESH-NAV-START -->\n## Current supplied membership\n\n'+kb.table(['Family','Exact definition','Membership evidence','Schema source'],membership)+'\n<!-- REFRESH-NAV-END -->\n'
    kb.put(page,kb.front(oldmeta)+oldbody.lstrip('\r\n'))
   else:kb.put(page,text+'## Focused evidence and context\n\n'+kb.table(['Reference','Kind','Review'],docs)+'## Gaps\n\n'+'\n'.join('- '+x for x in limitations)+'\n\n'+kb.link(page,folder/'coverage.md','Extraction coverage')+' · '+kb.link(page,root/'catalog/README.md','Catalog')+'\n'+retained)
  rows=[]
  for s in group:
   stats=root/'work/documents'/s['source_id']/'status.json';workbook=root/'work/workbooks'/s['source_id']/'manifest.json'
   dest=folder/'documents'/s['source_id']/'index.md'
   if s['format']=='xsd':
    dest=root/kb.area(s['domain'])/'reference/messages'/s['message_ids'][0]/'structure.md' if s.get('message_ids') else root/'catalog/sources.json'
   elif s['format']=='xlsx':dest=folder/'workbooks'/s['source_id']/'index.md'
   elif s['format']=='json':dest=page
   elif s['format']=='zip':dest=root/'catalog/sources.json'
   if stats.exists():
    result=json.loads(stats.read_text(encoding='utf-8'))
    if result.get('output'):dest=root/result['output']
   if s['source_id'] in workbook_outputs:dest=root/workbook_outputs[s['source_id']]
   exists=dest.exists()
   if s.get('disposition')=='conflicting-candidate':
    s['comparison_reference_paths']=[dest.relative_to(root).as_posix()] if exists else []
    exists=False
   if s.get('disposition') not in ['historical-source-revision','conflicting-candidate'] and (not exists or s.get('disposition') not in ['processed-with-source-limitations','processed-needs-review','reviewed']):
    s['disposition']='extracted-needs-review' if exists and s['format']!='zip' else ('inventory-complete' if s['format']=='zip' else 'queued')
   maintained_paths=[p for p in s.get('canonical_output_paths',[]) if (root/p).exists()]
   s['canonical_output_paths']=list(dict.fromkeys(([dest.relative_to(root).as_posix()] if exists else [])+maintained_paths))
   if s.get('review_status')!='reviewed' and s.get('disposition')!='conflicting-candidate':s['review_status']='needs-review' if exists else 'draft'
   rows.append([s['source_id'],s['format'],s['disposition'],kb.link(folder/'coverage.md',dest,'Evidence') if exists else 'Pending','See item-level review evidence and remaining source-wide limitations' if s['format'] in ['docx','pdf','xlsx'] else 'See declaration coverage' if s['format']=='xsd' else 'See publication reference'])
  coverage=kb.front({**meta,'document_kind':'extraction-coverage'})+'# '+first['set_title']+' extraction coverage\n\n'+kb.table(['Source','Format','Disposition','Destination','Review'],rows)
  coverage+='## Boundaries and pending checks\n\nEach extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.\n\n'
  coverage+='- Reconcile every source table and figure with its complete rendered original.\n- Review participant definitions, activity order and message direction against the source.\n- Render Mermaid reconstructions and compare their labels and relationships.\n- Resolve document edition conflicts before combining business statements.\n\n'+kb.link(folder/'coverage.md',root/'tracking/issues.md','Open issues')+' · '+kb.link(folder/'coverage.md',page,'Set index')+'\n'
  if '/code-sets/' not in setpath or not (folder/'coverage.md').exists():
   covpage=folder/'coverage.md';cm,cb=kb.metadata(covpage) if covpage.exists() else ({},'');extra=re.search(r'\n<!-- [^\n]+ -->',cb)
   if selection is not None and covpage.exists():
    cb=re.sub(r'\n<!-- REFRESH-COVERAGE-START -->.*?<!-- REFRESH-COVERAGE-END -->\n?','\n',cb,flags=re.S)
    kb.put(covpage,kb.front(cm)+cb.lstrip('\r\n')+'\n<!-- REFRESH-COVERAGE-START -->\n## Current refresh disposition\n\n'+kb.table(['Source','Format','Disposition','Destination','Review'],rows)+'\n<!-- REFRESH-COVERAGE-END -->\n')
   elif not cm.get('manual_curated'):kb.put(covpage,coverage+(cb[extra.start():] if extra else ''))
  actualmeta,_=kb.metadata(page) if page.exists() else (meta,'')
  output.append({'path':setpath+'/index.md',**actualmeta,'schema_only':schema_only})
 return output

def rebuild(root,selection=None):
 ss=kb.sources(root);sets=generate_navigation(root,ss,selection)
 rr=list(records(root))
 # Canonical definitions exist exactly once; metadata and schema coverage define identity.
 messages=[r for r in rr if r.get('document_kind')=='message-index']
 participants=[r for r in rr if r.get('document_kind') in ['participant','participant-reference','shared-participant']]
 flows=[r for r in rr if r.get('document_kind') in ['flow','business-flow','flow-reference']]
 diagrams=[r for r in rr if r.get('document_kind')=='diagram']
 concepts=[r for r in rr if r.get('document_kind') in ['schema-type','concept','business-concept']]
 def compact(r):
  return {k:v for k,v in r.items() if k in ['path','title','document_kind','review_status','domain','message_id','message_family','message_families','message_name','namespace','schema_status','documentation_status','message_ids','source_ids','source_editions','source_line','source_locations','schema_path','participant_id','participant_ids','flow_id','flow_ids','participants','flows','source_labels','aliases','search_terms','limitations','message_sets','message_set','qname_or_schema_path','type_id','role_kind','role_type']}
 for name,items in [('messages',messages),('message-sets',sets),('participants',participants),('flows',flows),('diagrams',diagrams),('concepts',concepts)]:
  output=[compact(x) if name!='message-sets' else x for x in items]
  kb.dump(root/'catalog'/f'{name}.json',{'schema_version':1,'updated':kb.DATE,'records':output})
  page=root/'catalog'/f'{name}.md'
  kb.put(page,'# '+name.replace('-',' ').title()+'\n\nDerived from maintained reference metadata. Use the helper for bounded search. Draft and needs-review records expose unresolved checks.\n\n'+kb.table(['Reference','Domain','Source identities','Review'],[[kb.link(page,root/x['path'],x.get('title') or x.get('message_set') or x.get('set_slug')),x.get('domain',''),', '.join(x.get('source_ids',[])),x.get('review_status','needs-review')] for x in items])+'[Entry guide](README.md)\n')
 dbpath=root/'catalog/search.sqlite';db=sqlite3.connect(dbpath)
 db.execute('DROP TABLE IF EXISTS pages');db.execute('CREATE VIRTUAL TABLE pages USING fts5(path UNINDEXED,kind UNINDEXED,title,terms,metadata UNINDEXED)')
 for r in rr:
  vals=[]
  for key in ['message_id','message_ids','message_family','message_families','message_name','participant_id','participant_ids','flow_id','flow_ids','participants','flows','source_labels','aliases','search_terms','qname_or_schema_path','message_set','message_sets','role_kind','role_type','definition','source_ids']:
   v=r.get(key)
   if v:vals.append(json.dumps(v,ensure_ascii=False) if not isinstance(v,str) else v)
  terms=' '.join(vals);terms=re.sub(r'([a-z])([A-Z])',r'\1 \2',terms)
  db.execute('INSERT INTO pages VALUES(?,?,?,?,?)',(r['path'],r.get('document_kind',''),r['title'],terms,json.dumps(compact(r),ensure_ascii=False)))
 db.commit();db.close()
 summary={'date':kb.DATE,'unique_sources':len(ss),'source_occurrences':sum(len(s['occurrences']) for s in ss),'domains':dict(collections.Counter(x.get('domain') for x in messages)),'message_set_editions':len(sets),'messages':len(messages),'families':len(set(x.get('message_family') for x in messages)),'participants':len(participants),'flows':len(flows),'schema_components':len(concepts),'diagram_pages':len(diagrams),'pages':len(rr),'review_status_counts':dict(collections.Counter(x.get('review_status') for x in rr)),'all_supplied_material_processed':False,'all_desired_knowledge_available':False}
 summary['schema_components']=sum(r.get('document_kind')=='schema-type' for r in rr)
 summary['messages_with_supplied_schema']=sum(x.get('message_id') in {m for s in ss if s['format']=='xsd' for m in s.get('message_ids',[])} for x in messages)
 summary['documentation_only_messages']=sum(x.get('schema_status')=='not-supplied' for x in messages)
 summary['input_collections']=len(set(s['collection'] for s in ss))
 summary['archive_message_sets']=len({s['set_slug'] for s in ss if s.get('set_slug')!='t2s' and any(o.get('archive_member') for o in s.get('occurrences',[]))})
 summary['reference_groups']=len(sets)
 summary['code_publication_groups']=sum(x.get('collection_kind')=='code-publication' for x in sets)
 summary['message_set_editions']=sum(x.get('collection_kind')=='message-set' for x in sets)
 summary['message_sets']=len(set(x['set_slug'] for x in sets if x.get('collection_kind')=='message-set'))
 summary['business_concepts']=sum(r.get('document_kind')=='business-concept' for r in rr)
 summary['comparison_concepts']=sum(r.get('document_kind')=='concept' for r in rr)
 summary['source_process_sections']=sum(r.get('document_kind')=='source-process-section' for r in rr)
 summary['reference_kind_counts']=dict(collections.Counter(r.get('document_kind') for r in rr))
 summary['diagram_render_states']=dict(collections.Counter(r.get('render_status','not-recorded') for r in diagrams))
 def visual_state(r):
  value=r.get('visual_review','not-recorded')
  if isinstance(value,dict):return value.get('result',value.get('status','recorded-without-result'))
  if isinstance(value,list):return 'recorded-evidence-list'
  return str(value)
 summary['diagram_visual_review_states']=dict(collections.Counter(visual_state(r) for r in diagrams))
 docs=[]
 for p in (root/'work/documents').glob('*/status.json'):
  d=json.loads(p.read_text(encoding='utf-8'));docs.append(d)
 summary['document_extraction']={'docx_sources':sum(d['format']=='docx' for d in docs),'docx_tables':sum(d.get('tables',0) for d in docs if d['format']=='docx'),'docx_drawing_occurrences':sum(d.get('figure_occurrences',0) for d in docs if d['format']=='docx'),'pdf_sources_text_and_tables':sum(d['format']=='pdf' and d.get('pdf_tables_scanned',False) for d in docs),'pdf_pages':sum(d.get('pages',0) for d in docs if d['format']=='pdf'),'pdf_table_candidates':sum(d.get('tables',0) for d in docs if d['format']=='pdf'),'limitation':'Candidate counts are not confirmed unique substantive-table or diagram totals; source-wide visual reconciliation remains incomplete.'}
 wbpath=root/'work/workbook-results.json'
 if wbpath.exists():summary['workbook_extraction']=[{'source_id':d['source_id'],'format':d['format'],'counts':d.get('counts',{})} for d in json.loads(wbpath.read_text(encoding='utf-8'))]
 evidence_files={
  'docx_reconciliation':'tracking/reviews/docx-coverage-reconciliation.json',
  'canonical_diagram_evidence':'tracking/reviews/diagram-record-audit.json',
  'pdf_structural_review':'catalog/pdf-structural-review.json',
  'workbook_review':'tracking/reviews/workbook-status-audit.json',
  'native_object_dispositions':'catalog/native-object-dispositions.json'}
 summary['scoped_review_evidence']={k:v for k,v in evidence_files.items() if (root/v).exists()}
 summary['review_boundary']='Processing and fidelity checks do not resolve source contradictions, unavailable business context or uninspected native/internal content. Read the linked scoped evidence; counts include source occurrences and table parts where named.'
 assessment_path=root/'tracking/corpus-assessment.json'
 if assessment_path.exists() and selection is None:
  assessment=json.loads(assessment_path.read_text(encoding='utf-8'))
  if assessment.get('source_fingerprints')=={s['source_id']:s['sha256'] for s in ss}:
   for key in ['all_supplied_material_processed','all_desired_knowledge_available','all_supplied_sources_processed_to_recorded_limits']:
    if key in assessment:summary[key]=assessment[key]
   summary['corpus_assessment']='tracking/corpus-assessment.json'
 kb.dump(root/'catalog/coverage-summary.json',summary)
 # Preserve source identity fields while updating only processing disposition.
 manifest=json.loads((root/'catalog/sources.json').read_text(encoding='utf-8'));manifest['sources']=ss;kb.dump(root/'catalog/sources.json',manifest)
 source_page=root/'tracking/source-register.md'
 source_rows=[]
 for s in ss:
  occurrence_links=[]
  for o in s['occurrences']:
   occurrence_links.append((kb.link(source_page,root/o['path'],o['path']) if o.get('availability','current')=='current' else o['path']+' ('+o['availability']+' historical occurrence)')+((chr(32)+'member '+chr(96)+o['archive_member']+chr(96)) if o.get('archive_member') else ''))
  source_rows.append([s['source_id'],'<br>'.join(occurrence_links),s['format'],s['sha256'],s.get('source_edition') or 'Unknown; see metadata',s['disposition'],', '.join(s.get('job_ids',[])),'<br>'.join(kb.link(source_page,root/p,'Reference') for p in s.get('canonical_output_paths',[]))])
 kb.put(source_page,'# Source register\n\nMaintained identities and all source locations are in [sources.json](../catalog/sources.json). Changed bytes receive a new identity; identical loose/archive occurrences share one canonical content record. Publication labels and unresolved limitations remain explicit.\n\n'+kb.table(['ID','Original occurrences','Format','SHA-256','Publication','Disposition','Jobs','Output'],source_rows)+'[Jobs](conversion-status.md) · [Issues](issues.md)\n')
 for dom in ['shared','securities','payments','trade-finance','cards','fx']:
  page=root/kb.area(dom)/'index.md';relevant=[x for x in sets if x['domain']==dom]
  if selection is not None:
   import refresh
   relevant_domains={s['domain'] for s in refresh.selection_sources(root,selection)}
   if dom not in relevant_domains:continue
   if page.exists():
    body=page.read_text(encoding='utf-8');body=re.sub(r'\n<!-- REFRESH-DOMAIN-START -->.*?<!-- REFRESH-DOMAIN-END -->\n?','\n',body,flags=re.S)
    body+='\n<!-- REFRESH-DOMAIN-START -->\n## Current publication navigation\n\n'+kb.table(['Message set','Publication grouping','Review'],[[kb.link(page,root/x['path'],x.get('message_set',x.get('set_slug'))),', '.join(x.get('source_editions',[])) or 'Unknown',x.get('review_status','needs-review')] for x in relevant])+'\n<!-- REFRESH-DOMAIN-END -->\n'
    kb.put(page,body);continue
  kb.put(page,'# '+dom.replace('-',' ').title()+'\n\n'+('No supplied collection is routed here in the current inventory.\n\n' if not relevant else 'Sources retain their message-set folders under raw-input. Exact message definitions have one canonical reference; membership and business-area codes remain separate.\n\n')+kb.table(['Message set','Publication grouping','Review'],[[kb.link(page,root/x['path'],x['message_set']),', '.join(x['source_editions']) or 'Unknown','needs-review'] for x in relevant])+kb.link(page,root/'catalog/messages.md','Messages')+' · '+kb.link(page,root/'catalog/participants.md','Shared participants')+' · '+kb.link(page,root/'catalog/flows.md','Flows')+' · '+kb.link(page,root/'catalog/README.md','Entry guide')+'\n')
 print(json.dumps(summary))

def query(root,kind=None,text=None,limit=10):
 limit=max(1,min(int(limit),100));db=sqlite3.connect(root/'catalog/search.sqlite')
 filters=[];args=[]
 if kind:filters.append('kind=?');args.append(kind)
 if text:
  tokens=re.findall(r'[\w]+',text)
  expression=' AND '.join('"'+t.replace('"','')+'"' for t in tokens)
  filters.append('pages MATCH ?');args.append(expression)
 sql='SELECT metadata FROM pages'+(' WHERE '+' AND '.join(filters) if filters else '')+' ORDER BY path LIMIT ?';args.append(limit)
 try:result=[bounded_record(json.loads(x[0])) for x in db.execute(sql,args)]
 finally:db.close()
 return {'query':text,'limit':limit,'records':result,'limitations':['Results are bounded; a missing result does not establish absence of a concept. Review status and source limitations remain applicable.']}

def bounded_record(record):
 truncated={}
 for key,value in list(record.items()):
  if isinstance(value,list) and len(value)>8:
   record[key]=value[:8];truncated[key]={'returned':8,'total':len(value)}
 if truncated:record['truncated_metadata']=truncated;record['full_metadata_location']=record['path']
 return record

def lookup(root,identifier,limit=10):
 mm=json.loads((root/'catalog/messages.json').read_text(encoding='utf-8'))['records']
 return {'identifier':identifier,'records':[bounded_record(m) for m in mm if m.get('message_id')==identifier or m.get('message_family')==identifier][:min(max(limit,1),100)],'limitations':['Family lookup preserves every supplied exact definition; it does not compare versions.']}

def roles(root,identifier,limit=10):
 data=json.loads((root/'catalog/message-roles.json').read_text(encoding='utf-8'))
 selected=[r for r in data['records'] if r.get('message_id')==identifier or r.get('message_family')==identifier][:min(max(limit,1),100)]
 results=[]
 for r in selected:
  result={k:v for k,v in r.items() if k in ['message_id','message_family','namespace','path','status','source_provenance','source_locations','participants','participant_ids','limitations','review_items','directions','actions']}
  directions=r.get('directions',[])
  result['current_message_directions']=[d for d in directions if d.get('message_target') in ['current-message','current-message-scope-name-variant']]
  result['qualified_current_message_directions']=[d for d in directions if str(d.get('message_target','')).startswith('current-message-') and d.get('message_target')!='current-message-scope-name-variant']
  result['other_direction_claims_count']=len(directions)-len(result['current_message_directions'])-len(result['qualified_current_message_directions'])
  results.append(bounded_record(result))
 # Documentation-only definitions have maintained semantic references but no
 # exact Part2 Functionality extraction. Return their real evidence destination.
 mids={r['message_id'] for r in selected};sources={s['source_id']:s for s in kb.sources(root)}
 for r in json.loads((root/'catalog/messages.json').read_text(encoding='utf-8'))['records']:
  if r.get('schema_status')!='not-supplied' or r['message_id'] in mids or not (r['message_id']==identifier or r.get('message_family')==identifier):continue
  result={k:r[k] for k in ['message_id','message_family','namespace','path','source_locations','participant_ids','flow_ids','limitations'] if k in r};result.update(status='documentation-only-business-evidence',schema_status='not-supplied',documentation_status=r.get('documentation_status'),source_provenance=[{'source_id':sid,'sha256':sources[sid]['sha256'],'occurrences':sources[sid]['occurrences']} for sid in r.get('source_ids',[]) if sid in sources],current_message_directions=[],directions_available_at=r['path']);result['limitations']=result.get('limitations',[])+['No exact Part2 Functionality role extraction exists. Read the linked canonical source-example evidence and its flow references for the documented directions.'];results.append(bounded_record(result))
 results=results[:min(max(limit,1),100)]
 return {'identifier':identifier,'limit':min(max(limit,1),100),'records':results,'limitations':['Only explicitly scoped current-message clauses establish a message direction; related/anaphoric claims retain their original labels and conditions.','Participant names are contextual roles, not fixed institutional identities. Open the linked role page for complete evidence and uncapped arrays.']}

def template_scan_text(text):
 # Mermaid JSON configuration ends in adjacent structural braces. Preserve any
 # actual placeholder inside a JSON string instead of treating it as syntax.
 def config(match):
  try:value=json.loads(match.group(1))
  except (ValueError,TypeError):return match.group(0)
  def has_token(value):
   if isinstance(value,str):return '{{' in value or '}}' in value
   if isinstance(value,dict):return any(has_token(k) or has_token(v) for k,v in value.items())
   if isinstance(value,list):return any(has_token(v) for v in value)
   return False
  return match.group(0) if has_token(value) else ''
 return re.sub(r'%%\{init:\s*(\{.*?\})\s*\}%%',config,text,flags=re.S)

def validate(root,checksums=False):
 ss=kb.sources(root);issues=[];checked=collections.Counter();byid=collections.defaultdict(list);reference_digest=hashlib.sha256();identity_paths=collections.defaultdict(list);actual_index_metadata={};link_exists={}
 if checksums:
  for s in ss:
   for o in s['occurrences']:
    if o.get('availability','current')!='current':checked['historical_source_occurrences']+=1;continue
    try:
     data=kb.read_source(root,{'occurrences':[o]});sha=hashlib.sha256(data).hexdigest();checked['source_occurrences']+=1
     if sha!=s['sha256']:issues.append({'kind':'changed-source','source_id':s['source_id'],'occurrence':o})
    except Exception as exc:issues.append({'kind':'unreadable-source','source_id':s['source_id'],'error':str(exc)})
  actual={p.relative_to(root).as_posix() for p in (root/'raw-input').rglob('*') if p.is_file() and p.name.lower()!='readme.md'}
  registered={o['path'] for s in ss for o in s['occurrences']}
  for p in actual-registered:issues.append({'kind':'unregistered-source','path':p})
  import refresh
  scan=refresh.scan(root)
  registered_members={(o['path'],o.get('archive_member'),s['sha256']) for s in ss for o in s.get('occurrences',[]) if o.get('availability','current')=='current'}
  for candidate in scan['candidates']:
   for occurrence in candidate['occurrences']:
    if occurrence.get('archive_member') and (occurrence['path'],occurrence['archive_member'],candidate['sha256']) not in registered_members:
     issues.append({'kind':'unregistered-archive-member','path':occurrence['path'],'member':occurrence['archive_member']})
  issues.extend({'kind':'inventory-scan-error',**item} for item in scan['errors'])
 for r in records(root):
  p=root/r['path'];text=p.read_text(encoding='utf-8');checked['reference_pages']+=1
  reference_digest.update(r['path'].encode('utf-8')+b'\0'+text.encode('utf-8')+b'\0')
  actual_index_metadata[r['path']]={k:r.get(k) for k in ['document_kind','review_status','source_ids','message_id','namespace','participant_id','flow_id']}
  if r.get('document_kind') in ['participant','participant-reference','shared-participant'] and r.get('participant_id'):identity_paths[('participant_id',r['participant_id'])].append(r['path'])
  if r.get('document_kind') in ['flow','business-flow','flow-reference'] and r.get('flow_id'):identity_paths[('flow_id',r['flow_id'])].append(r['path'])
  scan=template_scan_text(text)
  if '{{' in scan or '}}' in scan:issues.append({'kind':'placeholder','path':r['path']})
  if r.get('document_kind')=='message-index':byid[(r.get('message_id'),r.get('namespace'))].append(r['path'])
  if r.get('review_status') not in ['draft','needs-review','reviewed']:issues.append({'kind':'invalid-status','path':r['path']})
  prose=re.sub(r'```.*?```','',text,flags=re.S)
  prose=re.sub(r'`[^`\n]*`','',prose)
  for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)',prose):
   value=next(x for x in target if x);value=value.split('#')[0].split(' "')[0].strip('<>')
   if not value or re.match(r'[a-z]+:',value,re.I):continue
   key=str(p.parent/unquote(value))
   if key not in link_exists:link_exists[key]=Path(key).resolve().exists()
   if not link_exists[key]:issues.append({'kind':'broken-link','path':r['path'],'target':value})
   checked['relative_links']+=1
  if checked['reference_pages']%10000==0:kb.dump(root/'work/validation-progress.json',{'stage':'reference-pages','checks':dict(checked),'errors_so_far':len(issues)})
 for k,v in byid.items():
  if len(v)>1:issues.append({'kind':'duplicate-canonical','message':k,'paths':v})
 for k,v in identity_paths.items():
  if len(v)>1:issues.append({'kind':'duplicate-reference-identity','identity':k,'paths':v})
 for name in ['messages','participants','flows','diagrams','concepts','message-sets']:
  index_path=root/'catalog'/(name+'.json')
  if not index_path.exists():issues.append({'kind':'missing-catalog','index':name});continue
  index=json.loads(index_path.read_text(encoding='utf-8'))['records'];seen=set()
  for item in index:
   path=item['path'];checked['catalog_records']+=1
   if path in seen:issues.append({'kind':'duplicate-catalog-path','index':name,'path':path})
   seen.add(path);actual=actual_index_metadata.get(path)
   if actual is None:issues.append({'kind':'catalog-reference-missing','index':name,'path':path});continue
   for key in ['review_status','source_ids','message_id','namespace','participant_id','flow_id']:
    if key in item and actual.get(key)!=item[key]:issues.append({'kind':'catalog-metadata-mismatch','index':name,'path':path,'field':key})
  indexed_kinds={'messages':['message-index'],'participants':['participant','participant-reference','shared-participant'],'flows':['flow','business-flow','flow-reference'],'diagrams':['diagram'],'concepts':['schema-type','concept','business-concept']}
  if name in indexed_kinds:
   expected={path for path,meta in actual_index_metadata.items() if meta['document_kind'] in indexed_kinds[name]}
   for path in sorted(expected-seen):issues.append({'kind':'catalog-reference-omitted','index':name,'path':path})
   for path in sorted(seen-expected):issues.append({'kind':'catalog-kind-mismatch','index':name,'path':path})
 schema_checks=[]
 schema_paths=list(root.glob('shared/reference/messages/*/schema-coverage.json'))+list(root.glob('domains/*/reference/messages/*/schema-coverage.json'))
 for p in schema_paths:
  c=json.loads(p.read_text(encoding='utf-8'));s=next(s for s in ss if s['source_id']==c['source_id'])
  from lxml import etree as E
  tree=E.fromstring(kb.read_source(root,s),E.XMLParser(resolve_entities=False,no_network=True))
  counts=dict(collections.Counter(E.QName(n).localname for n in tree.iter() if isinstance(n.tag,str)))
  if counts!=c['counts']:issues.append({'kind':'schema-count-mismatch','path':str(p)})
  from extract_schemas import path as schema_path
  original_by_path={schema_path(n):n for n in tree.iter() if isinstance(n.tag,str)}
  for comp in c['components']:
   page=root/comp['path'];txt=page.read_text(encoding='utf-8');match=re.search(r'```xml\n(.*?)\n```',txt,re.S)
   if not match:issues.append({'kind':'missing-schema-fragment','path':comp['path']});continue
   output=E.fromstring(match[1].encode('utf-8'),E.XMLParser(resolve_entities=False,no_network=True))
   original=original_by_path.get(comp['schema_path'])
   def signature(n):return (n.tag,dict(n.attrib),(n.text or '').strip(),[(signature(ch),(ch.tail or '').strip()) for ch in n if isinstance(ch.tag,str)])
   if original is None or signature(output)!=signature(original):issues.append({'kind':'schema-fragment-mismatch','path':comp['path']})
   checked['schema_fragments']+=1
  checked['schema_definitions']+=1
  if c['compile_result']!='pass':issues.append({'kind':'schema-compile-fail','message':c['message_id']})
 result={'date':kb.DATE,'checks':dict(checked),'source_fingerprints_sha256':hashlib.sha256(json.dumps({s['source_id']:s['sha256'] for s in ss},sort_keys=True).encode()).hexdigest(),'reference_text_sha256':reference_digest.hexdigest(),'errors':issues,'pass':not issues,'scope':'Mechanical identity, links, metadata and literal schema coverage only. This does not validate business interpretation, complete table/figure discovery or visual fidelity.'}
 kb.dump(root/'work/validation-progress.json',{'stage':'complete','checks':dict(checked),'errors':len(issues)})
 kb.dump(root/'tracking/validation.json',result);print(json.dumps({'checks':dict(checked),'errors':len(issues),'first_errors':issues[:20]}));return result
