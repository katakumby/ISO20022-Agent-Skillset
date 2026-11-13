---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-creditor"
title: "Creditor"
source_labels: ["Creditor"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[3]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000162", "heading_path": ["Description of BusinessActivities", "Direct Debit", "Direct Debit Reversal"], "locator": "/w:document/w:body/w:tbl[26]/w:tr[2]", "paragraph_id": null, "table_id": "T26"}, {"source_id": "src-000162", "locator": "T6 row3; P481–488; P557–566; P581–588; P596–600; P643"}]
flows: ["flow-src-000162-p119-sort-interbank-payment", "flow-src-000162-p127-process-direct-debit", "flow-src-000162-p129-process-return-request-for-refund", "flow-src-000162-p161-direct-debit-reversal"]
process_sections: ["flow-src-000162-p142-direct-debit", "flow-src-000162-p170-fito-ficustomer-credit-transfer", "flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p296-financial-institution-credit-transfer", "flow-src-000162-p303-debtor-and-creditor-are-correspondents", "flow-src-000162-p307-out-of-scope", "flow-src-000162-p317-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p324-out-of-scope", "flow-src-000162-p353-debtor-and-creditor-are-correspondents", "flow-src-000162-p367-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents", "flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p468-fito-ficustomer-direct-debit", "flow-src-000162-p499-creditor-negative-fito-fipayment-status-report-initiated-by-clearing-a", "flow-src-000162-p509-negative-fito-fipayment-status-report-initiated-by-debtor-agent", "flow-src-000162-p539-payment-return-initiated-by-debtor-agent", "flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit", "flow-src-000162-p580-financial-institution-direct-debit", "flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents", "flow-src-000162-p590-out-of-scope", "flow-src-000162-p595-creditor-agent-and-debtor-agent-are-correspondents", "flow-src-000162-p602-out-of-scope", "flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents", "flow-src-000162-p617-out-of-scope", "flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario", "flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit", "flow-src-000162-p645-creditor-sends-fito-fipayment-status-request"]
message_ids: []
message_families: ["pacs.002", "pacs.003", "pacs.004", "pacs.007", "pacs.008", "pacs.009", "pacs.010", "pacs.028"]
search_terms: ["Creditor", "pacs.002", "pacs.003", "pacs.004", "pacs.007", "pacs.008", "pacs.009", "pacs.010", "pacs.028"]
limitations: ["Scoped source role; classification terminology conflict remains issue-000054.", "No unsupported cross-source equivalence or fixed institutional role inferred."]
manual_curated: true
domains: ["payments"]
issue_ids: ["issue-000054"]
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "Cited definition/activity/flow evidence reviewed; terminology conflict remains."}
flow_ids: ["flow-src-000162-p154-direct-debit-instruction", "flow-src-000162-p157-return-direct-debit", "flow-src-000162-p159-request-refund-direct-debit", "flow-src-000162-p161-direct-debit-reversal", "flow-src-000162-p177-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p198-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents", "flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p249-debtor-agent-and-the-creditor-agent-are-correspondents", "flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p292-debtor-agent-sends-fito-fipayment-status-request", "flow-src-000162-p303-debtor-and-creditor-are-correspondents", "flow-src-000162-p310-debtor-and-creditor-agent-are-correspondents", "flow-src-000162-p317-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p327-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p335-debtor-agent-and-creditor-agent-are-not-correspondents", "flow-src-000162-p353-debtor-and-creditor-are-correspondents", "flow-src-000162-p360-debtor-and-creditor-agent-are-correspondents", "flow-src-000162-p367-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p379-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p391-debtor-agent-and-creditor-agent-not-correspondents", "flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents", "flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents", "flow-src-000162-p463-debtor-sends-fito-fipayment-status-request", "flow-src-000162-p468-fito-ficustomer-direct-debit", "flow-src-000162-p499-creditor-negative-fito-fipayment-status-report-initiated-by-clearing-a", "flow-src-000162-p509-negative-fito-fipayment-status-report-initiated-by-debtor-agent", "flow-src-000162-p529-fito-fipayment-status-report-to-confirm-processability-of-fito-ficusto", "flow-src-000162-p539-payment-return-initiated-by-debtor-agent", "flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit", "flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents", "flow-src-000162-p595-creditor-agent-and-debtor-agent-are-correspondents", "flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents", "flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario", "flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit", "flow-src-000162-p645-creditor-sends-fito-fipayment-status-request"]
---









































































































































































