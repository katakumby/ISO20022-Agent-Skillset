"""Local QA contacts of the final Cash Management reconstruction PNGs."""
from pathlib import Path
from local_runtime import load_font
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[1];dest=root/'domains/payments/assets/src-000014/reconstructed';font=load_font(20)
for start in range(1,37,4):
 items=[(n,Image.open(dest/f'fig-{n:04d}.png').convert('RGB')) for n in range(start,min(start+4,37))];w=max(im.width for _,im in items);h=max(im.height for _,im in items)+34;canvas=Image.new('RGB',(w*2,h*2),'#eeeeee');d=ImageDraw.Draw(canvas)
 for j,(n,im) in enumerate(items):x=j%2*w;y=j//2*h;d.text((x+8,y+5),f'Final reconstruction fig-{n:04d}',font=font,fill='black');canvas.paste(im,(x,y+34))
 canvas.save(dest/f'contact-{start:04d}-{items[-1][0]:04d}.png')
print('Nine final diagram contact sheets saved.')
