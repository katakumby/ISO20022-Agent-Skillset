---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C29 FXStandingInstructionPresenceRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C29"
source_locations: [{"source_id": "src-000197", "file_pages": [501], "printed_pages": [501], "heading": "17.3 Constraints", "constraint": "C29"}]
---

# C29 FXStandingInstructionPresenceRule

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 501. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If HoldIndicator is present and is value TRUE (Yes), then FXStandingInstruction must not be
present. In ISO 15022,
and therefore in ISO 20022, the FXStandingInstruction indicator can only be used when the
transation is instructed
in a released mode.

[Constraint index](../rules-business.md)
