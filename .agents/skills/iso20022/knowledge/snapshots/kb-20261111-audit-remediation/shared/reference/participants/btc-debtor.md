---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-debtor"
source_labels: ["debtor"]
aliases: []
source_locations: ["T5 row 3; Payments Families definition", "T17 row 15; Received and Issued Credit Transfers codes", "T19 row 12; Received and Issued Direct Debits codes"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-creditor", "btc-cash-account-owner", "btc-debtor-bank"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# debtor — Bank Transaction Code context

## Definition, role and business context

Provides the amount received by the account owner in received-credit-transfer definitions. May request cancellation after being debited but before interbank settlement, and may request a direct-debit refund.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T5 row 3](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Received Credit Transfers  Receivable Credit Transfers are instructions to receive an amount of money from a debtor by the account owner. The receivable credit transfers are related to transactions received by the account owner.
- [T17 row 15](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0017.md): Reversal due to Payment Cancellation Request Transaction is related to the cancellation of an initial credit transfer upon request from the debtor. The debtor had already been debited for the initial credit transfer, but interbank settlement had not been completed yet.
- [T19 row 12](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0019.md): Reversal due to Return/Unpaid Direct Debit  Transaction is related to a Returned Direct Debit. Several reasons may exist: debtor’s account closed, insufficient funds available, request for refund by the Debtor, etc.

## Relationships and reuse

- [creditor](btc-creditor.md).
- [account owner](btc-cash-account-owner.md).
- [debtor bank](btc-debtor-bank.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
