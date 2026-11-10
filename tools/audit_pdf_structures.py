"""Bounded, resumable Part2 PDF geometry and extracted-table audit.

This helper does not certify visual review. It preserves every unclassified painted
object and text discrepancy, leaves the earlier lexical figure inventory intact,
and writes source-scoped audit shards. Only --render-pages writes page PNGs.
"""
import argparse,collections,ctypes,datetime,hashlib,json,re,time,unicodedata
from pathlib import Path
import pypdfium2 as pdfium
import kb
DATE='2026-11-09'
EXCLUDE={'src-000011','src-000012','src-000349'}
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def normalize(s):return ''.join(unicodedata.normalize('NFKC',s or '').split())
def inside(a,b,tol=1.6):return a[0]>=b[0]-tol and a[1]>=b[1]-tol and a[2]<=b[2]+tol and a[3]<=b[3]+tol
def source_tables(root,sid):return json.loads((root/'work/documents'/sid/'tables.json').read_text(encoding='utf-8'))
def path_info(o,height):
 matrix=o.get_matrix();a,b,c,d,e,f=matrix.get();points=[];types=[];closes=[]
 for n in range(pdfium.raw.FPDFPath_CountSegments(o)):
  seg=pdfium.raw.FPDFPath_GetPathSegment(o,n);x=ctypes.c_float();y=ctypes.c_float()
  if not pdfium.raw.FPDFPathSegment_GetPoint(seg,x,y):raise ValueError('Path point unavailable')
  types.append(pdfium.raw.FPDFPathSegment_GetType(seg));points.append([a*x.value+c*y.value+e,height-(b*x.value+d*y.value+f)]);closes.append(bool(pdfium.raw.FPDFPathSegment_GetClose(seg)))
 fill=ctypes.c_int();stroke=ctypes.c_int();pdfium.raw.FPDFPath_GetDrawMode(o,fill,stroke)
 axis=bool(points) and all(t in (0,2) for t in types)
 for i in range(1,len(points)):
  if types[i]==2:continue
  if abs(points[i][0]-points[i-1][0])>0.05 and abs(points[i][1]-points[i-1][1])>0.05:axis=False
 if closes and closes[-1] and abs(points[-1][0]-points[0][0])>0.05 and abs(points[-1][1]-points[0][1])>0.05:axis=False
 rect=axis and len(points) in (4,5) and len({round(x,2) for x,y in points})==2 and len({round(y,2) for x,y in points})==2
 line=axis and len(points)==2 and types==[2,0]
 return {'segments':len(points),'segment_types':types,'points':[[round(v,4) for v in z] for z in points],'closed_segments':closes,'axis_aligned':axis,'axis_line':line,'axis_rectangle':rect,'fill_mode':fill.value,'stroke':bool(stroke.value)}
