---
template: false
document_kind: "participant"
title: "FFFFSESS — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P2213–P2283; /FICdtTrf/CdtTrfTxInf/IntrmyAgt1/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2290–P2351; /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2358–P2416; /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-ffffsess"
source_labels: ["FFFFSESS"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["InstdAgt", "InstgAgt", "IntrmyAgt1"]
functional_roles: ["InstdAgt", "InstgAgt", "IntrmyAgt1"]
flow_ids: ["flow-src-000162-example-16"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# FFFFSESS

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: FFFFSESS.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example16](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-16-pacs.009.001.13.md) | IntrmyAgt1 | P2213–P2283; /FICdtTrf/CdtTrfTxInf/IntrmyAgt1/FinInstnId/BICFI |
| [Example17](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-17-pacs.009.001.13.md) | InstdAgt | P2290–P2351; /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example18](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-18-pacs.009.001.13.md) | InstgAgt | P2358–P2416; /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-16](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-16.md)
