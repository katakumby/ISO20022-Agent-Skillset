---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
participant_id: "participant-src-000359-third-party"
title: "Third Party"
source_labels: ["Third Party"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Process", "Internal Scenario"], "locator": "/w:document/w:body/w:tbl[21]/w:tr[8]", "paragraph_id": null, "table_id": "T21"}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Process", "Internal Scenario"], "locator": "/w:document/w:body/w:tbl[21]/w:tr[9]", "paragraph_id": null, "table_id": "T21"}]
flows: ["flow-src-000359-p189-external-scenario", "flow-src-000359-p193-internal-scenario"]
process_sections: ["flow-src-000359-p230-in-internal-scenario"]
message_ids: []
message_families: ["camt.067", "camt.068"]
search_terms: ["Third Party", "camt.067", "camt.068"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000359-p193-internal-scenario", "flow-src-000359-p230-in-internal-scenario"]
---





# Third Party

Business context: T2S IntraBalanceMovement. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Monitor | Check for incoming communications associated with original instruction.<br> | Initiator | [T21](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0021.md) row 8 |
| Reconcile | External process reconciling impact of current status of original instruction. | Initiator | [T21](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0021.md) row 9 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [External Scenario](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p189-external-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Internal Scenario](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p193-internal-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [In internal scenario](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p230-in-internal-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `camt.067`, `camt.068`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Third Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000359](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`.

<!-- INTRABALANCE-FIG-11-START -->
[Internal intra-balance movement activity](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p193-internal-scenario.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0011.md)
<!-- INTRABALANCE-FIG-11-END -->

<!-- INTRABALANCE-FIG-18-START -->
[Internal cash settlement restriction creation](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p230-in-internal-scenario.md) · [Source diagram and directions](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/diagrams/intrabalance/fig-0018.md)
<!-- INTRABALANCE-FIG-18-END -->
