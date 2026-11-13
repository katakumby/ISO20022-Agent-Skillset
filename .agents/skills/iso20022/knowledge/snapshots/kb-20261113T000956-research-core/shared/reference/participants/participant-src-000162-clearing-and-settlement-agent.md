---
template: false
document_kind: "participant"
manual_curated: true
review_status: "reviewed"
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000162-clearing-and-settlement-agent"
title: "Clearing and Settlement Agent"
source_labels: ["Clearing and Settlement Agent"]
aliases: []
role_type: "Combined functional role"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
source_locations: [{"source_id": "src-000162", "locator": "P175; P301; P488–494; P551; P570–573; figures37–43/49"}]
flow_ids: ["flow-src-000162-p468-fito-ficustomer-direct-debit", "flow-src-000162-p499-creditor-negative-fito-fipayment-status-report-initiated-by-clearing-a", "flow-src-000162-p509-negative-fito-fipayment-status-report-initiated-by-debtor-agent", "flow-src-000162-p529-fito-fipayment-status-report-to-confirm-processability-of-fito-ficusto", "flow-src-000162-p539-payment-return-initiated-by-debtor-agent", "flow-src-000162-p556-fito-fipayment-reversal-with-direct-debit", "flow-src-000162-p575-creditor-agent-sends-fito-fipayment-status-request", "flow-src-000162-p645-creditor-sends-fito-fipayment-status-request"]
message_ids: []
limitations: ["One combined lifeline does not establish one permanent institution.", "No identifier scheme is specified in cited bounded role evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Source narrative and original/Word-rendered figures read."}
---



































# Clearing and Settlement Agent

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition, context and responsibilities

Receives and forwards interbank instructions and statuses; relays direct-debit returns/reversals. P494/P551/P570 expressly permit clearing and settlement by two parties. (P175; P301; P488–494; P551; P570–573; figures37–43/49)

Classification: Combined functional role.

## Relationships

- [clearing agent](participant-src-000162-clearing-agent.md)
- [settlement agent](participant-src-000162-settlement-agent.md)
- [debtor agent](participant-src-000162-debtor-agent.md)
- [creditor agent](participant-src-000162-creditor-agent.md)

## Limits and identifier schemes

One combined lifeline does not establish one permanent institution.

No identifier scheme is specified in the cited role evidence. Message and flow relationships are maintained below.

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

<!-- CLEARING-FLOW-575 -->
[Creditor Agent sends FIToFIPaymentStatusRequest](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p575-creditor-agent-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-575 -->

<!-- CLEARING-FLOW-645 -->
[Creditor sends FIToFIPaymentStatusRequest](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p645-creditor-sends-fito-fipayment-status-request.md)
<!-- /CLEARING-FLOW-645 -->

<!-- CLEARING-FLOW-553 -->
[Debtor refund request and return-code requirement](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/flow-src-000162-p553-refund-by-the-debtor.md)
<!-- /CLEARING-FLOW-553 -->
