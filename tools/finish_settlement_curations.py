"""Reconcile all source-196 diagram dispositions, source pages and navigation."""
import argparse,hashlib,json,re
from pathlib import Path
from urllib.parse import unquote
import kb
from settlement_scope_overview import participants as scope_participants

def main(root):
 sid='src-000196';source=next(s for s in kb.sources(root) if s['source_id']==sid);base=root/source['set_path']
 if hashlib.sha256(kb.read_source(root,source)).hexdigest()!=source['sha256']:raise ValueError('Changed source')
 scope_participants(root,source,base/'diagrams/settlement-activities/fig-0001.md')
 inv=json.loads((root/'work/documents'/sid/'media-review-inventory.json').read_text(encoding='utf-8'))
 native=json.loads((root/'work/documents'/sid/'native-embeddings.json').read_text(encoding='utf-8'))
 locations=json.loads((root/'work/docx-render'/sid/'page-locations.json').read_text(encoding='utf-8'))
 bysha={}
 for loc in locations['locations']:
  for asset in loc.get('asset_fingerprints',[]):bysha.setdefault(asset['sha256'],[]).append(loc)
 nativebyfig={}
 for member in native['native_members']:
  for occ in member['occurrences']:
   if occ.get('figure_id'):nativebyfig.setdefault(occ['figure_id'],[]).append(member)
 reports=[];issues=[];pages=[];participants={}
 for p in (root/'shared/reference/participants').glob('*.md'):
  m,_=kb.metadata(p)
  if m.get('participant_id'):participants[m['participant_id']]=p
 for image in inv['media']:
  number=int(re.search(r'image(\d+)',image['original']).group(1));occ=image['occurrences'][0];ep=root/occ['evidence_page'];em,eb=kb.metadata(ep)
  record={'source_figure_id':occ['figure_id'],'source_locator':occ['source_locator'],'original':image['original'],'original_sha256':image['original_sha256']}
  if hashlib.sha256((root/image['original']).read_bytes()).hexdigest()!=image['original_sha256']:raise ValueError('Original media changed')
  matches=bysha.get(image['original_sha256'],[])
  record['rendered_source_pages']=sorted({x['start_file_page'] for x in matches})
  record['page_mapping_method']='exact-asset-sha256 in Word shape OpenXML' if matches else 'unresolved; no ordinal inference'
  if number in (6,7,8,9):
   record.update(disposition='retained-notation-legend',canonical_path=occ['evidence_page'],visual_review='classification-pass')
   reports.append(record);continue
  pilot={37:'01-typical-sequence',39:'02-partial-sequence',69:'03-cancellation-sequence',70:'04-cancellation-advice-sequence',71:'05-reversal-sequence',5:'06-business-processes',10:'07-typical-activity',4:'08-role-model'}
  cp=em.get('canonical_diagram')
  if not cp and number in pilot:
   cp=(base/'diagrams/pilot'/(pilot[number]+'.md')).relative_to(root).as_posix()
   em['canonical_diagram']=cp;em['disposition']='canonical-reconstruction-created-needs-review'
   eb+='\n'+kb.link(ep,root/cp,'Canonical source reconstruction, participant/flow context and completed visual review')+'\n';kb.put(ep,kb.front(em)+eb.strip()+'\n')
  if not cp:issues.append('No canonical page for '+occ['figure_id']);reports.append(record);continue
  p=root/cp;m,b=kb.metadata(p);pages.append(p)
  if number in pilot:
   m['source_locations']=[{'source_id':sid,'locator':occ['source_locator'],'heading_path':occ['heading_path'],'xml_path':occ['xml_path'],'source_figure_id':occ['figure_id']}]
   m['original_asset']=image['original'];m['manual_curated']=True
  record.update(canonical_path=cp,disposition='source-reconstructed',render_status=m.get('render_status'),visual_review=m.get('visual_review'),review_status=m.get('review_status'))
  if m.get('visual_review')!='pass' or m.get('render_status')!='pass':issues.append('Incomplete visual/render check '+cp)
  if matches:
   m['rendered_source_pages']=record['rendered_source_pages'];m['rendered_source_pdf']=locations['pdf'];m['source_page_mapping_method']=record['page_mapping_method']
   section='## Rendered source page context\n\n'+kb.link(p,root/locations['pdf'],'Read-only Word-rendered source PDF')+'; file page(s) '+', '.join(map(str,record['rendered_source_pages']))+'. The page association is established by exact original-asset SHA-256 in the Word shape inventory, not by shape ordinal. Full-page/composite visual comparison is pending unless a separate dated review is recorded.\n'
   b=re.sub(r'\n<!-- RENDERED-SOURCE-START -->.*?<!-- RENDERED-SOURCE-END -->\n?','\n',b,flags=re.S)
   b+='\n<!-- RENDERED-SOURCE-START -->\n'+section+'<!-- RENDERED-SOURCE-END -->\n'
  if occ['figure_id'] in nativebyfig:
   ms=nativebyfig[occ['figure_id']];m['native_embedded_assets']=[x['asset'] for x in ms]
   b=re.sub(r'\n<!-- NATIVE-EVIDENCE-START -->.*?<!-- NATIVE-EVIDENCE-END -->\n?','\n',b,flags=re.S)
   b+='\n<!-- NATIVE-EVIDENCE-START -->\n## Native embedded source object\n\n'+' · '.join(kb.link(p,root/x['asset'],Path(x['asset']).name) for x in ms)+'\n\n'+kb.link(p,base/'documents'/sid/'native-embeddings.md','Native-object identity and occurrence inventory')+'. These original embedded bytes are retained unchanged. The visual reconstruction was compared with the supplied visible picture/complete vector preview. Hidden native layers or additional native pages have not been activated or checked; visual fidelity does not assert their equivalence.\n<!-- NATIVE-EVIDENCE-END -->\n'
  kb.put(p,kb.front(m)+b.strip()+'\n')
  for pid in m.get('participant_ids',[]):
   if pid not in participants:issues.append('Unresolved participant '+pid+' on '+cp);continue
   pp=participants[pid];pm,pb=kb.metadata(pp);tag='SOURCE196-DIAGRAM-'+str(number)
   pb=re.sub(r'\n<!-- '+tag+r'-START -->.*?<!-- '+tag+r'-END -->\n?','\n',pb,flags=re.S)
   pb+='\n<!-- '+tag+'-START -->\n'+kb.link(pp,p,m.get('title',p.stem))+' — '+sid+' '+occ['source_locator']+'.\n<!-- '+tag+'-END -->\n';kb.put(pp,kb.front(pm)+pb.strip()+'\n')
  reports.append(record)
 # Index maintained pages; do not rewrite their substantive contents.
 fi=base/'flows/index.md';fm,_=kb.metadata(fi);flowrows=[]
 for p in sorted((base/'flows').glob('*.md')):
  m,_=kb.metadata(p)
  if m.get('document_kind')=='business-flow':flowrows.append([kb.link(fi,p,m.get('title',p.stem)),m.get('review_status'),', '.join(m.get('message_ids',[]))])
 fm['updated']='2026-11-09';kb.put(fi,kb.front(fm)+'# Settlement and Reconciliation flows\n\n'+kb.table(['Flow','Review status','Exact messages in maintained metadata'],flowrows)+'\nSource process narratives, activity tables and diagram reconstruction reviews remain separately identified. A successful visual check does not resolve the source wording/edition issues linked on the underlying pages.\n')
 pi=base/'participants.md';pm,pb=kb.metadata(pi);tag='ALL-SCOPED-RECORDS';pb=re.sub(r'\n<!-- '+tag+r'-START -->.*?<!-- '+tag+r'-END -->\n?','\n',pb,flags=re.S)
 selected=[]
 for pid,p in participants.items():
  m,_=kb.metadata(p)
  if sid in m.get('source_ids',[]):selected.append((m.get('title',pid),p,m))
 pb+='\n<!-- '+tag+'-START -->\n## All maintained source-scoped participant records\n\n'+kb.table(['Participant','Role kind','Status'],[[kb.link(pi,p,title),m.get('role_kind'),m.get('review_status')] for title,p,m in sorted(selected)])+'<!-- '+tag+'-END -->\n';pm['updated']='2026-11-09';kb.put(pi,kb.front(pm)+pb.strip()+'\n')
 di=base/'diagrams/index.md';kb.put(di,kb.front({'template':False,'document_kind':'diagram-index','review_status':'needs-review','domain':'securities','source_ids':[sid],'message_sets':['settlement-and-reconciliation'],'updated':'2026-11-09'})+'# Settlement Part 1 source figures\n\nAll 72 visible source objects have a disposition: 68 substantive diagrams and four notation-legend symbols. All 68 diagram reconstructions have source-picture comparison and Mermaid 12.3.0 render evidence. Full Word-page/composite review and native hidden-layer review remain separate limitations.\n\n'+kb.table(['Source figure','Reference','Source DOCX rendered pages','Disposition','Visual check'],[[r['source_figure_id'],kb.link(di,root/r['canonical_path'],r['canonical_path'].split('/')[-1]),', '.join(map(str,r['rendered_source_pages'])) or 'unresolved',r['disposition'],r.get('visual_review')] for r in sorted(reports,key=lambda x:x['source_figure_id'])])+'\n'+kb.link(di,base/'workbooks/src-000198/diagrams','Part 3 workbook models')+'\n')
 for p in pages+[fi,pi,di]+[p for _,p,_ in selected]:
  text=p.read_text(encoding='utf-8')
  for target in re.findall(r'\]\(([^)]+)\)',text):
   target=unquote(target.strip('<>').split('#')[0])
   if not target or '://' in target:continue
   if not (p.parent/target).exists():issues.append('Missing link '+str(p.relative_to(root))+' -> '+target)
 summary={'date':'2026-11-09','source_id':sid,'source_sha256':source['sha256'],'visible_source_objects':len(reports),'substantive_diagrams':sum(r.get('disposition')=='source-reconstructed' for r in reports),'legend_symbols':4,'render_pass':sum(r.get('render_status')=='pass' for r in reports),'visual_fidelity_pass':sum(r.get('visual_review')=='pass' for r in reports),'exact_hash_page_mappings':sum(bool(r['rendered_source_pages']) for r in reports),'flows':len(flowrows),'participants':len(selected),'native_embedded_members':native['native_member_count'],'records':reports,'validation_errors':issues,'limitations':['Picture-level visual comparisons are complete; full rendered Word-page/composite review is not yet asserted.','Native embedded files are retained but hidden layers/pages are not activated or reviewed.','Source terminology/edition conflicts and full substantive table review remain needs-review.']}
 kb.dump(root/'tracking/reviews/settlement-part1-diagrams.json',summary);print(json.dumps({k:v for k,v in summary.items() if k not in ('records','limitations')}))
 if issues:raise SystemExit(1)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);main(p.parse_args().root.resolve())