def classify_paths(page,tables):
 h=page.get_height();w=page.get_width();counts=collections.Counter();unresolved=[];pathhash=[];objects=collections.Counter();all_objects=list(page.get_objects(max_depth=15));textboxes=[];underline_evidence=[]
 for ordinal,o in enumerate(all_objects,1):
  if o.type==pdfium.raw.FPDF_PAGEOBJ_TEXT:
   b=o.get_bounds();textboxes.append((ordinal,[b[0],h-b[3],b[2],h-b[1]]))
 for ordinal,o in enumerate(all_objects,1):
  objects[str(o.type)]+=1
  if o.type==pdfium.raw.FPDF_PAGEOBJ_TEXT:continue
  box=o.get_bounds();box=[box[0],h-box[3],box[2],h-box[1]];record={'object_ordinal':ordinal,'object_type':o.type,'form_depth':o.level,'bbox':[round(z,4) for z in box]}
  if o.type!=pdfium.raw.FPDF_PAGEOBJ_PATH:record['disposition']='unclassified-nontext-object';unresolved.append(record);counts[record['disposition']]+=1;continue
  p=path_info(o,h);record.update(p);pathhash.append(record);matched=[t for t in tables if inside(box,t['bbox'])]
  # Narrow horizontal page furniture only; contextual visual exemplars remain required.
  annotation=None
  if p['axis_line'] and box[3]-box[1]<=1.1:
   annot=pdfium.raw.FPDFLink_GetLinkAtPoint(page,(box[0]+box[2])/2,h-(box[1]+box[3])/2)
   if annot:
    ar=pdfium.raw.FS_RECTF()
    if pdfium.raw.FPDFLink_GetAnnotRect(annot,ar):
     ab=[ar.left,h-ar.top,ar.right,h-ar.bottom]
     if inside(box,ab):annotation=[round(z,4) for z in ab]
  if matched and p['axis_line']:kind='table-associated-axis-line'
  elif matched and p['axis_rectangle'] and p['fill_mode']!=0:kind='table-associated-filled-rectangle'
  elif annotation:kind='link-annotation-underline';underline_evidence.append({'path_object_ordinal':ordinal,'bbox':record['bbox'],'link_annotation_bbox':annotation})
  elif p['axis_line'] and box[3]-box[1]<=1.1 and box[2]-box[0]>=w*0.7 and (box[3]<60 or box[1]>h-70):kind='margin-rule-template-candidate'
  elif p['axis_line'] and box[3]-box[1]<=1.1 and (under:=[(i,t) for i,t in textboxes if abs(t[0]-(box[0]+0.5))<=4.5 and abs(t[2]-(box[2]-0.5))<=4.5 and abs(t[3]-(box[1]+0.5))<=2.6]):
   kind='text-underline-template-candidate';underline_evidence.append({'path_object_ordinal':ordinal,'bbox':record['bbox'],'matched_text_object_ordinals':[i for i,t in under]})
  else:kind='unclassified-painted-path'
  counts[kind]+=1
  if kind.startswith('unclassified'):record.update(disposition=kind,overlapping_table_ids=[x['table_id'] for x in matched]);unresolved.append(record)
 return {'painted_object_counts':dict(objects),'path_classes':dict(counts),'painted_geometry_sha256':digest(pathhash),'underline_geometry_evidence':underline_evidence,'unclassified_objects':unresolved}
def check_table(root,table,tp,h):
 p=root/table['output'];meta,body=kb.metadata(p) if p.exists() else ({},'');rows=table['rows'];width=max(map(len,rows),default=0);expected=kb.table([f'Source cell {i+1}' for i in range(width)],[r+['']*(width-len(r)) for r in rows]);markdown='pass' if expected in body else 'differs-or-missing';xs=sorted(set(round(c[0],4) for c in table['cells']));ys=sorted(set(round(c[1],4) for c in table['cells']));cells={(round(c[0],4),round(c[1],4)):c for c in table['cells']};errors=[];matched=0;spans=0;tested=0
 if len(ys)!=len(rows) or any(len(row)!=len(xs) for row in rows):errors.append({'kind':'grid-mapping-uncertain','x_positions':len(xs),'y_positions':len(ys),'row_widths':sorted(set(map(len,rows)))})
 else:
  for ri,row in enumerate(rows):
   for ci,value in enumerate(row):
    cell=cells.get((xs[ci],ys[ri]));loc={'row':ri+1,'column':ci+1}
    if cell is None:
     spans+=1
     if value is not None:errors.append({**loc,'kind':'non-null-value-without-independent-cell','stored_value':value})
     continue
    a,b,c,d=cell;actual=tp.get_text_bounded(a+0.01,h-d+0.01,c-0.01,h-b-0.01);tested+=1
    if normalize(value)==normalize(actual):matched+=1
    else:
     kind='pdfium-soft-hyphen-control-difference' if normalize(value)==normalize(actual.replace('\x02','-')) else 'independent-text-difference'
     errors.append({**loc,'kind':kind,'bbox':cell,'stored_value':value,'pdfium_value':actual})
 return {'table_id':table['table_id'],'file_page':table['page'],'bbox':table['bbox'],'output':table['output'],'rows':len(rows),'matrix_cells':sum(map(len,rows)),'physical_cells':len(table['cells']),'span_null_positions':spans,'cell_matrix_sha256':digest(rows),'cell_geometry_sha256':digest(table['cells']),'markdown_cell_preservation':markdown,'output_has_manual_visual_review':meta.get('table_cells_visual_review'),'independent_cells_checked':tested,'independent_cells_match':matched,'exceptions':errors,'review_status':'needs-review'}
