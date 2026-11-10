---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_sets: ["ccp-clearing"]
participant_id: "participant-src-000052-central-securities-depository-csd"
title: "Central Securities Depository (CSD)"
source_labels: ["Central Securities Depository (CSD)"]
role_type: "activity participant named in responsibility column"
aliases: []
source_locations: [{"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Settlement Management – Settlement Netting Process"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[3]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Settlement Management – Settlement Netting Process"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[5]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Settlement Management – Settlement Netting Process"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[7]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000052", "heading_path": ["Description of BusinessActivities", "BusinessProcess - Settlement Management – Settlement Netting Process"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[8]", "paragraph_id": null, "table_id": "T16"}]
flows: ["flow-src-000052-p201-business-process-settlement-management-settlement-netting-process", "flow-src-000052-p204-settlement-management-buy-in-process", "flow-src-000052-p247-settlement-netting-business-transaction"]
process_sections: []
message_ids: []
message_families: []
search_terms: ["Central Securities Depository (CSD)"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---







# Central Securities Depository (CSD)

Business context: CCP Clearing. Source classification: activity participant named in responsibility column.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Source activity row 3 | Report the settlement results:<br>The CSD sends the settlement result to the CCP (either the confirmation or pending or failed settlement). | Central Securities Depository (CSD) | [T16](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0016.md) row 3 |
| Source activity row 5 | Report the list of Corporate Events: <br>The CSD sends the list of all corporate events (CEs) that are announced. | Central Securities Depository (CSD) | [T16](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0016.md) row 5 |
| Source activity row 7 | Process the instruction:<br>The CSD processes the settlement instructions.<br> | Central Securities Depository (CSD) | [T16](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0016.md) row 7 |
| Source activity row 8 | Failed Trades:<br>The CSD sends a report with all failed trades and the CCPs will also report these failed trades if the GCM is not part of the settlement chain. | Central Securities Depository (CSD) | [T16](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000052/tables/tbl-0016.md) row 8 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [BusinessProcess - Settlement Management – Settlement Netting Process](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p201-business-process-settlement-management-settlement-netting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Central Securities Depository (CSD)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000052](../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart1_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v2.docx).

CCP clearing flow: [Settlement Netting](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p247-settlement-netting-business-transaction.md); diagram [fig-0017](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/business-transactions/fig-0017.md). Narrative role; not drawn in this two-endpoint sequence.

Activity responsibilities: [Settlement Management: Settlement Netting activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p201-business-process-settlement-management-settlement-netting-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0010.md). Narrative-only participants remain distinct from the drawn lanes.

Activity responsibilities: [Settlement Management: Buy-In activities](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/flows/flow-src-000052-p204-settlement-management-buy-in-process.md); [source diagram](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/diagrams/processes/fig-0011.md). Narrative-only participants remain distinct from the drawn lanes.
