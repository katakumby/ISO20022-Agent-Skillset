---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-payment-clearing-agent-a"
title: "PaymentClearingAgent A"
source_labels: ["PaymentClearingAgent A"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[2]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[3]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[4]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[5]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[6]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "locator": "T24 rows2–6; figure7"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["PaymentClearingAgent A"]
limitations: ["Scoped source role; classification terminology conflict remains issue-000054.", "No unsupported cross-source equivalence or fixed institutional role inferred."]
manual_curated: true
domains: ["payments"]
issue_ids: ["issue-000054"]
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "Cited definition/activity/flow evidence reviewed; terminology conflict remains."}
flow_ids: ["flow-src-000162-p138-credit-transfer"]
---







# PaymentClearingAgent A

Business context: Payments Clearing and Settlement. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Prepare onward interbank payment | The PaymentClearingAgent prepares the outgoing payment instruction and selects the next PaymentClearingAgent and/or the clearing channel through which the payment instruction will be cleared and/or settled. | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 2 |
| Send payment | The PaymentClearingAgent sends out the payment instruction to the selected channel/PaymentClearingAgent. | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 3 |
| Assess reject reason code | The PaymentClearingAgent assesses the reject reason code provided by the rejecting PaymentClearingAgent. | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 4 |
| Repair payment order | The PaymentClearingAgent reformats/supplements the original payment order for re-submission to the appropriate clearing channel/PaymentClearingAgent. | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 5 |
| Recycle payment order | The PaymentClearingAgent recycles the rejected payment order. Recycling can be by downgrading the STP level under which the payment order can be cleared and settled, or selecting another channel for clearing and settling the payment. | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 6 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `PaymentClearingAgent A`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md).

<!-- CLEARING-ROLE-REVIEW -->
## Curated responsibilities and contextual roles

Prepares and sends payment; assesses rejects, repairs and resends or recycles rejected orders. A is a source occurrence, not an institution name. (T24 rows2–6; figure7)

T1 and P102–104/T8 use BusinessRole/Participant terminology inconsistently (issue-000054). Literal source definitions are retained; functional roles are not fixed institutions. No identifier scheme is asserted beyond supplied evidence.
<!-- /CLEARING-ROLE-REVIEW -->

<!-- CLEARING-FLOW-138 -->
[Credit Transfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p138-credit-transfer.md)
<!-- /CLEARING-FLOW-138 -->
