---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000173-clearing-and-settlement-agent"
title: "Clearing and Settlement Agent"
source_labels: ["Clearing and Settlement Agent"]
role_type: "Combined functional role in the direct-debit sequence views"
aliases: []
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
source_locations: [{"source_id": "src-000173", "locator": "P221–229; figures19–25"}]
flow_ids: ["flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit", "flow-src-000173-p234-negative-customer-payment-status-report-creditor-agent", "flow-src-000173-p239-negative-customer-payment-status-report-clearing-and-settlement-agent", "flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent", "flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation", "flow-src-000173-p280-payment-return-initiated-by-debtor-agent", "flow-src-000173-p298-customer-payment-reversal-with-direct-debit"]
message_ids: []
limitations: ["The source explicitly permits clearing and settlement to be performed by two parties. The combined figure lifeline is not an assertion that one institution always performs both.", "No participant identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative and original figure evidence inspected."}
---





























# Clearing and Settlement Agent

[src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Definition, context and responsibilities

Receives FIToFICustomerDirectDebit from the creditor agent and forwards it to the debtor agent; exchanges processability status and relays returns/reversals. (P221–229; figures19–25)

Role classification: Combined functional role in the direct-debit sequence views.

## Relationships

- [clearing agent](participant-src-000173-clearing-agent.md)
- [settlement agent](participant-src-000173-settlement-agent.md)
- [creditor agent](participant-src-000173-creditor-agent.md)
- [debtor agent](participant-src-000173-debtor-agent.md)

## Identifier schemes and limitations

The source explicitly permits clearing and settlement to be performed by two parties. The combined figure lifeline is not an assertion that one institution always performs both.

No participant identifier scheme is specified in this bounded evidence. Functional roles describe relationships, not permanent institutional identities. Message and flow links are maintained below.

<!-- INITIATION-FLOW-198 -->
[CustomerDirectDebitInitiation and FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit.md)
<!-- /INITIATION-FLOW-198 -->

<!-- INITIATION-FLOW-234 -->
[Negative CustomerPaymentStatusReport - Creditor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p234-negative-customer-payment-status-report-creditor-agent.md)
<!-- /INITIATION-FLOW-234 -->

<!-- INITIATION-FLOW-239 -->
[Negative CustomerPaymentStatusReport - Clearing And Settlement Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p239-negative-customer-payment-status-report-clearing-and-settlement-agent.md)
<!-- /INITIATION-FLOW-239 -->

<!-- INITIATION-FLOW-249 -->
[Negative FIToFIPaymentStatusReport - Debtor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p249-negative-fito-fipayment-status-report-debtor-agent.md)
<!-- /INITIATION-FLOW-249 -->

<!-- INITIATION-FLOW-266 -->
[Confirmation of Processability of CustomerDirectDebitInitiation](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p266-confirmation-of-processability-of-customer-direct-debit-initiation.md)
<!-- /INITIATION-FLOW-266 -->

<!-- INITIATION-FLOW-280 -->
[PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md)
<!-- /INITIATION-FLOW-280 -->

<!-- INITIATION-FLOW-298 -->
[Customer Payment Reversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md)
<!-- /INITIATION-FLOW-298 -->
