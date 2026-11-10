"""Render bounded Word-derived page context and labelled contact sheets for review."""
import argparse,hashlib,json
from importlib.metadata import version
from pathlib import Path
from local_runtime import load_font
import pypdfium2 as pdfium
from PIL import Image,ImageDraw,ImageFont
import kb
def main(root,sid,pages,dpi):
 src=next(s for s in kb.sources(root) if s['source_id']==sid);pdf=root/'work/docx-render'/sid/'document.pdf';doc=pdfium.PdfDocument(pdf);nums=pages or list(range(1,len(doc)+1));assert all(1<=p<=len(doc) for p in nums);area=root/('shared' if src['domain']=='shared' else 'domains/'+src['domain']);dest=area/'assets'/sid/'word-page-context';dest.mkdir(parents=True,exist_ok=True);records=[]
 for num in nums:
  path=dest/f'page-{num:04d}.png';im=doc[num-1].render(scale=dpi/72).to_pil();im.save(path);records.append({'file_page':num,'path':path.relative_to(root).as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'width':im.width,'height':im.height})
 sheets=[];font=load_font(20)
 for start in range(0,len(records),4):
  chosen=records[start:start+4];w=max(r['width'] for r in chosen);h=max(r['height'] for r in chosen)+32;canvas=Image.new('RGB',(w*2,h*2),'#dddddd');draw=ImageDraw.Draw(canvas)
  for j,r in enumerate(chosen):
   x=j%2*w;y=j//2*h;draw.text((x+8,y+4),sid+' — Word file page '+str(r['file_page']),fill='black',font=font);canvas.paste(Image.open(root/r['path']),(x,y+32))
  path=dest/f'contact-{chosen[0]["file_page"]:04d}-{chosen[-1]["file_page"]:04d}.png';canvas.save(path);sheets.append(path.relative_to(root).as_posix())
 report={'source_id':sid,'source_sha256':src['sha256'],'parent_pdf':pdf.relative_to(root).as_posix(),'parent_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'renderer':'pypdfium2 '+version('pypdfium2'),'dpi':dpi,'pages':records,'contacts':sheets,'visual_review':'not-run','limitations':['Word-derived layout, not a publisher PDF. Local Word STYLEREF header artifacts remain separately recorded.','Contacts support complete-page visual inventory, not automatic verification of text or every table cell.']};kb.dump(dest/'manifest.json',report);print(json.dumps({'source':sid,'pages':len(records),'contacts':sheets}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--source',required=True);p.add_argument('--pages',type=int,nargs='*');p.add_argument('--dpi',type=int,default=100);a=p.parse_args();main(a.root.resolve(),a.source,a.pages,a.dpi)
