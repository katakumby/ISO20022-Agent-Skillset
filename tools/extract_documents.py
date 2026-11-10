"""Read-only source extraction into focused evidence pages and a working inventory.

Uses catalog source identities. Source bytes are verified before extraction. No raw-input
file is written. Extracted evidence remains needs-review until visual reconciliation.
Run with bundled Python: tools/extract_documents.py --root PATH --format docx|pdf
Use --source src-NNNNNN for a bounded source and --pdf-tables for line-based table candidates.
"""
from __future__ import annotations
import argparse,hashlib,io,json,logging,re,sys,zipfile,os,shutil,datetime
from pathlib import Path
from collections import Counter
from lxml import etree as E
import kb

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W,'a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','v':'urn:schemas-microsoft-com:vml'}
ID=re.compile(r'[a-z]{4}\.\d{3}\.\d{3}\.\d{2,}')
DATE=kb.DATE
PRESERVE_EXISTING=False
logging.getLogger('pypdf').setLevel(logging.ERROR)

def write_page(root,page,text):
 if page.exists() and PRESERVE_EXISTING:return
 if page.exists():
  oldmeta,_=kb.metadata(page)
  if oldmeta.get('manual_curated') or oldmeta.get('review_status')=='reviewed' or oldmeta.get('table_cells_visual_review')=='pass' or oldmeta.get('canonical_diagram'):return
  old=page.read_text(encoding='utf-8-sig')
  if old==text:return
 kb.put(page,text)

def plain(node):
 return ''.join((x.text or '') if x.tag=='{'+W+'}t' else '\n' if x.tag in ['{'+W+'}br','{'+W+'}cr'] else '\t' if x.tag=='{'+W+'}tab' else '' for x in node.iter())
def metadata(s,kind,**extra):
 return dict(template=False,document_kind=kind,review_status='needs-review',domain=s['domain'],message_set=s['set_title'],source_ids=[s['source_id']],source_editions=[s.get('source_edition')],message_ids=s.get('message_ids',[]),**extra)
def checked_bytes(root,s):
 b=kb.read_source(root,s)
 if hashlib.sha256(b).hexdigest()!=s['sha256']:raise ValueError('Source checksum changed: '+s['source_id'])
 return b

def source_intro(root,page,s,locator):
 return 'Source: '+kb.source_link(root,page,s)+'. Locator: '+locator+'.\n\n'

