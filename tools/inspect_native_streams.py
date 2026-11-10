#!/usr/bin/env python3
"""Bounded, read-only inspection of supplied CFB/OLE compound streams.
No object activation, application invocation, or native Visio decoding.
Usage: python tools/inspect_native_streams.py --root PATH
Format basis: Microsoft MS-CFB sections2.2-2.6 (header/FAT/miniFAT/directory).
"""
from pathlib import Path
import argparse,collections,hashlib,io,json,struct
from PIL import Image
import kb
END=0xfffffffe;FREE=0xffffffff
u16=lambda b,o:struct.unpack_from('<H',b,o)[0]
u32=lambda b,o:struct.unpack_from('<I',b,o)[0]
u64=lambda b,o:struct.unpack_from('<Q',b,o)[0]
sha=lambda b:hashlib.sha256(b).hexdigest()
class CFB:
 def __init__(self,b):
  self.b=b
  if b[:8]!=bytes.fromhex('d0cf11e0a1b11ae1'):raise ValueError('Not CFB')
  self.version=u16(b,26);self.ss=1<<u16(b,30);self.ms=1<<u16(b,32)
  if (self.version,self.ss) not in [(3,512),(4,4096)] or self.ms!=64 or u16(b,28)!=0xfffe:raise ValueError('Unsupported CFB geometry')
  self.nsec=len(b)//self.ss-1;self.cutoff=u32(b,56)
  ids=[x for x in struct.unpack_from('<109I',b,76) if x!=FREE];cur=u32(b,68);seen=set()
  for _ in range(u32(b,72)):
   if cur in seen:raise ValueError('DIFAT cycle')
   seen.add(cur);a=struct.unpack('<'+'I'*(self.ss//4),self.sec(cur));ids.extend(x for x in a[:-1] if x!=FREE);cur=a[-1]
  if len(ids)!=u32(b,44):raise ValueError('FAT count mismatch')
  self.fat=[x for sid in ids for x in struct.unpack('<'+'I'*(self.ss//4),self.sec(sid))]
  raw=b''.join(self.sec(i) for i in self.chain(u32(b,48),self.fat));self.entries=[]
  for i in range(0,len(raw),128):
   d=raw[i:i+128];ln=u16(d,64);kind=d[66]
   if not kind:continue
   if ln<2 or ln>64 or ln%2:raise ValueError('Directory name length')
   self.entries.append({'id':i//128,'name':d[:ln-2].decode('utf-16le'),'kind':kind,'left':u32(d,68),'right':u32(d,72),'child':u32(d,76),'start':u32(d,116),'size':u32(d,120) if self.version==3 else u64(d,120)})
  self.byid={e['id']:e for e in self.entries};rt=self.byid[0]
  if rt['kind']!=5:raise ValueError('Root kind')
  self.mini=self.regular(rt['start'],rt['size']);mf=u32(b,60)
  mraw=b''.join(self.sec(i) for i in self.chain(mf,self.fat)) if u32(b,64) else b''
  if len(mraw)!=u32(b,64)*self.ss:raise ValueError('MiniFAT count mismatch')
  self.minifat=list(struct.unpack('<'+'I'*(len(mraw)//4),mraw));self.paths={0:''};walked=set()
  def walk(i,parent):
   if i==FREE:return
   if i in walked or i not in self.byid:raise ValueError('Invalid directory tree')
   walked.add(i);e=self.byid[i];walk(e['left'],parent);self.paths[i]=parent+e['name'];
   if e['kind']==1:walk(e['child'],self.paths[i]+'/')
   walk(e['right'],parent)
  walk(rt['child'],'');self.unreachable=[e['id'] for e in self.entries if e['id'] not in self.paths]
 def sec(self,i):
  if not 0<=i<self.nsec:raise ValueError('Sector bound')
  return self.b[(i+1)*self.ss:(i+2)*self.ss]
 def chain(self,start,fat):
  out=[];seen=set();i=start
  while i!=END:
   if i==FREE and not out:return out
   if i in seen or not 0<=i<len(fat):raise ValueError('Invalid sector chain')
   seen.add(i);out.append(i);i=fat[i]
  return out
 def regular(self,start,size):
  if size==0:return b''
  raw=b''.join(self.sec(i) for i in self.chain(start,self.fat))
  if len(raw)<size:raise ValueError('Truncated regular stream')
  return raw[:size]
 def read(self,e):
  if e['size']==0:return b''
  if e['size']>=self.cutoff:return self.regular(e['start'],e['size'])
  raw=b''
  for i in self.chain(e['start'],self.minifat):
   pos=i*self.ms
   if pos+self.ms>len(self.mini):raise ValueError('Mini-sector bound')
   raw+=self.mini[pos:pos+self.ms]
  if len(raw)<e['size']:raise ValueError('Truncated mini stream')
  return raw[:e['size']]
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',default=Path(__file__).resolve().parents[1]);args=ap.parse_args();root=Path(args.root).resolve();cat=json.loads((root/'catalog/docx-native-embeddings.json').read_text(encoding='utf-8'));groups=collections.defaultdict(list)
 for s in cat['sources']:
  for n in s['native_members']:
   if n['format']!='vsdx':groups[n['sha256']].append(n)
 reports=[]
 for h,occ in groups.items():
  original=root/occ[0]['asset'];data=original.read_bytes()
  if sha(data)!=h:raise ValueError('Native fingerprint mismatch')
  c=CFB(data);work=root/'work/native-cfb'/h;work.mkdir(parents=True,exist_ok=True);streams=[];bmps=[]
  for e in c.entries:
   if e['kind']!=2:continue
   b=c.read(e);p=work/f"stream-{e['id']:04d}.bin";p.write_bytes(b);r={'directory_id':e['id'],'stream_path':c.paths.get(e['id'],'UNREACHABLE/'+e['name']),'size_bytes':len(b),'sha256':sha(b),'path':p.relative_to(root).as_posix(),'storage':'mini' if e['size']<c.cutoff else 'regular'};streams.append(r)
   if any(o['program_id']=='PBrush' for n in occ for o in n['occurrences']):
    start=0
    while True:
     at=b.find(b'BM',start)
     if at<0:break
     start=at+2
     if at+14>len(b):continue
     size=u32(b,at+2)
     if size<26 or at+size>len(b):continue
     raw=b[at:at+size]
     try:im=Image.open(io.BytesIO(raw));im.load()
     except Exception:continue
     dest=root/Path(occ[0]['asset']).parent/f'{original.stem}-native-bitmap-{len(bmps)+1}.bmp';dest.write_bytes(raw);pix=im.convert('RGBA');matches=[]
     for n in occ:
      for o in n['occurrences']:
       for prev in o['previews']:
        if prev.get('asset'):
         try:
          pi=Image.open(root/prev['asset']).convert('RGBA');eq=pi.size==pix.size and pi.tobytes()==pix.tobytes()
          matches.append({'source_id':n['source_id'],'source_locator':o['source_locator'],'figure_id':o['figure_id'],'preview':prev['asset'],'dimensions':list(pi.size),'pixels_equal':eq})
         except Exception as ex:matches.append({'source_id':n['source_id'],'error':str(ex)})
     bmps.append({'stream_path':r['stream_path'],'offset_bytes':at,'size_bytes':size,'sha256':sha(raw),'dimensions':list(im.size),'mode':im.mode,'asset':dest.relative_to(root).as_posix(),'preview_comparisons':matches})
  result={'native_sha256':h,'format':'CFB','occurrences':occ,'major_version':c.version,'sector_size':c.ss,'directory_entries':c.entries,'unreachable_directory_ids':c.unreachable,'streams':streams,'bitmaps':bmps,'inspection_date':'2026-11-09','activation':'not-activated','static_stream_inventory':'pass','semantic_review':'pending','limitations':['Stream inventory preserves bytes; VisioDocument internal pages and layers are not decoded. Bitmap equality is reported only for exact size/RGBA matches.']};kb.dump(work/'inspection.json',result);reports.append(result)
 summary={'unique_compound_files':len(reports),'occurrences':sum(len(x['occurrences']) for x in reports),'streams':sum(len(x['streams']) for x in reports),'unreachable_directory_entries':sum(len(x['unreachable_directory_ids']) for x in reports),'bitmap_payloads':sum(len(x['bitmaps']) for x in reports),'bitmap_preview_comparisons':sum(len(b['preview_comparisons']) for x in reports for b in x['bitmaps']),'exact_pixel_matches':sum(c.get('pixels_equal',False) for x in reports for b in x['bitmaps'] for c in b['preview_comparisons'])};kb.dump(root/'catalog/native-stream-inspection.json',{'summary':summary,'inspections':reports,'format_documentation':['https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cfb/05060311-bfce-4b12-874d-71fd4ce63aea','https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-cfb/b37413bb-f3ef-4adc-b18e-29bddd62c26e']});print(json.dumps(summary))
if __name__=='__main__':main()
