---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C2 ActiveOrHistoricCurrency"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C2"
source_locations: [{"source_id": "src-000197", "file_pages": [497], "printed_pages": [497], "heading": "17.3 Constraints", "constraint": "C2"}]
---

# C2 ActiveOrHistoricCurrency

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 497. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.

[Constraint index](<../rules-business.md>)
