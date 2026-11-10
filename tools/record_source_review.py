"""Reconcile source cells and record an explicitly supplied, completed visual-review profile.

This is not an automatic visual reviewer. Callers must enumerate the pages, figures,
manual exception decisions and limits that have actually been inspected.
"""
import hashlib,io,json,re,zipfile
from urllib.parse import unquote
from lxml import etree as E
from pypdf import PdfReader
import kb
from extract_documents import W,NS,plain
from curate_intrabalance import block,sha

def record(root,c):
 sid=c['source_id'];date=c['date'];key=c['key'];src=next(s for s in kb.sources(root) if s['source_id']==sid);base=root/src['set_path'];data=kb.read_source(root,src)
 if hashlib.sha256(data).hexdigest()!=src['sha256']:raise ValueError('Source changed')
 source=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8'));recon=json.loads((root/'work/docx-render'/sid/'reconciliation.json').read_text(encoding='utf-8'));wr={t['source_table_id']:t for t in recon['tables']};pdf=PdfReader(root/recon['pdf']);ptext={};norm=lambda s:''.join(re.findall('[A-Za-z0-9]+',s)).lower();tables=[];exceptions=[]
 with zipfile.ZipFile(io.BytesIO(data)) as z:xml=E.fromstring(z.read('word/document.xml'))
 original=xml.find('w:body',NS).findall('w:tbl',NS)
 if len(original)!=c['table_count'] or len(source['tables'])!=c['table_count']:raise ValueError('Table count differs')
 for num,(tab,rec) in enumerate(zip(original,source['tables']),1):
  cells=[['\n'.join(plain(p) for p in tc.findall('w:p',NS)) for tc in tr.findall('w:tc',NS)] for tr in tab.findall('w:tr',NS)]
  if cells!=rec['rows']:raise ValueError('Source cell extraction differs')
  page=base/'documents'/sid/'tables'/f'tbl-{num:04d}.md';m,b=kb.metadata(page);width=max(map(len,cells))
  if kb.table(['Source row']+[f'Source cell {j+1}' for j in range(width)],[[i+1]+r+['']*(width-len(r)) for i,r in enumerate(cells)]) not in b:raise ValueError('Markdown table differs '+str(num))
  merges=[]
  for ri,tr in enumerate(tab.findall('w:tr',NS),1):
   for ci,tc in enumerate(tr.findall('w:tc',NS),1):
    span=tc.find('w:tcPr/w:gridSpan',NS);vm=tc.find('w:tcPr/w:vMerge',NS)
    if span is not None or vm is not None:merges.append({'row':ri,'source_cell':ci,'grid_span':int(span.get('{'+W+'}val')) if span is not None else 1,'vertical_merge':vm.get('{'+W+'}val','continue') if vm is not None else None})
  if merges!=rec.get('merges',[]):raise ValueError('Merge extraction differs')
  if merges and kb.table(['Source row','Source cell','Grid span','Vertical merge'],[[x['row'],x['source_cell'],x['grid_span'],x['vertical_merge']] for x in merges]) not in b:raise ValueError('Markdown merge map differs')
  w=wr['T'+str(num)];sp=list(range(w['word_start_file_page'],w['word_end_file_page']+1));resolved=[]
  for pn in sp:
   if pn not in ptext:ptext[pn]=pdf.pages[pn-1].extract_text()
  for cell in w['unmatched_cells']:
   cellkey=(w['source_table_id'],cell['row'],cell['column'])
   if norm(cell['source_cell']) in norm(''.join(ptext[p] for p in sp)):basis='Alphanumeric content corroborated across the Word page span; punctuation and whitespace remain exact in the original extraction.'
   elif cellkey in c['manual_cells']:basis=c['manual_cells'][cellkey]
   else:raise ValueError('Unresolved Word cell '+str(cellkey))
   r={**cell,'source_table_id':w['source_table_id'],'word_pages':sp,'resolution':'pass','basis':basis};exceptions.append(r);resolved.append(r)
  refs=[{'id':e.get('{'+W+'}id'),'path':xml.getroottree().getpath(e)} for e in tab.findall('.//w:footnoteReference',NS)]
  m.update(table_source_cell_review='pass',table_merge_mapping_review='pass',word_table_text_review='pass',word_file_pages=sp,table_review_date=date)
  b=b.replace('Review: row extraction complete for the direct-body table; visual comparison, note linkage, and semantic header review not run.','Review: exact original-cell and merge-map comparison passed; rendered-text corroboration and targeted exception review are recorded below. Business-source interpretation remains separate.')
  text='## Complete cell reconciliation and targeted visual review\n\nOn '+date+', all '+str(sum(map(len,cells)))+' physical cells and '+str(len(merges))+' merge mappings were compared against the unchanged original OOXML and this Markdown table. All '+str(w['nonempty_cells'])+' nonempty cell texts were corroborated by Word-rendered pages '+', '.join(map(str,sp))+', including '+str(len(resolved))+' resolved matching exceptions. '+kb.link(page,root/'tracking/reviews'/(key+'-tables.json'),'Cell-specific audit evidence')+'.\n\n'+c['table_visual_scope']+' Every otherwise matched cell was not individually visually read. Source wording and business ambiguities remain unchanged.\n'
  if refs:text+=kb.link(page,base/'documents'/sid/'notes.md','Source footnote/endnote content')+'; exact reference paths remain in the audit.\n'
  kb.put(page,kb.front(m)+block(b,key.upper()+'-TABLE-REVIEW',text));tables.append({'source_table_id':w['source_table_id'],'path':page.relative_to(root).as_posix(),'physical_rows':len(cells),'physical_cells':sum(map(len,cells)),'nonempty_cells':w['nonempty_cells'],'merge_mappings':len(merges),'word_file_pages':sp,'resolved_exceptions':len(resolved),'footnotes':refs,'cell_and_merge_review':'pass','word_text_review':'pass'})
 tr={'date':date,'source_id':sid,'source_sha256':src['sha256'],'table_count':len(tables),'physical_cells':sum(x['physical_cells'] for x in tables),'nonempty_cells':sum(x['nonempty_cells'] for x in tables),'merge_mappings':sum(x['merge_mappings'] for x in tables),'resolved_exceptions':len(exceptions),'source_cell_preservation':'pass','word_text_corroboration':'pass','visual_scope':c['table_visual_scope'],'exceptions':exceptions,'records':tables};kb.dump(root/'tracking/reviews'/(key+'-tables.json'),tr)
 if c.get('tables_only'):return {k:v for k,v in tr.items() if k not in ['records','exceptions']}
 rows=json.loads((root/'work'/(key+'-curation.json')).read_text(encoding='utf-8'))['records'];rr={x['diagram']:x for x in json.loads((root/'tracking/reviews'/(key+'-render.json')).read_text(encoding='utf-8'))};reviewed=set(c['reviewed_figures']);pages=set(c['reviewed_pages']);errors=[];participants=set();flows=set()
 if {int(x['source_figure_id'][4:]) for x in rows}!=reviewed:raise ValueError('Explicit visual-review inventory differs')
 for r in rows:
  num=int(r['source_figure_id'][4:]);render=rr[r['source_figure_id']]
  if render['result']!='pass' or r['word_file_page'] not in pages:raise ValueError('Missing render or page inspection')
  for field,path in [('mermaid_sha256','mermaid'),('original_sha256','original'),('word_page_sha256','word_page')]:
   if sha(root/r[path])!=r[field]:raise ValueError('Reviewed artifact changed')
  p=root/r['path'];m,b=kb.metadata(p);m.update(render_status='pass',renderer=render['renderer'],renderer_version=render['version'],render_date=date,visual_review='pass',visual_review_date=date,word_composite_visual_review='pass',word_composite_visual_review_date=date,word_file_page=r['word_file_page']);participants.update(m.get('participant_ids',[]));flows.update(m.get('flow_ids',[]));text='## Completed rendering and visual review\n\n'+render['renderer']+'; Mermaid '+render['version']+'; '+date+': parse/render **pass**. '+kb.link(p,root/render['svg'],'Rendered SVG')+' · '+kb.link(p,root/render['png'],'Rendered PNG')+'.\n\n'+c['diagram_visual_scope']+' Extraction-fidelity comparison **pass with the page’s explicit notation limitations**. Whole Word page '+str(r['word_file_page'])+' was also inspected. This does not resolve source ambiguities or claim review of hidden native-application layers.\n\n'+kb.link(p,root/'tracking/reviews'/(key+'-diagrams.json'),'Hash-bound review evidence')+'.\n';kb.put(p,kb.front(m)+block(b,key.upper()+'-DIAGRAM-REVIEW',text));r.update(render=render,svg_sha256=sha(root/render['svg']),png_sha256=sha(root/render['png']),visual_review='pass',word_composite_review='pass')
  ep=base/'documents'/sid/'diagrams'/(r['source_figure_id']+'.md');em,eb=kb.metadata(ep);em.update(canonical_diagram=r['path'],disposition='converted-needs-review',render_status='pass',visual_review='pass',word_composite_visual_review='pass');kb.put(ep,kb.front(em)+block(eb,key.upper()+'-REVIEW',kb.link(ep,p,'Completed canonical reconstruction and review evidence')))
  for target in re.findall(r'\]\(([^)]+)\)',b):
   if target.startswith(('http:','https:','#')):continue
   t=unquote(target.split('#')[0])
   if t and not (p.parent/t).resolve().exists():errors.append({'page':r['path'],'target':target})
 inv=json.loads((root/'work/documents'/sid/'media-review-inventory.json').read_text(encoding='utf-8'));cp=root/'tracking/reviews/docx-media-classification.json';classification=json.loads(cp.read_text(encoding='utf-8'));entries=[x for x in classification['records'] if x.get('source_id')!=sid]
 for im in inv['media']:
  num=int(re.search(r'image(\d+)',im['original']).group(1));legend=num in c['legend_media'];component=num in c['composite_media'];disp='retained-notation-legend' if legend else ('retained-composite-component' if component else 'substantive-diagram');entries.append({'source_id':sid,'original':im['original'],'sha256':im['original_sha256'],'disposition':disp,'classification_review':'pass','classification_review_date':date,'classification_review_scope':c['diagram_visual_scope'],'classification_reason':'Retained substantive notation glyph with its source table definition.' if legend else ('Component of full native composite figures; surrounding labels/connectors retained in canonical page crops.' if component else 'Substantive original business-role, process or activity diagram.')})
 for num in c['legend_figures']:
  ep=base/'documents'/sid/'diagrams'/f'fig-{num:04d}.md';em,eb=kb.metadata(ep);em.update(disposition='retained-notation-legend',classification_review='pass',classification_review_date=date,word_file_page=c['legend_page']);text='Substantive notation legend glyph retained unchanged with '+kb.link(ep,base/'documents'/sid/'tables'/f'tbl-{c["legend_table"]:04d}.md','complete source legend definitions')+'. Directly inspected on complete Word page '+str(c['legend_page'])+'. This is not a decorative exclusion or an independent business scenario.';kb.put(ep,kb.front(em)+block(eb,key.upper()+'-LEGEND',text))
 classification.update(updated=date,records=entries);kb.dump(cp,classification)
 dr={'date':date,'source_id':sid,'source_sha256':src['sha256'],'source_figure_occurrences':len(source['figures']),'source_media':len(inv['media']),'substantive_diagrams':len(rows),'legend_glyphs':len(c['legend_figures']),'mermaid_render_pass':len(rows),'original_visual_review_pass':len(rows),'word_composite_review_pass':len(rows),'flow_references':len(flows),'participant_references':len(participants),'source_unchanged':True,'validation_errors':errors,'limitations':c['limitations'],'records':rows};kb.dump(root/'tracking/reviews'/(key+'-diagrams.json'),dr)
 coverage=base/(key+'-review.md');kb.put(coverage,kb.front({'template':False,'document_kind':'extraction-coverage','review_status':'needs-review','source_ids':[sid],'domain':src['domain'],'message_sets':[src['set_slug']],'updated':date})+'# '+src['set_title']+' source review\n\n'+str(len(source['figures']))+' figure occurrences are accounted for: '+str(len(rows))+' substantive diagrams and '+str(len(c['legend_figures']))+' retained notation glyphs. All substantive reconstructions parse/render and have an explicit original and whole-page comparison. All '+str(len(tables))+' tables have complete cell and rendered-text reconciliation.\n\n'+kb.link(coverage,base/'diagrams'/key/'index.md','Diagram and reusable-flow navigation')+' · '+kb.link(coverage,root/'tracking/reviews'/(key+'-diagrams.json'),'Diagram review evidence')+' · '+kb.link(coverage,root/'tracking/reviews'/(key+'-tables.json'),'Table reconciliation')+'\n\n'+'\n'.join('- '+x for x in c['limitations'])+'\n')
 for name in ['index.md','coverage.md','participants.md','flows.md']:
  p=base/name
  if p.exists():m,b=kb.metadata(p);kb.put(p,kb.front(m)+block(b,key.upper()+'-REVIEW',kb.link(p,coverage,'Source diagrams, flows and table review')))
 return {'diagrams':len(rows),'flow_references':len(flows),'participant_references':len(participants),'table_count':len(tables),'physical_cells':tr['physical_cells'],'nonempty_cells':tr['nonempty_cells'],'resolved_exceptions':len(exceptions),'errors':errors}
