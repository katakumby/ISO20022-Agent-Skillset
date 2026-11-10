"""Extract complete supplied XSD declarations to focused, namespace-scoped pages.

This helper preserves literal declaration XML and every schema node/attribute.
It checks compilation without retrieving missing dependencies. It never supplies
business meaning from element abbreviations. Review is separate from extraction.
"""
import argparse, collections, hashlib, json, re
from pathlib import Path
from lxml import etree as E
from kb import XS, DATE, sources, read_source, put, dump, front, table, link, source_link, area
import kb, refresh

def qn(value,node):
 if not value:return None
 if ':' in value:
  p,n=value.split(':',1);return '{'+node.nsmap.get(p,'UNRESOLVED:'+p)+'}'+n
 return '{'+(node.nsmap.get(None) or '')+'}'+value
def lname(n):return E.QName(n).localname if isinstance(n.tag,str) else 'comment'
def symbol_space(n):
 return 'type' if lname(n) in ['simpleType','complexType'] else lname(n)
def reference_space(attribute,node):
 if attribute in ['type','base','itemType','memberTypes']:return 'type'
 if attribute=='substitutionGroup':return 'element'
 return lname(node)
def path(n):
 parts=[]
 while n is not None and isinstance(n.tag,str):
  tag=lname(n);siblings=[x for x in n.getparent() if isinstance(x.tag,str) and x.tag==n.tag] if n.getparent() is not None else []
  parts.append('xs:'+tag+("[@name='"+n.get('name')+"']" if n.get('name') else ('['+str(siblings.index(n)+1)+']' if len(siblings)>1 else '')));n=n.getparent()
 return '/'+('/'.join(reversed(parts)))
def defaults(n,schema):
 t=lname(n);out={}
 if t in ['element','sequence','choice','all','group','any'] and n.getparent() is not schema:
  for k in ['minOccurs','maxOccurs']:
   if k not in n.attrib:out[k]='1 (effective default)'
 if t=='element':
  if 'nillable' not in n.attrib:out['nillable']='false (effective default)'
  if 'form' not in n.attrib and n.getparent() is not schema and not n.get('ref'):out['form']=schema.get('elementFormDefault','unqualified')+' (schema/default)'
 if t=='attribute':
  if 'use' not in n.attrib:out['use']='optional (effective default)'
  if 'form' not in n.attrib and n.getparent() is not schema and not n.get('ref'):out['form']=schema.get('attributeFormDefault','unqualified')+' (schema/default)'
 if t in ['any','anyAttribute']:
  if 'namespace' not in n.attrib:out['namespace']='##any (effective default)'
  if 'processContents' not in n.attrib:out['processContents']='strict (effective default)'
 return out
