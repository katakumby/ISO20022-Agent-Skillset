"""Inventory PDF image occurrences and vector-path candidates; render bounded pages on demand.

--source src-NNNNNN optionally bounds inventory. --render-pages 1-10,15 renders complete
pages at --dpi (default150) into assets, retaining the parent source/page provenance.
Vector detection is a candidate heuristic. It cannot replace full visual review or establish
that every substantive figure has been found. Original supplied bytes remain read-only.
"""
from __future__ import annotations
import argparse,io,json,re,hashlib,zipfile,subprocess,logging
from pathlib import Path
from collections import Counter
from pypdf import PdfReader
import kb
logging.getLogger('pypdf').setLevel(logging.ERROR)

def stream_bytes(obj):
 obj=obj.get_object() if hasattr(obj,'get_object') else obj
 if obj is None:return b''
 if isinstance(obj,list):return b'\n'.join(stream_bytes(x) for x in obj)
 return obj.get_data() if hasattr(obj,'get_data') else b''
def used_images(page):
 images=[];vector=Counter();errors=[]
 def walk(content,resources,path,seen):
  b=stream_bytes(content)
  vector.update(x.decode('ascii') for x in re.findall(rb'(?:^|\s)(m|l|c|v|y|re|S|f|f\*|B|B\*)\s',b))
  objects=resources.get('/XObject',{}) if resources else {}
  if hasattr(objects,'get_object'):objects=objects.get_object()
  for raw in re.findall(rb'/([^\s/]+)\s+Do\b',b):
   key='/'+raw.decode('latin1');xo=objects.get(key)
   if xo is None:errors.append('Unresolved XObject '+key);continue
   ref=str(getattr(xo,'idnum',''))+' '+str(getattr(xo,'generation',''))
   xo=xo.get_object()
   if xo.get('/Subtype')=='/Image':images.append(path+[key])
   elif xo.get('/Subtype')=='/Form' and ref not in seen:walk(xo,xo.get('/Resources',resources),path+[key],seen|{ref})
  if re.search(rb'\bBI\s',b):errors.append('Inline image syntax detected; inline image extraction requires separate review.')
 walk(page.get('/Contents'),page.get('/Resources'),[],set())
 return images,dict(vector),errors

def inspect(root,s,force=False):
 sid=s['source_id'];out=root/s['set_path']/'documents'/sid/'pdf-figures';asset=root/kb.area(s['domain'])/'assets'/sid/'pdf-images';work=root/'work/documents'/sid;status=work/'pdf-assets.json'
 if status.exists() and not force:
  old=json.loads(status.read_text(encoding='utf-8'))
  if old.get('source_sha256')==s['sha256']:return old
 data=kb.read_source(root,s)
 if hashlib.sha256(data).hexdigest()!=s['sha256']:raise ValueError('Changed source '+sid)
 reader=PdfReader(io.BytesIO(data));pages=[];images=[];asset_by_hash={};figure=0
 for pi,page in enumerate(reader.pages,1):
  paths,vector,errors=used_images(page);page_images=[]
  for path in paths:
   figure+=1;figid=f'fig-{figure:04d}'
   try:
    im=page.images[path[0] if len(path)==1 else path];b=im.data;h=hashlib.sha256(b).hexdigest();suffix=Path(im.name).suffix
    dest=asset/(h+suffix)
    if h not in asset_by_hash:dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b);asset_by_hash[h]=dest
    fp=out/(figid+'.md');record={'figure_id':figid,'file_page':pi,'xobject_path':path,'image_name':im.name,'asset':dest.relative_to(root).as_posix(),'sha256':h,'output':fp.relative_to(root).as_posix(),'disposition':'pending-visual-classification','reconstruction':'pending','visual_review':'not-run'};images.append(record);page_images.append(figid)
    text=kb.front(dict(template=False,document_kind='diagram-evidence',review_status='needs-review',domain=s['domain'],source_ids=[sid],source_editions=[s.get('source_edition')],figure_id=figid,file_pages=[pi],xobject_path=path,content_origin='source-reconstruction-pending',render_status='not-run',visual_review='not-run'))+'# '+figid+' - embedded PDF image occurrence\n\nSource: '+kb.source_link(root,fp,s)+f'. File page {pi}; XObject path '+repr(path)+'. The asset is extracted image data; the parent PDF remains authoritative for placement, labels and surrounding vector objects.\n\n!['+figid+']('+kb.rel(fp,dest)+')\n\n## Interpretation and pending work\n\nThis image occurrence is inventoried, not yet classified as substantive or decorative. It may be one component of a larger figure. Full-page rendering, complete figure cropping, textual semantics, participant/flow linking and Mermaid reconstruction remain pending. No parse, render or visual-review pass is claimed.\n';kb.put(fp,text)
   except Exception as e:errors.append('Image extraction '+repr(path)+': '+repr(e))
  pages.append({'file_page':pi,'image_occurrences':page_images,'vector_operator_candidates':vector,'requires_vector_visual_inspection':bool(vector),'errors':errors})
  if pi%500==0:print(json.dumps({'source_id':sid,'asset_pages_scanned':pi,'images':len(images)}),flush=True)
 record={'source_id':sid,'source_sha256':s['sha256'],'pages':pages,'image_occurrences':images,'unique_image_assets':len(asset_by_hash),'review_status':'needs-review','limitations':['Vector operator counts are lexical candidates, including table borders and decoration; they do not count substantive figures.','Text labels, clipping and image/vector composites require full rendered-page inspection.','Inline images and unresolved XObjects remain explicit errors rather than silently dropped figures.']};kb.dump(status,record)
 idx=out/'index.md';text=kb.front(dict(template=False,document_kind='diagram-inventory',review_status='needs-review',domain=s['domain'],source_ids=[sid]))+'# PDF figure candidates\n\n'+f"Scanned {len(pages)} file pages. Retained {len(images)} embedded image occurrences and {len(asset_by_hash)} unique extracted image assets. Vector-only pages remain candidates requiring visual inspection. Counts are not substantive-diagram coverage.\n\n"+kb.table(['Figure occurrence','File page','XObject path','Disposition'],[[kb.link(idx,root/x['output'],x['figure_id']),x['file_page'],repr(x['xobject_path']),x['disposition']] for x in images])+'## Page inventory\n\n'+kb.table(['File page','Images','Vector operator candidates','Errors'],[[p['file_page'],', '.join(p['image_occurrences']),json.dumps(p['vector_operator_candidates']),'; '.join(p['errors'])] for p in pages])+'\n'+ '\n'.join('- '+x for x in record['limitations'])+'\n';kb.put(idx,text)
 print(json.dumps({'source_id':sid,'pages':len(pages),'images':len(images),'unique_assets':len(asset_by_hash)}),flush=True);return record

