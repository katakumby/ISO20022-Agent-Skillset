---
template: false
document_kind: "participant"
review_status: "reviewed"
manual_curated: true
domain: "shared"
domains: ["payments"]
participant_id: "participant-src-000173-ach-system-transaction-administrator"
title: "ACH (System Transaction Administrator)"
source_labels: ["ACH (System Transaction Administrator)"]
role_type: "Source-labelled system/functional activity participant"
aliases: []
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_sets: ["payments-initiation"]
source_locations: [{"source_id": "src-000173", "locator": "P148 figure10; P152 figure12"}]
flow_ids: ["flow-src-000173-p147-customer-to-bank-direct-debit", "flow-src-000173-p151-request-refund-of-direct-debit"]
message_ids: []
limitations: ["Source labels this lane ACH (System Transaction Administrator). Its depiction is not sufficient to merge it with every Clearing System or Clearing Agent definition.", "No participant identifier scheme is specified in the cited evidence."]
review_evidence: {"date": "2026-11-09", "scope": "Cited narrative and original figure evidence inspected."}
---









# ACH (System Transaction Administrator)

[src-000173](../../../evidence/omitted/baf7abf3460122a33db6052d.md)

## Definition, context and responsibilities

In the direct-debit activity view accepts or rejects instructions, clears them and forwards the cleared request; in the refund view accepts or rejects the direct-debit return instruction and clears an accepted return. (P148 figure10; P152 figure12)

Role classification: Source-labelled system/functional activity participant.

## Relationships

- [clearing system](participant-src-000173-clearing-system.md)
- [clearing agent](participant-src-000173-clearing-agent.md)
- [creditor agent](participant-src-000173-creditor-agent.md)
- [debtor agent](participant-src-000173-debtor-agent.md)

## Identifier schemes and limitations

Source labels this lane ACH (System Transaction Administrator). Its depiction is not sufficient to merge it with every Clearing System or Clearing Agent definition.

No participant identifier scheme is specified in this bounded evidence. Functional roles describe relationships, not permanent institutional identities. Message and flow links are maintained below.

<!-- INITIATION-FLOW-147 -->
[Customer-to-bank Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p147-customer-to-bank-direct-debit.md)
<!-- /INITIATION-FLOW-147 -->

<!-- INITIATION-FLOW-151 -->
[Request Refund of Direct Debit](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/flows/flow-src-000173-p151-request-refund-of-direct-debit.md)
<!-- /INITIATION-FLOW-151 -->
