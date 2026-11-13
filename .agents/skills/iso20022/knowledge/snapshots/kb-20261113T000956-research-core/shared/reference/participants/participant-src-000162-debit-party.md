---
template: false
document_kind: "participant"
manual_curated: true
review_status: "reviewed"
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000162-debit-party"
title: "Debit Party"
source_labels: ["Debit Party"]
aliases: []
role_type: "Directional settlement-party role"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
source_locations: [{"source_id": "src-000162", "locator": "P551; P572; T26 row8"}]
flow_ids: ["flow-src-000162-p539-payment-return-initiated-by-debtor-agent", "flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit"]
message_ids: []
limitations: ["Source does not fix this role to the customer debtor rather than an interbank settlement party.", "No identifier scheme is specified in cited bounded role evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Source narrative and original/Word-rendered figures read."}
---









# Debit Party

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition, context and responsibilities

Party to which settlement agent transfers returned/reversed funds in the described settlement direction. (P551; P572; T26 row8)

Classification: Directional settlement-party role.

## Relationships

- [credit party](participant-src-000162-credit-party.md)
- [settlement agent](participant-src-000162-settlement-agent.md)

## Limits and identifier schemes

Source does not fix this role to the customer debtor rather than an interbank settlement party.

No identifier scheme is specified in the cited role evidence. Message and flow relationships are maintained below.

<!-- CLEARING-FLOW-539 -->
[PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p539-payment-return-initiated-by-debtor-agent.md)
<!-- /CLEARING-FLOW-539 -->

<!-- CLEARING-FLOW-556 -->
[FIToFIPaymentReversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit.md)
<!-- /CLEARING-FLOW-556 -->