def docx(root,s,data):
 sid=s['source_id']; out=root/s['set_path']/'documents'/sid;work=root/'work/documents'/sid; assets=root/kb.area(s['domain'])/'assets'/sid/'originals'
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  r=E.fromstring(z.read('word/document.xml'));tree=r.getroottree();body=r.find('w:body',NS)
  styles={}
  if 'word/styles.xml' in z.namelist():
   st=E.fromstring(z.read('word/styles.xml'))
   for x in st.findall('w:style',NS):
    nm=x.find('w:name',NS);styles[x.get('{'+W+'}styleId')]=nm.get('{'+W+'}val') if nm is not None else ''
  rels={}
  if 'word/_rels/document.xml.rels' in z.namelist():
   rr=E.fromstring(z.read('word/_rels/document.xml.rels'))
   rels={x.get('Id'):x.get('Target') for x in rr}
  media=[]
  for n in z.namelist():
   if n.startswith('word/media/') and not n.endswith('/'):
    b=z.read(n);dest=assets/Path(n).name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
    media.append({'archive_member':n,'path':dest.relative_to(root).as_posix(),'sha256':hashlib.sha256(b).hexdigest(),'disposition':'pending-visual-classification'})
  records=[];paragraphs=[];tables=[];figures=[];headings=[];pidx=0;tidx=0;fidx=0
  def figrecord(el,locator,heading):
   nonlocal fidx
   blocks=el.xpath('.//w:drawing | .//w:pict | .//w:object',namespaces=NS)
   if not blocks:return
   fidx+=1; rids=el.xpath('.//a:blip/@r:embed | .//v:imagedata/@r:id',namespaces=NS)
   images=[]
   for rid in dict.fromkeys(rids):
    target=rels.get(rid,''); n='word/'+target.lstrip('/')
    if target.startswith('/'):n=target.lstrip('/')
    mediaref=next((m for m in media if m['archive_member']==n),None)
    images.append({'relationship_id':rid,'target':target,'asset':mediaref['path'] if mediaref else None})
   fig={'figure_id':f'fig-{fidx:04d}','locator':locator,'xml_path':tree.getpath(el),'heading_path':heading.copy(),'drawing_containers':len(blocks),'images':images,'shape_text':plain(el),'disposition':'pending','render_status':'not-run','visual_review':'not-run','limitations':['Embedded assets may be only part of a composite figure. Full rendered figure and Mermaid reconstruction require visual review.']}
   figures.append(fig);records.append({'kind':'figure',**fig})
  for child in body:
   if child.tag=='{'+W+'}p':
    pidx+=1;txt=plain(child);sty=child.find('w:pPr/w:pStyle',NS);sidstyle=sty.get('{'+W+'}val') if sty is not None else '';name=styles.get(sidstyle,sidstyle)
    level=None;m=re.search(r'heading\s*([1-9])',name,re.I)
    if m:level=int(m.group(1))
    ol=child.find('w:pPr/w:outlineLvl',NS)
    if level is None and ol is not None:level=int(ol.get('{'+W+'}val'))+1
    if level and txt:headings=headings[:level-1]+[txt]
    par={'paragraph_id':f'P{pidx}','xml_path':tree.getpath(child),'text':txt,'style':name,'heading_level':level,'heading_path':headings.copy(),'message_ids':sorted(set(ID.findall(txt)))}
    paragraphs.append(par);records.append({'kind':'paragraph',**par});figrecord(child,f'direct-body paragraph P{pidx}',headings)
   elif child.tag=='{'+W+'}tbl':
    tidx+=1;rows=[];merges=[];nested=[]
    for ri,tr in enumerate(child.findall('w:tr',NS),1):
     cells=[]
     for ci,tc in enumerate(tr.findall('w:tc',NS),1):
      ps=[''.join(plain(p)) for p in tc.findall('w:p',NS)];cells.append('\n'.join(ps))
      span=tc.find('w:tcPr/w:gridSpan',NS);vm=tc.find('w:tcPr/w:vMerge',NS)
      if span is not None or vm is not None:merges.append({'row':ri,'source_cell':ci,'grid_span':int(span.get('{'+W+'}val')) if span is not None else 1,'vertical_merge':vm.get('{'+W+'}val','continue') if vm is not None else None})
      for nt in tc.findall('w:tbl',NS):nested.append({'xml_path':tree.getpath(nt),'text':plain(nt)})
      figrecord(tc,f'direct-body table T{tidx} row {ri} cell {ci}',headings)
     rows.append(cells)
    tab={'table_id':f'tbl-{tidx:04d}','source_table_id':f'T{tidx}','xml_path':tree.getpath(child),'heading_path':headings.copy(),'rows':rows,'merges':merges,'nested_tables':nested,'disposition':'converted-needs-review'}
    tables.append(tab);records.append({'kind':'table',**tab})
  # Footnotes/endnotes/comments are retained separately; table notes may depend on them.
  auxiliary=[]
  for n in ['word/footnotes.xml','word/endnotes.xml','word/comments.xml']:
   if n in z.namelist():
    rr=E.fromstring(z.read(n))
    for x in rr:auxiliary.append({'member':n,'id':x.get('{'+W+'}id'),'text':plain(x)})
  report={'source_id':sid,'format':'docx','source_sha256':s['sha256'],'source_occurrences':s['occurrences'],'paragraph_index_convention':'P indexes direct body w:p only; T indexes direct body w:tbl only; XML paths provide unambiguous location.','paragraphs':paragraphs,'tables':tables,'figures':figures,'media':media,'auxiliary':auxiliary,'records':records,'review_status':'needs-review','limitations':['DOCX pagination not rendered here. Composite diagrams and textboxes require full-page comparison.','Markdown table cells preserve physical source cells; merged-cell mappings are explicit. Blank cells are blank evidence, not zero.','Nested tables are retained as text plus XML location and require separate row reconciliation.']}
  kb.dump(work/'records.json',report)
  # Focused heading sections. Source table/figure pages remain independent.
  sections=[];cur=None
  for rec in records:
   if rec['kind']=='paragraph' and rec['heading_level'] and rec['text']:
    cur={'title':rec['text'],'heading_path':rec['heading_path'],'records':[]};sections.append(cur)
   if cur is None:cur={'title':'Publication front matter','heading_path':[],'records':[]};sections.append(cur)
   cur['records'].append(rec)
  secrows=[]
  for i,sec in enumerate(sections,1):
   p=out/'sections'/f'section-{i:04d}.md';text=kb.front(metadata(s,'source-section',heading_path=sec['heading_path'],content_origin='source-transcription'))+'# '+sec['title']+'\n\n'+source_intro(root,p,s,'heading path '+ ' / '.join(sec['heading_path']))
   text+='Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.\n\n'
   for rec in sec['records']:
    if rec['kind']=='paragraph' and rec['text']:text+='**'+rec['paragraph_id']+'** '+rec['text'].replace('\n','  \n')+'\n\n'
    elif rec['kind']=='table':text+=kb.link(p,out/'tables'/(rec['table_id']+'.md'),rec['source_table_id']+' - complete table')+'\n\n'
    elif rec['kind']=='figure':text+=kb.link(p,out/'diagrams'/(rec['figure_id']+'.md'),rec['figure_id']+' - original figure evidence')+'\n\n'
   write_page(root,p,text);secrows.append([sec['title'],kb.link(out/'index.md',p,'Section'),', '.join(r['paragraph_id'] for r in sec['records'] if r['kind']=='paragraph')])
  for tab in tables:
   p=out/'tables'/(tab['table_id']+'.md');ncol=max([len(r) for r in tab['rows']]or[0]);rows=[[i+1]+r+['']*(ncol-len(r)) for i,r in enumerate(tab['rows'])]
   text=kb.front(metadata(s,'extracted-table',table_id=tab['table_id'],heading_path=tab['heading_path'],source_locator=tab['xml_path']))+'# '+tab['table_id']+' - '+' / '.join(tab['heading_path'])+'\n\n'+source_intro(root,p,s,tab['source_table_id']+'; '+tab['xml_path'])
   text+='All physical source cells are retained, including source header rows. Generic column labels below are navigation aids; source row 1 is not assumed to be the only header. Empty strings remain blank. Original merged headers apply through the mappings below.\n\n'+kb.table(['Source row']+[f'Source cell {i+1}' for i in range(ncol)],rows)
   if tab['merges']:text+='## Merged cells\n\n'+kb.table(['Source row','Source cell','Grid span','Vertical merge'],[[m['row'],m['source_cell'],m['grid_span'],m['vertical_merge']] for m in tab['merges']])
   if tab['nested_tables']:text+='## Nested table evidence requiring reconciliation\n\n'+kb.table(['XML path','Extracted text'],[[n['xml_path'],n['text']] for n in tab['nested_tables']])
   text+='Review: row extraction complete for the direct-body table; visual comparison, note linkage, and semantic header review not run.\n';write_page(root,p,text)
  for fig in figures:
   p=out/'diagrams'/(fig['figure_id']+'.md');text=kb.front(metadata(s,'diagram-evidence',diagram_id=fig['figure_id'],content_origin='source-reconstruction-pending',render_status='not-run',visual_review='not-run',heading_path=fig['heading_path']))+'# '+fig['figure_id']+' - original figure evidence\n\n'+source_intro(root,p,s,fig['locator']+'; '+' / '.join(fig['heading_path'])+'; '+fig['xml_path'])
   for im in fig['images']:
    if im['asset']:
     dest=root/im['asset'];text+='Original extracted asset: '+kb.link(p,dest,Path(im['target']).name)+'\n\n'
     if dest.suffix.lower() in ['.png','.jpg','.jpeg','.gif','.svg']:text+='!['+fig['figure_id']+']('+kb.rel(p,dest)+')\n\n'
   text+='## Interpretation and pending work\n\n'+(fig['shape_text']+'\n\n' if fig['shape_text'] else '')+'This source occurrence has not yet been reconstructed in Mermaid. Original assets are retained unchanged. Labels, boundaries, direction, relationships, participant links, composite completeness, and decorative/substantive disposition require visual inspection. No render or visual-review pass is claimed.\n';write_page(root,p,text)
  if auxiliary:write_page(root,out/'notes.md',kb.front(metadata(s,'source-notes'))+'# Source notes and comments\n\n'+kb.table(['OOXML member','ID','Text'],[[n['member'],n['id'],n['text']] for n in auxiliary]))
  idx=out/'index.md';text=kb.front(metadata(s,'source-extraction-index'))+'# '+Path(s['occurrences'][0].get('archive_member') or s['occurrences'][0]['path']).name+'\n\n'+source_intro(root,idx,s,'complete main document XML, embedded media, footnotes, endnotes and comments')+f"Extracted {pidx} direct-body paragraphs, {tidx} direct-body tables, {fidx} drawing occurrences, and {len(media)} original media files. These are extraction counts, not reviewed substantive-coverage counts.\n\n"+kb.table(['Heading','Reference','Paragraph locators'],secrows)+'## Limitations\n\n'+'\n'.join('- '+x for x in report['limitations'])+'\n'
  write_page(root,idx,text)
  return {'source_id':sid,'format':'docx','output':idx.relative_to(root).as_posix(),'work_records':(work/'records.json').relative_to(root).as_posix(),'paragraphs':pidx,'tables':tidx,'figure_occurrences':fidx,'media':len(media),'status':'needs-review','limitations':report['limitations']}

