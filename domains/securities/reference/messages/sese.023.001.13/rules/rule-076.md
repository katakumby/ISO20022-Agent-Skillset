---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C76 TradeDateTimeUTCRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C76"
source_locations: [{"source_id": "src-000197", "file_pages": [507], "printed_pages": [507], "heading": "17.3 Constraints", "constraint": "C76"}]
---

# C76 TradeDateTimeUTCRule

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 507. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time
of the place of trade, for example, of the stock exchange, or of the selling broker for OTC.

[Constraint index](<../rules-business.md>)
