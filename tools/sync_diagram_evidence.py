"""Synchronize occurrence navigation with existing canonical diagram evidence, never invent review."""
import argparse,json,re
from pathlib import Path
import kb
def main(root):
 updated=[];unresolved=[]
 for src in kb.sources(root):
  sid=src['source_id']
  if src['format']!='docx':continue
  doc=root/src['set_path']/'documents'/sid;byfigure={}
  for p in (doc/'diagrams').glob('fig-*.md'):
   m,b=kb.metadata(p);target=m.get('canonical_diagram')
   if not target or not isinstance(target,str):continue
   cp=root/target
   if not cp.exists():unresolved.append({'path':p.relative_to(root).as_posix(),'missing_canonical':target});continue
   cm,_=kb.metadata(cp)
   if cm.get('document_kind')!='diagram':continue
   old=dict(m);existing=m.get('disposition','');qualified=any(x in existing for x in ['contextual-review-open','context-review-open'])
   for key in ['render_status','visual_review','renderer','rendered_svg','rendered_png','visual_review_date','visual_review_timezone']:
    if key in cm:m[key]=cm[key]
   m['content_origin']='source-occurrence';m['review_status']='needs-review' if qualified else cm.get('review_status','needs-review')
   if 'deduplicat' not in existing and not qualified:m['disposition']='source-reconstruction'
   m['canonical_issue_ids']=cm.get('issue_ids',[]);m['canonical_review_limitations']=cm.get('limitations',[])
   replacement='## Canonical reconstruction and review\n\n'+kb.link(p,cp,'Canonical diagram, source qualifications, participant/flow links and recorded review evidence')+'. Original media and this occurrence\'s precise locator are retained. Rendering and visual comparison results above are copied from the canonical reference; any unresolved business, version or contextual limitation remains open.\n'
   b=re.sub(r'## Interpretation and pending work\n.*?(?=\n<!--|\n## |\Z)',replacement,b,flags=re.S)
   if qualified:b+='\nThe occurrence retains an open contextual-review qualification even though the artwork has rendering/visual evidence.\n' if 'retains an open contextual-review qualification' not in b else ''
   kb.put(p,kb.front(m)+b);byfigure[m.get('diagram_id',p.stem)]={'canonical_diagram':target,'review_status':m['review_status'],'render_status':m.get('render_status'),'visual_review':m.get('visual_review'),'disposition':m.get('disposition'),'canonical_issue_ids':m['canonical_issue_ids']}
   if old!=m:updated.append({'path':p.relative_to(root).as_posix(),'canonical':target,'previous_review_status':old.get('review_status'),'review_status':m['review_status'],'disposition':m.get('disposition')})
  invpath=root/'work/documents'/sid/'media-review-inventory.json'
  if invpath.exists():
   inv=json.loads(invpath.read_text(encoding='utf-8'))
   for media in inv['media']:
    found=[]
    for occurrence in media['occurrences']:
     item=byfigure.get(occurrence['figure_id'])
     if item:occurrence.update(item);found.append(item)
    if found:
     media['canonical_review_results']=found
     if len(found)==len(media['occurrences']):
      media['review_status']='reviewed' if all(x['review_status']=='reviewed' for x in found) else 'needs-review'
      if len({x['disposition'] for x in found})==1:media['disposition']=found[0]['disposition']
      if all(x.get('render_status')=='pass' for x in found):media['canonical_render_status']='pass'
   kb.dump(invpath,inv)
 kb.dump(root/'tracking/reviews/diagram-evidence-consistency.json',{'date':kb.DATE,'scope':'Existing DOCX canonical links only. No new review performed.','updated':updated,'missing_canonical':unresolved});print(json.dumps({'updated':len(updated),'missing_canonical':len(unresolved)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
