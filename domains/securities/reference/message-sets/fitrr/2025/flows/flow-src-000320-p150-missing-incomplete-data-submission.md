---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p150-missing-incomplete-data-submission"
title: "Missing or incomplete data"
source_locations: [{"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Missing / Incomplete Data Submission"], "locator": "/w:document/w:body/w:p[150]", "paragraph_id": "P150", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Missing / Incomplete Data Submission"], "locator": "/w:document/w:body/w:p[151]", "paragraph_id": "P151", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Missing / Incomplete Data Submission"], "locator": "/w:document/w:body/w:tbl[26]", "paragraph_id": null, "table_id": "T26"}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Missing / Incomplete Data Submission", "IF", "RE", "CA", "SA"]
limitations: ["Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.", "Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.", "T26 Receive Message row prints initiator SA, but its description says CA and this activity is in the Competent Authority lane. Both claims are retained (issue-000036)."]
manual_curated: true
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0011.md"]
---

# Missing or incomplete data

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); Description of BusinessActivities / Reference Data Reporting / Missing / Incomplete Data Submission; direct-body paragraph P151; T26.

## Purpose and source conditions

The SA checks for missing venue submissions and incomplete expected data. It generates venue-specific status advice to trigger correction (T26 rows2–3, P202).

## Participants and their responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Check Data Completeness | SA checks all data that it has received to identify if all venues have submitted all the data they are meant to. Issues that can be identified and which result in incomplete data include:<br>No message has been submitted by a specific venue<br>Not all data that should have been submitted has been submitted | SA |
| Create Message | For each venue which meets the criteria of incomplete data, SA creates a status advice message and distribute it to the venue informing them that they have reported incomplete data for the given day and submitted dataset | SA |
| Receive Message | CA not delegating data collection, must accept the status advice message and perform necessary operations based on the delegation agreement that is to be used | SA |
| Route Message | CA delegating data calculation operations, must route the response information to the original RE | CA |
| Process and Generate Message | CA not delegating calculations, receives one or more files which must be processed and the appropriate data extracted which is to be communicated to REs | CA |
| Receive and Process Message | RE which have not reported a full data set as expected at the SA will receive a status advice message capturing which instruments and data has not been submitted. RE shall process the message and perform all necessary corrective action to ensure future submissions are full and complete | RE |


## Decisions, ordered paths and exceptional outcomes

[Full activity reconstruction and labelled edge table](../diagrams/fitrr-activities/fig-0011.md)

Each table row describes an activity, not a universal linear execution order. Follow the graph for delegation choices, fork/merge paths, accepted outcomes and corrective-action loops.

## Message exchanges and related flows

- [Sequence 24 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0024.md)
- [Sequence 25 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0025.md)

## Limitations

- Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.
- Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.
- T26 Receive Message row prints initiator SA, but its description says CA and this activity is in the Competent Authority lane. Both claims are retained (issue-000036).