# Creditor

Business context: Payments Clearing and Settlement. Source classification: functional participant role.

## Definition

Party to which an amount of money is due. In the context of the payment model, the creditor is also the credit account owner.

Evidence: [T6](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0006.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Request reversal of the Direct Debit payment order | The creditor identifies the original direct debit instruction (or a file of direct debit instructions) and generates an offsetting transaction in favor of the debtor under quotation of the reversal reason. | Initiator | [T26](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0026.md) row 2 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Party](participant-src-000162-party.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 3, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Sort Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p119-sort-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Process direct debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p127-process-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Process Return/Request for Refund](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p129-process-return-request-for-refund.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p142-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct Debit Reversal](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p161-direct-debit-reversal.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFICustomerCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p170-fito-ficustomer-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FinancialInstitutionCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p296-financial-institution-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p303-debtor-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of Scope](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p307-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p317-debtor-agent-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of Scope](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p324-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p353-debtor-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p367-debtor-agent-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor and Creditor are direct Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CreditorNegative FIToFIPaymentStatusReport initiated by Clearing and Settlement Agent](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p499-creditor-negative-fito-fipayment-status-report-initiated-by-clearing-a.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Negative FIToFIPaymentStatusReport Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p509-negative-fito-fipayment-status-report-initiated-by-debtor-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFIPaymentReversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FinancialInstitutionDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p580-financial-institution-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Creditor and Debtor Agent are correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of Scope](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p590-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Creditor Agent and Debtor Agent are correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p595-creditor-agent-and-debtor-agent-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of Scope](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p602-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Creditor Agent and Debtor Agent are not correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of Scope](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p617-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Payment Return in a FinancialInstitutionDirectDebit scenario](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFIPaymentReversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Creditor sends FIToFIPaymentStatusRequest](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p645-creditor-sends-fito-fipayment-status-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pacs.002`, `pacs.003`, `pacs.004`, `pacs.007`, `pacs.008`, `pacs.009`, `pacs.010`, `pacs.028`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Creditor`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md).

<!-- CLEARING-ROLE-REVIEW -->
## Curated responsibilities and contextual roles

Owns credit account in T6. Originates collection; may dematerialise mandate and pre-notify; can reverse a paid duplicate after settlement. For FI direct debit, creditor is a financial institution and can request funds at another account. (T6 row3; P481–488; P557–566; P581–588; P596–600; P643)

T1 and P102–104/T8 use BusinessRole/Participant terminology inconsistently (issue-000054). Literal source definitions are retained; functional roles are not fixed institutions. No identifier scheme is asserted beyond supplied evidence.
<!-- /CLEARING-ROLE-REVIEW -->

<!-- CLEARING-FLOW-154 -->
[Direct debit instruction](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p154-direct-debit-instruction.md)
<!-- /CLEARING-FLOW-154 -->

<!-- CLEARING-FLOW-157 -->
[Return Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p157-return-direct-debit.md)
<!-- /CLEARING-FLOW-157 -->

<!-- CLEARING-FLOW-159 -->
[Request Refund Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p159-request-refund-direct-debit.md)
<!-- /CLEARING-FLOW-159 -->

<!-- CLEARING-FLOW-161 -->
[Direct Debit Reversal](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p161-direct-debit-reversal.md)
<!-- /CLEARING-FLOW-161 -->