def extract(root,s):
 data=read_source(root,s)
 if hashlib.sha256(data).hexdigest()!=s['sha256']:raise ValueError('Source changed: '+s['source_id'])
 schema=E.fromstring(data,E.XMLParser(resolve_entities=False,no_network=True,remove_blank_text=False));ns=schema.get('targetNamespace');mid=s['message_ids'][0] if s['message_ids'] else None
 if not mid:return {'source_id':s['source_id'],'message_id':None,'components':[],'compile_result':'dependency-only','limitations':['Reusable schema declarations are published with their selected owning message.']}
 canonical,conflicts=kb.canonical_schemas(root)
 if mid not in canonical or canonical[mid]['source_id']!=s['source_id']:raise ValueError('Conflicting exact definition '+mid)

 folder=root/area(s['domain'])/'reference/messages'/mid
 existing=folder/'schema-coverage.json';previous=None;preserve_existing=False
 if existing.exists():
  previous=json.loads(existing.read_text())
  if previous.get('sha256')==s['sha256']:
   preserve_existing=True
   required=[folder/'index.md',folder/'structure.md']+[root/c['path'] for c in previous.get('components',[])]
   if previous.get('helper_version')==3 and previous.get('compile_result')=='pass' and not previous.get('dependencies') and all(p.exists() for p in required):return previous
  if previous.get('sha256')!=s['sha256']:raise ValueError('Conflicting exact definition '+mid)
 def write_page(page,text):
  if not preserve_existing or not page.exists():put(page,text)
 declarations=[n for n in schema if isinstance(n.tag,str) and lname(n) not in ['annotation','import','include','redefine','override']]
 anonymous=[n for n in schema.iter() if isinstance(n.tag,str) and lname(n) in ['simpleType','complexType'] and n.getparent() is not schema]
 components=declarations+anonymous
 page_for={id(n):folder/'types'/f'type-{i:04d}.md' for i,n in enumerate(components,1)}
 names={ (symbol_space(n),'{'+(ns or '')+'}'+n.get('name')):n for n in declarations if n.get('name')}
 references=collections.defaultdict(list)
 for n in schema.iter():
  if not isinstance(n.tag,str):continue
  for k in ['type','base','ref','itemType','substitutionGroup','memberTypes']:
   for v in n.get(k,'').split():references[(reference_space(k,n),qn(v,n))].append((path(n),n.sourceline,k))
 dependencies=[{'kind':lname(n),'attributes':dict(n.attrib),'line':n.sourceline,'path':path(n)} for n in schema if isinstance(n.tag,str) and lname(n) in ['import','include','redefine','override']]
 try:
  refresh.SuppliedSchemaResolver(root,sources(root)).compile(s);compile_result='pass';compile_error=None
 except (E.XMLSchemaParseError,OSError,ValueError) as exc:compile_result='fail';compile_error=str(exc)
 nodes=[n for n in schema.iter() if isinstance(n.tag,str)]
 counts=dict(collections.Counter(lname(n) for n in nodes))
 index=[]
 for i,n in enumerate(components,1):
  page=page_for[id(n)];identity='{'+(ns or '')+'}'+n.get('name') if n.get('name') else path(n);kind=lname(n)
  annotation=[' '.join(''.join(x.itertext()).split()) for x in n.findall('.//{'+XS+'}documentation')]
  meta={'template':False,'document_kind':'schema-type','review_status':'needs-review','domain':s['domain'],'message_id':mid,'message_family':'.'.join(mid.split('.')[:2]),'type_id':f'type-{i:04d}','type_kind':kind,'qname_or_schema_path':identity,'namespace':ns,'source_ids':[s['source_id']],'source_editions':[s['source_edition']] if s['source_edition'] else [],'schema_path':path(n),'source_line':n.sourceline,'limitations':['Business semantics require MDR evidence; mechanical extraction is not visual or editorial review.']}
  text=front(meta)+'# '+(n.get('name') or 'Anonymous '+kind)+'\n\n'
  text+='## Identity and provenance\n\n'+source_link(root,page,s)+'; target namespace `'+str(ns)+'`; declaration `'+identity+'`; `'+path(n)+'`, line '+str(n.sourceline)+'.\n\n'
  text+='## Source annotations\n\n'+('\n\n'.join(annotation) if annotation else 'No xs:documentation annotation is present in this declaration. This does not establish absence of business rules in MDR documentation.')+'\n\n'
  text+='## Complete compositor, member and restriction reference\n\nRows preserve XML preorder and enclosing paths. A choice selects among its alternatives subject to both group and member occurrences; its members are not independently required. Literal attributes and effective defaults occupy separate columns. Facets and enumeration values below are schema constraints.\n\n'
  rows=[]
  for child in n.iter():
   if not isinstance(child.tag,str):continue
   refs=[]
   for attr in ['type','base','ref','itemType','memberTypes','substitutionGroup']:
    for val in child.get(attr,'').split():
     q=qn(val,child);target=names.get((reference_space(attr,child),q))
     refs.append(attr+' = '+(link(page,page_for[id(target)],q) if target is not None else '`'+str(q)+'`'))
   attrs='`'+json.dumps(dict(child.attrib),ensure_ascii=False)+'`'
   rows.append([lname(child),path(child),attrs,json.dumps(defaults(child,schema),ensure_ascii=False),'; '.join(refs),str(child.sourceline)])
  text+=table(['Construct / order','Schema path / enclosing group','Literal attributes','Effective omitted defaults','Resolved references','Source line'],rows)
  text+='## Literal declaration\n\nThe following source fragment preserves annotations, order, facets, defaults, fixed values, identity constraints, wildcards and other supplied constructs exactly at the XML data-model level. Indentation and namespace declarations may be serialized by the XML parser.\n\n```xml\n'+E.tostring(n,encoding='unicode',pretty_print=True).strip()+'\n```\n\n'
  used=references.get((symbol_space(n),identity),[])
  text+='## Reuse and recursion\n\n'+(table(['Referencing schema path','Line','Attribute'],used) if used else 'No incoming named reference was found in this supplied schema.\n\n')
  if n.get('name','').startswith('External'):text+='The external type name is not a current code-set enumeration. Consult the separately versioned '+link(page,root/'shared/reference/code-sets','code publications')+'.\n\n'
  text+='## Review and navigation\n\n'+link(page,folder/'structure.md','Structure and type index')+' · '+link(page,folder/'index.md','Message')+' · '+link(page,root/'tracking/issues.md','Open issues')+'\n\nDeclaration extraction includes every descendant node and attribute. Schema compilation: **'+compile_result+'** using lxml '+E.LXML_VERSION.__str__()+' / libxml2 '+E.LIBXML_VERSION.__str__()+' on '+DATE+'. Business and visual checks remain separate.\n'
  write_page(page,text)
  index.append({'id':f'type-{i:04d}','name':n.get('name'),'qname':identity,'kind':kind,'schema_path':path(n),'line':n.sourceline,'path':page.relative_to(root).as_posix(),'node_count':sum(1 for c in n.iter() if isinstance(c.tag,str))})
 root_elements=schema.findall('{'+XS+'}element')
 msgname=None
 for el in root_elements:
  target=names.get(('type',qn(el.get('type'),el)))
  if target is not None and el.get('name')=='Document':
   inner=target.find('.//{'+XS+'}element')
   if inner is not None:msgname=inner.get('type') or inner.get('name')
  elif target is not None:msgname=el.get('type')
 msgname=msgname or mid
 coverage={'helper_version':3,'source_id':s['source_id'],'sha256':s['sha256'],'message_id':mid,'namespace':ns,'message_name':msgname,'domain':s['domain'],'set_path':s['set_path'],'counts':counts,'top_level_declarations':len(declarations),'anonymous_types':len(anonymous),'components':index,'dependencies':dependencies,'compile_result':compile_result,'compile_error':compile_error,'review_status':'needs-review','date':DATE,'all_nodes_preserved':sum(c['node_count'] for c in index)>=len(nodes)-1,'limitations':['MDR business content is reviewed independently.','Source tables and figures are not reconciled by schema extraction.']}
 dep_coverage=publish_dependencies(root,folder,s)
 coverage['dependency_coverage']=dep_coverage
 if previous and preserve_existing:
  coverage['review_status']=previous.get('review_status','needs-review')
  coverage={**previous,**coverage}
 dump(folder/'schema-coverage.json',coverage)
 page=folder/'structure.md'
 m={'template':False,'document_kind':'message-structure','review_status':'needs-review','domain':s['domain'],'message_id':mid,'message_family':'.'.join(mid.split('.')[:2]),'namespace':ns,'source_ids':[s['source_id']],'source_editions':[s['source_edition']] if s['source_edition'] else []}
 text=front(m)+'# '+mid+' structure\n\n'+source_link(root,page,s)+'; `'+ns+'`, `/xs:schema`, line 1.\n\n'
 text+='## Namespace and roots\n\n'+table(['Property','Source value'],list(schema.attrib.items()))
 text+=table(['Root','Type','Line'],[[e.get('name'),qn(e.get('type'),e),e.sourceline] for e in root_elements])
 text+='## Dependencies\n\n'+(table(['Kind','Attributes','Line'],[[d['kind'],json.dumps(d['attributes']),d['line']] for d in dependencies]) if dependencies else 'No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.\n\n')
 if dep_coverage:text+='## Supplied dependency declarations\n\n'+table(['Source','Namespace','Reference'],[[d['source_id'],d['namespace'],link(page,root/d['index'],'Complete declarations')] for d in dep_coverage])+'\n'
 text+='## Effective schema defaults\n\nUnless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.\n\n'
 text+='## Complete declaration and type index\n\n'+table(['Page','Kind','QName / anonymous path','Source line'],[[link(page,root/c['path'],c['id']),c['kind'],c['qname'],c['line']] for c in index])
 text+='## Coverage\n\n'+table(['Construct','Supplied count'],sorted(counts.items()))
 text+='Compilation: **'+compile_result+'**. '+(compile_error or 'All supplied declarations compile locally; no network schema retrieval was performed.')+'\n\n'+link(page,folder/'schema-coverage.json','Machine-readable declaration coverage')+' · '+link(page,folder/'index.md','Message')+'\n'
 write_page(page,text)
 page=folder/'index.md'
 m.update(document_kind='message-index',message_name=msgname,business_area=mid[:4],message_version=mid.split('.')[-1],message_sets=[s['set_slug']],source_editions=[s['source_edition']] if s['source_edition'] else [],limitations=coverage['limitations'])
 text=front(m)+'# '+mid+' — '+msgname+'\n\n'
 text+='## Purpose, usage and actors\n\nThe supplied XSD establishes XML structure. Its message type name is `'+msgname+'`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.\n\n'
 text+='## Identification\n\n'+table(['Fact','Value','Evidence'],[['Exact definition',mid,source_link(root,page,s)+'; targetNamespace'],['Namespace',ns,'/xs:schema/@targetNamespace'],['Root(s)',', '.join(s['roots']),'/xs:schema/xs:element'],['Collection',s['set_title'],s['occurrences'][0]['path']]])
 text+='## References\n\n- '+link(page,folder/'structure.md','Complete structure and type index')+'\n- '+link(page,root/s['set_path']/'index.md','Message-set context, tables and diagrams')+'\n- '+link(page,root/s['set_path']/'coverage.md','Source extraction coverage')+'\n- '+link(page,root/'catalog/participants.md','Shared participants')+'\n- '+link(page,root/'catalog/flows.md','Business flows')+'\n- '+link(page,root/'tracking/source-register.md','Source identities and original occurrences')+'\n- '+link(page,root/'tracking/issues.md','Known gaps and review requirements')+'\n\n'
 if (folder/'business.md').exists():text+='## Curated business reference\n\n'+link(page,folder/'business.md','Purpose, participants, flows and business rules')+'\n\n'
 text+='## Review\n\nComplete supplied schema declarations have focused pages with literal XML, qualified references and nested paths. Automated schema compilation: **'+compile_result+'**. Extraction is **needs-review**; this does not claim that source documentation, tables or diagrams have passed visual review.\n'
 write_page(page,text)
 return coverage

