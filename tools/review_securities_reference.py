"""Record checks actually performed for SecuritiesReferenceData source377."""
import argparse,json
from pathlib import Path
from record_source_review import record
CONFIG={'source_id':'src-000377','date':'2026-11-09','key':'securities-reference','table_count':19,'manual_cells':{
 ('T3',3,1):'Directly read Word pages6–7: reference name is on page6, complete URD URL continues on page7 after a repeated table header. Original URL and punctuation remain unchanged.',
 ('T6',4,2):'Directly read Word pages11–12: Market Infrastructure definition continues across the repeated table header.',
 ('T9',4,2):'Directly read Word pages13–14: modification precondition continues after the table header with changed which requires a modification of the security.',
 ('T15',3,2):'Directly read Word pages17–18: Validate ends on page17 with instruction will be and continues on page18 with resubmit to validation after e.g. a night-time cycle.',
 ('T16',3,2):'Directly read Word pages18–19: Validate begins on page18 and continues on page19 through checks, REJECTED/COMPLETED/QUEUED and resubmission conditions.'},
 'table_visual_scope':'All five prior text-matching exceptions were directly read across full-size Word pages6–7,11–14,17–19; repeated headers/page breaks explain the text discontinuities.',
 'reviewed_figures':[1,2]+list(range(7,21)),'reviewed_pages':[6,7,11,12,13,14,15,17,18,19,20,22,23,24,25,26,27,28,29],
 'diagram_visual_scope':'Each original figure and final Mermaid render was directly compared for all labels, endpoints, arrow direction, solid/dashed connectors, decision branches and lane/role boundaries. Native composites12–20 were inspected as full Word pages; figures1–2 received explicit high-priority role/process review.',
 'legend_media':[3,4,5,6],'legend_figures':[3,4,5,6],'legend_page':15,'legend_table':13,'composite_media':list(range(12,20)),
 'limitations':['June2021 source377 and March2024 companion source378 remain separate publications (issue-000010). Part1 business-example headings independently establish all11 exact message identifiers.','Copied functional-role/restriction wording P136/P217 remains issue-000051. Activity status vocabulary and recipient labels remain scoped distinctions, not invented equivalences.','No decorative exclusions are claimed. Source XML examples remain unchanged; omitted namespaces prevent claiming full schema-validation success.','Native embeddings and hidden application layers beyond visible Word figures remain separately inventoried.']}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);print(json.dumps(record(p.parse_args().root.resolve(),CONFIG)))
