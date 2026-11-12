---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p575-request-status-of-redemption"
title: "Redemption cancellation status query"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P564", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[564]"}, {"source_id": "src-000095", "paragraph_id": "P565", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[565]"}, {"source_id": "src-000095", "paragraph_id": "P566", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[566]"}, {"source_id": "src-000095", "paragraph_id": "P567", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[567]"}, {"source_id": "src-000095", "paragraph_id": "P568", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request"], "xml_path": "/w:document/w:body/w:p[568]"}, {"source_id": "src-000095", "paragraph_id": "P576", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Redemption"], "xml_path": "/w:document/w:body/w:p[576]"}, {"source_id": "src-000095", "paragraph_id": "P577", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Redemption"], "xml_path": "/w:document/w:body/w:p[577]"}, {"source_id": "src-000095", "paragraph_id": "P578", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Redemption"], "xml_path": "/w:document/w:body/w:p[578]"}, {"source_id": "src-000095", "paragraph_id": "P579", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Redemption"], "xml_path": "/w:document/w:body/w:p[579]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P580", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Request Status of Redemption"], "xml_path": "/w:document/w:body/w:p[580]", "figure_id": "fig-0081"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[5]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2101; 44 setr.004.001.05 RedemptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[6]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2305; 45 setr.005.001.05 RedemptionOrderCancellationRequestV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4205; 57 setr.017.001.05 OrderCancellationStatusReportV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[4]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4232; 58 setr.018.001.05 RequestForOrderStatusReportV05"}]
message_ids: ["setr.004.001.05", "setr.005.001.05", "setr.016.001.05", "setr.017.001.05", "setr.018.001.05"]
message_families: ["setr.004", "setr.005", "setr.017", "setr.018"]
search_terms: ["Request Status of Redemption", "Instructing Party", "Executing Party", "setr.004", "setr.005", "setr.017", "setr.018"]
limitations: ["The final picture label is OrderCancellationStatusRequest (CAND); P579 names OrderCancellationStatusReport. Both claims remain visible.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0081.md"]
updated: "2026-11-09"
---

# Redemption cancellation status query

## Purpose, trigger and outcome

Request the status of a prior redemption cancellation request.

**Trigger:** After the redemption order and cancellation request, the instructing party requests cancellation status.

**Source-defined outcome:** The narrative says the executing party has effected cancellation and returns OrderCancellationStatusReport with CAND.

These statements are grounded in src-000095 P576–P579. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | RedemptionOrder |
| 2 | Instructing Party | Executing Party | RedemptionOrderCancellationRequest |
| 3 | Instructing Party | Executing Party | RequestForOrderStatusReport |
| 4 | Executing Party | Instructing Party | OrderCancellationStatusRequest (CAND) |


## Ordered narrative, conditions and alternatives

**src-000095 P576** — An instructing party sends a RedemptionOrder message to the executing party.

**src-000095 P577** — Subsequently, the instructing party sends a RedemptionOrderCancellationRequest message to the executing party.

**src-000095 P578** — Later, the instructing party sends a RequestForOrderStatusReport message to find out the status of its cancellation request.

**src-000095 P579** — As the executing party has now effected the cancellation, it sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the instructing party.

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
| RedemptionOrder | [setr.004.001.05](../../../../messages/setr.004.001.05/index.md) | src-000096 file page 2101; 44 setr.004.001.05 RedemptionOrderV05 |
| RedemptionOrderCancellationRequest | [setr.005.001.05](../../../../messages/setr.005.001.05/index.md) | src-000096 file page 2305; 45 setr.005.001.05 RedemptionOrderCancellationRequestV05 |
| RequestForOrderStatusReport | [setr.018.001.05](../../../../messages/setr.018.001.05/index.md) | src-000096 file page 4232; 58 setr.018.001.05 RequestForOrderStatusReportV05 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0081.md)

- The final picture label is OrderCancellationStatusRequest (CAND); P579 names OrderCancellationStatusReport. Both claims remain visible.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.
