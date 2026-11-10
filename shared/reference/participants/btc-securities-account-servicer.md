---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-securities-account-servicer"
source_labels: ["account servicer"]
aliases: []
source_locations: ["T37 row 17; Trading, Clearing and Settlement & Non Settled Sub-families codes", "T37 row 18; Trading, Clearing and Settlement & Non Settled Sub-families codes", "T37 row 21; Trading, Clearing and Settlement & Non Settled Sub-families codes"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-securities-instructing-party", "btc-investment-manager"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# account servicer — Bank Transaction Code context

## Definition, role and business context

Services the account relationships in internal/external securities transfers and may be a source or destination servicer for a portfolio move.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T37 row 17](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0037.md): External Account Transfer Cash movement related to an external securities account transfer ie a transfer involving more than one instructing party and/or account servicer.
- [T37 row 18](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0037.md): Internal Account Transfer Cash movement related to an internal securities account transfer ie a transfer involving one instructing party at one account servicer.
- [T37 row 21](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0037.md): Portfolio Move Cash movement related to a portfolio move from one investment manager to another and/or from an account servicer to another.

## Relationships and reuse

- [instructing party](btc-securities-instructing-party.md).
- [investment manager](btc-investment-manager.md).

The same label has separate cash-reporting and securities-transfer records. These scopes are cross-retrievable, without transferring workflow responsibilities between them: [other account-servicer context](btc-cash-account-servicer.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
