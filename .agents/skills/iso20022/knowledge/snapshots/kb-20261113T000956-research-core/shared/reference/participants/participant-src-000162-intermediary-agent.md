---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "shared"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-intermediary-agent"
title: "Intermediary Agent"
source_labels: ["Intermediary Agent"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[14]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000162", "locator": "T6 row14; P173; P187–197; P299; P336–344; P608–621"}]
flows: ["flow-src-000162-p138-credit-transfer"]
process_sections: ["flow-src-000162-p170-fito-ficustomer-credit-transfer", "flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p195-out-of-scope", "flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p230-case-a", "flow-src-000162-p233-case-b", "flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p296-financial-institution-credit-transfer", "flow-src-000162-p335-debtor-agent-and-creditor-agent-are-not-correspondents", "flow-src-000162-p391-debtor-agent-and-creditor-agent-not-correspondents", "flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents", "flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents", "flow-src-000162-p617-out-of-scope", "flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario"]
message_ids: []
message_families: ["pacs.002", "pacs.004", "pacs.008", "pacs.009", "pacs.010"]
search_terms: ["Intermediary Agent", "pacs.002", "pacs.004", "pacs.008", "pacs.009", "pacs.010"]
limitations: ["Scoped source role; classification terminology conflict remains issue-000054.", "No unsupported cross-source equivalence or fixed institutional role inferred."]
manual_curated: true
domains: ["payments"]
issue_ids: ["issue-000054"]
definition_review: {"date": "2026-11-09", "result": "pass", "scope": "Cited definition/activity/flow evidence reviewed; terminology conflict remains."}
flow_ids: ["flow-src-000162-p177-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents", "flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p249-debtor-agent-and-the-creditor-agent-are-correspondents", "flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p292-debtor-agent-sends-fito-fipayment-status-request", "flow-src-000162-p303-debtor-and-creditor-are-correspondents", "flow-src-000162-p310-debtor-and-creditor-agent-are-correspondents", "flow-src-000162-p317-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p327-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p335-debtor-agent-and-creditor-agent-are-not-correspondents", "flow-src-000162-p353-debtor-and-creditor-are-correspondents", "flow-src-000162-p360-debtor-and-creditor-agent-are-correspondents", "flow-src-000162-p367-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p379-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p391-debtor-agent-and-creditor-agent-not-correspondents", "flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents", "flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents", "flow-src-000162-p463-debtor-sends-fito-fipayment-status-request", "flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents", "flow-src-000162-p595-creditor-agent-and-debtor-agent-are-correspondents", "flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents", "flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario", "flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit"]
---















































































































# Intermediary Agent

Business context: Payments Clearing and Settlement. Source classification: functional participant role.

## Definition

Agent between the debtor's agent and the creditor's agent. There can be several intermediary agents specified for the execution of a payment.

Evidence: [T6](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0006.md), source row 14.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Financial Institution](participant-src-000162-financial-institution.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 14, column 2 |
| Can play the functional participant role in this source context | [Clearing System](participant-src-000162-clearing-system.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 14, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Credit Transfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p138-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFICustomerCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p170-fito-ficustomer-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of Scope](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p195-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Case A](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p230-case-a.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Case B](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p233-case-b.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FinancialInstitutionCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p296-financial-institution-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p335-debtor-agent-and-creditor-agent-are-not-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p391-debtor-agent-and-creditor-agent-not-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Creditor Agent and Debtor Agent are not correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of Scope](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p617-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Payment Return in a FinancialInstitutionDirectDebit scenario](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pacs.002`, `pacs.004`, `pacs.008`, `pacs.009`, `pacs.010`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Intermediary Agent`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md).

<!-- CLEARING-ROLE-REVIEW -->
## Curated responsibilities and contextual roles

Sits between debtor and creditor agents; multiple may exist. Serial transfers/statuses/returns pass through it; cover narrative may assign middle lifeline a reimbursement capacity instead. (T6 row14; P173; P187–197; P299; P336–344; P608–621)

T1 and P102–104/T8 use BusinessRole/Participant terminology inconsistently (issue-000054). Literal source definitions are retained; functional roles are not fixed institutions. No identifier scheme is asserted beyond supplied evidence.
<!-- /CLEARING-ROLE-REVIEW -->

<!-- CLEARING-FLOW-177 -->
[Debtor Agent and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p177-debtor-agent-and-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-177 -->

<!-- CLEARING-FLOW-186 -->
[Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
<!-- /CLEARING-FLOW-186 -->

<!-- CLEARING-FLOW-214 -->
[Debtor Agent and Creditor Agent are Direct Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p214-debtor-agent-and-creditor-agent-are-direct-correspondents.md)
<!-- /CLEARING-FLOW-214 -->

<!-- CLEARING-FLOW-221 -->
[Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
<!-- /CLEARING-FLOW-221 -->

<!-- CLEARING-FLOW-249 -->
[Debtor Agent and the Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p249-debtor-agent-and-the-creditor-agent-are-correspondents.md)
<!-- /CLEARING-FLOW-249 -->

<!-- CLEARING-FLOW-260 -->
[Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1.md)
<!-- /CLEARING-FLOW-260 -->

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
