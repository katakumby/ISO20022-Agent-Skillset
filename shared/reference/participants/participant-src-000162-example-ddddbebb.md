---
template: false
document_kind: "participant"
title: "DDDDBEBB — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/CdtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1678–P1793; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-ddddbebb"
source_labels: ["DDDDBEBB"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["CdtrAgt", "InstdAgt"]
functional_roles: ["CdtrAgt", "InstdAgt"]
flow_ids: ["flow-src-000162-example-08"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# DDDDBEBB

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: DDDDBEBB.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example9](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-09-pacs.008.001.14.md) | CdtrAgt | P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/CdtrAgt/FinInstnId/BICFI |
| [Example11](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-11-pacs.008.001.14.md) | InstdAgt | P1678–P1793; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example11](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-11-pacs.008.001.14.md) | CdtrAgt | P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
