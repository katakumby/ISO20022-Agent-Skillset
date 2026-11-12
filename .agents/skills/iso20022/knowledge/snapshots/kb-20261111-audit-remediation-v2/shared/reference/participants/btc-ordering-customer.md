---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-ordering-customer"
source_labels: ["ordering customer"]
aliases: []
source_locations: ["T5 row 15; Payments Families definition", "T25 row 6; Drafts / Bill to Order codes"]
domains: ["payments"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-draft-beneficiary"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# ordering customer — Bank Transaction Code context

## Definition, role and business context

Has issued the draft through an account debited on value date; a failure to debit that account is described for the dishonoured/unpaid-draft code.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T5 row 15](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0005.md): Drafts / Bill Of Orders Transaction is related to a guaranteed bank cheque issued by the account owner with a future value date (do not pay before), which in commercial terms is a ‘negotiable instrument’: the beneficiary can receive early payment from any bank under subtraction of a discount. The ordering customer’s account that has issued the draft is debited on value date.
- [T25 row 6](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0025.md): Dishonoured/Unpaid Draft  Transaction is related to a Dishonoured / Unpaid Draft or Bill To Order. The beneficiary has received early payment, but the ordering customer’s account could not be debited on value date.

## Relationships and reuse

- [beneficiary](btc-draft-beneficiary.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
