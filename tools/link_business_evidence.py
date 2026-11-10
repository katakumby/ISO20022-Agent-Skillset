"""Connect exact message definitions to supplied MDR functionality and detailed evidence.

No version substitution: only page-leading exact definition IDs are matched. This
helper preserves source semantics verbatim with locators; it does not infer roles.
"""
import argparse,collections,json,re
from pathlib import Path
import kb

def main(root,selection=None):
 ss=kb.sources(root);byid={s['source_id']:s for s in ss};schemas=kb.canonical_schemas(root,ss)[0]
 selected_ids={s['source_id'] for s in __import__('refresh').selection_sources(root,selection)} if selection else None
 selected_messages=__import__('refresh').selected_messages(root,selection) if selection else None
 definitions=collections.defaultdict(list)
 for p in (root/'work/documents').glob('*/message-definitions.json'):
  defs_for_source=json.loads(p.read_text(encoding='utf-8'))
  for d in defs_for_source:definitions[d['message_id']].append(d)
  if p.parent.name in byid and (selected_ids is None or p.parent.name in selected_ids):
   byid[p.parent.name]['defined_message_ids']=sorted(set(d['message_id'] for d in defs_for_source))
   byid[p.parent.name]['message_ids']=byid[p.parent.name]['defined_message_ids']
 pages_cache={};section_cache={};outputs=[]
 for mid,s in schemas.items():
  if selected_messages is not None and mid not in selected_messages:continue
  folder=root/kb.area(s['domain'])/'reference/messages'/mid
  if not (folder/'index.md').exists():continue
  page=folder/'mdr-evidence.md';defs=definitions.get(mid,[])
  if not defs:continue
  meta={'template':False,'document_kind':'message-mdr-evidence','review_status':'needs-review','domain':s['domain'],'message_id':mid,'message_family':'.'.join(mid.split('.')[:2]),'namespace':s['namespace'],'source_ids':sorted(set(d['source_id'] for d in defs)),'source_locations':[{'source_id':d['source_id'],'heading':d['title'],'file_pages':[d['start_page'],d['end_page']]} for d in defs],'limitations':['PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.','Separate publication statements are retained without version-comparison or silent conflict resolution.']}
  text=kb.front(meta)+'# '+mid+' MDR business evidence\n\nThe following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.\n\n'
  for d in defs:
   src=byid[d['source_id']];sid=src['source_id']
   if sid not in pages_cache:pages_cache[sid]=json.loads((root/'work/documents'/sid/'pages.json').read_text(encoding='utf-8'))['pages']
   pages=pages_cache[sid];section_no=re.match(r'(\d+)\s',d['title']);section_no=section_no.group(1) if section_no else None
   text+='## '+sid+' — '+d['title']+'\n\n'+kb.source_link(root,page,src)+'; file pp'+str(d['start_page'])+'–'+str(d['end_page'])+'; publication '+str(src.get('source_edition') or 'edition not established')+'. Printed labels are retained in the page text; these locators use one-based file pages.\n\n'
   text+='### Purpose, usage, participant roles and structure outline\n\n'
   extracted=[];started=False
   for p in pages[d['start_page']-1:min(d['end_page'],d['start_page']+12)]:
    tx=p['text']
    if not started:
     m=re.search(r'(?:\d+\.1\s+)?MessageDefinition\s+Functionality',tx,re.I)
     if m:tx=tx[m.end():];started=True
     else:continue
    stop=re.search((r'\b'+re.escape(section_no)+r'\.2\s') if section_no else r'\bMessageDefinition\s+Structure',tx)
    if stop:tx=tx[:stop.start()]
    # Keep text order and line breaks; page footers are evidence rather than removed by guessing.
    if tx.strip():extracted.append({'page':p['page'],'text':tx.strip()})
    if stop:break
   if extracted:
    for x in extracted:text+='**'+sid+', '+d['title']+', Functionality, file p'+str(x['page'])+'.**\n\n'+x['text']+'\n\n'
   else:text+='The automatic functionality boundary was not resolved. Consult the linked original and focused sections; no purpose or actor statement is inferred here.\n\n'
   sourcefolder=root/src['set_path']/'documents'/sid
   candidates=[]
   if sid not in section_cache:
    section_cache[sid]=[]
    for pp in (sourcefolder/'sections').glob('*.md'):
     mm,_=kb.metadata(pp);pg=mm.get('file_pages') or mm.get('pages') or []
     if not pg and mm.get('start_page'):pg=[mm['start_page'],mm.get('end_page',mm['start_page'])]
     if isinstance(pg,list) and pg:section_cache[sid].append((pp,pg,mm.get('heading_path',[])))
   for pp,pg,hp in section_cache[sid]:
    if max(pg)>=d['start_page'] and min(pg)<=d['end_page']:candidates.append([kb.link(page,pp,' / '.join(hp) or pp.stem),str(min(pg))+'–'+str(max(pg))])
   text+='### Detailed rules, components, tables and diagrams\n\n'+kb.link(page,sourcefolder/'index.md','Source section and coverage index')+' provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.\n\n'
   if candidates:text+=kb.table(['Focused section','File pages'],candidates)
  # Participant and flow links are scoped to actual same-collection evidence, not global label equivalence.
  related=[]
  for base in [root/'shared/reference/participants',root/s['set_path']/'flows']:
   if base.exists():
    for p in base.rglob('*.md'):
     m,_=kb.metadata(p)
     if m.get('document_kind') in ['participant','business-flow'] and (mid in m.get('message_ids',[]) or s['set_slug'] in m.get('message_sets',[])):related.append([kb.link(page,p,m.get('title') or m.get('participant_id') or m.get('flow_id') or p.stem),m.get('document_kind'),', '.join(m.get('source_ids',[]))])
  text+='## Scoped participants and related business flows\n\n'+(kb.table(['Reference','Kind','Source'],related) if related else 'Participant/flow curation for this exact message is not complete. Refer to the source functionality above and the message-set process references.\n\n')
  text+=kb.link(page,folder/'index.md','Canonical message')+' · '+kb.link(page,folder/'structure.md','Schema structure')+' · '+kb.link(page,root/'tracking/issues.md','Known gaps')+'\n'
  if selection and page.exists():
   pm,pt=kb.metadata(page)
   if pm.get('review_status')=='reviewed' or pm.get('manual_curated'):
    old_evidence=page.parent/'mdr-evidence-refresh.md'
    kb.put(old_evidence,text);page=old_evidence
   else:kb.put(page,text)
  else:kb.put(page,text)
  outputs.append({'message_id':mid,'path':page.relative_to(root).as_posix(),'definition_occurrences':len(defs)})
  # Append generated navigation without replacing curated message content.
  ip=folder/'index.md';im,it=kb.metadata(ip)
  im['source_ids']=sorted(set(im.get('source_ids',[])+[d['source_id'] for d in defs]))
  im['source_editions']=sorted({byid[sid]['source_edition'] for sid in im['source_ids'] if sid in byid and byid[sid].get('source_edition')})
  im['message_sets']=sorted(set(im.get('message_sets',[])+[byid[d['source_id']]['set_slug'] for d in defs]))
  im['mdr_definitions']=[{'source_id':d['source_id'],'file_pages':[d['start_page'],d['end_page']],'heading':d['title']} for d in defs]
  it=kb.front(im)+it.lstrip();it=re.sub(r'\n<!-- MDR-NAV-START -->.*?<!-- MDR-NAV-END -->\n?','\n',it,flags=re.S)
  nav='\n<!-- MDR-NAV-START -->\n## Supplied business evidence\n\n'+kb.link(ip,page,'Purpose, usage, actors and detailed MDR evidence')
  if (folder/'business.md').exists():nav+=' · '+kb.link(ip,folder/'business.md','Curated message context')
  nav+='\n<!-- MDR-NAV-END -->\n';kb.put(ip,it+nav)
 kb.dump((root/'tracking/refresh'/selection['job_id']/'message-business-evidence.json') if selection and selection.get('job_id') else root/'work/message-business-evidence.json',{'outputs':outputs,'schema_messages_without_exact_MDR_definition':[m for m in schemas if m not in definitions]})
 manifest=json.loads((root/'catalog/sources.json').read_text(encoding='utf-8'));manifest['sources']=ss;kb.dump(root/'catalog/sources.json',manifest)
 print(json.dumps({'message_business_references':len(outputs),'definition_occurrences':sum(x['definition_occurrences'] for x in outputs),'unmatched_schema_definitions':len([m for m in schemas if m not in definitions])}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--selection',type=Path);p.add_argument('--job');a=p.parse_args();root=a.root.resolve()
 selection=__import__('refresh').read_json(a.selection) if a.selection else None
 if a.job:kb.set_write_context(root,a.job)
 if selection:__import__('refresh').check_selection(root,selection,True)
 main(root,selection)
