---
template: false
document_kind: "participant"
title: "AAAAGB2L — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.004.001.15", "pacs.008.001.14", "pacs.009.001.13", "pacs.028.001.07"]
message_families: ["pacs.004", "pacs.008", "pacs.009", "pacs.028"]
source_locations: [{"source_id": "src-000162", "locator": "P906–P966; /PmtRtr/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1284–P1392; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1284–P1392; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1805–P1907; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1805–P1907; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1914–P2027; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2036–P2147; /FICdtTrf/CdtTrfTxInf/Cdtr/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/CdtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2154–P2199; /FICdtTrf/CdtTrfTxInf/Cdtr/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2514–P2615; /FIToFIPmtStsReq/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2514–P2615; /FIToFIPmtStsReq/TxInf/OrgnlTxRef/CdtrAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-aaaagb2l"
source_labels: ["AAAAGB2L"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Cdtr", "CdtrAgt", "DbtrAgt", "InstdAgt", "InstgAgt"]
functional_roles: ["Cdtr", "CdtrAgt", "DbtrAgt", "InstdAgt", "InstgAgt"]
flow_ids: ["flow-src-000162-example-03", "flow-src-000162-example-08", "flow-src-000162-example-12", "flow-src-000162-example-14", "flow-src-000162-example-20"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# AAAAGB2L

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: AAAAGB2L.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example4](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-04-pacs.004.001.15.md) | InstdAgt | P906–P966; /PmtRtr/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-08-pacs.008.001.14.md) | InstdAgt | P1284–P1392; /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-08-pacs.008.001.14.md) | CdtrAgt | P1284–P1392; /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [Example12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-12-pacs.008.001.14.md) | InstgAgt | P1805–P1907; /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-12-pacs.008.001.14.md) | DbtrAgt | P1805–P1907; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [Example13](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-13-pacs.008.001.14.md) | DbtrAgt | P1914–P2027; /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [Example14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-14-pacs.009.001.13.md) | Cdtr | P2036–P2147; /FICdtTrf/CdtTrfTxInf/Cdtr/FinInstnId/BICFI |
| [Example14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-14-pacs.009.001.13.md) | CdtrAgt | P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/CdtrAgt/FinInstnId/BICFI |
| [Example15](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-15-pacs.009.001.13.md) | Cdtr | P2154–P2199; /FICdtTrf/CdtTrfTxInf/Cdtr/FinInstnId/BICFI |
| [Example20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-20-pacs.028.001.07.md) | InstdAgt | P2514–P2615; /FIToFIPmtStsReq/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-20-pacs.028.001.07.md) | CdtrAgt | P2514–P2615; /FIToFIPmtStsReq/TxInf/OrgnlTxRef/CdtrAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-03](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-03.md)
- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
- [flow-src-000162-example-12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-12.md)
- [flow-src-000162-example-14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-14.md)
- [flow-src-000162-example-20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-20.md)
