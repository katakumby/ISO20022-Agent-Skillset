---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C66 SecuritiesFinancingSettlementRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C66"
source_locations: [{"source_id": "src-000197", "file_pages": [505], "printed_pages": [505], "heading": "17.3 Constraints", "constraint": "C66"}]
---

# C66 SecuritiesFinancingSettlementRule

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 505. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

In the framework of Securities Financing (repo, reverse repo, sec lending, sec borrowing), the
SettlementInstruction can only be used for the plain vanilla settlement of the opening leg and
closing leg.
This constraint is defined at the MessageDefinition level.

[Constraint index](../rules-business.md)
