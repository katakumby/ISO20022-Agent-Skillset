---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000162", "src-000163"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
participant_id: "participant-src-000162-financial-institution"
title: "Financial Institution"
source_labels: ["Financial Institution", "one financial institution"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000162", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[2]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000163", "heading": "6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "file_pages": [702], "evidence_id": "src-000163-pacs.008.001.14-p702-c007"}]
flows: ["flow-src-000162-p114-accept-inter-bank-payment", "flow-src-000162-p115-asses-interbank-payment-risk", "flow-src-000162-p116-validate-interbank-payment", "flow-src-000162-p117-authorise-interbank-payment", "flow-src-000162-p118-clear-interbank-payment", "flow-src-000162-p119-sort-interbank-payment", "flow-src-000162-p120-calculate-the-settlement-positions", "flow-src-000162-p121-prepare-onward-interbank-payment", "flow-src-000162-p122-settle-interbank-payment", "flow-src-000162-p123-generate-regulatory-reporting-information", "flow-src-000162-p127-process-direct-debit", "flow-src-000162-p128-process-reject", "flow-src-000162-p129-process-return-request-for-refund", "flow-src-000162-p130-process-reversal", "flow-src-000162-p154-direct-debit-instruction"]
process_sections: ["flow-src-000162-p198-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p208-negative-fito-fipayment-status-report-with-fito-ficustomer-credit-tran", "flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2", "flow-src-000162-p296-financial-institution-credit-transfer", "flow-src-000162-p303-debtor-and-creditor-are-correspondents", "flow-src-000162-p307-out-of-scope", "flow-src-000162-p310-debtor-and-creditor-agent-are-correspondents", "flow-src-000162-p317-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p324-out-of-scope", "flow-src-000162-p327-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p335-debtor-agent-and-creditor-agent-are-not-correspondents", "flow-src-000162-p347-negative-fito-fipayment-status-report-with-financial-institution-credi", "flow-src-000162-p353-debtor-and-creditor-are-correspondents", "flow-src-000162-p360-debtor-and-creditor-agent-are-correspondents", "flow-src-000162-p367-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p379-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p391-debtor-agent-and-creditor-agent-not-correspondents", "flow-src-000162-p407-payment-return-with-financial-institution-credit-transfer", "flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents", "flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents", "flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents", "flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents", "flow-src-000162-p463-debtor-sends-fito-fipayment-status-request", "flow-src-000162-p468-fito-ficustomer-direct-debit", "flow-src-000162-p575-creditor-agent-sends-fito-fipayment-status-request", "flow-src-000162-p580-financial-institution-direct-debit", "flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents", "flow-src-000162-p590-out-of-scope", "flow-src-000162-p595-creditor-agent-and-debtor-agent-are-correspondents", "flow-src-000162-p602-out-of-scope", "flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents", "flow-src-000162-p617-out-of-scope", "flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario", "flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit", "flow-src-000162-p645-creditor-sends-fito-fipayment-status-request"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
search_terms: ["Financial Institution", "pacs.002", "pacs.003", "pacs.004", "pacs.007", "pacs.008", "pacs.009", "pacs.010", "pacs.028"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000162-p111-credit-transfer", "flow-src-000162-p124-direct-debit", "flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents", "flow-src-000162-p595-creditor-agent-and-debtor-agent-are-correspondents", "flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents", "flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario", "flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit", "flow-src-000162-p645-creditor-sends-fito-fipayment-status-request"]
---



































# Financial Institution

Business context: Payments Clearing and Settlement. Source classification: business role.

## Definition

Organisation established primarily to provide financial services.

Evidence: [T7](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0007.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Debtor agent](participant-src-000162-debtor-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 6, column 2 |
| Business role listed for this functional participant | [Creditor Agent](participant-src-000162-creditor-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 7, column 2 |
| Business role listed for this functional participant | [Forwarding Agent](participant-src-000162-forwarding-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 8, column 2 |
| Business role listed for this functional participant | [Account Owner](participant-src-000162-account-owner.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 10, column 2 |
| Business role listed for this functional participant | [Account Servicer](participant-src-000162-account-servicer.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 11, column 2 |
| Business role listed for this functional participant | [Payment Clearing Agent](participant-src-000162-payment-clearing-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 12, column 2 |
| Business role listed for this functional participant | [PaymentSettlementAgent](participant-src-000162-payment-settlement-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 13, column 2 |
| Business role listed for this functional participant | [Intermediary Agent](participant-src-000162-intermediary-agent.md) | [T8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/documents/src-000162/tables/tbl-0008.md) row 14, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Accept Inter-Bank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p114-accept-inter-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Asses Interbank Payment Risk](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p115-asses-interbank-payment-risk.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Validate Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p116-validate-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Authorise Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p117-authorise-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Clear Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p118-clear-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Sort Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p119-sort-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Calculate the Settlement Positions](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p120-calculate-the-settlement-positions.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Prepare Onward Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p121-prepare-onward-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Settle Interbank Payment](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p122-settle-interbank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Generate Regulatory Reporting Information](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p123-generate-regulatory-reporting-information.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Process direct debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p127-process-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Process Reject](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p128-process-reject.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Process Return/Request for Refund](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p129-process-return-request-for-refund.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Process Reversal](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p130-process-reversal.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Direct debit instruction](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p154-direct-debit-instruction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p198-debtor-agent-and-creditor-agent-are-not-correspondents-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p208-negative-fito-fipayment-status-report-with-fito-ficustomer-credit-tran.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p236-debtor-agent-and-creditor-agent-are-not-correspondents-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are not Correspondents - 2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p277-debtor-agent-and-creditor-agent-are-not-correspondents-2.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FinancialInstitutionCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p296-financial-institution-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p303-debtor-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of Scope](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p307-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p310-debtor-and-creditor-agent-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p317-debtor-agent-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of Scope](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p324-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p327-debtor-agent-and-creditor-agent-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p335-debtor-agent-and-creditor-agent-are-not-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Negative FIToFIPaymentStatusReport with FinancialInstitutionCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p347-negative-fito-fipayment-status-report-with-financial-institution-credi.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p353-debtor-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p360-debtor-and-creditor-agent-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p367-debtor-agent-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p379-debtor-agent-and-creditor-agent-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p391-debtor-agent-and-creditor-agent-not-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn with FinancialInstitutionCreditTransfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p407-payment-return-with-financial-institution-credit-transfer.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor and Creditor are direct Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p409-debtor-and-creditor-are-direct-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p420-debtor-agent-and-creditor-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p433-debtor-agent-and-creditor-agent-are-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor Agent and Creditor Agent are Not Correspondents](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p445-debtor-agent-and-creditor-agent-are-not-correspondents.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Debtor sends FIToFIPaymentStatusRequest](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p463-debtor-sends-fito-fipayment-status-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p468-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Creditor Agent sends FIToFIPaymentStatusRequest](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p575-creditor-agent-sends-fito-fipayment-status-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
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

Source labels: `Financial Institution`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md).

<!-- CLEARING-FLOW-111 -->
[Credit Transfer](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p111-credit-transfer.md)
<!-- /CLEARING-FLOW-111 -->

<!-- CLEARING-FLOW-124 -->
[Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p124-direct-debit.md)
<!-- /CLEARING-FLOW-124 -->

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

<!-- FUNCTIONALITY-ALIASES-src-000163 -->
## Additional literal publication labels

One is the sender position in the serial-method description, not an institutional identifier. The functional exchange and condition of more than two institutions remain in the quote.

| Source label | Source context |
| --- | --- |
| one financial institution | src-000163-pacs.008.001.14-p702-c007 |


> If more than two financial institutions are involved in the payment chain and if the FIToFICustomerCreditTransfer is sent from one financial institution to the next financial institution in the payment chain, then the payment method is called the Serial method.

src-000163, file pages702; 6 pacs.008.001.14 FIToFICustomerCreditTransferV14.

<!-- /FUNCTIONALITY-ALIASES-src-000163 -->
