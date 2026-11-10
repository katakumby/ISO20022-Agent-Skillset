---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C21 CurrentInstructionNumberRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C21"
source_locations: [{"source_id": "src-000197", "file_pages": [500], "printed_pages": [500], "heading": "17.3 Constraints", "constraint": "C21"}]
---

# C21 CurrentInstructionNumberRule

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 500. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.

[Constraint index](<../rules-business.md>)
