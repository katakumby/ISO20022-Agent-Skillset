---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p159-trading-volume-cap"
title: "Trading volume cap"
source_locations: [{"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Trading Volume Cap"], "locator": "/w:document/w:body/w:p[159]", "paragraph_id": "P159", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Trading Volume Cap"], "locator": "/w:document/w:body/w:p[160]", "paragraph_id": "P160", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Trading Volume Cap"], "locator": "/w:document/w:body/w:tbl[30]", "paragraph_id": null, "table_id": "T30"}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
message_mapping_evidence: []
message_ids: []
message_families: []
search_terms: ["Trading Volume Cap", "Reporting Entity", "IF", "RE", "CA", "SA"]
limitations: ["Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.", "Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred."]
manual_curated: true
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-reporting-entity", "participant-src-000320-supervisory-authority"]
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0015.md"]
---

# Trading volume cap

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); Description of BusinessActivities / Trading Volume Cap; direct-body paragraph P160; T30.

## Purpose and source conditions

[T19](../documents/src-000320/tables/tbl-0019.md)

| Item | Description |
| --- | --- |
| Definition | For all Equity / Equity-like instruments that are traded in the EEA, Reporting Entities (RM, MTF, CTP) are to report volumes of trade per currency that they have undertaken on each instrument over the preceding period (01-15 or 16-31 of each month). The report captures total volume of trades as well as volumes of trades that have been undertaken under Negotiated Transactions and Reference Price waivers. |
| Trigger | The Reporting Entity submits data twice per month, typically on the 1st and 16th of each month. |
| Pre-conditions | The Equity / Equity like financial instruments have been previously submitted through the reference data and transparency additional reference data messages. |
| Post-conditions | The double volume cap calculations are performed taking into account a years' worth of data to establish the percentage of trades that are being performed under either Reference Price or Negotiated Transactions waiver. |
| Role | Reporting entity |


## Participants and their responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Supervisory Authority](../../../../../../../shared/reference/participants/participant-src-000320-supervisory-authority.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Capture and Submit Trading Volume Cap Message | Extract equity / equity like trading data, create the message and submit it to the appropriate authority based on the agreements that exist between the CA and SA | RE |
| Receive Message (a) | CA not delegating data collection receives the message. Based on the agreement, they either submit the message directly to the SA or they perform additional operations | CA |
| Submit Message | CA not delegating data collection, submits the message to the SA using the same channel as REs | CA |
| Process Message | CA not delegating calculation processing to the SA, must check and validate all data that is received e.g. data checks, data aggregation, error record removal. Depending on the data checks, they submit an appropriate message to the SA<br>They must generate and distribute a status advice message to the RE | CA |
| Receive Message (b) | SA retrieves the submitted messages from the submission channel | SA |
| Process Message and Generate Status Advice | Each received message is checked for <br>Completeness of message<br>Validity against previously submitted data<br>Once complete, generate the status advice file for distribution | SA |
| Receive Response | CAs check periodically for the status of the message that they have submitted and download the response once available | CA |
| Process Response | CA not delegating calculations, must check the response from the SA to identify should the response be routed to the RE or not. If no issues were found, there is no need to inform the reporting entity as they already have received the appropriate status advice. If an issue exists, this must be routed to the RE so that they can take appropriate actions | CA |
| Route Response | CA delegating data calculation operations, must route the response information to the original RE<br>CA not delegating operations may still need to route the response from the SA to the RE in the case where an issue was identified by the SA | CA |
| Receive and Process Response | RE checks for and receives status advice messages which provide details on the records they submitted. They download and process the status advice message to identify if any further actions need to be taken complete the data submission process | RE |
| Corrective Action | Where an issue has been identified in a submitted record, the record must be fixed and the updated records re-submitted | RE |


## Decisions, ordered paths and exceptional outcomes

[Full activity reconstruction and labelled edge table](../diagrams/fitrr-activities/fig-0015.md)

Each table row describes an activity, not a universal linear execution order. Follow the graph for delegation choices, fork/merge paths, accepted outcomes and corrective-action loops.

## Message exchanges and related flows

- [Sequence 33 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0033.md)
- [Sequence 34 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0034.md)
- [Sequence 35 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0035.md)

## Limitations

- Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.
- Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.
