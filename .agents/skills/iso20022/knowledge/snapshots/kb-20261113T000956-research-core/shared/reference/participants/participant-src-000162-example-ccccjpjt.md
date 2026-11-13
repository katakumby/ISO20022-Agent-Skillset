---
template: false
document_kind: "participant"
title: "CCCCJPJT — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14", "pacs.009.001.13"]
message_families: ["pacs.008", "pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P1284–P1392; /FIToFICstmrCdtTrf/GrpHdr/SttlmInf/InstgRmbrsmntAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2036–P2147; /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2154–P2199; /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-ccccjpjt"
source_labels: ["CCCCJPJT"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["InstdAgt", "InstgAgt", "InstgRmbrsmntAgt"]
functional_roles: ["InstdAgt", "InstgAgt", "InstgRmbrsmntAgt"]
flow_ids: ["flow-src-000162-example-08", "flow-src-000162-example-14"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# CCCCJPJT

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: CCCCJPJT.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-08-pacs.008.001.14.md) | InstgRmbrsmntAgt | P1284–P1392; /FIToFICstmrCdtTrf/GrpHdr/SttlmInf/InstgRmbrsmntAgt/FinInstnId/BICFI |
| [Example14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-14-pacs.009.001.13.md) | InstdAgt | P2036–P2147; /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example15](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-15-pacs.009.001.13.md) | InstgAgt | P2154–P2199; /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
- [flow-src-000162-example-14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-14.md)
