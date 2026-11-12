---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p153-mi-fir-specific-additional-reference-data"
title: "MiFIR additional reference / transparency data"
source_locations: [{"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transparency Reporting", "MiFIR specific additional Reference Data"], "locator": "/w:document/w:body/w:p[153]", "paragraph_id": "P153", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transparency Reporting", "MiFIR specific additional Reference Data"], "locator": "/w:document/w:body/w:p[154]", "paragraph_id": "P154", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transparency Reporting", "MiFIR specific additional Reference Data"], "locator": "/w:document/w:body/w:tbl[27]", "paragraph_id": null, "table_id": "T27"}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["MiFIR specific additional Reference Data", "Supervisory Authority", "Reporting Entity", "IF", "RE", "CA", "SA"]
limitations: ["Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.", "Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred."]
manual_curated: true
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0012.md"]
---

# MiFIR additional reference / transparency data

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); Description of BusinessActivities / Transparency Reporting / MiFIR specific additional Reference Data; direct-body paragraph P154; T27.

## Purpose and source conditions

[T16](../documents/src-000320/tables/tbl-0016.md)

| Item | Description |
| --- | --- |
| Definition | To support correct implementation of the transparency regime, specific transparency reference data must be submitted by a Reporting Entity (RM, MTF, OTF, APA, CTP) to ESMA. |
| Trigger | Data is submitted when the financial instrument is first traded or requested to trade has occurred<br>or<br>On a change to the data reported as part of the Transparency Reference Data |
| Pre-conditions | The financial instrument is registered on the reporting entities system. |
| Post-conditions | The reporting entity has submitted appropriate MiFIR specific additional reference data to ESMA. |
| Role | Reporting Entity |


## Participants and their responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Capture and Submit Transparency Data Report Message | Extract local data, create the message and submit it to the appropriate authority based on the agreements that exist between the CA and SA | RE |
| Receive Message (a) | CA not delegating data collection receives the message. Based on the agreement, they either submit the message directly to the SA or they perform additional operations | CA |
| Submit Message | CA not delegating data collection, submits the message to the SA using the same channel as REs | CA |
| Process Message | CA not delegating calculation processing to the SA, must check and validate all data that is received e.g. data checks, data aggregation, error record removal. Depending on the data checks, they submit an appropriate message to the supervisory authority<br>They must generate and distribute a status advice message to the reporting entity | CA |
| Receive Message (b) | SA retrieves the submitted messages from the submission channel | SA |
| Process Message and Generate Status Advice | Each received message is checked for <br>Completeness of message<br>Validity against previously submitted data<br>Once complete, generate the status advice file for distribution | SA |
| Receive Response | CA checks periodically for the status of the message that they have submitted and downloads the response once available | CA |
| Process Response | CA not delegating calculations, must check the response from the SA to identify should the response be routed to the RE or not. If no issues were found, there is no need to inform the RE as they already have received the appropriate status advice. If an issue exists, this must be routed to the RE so that they can take appropriate actions | CA |
| Route Response | CA delegating data calculation operations, must route the response information to the original RE<br>CA not delegating operations may still need to route the response from the SA to the RE in the case where an issue was identified by the SA | CA |
| Receive and Process Response | RE checks for and receives status advice messages which provide details on the records they submitted. They download and process the status advice message to identify if any further actions need to be taken complete the data submission process | RE |
| Corrective Action | Where an issue has been identified in a submitted record, the record must be fixed and the updated records re-submitted | RE |


## Decisions, ordered paths and exceptional outcomes

[Full activity reconstruction and labelled edge table](../diagrams/fitrr-activities/fig-0012.md)

Each table row describes an activity, not a universal linear execution order. Follow the graph for delegation choices, fork/merge paths, accepted outcomes and corrective-action loops.

## Message exchanges and related flows

- [Sequence 26 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0026.md)
- [Sequence 27 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0027.md)
- [Sequence 28 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0028.md)

## Limitations

- Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.
- Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.
