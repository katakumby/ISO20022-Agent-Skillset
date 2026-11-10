---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-payment-settlement-agent"
title: "PaymentSettlementAgent"
source_labels: ["PaymentSettlementAgent"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[14]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[15]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Credit Transfer"], "locator": "/w:document/w:body/w:tbl[24]/w:tr[16]", "paragraph_id": null, "table_id": "T24"}, {"source_id": "src-000162", "locator": "T24 rows14–16; figure7; P140"}]
flows: []
process_sections: []
message_ids: []
message_families: []
search_terms: ["PaymentSettlementAgent"]
limitations: ["Scoped source role; classification terminology conflict remains issue-000054.", "No unsupported cross-source equivalence or fixed institutional role inferred."]
manual_curated: true
domains: ["payments"]
issue_ids: ["issue-000054"]
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "Cited definition/activity/flow evidence reviewed; terminology conflict remains."}
flow_ids: ["flow-src-000162-p138-credit-transfer"]
---







# PaymentSettlementAgent

Business context: Payments Clearing and Settlement. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Assess interbank payment risk |  | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 14 |
| Settle payment order |  | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 15 |
| Inform about settlement |  | Initiator | [T24](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0024.md) row 16 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Financial Institution](participant-src-000162-financial-institution.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 13, column 2 |
| Can play the functional participant role in this source context | [Clearing System](participant-src-000162-clearing-system.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 13, column 3 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `PaymentSettlementAgent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx).

<!-- CLEARING-ROLE-REVIEW -->
## Curated responsibilities and contextual roles

Assesses interbank risk, settles if possible and informs clearing agent of settlement failure/passed outcome. Generic activity role; P140 gives concrete-agent examples separately. (T24 rows14–16; figure7; P140)

T1 and P102–104/T8 use BusinessRole/Participant terminology inconsistently (issue-000054). Literal source definitions are retained; functional roles are not fixed institutions. No identifier scheme is asserted beyond supplied evidence.
<!-- /CLEARING-ROLE-REVIEW -->

<!-- CLEARING-FLOW-138 -->
[Credit Transfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p138-credit-transfer.md)
<!-- /CLEARING-FLOW-138 -->
