#!/usr/bin/env python3
"""Preserve DOCX native embedded objects without activating them.

Usage: python tools/inspect_docx_embeddings.py --root PATH [--source src-000079]
The supplied DOCX is read-only. Native members retain their bytes under assets;
relationships, enclosing source locations and picture previews are catalogued.
"""
from pathlib import Path, PurePosixPath
import argparse, hashlib, io, json, posixpath, zipfile
from lxml import etree
import kb
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','o':'urn:schemas-microsoft-com:office:office','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
R='{'+NS['r']+'}';W='{'+NS['w']+'}'
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p,default):return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default
def resolve(part,target):return posixpath.normpath(posixpath.join(posixpath.dirname(part),target)).lstrip('/')
def inspect(root,s):
 sid=s['source_id'];data=kb.read_source(root,s)
 if sha(data)!=s['sha256']:raise ValueError('Source fingerprint mismatch: '+sid)
 z=zipfile.ZipFile(io.BytesIO(data));members=sorted(n for n in z.namelist() if n.startswith('word/embeddings/') and not n.endswith('/'))
 rec=load(root/'work/documents'/sid/'records.json',{});figs=rec.get('figures',[]);objects=[];relsall=[]
 for part in sorted(n for n in z.namelist() if n.startswith('word/') and n.endswith('.xml') and '/_rels/' not in n):
  rp=posixpath.join(posixpath.dirname(part),'_rels',posixpath.basename(part)+'.rels')
  if rp not in z.namelist():continue
  rt=etree.fromstring(z.read(rp));rels={a.get('Id'):{'target':a.get('Target'),'type':a.get('Type'),'mode':a.get('TargetMode'),'member':None if a.get('TargetMode')=='External' else resolve(part,a.get('Target',''))} for a in rt}
  for rid,r in rels.items():
   if r['member'] in members:relsall.append({'part':part,'relationship_id':rid,**r})
  doc=etree.fromstring(z.read(part));tree=doc.getroottree()
  for obj in doc.xpath('//o:OLEObject',namespaces=NS):
   rid=obj.get(R+'id');r=rels.get(rid,{})
   locator=part+' '+tree.getpath(obj);figure=None;heading=[];container=next((a for a in obj.iterancestors() if a.tag==W+'object'),obj.getparent())
   anchor=next((a for a in obj.iterancestors() if a.getparent() is not None and a.getparent().tag==W+'body'),None)
   if part=='word/document.xml' and anchor is not None:
    kind=etree.QName(anchor).localname;idx=1+sum(1 for a in anchor.itersiblings(preceding=True) if a.tag==anchor.tag);xp='/w:document/w:body/w:'+kind+'['+str(idx)+']'
    if kind=='p':locator='direct-body paragraph P'+str(idx)
    elif kind=='tbl':locator='direct-body table T'+str(idx)+'; '+tree.getpath(obj)
    found=[f for f in figs if f.get('xml_path')==xp or tree.getpath(obj).startswith(f.get('xml_path','__missing__'))]
    if found:figure=found[0]['figure_id'];heading=found[0].get('heading_path',[])
   previews=[]
   for node in container.iter():
    if node is obj:continue
    for name,val in node.attrib.items():
     if name in [R+'id',R+'embed',R+'link'] and val in rels:
      rr=rels[val]
      if rr.get('member','') and rr['member'].startswith('word/media/'):
       asset=next((i.get('asset') for f in figs for i in f.get('images',[]) if i.get('relationship_id')==val and part=='word/document.xml'),None)
       previews.append({'relationship_id':val,'member':rr['member'],'sha256':sha(z.read(rr['member'])) if rr['member'] in z.namelist() else None,'asset':asset})
   objects.append({'part':part,'relationship_id':rid,'member':r.get('member'),'target':r.get('target'),'target_mode':r.get('mode'),'object_attributes':dict(obj.attrib),'program_id':obj.get('ProgID'),'object_type':obj.get('Type'),'source_locator':locator,'xml_path':tree.getpath(obj),'heading_path':heading,'figure_id':figure,'previews':previews,'activation':'not-activated'})
 natives=[]
 for member in members:
  b=z.read(member);h=sha(b);dest=root/kb.area(s['domain'])/'assets'/sid/'native-embeddings'/PurePosixPath(member).name
  dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists() and sha(dest.read_bytes())!=h:raise ValueError('Native output collision '+str(dest))
  if not dest.exists():dest.write_bytes(b)
  usages=[o for o in objects if o['member']==member];natives.append({'source_id':sid,'parent_sha256':s['sha256'],'archive_member':member,'sha256':h,'size_bytes':len(b),'format':dest.suffix.lower().lstrip('.'),'asset':dest.relative_to(root).as_posix(),'occurrences':usages,'relationships':[r for r in relsall if r['member']==member],'disposition':'native-original-retained','activation':'not-activated','review_status':'needs-review','limitations':(['No enclosing OLE object matched; relationship record retained.'] if not usages else [])+['Native application rendering not performed. Existing picture preview is linked where supplied; equivalence to all native pages/layers is not yet established.']})
  canonical=root/'shared/reference/native-assets'/(h+'.md')
  if canonical.exists():
   meta,_=kb.metadata(canonical)
   if meta.get('manual_curated'):
    natives[-1].update(review_status=meta['review_status'],disposition=meta.get('disposition','native-original-retained'),canonical_reference=canonical.relative_to(root).as_posix(),limitations=meta.get('limitations',[]),issue_ids=meta.get('issue_ids',[]),review_date=meta.get('review_date'),review_basis='Maintained canonical native-object metadata; source identity unchanged.')
 result={'source_id':sid,'source_sha256':s['sha256'],'source_occurrences':s['occurrences'],'native_member_count':len(members),'ole_object_count':len(objects),'native_members':natives,'objects':objects,'scan_date':'2026-11-09','timezone':'Europe/Warsaw','disposition':'native-originals-preserved' if members else 'no-native-embedding-members','limitations':['Native objects are preserved without activation. Native pages, layers, and editing-only content require format-specific inspection before complete semantic equivalence can be claimed.'] if members else []}
 kb.dump(root/'work/documents'/sid/'native-embeddings.json',result)
 page=root/s['set_path']/'documents'/sid/'native-embeddings.md';rows=[]
 for n in natives:
  loc='; '.join(o['source_locator'] for o in n['occurrences']) or 'relationship-only; enclosing object unresolved';prev=[]
  for o in n['occurrences']:
   for p in o['previews']:
    if p['asset']:prev.append(kb.link(page,root/p['asset'],p['member']))
  rows.append([kb.link(page,root/n['asset'],n['archive_member']),str(n['size_bytes']),n['sha256'],loc,', '.join(sorted(set(o['program_id'] or '' for o in n['occurrences']))),'; '.join(dict.fromkeys(prev)) or 'No matched preview','Retained; not activated'])
 meta={'template':False,'document_kind':'source-native-assets','review_status':'needs-review','domain':s['domain'],'source_ids':[sid],'source_locations':[{'source_id':sid,'locator':'DOCX package word/embeddings/* and associated *.rels; every XML part scanned for o:OLEObject'}],'native_member_count':len(natives),'limitations':result['limitations']}
 body='# Native embedded originals\n\n'+kb.source_link(root,page,s)+'. All '+str(len(members))+' native embedding members are retained byte-for-byte; SHA-256 values were checked against their DOCX package members. They are constituent source assets, not separately supplied publications.\n\n'
 body+=kb.table(['Native original / package member','Bytes','SHA-256','Source location','Embedded program label','Supplied picture preview','Disposition'],rows) if rows else 'No members under `word/embeddings/` occur in this DOCX. All XML parts were also scanned for OLE objects.\n'
 body+='\n## Interpretation and limitations\n\nNative files were not activated or executed. Picture previews may show only one native page or view. Their presence does not prove that hidden layers, other native pages or embedded application data contain no additional substantive material. The full member/relationship/object/preview mapping is in '+kb.link(page,root/'work/documents'/sid/'native-embeddings.json','machine-readable evidence')+'.\n';
 if not page.exists() or not kb.metadata(page)[0].get('manual_curated'):kb.put(page,kb.front(meta)+body)
 print(json.dumps({'source_id':sid,'native_members':len(natives),'ole_objects':len(objects)}),flush=True)
 return result

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',default='.');ap.add_argument('--source',action='append');a=ap.parse_args();root=Path(a.root).resolve()
 for s in kb.sources(root):
  if s['format']=='docx' and (not a.source or s['source_id'] in a.source):inspect(root,s)
 reports=[load(p,{}) for p in sorted((root/'work/documents').glob('*/native-embeddings.json'))];native=[n for r in reports for n in r['native_members']];ids={}
 for n in native:ids.setdefault(n['sha256'],[]).append({'source_id':n['source_id'],'member':n['archive_member'],'asset':n['asset']})
 kb.dump(root/'catalog/docx-native-embeddings.json',{'sources':reports,'summary':{'docx_sources_scanned':len(reports),'native_members':len(native),'unique_native_bytes':len(ids),'ole_objects':sum(r['ole_object_count'] for r in reports),'unmapped_native_members':sum(not n['occurrences'] for n in native),'reviewed_native_occurrences':sum(n.get('review_status')=='reviewed' for n in native),'needs_review_native_occurrences':sum(n.get('review_status')=='needs-review' for n in native)},'identities':[{'sha256':h,'occurrences':oc} for h,oc in sorted(ids.items())]})
 print(json.dumps({'complete':True,'sources':len(reports),'native_members':len(native),'unique_bytes':len(ids)}))
if __name__=='__main__':main()
