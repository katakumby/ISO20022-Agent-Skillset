---
template: false
document_kind: "participant"
manual_curated: true
review_status: "reviewed"
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000162-credit-party"
title: "Credit Party"
source_labels: ["Credit Party"]
aliases: []
role_type: "Directional settlement-party role"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
source_locations: [{"source_id": "src-000162", "locator": "P551; P572; T26 row8"}]
flow_ids: ["flow-src-000162-p539-payment-return-initiated-by-debtor-agent", "flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit"]
message_ids: []
limitations: ["Source does not fix this role to the customer creditor rather than an interbank settlement party.", "No identifier scheme is specified in cited bounded role evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Source narrative and original/Word-rendered figures read."}
---









# Credit Party

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition, context and responsibilities

Party from which settlement agent transfers returned/reversed funds in the described settlement direction. (P551; P572; T26 row8)

Classification: Directional settlement-party role.

## Relationships

- [debit party](participant-src-000162-debit-party.md)
- [settlement agent](participant-src-000162-settlement-agent.md)

## Limits and identifier schemes

Source does not fix this role to the customer creditor rather than an interbank settlement party.

No identifier scheme is specified in the cited role evidence. Message and flow relationships are maintained below.

<!-- CLEARING-FLOW-539 -->
[PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md)
<!-- /CLEARING-FLOW-539 -->

<!-- CLEARING-FLOW-556 -->
[FIToFIPaymentReversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit.md)
<!-- /CLEARING-FLOW-556 -->
