"""Build focused conceptual-component pages from supplied FullBusinessModel sheets.

Usage: python tools/index_business_components.py --root REPOSITORY
Requires extract_workbooks.py output. Original workbooks and archive members are
re-hashed; sources remain read-only. Complete exact A:F component-row content is
the deduplication key. Names alone never merge definitions. This is a conceptual
business model index, not a schema or participant conversion.
"""
import argparse,collections,gc,hashlib,json,os,re,shutil
from pathlib import Path
from zipfile import ZipFile
DATE='2026-11-08'
AP=argparse.ArgumentParser();AP.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);A=AP.parse_args();R=A.root.resolve()
SOURCE_LIST=json.loads((R/'catalog/sources.json').read_text(encoding='utf8'))['sources'];SOURCES={s['source_id']:s for s in SOURCE_LIST}
OUT=R/'shared/reference/business-components';OUT.mkdir(parents=True,exist_ok=True)
def dump(x):return json.dumps(x,ensure_ascii=False,indent=2)
def front(**kw):return '---\n'+'\n'.join(k+': '+json.dumps(v,ensure_ascii=False) for k,v in {'template':False,'review_status':'needs-review',**kw}.items())+'\n---\n\n'
def rel(p,t):return os.path.relpath(t,p.parent).replace('\\','/')
def link(p,t,label):return '['+str(label).replace('[','\\[').replace(']','\\]')+'](<'+rel(p,t)+'>)'
def esc(v):return '∅' if v is None else str(v).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','\\|').replace('\r\n','\n').replace('\r','\n').replace('\n','<br>')
def write(p,text):
 p=Path(p).resolve();assert p.is_relative_to(R) and not p.is_relative_to(R/'raw-input')
 p.parent.mkdir(parents=True,exist_ok=True);data=text.encode('utf8')
 if p.exists():
  old=p.read_bytes()
  if old==data:return
  backup=R/'tracking/history/job-000001'/(DATE+'-business-components')/p.relative_to(R)
  if not backup.exists():backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(old)
 p.write_bytes(data)
def source_bytes(s):
 o=s['occurrences'][0];p=R/o['path']
 if o.get('archive_member'):
  with ZipFile(p) as z:b=z.read(o['archive_member'])
 else:b=p.read_bytes()
 assert hashlib.sha256(b).hexdigest()==s['sha256'],'Source bytes changed: '+s['source_id']
 return b
def original(p,s):
 return '; '.join(link(p,R/o['path'],s['source_id']+' original')+(' archive member `'+o['archive_member']+'`' if o.get('archive_member') else '') for o in s['occurrences'])
def ranges(numbers):
 numbers=sorted(numbers);out=[]
 for n in numbers:
  if out and out[-1][1]+1==n:out[-1][1]=n
  else:out.append([n,n])
 return ['A'+str(a)+':F'+str(b) for a,b in out]
def cell_content(cell):
 if cell is None:return {'value':None}
 # Formatting-only style IDs are not semantic; preserve actual number formats,
 # formulas and cached/typed values. Coordinates differ between occurrences.
 return {k:cell[k] for k in ['value','storage_type','number_format','displayed_or_typed_value','formula','cached_value'] if k in cell}
