---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
participant_id: "participant-src-000095-transferee-s-bank-executing-party"
title: "Transferee's Bank (Executing Party)"
source_labels: ["Transferee's Bank (Executing Party)"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000095", "heading_path": ["Description of BusinessActivities", "Stock Transfers (Single Leg Transfer)"], "locator": "/w:document/w:body/w:tbl[43]/w:tr[7]", "paragraph_id": null, "table_id": "T43"}]
flows: ["flow-src-000095-p221-stock-transfers-single-leg-transfer"]
process_sections: []
message_ids: []
message_families: ["sese.001", "sese.005", "sese.007", "sese.011"]
search_terms: ["Transferee's Bank (Executing Party)", "sese.001", "sese.005", "sese.007", "sese.011"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000095-p221-stock-transfers-single-leg-transfer"]
---



# Transferee's Bank (Executing Party)

Business context: Investment Funds. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Inform End Client | The transferee's bank informs the end-client of the transfer. | Initiator | [T43](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000095/tables/tbl-0043.md) row 7 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Stock Transfers (Single Leg Transfer)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `sese.001`, `sese.005`, `sese.007`, `sese.011`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Transferee's Bank (Executing Party)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000095](../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx).

<!-- FUNDS-PROCESS-fig-0015 -->
[Transfer Flow — Single Leg (from transfer agent perspective)](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-processes/fig-0015.md) · [Flow responsibilities](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/flow-src-000095-p221-stock-transfers-single-leg-transfer.md)
<!-- /FUNDS-PROCESS-fig-0015 -->