def audit(root,s,force=False,start=None,end=None,refresh_markdown=False):
 sid=s['source_id'];work=root/'work/documents'/sid;out=work/'structural-audit';summary=out/'summary.json';data=kb.read_source(root,s)
 if hashlib.sha256(data).hexdigest()!=s['sha256']:raise ValueError('Source fingerprint changed')
 tables=source_tables(root,sid);by_page=collections.defaultdict(list)
 for t in tables:by_page[t['page']].append(t)
 doc=pdfium.PdfDocument(data);begin=start or 1;finish=end or len(doc);out.mkdir(parents=True,exist_ok=True);done=0;t0=time.time()
 for pi in range(begin,min(finish,len(doc))+1):
  dest=out/f'page-{pi:05d}.json'
  if dest.exists() and not force:
   old=json.loads(dest.read_text(encoding='utf-8'))
   if old.get('source_sha256')==s['sha256'] and old.get('method_version')==3:
    if refresh_markdown:
     originals={t['table_id']:t for t in by_page[pi]}
     for checked in old['tables']:
      t=originals[checked['table_id']];rows=t['rows'];width=max(map(len,rows),default=0);expected=kb.table([f'Source cell {i+1}' for i in range(width)],[r+['']*(width-len(r)) for r in rows]);path=root/t['output'];checked['markdown_cell_preservation']='pass' if path.exists() and expected in path.read_text(encoding='utf-8') else 'differs-or-missing'
     old['markdown_check_date']=DATE;kb.dump(dest,old)
    continue
  page=doc[pi-1];tp=page.get_textpage();geometry=classify_paths(page,by_page[pi]);checks=[check_table(root,t,tp,page.get_height()) for t in by_page[pi]];record={'source_id':sid,'source_sha256':s['sha256'],'file_page':pi,'method_version':3,'date':DATE,'page_size':[page.get_width(),page.get_height()],**geometry,'tables':checks,'visual_review':'not-run'};kb.dump(dest,record);tp.close();page.close();done+=1
  if done%200==0:print(json.dumps({'source_id':sid,'new_pages_audited':done,'file_page':pi,'total':len(doc),'elapsed_seconds':round(time.time()-t0,1)}),flush=True)
 rows=[];counts=collections.Counter();tc=collections.Counter();unknown=[];exceptions=[];markdown=[];samples={}
 for pi in range(1,len(doc)+1):
  path=out/f'page-{pi:05d}.json'
  if not path.exists():continue
  p=json.loads(path.read_text(encoding='utf-8'));counts.update(p['path_classes']);rows.append({'file_page':pi,'path_classes':p['path_classes'],'table_count':len(p['tables']),'audit':path.relative_to(root).as_posix()});signature=','.join(sorted(p['path_classes'])) or 'no-painted-path';samples.setdefault(signature,pi)
  if p['unclassified_objects']:unknown.append({'file_page':pi,'count':len(p['unclassified_objects']),'audit':path.relative_to(root).as_posix()})
  for t in p['tables']:
   tc.update({'tables':1,'matrix_cells':t['matrix_cells'],'physical_cells':t['physical_cells'],'span_null_positions':t['span_null_positions'],'independent_cells_checked':t['independent_cells_checked'],'independent_cells_match':t['independent_cells_match']})
   if t['markdown_cell_preservation']!='pass':markdown.append({'table_id':t['table_id'],'file_page':pi,'output':t['output']})
   if t['exceptions']:
    counts_e=collections.Counter(x['kind'] for x in t['exceptions']);exceptions.append({'table_id':t['table_id'],'file_page':pi,'output':t['output'],'exception_kinds':dict(counts_e),'audit':path.relative_to(root).as_posix()})
 report={'source_id':sid,'source_sha256':s['sha256'],'date':DATE,'method_version':3,'pages_total':len(doc),'pages_audited':len(rows),'complete_page_enumeration':len(rows)==len(doc),'tables_in_prior_inventory':len(tables),'table_counts':dict(tc),'painted_path_classes':dict(counts),'unclassified_pages':unknown,'text_exception_tables':exceptions,'markdown_cell_discrepancies':markdown,'visual_exemplar_candidates':[{'signature':k,'file_page':v} for k,v in samples.items()],'pages':rows,'review_status':'needs-review','limitations':['Geometric association with a table is not independent semantic review of its contents. All original lexical vector candidates remain available.','PDFium omits unpainted clipping paths from its painted-object list; unsupported image/form/shading objects and non-axis paths remain unresolved.','Cell text comparison normalizes only Unicode compatibility and whitespace, preserving case, digits and punctuation. Soft-hyphen control differences remain explicit exceptions.','Span/null positions preserve missing separate extracted cells; their semantics require original page/table context.','No claim that each page or each cell has been individually visually inspected. Text-only diagrams and source-level semantic ambiguities are outside this mechanical classification.']};kb.dump(summary,report);doc.close();print(json.dumps({k:report[k] for k in ['source_id','pages_audited','pages_total','table_counts','painted_path_classes']}),flush=True);return report
