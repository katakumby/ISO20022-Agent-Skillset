---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
domains: ["securities"]
source_ids: ["src-000052"]
source_editions: ["March 2026"]
participant_id: "participant-src-000052-preferred-brokers"
title: "Preferred Brokers"
source_labels: ["Preferred Brokers"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000052", "locator": "T17 row4, CCP column"}]
message_sets: ["ccp-clearing"]
message_ids: []
flows: ["flow-src-000052-p204-settlement-management-buy-in-process", "flow-src-000052-p250-buy-in-business-transaction"]
search_terms: ["Preferred Brokers"]
limitations: ["Scoped narrative role; the source does not provide a separate formal participant definition or an identifier scheme. No institution-level equivalence is inferred."]
---





# Preferred Brokers

## Definition and context

Pool of brokers that a CCP may contact to obtain missing securities after the buy-in process has been launched.

Source: [src-000052](../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx); T17 row4, CCP column.

## Responsibilities

- May be contacted by the CCP as an alternative to an auction when obtaining missing securities.

## Relationships and identification

The linked CCP clearing flow determines the relationship and action. No identifier scheme is specified in the cited source passage. This contextual role is not merged with similarly named roles in other message sets.

CCP clearing flow: [Buy-in](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p250-buy-in-business-transaction.md); diagram [fig-0018](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0018.md). Narrative role; not drawn in this two-endpoint sequence.

Activity responsibilities: [Settlement Management: Buy-In activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p204-settlement-management-buy-in-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0011.md). Narrative-only participants remain distinct from the drawn lanes.
