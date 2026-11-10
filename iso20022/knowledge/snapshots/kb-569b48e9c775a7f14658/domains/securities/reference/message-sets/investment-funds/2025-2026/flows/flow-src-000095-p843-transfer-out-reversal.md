---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p843-transfer-out-reversal"
title: "Transfer-out confirmation reversal"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P806", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[806]"}, {"source_id": "src-000095", "paragraph_id": "P807", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[807]"}, {"source_id": "src-000095", "paragraph_id": "P808", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[808]"}, {"source_id": "src-000095", "paragraph_id": "P809", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[809]"}, {"source_id": "src-000095", "paragraph_id": "P810", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[810]"}, {"source_id": "src-000095", "paragraph_id": "P844", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer Out Reversal "], "xml_path": "/w:document/w:body/w:p[844]"}, {"source_id": "src-000095", "paragraph_id": "P845", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer Out Reversal "], "xml_path": "/w:document/w:body/w:p[845]"}, {"source_id": "src-000095", "paragraph_id": "P846", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer Out Reversal "], "xml_path": "/w:document/w:body/w:p[846]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P847", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer Out Reversal "], "xml_path": "/w:document/w:body/w:p[847]", "figure_id": "fig-0119"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[4]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 519; 26 sese.003.001.10 TransferOutConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[5]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 602; 27 sese.004.001.09 ReversalOfTransferOutConfirmationV09"}]
message_ids: ["sese.001.001.10", "sese.003.001.10", "sese.004.001.09"]
message_families: ["sese.001", "sese.003", "sese.004"]
search_terms: ["Transfer Out Reversal", "Instructing Party", "Executing Party", "sese.001", "sese.003", "sese.004"]
limitations: ["The reversal is sent by the executing party after its confirmation. This source scenario does not describe it as an instructing-party cancellation request.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0119.md"]
updated: "2026-11-09"
---

# Transfer-out confirmation reversal

## Purpose, trigger and outcome

Reverse a previously sent transfer-out confirmation.

**Trigger:** The executing party has already confirmed delivery and subsequently sends a reversal.

**Source-defined outcome:** ReversalOfTransferOutConfirmation reverses the TransferOutConfirmation message (P846).

These statements are grounded in src-000095 P844–P846. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | TransferOutInstruction |
| 2 | Executing Party | Instructing Party | TransferOutConfirmation |
| 3 | Executing Party | Instructing Party | ReversalOfTransferOutConfirmation |


## Ordered narrative, conditions and alternatives

**src-000095 P844** — An instructing party sends a TransferOutInstruction message to the executing party. The message requests the executing party to withdraw a quantity of financial instrument from an account the instructing party owns and deliver it to another account. 

**src-000095 P845** — The executing party sends a TransferOutConfirmation message to the instructing party to confirm the delivery.

**src-000095 P846** — Subsequently, the executing party sends a ReversalOfTransferOutConfirmation message to reverse the TransferOutConfirmation message. 

### Common source context

**src-000095 P806** — This message flow section illustrates the use of the transfer messages in typical message sequencing scenarios. The transfer instruction messages are sent by the instructing party to the executing party to instruct either a transfer out or a transfer in.

**src-000095 P807** — The transfer confirmation messages are sent by the executing party to the instructing party to confirm a transfer out or transfer in.

**src-000095 P808** — The transfer status messages are sent by the executing party to the instructing party to provide the status of the transfer instructions.

**src-000095 P809** — There may be one or more intermediaries in the transaction chain.

**src-000095 P810** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| ReversalOfTransferOutConfirmation | [sese.004.001.09](../../../../messages/sese.004.001.09/index.md) | src-000096 file page 602; 27 sese.004.001.09 ReversalOfTransferOutConfirmationV09 |
| TransferOutConfirmation | [sese.003.001.10](../../../../messages/sese.003.001.10/index.md) | src-000096 file page 519; 26 sese.003.001.10 TransferOutConfirmationV10 |
| TransferOutInstruction | [sese.001.001.10](../../../../messages/sese.001.001.10/index.md) | src-000096 file page 433; 24 sese.001.001.10 TransferOutInstructionV10 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0119.md)

- The reversal is sent by the executing party after its confirmation. This source scenario does not describe it as an instructing-party cancellation request.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
