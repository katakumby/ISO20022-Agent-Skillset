---
template: false
document_kind: "participant"
title: "DEF Electronics — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14", "pacs.028.001.07"]
message_families: ["pacs.008", "pacs.028"]
source_locations: [{"source_id": "src-000162", "locator": "P1284–P1392; /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm"}, {"source_id": "src-000162", "locator": "P2514–P2615; /FIToFIPmtStsReq/TxInf/OrgnlTxRef/Cdtr/Pty/Nm"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-def-electronics-bf4c618"
source_labels: ["DEF Electronics"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Cdtr"]
functional_roles: ["Cdtr"]
flow_ids: ["flow-src-000162-example-08", "flow-src-000162-example-20"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# DEF Electronics

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Source label: DEF Electronics. No institution identity is inferred from a role name.

Source postal context: {"StrtNm": "Mark Lane", "BldgNb": "55", "PstCd": "EC3R7NE", "TwnNm": "London", "Ctry": "GB", "AdrLine": "Corn Exchange 5th Floor"}.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example8](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-08-pacs.008.001.14.md) | Cdtr | P1284–P1392; /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm |
| [Example20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-20-pacs.028.001.07.md) | Cdtr | P2514–P2615; /FIToFIPmtStsReq/TxInf/OrgnlTxRef/Cdtr/Pty/Nm |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
- [flow-src-000162-example-20](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-20.md)
