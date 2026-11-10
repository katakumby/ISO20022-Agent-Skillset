---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C53 RegistrationDetailsRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C53"
source_locations: [{"source_id": "src-000197", "file_pages": [504], "printed_pages": [504], "heading": "17.3 Constraints", "constraint": "C53"}]
---

# C53 RegistrationDetailsRule

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 504. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If SettlementParameters/Registration is present with code YREG (Registration to take place),
then additional registration details must be specified in the AdditonalInformation/
RegistrationDetails field of the Party (Receiving or DeliveringSettlementParties) under whom
the registration must take place, unless this information is already available at the account
servicer via standing instruction/SLA.
This constraint is defined at the MessageDefinition level.

[Constraint index](<../rules-business.md>)
