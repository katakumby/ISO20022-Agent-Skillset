---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C13 BuyToCoverRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C13"
source_locations: [{"source_id": "src-000197", "file_pages": [499], "printed_pages": [499], "heading": "17.3 Constraints", "constraint": "C13"}]
---

# C13 BuyToCoverRule

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 499. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If SettlementParameters/SettlementTransactionCondition BuyToCover (BUTC) is present then
at least one Linkage must be present with the reference of the sell instruction (may be more
than one) to be covered by the concerned buy.
This constraint is defined at the MessageDefinition level.

[Constraint index](<../rules-business.md>)
