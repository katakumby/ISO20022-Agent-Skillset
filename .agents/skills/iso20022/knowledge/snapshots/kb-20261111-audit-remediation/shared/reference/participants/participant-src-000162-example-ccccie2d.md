---
template: false
document_kind: "participant"
title: "CCCCIE2D — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.004.001.15", "pacs.008.001.14"]
message_families: ["pacs.004", "pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P844–P899; /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P844–P899; /PmtRtr/TxInf/ChrgsInf/Agt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P906–P966; /PmtRtr/TxInf/ChrgsInf[1]/Agt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1805–P1907; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1914–P2027; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1914–P2027; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-ccccie2d"
source_labels: ["CCCCIE2D"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Agt", "CdtrAgt", "InstdAgt", "InstgAgt"]
functional_roles: ["Agt", "CdtrAgt", "InstdAgt", "InstgAgt"]
flow_ids: ["flow-src-000162-example-03", "flow-src-000162-example-12"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# CCCCIE2D

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: CCCCIE2D.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example3](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-03-pacs.004.001.15.md) | InstgAgt | P844–P899; /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example3](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-03-pacs.004.001.15.md) | Agt | P844–P899; /PmtRtr/TxInf/ChrgsInf/Agt/FinInstnId/BICFI |
| [Example4](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-04-pacs.004.001.15.md) | Agt | P906–P966; /PmtRtr/TxInf/ChrgsInf[1]/Agt/FinInstnId/BICFI |
| [Example12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-12-pacs.008.001.14.md) | CdtrAgt | P1805–P1907; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [Example13](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-13-pacs.008.001.14.md) | InstdAgt | P1914–P2027; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example13](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-13-pacs.008.001.14.md) | CdtrAgt | P1914–P2027; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-03](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-03.md)
- [flow-src-000162-example-12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-12.md)
