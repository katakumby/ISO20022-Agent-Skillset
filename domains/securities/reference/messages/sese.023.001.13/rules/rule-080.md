---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C80 WithLinkageRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C80"
source_locations: [{"source_id": "src-000197", "file_pages": [510], "printed_pages": [510], "heading": "17.3 Constraints", "constraint": "C80"}]
---

# C80 WithLinkageRule

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 510. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.

[Constraint index](<../rules-business.md>)
