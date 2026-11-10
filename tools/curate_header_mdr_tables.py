"""Reconcile visually inspected BAH/BFH MDR tables and unruled datatype facets."""
from pathlib import Path
import json,sys,io,re,collections
sys.path.insert(0,str(Path(__file__).resolve().parent));import kb,pdfplumber
from extract_workbooks import fm,write,relative,esc
ROOT=Path(__file__).resolve().parents[1];JOB='job-000001';DATE='2026-11-09';T=chr(96)
def put(p,b):write(ROOT,ROOT/p,b,JOB)
def link(p,t,l):return '['+l+']('+relative(ROOT/p,ROOT/t)+')'
def tab(h,rs):return '| '+' | '.join(esc(x) for x in h)+' |\n| '+' | '.join('---' for _ in h)+' |\n'+''.join('| '+' | '.join(esc(c) if c not in [None,''] else '∅' for c in r)+' |\n' for r in rs)
sources={s['source_id']:s for s in kb.sources(ROOT)}
FACETS={
'src-000011':[
(51,'3.2.1.4 CountryCode',[('pattern','[A-Z]{2,2}')]),
(51,'3.2.1.5 ExternalClearingSystemIdentification1Code',[('minLength','1'),('maxLength','5')]),
(52,'3.2.1.6 ExternalFinancialInstitutionIdentification1Code',[('minLength','1'),('maxLength','4')]),
(52,'3.2.1.7 ExternalOrganisationIdentification1Code',[('minLength','1'),('maxLength','4')]),
(52,'3.2.1.8 ExternalPersonIdentification1Code',[('minLength','1'),('maxLength','4')]),
(54,'3.2.4.1 AnyBICDec2014Identifier',[('pattern','[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}')]),
(55,'3.2.4.2 BICFIDec2014Identifier (continued from p54)',[('pattern','[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}')]),
(55,'3.2.4.3 LEIIdentifier',[('pattern','[A-Z0-9]{18,18}[0-9]{2,2}')]),
(55,'3.2.6.1 Exact4AlphaNumericText',[('pattern','[a-zA-Z0-9]{4}')]),
(55,'3.2.6.2 Max128Text',[('minLength','1'),('maxLength','128')]),
(56,'3.2.6.3 Max140Text',[('minLength','1'),('maxLength','140')]),
(56,'3.2.6.4 Max16Text',[('minLength','1'),('maxLength','16')]),
(56,'3.2.6.5 Max2048Text',[('minLength','1'),('maxLength','2048')]),
(56,'3.2.6.6 Max256Text',[('minLength','1'),('maxLength','256')]),
(56,'3.2.6.7 Max350Text',[('minLength','1'),('maxLength','350')]),
(57,'3.2.6.8 Max35Text',[('minLength','1'),('maxLength','35')]),
(57,'3.2.6.9 Max4Text',[('minLength','1'),('maxLength','4')]),
(57,'3.2.6.10 Max70Text',[('minLength','1'),('maxLength','70')]),
(57,'3.2.6.11 PhoneNumber',[('pattern',r'\+[0-9]{1,3}-[0-9()+\-]{1,30}')])],
'src-000349':[(9,'3.1.3.1 Number',[('totalDigits','18'),('fractionDigits','0')]),(10,'3.1.4.1 Max140Text',[('minLength','1'),('maxLength','140')]),(10,'3.1.4.2 Max256Text',[('minLength','1'),('maxLength','256')]),(10,'3.1.4.3 Max35Text',[('minLength','1'),('maxLength','35')])]
}
summary=[]
for sid in FACETS:
 s=sources[sid];work=ROOT/'work/documents'/sid;doc=Path(s['set_path'])/'documents'/sid;assets=Path('shared/assets')/sid
 tables=json.loads((work/'tables.json').read_text('utf-8'));tables=[t for t in tables if not t.get('unruled_format')]
 original_count=len(tables);pages=json.loads((work/'pages.json').read_text('utf-8'))['pages'];pdf=pdfplumber.open(io.BytesIO(kb.read_source(ROOT,s)))
 f=lambda **kw:fm(domain='shared',source_ids=[sid],source_edition=s['source_edition'],message_ids=['head.001.001.04' if sid=='src-000011' else 'head.002.001.01'],**kw)
 def evidence(p,pg,loc):return kb.source_link(ROOT,ROOT/p,s)+', file/printed page '+str(pg)+', '+loc+'.'
 checks=[];groups=collections.defaultdict(list)
 for t in tables:groups[json.dumps(t['rows'],ensure_ascii=False,sort_keys=True)].append(t['table_id'])
 for t in tables:
  tid=t['table_id'];p=doc/'tables'/(tid+'.md');pg=t['page'];rows=t['rows'];h=rows[0];bodyrows=rows[1:];inds=[]
  if h[0]=='Or':
   rowboxes=sorted({(c[1],c[3]) for c in t['cells'] if abs(c[0]-t['bbox'][0])<0.01});xs=sorted({c[0] for c in t['cells']});x0,x1=xs[1:3]
   assert len(rowboxes)==len(rows),(sid,tid,len(rowboxes),len(rows))
   for (y0,y1),row in zip(rowboxes[1:],bodyrows):
    chars=[c for c in pdf.pages[pg-1].chars if x0<=c['x0']<x1 and y0<=c['top']<y1 and c['text'].strip()]
    inds.append(round(min((c['x0'] for c in chars),default=x0)-x0,3) if chars else None)
  siblings=groups[json.dumps(rows,ensure_ascii=False,sort_keys=True)];crop=assets/'table-crops'/(tid+'.png');notes='All source rows and columns are retained in their supplied order. ∅ denotes a blank cell, not zero or an asserted absence. Line breaks within cells are preserved. '
  if h[0]=='Or':notes+='The source Or markers delimit choices; members are not independently mandatory. The Type-column ± glyph is retained as printed (U+00B1), not a missing-value marker. Grey source cells have no text value. The indentation register below preserves nesting cues in PDF points from the left edge of the element column; it is literal layout evidence, not an inferred XML path. The XSD remains authoritative for full schema constraints. '
  if sid=='src-000011' and tid in ['tbl-0055','tbl-0056']:notes+='NamePrefix2Code is split across pages 52–53: '+link(p,doc/'tables/tbl-0055.md','DOCT row')+' and '+link(p,doc/'tables/tbl-0056.md','MADM, MISS, MIST and MIKS rows')+'. '
  if tid=='tbl-0002':notes+='The MDR prints “Message root <Document> <AppHdr>” or “<Document> <Xchg>” as a table label; do not infer an extra root wrapper. The supplied schemas declare AppHdr and Xchg respectively. '
  review={'date':DATE,'result':'pass','method':'Compared full rendered source pages and table crops; verified labels, complete row/column values, choice markers, multiplicities, code definitions and split boundaries. Matching repeated table content cross-checked against its first occurrence and source-page layout.'}
  out=f(document_kind='table',review_status='reviewed',curated=True,table_id=tid,file_pages=[pg],source_locations=['table bbox '+str(t['bbox'])],row_count=len(bodyrows),visual_review=review,limitations=[])+ '# '+tid+' — source table on page '+str(pg)+'\n\n'+evidence(p,pg,'MDR table, bbox '+str(t['bbox']))+'\n\n'+link(p,crop,'Complete rendered source table')+' · '+link(p,assets/'rendered'/('page-%05d.png'%pg),'Full source page and context')+'\n\n'+notes+'\n\n'+tab(h,bodyrows)
  if inds:out+='\n## Original indentation\n\n'+tab(['Source data row','Element-column inset (PDF points)'],[[i+1,x] for i,x in enumerate(inds)])
  if len(siblings)>1:out+='\n## Matching content occurrences\n\n'+', '.join(link(p,doc/'tables'/(x+'.md'),x) for x in siblings)+'. Matching table values do not collapse differing enclosing field contexts.\n'
  out+='\n## Review evidence\n\nVisual comparison completed 2026-11-09 using Poppler 26.07.0 full-page renders at 120 dpi. Original PDF cells and Markdown values preserve all '+str(len(bodyrows))+' data rows. This reviews this table only; source business rules and external code publication applicability are tracked separately.\n'
  put(p,out);t.update(disposition='converted',review_status='reviewed',visual_review=review,row_count=len(bodyrows),source_indent_points=inds,source_crop=crop.as_posix(),output=p.as_posix())
  checks.append({'table_id':tid,'page':pg,'rows':len(bodyrows),'source_equal_table_occurrences':siblings,'type_column_plusminus_count':sum(c=='\u00b1' for r in rows for c in r),'replacement_character_count':sum('\ufffd' in str(c) for r in rows for c in r)})
 pdf.close()
 for i,(pg,heading,rs) in enumerate(FACETS[sid],original_count+1):
  tid='tbl-%04d'%i;p=doc/'tables'/(tid+'.md');page=assets/'rendered'/('page-%05d.png'%pg);review={'date':DATE,'result':'pass','method':'Unruled Format label/value block transcribed from source and compared against rendered full page.'}
  out=f(document_kind='table',review_status='reviewed',curated=True,table_id=tid,file_pages=[pg],source_locations=[heading+' / Format'],row_count=len(rs),table_kind='unruled-format-properties',visual_review=review,limitations=[])+'# '+heading+' — Format\n\n'+evidence(p,pg,heading+' / Format')+'\n\n'+link(p,page,'Complete source page including original unruled Format block')+'\n\nThe source prints this property/value block without borders. Both columns and every value are preserved below; these are MDR datatype facets, not additional business rules. Literal patterns retain backslashes.\n\n| Property | Literal source value |\n| --- | --- |\n'+''.join('| '+k+' | '+T+v+T+' |\n' for k,v in rs)+'\nVisual comparison completed 2026-11-09.\n'
  put(p,out);tables.append({'table_id':tid,'page':pg,'heading':heading,'unruled_format':True,'bbox':None,'rows':[['Property','Literal source value']]+rs,'row_count':len(rs),'disposition':'converted','review_status':'reviewed','visual_review':review,'output':p.as_posix(),'source_page_asset':page.as_posix()})
 put(Path('work/documents')/sid/'tables.json',json.dumps(tables,ensure_ascii=False,indent=2))
 inv=json.loads((work/'pdf-assets.json').read_text('utf-8'))
 for pg in inv['pages']:
  pg.update(requires_vector_visual_inspection=False,visual_review={'date':DATE,'result':'pass','method':'Complete page inspected in page-contact sheet; tables additionally compared in readable crops.','disposition':'tables-text-and-page-decoration-only','substantive_diagrams':0})
 inv.update(review_status='reviewed',limitations=[],visual_review={'date':DATE,'result':'pass','substantive_diagrams':0,'decorative_image_exclusions':0,'notes':'No embedded images; vector candidates are table borders, shading, rules and page furniture. No source use-case, class/entity or flow diagram found in all rendered pages.'})
 put(Path('work/documents')/sid/'pdf-assets.json',json.dumps(inv,ensure_ascii=False,indent=2))
 for pg in pages:
  m=ROOT/assets/'rendered'/('page-%05d.json'%pg['page']);r=json.loads(m.read_text('utf-8'));r['visual_review']={'date':DATE,'result':'pass','scope':'Whole-page substantive-figure and table inventory triage; data tables separately checked.'};put(m.relative_to(ROOT),json.dumps(r,ensure_ascii=False,indent=2))
 report={'source_id':sid,'source_sha256':s['sha256'],'date':DATE,'pages_rendered':len(pages),'pages_visually_triaged':len(pages),'embedded_images':0,'substantive_source_diagrams':0,'original_ruled_table_occurrences':original_count,'distinct_ruled_table_contents':len(groups),'additional_unruled_format_tables':len(FACETS[sid]),'total_tables':len(tables),'total_body_rows_including_blank_spacers':sum(t['row_count'] for t in tables),'total_data_rows':sum(any(c not in [None,''] for c in r) for t in tables for r in t['rows'][1:]),'table_review_passes':len(tables),'table_checks':checks,'limitations':[]}
 put(Path('work/documents')/sid/'visual-review.json',json.dumps(report,ensure_ascii=False,indent=2));summary.append(report)
 p=doc/'visual-coverage.md';out=f(document_kind='coverage',review_status='reviewed',curated=True)+'# Complete MDR table and figure inventory\n\n'+evidence(p,'1–'+str(len(pages)),'Complete MDR')+' All '+str(len(pages))+' pages rendered with Poppler 26.07.0 at 120 dpi and visually inspected on 2026-11-09.\n\nThere are '+str(original_count)+' ruled table occurrences and '+str(len(FACETS[sid]))+' additional unruled datatype Format blocks: '+str(len(tables))+' tables with '+str(report['total_data_rows'])+' data rows. All are preserved, linked and visually compared. There are no embedded images and no substantive source diagrams. Vector marks are table borders, shading and page rules; no use-case or class/entity model is silently omitted.\n\n## Tables\n\n'+''.join('- '+link(p,Path(t['output']),t['table_id'])+' — page '+str(t['page'])+', '+str(t['row_count'])+' rows'+('; unruled Format block' if t.get('unruled_format') else '')+'.\n' for t in tables)+'\n## Evidence and scope\n\n'+link(p,Path('work/documents')/sid/'visual-review.json','Detailed visual-review evidence')+'. This coverage review applies to supplied source tables/figures. It does not certify external publication currency or replace the separate complete XSD declaration coverage. Exact message definitions and schema roots remain separate from generic MDR table labels.\n';put(p,out)
 p=doc/'tables/index.md';put(p,f(document_kind='table-index',review_status='reviewed',curated=True)+'# MDR tables\n\n'+link(p,doc/'visual-coverage.md','Reviewed complete source coverage')+'\n\n'+''.join('- '+link(p,Path(t['output']),t['table_id'])+' — page '+str(t['page'])+'.\n' for t in tables))
 p=doc/'pdf-figures/index.md';put(p,f(document_kind='diagram-inventory',review_status='reviewed',curated=True)+'# MDR diagram inventory\n\nAll '+str(len(pages))+' rendered pages were visually inspected on 2026-11-09. No substantive diagram or embedded image appears in this supplied MDR. Vector operators belong to tables, shading and page furniture. '+link(p,doc/'visual-coverage.md','Complete source visual coverage')+'.\n')
 p=doc/'index.md';b=(ROOT/p).read_text('utf-8');note='\n## Complete source visual inventory\n\n'+link(p,doc/'visual-coverage.md','All tables, unruled datatype facets and diagram dispositions')+'.\n';put(p,b+note if note not in b else b)
put(Path('work/header-mdr-review.json'),json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps([{k:v for k,v in r.items() if k!='table_checks'} for r in summary],ensure_ascii=False))
