---
template: false
document_kind: "participant"
title: "BBBBIE2D — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.004.001.15", "pacs.008.001.14"]
message_families: ["pacs.004", "pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P844–P899; /PmtRtr/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P906–P966; /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P906–P966; /PmtRtr/TxInf/ChrgsInf[2]/Agt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1805–P1907; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1914–P2027; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1914–P2027; /FIToFICstmrCdtTrf/CdtTrfTxInf/ChrgsInf/Agt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-bbbbie2d"
source_labels: ["BBBBIE2D"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Agt", "InstdAgt", "InstgAgt"]
functional_roles: ["Agt", "InstdAgt", "InstgAgt"]
flow_ids: ["flow-src-000162-example-03", "flow-src-000162-example-12"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# BBBBIE2D

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: BBBBIE2D.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example3](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-03-pacs.004.001.15.md) | InstdAgt | P844–P899; /PmtRtr/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example4](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-04-pacs.004.001.15.md) | InstgAgt | P906–P966; /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example4](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-04-pacs.004.001.15.md) | Agt | P906–P966; /PmtRtr/TxInf/ChrgsInf[2]/Agt/FinInstnId/BICFI |
| [Example12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-12-pacs.008.001.14.md) | InstdAgt | P1805–P1907; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example13](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-13-pacs.008.001.14.md) | InstgAgt | P1914–P2027; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example13](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-13-pacs.008.001.14.md) | Agt | P1914–P2027; /FIToFICstmrCdtTrf/CdtTrfTxInf/ChrgsInf/Agt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-03](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-03.md)
- [flow-src-000162-example-12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-12.md)
