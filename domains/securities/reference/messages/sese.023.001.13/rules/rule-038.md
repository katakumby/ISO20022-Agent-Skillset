---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C38 LinkageGuideline"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C38"
source_locations: [{"source_id": "src-000197", "file_pages": [502], "printed_pages": [502], "heading": "17.3 Constraints", "constraint": "C38"}]
---

# C38 LinkageGuideline

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 502. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

Global market practice rules on the use of the linkages exists for various business scenarios
such as cancellations, settlement confirmation but also more complex processes like pair-off,
back-to-back, block trades, sell-buy back, buy-sell back, securities lending and borrowing.
For more details, see the relevant market practice documents on www.smpg.info.
This constraint is defined at the MessageDefinition level.

[Constraint index](<../rules-business.md>)
