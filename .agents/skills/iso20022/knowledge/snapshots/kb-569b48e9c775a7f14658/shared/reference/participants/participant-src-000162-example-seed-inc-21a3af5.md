---
template: false
document_kind: "participant"
title: "Seed Inc. — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1805–P1907; /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm"}, {"source_id": "src-000162", "locator": "P1914–P2027; /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-seed-inc-21a3af5"
source_labels: ["Seed Inc."]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Cdtr"]
functional_roles: ["Cdtr"]
flow_ids: ["flow-src-000162-example-12"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# Seed Inc.

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Source label: Seed Inc.. No institution identity is inferred from a role name.

Source postal context: {"StrtNm": "Grain Lane", "BldgNb": "27", "TwnNm": "Dublin", "Ctry": "IE"}.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-12-pacs.008.001.14.md) | Cdtr | P1805–P1907; /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm |
| [Example13](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-13-pacs.008.001.14.md) | Cdtr | P1914–P2027; /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-12.md)
