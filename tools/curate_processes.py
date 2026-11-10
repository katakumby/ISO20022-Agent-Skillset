"""Build scoped participant and flow drafts from already extracted MDR Part 1 evidence.

Does not merge same-labelled roles across sources. Uses explicit role-definition tables,
role-to-participant matrices, activity initiator cells, source labels/headings and narrative.
Every generated statement links back to paragraph/table/figure evidence. Review stays pending.
"""
from __future__ import annotations
import argparse,json,re,collections,hashlib,shutil,datetime
from pathlib import Path
import kb

FAMILY=re.compile(r'\b[a-z]{4}\.\d{3}(?!\d)')
FULL=re.compile(r'\b[a-z]{4}\.\d{3}\.\d{3}\.\d{2,}')

def clean(s):return re.sub(r'\s+',' ',str(s or '')).strip()
def norm(s):return re.sub(r'[^a-z0-9]+','',clean(s).lower())
def is_flow_heading(path):
 return any(any(t in norm(x) for t in ['businessprocess','businessactivities','businesstransaction','messageflows','messagingflows']) for x in path)
def meta(s,kind,**extra):
 return dict(template=False,document_kind=kind,review_status='needs-review',domain=s['domain'],source_ids=[s['source_id']],source_editions=[s.get('source_edition')],message_sets=[s['set_slug']],**extra)
def evidence_link(root,s,page,rec):
 base=root/s['set_path']/'documents'/s['source_id']
 if rec['kind']=='table':return kb.link(page,base/'tables'/(rec['table_id']+'.md'),rec['source_table_id'])
 if rec['kind']=='figure':return kb.link(page,base/'diagrams'/(rec['figure_id']+'.md'),rec['figure_id'])
 return kb.source_link(root,page,s)+' '+rec['paragraph_id']+' ('+rec['xml_path']+')'
def loc(s,rec,row=None):
 return {'source_id':s['source_id'],'heading_path':rec.get('heading_path',[]),'locator':rec.get('xml_path','')+(f'/w:tr[{row}]' if row else ''),'paragraph_id':rec.get('paragraph_id'),'table_id':rec.get('source_table_id')}