def publish_dependencies(root,folder,source):
 resolver=refresh.SuppliedSchemaResolver(root,sources(root));seen={source['source_id']};outputs=[]
 def walk(s):
  data=read_source(root,s);tree=E.fromstring(data,E.XMLParser(resolve_entities=False,no_network=True))
  for node in tree:
   if not isinstance(node.tag,str) or lname(node) not in ['import','include','redefine','override']:continue
   dep=resolver.dependency(s,node.get('schemaLocation'),node.get('namespace'))
   if not dep or dep['source_id'] in seen:continue
   seen.add(dep['source_id']);dt=E.fromstring(read_source(root,dep),E.XMLParser(resolve_entities=False,no_network=True))
   base=folder/'dependencies'/dep['source_id'];pg=base/'index.md';ns=dt.get('targetNamespace')
   components=[]
   decls=[n for n in dt if isinstance(n.tag,str) and lname(n) not in ['annotation','import','include','redefine','override']]
   decls += [n for n in dt.iter() if isinstance(n.tag,str) and lname(n) in ['simpleType','complexType'] and n.getparent() is not dt]
   for i,n in enumerate(decls,1):
    out=base/'types'/f'type-{i:04d}.md'
    meta={'template':False,'document_kind':'schema-type','review_status':'needs-review','domain':source['domain'],
      'source_ids':[dep['source_id']],'namespace':ns,'schema_path':path(n),'source_line':n.sourceline,
      'qname_or_schema_path':('{'+str(ns)+'}'+n.get('name')) if n.get('name') else path(n)}
    rows=[[lname(c),path(c),json.dumps(dict(c.attrib)),json.dumps(defaults(c,dt)),c.sourceline] for c in n.iter() if isinstance(c.tag,str)]
    body=front(meta)+'# '+(n.get('name') or 'Anonymous '+lname(n))+'\n\n'+source_link(root,out,dep)+'; '+str(ns)+'; '+path(n)+'.\n\n'
    body+=table(['Construct / ordering','Declaration path','Literal attributes','Effective defaults','Line'],rows)
    body+='\n'+chr(96)*3+'xml\n'+E.tostring(n,encoding='unicode').strip()+'\n'+chr(96)*3+'\n\n'+link(out,pg,'Dependency declarations')+'\n'
    if not out.exists():put(out,body)
    components.append({'path':out.relative_to(root).as_posix(),'schema_path':path(n),'kind':lname(n),'line':n.sourceline})
   meta={'template':False,'document_kind':'schema-dependency','review_status':'needs-review','domain':source['domain'],'source_ids':[dep['source_id']],'namespace':ns}
   body=front(meta)+'# Supplied schema dependency '+dep['source_id']+'\n\n'+source_link(root,pg,dep)+'; namespace '+str(ns)+'.\n\n'
   body+=table(['Declaration','Schema path'],[[link(pg,root/c['path'],Path(c['path']).stem),c['schema_path']] for c in components])
   body+='\n'+link(pg,folder/'structure.md','Owning message structure')+'\n'
   if not pg.exists():put(pg,body)
   entry={'source_id':dep['source_id'],'sha256':dep['sha256'],'namespace':ns,'index':pg.relative_to(root).as_posix(),'components':components}
   dump(base/'coverage.json',entry);outputs.append(entry);walk(dep)
 walk(source);return outputs

