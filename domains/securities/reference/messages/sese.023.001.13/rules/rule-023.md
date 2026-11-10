---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C23 DeliveringDepositoryAndParty1Rule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C23"
source_locations: [{"source_id": "src-000197", "file_pages": [501], "printed_pages": [501], "heading": "17.3 Constraints", "constraint": "C23"}]
---

# C23 DeliveringDepositoryAndParty1Rule

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 501. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If the instruction is a receive and no standing settlement instruction applies, then
DeliveringDepository and Party1 must be present.
On Condition
    /SettlementTypeAndAdditionalParameters/SecuritiesMovementType is equal to 
value 'Receive'
 And    /StandingSettlementInstructionDetails is absent
Following Must be True
    /DeliveringSettlementParties/Depository Must be present
 And    /DeliveringSettlementParties/Party1 Must be present
This constraint is defined at the MessageDefinition level.

[Constraint index](<../rules-business.md>)
