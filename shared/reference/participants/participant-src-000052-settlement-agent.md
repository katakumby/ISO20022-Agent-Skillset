---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
domains: ["securities"]
source_ids: ["src-000052"]
source_editions: ["March 2026"]
participant_id: "participant-src-000052-settlement-agent"
title: "Settlement Agent"
source_labels: ["Settlement Agent"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000052", "locator": "T17 row7, Clearing Member column"}]
message_sets: ["ccp-clearing"]
message_ids: []
flows: ["flow-src-000052-p204-settlement-management-buy-in-process", "flow-src-000052-p250-buy-in-business-transaction"]
search_terms: ["Settlement Agent"]
limitations: ["Scoped narrative role; the source does not provide a separate formal participant definition or an identifier scheme. No institution-level equivalence is inferred."]
---





# Settlement Agent

## Definition and context

Recipient of a prior clearing member settlement instruction that the member cancels in the buy-in flow. The source names settlement agent/CSD as alternative recipient labels, without establishing institutional equivalence.

Source: [src-000052](../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx); T17 row7, Clearing Member column.

## Responsibilities

- Is recipient of the settlement instruction the clearing member cancels after buy-in confirmation; settlement processing is outside this MDR scope.

## Relationships and identification

The linked CCP clearing flow determines the relationship and action. No identifier scheme is specified in the cited source passage. This contextual role is not merged with similarly named roles in other message sets.

CCP clearing flow: [Buy-in](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p250-buy-in-business-transaction.md); diagram [fig-0018](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0018.md). Narrative role; not drawn in this two-endpoint sequence.

Activity responsibilities: [Settlement Management: Buy-In activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p204-settlement-management-buy-in-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0011.md). Narrative-only participants remain distinct from the drawn lanes.
