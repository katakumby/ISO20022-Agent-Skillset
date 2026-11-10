---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p745-switch"
title: "Switch amended-confirmation status query"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P727", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request "], "xml_path": "/w:document/w:body/w:p[727]"}, {"source_id": "src-000095", "paragraph_id": "P728", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request "], "xml_path": "/w:document/w:body/w:p[728]"}, {"source_id": "src-000095", "paragraph_id": "P729", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request "], "xml_path": "/w:document/w:body/w:p[729]"}, {"source_id": "src-000095", "paragraph_id": "P730", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request "], "xml_path": "/w:document/w:body/w:p[730]"}, {"source_id": "src-000095", "paragraph_id": "P746", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request ", "Switch "], "xml_path": "/w:document/w:body/w:p[746]"}, {"source_id": "src-000095", "paragraph_id": "P747", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request ", "Switch "], "xml_path": "/w:document/w:body/w:p[747]"}, {"source_id": "src-000095", "paragraph_id": "P748", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request ", "Switch "], "xml_path": "/w:document/w:body/w:p[748]"}, {"source_id": "src-000095", "paragraph_id": "P749", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request ", "Switch "], "xml_path": "/w:document/w:body/w:p[749]"}, {"source_id": "src-000095", "paragraph_id": "P750", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request ", "Switch "], "xml_path": "/w:document/w:body/w:p[750]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P751", "heading_path": ["BusinessTransactions", "Order Confirmation Status Request ", "Switch "], "xml_path": "/w:document/w:body/w:p[751]", "figure_id": "fig-0105"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[14]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3487; 53 setr.013.001.05 SwitchOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[16]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3802; 55 setr.015.001.05 SwitchOrderConfirmationV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[8]/w:tr[6]", "paragraph_id": null, "table_id": "T8"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[5]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[6]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4303; 65 setr.058.001.03 RequestForOrderConfirmationStatusReportV03"}]
message_ids: ["setr.013.001.05", "setr.015.001.05", "setr.057.001.03", "setr.058.001.03"]
message_families: ["setr.013", "setr.015", "setr.056", "setr.057", "setr.058"]
search_terms: ["Switch", "Instructing Party", "Executing Party", "setr.013", "setr.015", "setr.056", "setr.057", "setr.058"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0105.md"]
updated: "2026-11-09"
---

# Switch amended-confirmation status query

## Purpose, trigger and outcome

Request the status of a previously sent amended switch confirmation.

**Trigger:** The executing party has sent a confirmation and an amendment, and then requests its status.

**Source-defined outcome:** The instructing party reports that the amended confirmation is accepted.

These statements are grounded in src-000095 P746–P750. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | SwitchOrder |
| 2 | Executing Party | Instructing Party | SwitchOrderConfirmation |
| 3 | Executing Party | Instructing Party | SwitchOrderConfirmation &lt;AmdmntInd&gt; true |
| 4 | Executing Party | Instructing Party | RequestForOrderConfirmationStatusReport |
| 5 | Instructing Party | Executing Party | OrderConfirmationStatusReport |


## Ordered narrative, conditions and alternatives

**src-000095 P746** — An instructing party sends a SwitchOrder message to the executing party. 

**src-000095 P747** — The executing party replies with a SwitchOrderConfirmation message.

**src-000095 P748** — As execution details need to be amended, the executing party sends another SwitchOrderConfirmation message with the AmendmentIndicator set to 'true' or '1'..

**src-000095 P749** — Later, the executing party sends a RequestForOrderConfirmationStatusReport message to find out the status of its SwitchOrderConfirmation (amendment) message.

**src-000095 P750** — The instructing party sends an OrderConfirmationStatusReport message to the executing party, indicating the status of the SwitchOrderConfirmation (amendment) is accepted.

### Common source context

**src-000095 P727** — This message flow section illustrates the use of the RequestForOrderConfirmationStatusReport message in typical message sequencing scenarios. The RequestForOrderConfirmationStatusReport message is sent by the executing party to the instructing party. It is used to request the status of one or several order confirmation messages. There may be one or more intermediaries in the transaction chain.

**src-000095 P728** — The reply to the RequestForOrderConfirmationStatusReport message is an OrderConfirmationStatusReport message.

**src-000095 P729** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P730** — The intermediary party is, for example, a distributor.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| OrderConfirmationStatusReport | [setr.057.001.03](../../../../messages/setr.057.001.03/index.md) | src-000096 file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03 |
| RequestForOrderConfirmationStatusReport | [setr.058.001.03](../../../../messages/setr.058.001.03/index.md) | src-000096 file page 4303; 65 setr.058.001.03 RequestForOrderConfirmationStatusReportV03 |
| SwitchOrder | [setr.013.001.05](../../../../messages/setr.013.001.05/index.md) | src-000096 file page 3487; 53 setr.013.001.05 SwitchOrderV05 |
| SwitchOrderConfirmation | [setr.015.001.05](../../../../messages/setr.015.001.05/index.md) | src-000096 file page 3802; 55 setr.015.001.05 SwitchOrderConfirmationV05 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0105.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md)
- [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
