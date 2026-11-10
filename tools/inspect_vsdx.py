#!/usr/bin/env python3
"""Inspect supplied VSDX parts statically, without activating native objects.
Usage: python tools/inspect_vsdx.py --root PATH
Preserves page boundaries, shape IDs/text/cells, connectors and native members.
"""
from pathlib import Path
from collections import defaultdict
import argparse, hashlib, json, posixpath, zipfile
from lxml import etree
import kb
V='http://schemas.microsoft.com/office/visio/2012/main';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships';NS={'v':V,'r':R}
def local(n):return etree.QName(n).localname
def parse(z,p):return etree.fromstring(z.read(p))
def text(n):return ''.join(n.itertext())
def records(z,part):
 d=parse(z,part);out=[]
 for sh in d.findall('.//{'+V+'}Shape'):
  tx=sh.find('{'+V+'}Text');cells=[]
  for c in sh.iter():
   if local(c)=='Cell':
    nearest=next((a for a in c.iterancestors() if local(a)=='Shape'),None)
    if nearest is sh:cells.append({'xml_path':c.getroottree().getpath(c),'attributes':dict(c.attrib),'text':text(c)})
  out.append({'shape_attributes':dict(sh.attrib),'xml_path':sh.getroottree().getpath(sh),'text':text(tx) if tx is not None else None,'text_xml':etree.tostring(tx,encoding='unicode') if tx is not None else None,'cells':cells})
 return {'part':part,'shapes':out,'connectors':[dict(x.attrib) for x in d.findall('.//{'+V+'}Connect')],'page_sheet_cells':[dict(c.attrib) for c in d.findall('./{'+V+'}PageSheet//{'+V+'}Cell')]}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',default='.');a=ap.parse_args();root=Path(a.root).resolve();catalog=json.loads((root/'catalog/docx-native-embeddings.json').read_text(encoding='utf-8'));src={s['source_id']:s for s in kb.sources(root)};groups=defaultdict(list)
 for s in catalog['sources']:
  for n in s['native_members']:
   if n['format']=='vsdx':groups[n['sha256']].append(n)
 summary=[]
 for h,occ in groups.items():
  first=occ[0];s=src[first['source_id']];native=root/first['asset']
  if hashlib.sha256(native.read_bytes()).hexdigest()!=h:raise ValueError('native mismatch')
  z=zipfile.ZipFile(native);work=root/'work/native-vsdx'/h;work.mkdir(parents=True,exist_ok=True)
  manifest=[]
  for name in z.namelist():
   if name.endswith('/'):continue
   b=z.read(name);p=(work/name).resolve()
   if work.resolve() not in p.parents:raise ValueError('Unsafe package path')
   p.parent.mkdir(parents=True,exist_ok=True)
   if not p.exists():p.write_bytes(b)
   manifest.append({'member':name,'sha256':hashlib.sha256(b).hexdigest(),'size_bytes':len(b),'extracted_path':p.relative_to(root).as_posix()})
  pagesdoc=parse(z,'visio/pages/pages.xml');rels=parse(z,'visio/pages/_rels/pages.xml.rels');relmap={x.get('Id'):posixpath.normpath(posixpath.join('visio/pages',x.get('Target'))) for x in rels};pages=[]
  base=root/s['set_path']/'documents'/s['source_id']/'native-diagrams'/native.stem.lower().replace('_','-').replace(' ','-')
  for idx,p in enumerate(pagesdoc.findall('{'+V+'}Page'),1):
   rn=p.find('{'+V+'}Rel');part=relmap[rn.get('{'+R+'}id')];r=records(z,part);r['page_attributes']=dict(p.attrib);r['page_number']=idx
   dest=base/f'page-{idx:04d}.md';r['output']=dest.relative_to(root).as_posix();pages.append(r)
   meta={'template':False,'document_kind':'native-diagram-evidence','review_status':'needs-review','content_origin':'source-extraction','domain':s['domain'],'source_ids':sorted(set(n['source_id'] for n in occ)),'source_locations':[{'source_id':n['source_id'],'locator':n['archive_member']+' / '+part+'; '+o['source_locator']} for n in occ for o in n['occurrences']],'native_sha256':h,'limitations':['Static XML extraction only; native rendering and comparison with supplied picture preview outstanding (issue-000028). Shape/master references and geometry cells are retained without inferring missing visual semantics.'],'issue_ids':['issue-000028']}
   body='# Native Visio page '+str(idx)+': '+p.get('Name','')+'\n\n'+kb.link(dest,native,'Preserved native VSDX')+'; '+kb.link(dest,work/part,'complete page XML')+'. Page attributes: `'+json.dumps(dict(p.attrib),ensure_ascii=False)+'`.\n\n## Shapes and text\n\n'
   body+=kb.table(['Native shape ID','Name / nameU','Type / master / master-shape','Exact text'],[[r['shape_attributes'].get('ID',''),r['shape_attributes'].get('Name','')+' / '+r['shape_attributes'].get('NameU',''),json.dumps({k:r['shape_attributes'][k] for k in ['Type','Master','MasterShape'] if k in r['shape_attributes']}),r['text'] if r['text'] is not None else '(no local Text element)'] for r in r['shapes']])
   body+='\n## Explicit connector records\n\n'+kb.table(['From sheet','From cell / part','To sheet','To cell / part','All supplied attributes'],[[c.get('FromSheet',''),c.get('FromCell','')+' / '+c.get('FromPart',''),c.get('ToSheet',''),c.get('ToCell','')+' / '+c.get('ToPart',''),json.dumps(c,ensure_ascii=False)] for c in r['connectors']])
   body+='\n## Native details and limits\n\nAll local shape cells, formulas, geometry, nested-shape paths, exact rich-text XML, and page-sheet cells are retained in '+kb.link(dest,work/'inspection.json','inspection record')+'. Native master definitions and package relationships are retained in the extracted package; inherited visual details require master resolution. Connector endpoints are native shape references, not automatically business message directions. No source-to-preview equivalence or visual review is claimed.\n';kb.put(dest,kb.front(meta)+body)
  masters=[records(z,p) for p in z.namelist() if p.startswith('visio/masters/master') and p.endswith('.xml') and '/_rels/' not in p and posixpath.basename(p)!='masters.xml'];report={'native_sha256':h,'occurrences':occ,'pages':pages,'masters':masters,'package_members':manifest,'review_status':'needs-review','issue_ids':['issue-000028'],'inspection_date':'2026-11-09','timezone':'Europe/Warsaw'};kb.dump(work/'inspection.json',report)
  entry={'native_sha256':h,'occurrences':len(occ),'page_count':len(pages),'shape_count':sum(len(p['shapes']) for p in pages),'connector_count':sum(len(p['connectors']) for p in pages),'master_parts':len(masters),'report':(work/'inspection.json').relative_to(root).as_posix(),'page_outputs':[p['output'] for p in pages]};summary.append(entry)
  for n in occ:
   ss=src[n['source_id']];p=root/ss['set_path']/'documents'/ss['source_id']/'native-embeddings.md';m,b=kb.metadata(p);m['issue_ids']=['issue-000028'];marker='\n## Static VSDX evidence: '+Path(n['asset']).name+'\n\n'
   if marker not in b:b+=marker+'Byte-identical native content is inspected once, preserving every parent-document occurrence. '+', '.join(kb.link(p,root[pp] if False else root/pp,'Native page '+str(i+1)) for i,pp in enumerate(entry['page_outputs']))+'. This preserves '+str(entry['shape_count'])+' native shapes and '+str(entry['connector_count'])+' explicit connector records; visual equivalence remains unverified (issue-000028).\n'
   kb.put(p,kb.front(m)+b)
  print(json.dumps(entry),flush=True)
 kb.dump(root/'catalog/vsdx-static-inspection.json',{'unique_native_files':len(summary),'native_occurrences':sum(x['occurrences'] for x in summary),'native_pages':sum(x['page_count'] for x in summary),'inspections':summary,'review_status':'needs-review','issue_ids':['issue-000028']})
if __name__=='__main__':main()
