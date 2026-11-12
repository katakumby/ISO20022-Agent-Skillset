---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C16 CurrencyAmount"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C16"
source_locations: [{"source_id": "src-000197", "file_pages": [499], "printed_pages": [499], "heading": "17.3 Constraints", "constraint": "C16"}]
---

# C16 CurrencyAmount

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 499. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.

[Constraint index](../rules-business.md)
