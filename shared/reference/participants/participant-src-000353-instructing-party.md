---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000353"]
source_editions: ["may-2025"]
message_sets: ["t2s-collateral-management-reference-data"]
participant_id: "participant-src-000353-instructing-party"
title: "Instructing Party"
source_labels: ["Instructing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000353", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[2]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000353", "heading_path": ["Description of BusinessActivities", "Collateral Management Reference Data", "Collateral Reference Data creation"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[2]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000353", "heading_path": ["Description of BusinessActivities", "Collateral Management Reference Data", "Collateral Reference Data creation"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[6]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000353", "heading_path": ["Description of BusinessActivities", "Collateral Management Reference Data", "Collateral Reference Data deletion"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000353", "heading_path": ["Description of BusinessActivities", "Collateral Management Reference Data", "Collateral Reference Data deletion"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}]
flows: ["flow-src-000353-p104-collateral-reference-data-creation", "flow-src-000353-p105-collateral-reference-data-deletion", "flow-src-000353-p110-collateral-reference-data-creation", "flow-src-000353-p115-collateral-reference-data-deletion", "flow-src-000353-p121-confirmation-scenario", "flow-src-000353-p134-rejection-scenario", "flow-src-000353-p149-confirmation-scenario", "flow-src-000353-p160-rejection-scenario"]
process_sections: ["flow-src-000353-p121-confirmation-scenario", "flow-src-000353-p126-collateral-management-reference-data-creation-request", "flow-src-000353-p134-rejection-scenario", "flow-src-000353-p139-collateral-management-reference-data-creation-request", "flow-src-000353-p149-confirmation-scenario", "flow-src-000353-p154-collateral-management-reference-data-deletion-request", "flow-src-000353-p160-rejection-scenario", "flow-src-000353-p165-collateral-management-reference-data-deletion-request"]
message_ids: ["reda.024.001.01", "reda.025.001.01", "reda.026.001.01", "reda.027.001.01", "reda.028.001.01", "reda.044.001.01", "reda.075.001.01", "reda.077.001.01"]
message_families: ["reda.024", "reda.025", "reda.026", "reda.027", "reda.028", "reda.044", "reda.075", "reda.077"]
search_terms: ["Instructing Party", "reda.024", "reda.025", "reda.026", "reda.027", "reda.028", "reda.044", "reda.075", "reda.077"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---















# Instructing Party

Business context: T2S CollateralManagementReferenceData. Source classification: functional participant role.

## Definition

Party that instructs the executing/servicing party to process and monitor a transaction.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0005.md), source row 2.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Instruction | Instruct the Executing/Servicing Party to create: <br>• a Security Valuation<br>• an Auto-Collateralisation Eligibility Link<br>• a Close Link<br>• an Eligible Counterpart CSD | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0011.md) row 2 |
| Monitor process | Instructing Party monitors the status of the instruction. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0011.md) row 6 |
| Instruction | Instruct the Executing/Servicing Party to delete: <br>• an Auto-Collateralisation Eligibility Link<br>• a Close Link | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0012.md) row 2 |
| Monitor process | Instructing Party monitors the status of the instruction. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/documents/src-000353/tables/tbl-0012.md) row 6 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Collateral Reference Data creation](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p104-collateral-reference-data-creation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Collateral Reference Data deletion](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p105-collateral-reference-data-deletion.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Collateral Reference Data creation](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p110-collateral-reference-data-creation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Collateral Reference Data deletion](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p115-collateral-reference-data-deletion.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p121-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Collateral Management Reference Data Creation Request](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p126-collateral-management-reference-data-creation-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p134-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Collateral Management Reference Data Creation Request](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p139-collateral-management-reference-data-creation-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p149-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Collateral Management Reference Data Deletion Request](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p154-collateral-management-reference-data-deletion-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p160-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Collateral Management Reference Data Deletion Request](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p165-collateral-management-reference-data-deletion-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.024`, `reda.025`, `reda.026`, `reda.027`, `reda.028`, `reda.044`, `reda.075`, `reda.077`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Instructing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000353](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_CollateralManagementReferenceData_v2.docx`.

Collateral-reference source context: [Collateral-reference business-role context](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0001.md). .

Collateral-reference source context: [Collateral-reference maintenance overview](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0002.md). [flow Collateral Reference Data creation](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p104-collateral-reference-data-creation.md), [flow Collateral Reference Data deletion](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p105-collateral-reference-data-deletion.md).

Collateral-reference source context: [Collateral-reference creation/deletion activity reused](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0007.md). [flow Collateral Reference Data creation](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p110-collateral-reference-data-creation.md), [flow Collateral Reference Data deletion](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p115-collateral-reference-data-deletion.md).

Collateral-reference source context: [Collateral-reference creation completed](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0009.md). [flow Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p121-confirmation-scenario.md).

Collateral-reference source context: [Collateral-reference creation rejected](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0010.md). [flow Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p134-rejection-scenario.md).

Collateral-reference source context: [Collateral-reference deletion completed](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0011.md). [flow Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p149-confirmation-scenario.md).

Collateral-reference source context: [Collateral-reference deletion rejected](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/diagrams/curated/fig-0012.md). [flow Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/flows/flow-src-000353-p160-rejection-scenario.md).
