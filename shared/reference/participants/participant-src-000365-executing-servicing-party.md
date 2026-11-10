---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000365", "src-000366"]
source_editions: ["december-2024"]
message_sets: ["t2s-link-reference-data"]
participant_id: "participant-src-000365-executing-servicing-party"
title: "Executing / Servicing Party"
source_labels: ["Executing / Servicing Party", "Executing/Servicing Party", "executing/ servicing party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000365", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Creation Process"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[3]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Creation Process"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[4]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Creation Process"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[5]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[3]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[4]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000365", "heading_path": ["Description of BusinessActivities", "Link Reference Data", "Link Modification Process"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[5]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000366", "heading": "6 reda.050.001.01 AccountLinkMaintenanceRequestV01", "file_pages": [41], "evidence_id": "src-000366-reda.050.001.01-p41-c001"}]
flows: ["flow-src-000365-p120-link-creation-process", "flow-src-000365-p122-link-modification-process", "flow-src-000365-p128-link-creation-process", "flow-src-000365-p132-link-modification-process", "flow-src-000365-p139-confirmation-scenario", "flow-src-000365-p153-rejection-scenario", "flow-src-000365-p177-confirmation-scenario", "flow-src-000365-p197-rejection-scenario"]
process_sections: ["flow-src-000365-p139-confirmation-scenario", "flow-src-000365-p145-the-instructing-party-sends-the-instruction-to-the-executing-servicing", "flow-src-000365-p153-rejection-scenario", "flow-src-000365-p158-reference-data-link-creation-request", "flow-src-000365-p177-confirmation-scenario", "flow-src-000365-p190-reference-data-link-maintenance-request", "flow-src-000365-p192-reference-data-link-status-advice", "flow-src-000365-p197-rejection-scenario", "flow-src-000365-p212-reference-data-link-maintenance-request", "flow-src-000365-p214-reference-data-link-status-advice"]
message_ids: ["reda.045.001.01", "reda.046.001.01", "reda.047.001.01", "reda.049.001.01", "reda.050.001.01", "reda.051.001.01"]
message_families: ["reda.045", "reda.046", "reda.047", "reda.049", "reda.050", "reda.051"]
search_terms: ["Executing / Servicing Party", "reda.046", "reda.047", "reda.050", "reda.051"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---

























# Executing / Servicing Party

Business context: T2S LinkReferenceData. Source classification: functional participant role.

## Definition

Party that processes, monitors and reports on transactions received from the Instructing party.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0005.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Validate | Executing/Servicing Party system checks if this instruction is a new occurrence or not. <br>It also checks if this instruction is already handled or not.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the creation of the link, the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after a specific event. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0011.md) row 3 |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0011.md) row 4 |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Initiator | [T11](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0011.md) row 5 |
| Validate: | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the data can or cannot be updated.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the update of the link, the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after a specific event. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0012.md) row 3 |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0012.md) row 4 |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Initiator | [T12](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0012.md) row 5 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [CSD](participant-src-000365-csd.md) | [T7](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0007.md) row 5, column 3 |
| Business role listed for this functional participant | [Market Data Provider](participant-src-000365-market-data-provider.md) | [T7](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0007.md) row 6, column 3 |
| Business role listed for this functional participant | [Market Infrastructure](participant-src-000365-market-infrastructure.md) | [T7](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/documents/src-000365/tables/tbl-0007.md) row 7, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Link Creation Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p120-link-creation-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Link Modification Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p122-link-modification-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Link Creation Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p128-link-creation-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Link Modification Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p132-link-modification-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p139-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [The Instructing Party sends the instruction to the Executing/Servicing Party to create a new Reference Data Link. This instruction contains information that clearly identify the Reference Data Link.](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p145-the-instructing-party-sends-the-instruction-to-the-executing-servicing.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p153-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reference Data Link Creation Request:](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p158-reference-data-link-creation-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p177-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reference Data Link Maintenance Request](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p190-reference-data-link-maintenance-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reference Data Link Status Advice](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p192-reference-data-link-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p197-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reference Data Link Maintenance Request](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p212-reference-data-link-maintenance-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Reference Data Link Status Advice](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p214-reference-data-link-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.046`, `reda.047`, `reda.050`, `reda.051`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing / Servicing Party`, `Executing/Servicing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000365](../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`.

Link-reference source context: [Link reference-data role mappings](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0001.md). .

Link-reference source context: [Link creation and modification overview](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0002.md). [flow Link Creation Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p120-link-creation-process.md), [flow Link Modification Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p122-link-modification-process.md).

Link-reference source context: [Link creation activity with validation and retry](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0007.md). [flow Link Creation Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p120-link-creation-process.md).

Link-reference source context: [Link modification activity with validation and retry](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0007.md). [flow Link Modification Process](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p122-link-modification-process.md).

Link-reference source context: [Link creation confirmation sequence](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0009.md). [flow Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p139-confirmation-scenario.md).

Link-reference source context: [Link creation rejection sequence](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0010.md). [flow Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p153-rejection-scenario.md).

Link-reference source context: [Link modification confirmation sequence — source role-label conflict](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0011.md). [flow Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p177-confirmation-scenario.md).

Link-reference source context: [Link modification rejection sequence — source role-label conflict](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/diagrams/curated/fig-0012.md). [flow Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/flows/flow-src-000365-p197-rejection-scenario.md).




<!-- FUNCTIONALITY-ALIASES-src-000366 -->
## Additional literal publication labels

The source uses a spacing variant of Executing/Servicing Party in AccountLinkMaintenanceRequest.

| Source label | Source context |
| --- | --- |
| executing/ servicing party | src-000366-reda.050.001.01-p41-c001 |


> The AccountLinkMaintenanceRequest message is sent by the instructing party to the executing/ servicing party to request for the maintenance of an account link in their system.

src-000366, file pages41; 6 reda.050.001.01 AccountLinkMaintenanceRequestV01.

<!-- /FUNCTIONALITY-ALIASES-src-000366 -->
