---
template: false
document_kind: "participant"
title: "DDDDLULL — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P2213–P2283; /FICdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2290–P2351; /FICdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2358–P2416; /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-ddddlull"
source_labels: ["DDDDLULL"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["CdtrAgt", "InstdAgt"]
functional_roles: ["CdtrAgt", "InstdAgt"]
flow_ids: ["flow-src-000162-example-16"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# DDDDLULL

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: DDDDLULL.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example16](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-16-pacs.009.001.13.md) | CdtrAgt | P2213–P2283; /FICdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [Example17](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-17-pacs.009.001.13.md) | CdtrAgt | P2290–P2351; /FICdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [Example18](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-18-pacs.009.001.13.md) | InstdAgt | P2358–P2416; /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-16](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-16.md)