COMPONENTS={};WORKBOOKS=[];ISSUES=[]
for file in sorted((R/'work/workbooks').glob('*/workbook.json')):
 data=json.loads(file.read_text(encoding='utf8'));sid=data['source_id'];source=SOURCES[sid]
 assert data['sha256']==source['sha256'],'Stale workbook extraction '+sid
 sheets=[sh for sh in data['sheets'] if sh['name'].replace(' ','').lower()=='fullbusinessmodel']
 if not sheets:
  WORKBOOKS.append({'source_id':sid,'disposition':'no-fullbusinessmodel-sheet','sheets':[]});del data;gc.collect();continue
 source_bytes(source)
 w={'source_id':sid,'source_sha256':source['sha256'],'disposition':'indexed-needs-review','sheets':[]}
 for sh in sheets:
  grid=collections.defaultdict(dict)
  for cell in sh['cells']:
   m=re.fullmatch(r'([A-Z]+)([0-9]+)',cell['cell'])
   if m and m[1] in 'ABCDEF' and len(m[1])==1:grid[int(m[2])][m[1]]=cell
  content_rows={rn:cells for rn,cells in grid.items() if any(c.get('value') is not None or c.get('formula') is not None for c in cells.values())}
  headers=[rn for rn,cells in content_rows.items() if cells.get('A',{}).get('value')=='Business Component Name' and cells.get('B',{}).get('value')=='Business Element Name']
  if len(headers)!=1:ISSUES.append({'source_id':sid,'sheet':sh['name'],'problem':'Expected one exact A/B component header','header_rows':headers});continue
  header=headers[0]
  expected_headers=['Business Component Name','Business Element Name','Business Component Parent Name','Documentation','Business Element Type Name','Name of Opposite End']
  if [grid[header].get(c,{}).get('value') for c in 'ABCDEF']!=expected_headers:
   ISSUES.append({'source_id':sid,'sheet':sh['name'],'problem':'Unexpected six-column schema; source column ordering must be inspected'});continue
  groups=collections.OrderedDict();unowned=[]
  for rn,cells in sorted(content_rows.items()):
   if rn==header:continue
   name=cells.get('A',{}).get('value')
   if not isinstance(name,str) or not name:
    unowned.append(rn);continue
   groups.setdefault(name,[]).append((rn,[cell_content(cells.get(c)) for c in 'ABCDEF']))
  local={};items=[]
  for name,records in groups.items():
   semantic=[cells for rn,cells in records];raw=json.dumps(semantic,ensure_ascii=False,separators=(',',':'),sort_keys=True).encode('utf8');sha=hashlib.sha256(raw).hexdigest();bid='bc-'+sha[:20]
   if bid in COMPONENTS:assert COMPONENTS[bid]['sha256']==sha,'Content ID prefix collision'
   else:COMPONENTS[bid]={'id':bid,'name':name,'sha256':sha,'rows':semantic,'occurrences':[]}
   occ={'source_id':sid,'sheet':sh['name'],'row_numbers':[rn for rn,cells in records],'ranges':ranges([rn for rn,cells in records]),'row_count':len(records)}
   COMPONENTS[bid]['occurrences'].append(occ);local[name]=bid
   items.append({'id':bid,'name':name,'path':(OUT/(bid+'.md')).relative_to(R).as_posix(),'sha256':sha,**occ})
  total=sum(i['row_count'] for i in items)
  assert total+len(unowned)==len(content_rows)-1,'Source row accounting mismatch'
  if unowned:ISSUES.append({'source_id':sid,'sheet':sh['name'],'problem':'Nonblank component rows lack explicit component name','rows':unowned})
  w['sheets'].append({'name':sh['name'],'state':sh['state'],'header_row':header,'header_values':[grid[header].get(c,{}).get('value') for c in 'ABCDEF'],'row_count_with_content':len(content_rows),'blank_or_formatting_only_rows':sorted(set(grid)-set(content_rows)),'components':items,'local_names':local,'component_rows':total,'unowned_rows':unowned,'reconciled':not unowned})
 WORKBOOKS.append(w);print(sid,'components',sum(len(s['components']) for s in w['sheets']),'rows',sum(s['component_rows'] for s in w['sheets']),flush=True);del data;gc.collect()
