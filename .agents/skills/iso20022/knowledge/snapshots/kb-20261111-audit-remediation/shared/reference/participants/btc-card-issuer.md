---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-card-issuer"
source_labels: ["credit institution or a card company"]
aliases: []
source_locations: ["T5 row 11; Payments Families definition"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-cardholder"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# credit institution or a card company — Bank Transaction Code context

## Definition, role and business context

Issues cards allowing the holder to charge a bank account or draw on a credit line up to an authorised limit.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T5 row 11](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Customer Card Transactions Transaction is a payment card operation performed by the customer by the means of a debit or credit card. Cards are issued by a credit institution or a card company. They indicate that the holder of the card may charge his/her account at the bank (debit card) or draw on a line of credit (credit card) up to an authorised limit.

## Relationships and reuse

- [holder of the card](btc-cardholder.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
