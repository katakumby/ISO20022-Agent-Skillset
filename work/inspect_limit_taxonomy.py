from pathlib import Path
from PIL import Image
root=Path('.').resolve();im=Image.open(root/'domains/securities/assets/src-000362/originals/image5.jpeg');print(im.size)
for name,box in [('top',(300,180,585,490)),('bottom',(300,480,585,932))]:im.crop(box).resize(((box[2]-box[0])*3,(box[3]-box[1])*3)).save(root/'work/documents/src-000362'/('taxonomy-'+name+'-inspection.png'))
