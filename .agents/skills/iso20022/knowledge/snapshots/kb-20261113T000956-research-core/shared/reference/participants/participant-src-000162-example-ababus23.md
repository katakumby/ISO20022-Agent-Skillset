---
template: false
document_kind: "participant"
title: "ABABUS23 — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.002.001.16", "pacs.003.001.12", "pacs.004.001.15", "pacs.007.001.14"]
message_families: ["pacs.002", "pacs.003", "pacs.004", "pacs.007"]
source_locations: [{"source_id": "src-000162", "locator": "P659–P731; /FIToFIPmtStsRpt/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P740–P835; /FIToFICstmrDrctDbt/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P975–P1060; /PmtRtr/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1067–P1159; /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1067–P1159; /PmtRtr/TxInf/ChrgsInf[2]/Agt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1168–P1258; /FIToFIPmtRvsl/GrpHdr/InstdAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-ababus23"
source_labels: ["ABABUS23"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Agt", "InstdAgt", "InstgAgt"]
functional_roles: ["Agt", "InstdAgt", "InstgAgt"]
flow_ids: ["flow-src-000162-example-01", "flow-src-000162-example-02", "flow-src-000162-example-05", "flow-src-000162-example-07"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# ABABUS23

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: ABABUS23.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-01-pacs.002.001.16.md) | InstgAgt | P659–P731; /FIToFIPmtStsRpt/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-02-pacs.003.001.12.md) | InstdAgt | P740–P835; /FIToFICstmrDrctDbt/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example5](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-05-pacs.004.001.15.md) | InstdAgt | P975–P1060; /PmtRtr/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example6](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-06-pacs.004.001.15.md) | InstgAgt | P1067–P1159; /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example6](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-06-pacs.004.001.15.md) | Agt | P1067–P1159; /PmtRtr/TxInf/ChrgsInf[2]/Agt/FinInstnId/BICFI |
| [Example7](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-07-pacs.007.001.14.md) | InstdAgt | P1168–P1258; /FIToFIPmtRvsl/GrpHdr/InstdAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-01](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-01.md)
- [flow-src-000162-example-02](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-02.md)
- [flow-src-000162-example-05](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-05.md)
- [flow-src-000162-example-07](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-07.md)
