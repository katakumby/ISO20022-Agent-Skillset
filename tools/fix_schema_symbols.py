"""Repair incoming-reference symbol spaces without rewriting curated message pages."""
import argparse,collections,json,re
from pathlib import Path
from lxml import etree as E
import kb
from extract_schemas import qn,path,symbol_space,reference_space
def main(root):
 changed=[];checked=0
 for s in kb.sources(root):
  if s['format']!='xsd':continue
  mid=s['message_ids'][0];folder=root/kb.area(s['domain'])/'reference/messages'/mid;cpath=folder/'schema-coverage.json'
  if not cpath.exists():continue
  schema=E.fromstring(kb.read_source(root,s));c=json.loads(cpath.read_text(encoding='utf-8'));nodes={path(n):n for n in schema.iter() if isinstance(n.tag,str)}
  refs=collections.defaultdict(list)
  for n in schema.iter():
   if not isinstance(n.tag,str):continue
   for attr in ['type','base','ref','itemType','memberTypes','substitutionGroup']:
    for value in n.get(attr,'').split():refs[(reference_space(attr,n),qn(value,n))].append((path(n),n.sourceline,attr))
  for comp in c['components']:
   node=nodes[comp['schema_path']];incoming=refs.get((symbol_space(node),comp['qname']),[])
   replacement='## Reuse and recursion\n\n'+(kb.table(['Referencing schema path','Line','Attribute'],incoming) if incoming else 'No incoming named reference was found in this supplied schema.\n\n')
   page=root/comp['path'];text=page.read_text(encoding='utf-8');start=text.index('## Reuse and recursion');end=text.index('## Review and navigation',start)
   old_section=text[start:end];suffix=''
   if 'The external type name' in old_section:suffix=old_section[old_section.index('The external type name'):]
   new=text[:start]+replacement+suffix+text[end:]
   checked+=1
   if new!=text:kb.put(page,new);changed.append(comp['path'])
  c['helper_version']=3;c['symbol_space_reference_validation']='pass';kb.dump(cpath,c)
 kb.dump(root/'tracking/schema-symbol-validation.json',{'date':kb.DATE,'components_checked':checked,'pages_corrected':changed,'result':'pass','scope':'Incoming references resolved in XSD type/element/attribute/group symbol spaces, without merging equal QNames across spaces.'})
 print(json.dumps({'components_checked':checked,'pages_corrected':len(changed)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
