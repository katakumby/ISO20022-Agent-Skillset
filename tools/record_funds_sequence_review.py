"""Record only explicitly completed, hash-bound original/render comparisons."""
import argparse,hashlib,json,re
from pathlib import Path
import kb
def main(root,newly_inspected=()):
 manifest=json.loads((root/'work/funds-sequences.json').read_text(encoding='utf-8'));report=root/'tracking/reviews/funds-sequences.json';old=json.loads(report.read_text(encoding='utf-8')) if report.exists() else {'records':[]};prior={r['source_figure_id']:r for r in old['records']}
 renders={r['diagram']:r for r in json.loads((root/'work/funds-sequences-render.json').read_text(encoding='utf-8'))};rows=[]
 for item in manifest['outputs']:
  fid=item['source_figure_id'];num=int(fid.split('-')[1])
  if fid not in prior and num not in newly_inspected:continue
  p=root/item['path'];sha=hashlib.sha256(p.with_suffix('.mmd').read_bytes()).hexdigest()
  if sha!=item['mermaid_sha256']:raise ValueError('Manifest changed '+fid)
  if fid in prior and sha!=prior[fid]['mermaid_sha256'] and num not in newly_inspected:raise ValueError('Fresh review required '+fid)
  if hashlib.sha256((root/item['original']).read_bytes()).hexdigest()!=item['original_sha256']:raise ValueError('Original changed '+fid)
  rr=renders[fid]
  if rr['result']!='pass':raise ValueError('Render failed '+fid)
  m,b=kb.metadata(p);m.update(render_status='pass',visual_review='pass',renderer='Mermaid '+rr['version'],rendered_svg=rr['svg'],rendered_png=rr['png'],render_date_utc=rr['date'],visual_review_date='2026-11-09',visual_review_timezone='Europe/Warsaw')
  b=re.sub(r'## Rendering and visual review\n.*','## Rendering and visual review\n\nMermaid '+rr['version']+' parsed and rendered successfully using '+rr['renderer']+'. '+kb.link(p,root/rr['svg'],'Rendered SVG')+' · '+kb.link(p,root/rr['png'],'Rendered PNG')+'.\n\nThe unchanged source image and final reconstruction were directly compared on 2026-11-09 (Europe/Warsaw): participant instances, message labels, sender/receiver endpoints, vertical ordering and open arrowheads. Result: **visual relationship fidelity pass**. Recorded source wording/order differences remain unresolved as described above. The renderer’s UTC date is '+rr['date']+'.\n\n'+kb.link(p,report,'Hash-bound review evidence')+'\n',b,flags=re.S);kb.put(p,kb.front(m)+b.strip()+'\n')
  rows.append({**item,'render_status':'pass','visual_review':'pass','visual_review_date':'2026-11-09','visual_review_timezone':'Europe/Warsaw','renderer':rr['renderer'],'renderer_version':rr['version'],'render_date_utc':rr['date'],'png':rr['png'],'svg':rr['svg'],'rendered_png_sha256':hashlib.sha256((root/rr['png']).read_bytes()).hexdigest(),'review_scope':'Direct original-picture versus final-render label, participant, endpoint, ordering and open-arrow comparison. Source business conflicts and Word-page/native-layer checks remain separate.'})
 kb.dump(report,{'date':'2026-11-09','source_id':manifest['source_id'],'source_sha256':manifest['source_sha256'],'diagram_count':len(rows),'render_pass':len(rows),'visual_fidelity_pass':len(rows),'records':rows});print(json.dumps({'diagrams':len(rows),'render_pass':len(rows),'visual_fidelity_pass':len(rows)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--newly-inspected',type=int,nargs='*',default=[]);a=p.parse_args();main(a.root.resolve(),a.newly_inspected)
