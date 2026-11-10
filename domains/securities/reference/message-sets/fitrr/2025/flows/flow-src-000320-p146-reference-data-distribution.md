---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p146-reference-data-distribution"
title: "Reference data distribution"
source_locations: [{"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Reference Data Distribution"], "locator": "/w:document/w:body/w:p[146]", "paragraph_id": "P146", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Reference Data Distribution"], "locator": "/w:document/w:body/w:p[147]", "paragraph_id": "P147", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Reference Data Reporting", "Reference Data Distribution"], "locator": "/w:document/w:body/w:tbl[24]", "paragraph_id": null, "table_id": "T24"}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Reference Data Distribution", "CA", "SA"]
limitations: ["Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.", "Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.", "The Reporting Entity lane is empty in this activity picture. Narrative P199 and sequence figure23 additionally include Public, Reporting Entity and 3rd Party Systems; this activity diagram intentionally presents only the CA distribution-processing path."]
manual_curated: true
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0009.md"]
---

# Reference data distribution

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); Description of BusinessActivities / Reference Data Reporting / Reference Data Distribution; direct-body paragraph P147; T24.

## Purpose and source conditions

[T14](../documents/src-000320/tables/tbl-0014.md)

| Item | Description |
| --- | --- |
| Definition | A Supervisory Authority receives instruments reference data and shares it with other Business Participants. |
| Trigger | Daily upon reception of data from Entities reporting instruments reference data. |
| Pre-conditions | ESMA has received and generated a complete list of all instruments admitted to trading that are still valid or where a request for admission to trading has been made in the EEA. ESMA has generated all appropriate additional files. |
| Post-conditions | All data has been distributed to CAs for them to integrate within their systems as required. |
| Role | Supervisory Authority |


## Participants and their responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Download 3rd Party Data | Additional quality control data is downloaded from 3rd party reference systems - country code, currency list, Legal Entity Identifier (LEI) code lists | SA |
| Format for Distribution | Using both internal data and 3rd party data, create ISO 20022 messages for the following for distribution: <br>Reference Data (Full, Delta, Invalid, Index Expression of Interest)<br>Country and Currency Data<br>MIC list <br>CFI Data<br>Non-Working Day Data<br>LEI data is also distributed but it is not changed from that downloaded from Global Legal Entity Identifier Foundation (GLEIF) source | SA |
| Distribute | Upload to a known location by a set time e.g. 0800 Central European Time (CET), the distribution bundle that will be downloadable by CAs | SA |
| Receive and Process Message Bundle | Connect to the SA download channel and download the messages that are being distributed. Process the files contained in the bundle and update all necessary systems of the CA accordingly | CA |


## Decisions, ordered paths and exceptional outcomes

[Full activity reconstruction and labelled edge table](../diagrams/fitrr-activities/fig-0009.md)

Each table row describes an activity, not a universal linear execution order. Follow the graph for delegation choices, fork/merge paths, accepted outcomes and corrective-action loops.

## Message exchanges and related flows

- [Sequence 23 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0023.md)

Additional narrative participants: [Public](../../../../../../../shared/reference/participants/participant-src-000320-public.md) and [3rd Party Systems](../../../../../../../shared/reference/participants/participant-src-000320-third-party-systems.md). These roles are absent from this activity swimlane picture but present in P199/figure23.

## Limitations

- Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.
- Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.
- The Reporting Entity lane is empty in this activity picture. Narrative P199 and sequence figure23 additionally include Public, Reporting Entity and 3rd Party Systems; this activity diagram intentionally presents only the CA distribution-processing path.