CONTEXT={(w['source_id'],s['name']):s for w in WORKBOOKS for s in w['sheets']}
for bid,c in sorted(COMPONENTS.items()):
 p=OUT/(bid+'.md');sids=sorted({o['source_id'] for o in c['occurrences']});domains=sorted({SOURCES[s]['domain'] for s in sids});sets=sorted({SOURCES[s]['set_slug'] for s in sids});editions=sorted({SOURCES[s]['source_edition'] for s in sids if SOURCES[s].get('source_edition')})
 rows=[[cell.get('value') for cell in cells] for cells in c['rows']]
 parents=sorted({v[2] for v in rows if v[2] is not None});fields=[v for v in rows if v[1] is not None];defs=[v[3] for v in rows if v[1] is None and v[3] is not None]
 locations=[{'source_id':o['source_id'],'worksheet':o['sheet'],'ranges':o['ranges']} for o in c['occurrences']]
 limitations=['Conceptual business model; not an XML type, database definition or institutional participant assignment.','Cardinalities, composition and ownership are not inferred from this six-column table.','Same-name components with different complete row content remain separate.','Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.']
 text=front(document_kind='business-concept',concept_id=bid,title=c['name'],business_component_name=c['name'],aliases=[],domain='shared',domains=domains,message_sets=sets,applicability='source-publication-provenance; message usage requires Traces evidence',source_ids=sids,source_editions=editions,source_locations=locations,content_sha256=c['sha256'],parent_names=parents,related_component_names=sorted({v[4] for v in fields if isinstance(v[4],str)}),limitations=limitations)+'# '+c['name']+'\n\n'
 text+='## Definition\n\n'+('\n\n'.join(defs) if defs else 'No standalone component definition was located in this component’s rows. This is a missing definition, not confirmed absence of meaning.')+'\n\n'
 text+='## Complete component rows\n\n`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.\n\n| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |\n| --- | --- | --- | --- | --- | --- | --- |\n'
 for i,v in enumerate(rows,1):text+='| '+str(i)+' | '+' | '.join(esc(x) for x in v)+' |\n'
 specials=[(i,j,cell) for i,cells in enumerate(c['rows'],1) for j,cell in enumerate(cells) if cell.get('formula') is not None]
 if specials:
  text+='\n### Formula and cached-value evidence\n\nFormulas are not recalculated.\n\n| Row ordinal | Column | Formula | Cached value | Displayed/typed value | Number format |\n| --- | --- | --- | --- | --- | --- |\n'
  for i,j,cell in specials:text+='| '+' | '.join(map(esc,[i,'ABCDEF'[j],cell.get('formula'),cell.get('cached_value'),cell.get('displayed_or_typed_value'),cell.get('number_format')]))+' |\n'
 text+='\n## Provenance and all equivalent occurrences\n\nComplete row-content SHA-256: `'+c['sha256']+'`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.\n\n| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |\n| --- | --- | --- | --- | --- |\n'
 for o in c['occurrences']:
  s=SOURCES[o['source_id']];wp=R/s['set_path']/'workbooks'/s['source_id']/'components.md'
  text+='| '+' | '.join([o['source_id'],esc(o['sheet'])+'!'+', '.join(o['ranges']),', '.join(map(str,o['row_numbers'])),original(p,s),link(p,wp,'Lookup')])+' |\n'
 text+='\n## Parent and field-type relationships by source context\n\nTargets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.\n\n| Source | Relationship | Source row/cell | Referenced name | Same-source target |\n| --- | --- | --- | --- | --- |\n'
 relationships=[]
 for o in c['occurrences']:
  lookup=CONTEXT[(o['source_id'],o['sheet'])]['local_names']
  for i,v in enumerate(rows):
   for col,kind,name in [('C','parent',v[2]),('E','field-type',v[4])]:
    if not isinstance(name,str) or not name:continue
    target=lookup.get(name);record={'source_id':o['source_id'],'worksheet':o['sheet'],'cell':col+str(o['row_numbers'][i]),'kind':kind,'name':name,'target_id':target};relationships.append(record)
    text+='| '+' | '.join([o['source_id'],kind,record['cell'],esc(name),link(p,OUT/(target+'.md'),name) if target else 'Not a component record in this worksheet'])+' |\n'
 text+='\n## Interpretation and review\n\n'+'\n'.join('- '+l for l in limitations)+'\n\nThe presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.\n\n'+link(p,OUT/'index.md','Business-component index')+' · '+link(p,R/'tracking/issues.md','Known limitations and issues')+'\n'
 write(p,text);c['relationships']=relationships;c['parent_names']=parents;c['source_ids']=sids;c['path']=p.relative_to(R).as_posix()
