---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-customer-provider"
source_labels: ["provider of its customer"]
aliases: []
source_locations: ["T26 row 3; Miscellaneous Debit Operations"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-debtor-bank", "btc-bank-customer"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# provider of its customer — Bank Transaction Code context

## Definition, role and business context

Receives advance invoice-element information from the debtor bank concerning the bank customer settlement on the due date.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T26 row 3](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0026.md): Invoice Accepted with Differed Due Date Service allowing the debtor bank to inform directly and in advance the provider of its customer about the elements of the invoices the customer of the bank will settle on due date.

## Relationships and reuse

- [debtor bank](btc-debtor-bank.md).
- [customer of the bank](btc-bank-customer.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