def message_definitions(sid,pages,boundaries):
 definitions=[]
 for page in pages:
  txt=page['text'];m=re.match(r'\s*(\d+)\s+(?:MX\s+)?([a-z]{4}\.\d{3}\.\d{3}\.\d{2,})\s*\n?',txt)
  if not m:continue
  marker=re.search(r'\b'+re.escape(m.group(1))+r'\.1\s+MessageDefinition Functionality',txt[:800])
  if not marker:continue
  name=re.sub(r'\s+','',txt[m.end():marker.start()]).strip()
  if not re.fullmatch(r'[A-Za-z][A-Za-z0-9]+V[0-9]+',name):continue
  definitions.append({'message_id':m.group(2),'title':m.group(1)+' '+('MX ' if re.search(r'\bMX\s',m.group(0)) else '')+m.group(2)+' '+name,'source_id':sid,'start_page':page['page'],'end_page':None,'heading_path':[m.group(1)+' '+('MX ' if re.search(r'\bMX\s',m.group(0)) else '')+m.group(2)+' '+name],'basis':'Page-leading exact message ID followed by its MessageDefinition Functionality heading; bookmarks may omit entries.'})
 for i,d in enumerate(definitions):
  later=[b['page'] for b in boundaries if b['page']>d['start_page'] and re.match(r'\d+ Message Items Types',b['title'])]
  d['end_page']=definitions[i+1]['start_page']-1 if i+1<len(definitions) else min(later)-1 if later else len(pages)
 return definitions

