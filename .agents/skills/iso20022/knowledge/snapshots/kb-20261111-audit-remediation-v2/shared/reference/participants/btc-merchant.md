---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-merchant"
source_labels: ["merchant"]
aliases: []
source_locations: ["T5 row 12; Payments Families definition", "T22 row 3; Merchant Card Transaction codes", "T22 row 5; Merchant Card Transaction codes"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-cardholder"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# merchant — Bank Transaction Code context

## Definition, role and business context

Has card operations reported for it and receives POS payment funds into its account; smart-card settlement transfers funds for the recorded transaction.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T5 row 12](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Merchant Card Transactions Transaction is a payment card operation performed by debit or credit card operation, reported for the merchant.
- [T22 row 3](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0022.md): Point-of-Sale (POS) Payment Transaction is a payment done through an electronic network of banks, debit cardholders, and merchants that permit consumers to electronically make direct payment at the place of purchase. The funds transfer directly from the account of the cardholder to the account of the merchant.
- [T22 row 5](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0022.md): Smart-Card Payment  Transaction is a card-based payment. For the merchant, the transaction related to transfer of the funds related to the settlement of the recorded transaction paid through smart-cards.

## Relationships and reuse

- [holder of the card](btc-cardholder.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
