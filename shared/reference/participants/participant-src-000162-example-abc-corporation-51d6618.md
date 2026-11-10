---
template: false
document_kind: "participant"
title: "ABC Corporation — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1572–P1671; /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-abc-corporation-51d6618"
source_labels: ["ABC Corporation"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Cdtr"]
functional_roles: ["Cdtr"]
flow_ids: ["flow-src-000162-example-08"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# ABC Corporation

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Source label: ABC Corporation. No institution identity is inferred from a role name.

Source postal context: {"Dept": "Treasury Department", "StrtNm": "Bush Street", "BldgNb": "13", "PstCd": "CA 94108", "TwnNm": "San Francisco", "Ctry": "US"}.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example10](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-10-pacs.008.001.14.md) | Cdtr | P1572–P1671; /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
