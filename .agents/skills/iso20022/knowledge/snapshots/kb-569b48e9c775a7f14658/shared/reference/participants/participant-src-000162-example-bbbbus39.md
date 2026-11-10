---
template: false
document_kind: "participant"
title: "BBBBUS39 — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.003.001.12", "pacs.004.001.15", "pacs.007.001.14"]
message_families: ["pacs.003", "pacs.004", "pacs.007"]
source_locations: [{"source_id": "src-000162", "locator": "P740–P835; /FIToFICstmrDrctDbt/DrctDbtTxInf/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P975–P1060; /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P975–P1060; /PmtRtr/TxInf/ChrgsInf/Agt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1067–P1159; /PmtRtr/TxInf/ChrgsInf[1]/Agt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P1168–P1258; /FIToFIPmtRvsl/TxInf/OrgnlTxRef/DbtrAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-bbbbus39"
source_labels: ["BBBBUS39"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Agt", "DbtrAgt", "InstgAgt"]
functional_roles: ["Agt", "DbtrAgt", "InstgAgt"]
flow_ids: ["flow-src-000162-example-02", "flow-src-000162-example-05", "flow-src-000162-example-07"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# BBBBUS39

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: BBBBUS39.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-02-pacs.003.001.12.md) | DbtrAgt | P740–P835; /FIToFICstmrDrctDbt/DrctDbtTxInf/DbtrAgt/FinInstnId/BICFI |
| [Example5](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-05-pacs.004.001.15.md) | InstgAgt | P975–P1060; /PmtRtr/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [Example5](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-05-pacs.004.001.15.md) | Agt | P975–P1060; /PmtRtr/TxInf/ChrgsInf/Agt/FinInstnId/BICFI |
| [Example6](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-06-pacs.004.001.15.md) | Agt | P1067–P1159; /PmtRtr/TxInf/ChrgsInf[1]/Agt/FinInstnId/BICFI |
| [Example7](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-07-pacs.007.001.14.md) | DbtrAgt | P1168–P1258; /FIToFIPmtRvsl/TxInf/OrgnlTxRef/DbtrAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-02](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-02.md)
- [flow-src-000162-example-05](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-05.md)
- [flow-src-000162-example-07](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-07.md)
