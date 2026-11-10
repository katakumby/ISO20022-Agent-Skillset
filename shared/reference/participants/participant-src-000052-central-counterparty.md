---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
participant_id: "participant-src-000052-central-counterparty"
title: "Central Counterparty"
source_labels: ["Central Counterparty\n"]
role_type: "functional participant role"
aliases: ["CCP", "Central Counterparty (CCP)"]
source_locations: [{"source_id": "src-000052", "heading_path": ["BusinessRoles and Participants"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[5]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000052", "locator": "P216; T12 header; T10 row5"}]
flows: ["flow-src-000052-p191-business-process-trade-management", "flow-src-000052-p194-business-process-risk-management-netting-process", "flow-src-000052-p196-business-process-risk-management-margining-process", "flow-src-000052-p198-business-process-risk-management-default-fund-contribution-process", "flow-src-000052-p201-business-process-settlement-management-settlement-netting-process", "flow-src-000052-p204-settlement-management-buy-in-process", "flow-src-000052-p217-trade-leg-notification-business-transaction", "flow-src-000052-p221-trade-leg-notification-cancellation-business-transaction", "flow-src-000052-p225-position-netting-business-transaction", "flow-src-000052-p229-margining-business-transaction", "flow-src-000052-p240-default-fund-contribution-business-transaction", "flow-src-000052-p247-settlement-netting-business-transaction", "flow-src-000052-p250-buy-in-business-transaction"]
process_sections: ["flow-src-000052-p250-buy-in-business-transaction"]
message_ids: []
message_families: []
search_terms: ["Central Counterparty"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---





























# Central Counterparty

Business context: CCP Clearing. Source classification: functional participant role.

## Definition

An entity that interposes itself between the counterparties to the contracts traded in one or more financial markets, on one or more trading venues, becoming the buyer to every seller and the seller to every buyer.

Evidence: [T10](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0010.md), source row 5.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [CCP](participant-src-000052-ccp.md) | [T11](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0011.md) row 6, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [BusinessProcess - Settlement Management – Settlement Netting Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p201-business-process-settlement-management-settlement-netting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Buy-in BusinessTransaction](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p250-buy-in-business-transaction.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Central Counterparty`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000052](../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx).

## Source-supported labels

CCP, Central Counterparty (CCP) refer to this functional role within the cited CCP clearing context (P216; T12 header; T10 row5). The business role CCP in T10 and its T11 relationship remain separately recorded.

CCP clearing flow: [Trade Leg Notification](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p217-trade-leg-notification-business-transaction.md); diagram [fig-0012](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0012.md). Message endpoint shown in source sequence.

CCP clearing flow: [Trade Leg Notification Cancellation](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p221-trade-leg-notification-cancellation-business-transaction.md); diagram [fig-0013](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0013.md). Message endpoint shown in source sequence.

CCP clearing flow: [Position Netting](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p225-position-netting-business-transaction.md); diagram [fig-0014](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0014.md). Message endpoint shown in source sequence.

CCP clearing flow: [Margining](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p229-margining-business-transaction.md); diagram [fig-0015](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0015.md). Message endpoint shown in source sequence.

CCP clearing flow: [Default Fund Contribution](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p240-default-fund-contribution-business-transaction.md); diagram [fig-0016](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0016.md). Message endpoint shown in source sequence.

CCP clearing flow: [Settlement Netting](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p247-settlement-netting-business-transaction.md); diagram [fig-0017](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0017.md). Message endpoint shown in source sequence.

CCP clearing flow: [Buy-in](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p250-buy-in-business-transaction.md); diagram [fig-0018](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0018.md). Message endpoint shown in source sequence.

Activity responsibilities: [Trade Management activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p191-business-process-trade-management.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0006.md). Narrative-only participants remain distinct from the drawn lanes.

Activity responsibilities: [Risk Management: Netting activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p194-business-process-risk-management-netting-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0007.md). Narrative-only participants remain distinct from the drawn lanes.

Activity responsibilities: [Risk Management: Margining activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p196-business-process-risk-management-margining-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0008.md). Narrative-only participants remain distinct from the drawn lanes.

Activity responsibilities: [Risk Management: Default Fund Contribution activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p198-business-process-risk-management-default-fund-contribution-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0009.md). Narrative-only participants remain distinct from the drawn lanes.

Activity responsibilities: [Settlement Management: Settlement Netting activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p201-business-process-settlement-management-settlement-netting-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0010.md). Narrative-only participants remain distinct from the drawn lanes.

Activity responsibilities: [Settlement Management: Buy-In activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p204-settlement-management-buy-in-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0011.md). Narrative-only participants remain distinct from the drawn lanes.
