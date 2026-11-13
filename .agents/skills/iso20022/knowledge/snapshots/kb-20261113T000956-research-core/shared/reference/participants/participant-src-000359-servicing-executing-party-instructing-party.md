---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
participant_id: "participant-src-000359-servicing-executing-party-instructing-party"
title: "Servicing/Executing Party Instructing Party"
source_labels: ["Servicing/Executing Party Instructing Party"]
role_type: "activity participant; classification not established"
aliases: []
source_locations: [{"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Modification/Cancellation Query/Report Process", "Push Mode"], "locator": "/w:document/w:body/w:tbl[23]/w:tr[2]", "paragraph_id": null, "table_id": "T23"}, {"source_id": "src-000359", "heading_path": ["Description of BusinessActivities", "Intra-Balance Movement Pending/Posting Report Process"], "locator": "/w:document/w:body/w:tbl[25]/w:tr[2]", "paragraph_id": null, "table_id": "T25"}]
flows: ["flow-src-000359-p200-push-mode", "flow-src-000359-p208-intra-balance-movement-pending-posting-report-process", "flow-src-000359-p211-intra-balance-movement-query-response-process"]
process_sections: ["flow-src-000359-p219-in-external-scenario", "flow-src-000359-p238-modification-and-cancellation-process", "flow-src-000359-p298-intra-balance-movement-pending-posting-report-process", "flow-src-000359-p310-intra-balance-movement-query-response-process"]
message_ids: []
message_families: ["camt.066", "camt.067", "camt.068", "camt.072", "camt.073", "camt.074", "camt.075", "camt.078", "camt.079", "camt.084", "camt.085"]
search_terms: ["Servicing/Executing Party Instructing Party", "camt.066", "camt.067", "camt.068", "camt.072", "camt.073", "camt.074", "camt.075", "camt.078", "camt.079", "camt.084", "camt.085"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Servicing/Executing Party Instructing Party

Business context: T2S IntraBalanceMovement. Source classification: activity participant; classification not established.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| System Event Triggered | External process resulting in need for liquidity movements reporting. | Initiator | [T23](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0023.md) row 2 |
| System Event Triggered | External process resulting in need for liquidity movements reporting. | Initiator | [T25](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0025.md) row 2 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Push Mode](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p200-push-mode.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intra-Balance Movement Pending/Posting Report Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p208-intra-balance-movement-pending-posting-report-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intra-Balance Movement Query/Response Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p211-intra-balance-movement-query-response-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [In external scenario](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p219-in-external-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Modification and Cancellation Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p238-modification-and-cancellation-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intra-Balance Movement Pending/Posting Report Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p298-intra-balance-movement-pending-posting-report-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Intra-Balance Movement Query/Response Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p310-intra-balance-movement-query-response-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `camt.066`, `camt.067`, `camt.068`, `camt.072`, `camt.073`, `camt.074`, `camt.075`, `camt.078`, `camt.079`, `camt.084`, `camt.085`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Servicing/Executing Party Instructing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000359](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`.
