"""Audit canonical diagram destinations and existing render/visual evidence without re-approving them."""
import argparse,collections,json,re,subprocess
from pathlib import Path
import kb

def run(root):
 result=subprocess.run(['rg','-l','--glob','*.md','--regexp','^document_kind: "diagram"\r?$','domains','shared'],cwd=root,capture_output=True,text=True,check=False)
 if result.returncode not in (0,1):raise RuntimeError(result.stderr)
 records=[];errors=[]
 for name in result.stdout.splitlines():
  p=root/name;m,b=kb.metadata(p);render=m.get('render_status');visual=m.get('visual_review');v=visual.get('result',visual.get('status')) if isinstance(visual,dict) else visual
  blocks=re.findall(r'```mermaid\s*\n(.*?)\n```',b,re.S)
  r={'path':p.relative_to(root).as_posix(),'source_ids':m.get('source_ids',[]),'review_status':m.get('review_status'),'render_status':render,'visual_review':v,'mermaid_blocks':len(blocks),'source_kind':m.get('content_origin',m.get('origin')),'issue_ids':m.get('issue_ids',[])}
  if not blocks:errors.append({'kind':'missing-mermaid','path':r['path']})
  if render not in ['pass','passed']:errors.append({'kind':'render-evidence-not-passing','path':r['path'],'value':render})
  if v in [None,'not-run','not-recorded']:errors.append({'kind':'visual-evidence-absent','path':r['path']})
  if not r['source_ids']:errors.append({'kind':'source-identity-absent','path':r['path']})
  for key in ['rendered_svg','rendered_png']:
   target=m.get(key)
   if target and isinstance(target,str) and not (root/target).exists() and not (p.parent/target).exists():errors.append({'kind':'missing-rendered-artifact','path':r['path'],'field':key,'target':target})
  records.append(r)
 out={'date':kb.DATE,'scope':'Canonical diagram Markdown, existing render/visual evidence and named artifact existence. Qualified/partial source comparisons remain qualified; this is not a new render or visual approval.','canonical_diagrams':len(records),'render_states':dict(collections.Counter(str(x['render_status']) for x in records)),'visual_states':dict(collections.Counter(str(x['visual_review']) for x in records)),'review_states':dict(collections.Counter(x['review_status'] for x in records)),'errors':errors,'records':records}
 kb.dump(root/'tracking/reviews/diagram-record-audit.json',out)
 print(json.dumps({k:v for k,v in out.items() if k!='records'},ensure_ascii=False))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();run(a.root.resolve())