def put(root,path,text):
 if path.exists():
  oldmeta,oldbody=kb.metadata(path)
  if oldmeta.get('manual_curated') or oldmeta.get('review_status')=='reviewed':return
  if path.read_text(encoding='utf-8-sig')==text:return
  hist=root/'tracking/history/job-000001'/('process-refresh-'+datetime.datetime.now().strftime('%Y%m%dT%H%M%S'))/path.relative_to(root)
  hist.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(path,hist)
 kb.put(path,text)

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--source',action='append');a=ap.parse_args();root=a.root.resolve();all_sources=kb.sources(root);catalog=[];processed=[]
 for s in all_sources:
  sid=s['source_id'];input=root/'work/documents'/sid/'records.json'
  if s['format']!='docx' or sid=='src-000196' or not input.exists() or a.source and sid not in a.source:continue
  processed.append(sid)
  d=json.loads(input.read_text(encoding='utf-8'));records=d['records'];roles={};last_label=None;defs=[];matrices=[];messages={};mapping_evidence={}
  def ensure(label,role_type='activity participant; classification not established'):
   key=norm(label)
   if not key:return None
   if key not in roles:
    slug=kb.slug(clean(label)) or hashlib.sha256(str(label).encode()).hexdigest()[:8]
    roles[key]={'participant_id':'participant-'+sid+'-'+slug,'label':clean(label),'source_labels':[label],'role_type':role_type,'definitions':[],'responsibilities':[],'relationships':[],'flows':[],'source_locations':[],'aliases':[]}
   elif label not in roles[key]['source_labels']:roles[key]['source_labels'].append(label)
   return roles[key]
  for rec in records:
   if rec['kind']=='paragraph':
    if norm(rec['text']) in ['participants','businessroles']:last_label='functional participant role' if norm(rec['text'])=='participants' else 'business role'
   if rec['kind']!='table' or not rec['rows']:continue
   rows=rec['rows'];hdr=[norm(x) for x in rows[0]]
   if any('messagedefinition'==x for x in hdr) and any('messageidentifier'==x for x in hdr):
    mi=next(i for i,x in enumerate(hdr) if x=='messageidentifier');ni=next(i for i,x in enumerate(hdr) if x=='messagedefinition')
    for ri,row in enumerate(rows[1:],2):
     if len(row)>max(mi,ni):
      name=norm(row[ni]);messages.setdefault(name,set()).update(FAMILY.findall(row[mi]));mapping_evidence.setdefault(name,[]).append(loc(s,rec,ri))
   if any('businessroles' in norm(x) and 'participants' in norm(x) for x in rec['heading_path']) and any('definition' in [norm(v) for v in row] and ('description' in [norm(v) for v in row] or 'name' in [norm(v) for v in row]) for row in rows[:3]):
    hix=next(i for i,row in enumerate(rows[:3]) if 'definition' in [norm(v) for v in row] and ('description' in [norm(v) for v in row] or 'name' in [norm(v) for v in row]));hd=[norm(x) for x in rows[hix]];li=hd.index('description') if 'description' in hd else hd.index('name');di=hd.index('definition');classify=last_label
    for ri,row in enumerate(rows[hix+1:],hix+2):
     if len(row)==1 and norm(row[0]) in ['participants','businessroles']:
      classify='functional participant role' if norm(row[0])=='participants' else 'business role';continue
     if len(row)<=max(li,di) or not clean(row[li]):continue
     role=ensure(row[li],classify or 'source-defined role; classification not established');role['definitions'].append({'text':row[di],'source':rec,'row':ri});role['source_locations'].append(loc(s,rec,ri))
   elif any('businessrolesandparticipantstable' in norm(x) for x in rec['heading_path']) or 'matrixtable' in norm(' '.join(rows[0])):matrices.append(rec)
   if 'description' in norm(' '.join(rows[0])) and ('activities' in norm(' '.join(rows[0]))) and len(rows)>1 and len(rows[1])>1:
    for ci,label in enumerate(rows[1]):
     if not clean(label):continue
     role=ensure(label,'activity participant named in responsibility column')
     for ri,row in enumerate(rows[2:],3):
      if ci<len(row) and clean(row[ci]):role['responsibilities'].append({'step':'Source activity row '+str(ri),'description':row[ci],'source':rec,'row':ri,'column_label':label});role['source_locations'].append(loc(s,rec,ri))
   if 'step' in hdr and ('initiator' in hdr or 'responsibleparticipant' in hdr):
    who=hdr.index('initiator') if 'initiator' in hdr else hdr.index('responsibleparticipant');description=hdr.index('description') if 'description' in hdr else 1
    for ri,row in enumerate(rows[1:],2):
     if len(row)<=who or not clean(row[who]):continue
     label=clean(row[who]);role=ensure(label)
     role['responsibilities'].append({'step':row[0],'description':row[description] if len(row)>description else '', 'source':rec,'row':ri,'column_label':rows[0][who]});role['source_locations'].append(loc(s,rec,ri))
  # Exact MDR2 definition headings can disambiguate erroneous message-name rows without changing source evidence.
  pdf_names={}
  for ps in all_sources:
   mf=root/'work/documents'/ps['source_id']/'message-definitions.json'
   if ps['format']!='pdf' or ps['set_slug']!=s['set_slug'] or not mf.exists():continue
   for definition in json.loads(mf.read_text(encoding='utf-8')):
    name=norm(re.sub(r'V[0-9]+$','',definition['title'].split(' ',2)[-1]))
    pdf_names.setdefault(name,set()).add(definition['message_id'][:8]);mapping_evidence.setdefault(name,[]).append({'source_id':ps['source_id'],'locator':'file page '+str(definition['start_page'])+'; '+definition['title']})
  for name,families in pdf_names.items():messages[name]=families
  # Explicit X marks in role-to-functional-participant matrices; no institution equivalence inference.
  for t in matrices:
   hix=1 if len(t['rows'][0])==1 and len(t['rows'])>1 else 0;headers=t['rows'][hix]
   for ri,row in enumerate(t['rows'][hix+1:],hix+2):
    if not row:continue
    role=roles.get(norm(row[0]))
    if not role:role=ensure(row[0],'business role (matrix label; definition not extracted)')
    for ci,value in enumerate(row[1:],1):
     if clean(value).lower()!='x' or ci>=len(headers):continue
     label=re.sub(r'^\s*Participant\s*','',headers[ci],flags=re.I);part=roles.get(norm(label)) or ensure(label,'functional participant role (matrix label; definition not extracted)')
     relation={'target':part['participant_id'],'target_label':part['label'],'relation':'Can play the functional participant role in this source context','source':t,'row':ri,'column':ci+1}
     role['relationships'].append(relation)
     part['relationships'].append({'target':role['participant_id'],'target_label':role['label'],'relation':'Business role listed for this functional participant','source':t,'row':ri,'column':ci+1})
  # Source-delimited segments preserve titles, optional paths, and surrounding narrative.
  segments=[];cur=None
  for rec in records:
   eligible=is_flow_heading(rec.get('heading_path',[]))
   if not eligible:cur=None;continue
   boundary=rec['kind']=='paragraph' and clean(rec['text']) and (rec.get('heading_level') is not None or 'block label' in rec.get('style','').lower())
   if cur is None or boundary:
    title=clean(rec['text']) if rec['kind']=='paragraph' and rec.get('text') else clean(rec['heading_path'][-1])
    cur={'title':title,'heading_path':rec.get('heading_path',[]),'records':[],'start':rec.get('paragraph_id') or rec.get('source_table_id') or rec.get('figure_id')};segments.append(cur)
   cur['records'].append(rec)
  flows=[]
  for seg in segments:
   meaningful=[r for r in seg['records'] if r['kind']!='paragraph' or (clean(r['text']) and clean(r['text'])!=seg['title'])]
   if not meaningful:continue
   # Legend-only sections describe notation, not a business flow.
   if all(r['kind']=='table' and r['rows'] and norm(r['rows'][0][0])=='symbol' for r in meaningful):continue
   content='\n'.join(r.get('text','') if r['kind']=='paragraph' else '\n'.join(' '.join(row) for row in r['rows']) if r['kind']=='table' else r.get('shape_text','') for r in seg['records'])
   fields={};activities=[]
   for r in seg['records']:
    if r['kind']!='table' or not r['rows']:continue
    hdr=[norm(x) for x in r['rows'][0]]
    if len(hdr)>1 and hdr[0]=='item':
     for ri,row in enumerate(r['rows'][1:],2):
      if len(row)>1:fields.setdefault(clean(row[0]),[]).append({'text':row[1],'source':r,'row':ri})
    if 'step' in hdr or 'activities' in norm(' '.join(r['rows'][0])):activities.append(r)
   umbrella={'businessprocessdescription','businessprocessdiagram','descriptionofbusinessactivities','businessactivities','businesstransactions','businesstransaction','outofscope','inscope','scope','legend','narrative','examples','messageflows','messagingflows','definition','participants','preconditions','postconditions'}
   kind='business-flow' if (fields or activities) and norm(seg['title']) not in umbrella else 'source-process-section'
   present=[]
   normalized=norm(content)
   spaced=re.sub(r'[^a-z0-9]+',' ',re.sub(r'([a-z])([A-Z])',r'\1 \2',content).lower())
   spans=[]
   for role in roles.values():
    label=re.sub(r'[^a-z0-9]+',' ',role['label'].lower()).strip()
    if not label:continue
    for match in re.finditer(r'(?<![a-z0-9])'+re.escape(label)+r'(?![a-z0-9])',spaced):spans.append((match.start(),match.end(),role))
   accepted=[]
   for start,end,role in sorted(spans,key=lambda x:-(x[1]-x[0])):
    if any(start>=a and end<=b for a,b in accepted):continue
    accepted.append((start,end))
    if role not in present:present.append(role)
   full=sorted(set(FULL.findall(content)));families=set(FAMILY.findall(content))
   used_mappings=[]
   for name,ids in messages.items():
    if name and name in normalized and len(ids)==1:
     families.update(ids);used_mappings.extend(mapping_evidence.get(name,[]))
   flowid='flow-'+sid+'-'+kb.slug(seg['start'])+'-'+kb.slug(seg['title'])[:70];page=root/s['set_path']/'flows'/(flowid+'.md')
   for role in present:role['flows'].append({'flow_id':flowid,'title':seg['title'],'path':page.relative_to(root).as_posix(),'document_kind':kind,'mention_basis':'Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence.'})
   limitations=['Source-delimited draft; visual diagram reconciliation and cross-section flow consolidation remain pending.','Message family mentions do not identify an exact supplied schema version unless the full identifier is stated.','Participants listed from narrative mentions are not automatically senders, receivers, or responsible actors.']
   fm=meta(s,kind,flow_id=flowid,title=seg['title'],source_locations=[loc(s,r) for r in seg['records'] if r['kind'] in ['paragraph','table']],participants=[r['participant_id'] for r in present],message_mapping_evidence=used_mappings,message_ids=full,message_families=sorted(families),search_terms=[seg['title']]+[r['label'] for r in present]+sorted(families),limitations=limitations)
   text=kb.front(fm)+'# '+seg['title']+'\n\nSource context: '+s['set_title']+'. This reference preserves the source-defined segment and its evidence.\n\n'
   if fields:
    text+='## Purpose, trigger and conditions\n\n'
    for key,vals in fields.items():
     text+='### '+key+'\n\n'
     for val in vals:text+=val['text']+'\n\nEvidence: '+evidence_link(root,s,page,val['source'])+f", source row {val['row']}.\n\n"
   else:text+='Purpose, trigger, preconditions and postconditions are not separately established in this extracted segment. The narrative and linked process tables preserve the available evidence.\n\n'
   text+='## Participants\n\n'
   if present:text+=kb.table(['Source role','Canonical scoped record','Evidence interpretation'],[[r['label'],kb.link(page,root/'shared/reference/participants'/(r['participant_id']+'.md'),'Participant'),'Mentioned in this segment; use the activity/narrative evidence for actions and message direction'] for r in present])
   else:text+='No canonical role label was automatically matched in this segment. Diagram-only or differently worded participants still require review.\n\n'
   text+='## Ordered activities and source narrative\n\n'
   for rec in seg['records']:
    if rec['kind']=='paragraph' and clean(rec['text']) and clean(rec['text'])!=seg['title']:text+='**'+rec['paragraph_id']+'** '+rec['text']+'\n\n'
    elif rec['kind']=='table':
     text+='Source table '+evidence_link(root,s,page,rec)+'.\n\n'
     if rec in activities:
      maxcol=max(len(r) for r in rec['rows']);text+=kb.table([f'Source column {i+1}' for i in range(maxcol)], [r+['']*(maxcol-len(r)) for r in rec['rows']])
    elif rec['kind']=='figure':text+='Source diagram evidence: '+evidence_link(root,s,page,rec)+'. Mermaid reconstruction and visual review are pending.\n\n'
   text+='## Messages and alternative paths\n\n'
   if families:text+='Source-supported message family mentions: '+', '.join('`'+x+'`' for x in sorted(families))+'. Full versions are retained only when explicitly present: '+(', '.join('`'+x+'`' for x in full) or 'none established in this segment')+'.\n\n'
   text+='Optional, failure, cancellation, reversal and decision paths remain as described in the source narrative and activity rows above. No additional path is inferred from message names or XML containment.\n\n## Limitations and provenance\n\n'+'\n'.join('- '+x for x in limitations)+'\n\nOriginal: '+kb.source_link(root,page,s)+'. Heading path: '+ ' / '.join(seg['heading_path'])+'.\n'
   put(root,page,text);flows.append({'flow_id':flowid,'title':seg['title'],'path':page.relative_to(root).as_posix(),'participants':[r['participant_id'] for r in present],'message_ids':full,'message_families':sorted(families),'document_kind':kind})
  for role in roles.values():
   page=root/'shared/reference/participants'/(role['participant_id']+'.md');limits=['Definition is scoped to this source and message-set context; same labels in other sources remain distinct.','Aliases and identifier schemes have not been established beyond explicit source labels.','Narrative-only participants not captured by definition/initiator tables require additional review.']
   role_flows=role['flows'];families=sorted(set(f for flow in flows if flow['flow_id'] in {x['flow_id'] for x in role_flows} for f in flow['message_families']));full=sorted(set(m for flow in flows if flow['flow_id'] in {x['flow_id'] for x in role_flows} for m in flow['message_ids']))
   text=kb.front(meta(s,'participant',participant_id=role['participant_id'],title=role['label'],source_labels=role['source_labels'],role_type=role['role_type'],aliases=role['aliases'],source_locations=role['source_locations'],flows=[x['flow_id'] for x in role_flows if x['document_kind']=='business-flow'],process_sections=[x['flow_id'] for x in role_flows if x['document_kind']!='business-flow'],message_ids=full,message_families=families,search_terms=[role['label']]+families,limitations=limits))+'# '+role['label']+'\n\nBusiness context: '+s['set_title']+'. Source classification: '+role['role_type']+'.\n\n## Definition\n\n'
   if role['definitions']:
    for val in role['definitions']:text+=val['text']+'\n\nEvidence: '+evidence_link(root,s,page,val['source'])+f", source row {val['row']}.\n\n"
   else:text+='The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.\n\n'
   text+='A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.\n\n## Responsibilities and actions\n\n'
   if role['responsibilities']:text+=kb.table(['Activity','Source description','Source responsibility column','Evidence'],[[x['step'],x['description'],x['column_label'],evidence_link(root,s,page,x['source'])+f" row {x['row']}" ] for x in role['responsibilities']])
   else:text+='Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.\n\n'
   text+='## Relationships\n\n'
   if role['relationships']:text+=kb.table(['Relationship','Related scoped record','Evidence'],[[x['relation'],kb.link(page,root/'shared/reference/participants'/(x['target']+'.md'),x['target_label']),evidence_link(root,s,page,x['source'])+f" row {x['row']}, column {x['column']}" ] for x in role['relationships']])
   else:text+='No role-matrix relationship was extracted for this label; this does not establish that none exists.\n\n'
   text+='## Flows, source process sections and messages\n\n'
   if role_flows:text+=kb.table(['Flow','Participation evidence'],[[kb.link(page,root/x['path'],x['title']),x['mention_basis']] for x in role_flows])
   else:text+='No flow segment has yet been matched to this role label.\n\n'
   text+='Message families found in these flows: '+(', '.join('`'+x+'`' for x in families) or 'not established')+'. Exact-version applicability requires the linked source locator.\n\n## Aliases, identification and limitations\n\nSource labels: '+', '.join('`'+clean(x)+'`' for x in role['source_labels'])+'. No external identifier scheme or alias equivalence has been inferred.\n\n'+'\n'.join('- '+x for x in limits)+'\n\nOriginal: '+kb.source_link(root,page,s)+'.\n';put(root,page,text)
  if not roles and not flows:continue
  idx=root/s['set_path']/'participants.md';put(root,idx,kb.front(meta(s,'participant-index'))+'# Participants in '+s['set_title']+'\n\n'+kb.table(['Scoped role','Classification','Definition source'],[[kb.link(idx,root/'shared/reference/participants'/(r['participant_id']+'.md'),r['label']),r['role_type'],sid] for r in roles.values()]))
  fidx=root/s['set_path']/'flows'/'index.md';put(root,fidx,kb.front(meta(s,'flow-index'))+'# Flows in '+s['set_title']+'\n\nThese source-delimited references retain process tables, activity order, narrative alternatives and original-figure links. They need semantic consolidation and visual review.\n\n'+kb.table(['Reference','Classification','Participants','Message families'],[[kb.link(fidx,root/f['path'],f['title']),f['document_kind'],len(f['participants']),', '.join(f['message_families'])] for f in flows]))
  result={'source_id':sid,'participants':len(roles),'flows':sum(f['document_kind']=='business-flow' for f in flows),'source_process_sections':sum(f['document_kind']=='source-process-section' for f in flows),'participant_index':idx.relative_to(root).as_posix(),'flow_index':fidx.relative_to(root).as_posix(),'status':'needs-review'};catalog.append(result);print(json.dumps(result),flush=True)
 previous=root/'catalog/process-extraction.json'
 if previous.exists():catalog=[x for x in json.loads(previous.read_text(encoding='utf-8')).get('records',[]) if x['source_id'] not in processed]+catalog
 kb.dump(previous,{'updated':'2026-11-08','records':sorted(catalog,key=lambda x:x['source_id']),'review_status':'needs-review'})
if __name__=='__main__':main()
