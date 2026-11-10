---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C44 PairOffTurnRule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C44"
source_locations: [{"source_id": "src-000197", "file_pages": [503], "printed_pages": [503], "heading": "17.3 Constraints", "constraint": "C44"}]
---

# C44 PairOffTurnRule

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 503. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

If LinkedQuantity is present in minimum one occurrence of Linkages, then the type of
settlement transaction must be a pair-off or a turnaround, that is, SettlementParameters/
SecuritiesTransactionType must be PAIR or TURN.
On Condition
    /Linkages[*]/LinkedQuantity is present
Following Must be True
    /SettlementParameters/SecuritiesTransactionType/Code Must be equal to 
value 'PairOff'
 Or    /SettlementParameters/SecuritiesTransactionType/Code Must be equal to 
value 'Turnaround'
This constraint is defined at the MessageDefinition level.

[Constraint index](../rules-business.md)
