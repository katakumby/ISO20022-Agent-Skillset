---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C36 ISO8532AndIssuerSchemeNameRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C36"
source_locations: [{"source_id": "src-000197", "file_pages": [502], "printed_pages": [502], "heading": "17.3 Constraints", "constraint": "C36"}]
---

# C36 ISO8532AndIssuerSchemeNameRule

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 502. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.

[Constraint index](../rules-business.md)
