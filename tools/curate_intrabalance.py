"""Publish source359 inspected diagrams and scoped, source-grounded reusable flows."""
import argparse,hashlib,json,re
from pathlib import Path
import kb
from intrabalance_diagram_data import DATA
SID='src-000359';DATE='2026-11-09'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def block(body,tag,text):return re.sub(r'\n<!-- '+tag+r'-START -->.*?<!-- '+tag+r'-END -->\n?','\n',body,flags=re.S).rstrip()+'\n\n<!-- '+tag+'-START -->\n'+text+'\n<!-- '+tag+'-END -->\n'
def main(root):
 src=next(x for x in kb.sources(root) if x['source_id']==SID);base=root/src['set_path'];out=base/'diagrams/intrabalance';records=json.loads((root/'work/documents'/SID/'records.json').read_text(encoding='utf-8'));pars={int(p['paragraph_id'][1:]):p for p in records['paragraphs']};figs={int(f['figure_id'][4:]):f for f in records['figures']};inv=json.loads((root/'work/documents'/SID/'media-review-inventory.json').read_text(encoding='utf-8'));media={m['original']:m for m in inv['media']};tables={int(t['source_table_id'][1:]):t for t in records['tables']};defs=json.loads((root/'work/documents/src-000360/message-definitions.json').read_text(encoding='utf-8'));exact={d['message_id'][:8]:d for d in defs};proot=root/'shared/reference/participants';outputs=[]
 def pp(slug):return proot/f'participant-{SID}-{slug}.md'
 new={
 'csd-participant':('CSDParticipant','A FinancialInstitution-stereotyped actor associated from CashManagement in the source business-context use case. The picture does not supply an independent institutional definition.',156),
 'system-application':('SystemApplication','A System-stereotyped actor associated from CashManagement in the source business-context use case. No legal institution is inferred.',156),
 'payment-agent':('PaymentAgent','A FinancialInstitution-stereotyped actor associated from CashManagement in the source business-context use case. The source does not state that this label equals Payment Bank.',156),
 'servicing-party':('Servicing Party','The source transaction and query/report activity label for the party receiving cancellation/modification queries and sending reports or request status to the Instructing Party. Source label variants Servicing/Executing Party and Executing/Servicing Party are retained as separate records; no global equivalence is inferred.',258),
 'account-owner':('Account owner','Contextual role in T9/T10/T13/T16 receiving status/confirmation or requesting query, explicitly parenthesized Instructing Party there; T17/T18 instead parenthesize Receiving Party. This is a relationship role, not a particular institution.',159)
 }
 for slug,(label,definition,pnum) in new.items():
  path=pp(slug)
  if not path.exists():
   m={'template':False,'document_kind':'participant','review_status':'needs-review','participant_id':path.stem,'title':label,'source_labels':[label],'aliases':[],'source_ids':[SID],'source_editions':[src['source_edition']],'domain':'securities','message_sets':['t2s-intra-balance-movement'],'role_type':'source-scoped actor label; no broader equivalence asserted','source_locations':[{'source_id':SID,'paragraph_id':'P'+str(pnum),'heading_path':pars[pnum]['heading_path']}],'limitations':['Identifier schemes are not specified in the cited role evidence. Institutional examples and functional roles are not equated.'],'updated':DATE}
   kb.put(path,kb.front(m)+'# '+label+'\n\n'+definition+'\n\n'+kb.source_link(root,path,src)+'; '+SID+' P'+str(pnum)+'.\n\n## Responsibilities and relationships\n\nThe linked flows below retain the source-specific actions and counterparties. No identifier scheme or unprinted alias is inferred.\n')
 # Reuse exact artwork without falsely claiming the contextual canonical is reviewed.
 parent=root/'shared/reference/message-sets/t2s-administration/march-2024/diagrams/administration/fig-0001.md';pm,pb=kb.metadata(parent);code=parent.with_suffix('.mmd').read_text(encoding='utf-8')
 DATA[1]={'title':'Hierarchical roles and access-rights context','page':10,'start':140,'end':148,'tables':[5,6,7],'roles':['t2s-operator','central-securities-depositories-csd','national-central-bank-ncb','payment-bank','central-counterparty'],'code':code,'notes':['Source P140 says Collateral Reporting despite this IntraBalanceMovement publication (issue-000047).','The artwork is byte-identical to source343 figure1; its existing source reconstruction is reused. The source343 canonical context remains needs-review under issue-000039. Disposition is canonical-artwork-reused; contextual-review-open, not deduplicated-to-reviewed.','P143 defines the grey area as dedicated cash-account static-data setup and explains that an NCB acting as a CSD exists in both roles. Institutions are not collapsed into their contextual role.','Mermaid flowchart boxes preserve hierarchy and account labels; original grey shading, levels 1–4 and repeated CSD B occurrences remain explicit in the source artwork.']}
 for num,d in sorted(DATA.items()):
  f=figs[num];page=out/f'fig-{num:04d}.md';mmd=page.with_suffix('.mmd');kind='sequenceDiagram' if num>=17 else ('usecase-beta' if num==2 else 'flowchart');word=root/'domains/securities/assets'/SID/'word-page-context'/f'page-{d["page"]:04d}.png';assets=[root/i['asset'] for i in f['images']];original=word if num>=17 else assets[0];notes=list(d['notes'])
  if num>=17:notes+=['Source-native text boxes and connector objects form a complete figure. The retained Word page is the complete composite; the small WMF bank pictograms are not treated as standalone diagrams.','Solid/dashed connectors and their directions are preserved. Source colours are recorded per message step below; colours distinguish pictured context without asserting extra protocol semantics.','Native Mermaid boxes replace institutional pictograms; labels define the functional participants and do not bind a role to one institution.']
  elif num>=10:notes+=['Native Mermaid flowchart subgraphs retain source swimlane responsibility. Source start/end glyphs, labelled decisions and bars remain explicit. T19 defines bars as parallel actions; the original uses some bars at converging alternative paths, so no extra execution semantics are inferred.']
  pids={pp(slug).stem for slug in d['roles']}
  if d['tables'] and any(t in d['tables'] for t in [9,10,13,16,17,18]):pids.add(pp('account-owner').stem)
  if num==18:pids.add(pp('instructing-party').stem)
  # Exact message binding is separate from the unversioned artwork.
  families=set(re.findall(r'camt\.\d{3}',f.get('shape_text','')+'\n'+d['code']))
  if num in (10,11):families|={'camt.066','camt.067','camt.068'}
  if num==12:families|={'camt.072','camt.073','camt.074','camt.075'}
  if num in (13,14):families|={'camt.080','camt.081','camt.082','camt.083'}
  if num==15:families|={'camt.084','camt.085'}
  if num==16:families|={'camt.078','camt.079'}
  bindings=[exact[x] for x in sorted(families) if x in exact];mids=[x['message_id'] for x in bindings]
  flows=list((base/'flows').glob(f'flow-{SID}-p{d["start"]}-*.md'));flow=flows[0] if flows else None
  loc={'source_id':SID,'locator':f['locator'],'heading_path':f['heading_path'],'xml_path':f['xml_path'],'figure_id':f['figure_id'],'word_file_page':d['page']}
  m={'template':False,'document_kind':'diagram','review_status':'needs-review','manual_curated':True,'title':d['title'],'domain':'securities','source_ids':[SID],'source_editions':[src['source_edition']],'message_sets':['t2s-intra-balance-movement'],'diagram_id':f['figure_id'],'diagram_kind':kind,'content_origin':'source-reconstruction','source_locations':[loc],'original_asset':original.relative_to(root).as_posix(),'original_components':[p.relative_to(root).as_posix() for p in assets],'participant_ids':sorted(pids),'flow_ids':[flow.stem] if flow else [],'message_ids':mids,'render_status':'not-run','visual_review':'not-run','word_composite_visual_review':'not-run','limitations':notes,'updated':DATE}
  if num==1:m.update(canonical_artwork=parent.relative_to(root).as_posix(),disposition='canonical-artwork-reused; contextual-review-open')
  body='# '+d['title']+'\n\n'+kb.source_link(root,page,src)+'; '+f['locator']+'; '+' / '.join(f['heading_path'])+'; Word-derived file page '+str(d['page'])+'.\n\n'+kb.link(page,original,'Complete source figure / rendered composite')+' · '+kb.link(page,word,'Complete Word-page context')+'\n\n'
  if num==1:body+=kb.link(page,parent,'Canonical reused artwork and its open contextual review')+'\n\n'
  body+='## Mermaid reconstruction\n\n```mermaid\n'+d['code']+'```\n\n## Actors, entities and relationships\n\n'
  if num>=17:
   body+=kb.table(['Step','Sender','Receiver','Complete source label','Line','Source colour'],[[i,d['actor_labels'][a],d['actor_labels'][b],label,'dashed' if dashed else 'solid',color] for i,(a,b,label,dashed,color) in enumerate(d['steps'],1)])
  else:
   # Literal edge listing supplies a small searchable relationship index alongside the artwork.
   body+='The reconstruction above retains the source-labelled entities, directed or undirected connectors, decision labels and lane boundaries. Each Mermaid line is the maintained relationship transcription; source activity-table definitions and responsibilities are linked below.\n\n'
  body+='\n'.join('- '+kb.link(page,proot/(pid+'.md'),kb.metadata(proot/(pid+'.md'))[0].get('title',pid)) for pid in sorted(pids))+'\n\n'
  if flow:body+=kb.link(page,flow,'Reusable flow: trigger, conditions, responsibilities and narrative')+'\n\n'
  body+='## Source tables and limitations\n\n'+'\n'.join('- '+kb.link(page,base/'documents'/SID/'tables'/f'tbl-{t:04d}.md',f'T{t}: '+' / '.join(tables[t]['heading_path'])) for t in d['tables'])+'\n\n'+'\n'.join('- '+x for x in notes)+'\n\n'+kb.link(page,root/'tracking/issues.md','Source ambiguities: issue-000047')+'\n\n## Review evidence\n\nTranscribed after direct original and complete native-composite inspection. Parsing, final rendered comparison and whole-page review are recorded separately, not inferred from transcription.\n'
  kb.put(mmd,d['code']);kb.put(page,kb.front(m)+body)
  evidence=base/'documents'/SID/'diagrams'/f'fig-{num:04d}.md'
  if evidence.exists():
   em,eb=kb.metadata(evidence);em.update(canonical_diagram=page.relative_to(root).as_posix(),disposition='canonical-reconstruction-created-needs-review');kb.put(evidence,kb.front(em)+block(eb,'INTRABALANCE-CANONICAL',kb.link(evidence,page,'Canonical complete reconstruction and review evidence')))
  if flow:
   fm,fb=kb.metadata(flow);fm.update(document_kind='business-flow',manual_curated=True,participant_ids=sorted(set(fm.get('participant_ids',[]))|pids),message_ids=sorted(set(fm.get('message_ids',[]))|set(mids)),diagram_paths=sorted(set(fm.get('diagram_paths',[]))|{page.relative_to(root).as_posix()}))
   text='## Curated scenario and source responsibilities\n\n'+kb.link(flow,page,d['title']+' — source diagram and directions')+'\n\n'
   if num>=17:text+=kb.table(['Step','Sender / transmitting participant','Receiver','Literal message label'],[[i,d['actor_labels'][a],d['actor_labels'][b],label] for i,(a,b,label,_,_) in enumerate(d['steps'],1)])+'\n'
   narrative=[p for n,p in pars.items() if d['start']<=n<=d['end'] and p['text'].strip() and n!=int(re.search(r'P(\d+)',f['locator']).group(1))]
   text+='### Narrative conditions, actions and outcomes\n\n'+'\n\n'.join('**'+SID+' '+p['paragraph_id']+'** — '+p['text'] for p in narrative)+'\n\n'
   text+='### Source-defined triggers, preconditions, postconditions and activity responsibilities\n\n'
   for t in d['tables']:
    tr=tables[t];tp=base/'documents'/SID/'tables'/f'tbl-{t:04d}.md';text+=kb.link(flow,tp,'Complete T'+str(t)+' with exact source rows')+'\n\n'
    if 8<=t<=18:text+=kb.table(['Source item','Source definition'],tr['rows'][1:])+'\n'
    elif t>=20:text+=kb.table(['Source step','Description / conditions','Initiator / responsible role'],tr['rows'][1:])+'\n'
   text+='### Scoped participants\n\n'+'\n'.join('- '+kb.link(flow,proot/(pid+'.md'),kb.metadata(proot/(pid+'.md'))[0].get('title',pid)) for pid in sorted(pids))+'\n\n### Exact supplied message definitions\n\n'+kb.table(['Exact definition','Binding evidence'],[[kb.link(flow,root/'domains/securities/reference/messages'/x['message_id']/'index.md',x['message_id']),f'src-000360 file page {x["start_page"]}: '+x['title']] for x in bindings])+'\nPart 1 uses family identifiers or unversioned names. These exact references come separately from supplied Part 2 headings. Where no exact message is printed or otherwise established, none is invented.\n\n### Alternatives and source limitations\n\n'+'\n'.join('- '+x for x in notes)+'\n\n'+kb.link(flow,root/'tracking/issues.md','issue-000047 — unresolved source wording and rendered-label differences')+'\n'
   kb.put(flow,kb.front(fm)+block(fb,'INTRABALANCE-FIG-'+str(num),text))
   for pid in pids:
    path=proot/(pid+'.md');pm,pb=kb.metadata(path);pm['flow_ids']=sorted(set(pm.get('flow_ids',[]))|{flow.stem});kb.put(path,kb.front(pm)+block(pb,'INTRABALANCE-FIG-'+str(num),kb.link(path,flow,d['title'])+' · '+kb.link(path,page,'Source diagram and directions')))
   for x in bindings:
    path=root/'domains/securities/reference/messages'/x['message_id']/'index.md';mm,mb=kb.metadata(path);kb.put(path,kb.front(mm)+block(mb,'INTRABALANCE-FIG-'+str(num),kb.link(path,flow,d['title'])+' — source359 roles, conditions and message directions.'))
  outputs.append({'source_figure_id':f['figure_id'],'path':page.relative_to(root).as_posix(),'mermaid':mmd.relative_to(root).as_posix(),'mermaid_sha256':sha(mmd),'original':original.relative_to(root).as_posix(),'original_sha256':sha(original),'word_file_page':d['page'],'word_page':word.relative_to(root).as_posix(),'word_page_sha256':sha(word),'flow_path':flow.relative_to(root).as_posix() if flow else None,'notes':notes})
 ix=out/'index.md';kb.put(ix,kb.front({'template':False,'document_kind':'diagram-index','review_status':'needs-review','source_ids':[SID],'domain':'securities'})+'# Intra-balance movement diagrams\n\n'+kb.table(['Figure','Source page','Reference'],[[r['source_figure_id'],r['word_file_page'],kb.link(ix,root/r['path'],DATA[int(r['source_figure_id'][4:])]['title'])] for r in outputs])+'\nFigures6–9 are the four substantive notation-legend glyphs in T19, retained with their table definitions. They are not separate business scenarios.\n')
 kb.dump(root/'work/intrabalance-curation.json',{'source_id':SID,'source_sha256':src['sha256'],'date':DATE,'records':outputs})
 print(json.dumps({'diagrams':len(outputs),'flows':len({r['flow_path'] for r in outputs if r['flow_path']}),'new_scoped_participants':len(new)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);main(p.parse_args().root.resolve())
