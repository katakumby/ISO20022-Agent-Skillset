---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
participant_id: "participant-src-000320-relevant-ca"
title: "Relevant CA"
source_labels: ["Relevant CA"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:tbl[31]/w:tr[7]", "paragraph_id": null, "table_id": "T31"}]
flows: ["flow-src-000320-p162-financial-instrument-transaction-report"]
process_sections: ["flow-src-000320-p248-financial-instrument-transaction-report"]
message_ids: ["auth.016.001.03"]
message_families: ["auth.016"]
search_terms: ["Relevant CA", "auth.016"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000320-p162-financial-instrument-transaction-report", "flow-src-000320-p248-financial-instrument-transaction-report"]
---

# Relevant CA

Business context: Transactions and Financial Instruments Data Reporting. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Process Exchanged Message and Generate Status | Each exchanged message is checked for completeness and correctness of message. Once complete, generate the status advice file for distribution | Initiator | [T31](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0031.md) row 7 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Financial Instrument Transaction Report](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p162-financial-instrument-transaction-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Financial Instrument Transaction Report](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p248-financial-instrument-transaction-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `auth.016`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Relevant CA`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000320](../../../evidence/omitted/b0e9dc6419046e4d0523e995.md).




<!-- FITRR-SEQUENCES -->
## Source-reviewed sequence participation

- [Transaction reporting and authority exchange](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p248-financial-instrument-transaction-report.md) · [literal sender/receiver and conditions](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-sequences/fig-0036.md)



<!-- FITRR-RESPONSIBILITIES -->
## Source-assigned activities

| Activity | Source responsibility | Precise evidence |
| --- | --- | --- |
| Process Exchanged Message and Generate Status | Each exchanged message is checked for completeness and correctness of message. Once complete, generate the status advice file for distribution | [T31 row 7](../../../domains/securities/reference/message-sets/fitrr/2025/documents/src-000320/tables/tbl-0031.md) |


The source Initiator cells govern this table. T26 assigns Receive Message to SA while its description and diagram identify CA; [issue-000036](../../../tracking/issues.md#issue-000036) preserves the conflict. T18 has a separate calculation-result role conflict, [issue-000032](../../../tracking/issues.md#issue-000032).
<!-- /FITRR-RESPONSIBILITIES -->

<!-- FITRR-ACTIVITY-16 -->
[Transaction reporting and authority exchange](../../../domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0016.md) · [Activities and responsibilities](../../../domains/securities/reference/message-sets/fitrr/2025/flows/flow-src-000320-p162-financial-instrument-transaction-report.md)
<!-- /FITRR-ACTIVITY-16 -->
