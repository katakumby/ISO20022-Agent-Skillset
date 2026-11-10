---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000173-debit-party"
title: "Debit Party"
source_labels: ["Debit Party"]
role_type: "Directional settlement-party role in return/reversal narrative"
aliases: []
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
source_locations: [{"source_id": "src-000173", "locator": "P294; P315"}]
flow_ids: ["flow-src-000173-p280-payment-return-initiated-by-debtor-agent", "flow-src-000173-p298-customer-payment-reversal-with-direct-debit"]
message_ids: []
limitations: ["Retain the source term; do not infer that it is always the end debtor rather than an interbank settlement party.", "No participant identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative and original figure evidence inspected."}
---









# Debit Party

[src-000173](../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx)

## Definition, context and responsibilities

Source-named party to which the settlement agent transfers funds in the return/reversal settlement direction. (P294; P315)

Role classification: Directional settlement-party role in return/reversal narrative.

## Relationships

- [credit party](participant-src-000173-credit-party.md)
- [settlement agent](participant-src-000173-settlement-agent.md)

## Identifier schemes and limitations

Retain the source term; do not infer that it is always the end debtor rather than an interbank settlement party.

No participant identifier scheme is specified in this bounded evidence. Functional roles describe relationships, not permanent institutional identities. Message and flow links are maintained below.

<!-- INITIATION-FLOW-280 -->
[PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md)
<!-- /INITIATION-FLOW-280 -->

<!-- INITIATION-FLOW-298 -->
[Customer Payment Reversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md)
<!-- /INITIATION-FLOW-298 -->
