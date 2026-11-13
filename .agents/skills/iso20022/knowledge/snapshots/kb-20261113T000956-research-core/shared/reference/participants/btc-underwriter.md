---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-underwriter"
source_labels: ["underwriters"]
aliases: []
source_locations: ["T37 row 22; Trading, Clearing and Settlement & Non Settled Sub-families codes"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-lead-manager"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# underwriters — Bank Transaction Code context

## Definition, role and business context

Participates in a syndicate through which securities are issued, together with a Lead Manager.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T37 row 22](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0037.md): Syndicated Cash movement related to the issue of securities (bonds, warrants, equities etc) through a syndicate of underwriters and a Lead Manager.

## Relationships and reuse

- [Lead Manager](btc-lead-manager.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
