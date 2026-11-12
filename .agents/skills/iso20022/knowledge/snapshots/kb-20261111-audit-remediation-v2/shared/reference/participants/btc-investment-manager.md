---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-investment-manager"
source_labels: ["investment manager"]
aliases: []
source_locations: ["T37 row 21; Trading, Clearing and Settlement & Non Settled Sub-families codes", "T41 row 7; Miscellaneous Securities Operations codes"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-securities-account-servicer"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# investment manager — Bank Transaction Code context

## Definition, role and business context

May be changed by a portfolio move and charges management fees to an account for services provided.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T37 row 21](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0037.md): Portfolio Move Cash movement related to a portfolio move from one investment manager to another and/or from an account servicer to another.
- [T41 row 7](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0041.md): Management Fees Charges that an investment manager applies to an account for services provided.

## Relationships and reuse

- [account servicer](btc-securities-account-servicer.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
