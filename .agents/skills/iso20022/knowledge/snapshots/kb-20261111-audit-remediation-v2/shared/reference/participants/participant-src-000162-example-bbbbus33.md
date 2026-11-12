---
template: false
document_kind: "participant"
title: "BBBBUS33 — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14", "pacs.009.001.13", "pacs.028.001.07"]
message_families: ["pacs.008", "pacs.009", "pacs.028"]
source_locations: [{"source_id": "src-000162", "locator": "P1284–P1392; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1284–P1392; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1397–P1567; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/ChrgsInf/Agt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1572–P1671; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1572–P1671; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/ChrgsInf[1]/Agt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2036–P2147; /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2036–P2147; /FICdtTrf/CdtTrfTxInf/Dbtr/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2154–P2199; /FICdtTrf/CdtTrfTxInf/Dbtr/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2514–P2615; /FIToFIPmtStsReq/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2514–P2615; /FIToFIPmtStsReq/TxInf/OrgnlTxRef/DbtrAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-bbbbus33"
source_labels: ["BBBBUS33"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Agt", "Dbtr", "DbtrAgt", "InstgAgt"]
functional_roles: ["Agt", "Dbtr", "DbtrAgt", "InstgAgt"]
flow_ids: ["flow-src-000162-example-08", "flow-src-000162-example-14", "flow-src-000162-example-20"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# BBBBUS33

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: BBBBUS33.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-08-pacs.008.001.14.md) | InstgAgt | P1284–P1392; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-08-pacs.008.001.14.md) | DbtrAgt | P1284–P1392; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [Example9](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-09-pacs.008.001.14.md) | InstgAgt | P1397–P1567; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example9](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-09-pacs.008.001.14.md) | Agt | P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/ChrgsInf/Agt/FinInstnId/BICFI |
| [Example9](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-09-pacs.008.001.14.md) | DbtrAgt | P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/DbtrAgt/FinInstnId/BICFI |
| [Example9](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-09-pacs.008.001.14.md) | DbtrAgt | P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/DbtrAgt/FinInstnId/BICFI |
| [Example10](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-10-pacs.008.001.14.md) | InstgAgt | P1572–P1671; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example10](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-10-pacs.008.001.14.md) | DbtrAgt | P1572–P1671; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [Example11](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-11-pacs.008.001.14.md) | Agt | P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/ChrgsInf[1]/Agt/FinInstnId/BICFI |
| [Example11](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-11-pacs.008.001.14.md) | DbtrAgt | P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [Example14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-14-pacs.009.001.13.md) | InstgAgt | P2036–P2147; /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-14-pacs.009.001.13.md) | Dbtr | P2036–P2147; /FICdtTrf/CdtTrfTxInf/Dbtr/FinInstnId/BICFI |
| [Example14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-14-pacs.009.001.13.md) | DbtrAgt | P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/DbtrAgt/FinInstnId/BICFI |
| [Example15](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-15-pacs.009.001.13.md) | Dbtr | P2154–P2199; /FICdtTrf/CdtTrfTxInf/Dbtr/FinInstnId/BICFI |
| [Example20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-20-pacs.028.001.07.md) | InstgAgt | P2514–P2615; /FIToFIPmtStsReq/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-20-pacs.028.001.07.md) | DbtrAgt | P2514–P2615; /FIToFIPmtStsReq/TxInf/OrgnlTxRef/DbtrAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
- [flow-src-000162-example-14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-14.md)
- [flow-src-000162-example-20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-20.md)
