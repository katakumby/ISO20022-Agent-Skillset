---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-payment-clearing-agent-b"
title: "PaymentClearingAgent B"
source_labels: ["PaymentClearingAgent B"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[7]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[8]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[9]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[10]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[11]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[12]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[13]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "locator": "T24 rows7–13; figure7"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["PaymentClearingAgent B"]
limitations: ["Scoped source role; classification terminology conflict remains issue-000054.", "No unsupported cross-source equivalence or fixed institutional role inferred."]
manual_curated: true
domains: ["payments"]
issue_ids: ["issue-000054"]
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "Cited definition/activity/flow evidence reviewed; terminology conflict remains."}
flow_ids: ["flow-src-000162-p138-credit-transfer"]
---







# PaymentClearingAgent B

Business context: Payments Clearing and Settlement. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Receive payment order | The PaymentClearingAgent acknowledges receipt of the payment order (technical) and proceeds to next step. | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 7 |
| Apply technical validation | The PaymentClearingAgent applies technical validation on the payment order. Technical validation may comprise syntactic validation (conformance of the payment order with its technical definition), semantic validation ( message, through to technical content consistency). | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 8 |
| Apply business validation |  | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 9 |
| Reject payment order | The PaymentClearingAgent rejects the payment order to the preceding PaymentClearingAgent and appends a relevant reject reason code explaining the reason for the reject. | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 10 |
| Sort interbank payment |  | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 11 |
| Calculate settlement positions |  | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 12 |
| Prepare onward interbank payment | The PaymentClearingAgent prepares the outgoing payment instruction and selects the next PaymentClearingAgent and/or the clearing channel through which the payment instruction will be cleared and/or settled. | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 13 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `PaymentClearingAgent B`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md).

<!-- CLEARING-ROLE-REVIEW -->
## Curated responsibilities and contextual roles

Receives payment, validates technically/business-wise, rejects with reason or sorts/calculates positions/prepares onward payment after settlement information. B is a separate source occurrence. (T24 rows7–13; figure7)

T1 and P102–104/T8 use BusinessRole/Participant terminology inconsistently (issue-000054). Literal source definitions are retained; functional roles are not fixed institutions. No identifier scheme is asserted beyond supplied evidence.
<!-- /CLEARING-ROLE-REVIEW -->

<!-- CLEARING-FLOW-138 -->
[Credit Transfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p138-credit-transfer.md)
<!-- /CLEARING-FLOW-138 -->
