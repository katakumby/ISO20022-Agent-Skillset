---
template: false
document_kind: "participant"
title: "Seed Inc. — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.004.001.15"]
message_families: ["pacs.004"]
source_locations: [{"source_id": "src-000162", "locator": "P844–P899; /PmtRtr/TxInf/RtrRsnInf/Orgtr/Nm"}, {"source_id": "src-000162", "locator": "P906–P966; /PmtRtr/TxInf/RtrRsnInf/Orgtr/Nm"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-seed-inc-0785746"
source_labels: ["Seed Inc."]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Orgtr"]
functional_roles: ["Orgtr"]
flow_ids: ["flow-src-000162-example-03"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# Seed Inc.

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Source label: Seed Inc.. No institution identity is inferred from a role name.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example3](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-03-pacs.004.001.15.md) | Orgtr | P844–P899; /PmtRtr/TxInf/RtrRsnInf/Orgtr/Nm |
| [Example4](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-04-pacs.004.001.15.md) | Orgtr | P906–P966; /PmtRtr/TxInf/RtrRsnInf/Orgtr/Nm |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-03](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-03.md)
