---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-forwarding-agent"
title: "Forwarding Agent"
source_labels: ["Forwarding Agent"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[8]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000162", "locator": "T6 row8; P472"}]
flows: []
process_sections: ["flow-src-000162-p468-fito-ficustomer-direct-debit"]
message_ids: []
message_families: ["pacs.003"]
search_terms: ["Forwarding Agent", "pacs.003"]
limitations: ["Scoped source role; classification terminology conflict remains issue-000054.", "No unsupported cross-source equivalence or fixed institutional role inferred."]
manual_curated: true
domains: ["payments"]
issue_ids: ["issue-000054"]
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "Cited definition/activity/flow evidence reviewed; terminology conflict remains."}
flow_ids: ["flow-src-000162-p468-fito-ficustomer-direct-debit"]
---







# Forwarding Agent

Business context: Payments Clearing and Settlement. Source classification: functional participant role.

## Definition

Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution.

Evidence: [T6](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0006.md), source row 8.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Financial Institution](participant-src-000162-financial-institution.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 8, column 2 |
| Can play the functional participant role in this source context | [Clearing System](participant-src-000162-clearing-system.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 8, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pacs.003`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Forwarding Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx).

<!-- CLEARING-ROLE-REVIEW -->
## Curated responsibilities and contextual roles

Receives initiating-party payment and forwards to next execution-chain agent. P472 allows CustomerDirectDebitInitiation via forwarding agent even though figure37 shows direct creditor-agent route. (T6 row8; P472)

T1 and P102–104/T8 use BusinessRole/Participant terminology inconsistently (issue-000054). Literal source definitions are retained; functional roles are not fixed institutions. No identifier scheme is asserted beyond supplied evidence.
<!-- /CLEARING-ROLE-REVIEW -->

<!-- CLEARING-FLOW-468 -->
[FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md)
<!-- /CLEARING-FLOW-468 -->
