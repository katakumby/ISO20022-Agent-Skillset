---
template: false
document_kind: "participant"
title: "Mr. Jones — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/Dbtr/Nm"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-mr-jones-909aee6"
source_labels: ["Mr. Jones"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["Dbtr"]
functional_roles: ["Dbtr"]
flow_ids: ["flow-src-000162-example-08"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# Mr. Jones

[src-000162](../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Source label: Mr. Jones. No institution identity is inferred from a role name.

Source postal context: {"StrtNm": "16th Street", "BldgNb": "30", "PstCd": "NY10023", "TwnNm": "New York", "Ctry": "US"}.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example9](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-09-pacs.008.001.14.md) | Dbtr | P1397–P1567; /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/Dbtr/Nm |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-08](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-08.md)
