---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_sets: ["t2s-intra-balance-movement"]
participant_id: "participant-src-000359-executing-servicing-party"
title: "Executing/Servicing Party"
source_labels: ["Executing/Servicing Party", "Executing / Servicing Party"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000359", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[3]", "paragraph_id": null, "table_id": "T6"}, {"source_id": "src-000359", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[6]/w:tr[10]", "paragraph_id": null, "table_id": "T6"}]
flows: ["flow-src-000359-p158-movement-process", "flow-src-000359-p159-status-advice-process", "flow-src-000359-p160-confirmation-process", "flow-src-000359-p161-modification-process", "flow-src-000359-p162-cancellation-process", "flow-src-000359-p164-modification-cancellation-status-advice-process", "flow-src-000359-p166-movement-reporting-process", "flow-src-000359-p169-modification-cancellation-query-and-report-process", "flow-src-000359-p170-pending-reporting-process", "flow-src-000359-p171-posting-reporting-process"]
process_sections: []
message_ids: []
message_families: ["camt.066", "camt.078", "camt.079", "camt.084", "camt.085"]
search_terms: ["Executing/Servicing Party", "camt.066", "camt.078", "camt.079", "camt.084", "camt.085"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
---

# Executing/Servicing Party

Business context: T2S IntraBalanceMovement. Source classification: business role.

## Definition

Party that processes, monitors and reports on transactions received from an instructing party.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0006.md), source row 3.

Party that processes, monitors and reports on transactions received from the Instructing party.

Evidence: [T6](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0006.md), source row 10.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [System Member](participant-src-000359-system-member.md) | [T7](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0007.md) row 11, column 2 |
| Can play the functional participant role in this source context | [System Transaction Administrator](participant-src-000359-system-transaction-administrator.md) | [T7](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/documents/src-000359/tables/tbl-0007.md) row 11, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Movement Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p158-movement-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Status Advice Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p159-status-advice-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p160-confirmation-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Modification Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p161-modification-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Cancellation Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p162-cancellation-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Modification/Cancellation Status Advice Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p164-modification-cancellation-status-advice-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Movement Reporting Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p166-movement-reporting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Modification/Cancellation Query and Report Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p169-modification-cancellation-query-and-report-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Pending Reporting Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p170-pending-reporting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Posting Reporting Process](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p171-posting-reporting-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `camt.066`, `camt.078`, `camt.079`, `camt.084`, `camt.085`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing/Servicing Party`, `Executing / Servicing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000359](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`.
