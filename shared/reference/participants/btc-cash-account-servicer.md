---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-cash-account-servicer"
source_labels: ["account servicer"]
aliases: []
source_locations: ["P92 and P101; §3.1.1; rendered file/printed page 5", "T17 row 4; Received and Issued Credit Transfers codes"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: ["btc-cash-reporting-and-reconciliation", "btc-standing-order-processing"]
relationships: ["btc-cash-account-owner", "btc-originating-party"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# account servicer — Bank Transaction Code context

## Definition, role and business context

Reports transactions with the Bank Transaction Code for the cash account owner; receives an authorised standing order and processes the instructed periodic credit transfers.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

[src-000003](../../../raw-input/ExternalCodeSets/BTC_ExternalCodeListDescription_Nov2025.docx), P92 and P101, §3.1.1, rendered page 5: bank-to-customer cash reporting supports the servicer reporting and the owner cash-management/reconciliation activities, including reconciliation to a sub-ledger or routing to an adequate customer processing system.

- [T17 row 4](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0017.md): Standing Order  Transaction is a standing order. A standing order is an instruction given by a party having explicit authority on the debtor’s account to debit, i.e. either debit account owner or originating party, to an account servicer, to process credit transfers at specified intervals during an implicit or explicit period of time. It is given once, and is valid for an open or closed period of time.

## Relationships and reuse

- [account owner](btc-cash-account-owner.md).
- [originating party](btc-originating-party.md).

The same label has separate cash-reporting and securities-transfer records. These scopes are cross-retrievable, without transferring workflow responsibilities between them: [other account-servicer context](btc-securities-account-servicer.md).

## Flows, messages and identifiers

- [btc-cash-reporting-and-reconciliation](../code-sets/bank-transaction-codes/november-2025-v8.0/flows/btc-cash-reporting-and-reconciliation.md).
- [btc-standing-order-processing](../code-sets/bank-transaction-codes/november-2025-v8.0/flows/btc-standing-order-processing.md).

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
