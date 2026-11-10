---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C73 ShortLongNumberRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C73"
source_locations: [{"source_id": "src-000197", "file_pages": [507], "printed_pages": [507], "heading": "17.3 Constraints", "constraint": "C73"}]
---

# C73 ShortLongNumberRule

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 507. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.

[Constraint index](../rules-business.md)
