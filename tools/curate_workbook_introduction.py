"""Maintain the visually reviewed canonical introduction model and all exact-image occurrences."""
from pathlib import Path
import json,sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from extract_workbooks import fm,write,relative,source_id,original_links
ROOT=Path(__file__).resolve().parents[1];JOB='job-000001'
resultpath=ROOT/'work/workbook-results.json';results=json.loads(resultpath.read_text('utf-8'))
sources={s['source_id']:s for s in json.loads((ROOT/'catalog/sources.json').read_text('utf-8'))['sources']}
HASH='e4188e920a131656ea4c3f2fccb1fee9dc8a98b28988408646e31802bde426c7'
matches=[(s,d) for s in results for d in s.get('diagrams',[]) if d['sha256']==HASH]
page=ROOT/'shared/reference/models/business-component-inheritance/fig-0001.md'
code=(ROOT/'work/workbook-diagrams/business-component-inheritance.mmd').read_text('utf-8')
report=json.loads((ROOT/'work/workbook-diagram-render-report.json').read_text('utf-8'))[0]
meta=dict(document_kind='diagram',domain='shared',diagram_id='fig-0001',diagram_kind='classDiagram',origin='source-reconstruction',curated=True,source_ids=[s['source_id'] for s,d in matches],source_locations=[s['source_id']+': '+d['sheet']+'; '+d['drawing_part']+' anchor '+str(d['anchor_id'])+'; '+d.get('from_cell','absolute') for s,d in matches],review_status='reviewed',content_sha256=HASH,renderer='Mermaid 12.3.0; Chromium 156.0.8078.81',render_result='pass',visual_review='2026-11-08; source image and rendered output inspected; three class names, stereotypes, package labels, and two generalization directions agree.',limitations=['The source model has no multiplicity labels or data attributes; none are inferred.'])
body=fm(**meta)+'# Business component inheritance example\n\nThis is the substantive model shown in the Introduction worksheet of 23 supplied MDR workbooks. Byte-identical source artwork is represented once, with every source occurrence retained below.\n\n'
body+='![Original model]('+relative(page,ROOT/matches[0][1]['asset'])+')\n\n## Mermaid reconstruction\n\n'+chr(96)*3+'mermaid\n'+code+chr(96)*3+'\n\n'
body+='## Entities and relationships\n\nAll three classes carry the BusinessComponent stereotype and the source package label “from DICO_BusinessComponents”. AccountContract specializes Contract; CashAccountContract specializes AccountContract. Hollow triangles point to the parent class. The boxes show no data attributes or operations. No composition, database keys, ownership, multiplicity or business institution is inferred.\n\nThe original diagramming-tool navigation glyphs are interface ornaments, not additional semantic relationships. Their omission does not remove any model endpoint or label. Package labels are retained as Mermaid notes.\n\n'
body+='## Source occurrences\n\n| Source | Worksheet / drawing locator | Original artwork | Occurrence page |\n| --- | --- | --- | --- |\n'
for s,d in matches:
 sid=s['source_id'];loc=d['sheet']+'; '+d['drawing_part']+' anchor '+str(d['anchor_id'])+'; '+d.get('from_cell','absolute')
 body+='| '+original_links(ROOT,sources[sid],page)+' ('+sid+') | '+loc+' | [Image]('+relative(page,ROOT/d['asset'])+') | [Occurrence]('+relative(page,ROOT/d['page'])+') |\n'
body+='\n## Rendering and visual review\n\n- Mermaid 12.3.0 browser API parsed and rendered this code successfully using Chromium 156.0.8078.81 on 2026-11-08.\n- The original source image and rendered PNG were opened and compared on 2026-11-08. All three class names, stereotypes, package labels and both parent directions agree. The reconstruction changes layout only.\n- [Rendered PNG]('+relative(page,ROOT/report['png'])+'), [SVG]('+relative(page,ROOT/report['svg'])+'), [renderer report]('+relative(page,ROOT/'work/workbook-diagram-render-report.json')+').\n- This review covers this small figure only; it does not imply that any owning workbook or message set is fully reviewed.\n'
write(ROOT,page,body,JOB)
for s,d in matches:
 pg=ROOT/d['page'];sid=s['source_id'];loc=d['sheet']+'; '+d['drawing_part']+' anchor '+str(d['anchor_id'])+'; '+d.get('from_cell','absolute')
 content=fm(document_kind='diagram-occurrence',domain=sources[sid]['domain'],diagram_id=d['figure_id'],source_ids=[sid],source_locations=[loc],origin='source-reconstruction',review_status='reviewed',curated=True,disposition='deduplicated',canonical_output=page.relative_to(ROOT).as_posix(),limitations=[])+ '# '+d['sheet']+' — business component inheritance\n\n'+original_links(ROOT,sources[sid],pg)+'; '+sid+', '+loc+'.\n\nThe complete original image matches SHA-256 '+HASH+'. This substantive figure is represented by the '+ '[reviewed canonical reconstruction]('+relative(pg,page)+'). All class labels, stereotypes, package labels and generalization endpoints are retained there, together with Mermaid, rendering and visual-review evidence.\n\n[Original image]('+relative(pg,ROOT/d['asset'])+'). Exact drawing anchors and offsets remain in the [workbook extraction metadata]('+relative(pg,ROOT/'work/workbooks'/sid/'workbook.json')+').\n'
 write(ROOT,pg,content,JOB)
 d.update(disposition='deduplicated',review_status='reviewed',canonical_output=page.relative_to(ROOT).as_posix(),render_evidence='work/workbook-diagram-render-report.json',visual_review='2026-11-08; image hash equivalence and reviewed canonical reconstruction')
 # Keep the extraction record truthful without altering stored cells or original XML.
 mp=ROOT/'work/workbooks'/sid/'workbook.json';wm=json.loads(mp.read_text('utf-8'))
 for sh in wm['sheets']:
  for old in sh['drawings']:
   if old['page']==d['page']:old.update({k:d[k] for k in ['disposition','review_status','canonical_output','render_evidence','visual_review']})
 write(ROOT,mp,json.dumps(wm,ensure_ascii=False,indent=2),JOB)
 idx=ROOT/s['output'];existing=idx.read_text('utf-8')
 note='\n## Reviewed common figure\n\nThe Introduction business-component inheritance figure has a [reviewed canonical reconstruction]('+relative(idx,page)+'). Other figures retain their individual review status.\n'
 if '## Reviewed common figure' not in existing:write(ROOT,idx,existing+note,JOB)
 cov=idx.parent/'coverage.md';old=cov.read_text('utf-8')
 old=old.replace('They remain unresolved pending substantive/decorative classification, full-figure completeness assessment, textual transcription, Mermaid reconstruction and visual review. No workbook or diagram is marked reviewed.','The Introduction hierarchy is now deduplicated to a reviewed canonical diagram. The other picture occurrences remain pending substantive classification, full-figure completeness assessment, textual transcription, Mermaid reconstruction and visual review. The workbook remains needs-review.')
 write(ROOT,cov,old,JOB)
write(ROOT,resultpath,json.dumps(results,ensure_ascii=False,indent=2),JOB)
print('Canonical diagram reviewed; '+str(len(matches))+' exact source occurrences linked.')
