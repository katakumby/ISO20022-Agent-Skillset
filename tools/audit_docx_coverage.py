"""Reconcile DOCX table/figure destinations and recorded review metadata; never infer visual approval."""
import argparse,collections,json,re
from pathlib import Path
import kb

def run(root,repair_notation=False):
 records=[];gaps=[];updates=[]
 for src in kb.sources(root):
  if src['format']!='docx':continue
  sid=src['source_id'];doc=root/src['set_path']/'documents'/sid
  status_path=root/'work/documents'/sid/'status.json'
  status=json.loads(status_path.read_text(encoding='utf-8'))
  tables=[];figures=[]
  for p in sorted((doc/'tables').glob('tbl-*.md')):
   m,b=kb.metadata(p)
   evidence={k:v for k,v in m.items() if any(x in k for x in ['review','word_file','rendered_file'])}
   tables.append({'path':p.relative_to(root).as_posix(),'table_id':m.get('table_id'),'evidence':evidence})
  for p in sorted((doc/'diagrams').glob('fig-*.md')):
   m,b=kb.metadata(p);disposition=m.get('disposition','');canonical=m.get('canonical_diagram')
   notation=any(w in disposition for w in ['legend','notation','symbol','decorative','fragment','text-box','text-not-diagram'])
   if repair_notation and notation and m.get('classification_review')=='pass' and not canonical and '## Interpretation and pending work' in b:
    body='## Classified source item\n\nThis occurrence has a recorded visual classification. Its original asset and source locator are retained. The disposition below explains its role as source notation, a component of a complete figure, retained text, or a decorative exclusion. It is not an independent reconstructed business diagram.\n'
    b=re.sub(r'## Interpretation and pending work\n.*?(?=\n## |\n<!--|\Z)',body,b,flags=re.S)
    m.update(content_origin='classified-source-item',render_status='not-applicable-independent-reconstruction',visual_review='classification-recorded-see-disposition')
    kb.put(p,kb.front(m)+b);updates.append(p.relative_to(root).as_posix())
   r={'path':p.relative_to(root).as_posix(),'diagram_id':m.get('diagram_id'),'disposition':disposition,'canonical_diagram':canonical,'review_status':m.get('review_status'),'render_status':m.get('render_status'),'visual_review':m.get('visual_review'),'classification_review':m.get('classification_review')}
   figures.append(r)
   if canonical and not (root/canonical).exists():gaps.append({'source_id':sid,'kind':'missing-canonical-figure','path':r['path'],'target':canonical})
   elif not canonical and not notation and m.get('document_kind')!='diagram':gaps.append({'source_id':sid,'kind':'unresolved-figure-disposition','path':r['path'],'disposition':disposition})
  if len(tables)!=status.get('tables',0):gaps.append({'source_id':sid,'kind':'table-count-difference','extracted':status.get('tables'),'destinations':len(tables)})
  if len(figures)<status.get('figure_occurrences',0):gaps.append({'source_id':sid,'kind':'missing-figure-destinations','extracted':status.get('figure_occurrences'),'destinations':len(figures)})
  records.append({'source_id':sid,'source_sha256':src['sha256'],'source_index':(doc/'index.md').relative_to(root).as_posix(),'extraction_tables':status.get('tables',0),'extraction_figure_occurrences':status.get('figure_occurrences',0),'tables':tables,'figures':figures})
 report={'date':kb.DATE,'scope':'Destination and recorded-evidence reconciliation for all supplied DOCX sources. No new visual approval. Native objects and supplemental Word drawings have separately linked coverage.','sources':len(records),'table_destinations':sum(len(r['tables']) for r in records),'figure_destinations':sum(len(r['figures']) for r in records),'notation_prose_updates':updates,'gaps':gaps,'records':records}
 kb.dump(root/'tracking/reviews/docx-coverage-reconciliation.json',report)
 print(json.dumps({k:v for k,v in report.items() if k not in ['records','notation_prose_updates']}))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--repair-notation-prose',action='store_true');a=p.parse_args();run(a.root.resolve(),a.repair_notation_prose)
