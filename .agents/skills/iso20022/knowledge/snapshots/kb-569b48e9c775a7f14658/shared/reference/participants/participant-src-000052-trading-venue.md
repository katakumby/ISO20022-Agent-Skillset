---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
domains: ["securities"]
source_ids: ["src-000052"]
source_editions: ["March 2026"]
participant_id: "participant-src-000052-trading-venue"
title: "Trading Venue"
source_labels: ["Trading Venue"]
role_type: "business role"
aliases: ["Exchange", "Multilateral Trading Facility (MTF)"]
source_locations: [{"source_id": "src-000052", "locator": "P115; T12 rows3-4"}]
message_sets: ["ccp-clearing"]
message_ids: []
flows: ["flow-src-000052-p191-business-process-trade-management", "flow-src-000052-p217-trade-leg-notification-business-transaction", "flow-src-000052-p221-trade-leg-notification-cancellation-business-transaction"]
search_terms: ["Trading Venue", "Exchange", "Multilateral Trading Facility (MTF)"]
limitations: ["Scoped narrative role; the source does not provide a separate formal participant definition or an identifier scheme. No institution-level equivalence is inferred."]
---







# Trading Venue

## Definition and context

The venue that notifies a trade to the CCP and can send a cancellation after an error in specific data. The source explicitly places these notifications/cancellation requests outside the clearing message scope.

Source: [src-000052](../../../evidence/omitted/b45c53bac2be08dee677b607.md); P115; T12 rows3-4.

## Responsibilities

- Notifies trades to the CCP, triggering trade management.
- May request cancellation after an error; source T12 notes arrangements may instead send an opposite trade.

## Relationships and identification

The linked CCP clearing flow determines the relationship and action. No identifier scheme is specified in the cited source passage. This contextual role is not merged with similarly named roles in other message sets.

CCP clearing flow: [Trade Leg Notification](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p217-trade-leg-notification-business-transaction.md); diagram [fig-0012](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0012.md). Narrative role; not drawn in this two-endpoint sequence.

CCP clearing flow: [Trade Leg Notification Cancellation](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p221-trade-leg-notification-cancellation-business-transaction.md); diagram [fig-0013](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0013.md). Narrative role; not drawn in this two-endpoint sequence.

Activity responsibilities: [Trade Management activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p191-business-process-trade-management.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0006.md). Narrative-only participants remain distinct from the drawn lanes.
