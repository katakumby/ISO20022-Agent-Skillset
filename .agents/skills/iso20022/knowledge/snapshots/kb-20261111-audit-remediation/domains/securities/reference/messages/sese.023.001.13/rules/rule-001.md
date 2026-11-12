---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C1 ActiveCurrency"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C1"
source_locations: [{"source_id": "src-000197", "file_pages": [497], "printed_pages": [497], "heading": "17.3 Constraints", "constraint": "C1"}]
---

# C1 ActiveCurrency

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 497. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.

[Constraint index](../rules-business.md)
