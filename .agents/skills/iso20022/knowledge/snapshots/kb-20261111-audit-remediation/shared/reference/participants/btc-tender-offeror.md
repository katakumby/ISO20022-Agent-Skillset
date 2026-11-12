---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-tender-offeror"
source_labels: ["third party"]
aliases: []
source_locations: ["T40 row 29; Corporate Action & Custody Sub-Families codes"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-shareholder"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# third party — Bank Transaction Code context

## Definition, role and business context

Normally makes the offer requesting shareholders to sell or exchange their equities in the Tender definition; the source says normally and does not make third-party status mandatory.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T40 row 29](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0040.md): Tender Cash movement related to an offer made to shareholders, normally by a third party, requesting them to sell (tender) or exchange their equities.

## Relationships and reuse

- [shareholders](btc-shareholder.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
