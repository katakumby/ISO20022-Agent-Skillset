"""Inventory uncertain Unicode replacement glyphs without modifying evidence.

Counts U+FFFD in extracted PDF page text and extracted table cells separately;
these overlap and must not be added as unique source character counts.
"""
import argparse,json,datetime
from pathlib import Path
import kb

def audit(root):
 records=[];locations=[]
 for s in kb.sources(root):
  if s['format']!='pdf':continue
  work=root/'work/documents'/s['source_id'];pf=work/'pages.json';tf=work/'tables.json'
  pages=json.loads(pf.read_text(encoding='utf-8'))['pages'] if pf.exists() else []
  tables=json.loads(tf.read_text(encoding='utf-8')) if tf.exists() else []
  pc=tc=0;affected_pages=[];affected_tables=set();affected_cells=0
  for p in pages:
   text=p['text'];count=text.count('\ufffd')
   if not count:continue
   pi=p['page'];pc+=count;affected_pages.append(pi)
   contexts=[]
   for line_number,line in enumerate(text.splitlines(),1):
    if '\ufffd' in line:contexts.append({'extracted_text_line':line_number,'count':line.count('\ufffd'),'text':line})
   locations.append({'source_id':s['source_id'],'kind':'page-text','file_page':pi,'count':count,'contexts':contexts,'work_record':pf.relative_to(root).as_posix()})
  for t in tables:
   for ri,row in enumerate(t.get('rows',[]),1):
    for ci,cell in enumerate(row,1):
     text='' if cell is None else str(cell);count=text.count('\ufffd')
     if not count:continue
     tc+=count;affected_cells+=1;affected_tables.add(t['table_id']);dest=root/t['output'];meta,_=kb.metadata(dest) if dest.exists() else ({},'')
     locations.append({'source_id':s['source_id'],'kind':'table-cell','file_page':t['page'],'table_id':t['table_id'],'extracted_row':ri,'extracted_cell':ci,'bbox':t.get('bbox'),'count':count,'text':text,'output':t['output'],'output_visual_review':meta.get('table_cells_visual_review'),'work_record':tf.relative_to(root).as_posix()})
  records.append({'source_id':s['source_id'],'source_sha256':s['sha256'],'source_occurrences':s['occurrences'],'text_extraction_available':pf.exists(),'table_extraction_available':tf.exists(),'page_text_replacement_glyphs':pc,'affected_file_pages':affected_pages,'table_cell_replacement_glyphs':tc,'affected_tables':len(affected_tables),'affected_cells':affected_cells})
 date=datetime.date.today().isoformat();out=root/'catalog/pdf-replacement-glyph-audit.json'
 kb.dump(out,{'updated':date,'character':'U+FFFD REPLACEMENT CHARACTER','limitation':'Extraction uncertainty; presence is not evidence that the source itself contains this glyph. Page and table counts overlap. Visually corrected output may differ from immutable work extraction. Zero count does not establish correct character encoding.','records':records,'locations':locations})
 page=root/'tracking/reviews/pdf-replacement-glyph-audit.md'
 body=kb.front(dict(template=False,document_kind='extraction-audit',review_status='needs-review',updated=date,source_ids=[r['source_id'] for r in records if r['page_text_replacement_glyphs'] or r['table_cell_replacement_glyphs']],issue_ids=['issue-000019']))+'# PDF replacement-glyph audit\n\nCounts are from extracted work evidence, not original PDF character counts. Page-text and table-cell counts overlap and must not be summed as unique source errors. Output pages with recorded visual corrections are identified in the detailed audit and remain preserved. Zero replacement glyphs does not establish correct character encoding or table completeness.\n\n'+kb.link(page,out,'Complete machine-readable page and cell locators')+'.\n\n'+kb.table(['Source','Text glyphs','Affected pages','Table glyphs','Affected tables','Affected cells','Extraction available (text/table)'],[[r['source_id'],r['page_text_replacement_glyphs'],len(r['affected_file_pages']),r['table_cell_replacement_glyphs'],r['affected_tables'],r['affected_cells'],str(r['text_extraction_available'])+'/'+str(r['table_extraction_available'])] for r in records])+'\nEach table locator includes file page, extraction table ID, bounding box, one-based extracted row and cell, literal extracted text, destination page, and any table visual-review pass. Reconcile uncertain glyphs against rendered originals; preserve raw extracted evidence and record corrections on the reference page.\n'
 kb.put(page,body)
 print(json.dumps({'sources':len(records),'affected_sources':sum(bool(r['page_text_replacement_glyphs'] or r['table_cell_replacement_glyphs']) for r in records),'page_text_glyphs':sum(r['page_text_replacement_glyphs'] for r in records),'table_cell_glyphs':sum(r['table_cell_replacement_glyphs'] for r in records),'locations':len(locations),'audit':str(out)}))
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();audit(a.root.resolve())
