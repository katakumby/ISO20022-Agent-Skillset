#!/usr/bin/env python3
"""Inventory/preserve all DOCX SmartArt graph, drawing, layout and style parts.
Usage: python tools/inspect_docx_smartart.py --root PATH [--source SOURCE]
Static evidence extraction only. Does not reconstruct or review figure semantics.
"""
from pathlib import Path
import argparse,hashlib,io,json,posixpath,zipfile
from lxml import etree
import kb
D='http://schemas.openxmlformats.org/drawingml/2006/diagram';A='http://schemas.openxmlformats.org/drawingml/2006/main';R='http://schemas.openxmlformats.org/officeDocument/2006/relationships';W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';NS={'dgm':D,'a':A,'w':W}
def h(b):return hashlib.sha256(b).hexdigest()
def load(p,default):return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default
def resolve(p,t):return posixpath.normpath(posixpath.join(posixpath.dirname(p),t)).lstrip('/')
def inspect(root,s):
 sid=s['source_id'];data=kb.read_source(root,s)
 if h(data)!=s['sha256']:raise ValueError('Source checksum changed')
 z=zipfile.ZipFile(io.BytesIO(data));names=set(z.namelist());parts=sorted(n for n in names if n.startswith('word/diagrams/') and not n.endswith('/'));rec=load(root/'work/documents'/sid/'records.json',{});figs=rec.get('figures',[]);occ=[];members=[]
 for part in sorted(n for n in names if n.startswith('word/') and n.endswith('.xml') and '/_rels/' not in n and not n.startswith('word/diagrams/')):
  rp=posixpath.join(posixpath.dirname(part),'_rels',posixpath.basename(part)+'.rels')
  if rp not in names:continue
  rels={r.get('Id'):{'target':r.get('Target'),'type':r.get('Type'),'mode':r.get('TargetMode'),'member':None if r.get('TargetMode')=='External' else resolve(part,r.get('Target',''))} for r in etree.fromstring(z.read(rp))};doc=etree.fromstring(z.read(part))
  for el in doc.findall('.//{'+D+'}relIds'):
   refs={etree.QName(k).localname:{'relationship_id':v,**rels.get(v,{})} for k,v in el.attrib.items()};loc=part+' '+el.getroottree().getpath(el);figid=None;head=[]
   ancestor=next((a for a in el.iterancestors() if a.getparent() is not None and a.getparent().tag=='{'+W+'}body'),None)
   if part=='word/document.xml' and ancestor is not None:
    kind=etree.QName(ancestor).localname;i=1+sum(a.tag==ancestor.tag for a in ancestor.itersiblings(preceding=True));xp='/w:document/w:body/w:'+kind+'['+str(i)+']';loc=('direct-body paragraph P' if kind=='p' else 'direct-body table T')+str(i)
    fs=[f for f in figs if f.get('xml_path')==xp]
    if fs:figid=fs[0]['figure_id'];head=fs[0]['heading_path']
   occ.append({'part':part,'source_locator':loc,'xml_path':el.getroottree().getpath(el),'figure_id':figid,'heading_path':head,'relationships':refs})
 for name in parts:
  b=z.read(name);rel=name.removeprefix('word/diagrams/');dest=(root/kb.area(s['domain'])/'assets'/sid/'smartart-originals'/rel).resolve();assetroot=(root/kb.area(s['domain'])/'assets'/sid/'smartart-originals').resolve()
  if assetroot not in dest.parents:raise ValueError('Unsafe member path')
  dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists() and h(dest.read_bytes())!=h(b):raise ValueError('Asset collision')
  if not dest.exists():dest.write_bytes(b)
  members.append({'member':name,'sha256':h(b),'size_bytes':len(b),'asset':dest.relative_to(root).as_posix()})
 graphs=[]
 for name in sorted(n for n in parts if posixpath.basename(n).startswith('data') and n.endswith('.xml') and '/_rels/' not in n):
  doc=etree.fromstring(z.read(name));nodes=[]
  for pt in doc.findall('.//{'+D+'}pt'):
   paragraphs=[''.join(t.itertext()) for t in pt.findall('./{'+D+'}t/{'+A+'}p')];pr=pt.find('{'+D+'}prSet');nodes.append({'attributes':dict(pt.attrib),'property_set_attributes':dict(pr.attrib) if pr is not None else {},'text_paragraphs':paragraphs,'text':'\n'.join(paragraphs),'xml_path':pt.getroottree().getpath(pt),'xml':etree.tostring(pt,encoding='unicode')})
  edges=[{'attributes':dict(c.attrib),'xml_path':c.getroottree().getpath(c)} for c in doc.findall('.//{'+D+'}cxn')];uses=[o for o in occ if any(r.get('member')==name for r in o['relationships'].values())];page=root/s['set_path']/'documents'/sid/'smartart'/(Path(name).stem+'.md');graph={'source_id':sid,'data_part':name,'sha256':h(z.read(name)),'points':nodes,'connections':edges,'occurrences':uses,'output':page.relative_to(root).as_posix(),'disposition':'graph-extracted-needs-visual-review'};graphs.append(graph)
  m={'template':False,'document_kind':'smartart-evidence','review_status':'needs-review','content_origin':'source-extraction','domain':s['domain'],'source_ids':[sid],'source_locations':[{'source_id':sid,'locator':o['source_locator']+' / '+name} for o in uses] or [{'source_id':sid,'locator':name}],'limitations':['SmartArt graph data and all layout/drawing/style parts are preserved. Graph relationships are native presentation structure, not independently established business-message directions. Complete rendered figure and semantic reconstruction require visual comparison.']}
  orig=next(x['asset'] for x in members if x['member']==name);body='# SmartArt graph: '+Path(name).name+'\n\n'+kb.source_link(root,page,s)+'; '+kb.link(page,root/orig,'unchanged data XML')+'.\n\n## Point labels and identities\n\n'+kb.table(['Point model ID','Type','Exact text paragraphs','All attributes','Property-set attributes'],[[n['attributes'].get('modelId',''),n['attributes'].get('type','(omitted)'),n['text'],json.dumps(n['attributes'],ensure_ascii=False),json.dumps(n['property_set_attributes'],ensure_ascii=False)] for n in nodes])+'\n## Native connections\n\n'+kb.table(['Connection model ID','Type','Source point','Destination point','All attributes'],[[e['attributes'].get('modelId',''),e['attributes'].get('type','(omitted)'),e['attributes'].get('srcId',''),e['attributes'].get('destId',''),json.dumps(e['attributes'],ensure_ascii=False)] for e in edges])+'\n## Source occurrences and limits\n\n'
  for o in uses:
   body+='- '+o['source_locator']+'; '+(' / '.join(o['heading_path']))+'; '+(kb.link(page,root/s['set_path']/'documents'/sid/'diagrams'/(o['figure_id']+'.md'),o['figure_id']) if o['figure_id'] else 'No existing figure ID matched')+'.\n'
  body+='\nEvery point, property, layout relationship, connection order and original XML remains available in '+kb.link(page,root/'work/documents'/sid/'smartart.json','static evidence')+'. This page is an extraction, not a reviewed Mermaid reconstruction.\n';kb.put(page,kb.front(m)+body)
 report={'source_id':sid,'source_sha256':s['sha256'],'source_occurrences':s['occurrences'],'diagram_part_count':len(parts),'data_model_count':len(graphs),'smartart_occurrence_count':len(occ),'members':members,'graphs':graphs,'occurrences':occ,'scan_date':'2026-11-09','timezone':'Europe/Warsaw','review_status':'needs-review' if parts else 'not-applicable'};kb.dump(root/'work/documents'/sid/'smartart.json',report)
 print(json.dumps({'source_id':sid,'parts':len(parts),'graphs':len(graphs),'occurrences':len(occ)}),flush=True)
 return report

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',default='.');ap.add_argument('--source',action='append');a=ap.parse_args();root=Path(a.root).resolve()
 for s in kb.sources(root):
  if s['format']=='docx' and (not a.source or s['source_id'] in a.source):inspect(root,s)
 reports=[load(p,{}) for p in sorted((root/'work/documents').glob('*/smartart.json'))];kb.dump(root/'catalog/docx-smartart-inventory.json',{'sources':reports,'summary':{'sources_scanned':len(reports),'diagram_parts':sum(r['diagram_part_count'] for r in reports),'data_models':sum(r['data_model_count'] for r in reports),'smartart_occurrences':sum(r['smartart_occurrence_count'] for r in reports)}})
if __name__=='__main__':main()
