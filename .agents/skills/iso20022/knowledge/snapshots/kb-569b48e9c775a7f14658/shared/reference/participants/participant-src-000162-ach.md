---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-ach"
title: "ACH"
source_labels: ["ACH"]
role_type: "activity participant; classification not established"
aliases: ["ACH (System Transaction Administrator)"]
source_locations: [{"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Direct debit instruction "], "locator": "/w:document/w:body/w:tbl[25]/w:tr[8]", "paragraph_id": null, "table_id": "T25"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Direct Debit Reversal"], "locator": "/w:document/w:body/w:tbl[26]/w:tr[6]", "paragraph_id": null, "table_id": "T26"}, {"source_id": "src-000162", "locator": "Figures8/10; T25 row8; T26 rows4/6"}]
flows: ["flow-src-000162-p154-direct-debit-instruction", "flow-src-000162-p161-direct-debit-reversal"]
process_sections: []
message_ids: []
message_families: ["pacs.010"]
search_terms: ["ACH", "pacs.010"]
limitations: ["Scoped source role; classification terminology conflict remains issue-000054.", "No unsupported cross-source equivalence or fixed institutional role inferred."]
manual_curated: true
domains: ["payments"]
issue_ids: ["issue-000054"]
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "Cited definition/activity/flow evidence reviewed; terminology conflict remains."}
flow_ids: ["flow-src-000162-p154-direct-debit-instruction", "flow-src-000162-p159-request-refund-direct-debit", "flow-src-000162-p161-direct-debit-reversal"]
---















# ACH

Business context: Payments Clearing and Settlement. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Report Direct Debit Settlement Proceeds | Process that includes the calculation of the settlement positions and transmission of the settlement information to the settlement agent. | Initiator | [T25](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0025.md) row 8 |
| Clear Direct Debit Reversal | Preparation of the payment information for the next agent in the chain (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the next agent. | Initiator | [T26](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0026.md) row 6 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Direct debit instruction](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p154-direct-debit-instruction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct Debit Reversal](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p161-direct-debit-reversal.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pacs.010`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `ACH`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md).

<!-- CLEARING-ROLE-REVIEW -->
## Curated responsibilities and contextual roles

Activity clearing participant; source lane ACH (System Transaction Administrator) accepts/rejects and clears DD and return. T25 describes settlement positions/information; T26 reversal clearing. (Figures8/10; T25 row8; T26 rows4/6)

T1 and P102–104/T8 use BusinessRole/Participant terminology inconsistently (issue-000054). Literal source definitions are retained; functional roles are not fixed institutions. No identifier scheme is asserted beyond supplied evidence.
<!-- /CLEARING-ROLE-REVIEW -->

<!-- CLEARING-FLOW-154 -->
[Direct debit instruction](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p154-direct-debit-instruction.md)
<!-- /CLEARING-FLOW-154 -->

<!-- CLEARING-FLOW-159 -->
[Request Refund Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p159-request-refund-direct-debit.md)
<!-- /CLEARING-FLOW-159 -->

<!-- CLEARING-FLOW-161 -->
[Direct Debit Reversal](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p161-direct-debit-reversal.md)
<!-- /CLEARING-FLOW-161 -->
