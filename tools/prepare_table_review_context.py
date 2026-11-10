"""Render bounded full-page context for source table layout review; no review assertion."""
import argparse,json,hashlib
from pathlib import Path
from local_runtime import load_font
from PIL import Image,ImageDraw,ImageFont
import pypdfium2 as pdfium
import kb
def main(root,sid):
 s=next(s for s in kb.sources(root) if s['source_id']==sid);r=json.loads((root/'work/docx-render'/sid/'reconciliation.json').read_text(encoding='utf-8'));pages=sorted({p for t in r['tables'] for p in range(t['word_start_file_page'],t['word_end_file_page']+1)});dest=root/kb.area(s['domain'])/'assets'/sid/'table-review-context';dest.mkdir(parents=True,exist_ok=True);pdf=root/'work/docx-render'/sid/'document.pdf';d=pdfium.PdfDocument(pdf);items=[];font=load_font(18)
 for page in pages:
  path=dest/f'page-{page:04d}.png';im=d[page-1].render(scale=100/72).to_pil();im.save(path);items.append({'page':page,'path':path.relative_to(root).as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'width':im.width,'height':im.height,'tables':[t['source_table_id'] for t in r['tables'] if t['word_start_file_page']<=page<=t['word_end_file_page']]})
 contacts=[]
 for start in range(0,len(items),4):
  group=items[start:start+4];w=max(x['width'] for x in group);h=max(x['height'] for x in group)+30;canvas=Image.new('RGB',(w*2,h*2),'#dddddd');draw=ImageDraw.Draw(canvas)
  for j,x in enumerate(group):a=j%2*w;b=j//2*h;draw.text((a+6,b+3),sid+' p'+str(x['page'])+' '+','.join(x['tables']),font=font,fill='black');canvas.paste(Image.open(root/x['path']),(a,b+30))
  p=dest/f'contact-{start//4+1:03d}.png';canvas.save(p);contacts.append(p.relative_to(root).as_posix())
 kb.dump(dest/'manifest.json',{'source_id':sid,'source_sha256':s['sha256'],'parent_pdf':pdf.relative_to(root).as_posix(),'parent_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'dpi':100,'pages':items,'contacts':contacts,'review_status':'pending-direct-visual-review'});print(json.dumps({'source':sid,'pages':len(pages),'contacts':len(contacts)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--sources',nargs='+',required=True);a=p.parse_args()
 for sid in a.sources:main(a.root.resolve(),sid)
