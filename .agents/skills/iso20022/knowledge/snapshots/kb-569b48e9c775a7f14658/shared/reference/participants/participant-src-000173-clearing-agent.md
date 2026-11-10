---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000173-clearing-agent"
title: "Clearing Agent"
source_labels: ["Clearing Agent"]
role_type: "Separate functional participant in direct-debit processing"
aliases: []
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
source_locations: [{"source_id": "src-000173", "locator": "P225–228; P294; P311–314; figure11"}]
flow_ids: ["flow-src-000173-p149-return-direct-debit", "flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit", "flow-src-000173-p280-payment-return-initiated-by-debtor-agent", "flow-src-000173-p298-customer-payment-reversal-with-direct-debit"]
message_ids: []
limitations: ["The direct-debit operational Clearing Agent is cross-linked to, but not silently merged with, the general T6 Payment Clearing Agent (Instructing Agent).", "No participant identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative and original figure evidence inspected."}
---

















# Clearing Agent

[src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Definition, context and responsibilities

Clears direct debits/returns; checks and may reject a return instruction. If clearing and settlement are separate, calculates settlement positions and transmits payment information for the settlement cycle. (P225–228; P294; P311–314; figure11)

Role classification: Separate functional participant in direct-debit processing.

## Relationships

- [clearing and settlement agent](participant-src-000173-clearing-and-settlement-agent.md)
- [settlement agent](participant-src-000173-settlement-agent.md)
- [payment clearing agent instructing agent](participant-src-000173-payment-clearing-agent-instructing-agent.md)

## Identifier schemes and limitations

The direct-debit operational Clearing Agent is cross-linked to, but not silently merged with, the general T6 Payment Clearing Agent (Instructing Agent).

No participant identifier scheme is specified in this bounded evidence. Functional roles describe relationships, not permanent institutional identities. Message and flow links are maintained below.

<!-- INITIATION-FLOW-149 -->
[Return Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p149-return-direct-debit.md)
<!-- /INITIATION-FLOW-149 -->

<!-- INITIATION-FLOW-198 -->
[CustomerDirectDebitInitiation and FIToFICustomerDirectDebit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p198-customer-direct-debit-initiation-and-fito-ficustomer-direct-debit.md)
<!-- /INITIATION-FLOW-198 -->

<!-- INITIATION-FLOW-280 -->
[PaymentReturn Initiated by Debtor Agent](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p280-payment-return-initiated-by-debtor-agent.md)
<!-- /INITIATION-FLOW-280 -->

<!-- INITIATION-FLOW-298 -->
[Customer Payment Reversal with Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p298-customer-payment-reversal-with-direct-debit.md)
<!-- /INITIATION-FLOW-298 -->
