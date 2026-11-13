---
template: false
document_kind: "participant"
title: "ABC Corporation — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14", "pacs.009.001.13", "pacs.028.001.07"]
message_families: ["pacs.008", "pacs.009", "pacs.028"]
source_locations: [{"source_id": "src-000162", "locator": "P1284–P1392; /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm"}, {"source_id": "src-000162", "locator": "P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/Dbtr/Nm"}, {"source_id": "src-000162", "locator": "P1572–P1671; /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm"}, {"source_id": "src-000162", "locator": "P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm"}, {"source_id": "src-000162", "locator": "P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/InitgPty/Nm"}, {"source_id": "src-000162", "locator": "P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/Dbtr/Nm"}, {"source_id": "src-000162", "locator": "P2514–P2615; /FIToFIPmtStsReq/TxInf/OrgnlTxRef/Dbtr/Pty/Nm"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-abc-corporation-875623a"
source_labels: ["ABC Corporation"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Dbtr", "InitgPty"]
functional_roles: ["Dbtr", "InitgPty"]
flow_ids: ["flow-src-000162-example-08", "flow-src-000162-example-14", "flow-src-000162-example-20"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# ABC Corporation

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Source label: ABC Corporation. No institution identity is inferred from a role name.

Source postal context: {"StrtNm": "Times Square", "BldgNb": "7", "PstCd": "NY 10036", "TwnNm": "New York", "Ctry": "US"}.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-08-pacs.008.001.14.md) | Dbtr | P1284–P1392; /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm |
| [Example9](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-09-pacs.008.001.14.md) | Dbtr | P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/Dbtr/Nm |
| [Example10](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-10-pacs.008.001.14.md) | Dbtr | P1572–P1671; /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm |
| [Example11](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-11-pacs.008.001.14.md) | Dbtr | P1678–P1793; /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm |
| [Example14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-14-pacs.009.001.13.md) | InitgPty | P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/InitgPty/Nm |
| [Example14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-14-pacs.009.001.13.md) | Dbtr | P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/Dbtr/Nm |
| [Example20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-20-pacs.028.001.07.md) | Dbtr | P2514–P2615; /FIToFIPmtStsReq/TxInf/OrgnlTxRef/Dbtr/Pty/Nm |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
- [flow-src-000162-example-14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-14.md)
- [flow-src-000162-example-20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-20.md)
