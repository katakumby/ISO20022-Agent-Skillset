---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_sets: ["t2s-securities-reference-data"]
participant_id: "participant-src-000377-executing-servicing-party"
title: "Executing/Servicing Party"
source_labels: ["Executing/Servicing Party"]
role_type: "functional participant role"
aliases: []
source_locations: [{"source_id": "src-000377", "heading_path": ["BusinessRoles and Participants", "Participants and BusinessRoles Definitions"], "locator": "/w:document/w:body/w:tbl[5]/w:tr[3]", "paragraph_id": null, "table_id": "T5"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Creation Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[3]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Creation Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[4]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Creation Process"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[5]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Modification Process"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[3]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Modification Process"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[4]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Modification Process"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[5]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Deletion Process"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[3]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Deletion Process"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[4]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Deletion Process"], "locator": "/w:document/w:body/w:tbl[16]/w:tr[5]", "paragraph_id": null, "table_id": "T16"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Query/Query Response Process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[3]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Query/Query Response Process"], "locator": "/w:document/w:body/w:tbl[17]/w:tr[4]", "paragraph_id": null, "table_id": "T17"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Statement Process"], "locator": "/w:document/w:body/w:tbl[18]/w:tr[3]", "paragraph_id": null, "table_id": "T18"}, {"source_id": "src-000377", "heading_path": ["Description of BusinessActivities", "Statement Process"], "locator": "/w:document/w:body/w:tbl[18]/w:tr[4]", "paragraph_id": null, "table_id": "T18"}]
flows: ["flow-src-000377-p146-create-security", "flow-src-000377-p147-modify-security", "flow-src-000377-p148-delete-security", "flow-src-000377-p149-query", "flow-src-000377-p150-general-statement", "flow-src-000377-p154-creation-process", "flow-src-000377-p156-modification-process", "flow-src-000377-p159-deletion-process", "flow-src-000377-p162-query-query-response-process", "flow-src-000377-p165-statement-process"]
process_sections: ["flow-src-000377-p172-confirmation-scenario", "flow-src-000377-p176-security-creation-request", "flow-src-000377-p178-security-creation-status-advice", "flow-src-000377-p180-queued", "flow-src-000377-p182-completed", "flow-src-000377-p185-rejection-scenario", "flow-src-000377-p189-security-creation-request", "flow-src-000377-p191-security-creation-status-advice", "flow-src-000377-p199-queued", "flow-src-000377-p211-confirmation-scenario", "flow-src-000377-p215-security-maintenance-request", "flow-src-000377-p218-security-maintenance-status-advice", "flow-src-000377-p220-queued", "flow-src-000377-p222-completed", "flow-src-000377-p231-rejection-scenario", "flow-src-000377-p235-security-maintenance-request", "flow-src-000377-p237-security-maintenance-status-advice", "flow-src-000377-p245-queued", "flow-src-000377-p254-confirmation-scenario", "flow-src-000377-p258-security-deletion-request", "flow-src-000377-p260-security-deletion-status-advice", "flow-src-000377-p262-queued", "flow-src-000377-p264-completed", "flow-src-000377-p270-rejection-scenario", "flow-src-000377-p274-security-deletion-request", "flow-src-000377-p276-security-status-advice", "flow-src-000377-p284-queued", "flow-src-000377-p297-security-query", "flow-src-000377-p301-security-report", "flow-src-000377-p305-securities-audit-trail-query", "flow-src-000377-p309-securities-audit-trail-report", "flow-src-000377-p314-security-activity-advice"]
message_ids: []
message_families: ["reda.006", "reda.007", "reda.008", "reda.009", "reda.010", "reda.012", "reda.013", "reda.029", "reda.030", "reda.033", "reda.034"]
search_terms: ["Executing/Servicing Party", "reda.006", "reda.007", "reda.008", "reda.009", "reda.010", "reda.012", "reda.013", "reda.029", "reda.030", "reda.033", "reda.034"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
flow_ids: ["flow-src-000377-p143-business-process-description", "flow-src-000377-p154-creation-process", "flow-src-000377-p156-modification-process", "flow-src-000377-p159-deletion-process", "flow-src-000377-p162-query-query-response-process", "flow-src-000377-p165-statement-process", "flow-src-000377-p172-confirmation-scenario", "flow-src-000377-p185-rejection-scenario", "flow-src-000377-p211-confirmation-scenario", "flow-src-000377-p231-rejection-scenario", "flow-src-000377-p254-confirmation-scenario", "flow-src-000377-p270-rejection-scenario", "flow-src-000377-p294-security-query-security-report-scenario", "flow-src-000377-p303-securities-audit-trail-query-and-report-scenario", "flow-src-000377-p312-statement-process"]
---



























































































# Executing/Servicing Party

Business context: T2S SecuritiesReferenceData. Source classification: functional participant role.

## Definition

Party that processes, monitors and reports on transactions received from the Instructing party.

Evidence: [T5](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0005.md), source row 3.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Validate | Executing/Servicing Party system checks if this instruction is a new occurrence or not. <br>It also checks if this instruction is already handled or not.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the creation of the security (e.g. not during a night – time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Initiator | [T14](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0014.md) row 3 |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Initiator | [T14](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0014.md) row 4 |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Initiator | [T14](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0014.md) row 5 |
| Validate | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the data can or cannot be updated.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the update of the security (e.g. not during a night – time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Initiator | [T15](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0015.md) row 3 |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Initiator | [T15](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0015.md) row 4 |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Initiator | [T15](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0015.md) row 5 |
| Validate | Executing/Servicing Party checks if the instruction already exists in the system.<br>It checks also if the security can or cannot be deleted.<br>If validation of the message fails, a status message “REJECTED” will be sent including the related errors and reason information.<br>If the message is valid and the time permits the deletion of the security (e.g. not during a night – time sequence), the data will be processed and a status message “COMPLETED” will be sent.<br>Otherwise a status message “QUEUED” will be sent and the instruction will be resubmit to validation after e.g. a night –time cycle. | Initiator | [T16](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0016.md) row 3 |
| Process | If the instruction is accepted, the Executing/Servicing Party processes the instruction and informs the Instructing Party of the completeness of this instruction. | Initiator | [T16](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0016.md) row 4 |
| Report | Executing/Servicing Party informs the Instructing Party that this instruction is rejected and why. | Initiator | [T16](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0016.md) row 5 |
| Process query | Executing/Servicing Party processes the request.<br>In case the processing of the query takes too much time or cannot give any positive response, the Executing/Servicing Party sends an error message back to the Instructing Party with the error code and the related explanation. | Initiator | [T17](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0017.md) row 3 |
| Response | Executing/Services Party sends the response to the Instructing Party according to query results. | Initiator | [T17](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0017.md) row 4 |
| Process statement | Executing/Servicing Party processes the statement. | Initiator | [T18](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0018.md) row 3 |
| Response | Executing/Servicing Party sends the statement to the Instructing Party. | Initiator | [T18](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0018.md) row 4 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Business role listed for this functional participant | [Market Infrastructure](participant-src-000377-market-infrastructure.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0007.md) row 4, column 3 |
| Business role listed for this functional participant | [Market Data Provider](participant-src-000377-market-data-provider.md) | [T7](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/documents/src-000377/tables/tbl-0007.md) row 5, column 3 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Create Security](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p146-create-security.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Modify Security](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p147-modify-security.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Delete Security](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p148-delete-security.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Query](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p149-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [General Statement](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p150-general-statement.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Creation Process](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p154-creation-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Modification Process](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p156-modification-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Deletion Process](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p159-deletion-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Query/Query Response Process](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p162-query-query-response-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Statement Process](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p165-statement-process.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p172-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Creation Request](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p176-security-creation-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Creation Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p178-security-creation-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Queued](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p180-queued.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Completed](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p182-completed.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p185-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Creation Request](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p189-security-creation-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Creation Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p191-security-creation-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Queued](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p199-queued.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p211-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Maintenance Request](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p215-security-maintenance-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Maintenance Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p218-security-maintenance-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Queued](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p220-queued.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Completed](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p222-completed.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p231-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Maintenance Request](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p235-security-maintenance-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Maintenance Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p237-security-maintenance-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Queued](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p245-queued.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Confirmation Scenario](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p254-confirmation-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Deletion Request](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p258-security-deletion-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Deletion Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p260-security-deletion-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Queued](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p262-queued.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Completed](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p264-completed.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Rejection Scenario](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p270-rejection-scenario.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Deletion Request](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p274-security-deletion-request.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Status Advice](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p276-security-status-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Queued](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p284-queued.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Query](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p297-security-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Report](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p301-security-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Audit Trail Query](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p305-securities-audit-trail-query.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Securities Audit Trail Report](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p309-securities-audit-trail-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Security Activity Advice](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p314-security-activity-advice.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: `reda.006`, `reda.007`, `reda.008`, `reda.009`, `reda.010`, `reda.012`, `reda.013`, `reda.029`, `reda.030`, `reda.033`, `reda.034`. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Executing/Servicing Party`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000377](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`.































<!-- SECREF-FIG-2-START -->
[Securities reference-data high-level processes](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p143-business-process-description.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0002.md)
<!-- SECREF-FIG-2-END -->

<!-- SECREF-FIG-7-START -->
[Security creation activity](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p154-creation-process.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0007.md)
<!-- SECREF-FIG-7-END -->

<!-- SECREF-FIG-8-START -->
[Security modification activity](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p156-modification-process.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0008.md)
<!-- SECREF-FIG-8-END -->

<!-- SECREF-FIG-9-START -->
[Security deletion activity](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p159-deletion-process.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0009.md)
<!-- SECREF-FIG-9-END -->

<!-- SECREF-FIG-10-START -->
[Security query and audit-trail query activity](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p162-query-query-response-process.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0010.md)
<!-- SECREF-FIG-10-END -->

<!-- SECREF-FIG-11-START -->
[Security activity statement production](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p165-statement-process.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0011.md)
<!-- SECREF-FIG-11-END -->

<!-- SECREF-FIG-12-START -->
[Security creation — confirmation](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p172-confirmation-scenario.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0012.md)
<!-- SECREF-FIG-12-END -->

<!-- SECREF-FIG-13-START -->
[Security creation — rejection](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p185-rejection-scenario.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0013.md)
<!-- SECREF-FIG-13-END -->

<!-- SECREF-FIG-14-START -->
[Security maintenance — confirmation](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p211-confirmation-scenario.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0014.md)
<!-- SECREF-FIG-14-END -->

<!-- SECREF-FIG-15-START -->
[Security maintenance — rejection](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p231-rejection-scenario.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0015.md)
<!-- SECREF-FIG-15-END -->

<!-- SECREF-FIG-16-START -->
[Security deletion — confirmation](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p254-confirmation-scenario.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0016.md)
<!-- SECREF-FIG-16-END -->

<!-- SECREF-FIG-17-START -->
[Security deletion — rejection](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p270-rejection-scenario.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0017.md)
<!-- SECREF-FIG-17-END -->

<!-- SECREF-FIG-18-START -->
[Security query and report exchange](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p294-security-query-security-report-scenario.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0018.md)
<!-- SECREF-FIG-18-END -->

<!-- SECREF-FIG-19-START -->
[Securities audit-trail query and report exchange](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p303-securities-audit-trail-query-and-report-scenario.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0019.md)
<!-- SECREF-FIG-19-END -->

<!-- SECREF-FIG-20-START -->
[Unsolicited security activity advice](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/flows/flow-src-000377-p312-statement-process.md) · [Literal diagram roles and directions](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/diagrams/securities-reference/fig-0020.md)
<!-- SECREF-FIG-20-END -->
