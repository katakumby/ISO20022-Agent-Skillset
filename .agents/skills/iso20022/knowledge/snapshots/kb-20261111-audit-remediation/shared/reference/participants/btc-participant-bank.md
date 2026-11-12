---
template: false
review_status: "reviewed"
domain: "shared"
source_ids: ["src-000003"]
source_editions: ["November 2025 Version 8.0"]
message_ids: []
document_kind: "participant"
participant_id: "btc-participant-bank"
source_labels: ["participant bank"]
aliases: []
source_locations: ["T13 row 9; Securities Families definition"]
domains: ["securities"]
message_sets: ["external-code-sets"]
flows: []
relationships: ["btc-main-paying-agent"]
identifier_schemes: []
limitations: ["The publication describes this scoped role through transaction-code definitions; it does not provide a formal participant model or map it to exact message definitions.", "No equivalence with same-named MDR roles, institutions or product-specific roles is asserted."]
---

# participant bank — Bank Transaction Code context

## Definition, role and business context

Has corporate-action payment obligations based on its role as main paying agent, in the Custody Collection family definition.

This is a contextual business-role description from the supplied code publication. Its functional actions are limited to those in the cited evidence; an institution may occupy different roles in different relationships. The document does not formally classify business-role versus functional-participant types.

## Responsibilities and source evidence

- [T13 row 9](../code-sets/bank-transaction-codes/november-2025-v8.0/documents/src-000003/tables/tbl-0013.md): Custody Collection All corporate action related payment obligations of the participant bank, based on their role as main paying agent

## Relationships and reuse

- [main paying agent](btc-main-paying-agent.md).

The source explicitly says the participant bank acts in a main paying agent role here. This does not make the institution category and functional role universally equivalent.

## Flows, messages and identifiers

The cited code definitions do not supply a complete message-exchange flow for this scoped participant.

No exact message identifier, role identifier scheme or source-supported alias is specified in the cited evidence. The role is usable in the External code sets collection; applicability to a particular message must be checked in that exact message reference.

## Review boundary

Definition, actions and source row/paragraph locators checked against the complete supplied Word rendering on 2026-11-09. This reviews the scoped description; it does not fill unavailable business context or resolve publication issues 2 and 33.