def main():
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--message');p.add_argument('--collection')
 p.add_argument('--source',action='append');p.add_argument('--job');a=p.parse_args();root=a.root.resolve()
 if a.job:kb.set_write_context(root,a.job)
 a.source=refresh.job_sources(root,a.job,a.source)
 group=[s for s in sources(root) if s['format']=='xsd' and (not a.source or s['source_id'] in a.source) and (not a.message or any(m.startswith(a.message) for m in s['message_ids'])) and (not a.collection or s['collection']==a.collection)]
 order={c:i for i,c in enumerate(kb.COLLECTIONS)};group.sort(key=lambda s:(order.get(s['collection'],99),s['source_id']))
 results=[];blocked=[]
 for source in group:
  try:
   result=extract(root,source);results.append(result)
  except (ValueError,OSError) as exc:blocked.append({'source_id':source['source_id'],'message_ids':source.get('message_ids',[]),'error':str(exc)})
 output={'date':DATE,'messages':len(results),'components':sum(len(c['components']) for c in results),'failures':[c['message_id'] for c in results if c['compile_result'] not in ('pass','dependency-only')],'blocked':blocked,'results':[{'source_id':c.get('source_id'),'message_id':c['message_id'],'compile_result':c['compile_result']} for c in results]}
 dest=root/'tracking/refresh'/a.job/'schema-extraction.json' if a.job else root/'work/schema-extraction-summary.json'
 dump(dest,output);print(json.dumps(output))
if __name__=='__main__':main()
