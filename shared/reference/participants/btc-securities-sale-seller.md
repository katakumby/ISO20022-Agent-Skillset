---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-securities-sale-seller"
source_labels: ["seller"]
aliases: []
source_locations: ["T13 row 10; Securities Families definition"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-securities-sale-participant"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# seller — Bank Transaction Code context

## Definition, role and business context

Lack of the seller holdings can cause sales to fail; the LACK family represents extra funding for the resulting forecast cash non-delivery to the participant.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T13 row 10](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0013.md): LACK ‘LACK’ is an extra amount to be funded in addition to ‘FUND’, as it is a forecast of a cash amount that will not be delivered to the participant due to sales that will fail because of lack of holdings from the seller

## Relationships and reuse

- [participant](btc-securities-sale-participant.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
