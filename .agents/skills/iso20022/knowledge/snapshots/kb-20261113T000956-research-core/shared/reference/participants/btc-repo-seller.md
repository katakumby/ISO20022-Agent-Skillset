---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-repo-seller"
source_labels: ["seller"]
aliases: []
source_locations: ["T37 row 9; Trading, Clearing and Settlement & Non Settled Sub-families codes"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-repo-buyer"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# seller — Bank Transaction Code context

## Definition, role and business context

Acquires cash by selling collateral securities and simultaneously agrees to repurchase the same or similar securities at a future, possibly open, time in the repo definition.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T37 row 9](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0037.md): Repo Cash movement related to the initiation or closing of a repo transaction in which a seller acquires cash by selling securities (used as collateral) and simultaneously agrees to repurchase the same or similar securities at a future (may be open) time.

## Relationships and reuse

- [buyer](btc-repo-buyer.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
