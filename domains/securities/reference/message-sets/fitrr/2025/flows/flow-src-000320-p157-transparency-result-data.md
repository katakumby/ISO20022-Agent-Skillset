---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p157-transparency-result-data"
title: "Trading activity results"
source_locations: [{"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transparency Reporting", "Transparency Result Data"], "locator": "/w:document/w:body/w:p[157]", "paragraph_id": "P157", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transparency Reporting", "Transparency Result Data"], "locator": "/w:document/w:body/w:p[158]", "paragraph_id": "P158", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transparency Reporting", "Transparency Result Data"], "locator": "/w:document/w:body/w:tbl[29]", "paragraph_id": null, "table_id": "T29"}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Transparency Result Data", "RE", "CA", "SA"]
limitations: ["Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.", "Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.", "The Reporting Entity lane is empty. T18 Role names SA while this picture, T29 and P233–P235 assign calculation/submission to CA; issue-000032."]
manual_curated: true
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0014.md"]
---

# Trading activity results

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); Description of BusinessActivities / Transparency Reporting / Transparency Result Data; direct-body paragraph P158; T29.

## Purpose and source conditions

[T18](../documents/src-000320/tables/tbl-0018.md)

| Item | Description |
| --- | --- |
| Definition | CAs that have not delegated calculation operations to ESMA must perform and distribute the results of the transparency calculations they perform to ESMA for publication. |
| Trigger | Transparency calculations must be performed by specific cut-off times, defined by MiFIR regulations. At the cut-off, the venue (CA) performs the specified calculations. |
| Pre-conditions | The CA has captured all data it requires to perform the transparency calculation. |
| Post-conditions | The transparency calculation has been performed by the CA with the result data submitted to ESMA for publication along with all other Transparency results. |
| Role | Supervisory Authority |


## Participants and their responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Calculate and Submit Trading Activity Result | CA not delegating Transparency Calculations must perform the transparency calculation on the data for which they are the CA. Results, once known are submitted to the SA | CA |
| Receive Message | SA retrieves the submitted messages from the submission channel | SA |
| Process Message and Generate Status Advice | Process all result data that has been received, including verifying the data is accurate against known bounds. Based on the message process, create and distribute the status advice message to the submitting entity | SA |
| Receive and Process Response | Check periodically for the status of the message that has been submitted. Where a response exists, download and process the message contents | CA |
| Corrective Action | Where an issue has been identified in a submitted record, the record must be fixed and the updated records re-submitted | CA |


## Decisions, ordered paths and exceptional outcomes

[Full activity reconstruction and labelled edge table](../diagrams/fitrr-activities/fig-0014.md)

Each table row describes an activity, not a universal linear execution order. Follow the graph for delegation choices, fork/merge paths, accepted outcomes and corrective-action loops.

## Message exchanges and related flows

- [Sequence 32 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0032.md)

## Limitations

- Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.
- Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.
- The Reporting Entity lane is empty. T18 Role names SA while this picture, T29 and P233–P235 assign calculation/submission to CA; issue-000032.
