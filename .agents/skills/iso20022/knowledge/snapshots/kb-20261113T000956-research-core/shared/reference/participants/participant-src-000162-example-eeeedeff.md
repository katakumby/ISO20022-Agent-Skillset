---
template: false
document_kind: "participant"
title: "EEEEDEFF — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1397–P1567; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/CdtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1678–P1793; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/ChrgsInf[2]/Agt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-eeeedeff"
source_labels: ["EEEEDEFF"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Agt", "CdtrAgt", "InstdAgt", "InstgAgt"]
functional_roles: ["Agt", "CdtrAgt", "InstdAgt", "InstgAgt"]
flow_ids: ["flow-src-000162-example-08"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# EEEEDEFF

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: EEEEDEFF.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example9](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-09-pacs.008.001.14.md) | InstdAgt | P1397–P1567; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example9](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-09-pacs.008.001.14.md) | CdtrAgt | P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/CdtrAgt/FinInstnId/BICFI |
| [Example11](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-11-pacs.008.001.14.md) | InstgAgt | P1678–P1793; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example11](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-11-pacs.008.001.14.md) | Agt | P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/ChrgsInf[2]/Agt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
