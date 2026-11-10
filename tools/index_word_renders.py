"""Index additional Word pagination and independently reconcile DOCX table text.

Read-only source inspection. A cell-text match is not a visual/semantic review.
Tables are aligned by ordinal only when complete top-level table counts agree;
figure page locators require exact binary asset fingerprints, never ordinal guesses.
"""
import argparse,hashlib,json,re,unicodedata
from pathlib import Path
from pypdf import PdfReader
import kb

def norm(text):return re.sub(r'\s+','',unicodedata.normalize('NFKC',text).replace('\u00ad',''))
def main(root):
    sources={s['source_id']:s for s in kb.sources(root)};summary=[]
    for rp in sorted((root/'work/docx-render').glob('*/render-report.json')):
        rr=json.loads(rp.read_text(encoding='utf-8-sig'));sid=rr['source_id'];src=sources[sid];assert src['sha256']==rr['source_sha256'];assert rr['original_unchanged'];pdf=root/rr['output'];assert hashlib.sha256(pdf.read_bytes()).hexdigest()==rr['output_sha256']
        loc=json.loads((rp.parent/'page-locations.json').read_text(encoding='utf-8-sig'));raw=json.loads((root/'work/documents'/sid/'records.json').read_text(encoding='utf-8'));pages=[p.extract_text() or '' for p in PdfReader(str(pdf)).pages];tloc=[x for x in loc['locations'] if x['kind']=='table'];tables=[];matched=0;nonempty=0
        can_align=len(tloc)==len(raw['tables']) and all(not t.get('nested_tables') for t in raw['tables'])
        for i,t in enumerate(raw['tables']):
            item={'table_id':t['table_id'],'source_table_id':t['source_table_id'],'source_xml_path':t['xml_path'],'heading_path':t['heading_path'],'physical_rows':len(t['rows']),'nonempty_cells':sum(bool(c.strip()) for row in t['rows'] for c in row),'result':'not-aligned'}
            if can_align:
                tl=tloc[i];start=tl['start_file_page'];end=tl['end_file_page'];span=norm('\n'.join(pages[start-1:end]));unmatched=[];count=0
                for rownum,row in enumerate(t['rows'],1):
                    for colnum,cell in enumerate(row,1):
                        if not cell.strip():continue
                        count+=1
                        if norm(cell) not in span:unmatched.append({'row':rownum,'column':colnum,'source_cell':cell})
                item.update(word_start_file_page=start,word_end_file_page=end,word_start_printed_page=tl['start_printed_page'],matched_nonempty_cells=count-len(unmatched),unmatched_cells=unmatched,result='cell-text-reconciled' if not unmatched else 'unmatched-cell-text-needs-inspection');matched+=count-len(unmatched);nonempty+=count
            tables.append(item)
        byhash={}
        for l in loc['locations']:
            if l['kind']!='inline-shape':continue
            for fp in l.get('asset_fingerprints',[]):byhash.setdefault(fp['sha256'],[]).append(l)
        invp=root/'work/documents'/sid/'media-review-inventory.json';inv=json.loads(invp.read_text(encoding='utf-8')) if invp.exists() else {'media':[]};figures=[]
        for m in inv['media']:
            matches=byhash.get(m['original_sha256'],[])
            for occurrence in m['occurrences']:
                figures.append({'figure_id':occurrence['figure_id'],'original':m['original'],'original_sha256':m['original_sha256'],'source_locator':occurrence['source_locator'],'result':'exact-asset-page-match' if len(matches)==1 else 'multiple-page-candidates' if matches else 'page-not-established','word_page_candidates':[{'start_file_page':v['start_file_page'],'end_file_page':v['end_file_page'],'ordinal':v['ordinal']} for v in matches]})
        errors=[i+1 for i,p in enumerate(pages) if 'STYLEREF' in p or ('Błąd!' in p and ('Heading' in p or 'Nagłówek' in p)) or ('Error!' in p and ('Heading' in p or 'Style' in p))]
        result={'source_id':sid,'source_sha256':src['sha256'],'pdf':rr['output'],'pdf_sha256':rr['output_sha256'],'word_version':rr['word_version'],'word_build':rr['word_build'],'pages':len(pages),'original_unchanged_at_render':rr['original_unchanged'],'table_alignment_basis':'Equal top-level source/Word table counts, no nested source tables; ordinal alignment with independent PDF cell-text check' if can_align else 'Counts/nesting do not establish alignment','tables':tables,'figures':figures,'matched_nonempty_cells':matched,'nonempty_cells_checked':nonempty,'derived_header_error_pages':errors,'limitations':['Word pagination is additional to stable original paragraph/XML/table locators.','Normalized cell text is independently searched in its Word-PDF span; this does not prove grid/merge/footnote or semantic fidelity.','Repeated identical source assets can produce multiple candidate pages; no occurrence page is selected without further evidence.','Floating/composite objects without unique binary asset hashes require direct page inspection.','Word locale can produce a STYLEREF header error. This is a derived-render artifact, not a statement in the immutable original.','No visual-review or reviewed status is conferred by this helper.']}
        dest=root/'work/docx-render'/sid/'reconciliation.json';kb.dump(dest,result);page=root/src['set_path']/'documents'/sid/'render-verification.md';meta={'template':False,'document_kind':'source-render-coverage','review_status':'needs-review','domain':src['domain'],'source_ids':[sid],'source_editions':[src.get('edition') or src.get('edition_label') or 'See source register'],'message_sets':[src['set_slug']],'limitations':result['limitations']}
        body='# Word render and independent table-text reconciliation\n\n'+kb.source_link(root,page,src)+'\n\n'+kb.link(page,pdf,'Complete derived Word PDF')+' · '+kb.link(page,dest,'Detailed evidence, unmatched cells and figure-page candidates')+'\n\nRenderer: Microsoft Word '+str(rr['word_version'])+' build '+str(rr['word_build'])+'. File pages: '+str(len(pages))+'. Original checksum unchanged at render. No visual review is implied.\n\n'+kb.table(['Table','Word file pages','Cell-text matches','Result'],[[t['source_table_id'],str(t.get('word_start_file_page','?'))+'–'+str(t.get('word_end_file_page','?')),str(t.get('matched_nonempty_cells',0))+'/'+str(t['nonempty_cells']),t['result']] for t in tables])+'\n## Limitations\n\n'+'\n'.join('- '+x for x in result['limitations'])+'\n'
        if errors:body+='\nDerived header errors detected on file pages: '+', '.join(map(str,errors))+'. Consult the original source; body/table evidence is evaluated separately.\n'
        kb.put(page,kb.front(meta)+body);entry={k:result[k] for k in ['source_id','source_sha256','pages','matched_nonempty_cells','nonempty_cells_checked','derived_header_error_pages']};entry.update(path=page.relative_to(root).as_posix(),reconciliation=dest.relative_to(root).as_posix(),table_count=len(tables),figure_occurrences_with_unique_page=sum(x['result']=='exact-asset-page-match' for x in figures),figure_occurrences=len(figures));summary.append(entry);print(json.dumps({'source':sid,'tables':len(tables),'cell_matches':matched,'cell_total':nonempty,'figure_pages':entry['figure_occurrences_with_unique_page']}))
    kb.dump(root/'catalog/docx-word-renders.json',{'updated':kb.DATE,'records':summary,'limitations':['Derived render/text verification, not full visual or semantic review.']});index=root/'catalog/docx-word-renders.md';kb.put(index,'# DOCX Word render evidence\n\nThese 25 source renders supplement stable original locators. They do not confer reviewed status.\n\n'+kb.table(['Source','Pages','Tables','Independent cell-text matches','Uniquely mapped figure occurrences','Evidence'],[[s['source_id'],s['pages'],s['table_count'],str(s['matched_nonempty_cells'])+'/'+str(s['nonempty_cells_checked']),str(s['figure_occurrences_with_unique_page'])+'/'+str(s['figure_occurrences']),kb.link(index,root/s['path'],'Review evidence')] for s in summary]))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);a=p.parse_args();main(a.root.resolve())
