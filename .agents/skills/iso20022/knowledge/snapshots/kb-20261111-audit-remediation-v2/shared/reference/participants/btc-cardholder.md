---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-cardholder"
source_labels: ["holder of the card"]
aliases: []
source_locations: ["T5 row 11; Payments Families definition", "T21 row 6; Customer Card Transaction codes", "T22 row 6; Merchant Card Transaction codes"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-merchant", "btc-card-issuer"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# holder of the card — Bank Transaction Code context

## Definition, role and business context

Uses a debit card to charge an account or a credit card to draw on authorised credit. In POS payment the funds move from cardholder account to merchant account. May reject an unpaid card transaction for a justified reason.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T5 row 11](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Customer Card Transactions Transaction is a payment card operation performed by the customer by the means of a debit or credit card. Cards are issued by a credit institution or a card company. They indicate that the holder of the card may charge his/her account at the bank (debit card) or draw on a line of credit (credit card) up to an authorised limit.
- [T21 row 6](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0021.md): Point-of-Sale (POS) Payment  - Debit Card  Transaction is a payment done through an electronic network of banks, debit cardholders, and merchants that permit consumers to electronically make direct payment at the place of purchase. The funds transfer directly from the account of the cardholder to the account of the merchant.
- [T22 row 6](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0022.md): Unpaid Card Transaction  Transaction is related to the return of a debit/credit payment that has not been settled or has been rejected by the card holder for a justified reason.

## Relationships and reuse

- [merchant](btc-merchant.md).
- [credit institution or a card company](btc-card-issuer.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