def pdf(root,s,data,pdf_tables=False):
 from pypdf import PdfReader
 sid=s['source_id'];out=root/s['set_path']/'documents'/sid;work=root/'work/documents'/sid
 reader=PdfReader(io.BytesIO(data));boundaries=[]
 def walk(items,parents=[]):
  prior=None
  for item in items:
   if isinstance(item,list):walk(item,parents+([prior] if prior else []))
   else:
    try:
     page=reader.get_destination_page_number(item)+1;title=str(item.title);boundaries.append({'page':page,'title':title,'heading_path':parents+[title]});prior=title
    except Exception:pass
 walk(reader.outline)
 for b in boundaries:b['level']=len(b['heading_path'])
 kb.dump(work/'outline.json',boundaries)
 top=[b for b in boundaries if b['level']==1]
 definitions=[]
 for bi,b in enumerate(top):
  matches=ID.findall(b['title'])
  if matches:definitions.append({'message_id':matches[0],'title':b['title'],'source_id':sid,'start_page':b['page'],'end_page':top[bi+1]['page']-1 if bi+1<len(top) else len(reader.pages),'heading_path':b['heading_path']})
 kb.dump(work/'message-definitions.json',definitions)
 bypage={}
 for b in boundaries:
  if b['page'] not in bypage:bypage[b['page']]=b
 pages=[];sections=[];cur=None
 cache=work/'pages.json';cached={}
 if cache.exists():
  old=json.loads(cache.read_text(encoding='utf-8'))
  if old.get('source_sha256')==s['sha256']:cached={x['page']:x for x in old['pages']}
 for i,page in enumerate(reader.pages,1):
  txt=cached[i]['text'] if i in cached else (page.extract_text() or '');entry={'page':i,'text':txt,'message_ids':sorted(set(ID.findall(txt))),'mediabox':[float(x) for x in page.mediabox]}
  # Retain every page; no claim that text extraction accounts for vector artwork.
  pages.append(entry)
  if cur is None or i in bypage or len(cur['pages'])>=10:
   b=bypage.get(i,{'title':f'Continuation at file page {i}','heading_path':[]});cur={'title':b['title'],'heading_path':b['heading_path'],'pages':[]};sections.append(cur)
  cur['pages'].append(entry)
  if i%100==0:print(json.dumps({'source_id':sid,'pdf_pages_extracted':i,'total':len(reader.pages)}),flush=True)
 kb.dump(work/'pages.json',{'source_id':sid,'source_sha256':s['sha256'],'pages':pages})
 kb.dump(work/'message-definitions.json',message_definitions(sid,pages,boundaries))
 sectionrows=[]
 for j,sec in enumerate(sections,1):
  p=out/'sections'/f'section-{j:05d}.md';nums=[x['page'] for x in sec['pages']];title=sec['title'];ids=sorted(set(m for x in sec['pages'] for m in x['message_ids']))
  text=kb.front(metadata(s,'source-section',heading_path=sec['heading_path'],file_pages=nums,content_origin='source-text-extraction',mentioned_message_ids=ids))+'# '+title+'\n\n'+source_intro(root,p,s,f'one-based file pages {nums[0]} to {nums[-1]}')+'PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.\n\n'
  for ent in sec['pages']:text+='## File page '+str(ent['page'])+'\n\n```text\n'+ent['text'].replace('```','` ` `')+'\n```\n\n'
  write_page(root,p,text);sectionrows.append([title,f'{nums[0]}-{nums[-1]}',kb.link(out/'index.md',p,'Section')])
 tables=[]
 if pdf_tables:
  import pdfplumber
  with pdfplumber.open(io.BytesIO(data)) as pdfdoc:
   ti=0
   for pi,page in enumerate(pdfdoc.pages,1):
    shard=work/'table-pages'/f'page-{pi:05d}.json'
    payload=None
    if shard.exists():
     prev=json.loads(shard.read_text(encoding='utf-8'))
     if prev.get('source_sha256')==s['sha256']:payload=prev
    if payload is None:
     found=[];error=None
     try:
      for t in page.find_tables():found.append({'bbox':list(t.bbox),'cells':[list(c) for c in t.cells],'rows':t.extract()})
     except Exception as e:error=repr(e)
     payload={'source_id':sid,'source_sha256':s['sha256'],'file_page':pi,'tables':found,'error':error};kb.dump(shard,payload)
    for t in payload['tables']:
     ti+=1;rows=t['rows'];ncol=max([len(r) for r in rows]or[0]);tid=f'tbl-{ti:04d}';p=out/'tables'/(tid+'.md')
     text=kb.front(metadata(s,'extracted-table',table_id=tid,file_pages=[pi],bbox=t['bbox']))+'# '+tid+' - PDF table candidate\n\n'+source_intro(root,p,s,f'file page {pi}, bounding box '+str(t['bbox']))+'Detected by pdfplumber line intersections. Headers, merged cells, blank values and footnotes require visual reconciliation. Blank strings preserve extracted blank cells; nulls in the machine-readable shard mean no separate extracted cell (for example a span), not zero.\n\n'+kb.table([f'Source cell {i+1}' for i in range(ncol)],[r+['']*(ncol-len(r)) for r in rows]);write_page(root,p,text)
     tables.append({'table_id':tid,'page':pi,'bbox':t['bbox'],'cells':t['cells'],'rows':rows,'output':p.relative_to(root).as_posix(),'review_status':'needs-review'})
    if payload['error']:tables.append({'page':pi,'error':payload['error']})
    if pi%100==0:print(json.dumps({'source_id':sid,'pdf_table_pages_scanned':pi,'total':len(pdfdoc.pages),'table_candidates':len(tables)}),flush=True)
    page.close()
  kb.dump(work/'tables.json',tables)
 idx=out/'index.md';limits=['All PDF pages were text-extracted. Text extraction alone does not establish visual table or diagram coverage.','Source figures, vector drawings, composite images, and table footnotes require rendered-page reconciliation.','PDF replacement glyphs and column order may be imperfect. Consult the original before relying on uncertain wording.']
 if not pdf_tables:limits.append('PDF table detection has not run for this source; full table inventory remains pending.')
 text=kb.front(metadata(s,'source-extraction-index'))+'# '+Path(s['occurrences'][0].get('archive_member') or s['occurrences'][0]['path']).name+'\n\n'+source_intro(root,idx,s,f'all {len(pages)} file pages')+f"Extracted {len(pages)} pages into {len(sections)} bounded sections using bookmarks and a ten-page maximum. {len(tables)} table candidates.\n\n"+kb.table(['Source section','File pages','Evidence'],sectionrows)+'## Limitations\n\n'+'\n'.join('- '+x for x in limits)+'\n';write_page(root,idx,text)
 return {'source_id':sid,'format':'pdf','output':idx.relative_to(root).as_posix(),'work_records':(work/'pages.json').relative_to(root).as_posix(),'pages':len(pages),'sections':len(sections),'tables':len(tables),'pdf_tables_scanned':pdf_tables,'status':'needs-review','limitations':limits}

