---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C10 BlockTradeGuideline"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C10"
source_locations: [{"source_id": "src-000197", "file_pages": [498], "printed_pages": [498], "heading": "17.3 Constraints", "constraint": "C10"}]
---

# C10 BlockTradeGuideline

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 498. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

In a block trade instruction, the total number of children must be provided using
TotalOfLinkedInstructions.
The CurrentInstructionNumber of the parent must be 000000. The children must have an
incremental CurrentInstructionNumber from 1 to 999999.
For more details, see the relevant market practice document on www.smpg.info.

[Constraint index](<../rules-business.md>)
