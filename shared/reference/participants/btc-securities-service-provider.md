---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-securities-service-provider"
source_labels: ["service-provider"]
aliases: []
source_locations: ["T37 row 35; Trading, Clearing and Settlement & Non Settled Sub-families codes", "T37 row 38; Trading, Clearing and Settlement & Non Settled Sub-families codes"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-ccp-function-provider"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# service-provider — Bank Transaction Code context

## Definition, role and business context

May not distinguish CCP from other transactions; the Exchange Traded and OTC undifferentiated codes are only to be used under that stated condition.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T37 row 35](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0037.md): Exchange Traded Representing cash legs of transactions traded in exchanges – this code is only to be used where the service-provider does not distinguish between transactions going through CCP and other transactions
- [T37 row 38](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0037.md): OTC Represents the cash legs of transactions ‘over the counter’ (OTC) exchanges – this code is only to be used where the service-provider does not distinguish between transactions going through CCP and other transactions

## Relationships and reuse

- [CCP](btc-ccp-function-provider.md).

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
