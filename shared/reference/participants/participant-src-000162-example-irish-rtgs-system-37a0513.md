---
template: false
document_kind: "participant"
title: "Irish RTGS system — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1910", "heading_path": ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 2", "Second FIToFICustomerCreditTransfer"]}]
domains: ["payments"]
participant_id: "participant-src-000162-example-irish-rtgs-system-37a0513"
source_labels: ["Irish RTGS system"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["clearing-system"]
functional_roles: ["clearing-system"]
flow_ids: ["flow-src-000162-example-12"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# Irish RTGS system

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition and scope

Carries the BBBB→CCCC customer credit transfer.

Source label: Irish RTGS system. No institution identity is inferred from a role name.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-12-pacs.008.001.14.md) | clearing-system | P1910 |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-12](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-12.md)
