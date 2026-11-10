"""Finish all49 source196 table reconciliations with three directly inspected continuations."""
import argparse,json
from pathlib import Path
import kb
from record_source_review import record
from curate_intrabalance import block
CONFIG={'source_id':'src-000196','date':'2026-11-09','key':'settlement-part1','table_count':49,'tables_only':True,'manual_cells':{
 ('T30',4,2):'Directly inspected full Word pages22–23. Processed Yes/No condition begins on page22 and continues below the repeated header on page23, including optional status update after YES and update-status activity after NO.',
 ('T31',7,2):'Directly inspected full Word pages24–25. Settlement Executing Party Processed Yes/No condition continues after the repeated header on page25; both optional YES status update and NO update-status text remain intact.',
 ('T41',9,2):'Directly inspected full Word pages45–46. Settled Yes/No condition is on page45; the qualification Applies to all instructions, resulting from a split or not continues after the repeated header on page46.'},
 'table_visual_scope':'All three text-matching exceptions were directly read across full Word pages22–25 and45–46. These are page-boundary continuations, with repeated headers separating the extracted text; no source-cell content was repaired. Other source tables received complete cell/merge and rendered-text checks, not a claim of individual visual reading of every cell.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);root=ap.parse_args().root.resolve();r=record(root,CONFIG);base=root/'domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026';p=base/'settlement-part1-table-review.md';kb.put(p,kb.front({'template':False,'document_kind':'extraction-audit','review_status':'needs-review','source_ids':['src-000196'],'domain':'securities','updated':CONFIG['date']})+'# Settlement Part1 table reconciliation\n\nAll49 direct-body tables have exact original OOXML cell and merge-map preservation checks, Markdown consistency checks and Word-rendered text corroboration. Three source cells span repeated table headers and were directly inspected on complete Word pages22–25 and45–46.\n\n'+kb.link(p,root/'tracking/reviews/settlement-part1-tables.json','Complete cell counts and exact exception locators')+'\n\n'+CONFIG['table_visual_scope']+' Business-source ambiguities and original wording remain separately recorded in the issue register. This check does not upgrade those interpretations or imply that every page was visually read.\n');
 for name in ['index.md','coverage.md']:
  q=base/name;m,b=kb.metadata(q);kb.put(q,kb.front(m)+block(b,'SETTLEMENT-TABLES-CHECK',kb.link(q,p,'All49 Part1 tables: preservation, rendered-text checks and targeted continuation review')))
 print(json.dumps(r))
