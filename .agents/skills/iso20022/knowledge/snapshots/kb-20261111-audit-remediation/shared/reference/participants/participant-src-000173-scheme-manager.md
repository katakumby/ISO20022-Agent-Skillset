---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000173-scheme-manager"
title: "Scheme Manager"
source_labels: ["Scheme Manager"]
role_type: "Narrative service-provider role"
aliases: []
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
source_locations: [{"source_id": "src-000173", "locator": "P317"}]
flow_ids: ["flow-src-000173-p298-customer-payment-reversal-with-direct-debit"]
message_ids: []
limitations: ["Narrative-only participant; absent from figure25. Source gives no separate institutional definition or mandatory monitoring service.", "No participant identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative and original figure evidence inspected."}
---





# Scheme Manager

[src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Definition, context and responsibilities

May offer value-added monitoring to avoid crossing PaymentReturn and CustomerPaymentReversal; source also allows exceptional crossing to provoke investigation handling. (P317)

Role classification: Narrative service-provider role.

## Relationships

- [creditor](participant-src-000173-creditor.md)
- [debtor agent](participant-src-000173-debtor-agent.md)

## Identifier schemes and limitations

Narrative-only participant; absent from figure25. Source gives no separate institutional definition or mandatory monitoring service.

No participant identifier scheme is specified in this bounded evidence. Functional roles describe relationships, not permanent institutional identities. Message and flow links are maintained below.

<!-- INITIATION-FLOW-298 -->
[Customer Payment Reversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md)
<!-- /INITIATION-FLOW-298 -->
