---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p586-request-status-of-switch"
title: "Switch cancellation status query"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P564", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[564]"}, {"source_id": "src-000095", "paragraph_id": "P565", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[565]"}, {"source_id": "src-000095", "paragraph_id": "P566", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[566]"}, {"source_id": "src-000095", "paragraph_id": "P567", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[567]"}, {"source_id": "src-000095", "paragraph_id": "P568", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[568]"}, {"source_id": "src-000095", "paragraph_id": "P587", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Switch"], "xml_path": "/w:document/w:body/w:p[587]"}, {"source_id": "src-000095", "paragraph_id": "P588", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Switch"], "xml_path": "/w:document/w:body/w:p[588]"}, {"source_id": "src-000095", "paragraph_id": "P589", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Switch"], "xml_path": "/w:document/w:body/w:p[589]"}, {"source_id": "src-000095", "paragraph_id": "P590", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Switch"], "xml_path": "/w:document/w:body/w:p[590]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P591", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Switch"], "xml_path": "/w:document/w:body/w:p[591]", "figure_id": "fig-0083"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[14]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3487; 53 setr.013.001.05 SwitchOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[15]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4205; 57 setr.017.001.05 OrderCancellationStatusReportV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[4]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4232; 58 setr.018.001.05 RequestForOrderStatusReportV05"}, {"source_id": "src-000096", "locator": "file page 3797; 54 setr.014.001.05 SwitchOrderCancellationRequestV05"}]
message_ids: ["setr.013.001.05", "setr.014.001.05", "setr.016.001.05", "setr.017.001.05", "setr.018.001.05"]
message_families: ["setr.013", "setr.014", "setr.017", "setr.018"]
search_terms: ["Request Status of Switch", "Instructing Party", "Executing Party", "setr.013", "setr.014", "setr.017", "setr.018"]
limitations: ["The final picture label is OrderCancellationStatusRequest (CAND); P590 names OrderCancellationStatusReport. Both claims remain visible.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0083.md"]
updated: "2026-11-09"
---

# Switch cancellation status query

## Purpose, trigger and outcome

Request the status of a prior switch cancellation request.

**Trigger:** The instructing party sends a status query after its switch order and cancellation request.

**Source-defined outcome:** The narrative says the executing party has effected cancellation and returns OrderCancellationStatusReport with CAND.

These statements are grounded in src-000095 P587–P590. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | SwitchOrder |
| 2 | Instructing Party | Executing Party | SwitchOrderCancellationRequest |
| 3 | Instructing Party | Executing Party | RequestForOrderStatusReport |
| 4 | Executing Party | Instructing Party | OrderCancellationStatusRequest (CAND) |


## Ordered narrative, conditions and alternatives

**src-000095 P587** — An instructing party sends a SwitchOrder message to the executing party. 

**src-000095 P588** — Subsequently, the instructing party sends a SwitchOrderCancellationRequest message to the executing party.

**src-000095 P589** — Later, the instructing party sends a RequestForOrderStatusReport message to find out the status of its cancellation request.

**src-000095 P590** — As the executing party has now effected the cancellation, it sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the instructing party.

### Common source context

**src-000095 P564** — The RequestForOrderStatusReport message is sent by the instructing party to the executing party. It is used to request the status of one or several order messages and/or order cancellation instruction messages. 

**src-000095 P565** — The reply to the RequestForOrderStatusReport message is one of the following:

**src-000095 P566** — an OrderInstructionStatusReport, or,

**src-000095 P567** — an OrderCancellationStatusReport. 

**src-000095 P568** — The scenarios below focus on cases where a OrderCancellationStatusReport message is used.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| OrderCancellationStatusReport | [setr.017.001.05](../../../../messages/setr.017.001.05/index.md) | src-000096 file page 4205; 57 setr.017.001.05 OrderCancellationStatusReportV05 |
| OrderInstructionStatusReport | [setr.016.001.05](../../../../messages/setr.016.001.05/index.md) | src-000096 file page 4109; 56 setr.016.001.05 OrderInstructionStatusReportV05 |
| RequestForOrderStatusReport | [setr.018.001.05](../../../../messages/setr.018.001.05/index.md) | src-000096 file page 4232; 58 setr.018.001.05 RequestForOrderStatusReportV05 |
| SwitchOrder | [setr.013.001.05](../../../../messages/setr.013.001.05/index.md) | src-000096 file page 3487; 53 setr.013.001.05 SwitchOrderV05 |
| SwitchOrderCancellationRequest | [setr.014.001.05](../../../../messages/setr.014.001.05/index.md) | src-000096 file page 3797; 54 setr.014.001.05 SwitchOrderCancellationRequestV05 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0083.md)

- The final picture label is OrderCancellationStatusRequest (CAND); P590 names OrderCancellationStatusReport. Both claims remain visible.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.
