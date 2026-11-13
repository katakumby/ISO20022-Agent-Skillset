---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p558-request-and-status-intermediary"
title: "Switch cancellation — intermediary"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P505", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "xml_path": "/w:document/w:body/w:p[505]"}, {"source_id": "src-000095", "paragraph_id": "P506", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "xml_path": "/w:document/w:body/w:p[506]"}, {"source_id": "src-000095", "paragraph_id": "P507", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "xml_path": "/w:document/w:body/w:p[507]"}, {"source_id": "src-000095", "paragraph_id": "P508", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "xml_path": "/w:document/w:body/w:p[508]"}, {"source_id": "src-000095", "paragraph_id": "P509", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "xml_path": "/w:document/w:body/w:p[509]"}, {"source_id": "src-000095", "paragraph_id": "P510", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "xml_path": "/w:document/w:body/w:p[510]"}, {"source_id": "src-000095", "paragraph_id": "P511", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "xml_path": "/w:document/w:body/w:p[511]"}, {"source_id": "src-000095", "paragraph_id": "P512", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "xml_path": "/w:document/w:body/w:p[512]"}, {"source_id": "src-000095", "paragraph_id": "P513", "heading_path": ["BusinessTransactions", "Order Cancellation and Status "], "xml_path": "/w:document/w:body/w:p[513]"}, {"source_id": "src-000095", "paragraph_id": "P559", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Switch ", "Request and Status - Intermediary"], "xml_path": "/w:document/w:body/w:p[559]"}, {"source_id": "src-000095", "paragraph_id": "P560", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Switch ", "Request and Status - Intermediary"], "xml_path": "/w:document/w:body/w:p[560]"}, {"source_id": "src-000095", "paragraph_id": "P561", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Switch ", "Request and Status - Intermediary"], "xml_path": "/w:document/w:body/w:p[561]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P562", "heading_path": ["BusinessTransactions", "Order Cancellation and Status ", "Switch ", "Request and Status - Intermediary"], "xml_path": "/w:document/w:body/w:p[562]", "figure_id": "fig-0079"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-intermediary"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[14]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3487; 53 setr.013.001.05 SwitchOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[15]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4205; 57 setr.017.001.05 OrderCancellationStatusReportV05"}, {"source_id": "src-000096", "locator": "file page 3797; 54 setr.014.001.05 SwitchOrderCancellationRequestV05"}]
message_ids: ["setr.013.001.05", "setr.014.001.05", "setr.017.001.05"]
message_families: ["setr.013", "setr.014", "setr.017"]
search_terms: ["Request and Status - Intermediary", "Instructing Party", "Executing Party", "Intermediary", "setr.013", "setr.014", "setr.017"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0079.md"]
updated: "2026-11-09"
---

# Switch cancellation — intermediary

## Purpose, trigger and outcome

Relay a switch cancellation request and its completion through an intermediary.

**Trigger:** The instructing party requests cancellation of a switch order that was relayed through an intermediary.

**Source-defined outcome:** CAND is returned through the intermediary to the instructing party.

These statements are grounded in src-000095 P559–P561. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Intermediary | SwitchOrder |
| 2 | Intermediary | Executing Party | SwitchOrder |
| 3 | Instructing Party | Intermediary | SwitchOrderCancellationRequest |
| 4 | Intermediary | Executing Party | SwitchOrderCancellationRequest |
| 5 | Executing Party | Intermediary | OrderCancellationStatusReport (CAND) |
| 6 | Intermediary | Instructing Party | OrderCancellationStatusReport (CAND) |


## Ordered narrative, conditions and alternatives

**src-000095 P559** — The instructing party sends a SwitchOrder message to the intermediary party. The intermediary party sends the SwitchOrder message to the executing party. 

**src-000095 P560** — Subsequently, the instructing party sends a SwitchOrderCancellationRequest message to the intermediary party. The intermediary party sends the SwitchOrderCancellationRequest message to the executing party. 

**src-000095 P561** — The executing party responds by sending an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the intermediary party. In turn, the intermediary party sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the instructing party.

### Common source context

**src-000095 P505** — This message flow section illustrates the use of the order cancellation messages in typical message sequencing scenarios. The different order cancellation request messages are sent by the instructing party to the executing party. There may be one or more intermediaries in the transaction chain.

**src-000095 P506** — The OrderCancellationStatusReport message is sent by the executing party to the instructing party to inform the instructing party of the acceptance or rejection of an order cancellation request message that was previously sent by the instructing party. 

**src-000095 P507** — The deadline and acceptance of an order cancellation request message is subject to a service level agreement (SLA). 

**src-000095 P508** — Depending on the scenario, the executing party will verify whether:

**src-000095 P509** — it is legally possible to cancel the order, 

**src-000095 P510** — the party that initiated the cancellation request has the right to do so, 

**src-000095 P511** — the cancellation request is allowed by the service level agreement (SLA). 

**src-000095 P512** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P513** — The intermediary party is, for example, an distributor.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| OrderCancellationStatusReport | [setr.017.001.05](../../../../messages/setr.017.001.05/index.md) | src-000096 file page 4205; 57 setr.017.001.05 OrderCancellationStatusReportV05 |
| SwitchOrder | [setr.013.001.05](../../../../messages/setr.013.001.05/index.md) | src-000096 file page 3487; 53 setr.013.001.05 SwitchOrderV05 |
| SwitchOrderCancellationRequest | [setr.014.001.05](../../../../messages/setr.014.001.05/index.md) | src-000096 file page 3797; 54 setr.014.001.05 SwitchOrderCancellationRequestV05 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0079.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
