"""Link three exact-image T2S occurrences after scoped component-context checks."""
from pathlib import Path
import json,sys,re,collections,hashlib
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'));import kb
from extract_workbooks import fm,write,relative
JOB='job-000001';rp=ROOT/'work/workbook-results.json';results=json.loads(rp.read_text('utf-8'));sources={s['source_id']:s for s in kb.sources(ROOT)}
def get(sid,fid):return next(d for r in results if r['source_id']==sid for d in r['diagrams'] if d['figure_id']==fid)
def lk(p,t,title):return '['+title+']('+relative(ROOT/p,ROOT/t)+')'
def decls(sid):
 w=json.loads((ROOT/'work/workbooks'/sid/'workbook.json').read_text('utf-8'));sh=next(x for x in w['sheets'] if x['name']=='FullBusinessModel');rows=collections.defaultdict(dict)
 for c in sh['cells']:
  m=re.match('([A-Z]+)([0-9]+)',c['cell']);rows[int(m[2])][m[1]]=c['value']
 return {r['A']:(i,r) for i,r in rows.items() if r.get('A') and not r.get('B')}
checks=[]
for a,af,b,bf in [('src-000016','fig-0004','src-000364','fig-0002'),('src-000016','fig-0002','src-000364','fig-0003'),('src-000198','fig-0005','src-000382','fig-0002')]:
 canonical=get(a,af);occ=get(b,bf);cp=Path(canonical['page']);p=Path(occ['page']);body=(ROOT/cp).read_text('utf-8');assert 'review_status: "reviewed"' in body
 assert canonical['sha256']==occ['sha256']==hashlib.sha256((ROOT/canonical['asset']).read_bytes()).hexdigest()==hashlib.sha256((ROOT/occ['asset']).read_bytes()).hexdigest()
 concepts=re.search(r'^concepts: (.*)$',body,re.M)
 if concepts:names=json.loads(concepts[1])
 else:names='SecuritiesTransfer Security CorporateActionEvent SecuritiesQuantity SecuritiesSettlement IntraPositionTransfer SecuritiesBalance SecuritiesAccount DigitalWallet'.split()
 ad=decls(a);bd=decls(b);context=[]
 for n in names:
  assert n in ad and n in bd
  assert [ad[n][1].get(k) for k in ['C','D']]==[bd[n][1].get(k) for k in ['C','D']]
  context.append({'component':n,'canonical_declaration_row':ad[n][0],'occurrence_declaration_row':bd[n][0],'parent_and_definition_exact_match':True})
 loc=occ['sheet']+'!'+occ['from_cell']+(':'+occ['to_cell'] if occ.get('to_cell') else '')+'; '+occ['drawing_part']+'; anchor '+str(occ['anchor_id']);s=sources[b]
 meta=fm(domain=s['domain'],document_kind='diagram-occurrence',review_status='reviewed',curated=True,source_ids=[b],source_editions=[s['source_edition']],source_locations=[loc],message_sets=[s['set_slug']],figure_id=bf,diagram_kind='class',content_origin='source-reconstruction',disposition='deduplicated',canonical_output=cp.as_posix(),render_status='passed',visual_review={'date':'2026-11-09','result':'pass','method':'Verified unchanged full-image SHA-256 equivalence to the visually reviewed canonical source figure and exact parent/definition matches for all '+str(len(names))+' visible conceptual components in each owning workbook.'},limitations=['Diagram equivalence does not equate message-set membership, publication edition, participant scope or message definitions.'])
 out=meta+'# '+occ['sheet']+' — exact source-figure occurrence\n\n'+kb.source_link(ROOT,ROOT/p,s)+'; '+b+', '+loc+'.\n\nThe complete source image is byte-identical to '+a+' '+af+' (SHA-256 '+occ['sha256']+'). '+lk(p,cp,'The reviewed canonical diagram')+' contains the Mermaid reconstruction, complete relationship explanation, original figure and actual parse/render/visual-comparison evidence. Its reconstruction is reused once.\n\n'+lk(p,Path(occ['asset']),'Original image in this archive member')+' · '+lk(p,Path('work/workbooks')/b/'workbook.json','Exact workbook/drawing provenance')+' · '+lk(p,Path(s['set_path'])/'participants.md','This message set’s participants')+' · '+lk(p,Path(s['set_path'])/'flows/index.md','This message set’s flows')+'\n\n## Context check\n\nAll '+str(len(names))+' source component declarations have exact parent-class and definition-text matches between the two supplied workbooks. This supports reuse of the unchanged figure; the publication and message-set boundaries remain separate. No participant or exact message definition is merged by this image equivalence.\n\n| Component | Canonical source declaration | This source declaration |\n| --- | --- | --- |\n'
 for c in context:out+='| '+c['component']+' | '+a+' FullBusinessModel!A'+str(c['canonical_declaration_row'])+':F'+str(c['canonical_declaration_row'])+' | '+b+' FullBusinessModel!A'+str(c['occurrence_declaration_row'])+':F'+str(c['occurrence_declaration_row'])+' |\n'
 out+='\nReview performed 2026-11-09. The canonical review date remains that recorded at the canonical page; no new rendering is claimed for this duplicate.\n';write(ROOT,ROOT/p,out,JOB)
 update=dict(disposition='deduplicated',review_status='reviewed',canonical_output=cp.as_posix(),render_status='passed',visual_review={'date':'2026-11-09','result':'pass','method':'Exact full-image hash and scoped component-declaration equivalence verified; reviewed canonical figure reused.'});occ.update(update)
 wp=ROOT/'work/workbooks'/b/'workbook.json';w=json.loads(wp.read_text('utf-8'))
 for sh in w['sheets']:
  for d in sh.get('drawings',[]):
   if d.get('figure_id')==bf:d.update(update)
 write(ROOT,wp,json.dumps(w,ensure_ascii=False,indent=2),JOB)
 heading='## Exact-image occurrence in '+b+' '+bf
 if heading not in body:write(ROOT,ROOT/cp,body+'\n'+heading+'\n\n'+lk(cp,p,s['set_title']+' — '+occ['sheet'])+' retains its archive-member provenance and message-set context. Full source-figure SHA-256 and all visible component parent/definition claims match; see its declaration-row comparison.\n',JOB)
 checks.append(dict(source_id=b,figure_id=bf,canonical_output=cp.as_posix(),sha256=occ['sha256'],date='2026-11-09',components=context,review_status='reviewed'))
write(ROOT,rp,json.dumps(results,ensure_ascii=False,indent=2),JOB);write(ROOT,ROOT/'work/workbook-model-deduplication.json',json.dumps(checks,ensure_ascii=False,indent=2),JOB);print(json.dumps({'deduplicated_occurrences':len(checks),'context_checked_components':sum(len(c['components']) for c in checks)}))
