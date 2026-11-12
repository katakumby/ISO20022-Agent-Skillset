---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-correspondent-bank"
source_labels: ["correspondent bank"]
aliases: []
source_locations: ["T20 row 8; Received and Issued Cheques codes"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-circular-cheque-instructing-bank", "btc-creditor"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# correspondent bank — Bank Transaction Code context

## Definition, role and business context

Receives a bank instruction to pay a creditor a stated sum upon presentation of identification, in the circular-cheque definition.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T20 row 8](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0020.md): Circular Cheque  Transaction is related to an instruction from a bank to its correspondent bank to pay the creditor a stated sum upon the presentation of a means of identification.

## Relationships and reuse

- [bank](btc-circular-cheque-instructing-bank.md).
- [creditor](btc-creditor.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
