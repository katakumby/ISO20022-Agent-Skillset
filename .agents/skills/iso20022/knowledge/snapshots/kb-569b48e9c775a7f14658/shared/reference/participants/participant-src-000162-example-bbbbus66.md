---
template: false
document_kind: "participant"
title: "BBBBUS66 — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1572–P1671; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1572–P1671; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-bbbbus66"
source_labels: ["BBBBUS66"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["CdtrAgt", "InstdAgt"]
functional_roles: ["CdtrAgt", "InstdAgt"]
flow_ids: ["flow-src-000162-example-08"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# BBBBUS66

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: BBBBUS66.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example10](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-10-pacs.008.001.14.md) | InstdAgt | P1572–P1671; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example10](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-10-pacs.008.001.14.md) | CdtrAgt | P1572–P1671; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
