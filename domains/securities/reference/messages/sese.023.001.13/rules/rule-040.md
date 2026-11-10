---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C40 MarketTypeAndIdentificationRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C40"
source_locations: [{"source_id": "src-000197", "file_pages": [502], "printed_pages": [502], "heading": "17.3 Constraints", "constraint": "C40"}]
---

# C40 MarketTypeAndIdentificationRule

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 502. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.

[Constraint index](<../rules-business.md>)
