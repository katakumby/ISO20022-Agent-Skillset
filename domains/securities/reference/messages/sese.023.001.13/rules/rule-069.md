---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C69 SettlementAmountRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C69"
source_locations: [{"source_id": "src-000197", "file_pages": [505, 506], "printed_pages": [505, 506], "heading": "17.3 Constraints", "constraint": "C69"}]
---

# C69 SettlementAmountRule

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 505, 506. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If the instruction is against payment, then SettlementAmount must be present.
On Condition
    /SettlementTypeAndAdditionalParameters/Payment is equal to value 
'AgainstPaymentSettlement'
Following Must be True
    /SettlementAmount Must be present
This constraint is defined at the MessageDefinition level.

[Constraint index](<../rules-business.md>)
