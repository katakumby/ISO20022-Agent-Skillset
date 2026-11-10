---
template: false
document_kind: "participant"
manual_curated: true
review_status: "reviewed"
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000162-clearing-house"
title: "Clearing House"
source_labels: ["Clearing House"]
aliases: []
role_type: "Institutional capacity labelled in FI direct-debit artwork"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_sets: ["payments-clearing-and-settlement"]
source_locations: [{"source_id": "src-000162", "locator": "P581–584; P588; P611; P627; P643; figures44–48"}]
flow_ids: ["flow-src-000162-p585-creditor-and-debtor-agent-are-correspondents", "flow-src-000162-p595-creditor-agent-and-debtor-agent-are-correspondents", "flow-src-000162-p607-creditor-agent-and-debtor-agent-are-not-correspondents", "flow-src-000162-p623-payment-return-in-a-financial-institution-direct-debit-scenario", "flow-src-000162-p640-fito-fipayment-reversal-with-direct-debit"]
message_ids: []
limitations: ["A creditor capacity in this bounded picture, distinct from operational clearing agent and all Clearing System definitions.", "No identifier scheme is specified in cited bounded role evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Source narrative and original/Word-rendered figures read."}
---





















# Clearing House

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition, context and responsibilities

Listed as alternative creditor capacity in FI direct-debit diagrams, where creditor requests collection and receives status. (P581–584; P588; P611; P627; P643; figures44–48)

Classification: Institutional capacity labelled in FI direct-debit artwork.

## Relationships

- [creditor](participant-src-000162-creditor.md)
- [exchange](participant-src-000162-exchange.md)
- [debtor agent](participant-src-000162-debtor-agent.md)

## Limits and identifier schemes

A creditor capacity in this bounded picture, distinct from operational clearing agent and all Clearing System definitions.

No identifier scheme is specified in the cited role evidence. Message and flow relationships are maintained below.

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
