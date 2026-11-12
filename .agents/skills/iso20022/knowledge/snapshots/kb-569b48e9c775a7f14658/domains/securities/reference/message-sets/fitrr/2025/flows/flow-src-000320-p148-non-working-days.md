---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p148-non-working-days"
title: "Non-working days"
source_locations: [{"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Non-Working Days"], "locator": "/w:document/w:body/w:p[148]", "paragraph_id": "P148", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Non-Working Days"], "locator": "/w:document/w:body/w:p[149]", "paragraph_id": "P149", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Non-Working Days"], "locator": "/w:document/w:body/w:tbl[25]", "paragraph_id": null, "table_id": "T25"}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Non-Working Days", "IF", "RE", "CA", "SA"]
limitations: ["Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.", "Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred."]
manual_curated: true
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0010.md"]
---

# Non-working days

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); Description of BusinessActivities / Reference Data Reporting / Non-Working Days; direct-body paragraph P149; T25.

## Purpose and source conditions

[T15](../documents/src-000320/tables/tbl-0015.md)

| Item | Description |
| --- | --- |
| Definition | A reporting entity is required to submit data to the supervisory authority details on a daily basis except for days when the venue is not open for trading - holidays / weekends. To support knowing which venues are open and which are closed on specific days, all reporting entities must submit details, per venue they operate, on when they will be closed for trading. |
| Trigger | Ad hoc. |
| Pre-conditions | An entity knows what non-working days (including weekends) it plans through the year and submits this to the supervisory authority. |
| Post-conditions | The supervisory authority knows the dates when a specific venue will not be required to submit relevant data. |
| Role | Reporting entity |


## Participants and their responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Capture and submit Non-Working Days | Before the end of the year or where new non-working days have been identified, extract all non-working days for a given period including weekends e.g. until the end of a calendar year, generate and submit the non-working day message to the SA | RE |
| Receive Message (a) | CA not delegating data collection receives the message | CA |
| Process Message | CA not delegating operations to the SA, must check and validate all data that is received<br>CA generates and distributes a status advice message detailing all information that has been identified during the message processing | CA |
| Non-Working Day of the Year | CA captures their non-working days for submission to the SA | CA |
| Submit Message | CA not delegating data collection, submits the message using the same channel as reporting entities | CA |
| Receive Message (b) | SA retrieves the submitted messages from the submission channel | SA |
| Process Message and Generate Status Advice | Process all received non-working days files verifying various information in the file including. Once complete, generate the status advice file for distribution | SA |
| Receive Response | CA checks periodically for the status of the message that they have submitted and downloads the response. As a CA can have made a submission on their Non-Working days, they are checking for messages meant for them as well as messages meant for REs that either need to be processed or routed | CA |
| Route Response | CA delegating data calculation operations, must route the response information to the original RE | CA |
| Receive and Process Response | RE processes the status advice message they have received to know if further actions need to be taken or not | RE |
| Corrective Action (a) | RE must fix any issues that have been identified and if applicable, resubmit the message | RE |
| Process Response | Based on the response of the message submitted, CAs perform any necessary additional data operations that are appropriate | CA |
| Corrective Action (b) | CA fixes any issues that have been found with the message they have submitted | CA |


## Decisions, ordered paths and exceptional outcomes

[Full activity reconstruction and labelled edge table](../diagrams/fitrr-activities/fig-0010.md)

Each table row describes an activity, not a universal linear execution order. Follow the graph for delegation choices, fork/merge paths, accepted outcomes and corrective-action loops.

## Message exchanges and related flows

- [Sequence 20 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0020.md)
- [Sequence 21 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0021.md)
- [Sequence 22 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0022.md)

## Limitations

- Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.
- Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.
