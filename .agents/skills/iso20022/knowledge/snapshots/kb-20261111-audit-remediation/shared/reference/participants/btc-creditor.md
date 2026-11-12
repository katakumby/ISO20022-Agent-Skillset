---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-creditor"
source_labels: ["creditor"]
aliases: []
source_locations: ["T5 row 4; Payments Families definition", "T19 row 11; Received and Issued Direct Debits codes", "T19 row 13; Received and Issued Direct Debits codes"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-debtor", "btc-cash-account-owner"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# creditor — Bank Transaction Code context

## Definition, role and business context

Receives the payable-credit-transfer amount. May request cancellation of an initial direct debit after crediting but before interbank settlement, or request reimbursement of the debtor.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T5 row 4](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Issued Credit Transfers Payable Credit Transfers are instructions to transfer an amount of money by the account owner to a creditor. The payable credit transfers are related to instructions sent by the account owner.
- [T19 row 11](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0019.md): Reversal due to a Payment Cancellation Request Transaction is related to the cancellation of an initial direct debit upon request from the creditor. The creditor had already been credited for the initial direct debit, but interbank settlement had not been completed yet.
- [T19 row 13](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0019.md): Reversal due to Payment Reversal    Transaction is related to the reversal / reimbursement of a direct debit transaction (which may be related to a double processing, the debit of an incorrect account, or request to reimburse the debtor issued by the creditor)

## Relationships and reuse

- [debtor](btc-debtor.md).
- [account owner](btc-cash-account-owner.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