<!-- CLEARING-FLOW-177 -->
[Debtor Agent and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p177-debtor-agent-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-177 -->

<!-- CLEARING-FLOW-186 -->
[Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
<!-- /CLEARING-FLOW-186 -->

<!-- CLEARING-FLOW-198 -->
[Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p198-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
<!-- /CLEARING-FLOW-198 -->

<!-- CLEARING-FLOW-214 -->
[Debtor Agent and Creditor Agent are Direct Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents.md)
<!-- /CLEARING-FLOW-214 -->

<!-- CLEARING-FLOW-221 -->
[Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
<!-- /CLEARING-FLOW-221 -->

<!-- CLEARING-FLOW-236 -->
[Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
<!-- /CLEARING-FLOW-236 -->

<!-- CLEARING-FLOW-249 -->
[Debtor Agent and the Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p249-debtor-agent-and-the-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-249 -->

<!-- CLEARING-FLOW-260 -->
[Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
<!-- /CLEARING-FLOW-260 -->

<!-- CLEARING-FLOW-277 -->
[Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2.md)
<!-- /CLEARING-FLOW-277 -->

<!-- CLEARING-FLOW-292 -->
[Debtor Agent sends FIToFIPaymentStatusRequest](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p292-debtor-agent-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-292 -->

<!-- CLEARING-FLOW-303 -->
[Debtor and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p303-debtor-and-creditor-are-correspondents.md)
<!-- /CLEARING-FLOW-303 -->

<!-- CLEARING-FLOW-310 -->
[Debtor and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p310-debtor-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-310 -->

<!-- CLEARING-FLOW-317 -->
[Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p317-debtor-agent-and-creditor-are-correspondents.md)
<!-- /CLEARING-FLOW-317 -->

<!-- CLEARING-FLOW-327 -->
[Debtor Agent and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p327-debtor-agent-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-327 -->

<!-- CLEARING-FLOW-335 -->
[Debtor Agent and Creditor Agent are Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p335-debtor-agent-and-creditor-agent-are-not-correspondents.md)
<!-- /CLEARING-FLOW-335 -->

<!-- CLEARING-FLOW-353 -->
[Debtor and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p353-debtor-and-creditor-are-correspondents.md)
<!-- /CLEARING-FLOW-353 -->

<!-- CLEARING-FLOW-360 -->
[Debtor and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p360-debtor-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-360 -->

<!-- CLEARING-FLOW-367 -->
[Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p367-debtor-agent-and-creditor-are-correspondents.md)
<!-- /CLEARING-FLOW-367 -->

<!-- CLEARING-FLOW-379 -->
[Debtor Agent and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p379-debtor-agent-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-379 -->

<!-- CLEARING-FLOW-391 -->
[Debtor Agent and Creditor Agent Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p391-debtor-agent-and-creditor-agent-not-correspondents.md)
<!-- /CLEARING-FLOW-391 -->

<!-- CLEARING-FLOW-409 -->
[Debtor and Creditor are direct Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md)
<!-- /CLEARING-FLOW-409 -->

<!-- CLEARING-FLOW-420 -->
[Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents.md)
<!-- /CLEARING-FLOW-420 -->

<!-- CLEARING-FLOW-433 -->
[Debtor Agent and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-433 -->

<!-- CLEARING-FLOW-445 -->
[Debtor Agent and Creditor Agent are Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents.md)
<!-- /CLEARING-FLOW-445 -->

<!-- CLEARING-FLOW-463 -->
[Debtor sends FIToFIPaymentStatusRequest](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p463-debtor-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-463 -->

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

<!-- CLEARING-FLOW-585 -->
[Creditor and Debtor Agent are correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-585 -->

<!-- CLEARING-FLOW-595 -->
[Creditor Agent and Debtor Agent are correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p595-creditor-agent-and-debtor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-595 -->

<!-- CLEARING-FLOW-607 -->
[Creditor Agent and Debtor Agent are not correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents.md)
<!-- /CLEARING-FLOW-607 -->

<!-- CLEARING-FLOW-623 -->
[Payment Return in a FinancialInstitutionDirectDebit scenario](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario.md)
<!-- /CLEARING-FLOW-623 -->

<!-- CLEARING-FLOW-640 -->
[FIToFIPaymentReversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit.md)
<!-- /CLEARING-FLOW-640 -->

<!-- CLEARING-FLOW-645 -->
[Creditor sends FIToFIPaymentStatusRequest](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p645-creditor-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-645 -->

## Supplied named examples of contextual responsibilities

The following source-example flows show roles in their particular account or payment relationships. Named participants remain separate from this reusable functional role.

- [Source example flow2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-02.md)
- [Source example flow8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
- [Source example flow12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-12.md)
- [Source example flow16](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-16.md)
- [Source example flow19](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-19.md)