def aggregate(root):
 reports=[]
 for p in sorted((root/'work/documents').glob('*/structural-audit/summary.json')):
  r=json.loads(p.read_text(encoding='utf-8'));reports.append({k:v for k,v in r.items() if k not in ['pages','text_exception_tables','unclassified_pages']}|{'summary':p.relative_to(root).as_posix(),'unclassified_page_count':len(r['unclassified_pages']),'text_exception_table_count':len(r['text_exception_tables'])})
 kb.dump(root/'catalog/pdf-structural-audit.json',{'date':DATE,'method':'PDFium painted-object geometry and independent bounded cell text; maintained Markdown matrix comparison','records':reports,'review_status':'needs-review'})
def render(root,s,pages,dpi):
 data=kb.read_source(root,s)
 if hashlib.sha256(data).hexdigest()!=s['sha256']:raise ValueError('Changed source')
 doc=pdfium.PdfDocument(data);out=root/kb.area(s['domain'])/'assets'/s['source_id']/'structural-audit';out.mkdir(parents=True,exist_ok=True)
 for pi in pages:
  page=doc[pi-1];dest=out/f'page-{pi:05d}.png';bitmap=page.render(scale=dpi/72);bitmap.to_pil().save(dest);bitmap.close();page.close();kb.dump(dest.with_suffix('.json'),{'source_id':s['source_id'],'source_sha256':s['sha256'],'file_page':pi,'dpi':dpi,'renderer':'pypdfium2/PDFium','asset':dest.relative_to(root).as_posix(),'image_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'visual_review':'not-run'})
 doc.close()
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--source',action='append');ap.add_argument('--force',action='store_true');ap.add_argument('--refresh-markdown',action='store_true');ap.add_argument('--start-page',type=int);ap.add_argument('--end-page',type=int);ap.add_argument('--render-pages',type=int,nargs='+');ap.add_argument('--dpi',type=int,default=120);ap.add_argument('--aggregate-only',action='store_true');a=ap.parse_args();root=a.root.resolve()
 if not a.aggregate_only:
  for s in kb.sources(root):
   if s['format']!='pdf' or s['source_id'] in EXCLUDE or a.source and s['source_id'] not in a.source:continue
   if a.render_pages:render(root,s,a.render_pages,a.dpi)
   else:audit(root,s,a.force,a.start_page,a.end_page,a.refresh_markdown)
 aggregate(root)
if __name__=='__main__':main()
