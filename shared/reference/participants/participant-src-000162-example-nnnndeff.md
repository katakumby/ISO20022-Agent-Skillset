---
template: false
document_kind: "participant"
title: "NNNNDEFF — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.010.001.06"]
message_families: ["pacs.010"]
source_locations: [{"source_id": "src-000162", "locator": "P2425–P2503; /FIDrctDbt/GrpHdr/InstdAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2425–P2503; /FIDrctDbt/CdtInstr/DrctDbtTxInf[1]/DbtrAgt/FinInstnId/BICFI"}, {"source_id": "src-000162", "locator": "P2425–P2503; /FIDrctDbt/CdtInstr/DrctDbtTxInf[2]/DbtrAgt/FinInstnId/BICFI"}]
domains: ["payments"]
participant_id: "participant-src-000162-example-nnnndeff"
source_labels: ["NNNNDEFF"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["DbtrAgt", "InstdAgt"]
functional_roles: ["DbtrAgt", "InstdAgt"]
flow_ids: ["flow-src-000162-example-19"]
identifier_schemes: ["BICFI"]
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# NNNNDEFF

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition and scope

A named participant explicitly identified in the supplied clearing and settlement examples. Its roles below are scoped to each message instance and account relationship.

Identifier is supplied in BICFI fields: NNNNDEFF.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example19](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-19-pacs.010.001.06.md) | InstdAgt | P2425–P2503; /FIDrctDbt/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Example19](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-19-pacs.010.001.06.md) | DbtrAgt | P2425–P2503; /FIDrctDbt/CdtInstr/DrctDbtTxInf[1]/DbtrAgt/FinInstnId/BICFI |
| [Example19](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-19-pacs.010.001.06.md) | DbtrAgt | P2425–P2503; /FIDrctDbt/CdtInstr/DrctDbtTxInf[2]/DbtrAgt/FinInstnId/BICFI |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-19](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-19.md)
