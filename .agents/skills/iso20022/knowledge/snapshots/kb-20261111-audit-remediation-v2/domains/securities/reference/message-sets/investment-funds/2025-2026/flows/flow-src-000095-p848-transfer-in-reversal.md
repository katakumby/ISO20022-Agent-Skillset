---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p848-transfer-in-reversal"
title: "Transfer-in confirmation reversal"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P806", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[806]"}, {"source_id": "src-000095", "paragraph_id": "P807", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[807]"}, {"source_id": "src-000095", "paragraph_id": "P808", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[808]"}, {"source_id": "src-000095", "paragraph_id": "P809", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[809]"}, {"source_id": "src-000095", "paragraph_id": "P810", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[810]"}, {"source_id": "src-000095", "paragraph_id": "P849", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer In Reversal "], "xml_path": "/w:document/w:body/w:p[849]"}, {"source_id": "src-000095", "paragraph_id": "P850", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer In Reversal "], "xml_path": "/w:document/w:body/w:p[850]"}, {"source_id": "src-000095", "paragraph_id": "P851", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer In Reversal "], "xml_path": "/w:document/w:body/w:p[851]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P852", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer In Reversal "], "xml_path": "/w:document/w:body/w:p[852]", "figure_id": "fig-0120"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 608; 28 sese.005.001.10 TransferInInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[8]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 695; 30 sese.007.001.10 TransferInConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[9]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 778; 31 sese.008.001.09 ReversalOfTransferInConfirmationV09"}]
message_ids: ["sese.005.001.10", "sese.007.001.10", "sese.008.001.09"]
message_families: ["sese.005", "sese.007", "sese.008"]
search_terms: ["Transfer In Reversal", "Instructing Party", "Executing Party", "sese.005", "sese.007", "sese.008"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0120.md"]
updated: "2026-11-09"
---

# Transfer-in confirmation reversal

## Purpose, trigger and outcome

Reverse a previously sent transfer-in confirmation.

**Trigger:** The executing party has confirmed receipt and subsequently sends a reversal.

**Source-defined outcome:** ReversalOfTransferInConfirmation reverses the TransferInConfirmation message (P851).

These statements are grounded in src-000095 P849–P851. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | TransferInInstruction |
| 2 | Executing Party | Instructing Party | TransferInConfirmation |
| 3 | Executing Party | Instructing Party | ReversalOfTransferInConfirmation |


## Ordered narrative, conditions and alternatives

**src-000095 P849** — An instructing party sends a TransferInInstruction message to the executing party. The message requests the executing party to receive a quantity of financial instrument from another account.

**src-000095 P850** — The executing party sends a TransferInConfirmation message to the instructing party, to confirm a receipt into the account of the instructing party. 

**src-000095 P851** — Subsequently, the executing party sends a ReversalOfTransferInConfirmation message to reverse the TransferInConfirmation message.

### Common source context

**src-000095 P806** — This message flow section illustrates the use of the transfer messages in typical message sequencing scenarios. The transfer instruction messages are sent by the instructing party to the executing party to instruct either a transfer out or a transfer in.

**src-000095 P807** — The transfer confirmation messages are sent by the executing party to the instructing party to confirm a transfer out or transfer in.

**src-000095 P808** — The transfer status messages are sent by the executing party to the instructing party to provide the status of the transfer instructions.

**src-000095 P809** — There may be one or more intermediaries in the transaction chain.

**src-000095 P810** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| ReversalOfTransferInConfirmation | [sese.008.001.09](../../../../messages/sese.008.001.09/index.md) | src-000096 file page 778; 31 sese.008.001.09 ReversalOfTransferInConfirmationV09 |
| TransferInConfirmation | [sese.007.001.10](../../../../messages/sese.007.001.10/index.md) | src-000096 file page 695; 30 sese.007.001.10 TransferInConfirmationV10 |
| TransferInInstruction | [sese.005.001.10](../../../../messages/sese.005.001.10/index.md) | src-000096 file page 608; 28 sese.005.001.10 TransferInInstructionV10 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0120.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
