"""Record completed source380 visual checks, without upgrading source ambiguities."""
import argparse,json
from pathlib import Path
from record_source_review import record
CONFIG={'source_id':'src-000380','date':'2026-11-09','key':'settlement-restrictions','table_count':14,'manual_cells':{},
 'table_visual_scope':'Whole Word pages8 and14–23 were inspected for message lists, participant definitions/matrix, process conditions, legend and activity-table layout/continuations; Functionality pages9–12 were also read against the extracted clauses. No text-matching exception required a manual correction.',
 'reviewed_figures':[1,2,3,4,5,10,11,12,13,14],'reviewed_pages':list(range(6,25)),
 'diagram_visual_scope':'All ten original figures and final Mermaid renderings were directly compared for labels, endpoints, message direction, solid/dashed connectors, decision branches and scoped roles. Figures2–3 were checked as complete native Word composites on pages7–8. Role/process scope figure4 and native use-case figure5 received explicit label/edge review. Source colors, pictograms and bar geometry have the documented notation adaptations.',
 'legend_media':[8,9,10,11],'legend_figures':[6,7,8,9],'legend_page':17,'legend_table':9,'composite_media':[2,3,4,5],
 'limitations':['Source wording P200/P235 remains issue-000056; exact source content is unchanged.','Unversioned context families do not inherit arbitrary exact schema versions. The seven semt definitions are bound through companion Part2 src-000381 September2025.','No decorative exclusion is claimed. Four notation glyphs and all native composite components remain retained. Hidden embedded-application layers beyond visible Word content are separately inventoried.','Example payload excerpts deliberately omit wrapper/header content under P312. XML well-formedness is checked separately; complete XSD instance validation is not claimed.']}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);print(json.dumps(record(p.parse_args().root.resolve(),CONFIG)))
