---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C65 SafekeepingPlaceRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C65"
source_locations: [{"source_id": "src-000197", "file_pages": [505], "printed_pages": [505], "heading": "17.3 Constraints", "constraint": "C65"}]
---

# C65 SafekeepingPlaceRule

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 505. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

The SafekeepingPlace functionality in the settlement instructions is only to be used for global
custodians that allow their clients to specify where the securities are to be held, for example, in
an ICSD account versus an account at the local CSD.

[Constraint index](<../rules-business.md>)
