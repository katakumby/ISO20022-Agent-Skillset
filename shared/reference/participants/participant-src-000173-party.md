---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "payments"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
participant_id: "participant-src-000173-party"
title: "Party"
source_labels: ["Party"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000173", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[4]", "paragraph_id": null, "table_id": "T7"}]
flows: ["flow-src-000173-p116-order-customer-to-bank-payment", "flow-src-000173-p119-check-authorisation-customer-to-bank-payment", "flow-src-000173-p123-clear-customer-to-bank-payment", "flow-src-000173-p124-settle-customer-to-bank-payment", "flow-src-000173-p140-complex-scenario"]
process_sections: ["flow-src-000173-p162-account-information-from-creditor-agent-to-creditor", "flow-src-000173-p179-customer-credit-transfer-initiation-relay", "flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit", "flow-src-000173-p223-out-of-scope", "flow-src-000173-p278-payment-return-with-direct-debit", "flow-src-000173-p280-payment-return-initiated-by-debtor-agent", "flow-src-000173-p298-customer-payment-reversal-with-direct-debit"]
message_ids: []
message_families: ["pain.001", "pain.002", "pain.007", "pain.008"]
search_terms: ["Party", "pain.001", "pain.002", "pain.007", "pain.008"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Party

Business context: Payments Initiation. Source classification: business role.

## Definition

Entity involved in a payment. 

Evidence: [T7](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/documents/src-000173/tables/tbl-0007.md), source row 4.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Order Customer-to-bank payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p116-order-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Check Authorisation Customer-to-Bank Payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p119-check-authorisation-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Clear customer-to-bank payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p123-clear-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Settle customer-to-bank payment](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p124-settle-customer-to-bank-payment.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Complex scenario:](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p140-complex-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Account information from creditor agent to creditor](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p162-account-information-from-creditor-agent-to-creditor.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerCreditTransferInitiation - Relay](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p179-customer-credit-transfer-initiation-relay.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [CustomerDirectDebitInitiation and FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Out of scope](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p223-out-of-scope.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn with Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p278-payment-return-with-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Customer Payment Reversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `pain.001`, `pain.002`, `pain.007`, `pain.008`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx).
