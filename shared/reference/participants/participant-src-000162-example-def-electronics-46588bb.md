---
template: false
document_kind: "participant"
title: "DEF Electronics — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/Cdtr/Nm"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-def-electronics-46588bb"
source_labels: ["DEF Electronics"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Cdtr"]
functional_roles: ["Cdtr"]
flow_ids: ["flow-src-000162-example-14"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# DEF Electronics

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Source label: DEF Electronics. No institution identity is inferred from a role name.

Source postal context: {"StrtNm": "Mark Lane", "BldgNb": "55", "PstCd": "EC3RZNE", "TwnNm": "London", "Ctry": "GB", "AdrLine": "Corn Exchange 5th Floor"}.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-14-pacs.009.001.13.md) | Cdtr | P2036–P2147; /FICdtTrf/CdtTrfTxInf/UndrlygCstmrCdtTrf/Cdtr/Nm |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-14](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-14.md)
