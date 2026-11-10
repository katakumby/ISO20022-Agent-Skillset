---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
flow_id: "flow-src-000320-p162-financial-instrument-transaction-report"
title: "Transaction reporting and authority exchange"
source_locations: [{"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[162]", "paragraph_id": "P162", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[163]", "paragraph_id": "P163", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:tbl[31]", "paragraph_id": null, "table_id": "T31"}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[164]", "paragraph_id": "P164", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[165]", "paragraph_id": "P165", "table_id": null}, {"source_id": "src-000320", "heading_path": ["Description of BusinessActivities", "Transaction Reporting", "Financial Instrument Transaction Report"], "locator": "/w:document/w:body/w:p[166]", "paragraph_id": "P166", "table_id": null}]
participants: ["participant-src-000320-competent-authority", "participant-src-000320-relevant-ca", "participant-src-000320-reporting-entity"]
message_mapping_evidence: [{"source_id": "src-000320", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Transaction Reporting MessageDefinition"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[2]", "paragraph_id": null, "table_id": "T7"}]
message_ids: []
message_families: ["auth.016"]
search_terms: ["Financial Instrument Transaction Report", "Reporting Entity", "Relevant CA", "IF", "RE", "CA", "auth.016"]
limitations: ["Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.", "Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.", "The activity picture ends after the Relevant Competent Authority generates status; it does not draw a return arrow. Sequence figure36 separately shows that response. The source label Transactions Report Message is preserved, though T31 uses Transaction Report Message."]
manual_curated: true
participant_ids: ["participant-src-000320-competent-authority", "participant-src-000320-relevant-ca", "participant-src-000320-reporting-entity"]
related_diagrams: ["domains/securities/reference/message-sets/fitrr/2025/diagrams/fitrr-activities/fig-0016.md"]
---

# Transaction reporting and authority exchange

[src-000320](../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart1_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v2.docx); Description of BusinessActivities / Transaction Reporting / Financial Instrument Transaction Report; direct-body paragraph P163; T31.

## Purpose and source conditions

[T20](../documents/src-000320/tables/tbl-0020.md)

| Item | Description |
| --- | --- |
| Definition | Any entity (IF, ARM) that has to report transanction data to CA. Reported data is related to the transactions in the instruments that are admitted to trading or their derivatives. |
| Trigger | Data is submitted daily and no later than the close of the following working day transaction was executed. |
| Pre-conditions | Transaction in the financial instrument or its derivate is executed. |
| Post-conditions | The reporting entity has received a  status advice related to the submitted transactions report message. |
| Role | Reporting entity |


[T21](../documents/src-000320/tables/tbl-0021.md)

| Item | Description |
| --- | --- |
| Definition | CA that has to exchange relevant transanction data to another CA. Relevant data must fulfill exchange conditions agreed between CAs. |
| Trigger | CA received transaction data which fulfills exchange conditions agreed between CAs. |
| Pre-conditions | Transaction in the financial instrument or its derivate is executed and reported to one of CAs. |
| Post-conditions | Sending CA has received a status advice related to the exchanged data. |
| Role | Sending CA |


## Participants and their responsibilities

- [Reporting Entity](../../../../../../../shared/reference/participants/participant-src-000320-reporting-entity.md)
- [Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-competent-authority.md)
- [Relevant Competent Authority](../../../../../../../shared/reference/participants/participant-src-000320-relevant-ca.md)

| Step | Description | Initiator |
| --- | --- | --- |
| Generate and Submit Transaction Report Message | Reporting entity generates report related to executed transactions and submits it to the CA | RE |
| Receive Messages | CA receives the messages and performs additional operations on them | CA |
| Process Message and Generate Status Advice | Each received message is checked for <br>Completeness and correctness of message <br>Transaction to be exchanged with relevant CA<br>Once complete, generate the status advice file for distribution | CA |
| Receive and Process Response | RE checks for and receives status advice messages which provides details on the records they submitted. They download and process the status advice message to identify if any further actions need to be taken complete the data submission process | RE |
| Corrective Action | Where an issue has been identified in a submitted record, the record must be fixed and the updated records re-submitted | RE |
| Process Exchanged Message and Generate Status | Each exchanged message is checked for completeness and correctness of message. Once complete, generate the status advice file for distribution | Relevant CA |


## Decisions, ordered paths and exceptional outcomes

[Full activity reconstruction and labelled edge table](../diagrams/fitrr-activities/fig-0016.md)

Each table row describes an activity, not a universal linear execution order. Follow the graph for delegation choices, fork/merge paths, accepted outcomes and corrective-action loops.

## Message exchanges and related flows

- [Sequence 36 with sender/receiver, message families and narrative](../diagrams/fitrr-sequences/fig-0036.md)

## Limitations

- Mermaid flowchart subgraphs preserve the source swimlanes. Dark bar nodes retain each source control bar and all connected edges; they are not silently flattened into exclusive decisions. Source start/final symbols become labelled circles; blank source decisions remain unlabelled.
- Node IDs in the edge table distinguish otherwise repeated labels. The source original is retained for exact geometry; no additional business path or timing is inferred.
- The activity picture ends after the Relevant Competent Authority generates status; it does not draw a return arrow. Sequence figure36 separately shows that response. The source label Transactions Report Message is preserved, though T31 uses Transaction Report Message.
