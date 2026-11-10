"""Create labelled DOCX-media contact sheets and source-occurrence visual inventories.

Run render_docx_media.ps1 first for EMF/WMF previews. This helper recognises PNG data
stored with .tmp names and optionally decodes JPEG XR through bundled JxrDecApp.
Contact sheets are for triage; they do not establish complete Word composite figures.
"""
from pathlib import Path
import argparse,json,subprocess,hashlib,shutil,math
from PIL import Image,ImageOps,ImageDraw,ImageFont
import kb
from local_runtime import load_font

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--source',action='append');p.add_argument('--jxr-decoder');a=p.parse_args();root=a.root.resolve();results=[]
 override_file=root/'tracking/reviews/docx-media-classification.json';overrides={x['original']:x for x in json.loads(override_file.read_text(encoding='utf-8')).get('records',[])} if override_file.exists() else {}
 font=load_font(14)
 for s in kb.sources(root):
  if s['format']!='docx' or a.source and s['source_id'] not in a.source:continue
  sid=s['source_id'];work=root/'work/documents'/sid;rp=work/'records.json';pp=work/'media-previews.json'
  if not rp.exists() or not pp.exists():continue
  r=json.loads(rp.read_text(encoding='utf-8'));pre=json.loads(pp.read_text(encoding='utf-8-sig'));items=[]
  for m in pre['media']:
   m['preview']=m['preview'].replace('\\','/');original=root/m['original'];preview=root/m['preview'];ext=original.suffix.lower()
   if ext=='.tmp':
    try:
     im=Image.open(original)
     if im.format=='PNG':
      preview=original.parent.parent/'derived-previews'/(original.name+'.png');preview.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(original,preview);m.update(preview=preview.relative_to(root).as_posix(),renderer='PNG signature identification; unchanged bytes in preview copy',render_status='pass',error=None)
    except Exception as e:m['error']=repr(e)
   elif ext=='.wdp' and a.jxr_decoder:
    try:
     bmp=work/(original.name+'.bmp');preview=original.parent.parent/'derived-previews'/(original.name+'.png');preview.parent.mkdir(parents=True,exist_ok=True)
     subprocess.run([a.jxr_decoder,'-i',str(original),'-o',str(bmp),'-c','0'],check=True,capture_output=True)
     Image.open(bmp).save(preview);m.update(preview=preview.relative_to(root).as_posix(),renderer='JxrDecApp JPEG XR decode to BMP; Pillow PNG preview',render_status='pass',error=None)
    except Exception as e:m['error']=repr(e)
   occurrences=[]
   for f in r['figures']:
    if any(im.get('asset')==m['original'] for im in f['images']):
     evidence=root/s['set_path']/'documents'/sid/'diagrams'/(f['figure_id']+'.md');meta,_=kb.metadata(evidence) if evidence.exists() else ({},'')
     occurrences.append({'figure_id':f['figure_id'],'source_locator':f['locator'],'heading_path':f['heading_path'],'xml_path':f['xml_path'],'evidence_page':evidence.relative_to(root).as_posix(),'canonical_diagram':meta.get('canonical_diagram'),'drawing_containers':f['drawing_containers']})
   dims=None
   try:
    with Image.open(preview) as im:dims=list(im.size)
   except Exception as e:
    if m.get('error') is None:m['error']=repr(e)
   items.append({**m,'dimensions':dims,'occurrences':occurrences,'disposition':'pending-visual-classification','complete_composite_review':'not-run',**{k:v for k,v in overrides.get(m['original'],{}).items() if k not in ['source_id','original','sha256']}})
  sheets=[]
  for start in range(0,len(items),12):
   canvas=Image.new('RGB',(1500,1600),'#dddddd');draw=ImageDraw.Draw(canvas)
   for j,item in enumerate(items[start:start+12]):
    x=(j%3)*500;y=(j//3)*400
    label=Path(item['original']).name+' | '+', '.join(x['figure_id'] for x in item['occurrences'])
    loc='; '.join(x['source_locator'] for x in item['occurrences']) or 'No main-body occurrence mapped; inspect document package'
    draw.text((x+10,y+5),label[:67],font=font,fill='black');draw.text((x+10,y+25),loc[:67],font=font,fill='black')
    try:
     im=Image.open(root/item['preview']).convert('RGBA');im.thumbnail((480,335));background=Image.new('RGB',im.size,'white');background.paste(im,mask=im.getchannel('A'));canvas.paste(background,(x+(500-im.width)//2,y+55+(335-im.height)//2))
    except Exception as e:draw.text((x+10,y+100),'Preview unavailable: '+str(e)[:55],font=font,fill='red')
   dest=work/'contact-sheets'/f'media-{start+1:04d}-{min(start+12,len(items)):04d}.png';dest.parent.mkdir(parents=True,exist_ok=True);canvas.save(dest);sheets.append(dest.relative_to(root).as_posix())
  report={'source_id':sid,'source_sha256':s['sha256'],'media':items,'contact_sheets':sheets,'visual_review':'not-run','limitations':['Contact sheets are triage aids; readable full-size source/derived previews must be inspected before reconstructing labels or relationships.','w:object, w:drawing and grouped content can combine separately stored images and labels. Full-document page rendering remains required when an extracted asset omits relationships or text.','Unmapped media may occur in headers, footers, alternate drawings or unused package parts. No decorative exclusion is inferred.']};kb.dump(work/'media-review-inventory.json',report);kb.dump(pp,{**pre,'media':[{k:v for k,v in x.items() if k not in ['occurrences','disposition','complete_composite_review']} for x in items]})
  idx=root/s['set_path']/'documents'/sid/'media-inventory.md';text=kb.front(dict(template=False,document_kind='source-figure-inventory',review_status='needs-review',domain=s['domain'],source_ids=[sid]))+'# Original media and visual review inventory\n\nAll extracted originals remain unchanged. EMF/WMF previews are separate derived rasterizations. The complete Word figure may also contain text or relationships outside a single asset.\n\n'+kb.table(['Original asset','Preview','Source occurrences','Canonical reconstruction','Disposition'],[[kb.link(idx,root/x['original'],Path(x['original']).name),kb.link(idx,root/x['preview'],'Preview') if not x['error'] else x['error'],'; '.join(y['source_locator']+'; '+' / '.join(y['heading_path']) for y in x['occurrences']) or 'No main-body occurrence mapped','; '.join(kb.link(idx,root/y['canonical_diagram'],'Canonical') for y in x['occurrences'] if y.get('canonical_diagram')),x['disposition']] for x in items])+'\n## Complete-figure requirements\n\n'+'\n'.join('- '+x for x in report['limitations'])+'\n';kb.put(idx,text)
  result={'source_id':sid,'media':len(items),'rendered_or_viewable':sum(x['error'] is None for x in items),'unavailable':sum(x['error'] is not None for x in items),'contact_sheets':len(sheets),'inventory':idx.relative_to(root).as_posix(),'visual_review':'not-run'};results.append(result);print(json.dumps(result),flush=True)
 allresults=[]
 for stored in sorted((root/'work/documents').glob('*/media-review-inventory.json')):
  x=json.loads(stored.read_text(encoding='utf-8'));allresults.append({'source_id':x['source_id'],'media':len(x['media']),'rendered_or_viewable':sum(m['error'] is None for m in x['media']),'unavailable':sum(m['error'] is not None for m in x['media']),'contact_sheets':len(x['contact_sheets']),'visual_review':'not-run'})
 kb.dump(root/'catalog/docx-figure-inventory.json',{'updated':'2026-11-09','records':allresults,'review_status':'needs-review'})
if __name__=='__main__':main()
