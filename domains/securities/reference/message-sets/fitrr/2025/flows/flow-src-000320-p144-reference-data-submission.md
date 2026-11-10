---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p144-reference-data-submission"
title: "Reference data submission"
source_locations: [{"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Reference Data Submission"], "locator": "/w:document/w:body/w:p[144]", "paragraph_id": "P144", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Reference Data Submission"], "locator": "/w:document/w:body/w:p[145]", "paragraph_id": "P145", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Reference Data Submission"], "locator": "/w:document/w:body/w:tbl[23]", "paragraph_id": null, "table_id": "T23"}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reference Data Submission", "IF", "RE", "CA", "SA"]
limitations: ["Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.", "Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred."]
manual_curated: true
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0008.md"]
---

# Reference data submission

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); Description of BusinessActivities / Reference Data Reporting / Reference Data Submission; direct-body paragraph P145; T23.

## Purpose and source conditions

[T13](../documents/src-000320/tables/tbl-0013.md)

| Item | Description |
| --- | --- |
| Definition | A Reporting Entity (RM, MTF, OTF, SI) which has financial instruments that are admitted to trading that are still valid or for which a request for admission to trading has been made, must submit to its Competent Authority (CA), a list of all these instruments, which shall send it to ESMA. In case of delegation agreement, ESMA collect data directly from TV / SI. |
| Trigger | Data is submitted daily before the cut-off time stated in the Regulatory Technical Standard. |
| Pre-conditions | The reporting entity has financial instruments admitted to trading on a regulated market that are still valid or for a which a request for admission to trading has been made  |
| Post-conditions | The reporting entity has received a status advice message related to the data submitted and / or a reminder file (e.g. in case no file has been submitted by the reporting entity by the cut-off time). |
| Role | Reporting Entity |


## Participants and their responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Capture and Submit Reference Data | Extract local data, create the message and submit it to the appropriate authority based on the agreements that exist between the CA and SA | RE |
| Receive Message (a) | CA not delegating data collection receives the message. Based on the agreement, they either submit the message directly or they perform additional operations on the message | CA |
| Submit Message | CA not delegating data collection, submits the message using the same channel as REs | CA |
| Receive Message (b) | SA retrieves the submitted messages from the submission channel | SA |
| Process Message | CA not delegating operations to the SA, must check and validate all data that is received<br>CA generates and distributes a status advice message detailing all information that has been identified during the message processing | CA |
| Process Message and Generate Status Advice | Each received message is checked for <br>Completeness of message<br>Validity against previously submitted data<br>Once complete, generate the status advice file for distribution | SA |
| Receive Response | CA checks periodically for the status of the message that they have submitted and downloads the response | CA |
| Process Response | CA not delegating operations to the SA, must check that the data they submit has been accepted. Where it has been accepted, all processing of that submission is complete. Where an issue is identified, they must inform the RE of this.  | CA |
| Route Response | CA delegating data calculation operations, must route the response information to the original RE<br>CA not delegating operations may still need to route the response from the SA to the RE in the case where an issue was identified by the SA | CA |
| Receive and Process Response | RE checks for and receives feedback on the message data they submitted. They download and process the status advice message to identify if any further actions need to be taken complete the data submission process | RE |
| Corrective Action | RE must fix any issues that have been identified and if applicable, resubmit the message | RE |


## Decisions, ordered paths and exceptional outcomes

[Full activity reconstruction and labelled edge table](../diagrams/fitrr-activities/fig-0008.md)

Each table row describes an activity, not a universal linear execution order. Follow the graph for delegation choices, fork/merge paths, accepted outcomes and corrective-action loops.

## Message exchanges and related flows

- [Sequence 17 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0017.md)
- [Sequence 18 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0018.md)
- [Sequence 19 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0019.md)

## Limitations

- Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.
- Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.
