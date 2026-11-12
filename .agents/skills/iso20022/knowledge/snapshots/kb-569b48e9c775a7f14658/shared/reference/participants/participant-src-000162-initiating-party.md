---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-initiating-party"
title: "Initiating Party"
source_labels: ["Initiating Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[9]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000162", "locator": "T6 row9; P472"}]
flows: []
process_sections: ["flow-src-000162-p468-fito-ficustomer-direct-debit"]
message_ids: []
message_families: ["pacs.003"]
search_terms: ["Initiating Party", "pacs.003"]
limitations: ["Scoped source role; classification terminology conflict remains issue-000054.", "No unsupported cross-source equivalence or fixed institutional role inferred."]
manual_curated: true
domains: ["payments"]
issue_ids: ["issue-000054"]
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "Cited definition/activity/flow evidence reviewed; terminology conflict remains."}
flow_ids: ["flow-src-000162-p468-fito-ficustomer-direct-debit", "flow-src-000162-p499-creditor-negative-fito-fipayment-status-report-initiated-by-clearing-a", "flow-src-000162-p509-negative-fito-fipayment-status-report-initiated-by-debtor-agent", "flow-src-000162-p529-fito-fipayment-status-report-to-confirm-processability-of-fito-ficusto", "flow-src-000162-p539-payment-return-initiated-by-debtor-agent", "flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit"]
---



























# Initiating Party

Business context: Payments Clearing and Settlement. Source classification: functional participant role.

## Definition

Party initiating the payment to an agent. In the payment context, this can either be the debtor (in a credit transfer), the creditor (in a direct debit), or a party that initiates the payment on behalf of the debtor or creditor. 

Evidence: [T6](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0006.md), source row 9.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Party](participant-src-000162-party.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 9, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pacs.003`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Initiating Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md).

<!-- CLEARING-ROLE-REVIEW -->
## Curated responsibilities and contextual roles

Initiates payment; debtor for CT, creditor for DD or a party acting on their behalf. P472 identifies initiating creditor. (T6 row9; P472)

T1 and P102–104/T8 use BusinessRole/Participant terminology inconsistently (issue-000054). Literal source definitions are retained; functional roles are not fixed institutions. No identifier scheme is asserted beyond supplied evidence.
<!-- /CLEARING-ROLE-REVIEW -->

<!-- CLEARING-FLOW-468 -->
[FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md)
<!-- /CLEARING-FLOW-468 -->

<!-- CLEARING-FLOW-499 -->
[CreditorNegative FIToFIPaymentStatusReport initiated by Clearing and Settlement Agent](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p499-creditor-negative-fito-fipayment-status-report-initiated-by-clearing-a.md)
<!-- /CLEARING-FLOW-499 -->

<!-- CLEARING-FLOW-509 -->
[Negative FIToFIPaymentStatusReport Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p509-negative-fito-fipayment-status-report-initiated-by-debtor-agent.md)
<!-- /CLEARING-FLOW-509 -->

<!-- CLEARING-FLOW-529 -->
[FIToFIPaymentStatusReport to confirm Processability of FIToFICustomerDirectDebit instruction](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p529-fito-fipayment-status-report-to-confirm-processability-of-fito-ficusto.md)
<!-- /CLEARING-FLOW-529 -->

<!-- CLEARING-FLOW-539 -->
[PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md)
<!-- /CLEARING-FLOW-539 -->

<!-- CLEARING-FLOW-556 -->
[FIToFIPaymentReversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit.md)
<!-- /CLEARING-FLOW-556 -->
