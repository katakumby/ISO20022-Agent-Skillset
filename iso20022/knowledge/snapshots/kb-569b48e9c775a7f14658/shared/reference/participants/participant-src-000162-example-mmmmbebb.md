---
template: false
document_kind: "participant"
title: "MMMMBEBB — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.010.001.06"]
message_families: ["pacs.010"]
source_locations: [{"source_id": "src-000162", "locator": "P2425–P2503; /FIDrctDbt/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2425–P2503; /FIDrctDbt/CdtInstr/Cdtr/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-mmmmbebb"
source_labels: ["MMMMBEBB"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Cdtr", "InstgAgt"]
functional_roles: ["Cdtr", "InstgAgt"]
flow_ids: ["flow-src-000162-example-19"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# MMMMBEBB

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: MMMMBEBB.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example19](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-19-pacs.010.001.06.md) | InstgAgt | P2425–P2503; /FIDrctDbt/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example19](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-19-pacs.010.001.06.md) | Cdtr | P2425–P2503; /FIDrctDbt/CdtInstr/Cdtr/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-19](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-19.md)
