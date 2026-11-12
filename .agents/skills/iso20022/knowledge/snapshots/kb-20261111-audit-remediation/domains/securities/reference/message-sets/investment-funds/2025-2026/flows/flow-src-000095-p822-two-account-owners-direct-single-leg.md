---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p822-two-account-owners-direct-single-leg"
title: "Two-owner asset transfer — direct single leg"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P806", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[806]"}, {"source_id": "src-000095", "paragraph_id": "P807", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[807]"}, {"source_id": "src-000095", "paragraph_id": "P808", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[808]"}, {"source_id": "src-000095", "paragraph_id": "P809", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[809]"}, {"source_id": "src-000095", "paragraph_id": "P810", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[810]"}, {"source_id": "src-000095", "paragraph_id": "P823", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – Single Leg"], "xml_path": "/w:document/w:body/w:p[823]"}, {"source_id": "src-000095", "paragraph_id": "P824", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – Single Leg"], "xml_path": "/w:document/w:body/w:p[824]"}, {"source_id": "src-000095", "paragraph_id": "P825", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – Single Leg"], "xml_path": "/w:document/w:body/w:p[825]"}, {"source_id": "src-000095", "paragraph_id": "P826", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – Single Leg"], "xml_path": "/w:document/w:body/w:p[826]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P827", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – Single Leg"], "xml_path": "/w:document/w:body/w:p[827]", "figure_id": "fig-0116"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[4]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 519; 26 sese.003.001.10 TransferOutConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 608; 28 sese.005.001.10 TransferInInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[8]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 695; 30 sese.007.001.10 TransferInConfirmationV10"}]
message_ids: ["sese.001.001.10", "sese.003.001.10", "sese.005.001.10", "sese.007.001.10"]
message_families: ["sese.001", "sese.003", "sese.005", "sese.007"]
search_terms: ["Two Account Owners – Direct – Single Leg", "Instructing Party", "Executing Party", "sese.001", "sese.003", "sese.005", "sese.007"]
limitations: ["The paired confirmations share the same vertical position in the source picture. Separate Mermaid rows are for legibility and do not establish an order between these two confirmations.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0116.md"]
updated: "2026-11-09"
---

# Two-owner asset transfer — direct single leg

## Purpose, trigger and outcome

Transfer an asset between two owners at one executing party using only a transfer-out instruction.

**Trigger:** The SLA between executing party and instructing party 2 permits action without a corresponding TransferInInstruction.

**Source-defined outcome:** The executing party confirms delivery to party 1 and receipt to party 2.

These statements are grounded in src-000095 P823–P826. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)
- [Instructing Party 2](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party 1 | Executing Party | TransferOutInstruction |
| 2 | Executing Party | Instructing Party 1 | TransferOutConfirmation |
| 3 | Executing Party | Instructing Party 2 | TransferInConfirmation |


## Ordered narrative, conditions and alternatives

**src-000095 P823** — Instructing party 1 sends a TransferOutInstruction message to the executing party. 

**src-000095 P824** — The message requests the executing party to withdraw a quantity of financial instrument from the instructing party's account and deliver the financial instrument to instructing party 2, which also has its account at the executing party. 

**src-000095 P825** — The Service Level Agreement (SLA) in place between the executing party and instructing party 2, specifies that the executing party does not need to receive a corresponding TransferInInstruction message from instructing party 2 in order to act upon the TransferOutInstruction message. 

**src-000095 P826** — The executing party sends a TransferOutConfirmation message to instructing party 1 to confirm the delivery and a TransferInConfirmation message to instructing party 2, to confirm the receipt of the financial instrument.

### Common source context

**src-000095 P806** — This message flow section illustrates the use of the transfer messages in typical message sequencing scenarios. The transfer instruction messages are sent by the instructing party to the executing party to instruct either a transfer out or a transfer in.

**src-000095 P807** — The transfer confirmation messages are sent by the executing party to the instructing party to confirm a transfer out or transfer in.

**src-000095 P808** — The transfer status messages are sent by the executing party to the instructing party to provide the status of the transfer instructions.

**src-000095 P809** — There may be one or more intermediaries in the transaction chain.

**src-000095 P810** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| TransferInConfirmation | [sese.007.001.10](../../../../messages/sese.007.001.10/index.md) | src-000096 file page 695; 30 sese.007.001.10 TransferInConfirmationV10 |
| TransferInInstruction | [sese.005.001.10](../../../../messages/sese.005.001.10/index.md) | src-000096 file page 608; 28 sese.005.001.10 TransferInInstructionV10 |
| TransferOutConfirmation | [sese.003.001.10](../../../../messages/sese.003.001.10/index.md) | src-000096 file page 519; 26 sese.003.001.10 TransferOutConfirmationV10 |
| TransferOutInstruction | [sese.001.001.10](../../../../messages/sese.001.001.10/index.md) | src-000096 file page 433; 24 sese.001.001.10 TransferOutInstructionV10 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0116.md)

- The paired confirmations share the same vertical position in the source picture. Separate Mermaid rows are for legibility and do not establish an order between these two confirmations.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
