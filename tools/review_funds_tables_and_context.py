"""Record completed Funds source-cell audit and explicitly performed visual checks."""
import argparse,hashlib,io,json,re,zipfile
from pathlib import Path
from lxml import etree as E
from pypdf import PdfReader
import kb
from extract_documents import W,NS,plain
SID='src-000095';DATE='2026-11-09'
MANUAL_PAGE_MATCHES={89:80,100:88,104:90,109:94,112:96,126:103,129:105,137:108}
VISUAL_TABLE_PAGES=[15,16,19,20,21,22,23,24,25,26,31,32,33]
SPLIT_CELLS={('T18',2,2):[15,16],('T25',5,2):[20,21],('T33',2,2):[23,24],('T41',5,2):[31,32],('T42',2,2):[32,33]}
def main(root):
 source=next(s for s in kb.sources(root) if s['source_id']==SID);base=root/source['set_path'];data=kb.read_source(root,source)
 if hashlib.sha256(data).hexdigest()!=source['sha256']:raise ValueError('Original source changed')
 records=json.loads((root/'work/documents'/SID/'records.json').read_text(encoding='utf-8'));recon=json.loads((root/'work/docx-render'/SID/'reconciliation.json').read_text(encoding='utf-8'));word={t['source_table_id']:t for t in recon['tables']};context=root/'domains/securities/assets'/SID/'word-page-context';manifest=json.loads((context/'manifest.json').read_text(encoding='utf-8'));pages={r['file_page']:r for r in manifest['pages']};pdf=PdfReader(root/recon['pdf']);pdftext={}
 with zipfile.ZipFile(io.BytesIO(data)) as z:
  xml=E.fromstring(z.read('word/document.xml'));tables=xml.find('w:body',NS).findall('w:tbl',NS);footrefs=xml.findall('.//w:footnoteReference',NS)
 if len(tables)!=66 or len(records['tables'])!=66:raise ValueError('Unexpected table inventory')
 table_rows=[];cellcount=0;mergecount=0;errors=[];exceptions=[]
 for i,(tab,record) in enumerate(zip(tables,records['tables']),1):
  actual=[['\n'.join(plain(p) for p in tc.findall('w:p',NS)) for tc in tr.findall('w:tc',NS)] for tr in tab.findall('w:tr',NS)]
  if actual!=record['rows']:raise ValueError('Source to record differs T'+str(i))
  page=base/'documents'/SID/'tables'/f'tbl-{i:04d}.md';m,b=kb.metadata(page);width=max(map(len,actual));display=[[j+1]+r+['']*(width-len(r)) for j,r in enumerate(actual)];expected=kb.table(['Source row']+[f'Source cell {c+1}' for c in range(width)],display)
  if expected not in b:raise ValueError('Markdown row/field mismatch T'+str(i))
  merges=[]
  for ri,tr in enumerate(tab.findall('w:tr',NS),1):
   for ci,tc in enumerate(tr.findall('w:tc',NS),1):
    span=tc.find('w:tcPr/w:gridSpan',NS);vm=tc.find('w:tcPr/w:vMerge',NS)
    if span is not None or vm is not None:merges.append({'row':ri,'source_cell':ci,'grid_span':int(span.get('{'+W+'}val')) if span is not None else 1,'vertical_merge':vm.get('{'+W+'}val','continue') if vm is not None else None})
  if merges!=record.get('merges',[]):raise ValueError('Merge mismatch T'+str(i))
  if merges and kb.table(['Source row','Source cell','Grid span','Vertical merge'],[[x['row'],x['source_cell'],x['grid_span'],x['vertical_merge']] for x in merges]) not in b:raise ValueError('Markdown merge map differs T'+str(i))
  w=word['T'+str(i)];sp=list(range(w['word_start_file_page'],w['word_end_file_page']+1));norm=lambda s:''.join(re.findall(r'[A-Za-z0-9]+',s)).lower()
  for pn in sp:
   if pn not in pdftext:pdftext[pn]=pdf.pages[pn-1].extract_text()
  ptext='\n'.join(pdftext[pn] for pn in sp);resolved=[]
  for c in w['unmatched_cells']:
   key=(w['source_table_id'],c['row'],c['column']);simple=norm(c['source_cell']) in norm(ptext)
   if simple:reason='Exact alphanumeric content in the corresponding Word page span after ignoring bullet glyphs, punctuation and whitespace. Original literal cell text remains unchanged.'
   elif key in SPLIT_CELLS:reason='Directly read on full Word page images '+', '.join(map(str,SPLIT_CELLS[key]))+': source cell continues across a page boundary and repeated table headings/header/footer interrupt the PDF extraction. All source words are present.'
   else:raise ValueError('Unresolved Word text '+str(key))
   row={**c,'source_table_id':w['source_table_id'],'word_pages':sp,'resolution':'pass','reason':reason,'visual_review_pages':SPLIT_CELLS.get(key,[p for p in sp if p in VISUAL_TABLE_PAGES]),'source_cell_sha256':hashlib.sha256(c['source_cell'].encode()).hexdigest()};exceptions.append(row);resolved.append(row)
  note_refs=[]
  for ref in footrefs:
   xpath=xml.getroottree().getpath(ref)
   if xpath.startswith(record['xml_path']+'/'):note_refs.append({'member':'word/footnotes.xml','id':ref.get('{'+W+'}id'),'source_xml_path':xpath})
  count=sum(map(len,actual));cellcount+=count;mergecount+=len(merges);m.update(table_source_cell_review='pass',table_merge_mapping_review='pass',word_table_text_review='pass',word_unmatched_cells_visual_review='pass' if resolved else 'not-applicable-no-unmatched-cells',word_file_pages=sp,table_review_date=DATE)
  tag='FUNDS-TABLE-AUDIT';b=re.sub(r'\n<!-- '+tag+'-START -->.*?<!-- '+tag+'-END -->\n?','\n',b,flags=re.S);b=b.replace('Review: row extraction complete for the direct-body table; visual comparison, note linkage, and semantic header review not run.','Review: complete physical-cell and merge-map comparison against original OOXML passed; all nonempty cell texts are corroborated by the Word-rendered source, including directly checked split-cell and bullet exceptions. This is an extraction-fidelity check, not resolution of source business ambiguities.')
  b+='\n<!-- '+tag+'-START -->\n## Source and Word-render reconciliation\n\nOn '+DATE+', all '+str(count)+' physical cells (including blanks, header cells and literal XML/example values) and '+str(len(merges))+' merge mappings were compared with the unchanged original OOXML and this Markdown table. Word-rendered file pages '+str(sp[0])+('–'+str(sp[-1]) if len(sp)>1 else '')+' corroborate all '+str(w['nonempty_cells'])+' nonempty source cells. '+str(len(resolved))+' prior PDF-text matching exceptions were resolved as recorded in '+kb.link(page,root/'tracking/reviews/funds-tables.json','cell-specific review evidence')+'.\n\n'
  if note_refs:
   b+='**Source footnote 1**, attached to T6 row2 cell1: “Was previously called \' FundProcessingPassportReport\'”. '+kb.link(page,base/'documents'/SID/'notes.md','Original extracted note text')+'. The source footnote marker is structural OOXML; it was not part of the flattened cell text.\n\n'
  b+='Full-cell visual comparison of every otherwise matched cell is not claimed; exact source-cell preservation and Word text corroboration are distinguished from the targeted visual exception checks.\n<!-- '+tag+'-END -->\n';kb.put(page,kb.front(m)+b.strip()+'\n')
  table_rows.append({'source_table_id':w['source_table_id'],'table_id':record['table_id'],'path':page.relative_to(root).as_posix(),'source_xml_path':record['xml_path'],'physical_rows':len(actual),'physical_cells':count,'nonempty_cells':w['nonempty_cells'],'merge_mappings':len(merges),'source_cell_and_markdown_review':'pass','word_text_corroboration':'pass','resolved_exceptions':len(resolved),'word_file_pages':sp,'footnotes':note_refs})
 table_report={'date':DATE,'source_id':SID,'source_sha256':source['sha256'],'table_count':len(table_rows),'physical_cells':cellcount,'nonempty_cells':sum(x['nonempty_cells'] for x in table_rows),'merge_mappings':mergecount,'source_oo_xml_and_markdown_cell_review':'pass','word_text_corroboration':'pass','prior_matching_exceptions':len(exceptions),'resolved_matching_exceptions':len(exceptions),'visual_table_pages':[{**pages[n],'review':'pass','scope':'Direct source-cell/header/continuation comparison for unmatched table cells'} for n in VISUAL_TABLE_PAGES],'footnote_references':len(footrefs),'limitations':['The local Word render has known STYLEREF header errors; these are not source business content.','Every physical source cell and merge mapping was checked programmatically. Targeted full-page visual inspection covers the previously unmatched cells; not every matched cell was individually visually read.','Source business inconsistencies remain recorded rather than corrected.'],'records':table_rows,'exceptions':exceptions};kb.dump(root/'tracking/reviews/funds-tables.json',table_report)
 # These pages were actually inspected as complete-page contacts; unmatched images were additionally inspected at full page size.
 reviewed_pages=set(range(71,111))|{284,285,292,301,314,315,316};fullsize=set(MANUAL_PAGE_MATCHES.values());figures=json.loads((root/'tracking/reviews/funds-second-half.json').read_text(encoding='utf-8'))['records'];locations=json.loads((root/'work/docx-render'/SID/'page-locations.json').read_text(encoding='utf-8'))['locations'];frows=[]
 for r in figures:
  num=int(r['source_figure_id'].split('-')[1]);matches=[l['start_file_page'] for l in locations if any(f['sha256']==r['original_sha256'] for f in l.get('asset_fingerprints',[]))];pn=matches[0] if matches else MANUAL_PAGE_MATCHES[num]
  if pn not in reviewed_pages:raise ValueError('Page not inspected')
  page=root/r['path'];m,b=kb.metadata(page);m.update(word_composite_visual_review='pass',word_composite_visual_review_date=DATE,word_file_page=pn,word_page_locator_basis='exact asset SHA-256 plus page-context visual comparison' if matches else 'direct original-image, source-heading and full-page visual matching; no hash match claimed')
  tag='FUNDS-WORD-LOCATOR';b=re.sub(r'\n<!-- '+tag+'-START -->.*?<!-- '+tag+'-END -->\n?','\n',b,flags=re.S);b+='\n<!-- '+tag+'-START -->\n## Word-rendered source page and composite review\n\n'+kb.link(page,root/pages[pn]['path'],'Word-rendered file page '+str(pn))+' was inspected in complete-page context on '+DATE+'. '+('The asset identity also matches by SHA-256. ' if matches else 'This occurrence was located by direct full-page comparison of the original image, message labels and heading context; no asset-hash match is claimed. ')+'The original image contains the displayed substantive figure; no additional external labels or omitted drawing objects were observed in its page surroundings. The two-panel message5 overview intentionally spans pages314–315 (figures146–147), linked separately.\n\nThis whole-page check complements the prior detailed original-image versus reconstruction review. Known local Word header-field errors are excluded from business evidence. '+kb.link(page,root/'tracking/reviews/funds-second-half-word-context.json','Hash-bound page-context review evidence')+'.\n<!-- '+tag+'-END -->\n';kb.put(page,kb.front(m)+b.strip()+'\n')
  frows.append({'source_figure_id':r['source_figure_id'],'path':r['path'],'original_sha256':r['original_sha256'],'word_file_page':pn,'page_image':pages[pn]['path'],'page_image_sha256':pages[pn]['sha256'],'page_locator_basis':m['word_page_locator_basis'],'review':'pass','review_scope':'Complete-page visual surroundings/boundaries comparison; prior full original-image label and Mermaid comparison remains separately recorded.','fullsize_page_additionally_inspected':pn in fullsize})
 fr={'date':DATE,'source_id':SID,'source_sha256':source['sha256'],'parent_pdf_sha256':manifest['parent_pdf_sha256'],'diagram_count':len(frows),'reviewed_file_pages':sorted(reviewed_pages),'exact_asset_page_matches':sum(bool([l for l in locations if any(f['sha256']==r['original_sha256'] for f in l.get('asset_fingerprints',[]))]) for r in figures),'manual_visual_page_matches':MANUAL_PAGE_MATCHES,'complete_page_context_review':'pass','records':frows};kb.dump(root/'tracking/reviews/funds-second-half-word-context.json',fr)
 srpath=root/'tracking/reviews/funds-second-half.json';sr=json.loads(srpath.read_text(encoding='utf-8'));sr.update(word_composite_visual_review='pass',word_page_manual_visual_matches=MANUAL_PAGE_MATCHES,word_file_page_unresolved_figures=[]);kb.dump(srpath,sr)
 print(json.dumps({'tables':len(table_rows),'physical_cells':cellcount,'nonempty_cells':table_report['nonempty_cells'],'merge_mappings':mergecount,'resolved_exceptions':len(exceptions),'figure_full_page_checks':len(frows),'page_contexts':len(reviewed_pages)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
