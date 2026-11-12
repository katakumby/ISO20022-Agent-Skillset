---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-cheque-recipient"
source_labels: ["cheque recipient"]
aliases: []
source_locations: ["T5 row 10; Payments Families definition"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-cash-account-owner"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# cheque recipient — Bank Transaction Code context

## Definition, role and business context

Receives the cheque issued by an account owner to debit the cheque issuer account.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T5 row 10](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Issued Cheques Transaction is related to a written paper order – the cheque – issued by the account owner to the cheque recipient, to debit the account of the cheque issuer.

## Relationships and reuse

- [account owner](btc-cash-account-owner.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