INDEX=[]
for bid,c in sorted(COMPONENTS.items(),key=lambda x:(x[1]['name'],x[0])):INDEX.append({k:c[k] for k in ['id','name','sha256','path','source_ids','parent_names','occurrences','relationships']})
write(OUT/'index.json',dump({'schema_version':1,'date':DATE,'components':INDEX}))
p=OUT/'index.md';text='# Conceptual business-component index\n\nEach row resolves to one complete structured-content identity. Repeated names may have distinct supplied definitions. These are business concepts, not automatically participants or XML types.\n\n| Component | Content identity | Sources | Review status |\n| --- | --- | --- | --- |\n'
for c in INDEX:text+='| '+link(p,R/c['path'],c['name'])+' | `'+c['id']+'` | '+', '.join(c['source_ids'])+' | needs-review |\n'
write(p,text)
for w in WORKBOOKS:
 if not w['sheets']:continue
 s=SOURCES[w['source_id']];base=R/s['set_path']/'workbooks'/s['source_id'];p=base/'components.md'
 text=front(document_kind='business-component-index',domain=s['domain'],source_ids=[s['source_id']],source_editions=[s['source_edition']] if s.get('source_edition') else [])+'# '+s['set_title']+' conceptual components\n\n'+original(p,s)+'\n\n'
 for sh in w['sheets']:
  text+='## '+sh['name']+'\n\n'+str(sh['component_rows'])+' nonblank component rows are assigned exactly once to '+str(len(sh['components']))+' complete component occurrences. Header row '+str(sh['header_row'])+' is retained as schema context; '+str(len(sh['blank_or_formatting_only_rows']))+' blank/formatting-only rows are separately accounted.\n\n| Component | Source range | Canonical content identity |\n| --- | --- | --- |\n'
  for c in sh['components']:text+='| '+link(p,R/c['path'],c['name'])+' | '+', '.join(c['ranges'])+' | `'+c['id']+'` |\n'
 text+='\n'+link(p,base/'index.md','Workbook evidence')+' · '+link(p,OUT/'index.md','All component identities')+'\n';write(p,text)
 public={k:v for k,v in w.items() if k!='sheets'};public['sheets']=[{k:v for k,v in sh.items() if k!='local_names'} for sh in w['sheets']];write(base/'components.json',dump(public))
 # Add an idempotent navigation link without replacing workbook extraction evidence.
 p=base/'index.md';t=p.read_text(encoding='utf8');start='<!-- BUSINESS-COMPONENTS-START -->';end='<!-- BUSINESS-COMPONENTS-END -->';block=start+'\n\n[Focused conceptual business components](components.md) · [Machine-readable component lookup](components.json)\n\n'+end
 t=re.sub(re.escape(start)+'.*?'+re.escape(end),lambda m:block,t,flags=re.S) if start in t else t+'\n\n'+block+'\n';write(p,t)
coverage={'date':DATE,'source_workbooks_scanned':len(WORKBOOKS),'source_workbooks_with_components':sum(bool(w['sheets']) for w in WORKBOOKS),'canonical_complete_component_identities':len(COMPONENTS),'component_occurrences':sum(len(sh['components']) for w in WORKBOOKS for sh in w['sheets']),'component_rows':sum(sh['component_rows'] for w in WORKBOOKS for sh in w['sheets']),'all_nonblank_rows_assigned':not ISSUES,'issues':ISSUES,'workbooks':[{'source_id':w['source_id'],'disposition':w['disposition'],'sheets':[{k:v for k,v in sh.items() if k not in ['components','local_names']} for sh in w['sheets']]} for w in WORKBOOKS],'limitations':['Row-equivalence validation does not resolve contradictions with workbook drawings or provide missing component definitions.','Differing content identities are retained; no version-comparison conclusions are generated.']}
write(R/'tracking/reviews/business-components.json',dump(coverage));print(dump({k:v for k,v in coverage.items() if k!='workbooks'}))
