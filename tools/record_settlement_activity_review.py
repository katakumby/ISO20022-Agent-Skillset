"""Record an actual source/render comparison; default only restores known hashes."""
import argparse,hashlib,json,re
from pathlib import Path
import kb

def main(root,newly_inspected=()):
 manifest=json.loads((root/'work/settlement-activities.json').read_text(encoding='utf-8'))
 renders={x['diagram']:x for x in json.loads((root/'work/settlement-activities-render.json').read_text(encoding='utf-8'))}
 report_path=root/'tracking/reviews/settlement-activities.json'
 old=json.loads(report_path.read_text(encoding='utf-8')) if report_path.exists() else {'records':[]}
 prior={x['source_figure_id']:x for x in old['records']};rows=[]
 for item in manifest['outputs']:
  ident=item['source_figure_id'];num=int(ident.split('-')[1])
  if ident not in prior and num not in newly_inspected:continue
  page=root/item['path'];sha=hashlib.sha256(page.with_suffix('.mmd').read_bytes()).hexdigest()
  if item['mermaid_sha256']!=sha:raise ValueError('Mermaid/source manifest mismatch '+ident)
  if ident in prior and prior[ident]['mermaid_sha256']!=sha and num not in newly_inspected:raise ValueError('Fresh visual comparison required '+ident)
  if hashlib.sha256((root/item['original']).read_bytes()).hexdigest()!=item['original_sha256']:raise ValueError('Original changed '+ident)
  rr=renders[ident]
  if rr['result']!='pass':raise ValueError('Renderer failed '+ident)
  rec={**item,'visual_review':'pass','visual_review_date':'2026-11-09','visual_review_timezone':'Europe/Warsaw','render_result':'pass','renderer':rr['renderer'],'renderer_version':rr['version'],'render_date_utc':rr['date'],'svg':rr['svg'],'png':rr['png'],'rendered_png_sha256':hashlib.sha256((root/rr['png']).read_bytes()).hexdigest(),'checks':['Original raster or full vector preview and final rendered reconstruction directly viewed.','All role/swimlane boundaries, activity labels, decisions and Yes/No branches compared.','Every connector endpoint, feedback loop, visible arrowhead/plain connector and explicit synchronization bar compared.','Start/end symbols and green/blue activity distinctions retained; native layout may reflow lanes.','Generic communication categories remain generic; no exact message or institution inferred from a pictogram.'],'review_scope':'Visual relationship fidelity only; full table/business review and explicitly recorded source ambiguities remain open.'};rows.append(rec)
  m,b=kb.metadata(page);m.update(render_status='pass',visual_review='pass',renderer='Mermaid '+rr['version'],rendered_svg=rr['svg'],rendered_png=rr['png'],render_date_utc=rr['date'],visual_review_date='2026-11-09',visual_review_timezone='Europe/Warsaw')
  b=re.sub(r'## Rendering and visual review\n.*','## Rendering and visual review\n\nParse/render passed using Mermaid '+rr['version']+' with '+rr['renderer']+'. '+kb.link(page,root/rr['svg'],'Rendered SVG')+' · '+kb.link(page,root/rr['png'],'Rendered PNG')+'.\n\nOn 2026-11-09 (Europe/Warsaw), the original/full vector preview and the final reconstruction were directly compared for labels, role boundaries, decisions, branches, feedback paths, arrowheads/plain connections, start/end symbols and source synchronization bars. Result: **visual relationship fidelity pass**. Native layout reflows the lanes; original assets remain authoritative for pictorial layout. The machine render date is UTC '+rr['date']+'.\n\n'+kb.link(page,report_path,'Hash-bound review evidence')+'\n',b,flags=re.S);kb.put(page,kb.front(m)+b.strip()+'\n')
 kb.dump(report_path,{'date':'2026-11-09','timezone':'Europe/Warsaw','source_id':'src-000196','source_sha256':manifest['source_sha256'],'diagram_count':len(rows),'render_pass':len(rows),'visual_fidelity_pass':len(rows),'records':rows})
 out=root/'domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-activities';ix=out/'index.md';im,_=kb.metadata(ix);reviewed={x['source_figure_id'] for x in rows};kb.put(ix,kb.front(im)+'# Settlement activity and scope diagrams\n\n'+kb.table(['Figure','Reference','Review'],[[x['source_figure_id'],kb.link(ix,root/x['path'],Path(x['path']).stem),'visual fidelity pass; context needs review' if x['source_figure_id'] in reviewed else 'pending-render-comparison'] for x in manifest['outputs']]))
 print(json.dumps({'diagrams':len(rows),'render_pass':len(rows),'visual_fidelity_pass':len(rows)}))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--newly-inspected',type=int,nargs='*',default=[]);a=p.parse_args();main(a.root.resolve(),a.newly_inspected)
