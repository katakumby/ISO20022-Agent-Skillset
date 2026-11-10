---
template: false
document_kind: "participant"
title: "Swedish RTGS system RIX — clearing/settlement source examples"
review_status: "reviewed"
manual_curated: true
domain: "shared"
source_ids: ["src-000162"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P2286", "heading_path": ["Business Examples", "FinancialInstitutionCreditTransfer pacs.009.001.13 - 2", "Second FinancialInstitutionCreditTransfer"]}]
domains: ["payments"]
participant_id: "participant-src-000162-example-swedish-rtgs-system-rix-e7f1416"
source_labels: ["Swedish RTGS system RIX"]
aliases: []
participant_kind: "source-example participant"
business_roles: ["clearing-system"]
functional_roles: ["clearing-system"]
flow_ids: ["flow-src-000162-example-16"]
identifier_schemes: []
limitations: ["A named participant in supplied examples, not a claim about a current real institution.", "Scope is source162 Business Examples; names are not merged with external or other-publication participants."]
source_editions: ["March 2026"]
---

# Swedish RTGS system RIX

[src-000162](../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Definition and scope

Carries the CCCC→FFFF financial-institution credit transfer.

Source label: Swedish RTGS system RIX. No institution identity is inferred from a role name.

## Responsibilities, relationships and precise evidence

| Source example | Role field | Evidence |
| --- | --- | --- |
| [Example16](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/examples/example-16-pacs.009.001.13.md) | clearing-system | P2286 |


Sending/receiving responsibility is explicit only where the GroupHeader identifies InstgAgt/InstdAgt. Other role fields describe their containing payment or underlying transaction, not a universal institution type. The linked flow narrative gives account-owner/servicer relationships and actions where stated.

## Applicable flows

- [flow-src-000162-example-16](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/flows/example-src-000162-16.md)
