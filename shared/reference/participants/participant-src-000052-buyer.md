---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
domains: ["securities"]
source_ids: ["src-000052"]
source_editions: ["March 2026"]
participant_id: "participant-src-000052-buyer"
title: "Buyer"
source_labels: ["Buyer"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000052", "locator": "P114; P218; T12 row3"}]
message_sets: ["ccp-clearing"]
message_ids: []
flows: ["flow-src-000052-p191-business-process-trade-management", "flow-src-000052-p217-trade-leg-notification-business-transaction"]
search_terms: ["Buyer"]
limitations: ["Scoped narrative role; the source does not provide a separate formal participant definition or an identifier scheme. No institution-level equivalence is inferred."]
---





# Buyer

## Definition and context

Buyer in the original contract replaced through CCP novation. The source describes the CCP becoming its counterparty.

Source: [src-000052](../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx); P114; P218; T12 row3.

## Responsibilities

- Has the original contract replaced by a contract with the CCP through novation.

## Relationships and identification

The linked CCP clearing flow determines the relationship and action. No identifier scheme is specified in the cited source passage. This contextual role is not merged with similarly named roles in other message sets.

CCP clearing flow: [Trade Leg Notification](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p217-trade-leg-notification-business-transaction.md); diagram [fig-0012](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0012.md). Narrative role; not drawn in this two-endpoint sequence.

Activity responsibilities: [Trade Management activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p191-business-process-trade-management.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0006.md). Narrative-only participants remain distinct from the drawn lanes.
