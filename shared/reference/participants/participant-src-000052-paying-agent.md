---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
domains: ["securities"]
source_ids: ["src-000052"]
source_editions: ["March 2026"]
participant_id: "participant-src-000052-paying-agent"
title: "Paying Agent"
source_labels: ["Paying Agent"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000052", "locator": "T16 row6, Clearing Member column"}]
message_sets: ["ccp-clearing"]
message_ids: []
flows: ["flow-src-000052-p201-business-process-settlement-management-settlement-netting-process", "flow-src-000052-p247-settlement-netting-business-transaction"]
search_terms: ["Paying Agent"]
limitations: ["Scoped narrative role; the source does not provide a separate formal participant definition or an identifier scheme. No institution-level equivalence is inferred."]
---





# Paying Agent

## Definition and context

Recipient of the clearing member settlement instruction under the ordinary settlement-information path described in T16. A separate power-of-attorney path assigns instruction submission to the CCP.

Source: [src-000052](../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx); T16 row6, Clearing Member column.

## Responsibilities

- Receives settlement instructions from the clearing member unless the clearing member has signed a power of attorney with the CCP.

## Relationships and identification

The linked CCP clearing flow determines the relationship and action. No identifier scheme is specified in the cited source passage. This contextual role is not merged with similarly named roles in other message sets.

CCP clearing flow: [Settlement Netting](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p247-settlement-netting-business-transaction.md); diagram [fig-0017](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0017.md). Narrative role; not drawn in this two-endpoint sequence.

Activity responsibilities: [Settlement Management: Settlement Netting activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p201-business-process-settlement-management-settlement-netting-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0010.md). Narrative-only participants remain distinct from the drawn lanes.
