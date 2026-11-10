"""Record explicitly performed source359 image/context checks and complete cell audit."""
import argparse,hashlib,io,json,re,zipfile
from pathlib import Path
from urllib.parse import unquote
from lxml import etree as E
from pypdf import PdfReader
import kb
from extract_documents import W,NS,plain
from curate_intrabalance import block,SID,DATE,sha
def main(root):
 source=next(s for s in kb.sources(root) if s['source_id']==SID);base=root/source['set_path'];raw=kb.read_source(root,source)
 if hashlib.sha256(raw).hexdigest()!=source['sha256']:raise ValueError('Source changed')
 rec=json.loads((root/'work/documents'/SID/'records.json').read_text(encoding='utf-8'));recon=json.loads((root/'work/docx-render'/SID/'reconciliation.json').read_text(encoding='utf-8'));word={t['source_table_id']:t for t in recon['tables']};pdf=PdfReader(root/recon['pdf']);pdftext={};rows=[];exceptions=[]
 with zipfile.ZipFile(io.BytesIO(raw)) as z:xml=E.fromstring(z.read('word/document.xml'))
 original=xml.find('w:body',NS).findall('w:tbl',NS)
 if len(original)!=27 or len(rec['tables'])!=27:raise ValueError('Table inventory changed')
 norm=lambda s:''.join(re.findall('[A-Za-z0-9]+',s)).lower()
 for num,(tab,t) in enumerate(zip(original,rec['tables']),1):
  actual=[['\n'.join(plain(p) for p in tc.findall('w:p',NS)) for tc in tr.findall('w:tc',NS)] for tr in tab.findall('w:tr',NS)]
  if actual!=t['rows']:raise ValueError('Cell extraction mismatch '+str(num))
  page=base/'documents'/SID/'tables'/f'tbl-{num:04d}.md';m,b=kb.metadata(page);width=max(map(len,actual));expected=kb.table(['Source row']+[f'Source cell {c+1}' for c in range(width)],[[i+1]+r+['']*(width-len(r)) for i,r in enumerate(actual)])
  if expected not in b:raise ValueError('Markdown cells differ '+str(num))
  merges=[]
  for ri,tr in enumerate(tab.findall('w:tr',NS),1):
   for ci,tc in enumerate(tr.findall('w:tc',NS),1):
    span=tc.find('w:tcPr/w:gridSpan',NS);vm=tc.find('w:tcPr/w:vMerge',NS)
    if span is not None or vm is not None:merges.append({'row':ri,'source_cell':ci,'grid_span':int(span.get('{'+W+'}val')) if span is not None else 1,'vertical_merge':vm.get('{'+W+'}val','continue') if vm is not None else None})
  if merges!=t.get('merges',[]):raise ValueError('Merge mismatch '+str(num))
  if merges and kb.table(['Source row','Source cell','Grid span','Vertical merge'],[[x['row'],x['source_cell'],x['grid_span'],x['vertical_merge']] for x in merges]) not in b:raise ValueError('Markdown merge mismatch')
  w=word['T'+str(num)];sp=list(range(w['word_start_file_page'],w['word_end_file_page']+1));local=[]
  for pn in sp:
   if pn not in pdftext:pdftext[pn]=pdf.pages[pn-1].extract_text()
  for cell in w['unmatched_cells']:
   if norm(cell['source_cell']) in norm(''.join(pdftext[pn] for pn in sp)):basis='Alphanumeric text corroborated in the Word page span; original punctuation, bullets and whitespace remain preserved separately.'
   elif (w['source_table_id'],cell['row'],cell['column'])==('T6',8,2):basis='Direct full-size visual reading of Word pages11–12 confirms T2S operator definition continues after the repeated header; no words lost.'
   else:raise ValueError('Unresolved Word cell '+str(cell))
   entry={**cell,'source_table_id':w['source_table_id'],'word_pages':sp,'resolution':'pass','basis':basis};exceptions.append(entry);local.append(entry)
  refs=[{'id':e.get('{'+W+'}id'),'path':xml.getroottree().getpath(e)} for e in tab.findall('.//w:footnoteReference',NS)]
  m.update(table_source_cell_review='pass',table_merge_mapping_review='pass',word_table_text_review='pass',word_file_pages=sp,table_review_date=DATE)
  b=b.replace('Review: row extraction complete for the direct-body table; visual comparison, note linkage, and semantic header review not run.','Review: exact source-cell and merge preservation passed; Word text corroboration and targeted continuation review are recorded below. Source business discrepancies remain visible.')
  text='## Source-cell and rendered-text reconciliation\n\nOn '+DATE+', all '+str(sum(map(len,actual)))+' physical cells and '+str(len(merges))+' merge mappings were checked against unchanged original OOXML and this Markdown table. All '+str(w['nonempty_cells'])+' nonempty cell texts are corroborated by Word-derived pages '+', '.join(map(str,sp))+'. '+str(len(local))+' prior text-matching exceptions were resolved. '+kb.link(page,root/'tracking/reviews/intrabalance-tables.json','Exact cell audit and exception evidence')+'.\n\nThe T6 row8 cell2 continuation was directly read at full page size on pages11–12. Activity-table bullets on pages21–30 were inspected in page context and independently reconciled after normalization. Every otherwise matched cell was not individually visually read. Source facts, literal XML examples and table blanks remain unchanged.\n'
  if refs:text+='Footnote references are retained in the original and extracted notes: '+kb.link(page,base/'documents'/SID/'notes.md','Source notes')+'.\n'
  kb.put(page,kb.front(m)+block(b,'INTRABALANCE-TABLE-AUDIT',text));rows.append({'source_table_id':w['source_table_id'],'path':page.relative_to(root).as_posix(),'source_xml_path':t['xml_path'],'physical_rows':len(actual),'physical_cells':sum(map(len,actual)),'nonempty_cells':w['nonempty_cells'],'merge_mappings':len(merges),'word_file_pages':sp,'resolved_exceptions':len(local),'footnotes':refs,'cell_and_merge_review':'pass','word_text_review':'pass'})
 report={'date':DATE,'source_id':SID,'source_sha256':source['sha256'],'table_count':27,'physical_cells':sum(x['physical_cells'] for x in rows),'nonempty_cells':sum(x['nonempty_cells'] for x in rows),'merge_mappings':sum(x['merge_mappings'] for x in rows),'resolved_exceptions':len(exceptions),'source_cell_preservation':'pass','word_text_corroboration':'pass','records':rows,'exceptions':exceptions,'limitations':['Every physical source cell and merge map is checked. Targeted source-page inspection resolves continuation/bullet exceptions; not every matched cell was individually visually read.','Business wording conflicts remain issue-000047.']};kb.dump(root/'tracking/reviews/intrabalance-tables.json',report)
 # All listed diagrams were actually inspected, not sampled.
 curated=json.loads((root/'work/intrabalance-curation.json').read_text(encoding='utf-8'))['records'];renders={r['diagram']:r for r in json.loads((root/'tracking/reviews/intrabalance-render.json').read_text(encoding='utf-8'))};context=json.loads((root/'domains/securities/assets'/SID/'word-page-context/manifest.json').read_text(encoding='utf-8'));reviewed=set([10,11,12,13]+list(range(17,34))+list(range(35,40)));errors=[];participants=set();flows=set()
 for r in curated:
  for field,pathfield in [('mermaid_sha256','mermaid'),('original_sha256','original'),('word_page_sha256','word_page')]:
   if sha(root/r[pathfield])!=r[field]:raise ValueError('Reviewed artifact changed '+r[pathfield])
  if r['word_file_page'] not in reviewed:raise ValueError('Uninspected page')
  num=int(r['source_figure_id'][4:]);rr=renders[r['source_figure_id']]
  if rr['result']!='pass':raise ValueError('Render failure')
  page=root/r['path'];m,b=kb.metadata(page);m.update(render_status='pass',renderer=rr['renderer'],renderer_version=rr['version'],render_date=DATE,visual_review='pass',visual_review_date=DATE,word_composite_visual_review='pass',word_composite_visual_review_date=DATE,word_file_page=r['word_file_page']);participants.update(m.get('participant_ids',[]));flows.update(m.get('flow_ids',[]));review_scope='Original versus Mermaid: literal labels, connector endpoints/direction, decisions, solid/dashed lines, role boundaries and complete Word-page surroundings. Source-text labels clipped by the local Word rendering are explicitly disclosed, not presented as visibly read.'
  text='## Completed rendering and visual comparison\n\n'+rr['renderer']+'; Mermaid '+rr['version']+'; '+DATE+': parsing and rendering **pass**. '+kb.link(page,root/rr['svg'],'Rendered SVG')+' · '+kb.link(page,root/rr['png'],'Rendered PNG')+'.\n\n'+review_scope+' Review **pass for extraction fidelity with the stated limitations**. Complete Word file page '+str(r['word_file_page'])+' was inspected; standalone picture reconstructions were also compared against their detailed original previews. Native sequence figures17–24 use the full Word composite, including original drawing text when labels are clipped.\n\n'+kb.link(page,root/'tracking/reviews/intrabalance-diagrams.json','Hash-bound review and source-object inventory')+'. Contextual source ambiguities keep the page needs-review. This does not certify missing business context or hidden native layers.\n'
  b=b.replace('Parsing, final rendered comparison and whole-page review are recorded separately, not inferred from transcription.','Completed parsing, rendered comparison and whole-page review are recorded below.');kb.put(page,kb.front(m)+block(b,'INTRABALANCE-REVIEW',text));r.update(render=rr,svg_sha256=sha(root/rr['svg']),png_sha256=sha(root/rr['png']),visual_review='pass',word_composite_review='pass',review_scope=review_scope)
  ep=base/'documents'/SID/'diagrams'/(r['source_figure_id']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['path'],disposition='canonical-artwork-reused-contextual-review-open' if num==1 else 'converted-needs-review',render_status='pass',visual_review='pass',word_composite_visual_review='pass');kb.put(ep,kb.front(em)+block(eb,'INTRABALANCE-REVIEW',kb.link(ep,page,'Completed source reconstruction, rendered comparison and remaining context limitations')))
  for target in re.findall(r'\]\(([^)]+)\)',b):
   if target.startswith(('http:','https:','#')):continue
   t=unquote(target.split('#')[0])
   if t and not (page.parent/t).resolve().exists():errors.append({'page':r['path'],'target':target})
 # Retain all four legend glyphs and classify all20 original media without losing shared composite occurrences.
 inventory=json.loads((root/'work/documents'/SID/'media-review-inventory.json').read_text(encoding='utf-8'));cp=root/'tracking/reviews/docx-media-classification.json';classification=json.loads(cp.read_text(encoding='utf-8'));entries=[x for x in classification['records'] if x.get('source_id')!=SID]
 for im in inventory['media']:
  num=int(re.search(r'image(\d+)',im['original']).group(1));disp='retained-notation-legend' if 6<=num<=9 else ('retained-composite-component' if num>=17 else 'substantive-diagram')
  entries.append({'source_id':SID,'original':im['original'],'sha256':im['original_sha256'],'disposition':disp,'classification_review':'pass','classification_review_date':DATE,'classification_review_scope':'Direct original previews and complete Word-page inspection; native components reconciled to figures17–24.','classification_reason':'Four T19 notation glyphs are preserved with definitions, not decorative.' if 6<=num<=9 else ('Institutional pictogram component of eight complete native sequence drawings; canonical full-composite pages retain the surrounding text and connectors.' if num>=17 else 'Substantive source hierarchy, business use-case, scope or activity diagram.')})
  if 6<=num<=9:
   ep=base/'documents'/SID/'diagrams'/f'fig-{num:04d}.md';em,eb=kb.metadata(ep);em.update(disposition='retained-notation-legend',classification_review='pass',classification_review_date=DATE,word_file_page=20);kb.put(ep,kb.front(em)+block(eb,'INTRABALANCE-LEGEND','This is a substantive notation glyph in '+kb.link(ep,base/'documents'/SID/'tables/tbl-0019.md','T19: start/end/choice/parallel bar definitions')+'. It was directly inspected in complete Word page20 and retained unchanged. It is not a separate business diagram or a decorative exclusion.'))
 classification.update(updated=DATE,records=entries);kb.dump(cp,classification)
 final={'date':DATE,'source_id':SID,'source_sha256':source['sha256'],'source_figure_occurrences':24,'source_media':20,'substantive_diagrams':20,'legend_glyphs':4,'mermaid_render_pass':20,'original_visual_review_pass':20,'word_composite_review_pass':20,'canonical_artwork_reuse_context_open':['fig-0001'],'native_composites':list(range(17,25)),'flow_references':len(flows),'participant_references':len(participants),'parent_word_pdf_sha256':context['parent_pdf_sha256'],'source_unchanged':True,'validation_errors':errors,'records':curated,'limitations':['Source359 issue-000047 remains open; hierarchy source343 context issue-000039 also remains visible.','The four original WMF pictograms are components of eight native composite sequences, not 32 independent business diagrams.','No decorative exclusion is claimed. Native embedded application content beyond the visible Word figures remains separately inventoried.']};kb.dump(root/'tracking/reviews/intrabalance-diagrams.json',final)
 coverage=base/'intrabalance-review.md';kb.put(coverage,kb.front({'template':False,'document_kind':'extraction-coverage','review_status':'needs-review','source_ids':[SID],'domain':'securities','message_sets':['t2s-intra-balance-movement'],'updated':DATE})+'# Intra-balance movement source359 review\n\nAll24 source figure occurrences are accounted for:20 substantive figures and4 notation-legend glyphs. All20 Mermaid views parse and render, and each has an explicit original and whole-Word-page comparison. Figure1 reuses exact source343 artwork with contextual review still open. Native figures17–24 retain complete composites and XML-supported labels hidden by local rendering.\n\n'+kb.link(coverage,base/'diagrams/intrabalance/index.md','Diagram and flow navigation')+' · '+kb.link(coverage,root/'tracking/reviews/intrabalance-diagrams.json','Hash-bound diagram review')+' · '+kb.link(coverage,root/'tracking/reviews/intrabalance-tables.json','All27 tables: cell audit and rendered corroboration')+'\n\nSource issue-000047 preserves context/role/label discrepancies. Extracted XML examples and revision history remain in focused source sections and tables. Source checksums are unchanged; not all desired business knowledge is established merely by complete supplied-content extraction.\n')
 for name in ['index.md','coverage.md','participants.md','flows.md']:
  path=base/name
  if path.exists():m,b=kb.metadata(path);kb.put(path,kb.front(m)+block(b,'INTRABALANCE-REVIEW',kb.link(path,coverage,'Source359 diagram, flow and table review')))
 print(json.dumps({k:v for k,v in final.items() if k not in ('records','limitations','native_composites')},ensure_ascii=False));print(json.dumps({k:v for k,v in report.items() if k not in ('records','exceptions','limitations')}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);main(p.parse_args().root.resolve())
