"""Record the Nov09 direct visual comparison of inspected reconstructions.

This is a review record utility, not an automatic visual-review algorithm. It is
limited to the explicitly inspected Mermaid hashes captured on first invocation.
"""
import argparse,hashlib,json,re
from pathlib import Path
import kb

CHECKED={38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72}

def main(root,newly_inspected=()):
 report_path=root/'tracking/reviews/settlement-sequences.json'
 manifest=json.loads((root/'work/settlement-sequences.json').read_text(encoding='utf-8'))
 rendered={x['diagram']:x for x in json.loads((root/'work/settlement-sequences-render.json').read_text(encoding='utf-8'))}
 existing=json.loads(report_path.read_text(encoding='utf-8')) if report_path.exists() else None
 prior={x['source_figure_id']:x for x in existing['records']} if existing else {}
 rows=[]
 for item in manifest['outputs']:
  num=int(item['source_figure_id'].split('-')[1])
  if num not in CHECKED:continue
  page=root/item['path'];mmd=page.with_suffix('.mmd');sha=hashlib.sha256(mmd.read_bytes()).hexdigest();rid=page.stem
  if sha!=item['mermaid_sha256']:raise ValueError('Mermaid changed after generation '+rid)
  if prior and rid not in prior and num not in newly_inspected:continue
  if rid in prior and prior[rid]['mermaid_sha256']!=sha:raise ValueError('New visual comparison required '+rid)
  rr=rendered[rid]
  if rr['result']!='pass':raise ValueError('Render did not pass '+rid)
  original=root/item['original']
  if hashlib.sha256(original.read_bytes()).hexdigest()!=item['original_sha256']:raise ValueError('Original asset changed '+rid)
  rec={**item,'visual_review':'pass','visual_review_date':'2026-11-09','visual_review_timezone':'Europe/Warsaw',
   'render_result':'pass','renderer':rr['renderer'],'renderer_version':rr['version'],'render_date_utc':rr['date'],
   'svg':rr['svg'],'png':rr['png'],'rendered_png_sha256':hashlib.sha256((root/rr['png']).read_bytes()).hexdigest(),
   'checks':['Original image and rendered reconstruction both directly viewed.',
    'Participant labels and repeated role instances checked.',
    'Every source message label, arrow endpoint and direction checked.',
    'Top-to-bottom message order and repeated occurrences checked.',
    'Each optional frame checked, including two-message frames in figures56/57 and all eight distinct status frames in split-settlement parts.',
    'Split-settlement continuation notes and differently ordered near-duplicate source pictures retained.',
    'Source label discrepancies and narrative qualifications retained; no conflict silently repaired.'],
   'review_scope':'Visual fidelity of this source reconstruction only; source/business ambiguities and other table/diagram coverage remain open.'}
  rec['reconstruction_visual_review']='pass';rows.append(rec)
  m,b=kb.metadata(page);m.update(render_status='pass',visual_review='pass',renderer='Mermaid '+rr['version'],rendered_svg=rr['svg'],rendered_png=rr['png'],render_date_utc=rr['date'],visual_review_date='2026-11-09',visual_review_timezone='Europe/Warsaw')
  if num==40:m['issues']=sorted(set(m.get('issues',[])+['issue-000023']))
  b=re.sub(r'## Rendering and visual review\n.*', '## Rendering and visual review\n\nParse/render passed with Mermaid '+rr['version']+' and '+rr['renderer']+'. '+kb.link(page,root/rr['svg'],'Rendered SVG')+' · '+kb.link(page,root/rr['png'],'Rendered PNG')+'.\n\nOn 2026-11-09 (Europe/Warsaw), the original and rendered reconstruction were directly compared for all participant labels, message labels, endpoints, direction, order, repeated messages and optional groups. Result: **visual fidelity pass**. Render date in the machine report is UTC '+rr['date']+'. Source disagreements are preserved; this is not approval of the entire business flow.\n\n'+kb.link(page,report_path,'Hash-bound review evidence')+'\n', b,flags=re.S)
  if num==40:b+='\nSource conflict: '+kb.link(page,root/'tracking/issues.md#issue-000023','issue-000023')+'.\n'
  kb.put(page,kb.front(m)+b.strip()+'\n')
 kb.dump(report_path,{'date':'2026-11-09','timezone':'Europe/Warsaw','source_id':'src-000196','source_sha256':manifest['source_sha256'],'diagram_count':len(rows),'render_pass':len(rows),'visual_fidelity_pass':len(rows),'records':rows})
 index=root/'domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/diagrams/settlement-sequences/index.md'
 if index.exists():
  im,_=kb.metadata(index);reviewed={r['source_figure_id'] for r in rows}
  kb.put(index,kb.front(im)+'# Settlement sequence reconstructions\n\n'+kb.table(['Source figure','Reconstruction','Flow','Review'],[[x['source_figure_id'],kb.link(index,root/x['path'],Path(x['path']).stem),kb.link(index,root/x['flow_path'],Path(x['flow_path']).stem),'visual fidelity pass; context needs review' if x['source_figure_id'] in reviewed else 'pending-render-comparison'] for x in manifest['outputs']]))
 print(json.dumps({'diagrams':len(rows),'render_pass':len(rows),'visual_fidelity_pass':len(rows)}))

if __name__=='__main__':
  p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--newly-inspected',type=int,nargs='*',default=[]);a=p.parse_args();main(a.root.resolve(),a.newly_inspected)