def main():
 global PRESERVE_EXISTING
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--source',action='append');p.add_argument('--job');p.add_argument('--format',choices=['docx','pdf']);p.add_argument('--set');p.add_argument('--force',action='store_true');p.add_argument('--pdf-tables',action='store_true');args=p.parse_args();root=args.root.resolve()
 if args.job:kb.set_write_context(root,args.job)
 args.source=__import__('refresh').job_sources(root,args.job,args.source)
 for s in sorted(kb.sources(root),key=lambda x:(list(kb.COLLECTIONS).index(x['collection']) if x['collection'] in kb.COLLECTIONS else 999,x['source_id'])):
  if s['format'] not in ['docx','pdf'] or args.source and s['source_id'] not in args.source or args.format and s['format']!=args.format or args.set and s['set_slug']!=args.set:continue
  status=root/'work/documents'/s['source_id']/'status.json'
  try:checked_bytes(root,s)
  except Exception as exc:
   print(json.dumps({'source_id':s['source_id'],'status':'blocked','error':str(exc)}),flush=True);continue
  PRESERVE_EXISTING=False
  if status.exists() and not args.force:
   rec=json.loads(status.read_text(encoding='utf-8'))
   PRESERVE_EXISTING=rec.get('source_sha256')==s['sha256']
   if rec.get('source_sha256')==s['sha256'] and rec.get('status')=='needs-review' and not (args.pdf_tables and not rec.get('pdf_tables_scanned')) and __import__('refresh').extraction_outputs_valid(root,s,rec):print('REUSE '+s['source_id'],flush=True);continue
  print('START '+s['source_id']+' '+s['set_title']+' '+s['format'],flush=True)
  try:
   data=checked_bytes(root,s);rec=docx(root,s,data) if s['format']=='docx' else pdf(root,s,data,args.pdf_tables);rec['source_sha256']=s['sha256'];rec['date']=DATE;rec['output_fingerprints']=__import__('refresh').output_fingerprints(root,s,rec);kb.dump(status,rec);print(json.dumps(rec),flush=True)
  except Exception as e:
   kb.dump(status,{'source_id':s['source_id'],'source_sha256':s['sha256'],'status':'blocked','error':repr(e)});print('ERROR '+s['source_id']+' '+repr(e),flush=True)
 reports=[]
 for path in sorted((root/'work/documents').glob('*/status.json')):reports.append(json.loads(path.read_text(encoding='utf-8')))
 kb.dump(root/'catalog/document-extraction.json',{'updated':DATE,'records':reports,'review_status':'needs-review'})
if __name__=='__main__':main()
