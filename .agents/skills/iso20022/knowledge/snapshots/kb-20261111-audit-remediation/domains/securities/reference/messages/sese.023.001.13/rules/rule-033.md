---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C33 InvestorCountryCodeRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C33"
source_locations: [{"source_id": "src-000197", "file_pages": [502], "printed_pages": [502], "heading": "17.3 Constraints", "constraint": "C33"}]
---

# C33 InvestorCountryCodeRule

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 502. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If Investor is used with a country code, then the country code specifies the nationality of the
investor, for example, for the settlement of certain securities (that is, airlines, defence
manufacturers) under the EU legislation.

[Constraint index](../rules-business.md)
