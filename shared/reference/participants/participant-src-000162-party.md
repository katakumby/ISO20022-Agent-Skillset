---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-party"
title: "Party"
source_labels: ["Party"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[4]", "paragraph_id": null, "table_id": "T7"}]
flows: ["flow-src-000162-p116-validate-interbank-payment", "flow-src-000162-p119-sort-interbank-payment", "flow-src-000162-p120-calculate-the-settlement-positions", "flow-src-000162-p121-prepare-onward-interbank-payment", "flow-src-000162-p122-settle-interbank-payment", "flow-src-000162-p123-generate-regulatory-reporting-information", "flow-src-000162-p129-process-return-request-for-refund", "flow-src-000162-p161-direct-debit-reversal"]
process_sections: ["flow-src-000162-p170-fito-ficustomer-credit-transfer", "flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p198-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p247-payment-return-with-fito-ficustomer-credit-transfer", "flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1", "flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p296-financial-institution-credit-transfer", "flow-src-000162-p407-payment-return-with-financial-institution-credit-transfer", "flow-src-000162-p468-fito-ficustomer-direct-debit", "flow-src-000162-p535-payment-return-with-direct-debit", "flow-src-000162-p539-payment-return-initiated-by-debtor-agent", "flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit", "flow-src-000162-p580-financial-institution-direct-debit"]
message_ids: []
message_families: ["pacs.002", "pacs.003", "pacs.004", "pacs.007", "pacs.008", "pacs.009", "pacs.010"]
search_terms: ["Party", "pacs.002", "pacs.003", "pacs.004", "pacs.007", "pacs.008", "pacs.009", "pacs.010"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000162-p124-direct-debit"]
---





# Party

Business context: Payments Clearing and Settlement. Source classification: business role.

## Definition

Entity involved in a payment. 

Evidence: [T7](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0007.md), source row 4.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Debtor](participant-src-000162-debtor.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 2, column 4 |
| Business role listed for this functional participant | [Creditor](participant-src-000162-creditor.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 3, column 4 |
| Business role listed for this functional participant | [Ultimate Debtor](participant-src-000162-ultimate-debtor.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 4, column 4 |
| Business role listed for this functional participant | [Ultimate Creditor](participant-src-000162-ultimate-creditor.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 5, column 4 |
| Business role listed for this functional participant | [Initiating Party](participant-src-000162-initiating-party.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 9, column 4 |
| Business role listed for this functional participant | [Account Owner](participant-src-000162-account-owner.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 10, column 4 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Validate Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p116-validate-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Sort Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p119-sort-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Calculate the Settlement Positions](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p120-calculate-the-settlement-positions.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Prepare Onward Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p121-prepare-onward-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Settle Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p122-settle-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Generate Regulatory Reporting Information](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p123-generate-regulatory-reporting-information.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Process Return/Request for Refund](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p129-process-return-request-for-refund.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct Debit Reversal](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p161-direct-debit-reversal.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFICustomerCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p170-fito-ficustomer-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p186-debtor-agent-and-creditor-agent-are-not-correspondents-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p198-debtor-agent-and-creditor-agent-are-not-correspondents-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p221-debtor-agent-and-creditor-agent-are-not-correspondents-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn with FIToFICustomerCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p247-payment-return-with-fito-ficustomer-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p260-debtor-agent-and-creditor-agent-are-not-correspondents-1.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FinancialInstitutionCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p296-financial-institution-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn with FinancialInstitutionCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p407-payment-return-with-financial-institution-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn with Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p535-payment-return-with-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFIPaymentReversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FinancialInstitutionDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p580-financial-institution-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pacs.002`, `pacs.003`, `pacs.004`, `pacs.007`, `pacs.008`, `pacs.009`, `pacs.010`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx).

<!-- CLEARING-FLOW-124 -->
[Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p124-direct-debit.md)
<!-- /CLEARING-FLOW-124 -->
