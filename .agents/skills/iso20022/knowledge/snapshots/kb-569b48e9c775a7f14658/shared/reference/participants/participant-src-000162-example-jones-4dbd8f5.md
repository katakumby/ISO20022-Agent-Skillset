---
template: false
document_kind: "participant"
title: "Jones — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.002.001.16", "pacs.003.001.12", "pacs.004.001.15", "pacs.007.001.14"]
message_families: ["pacs.002", "pacs.003", "pacs.004", "pacs.007"]
source_locations: [{"source_id": "src-000162", "locator": "P659–P731; /FIToFIPmtStsRpt/TxInfAndSts/OrgnlTxRef/Dbtr/Pty/Nm"}, {"source_id": "src-000162", "locator": "P740–P835; /FIToFICstmrDrctDbt/DrctDbtTxInf/Dbtr/Nm"}, {"source_id": "src-000162", "locator": "P975–P1060; /PmtRtr/TxInf/OrgnlTxRef/Dbtr/Pty/Nm"}, {"source_id": "src-000162", "locator": "P1067–P1159; /PmtRtr/TxInf/OrgnlTxRef/Dbtr/Pty/Nm"}, {"source_id": "src-000162", "locator": "P1168–P1258; /FIToFIPmtRvsl/TxInf/OrgnlTxRef/Dbtr/Pty/Nm"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-jones-4dbd8f5"
source_labels: ["Jones"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Dbtr"]
functional_roles: ["Dbtr"]
flow_ids: ["flow-src-000162-example-01", "flow-src-000162-example-02", "flow-src-000162-example-05", "flow-src-000162-example-07"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# Jones

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Source label: Jones. No institution identity is inferred from a role name.

Source postal context: {"StrtNm": "Hudson Street", "BldgNb": "19", "PstCd": "NJ 07302", "TwnNm": "Jersey City", "Ctry": "US"}.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example1](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-01-pacs.002.001.16.md) | Dbtr | P659–P731; /FIToFIPmtStsRpt/TxInfAndSts/OrgnlTxRef/Dbtr/Pty/Nm |
| [Example2](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-02-pacs.003.001.12.md) | Dbtr | P740–P835; /FIToFICstmrDrctDbt/DrctDbtTxInf/Dbtr/Nm |
| [Example5](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-05-pacs.004.001.15.md) | Dbtr | P975–P1060; /PmtRtr/TxInf/OrgnlTxRef/Dbtr/Pty/Nm |
| [Example6](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-06-pacs.004.001.15.md) | Dbtr | P1067–P1159; /PmtRtr/TxInf/OrgnlTxRef/Dbtr/Pty/Nm |
| [Example7](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-07-pacs.007.001.14.md) | Dbtr | P1168–P1258; /FIToFIPmtRvsl/TxInf/OrgnlTxRef/Dbtr/Pty/Nm |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-01](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-01.md)
- [flow-src-000162-example-02](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-02.md)
- [flow-src-000162-example-05](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-05.md)
- [flow-src-000162-example-07](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-07.md)