def render(root,s,pages,dpi,poppler):
 if not poppler or not Path(poppler).exists():raise ValueError('Supply --pdftoppm with a working renderer executable path')
 data=kb.read_source(root,s)
 if hashlib.sha256(data).hexdigest()!=s['sha256']:raise ValueError('Changed source')
 o=s['occurrences'][0]
 if o.get('archive_member'):
  src=root/'work/documents'/s['source_id']/'render-source.pdf';src.parent.mkdir(parents=True,exist_ok=True);src.write_bytes(data)
 else:src=root/o['path']
 out=root/kb.area(s['domain'])/'assets'/s['source_id']/'rendered';out.mkdir(parents=True,exist_ok=True)
 total=len(PdfReader(io.BytesIO(data)).pages);selected=[]
 for term in pages.split(','):
  nums=[int(x) for x in term.split('-')];selected.extend(range(nums[0],nums[-1]+1))
 for pi in sorted(set(selected)):
  if pi<1 or pi>total:raise ValueError('Page outside source')
  prefix=out/f'page-{pi:05d}';subprocess.run([poppler,'-f',str(pi),'-l',str(pi),'-singlefile','-r',str(dpi),'-png',str(src),str(prefix)],check=True,capture_output=True)
  kb.dump(prefix.with_suffix('.json'),{'source_id':s['source_id'],'source_sha256':s['sha256'],'file_page':pi,'dpi':dpi,'render_tool':'pdftoppm','asset':prefix.with_suffix('.png').relative_to(root).as_posix(),'content_origin':'full-page-render','visual_review':'not-run'})
 print(json.dumps({'source_id':s['source_id'],'rendered_pages':len(set(selected)),'dpi':dpi}),flush=True)

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--source',action='append');ap.add_argument('--force',action='store_true');ap.add_argument('--render-pages');ap.add_argument('--dpi',type=int,default=150);ap.add_argument('--pdftoppm');a=ap.parse_args();root=a.root.resolve();reports=[]
 for s in kb.sources(root):
  if s['format']!='pdf' or a.source and s['source_id'] not in a.source:continue
  r=inspect(root,s,a.force);reports.append({'source_id':s['source_id'],'pages':len(r['pages']),'image_occurrences':len(r['image_occurrences']),'unique_image_assets':r['unique_image_assets'],'vector_candidate_pages':sum(p['requires_vector_visual_inspection'] for p in r['pages']),'errors':sum(len(p['errors']) for p in r['pages']),'review_status':'needs-review'})
  if a.render_pages:render(root,s,a.render_pages,a.dpi,a.pdftoppm)
 # Bounded updates rebuild the aggregate from all authoritative per-source inventories.
 reports=[]
 for stored in sorted((root/'work/documents').glob('*/pdf-assets.json')):
  r=json.loads(stored.read_text(encoding='utf-8'));reports.append({'source_id':r['source_id'],'pages':len(r['pages']),'image_occurrences':len(r['image_occurrences']),'unique_image_assets':r['unique_image_assets'],'vector_candidate_pages':sum(p['requires_vector_visual_inspection'] for p in r['pages']),'errors':sum(len(p['errors']) for p in r['pages']),'review_status':'needs-review'})
 kb.dump(root/'catalog/pdf-figure-inventory.json',{'updated':'2026-11-08','records':reports,'review_status':'needs-review'})
if __name__=='__main__':main()
