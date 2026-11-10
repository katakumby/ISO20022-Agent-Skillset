---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-receiving-party-all-levels"
title: "Receiving Party (all levels)"
source_labels: ["Receiving Party (all levels)"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Transparency of Holdings"], "locator": "/w:document/w:body/w:tbl[42]/w:tr[3]", "paragraph_id": null, "table_id": "T42"}, {"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Reconciliation (Statements)", "Transparency of Holdings"], "locator": "/w:document/w:body/w:tbl[42]/w:tr[4]", "paragraph_id": null, "table_id": "T42"}]
flows: ["flow-src-000095-p218-transparency-of-holdings"]
process_sections: []
message_ids: []
message_families: ["semt.002"]
search_terms: ["Receiving Party (all levels)", "semt.002"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p218-transparency-of-holdings"]
---



# Receiving Party (all levels)

Business context: Investment Funds. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Aggregate Holdings | Upon receipt of the Transparency of Holdings statement, the receiver combines data from its own books with the information received in the statement, and identifies any discrepancies to be reported as “account differences”. | Initiator | [T42](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0042.md) row 3 |
| Reconcile Aggregated Holdings | The receiver books all required updates in its own accounts for alignment. | Initiator | [T42](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0042.md) row 4 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Transparency of Holdings](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `semt.002`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Receiving Party (all levels)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx).

<!-- FUNDS-PROCESS-fig-0014 -->
[Report Transparency of Holdings](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0014.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p218-transparency-of-holdings.md)
<!-- /FUNDS-PROCESS-fig-0014 -->
