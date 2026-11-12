---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p857-transfer-in-cancellation"
title: "Transfer-in instruction cancellation request"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P806", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[806]"}, {"source_id": "src-000095", "paragraph_id": "P807", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[807]"}, {"source_id": "src-000095", "paragraph_id": "P808", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[808]"}, {"source_id": "src-000095", "paragraph_id": "P809", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[809]"}, {"source_id": "src-000095", "paragraph_id": "P810", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[810]"}, {"source_id": "src-000095", "paragraph_id": "P858", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer In Cancellation "], "xml_path": "/w:document/w:body/w:p[858]"}, {"source_id": "src-000095", "paragraph_id": "P859", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer In Cancellation "], "xml_path": "/w:document/w:body/w:p[859]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P860", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Transfer In Cancellation "], "xml_path": "/w:document/w:body/w:p[860]", "figure_id": "fig-0122"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 608; 28 sese.005.001.10 TransferInInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[7]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 689; 29 sese.006.001.09 TransferInCancellationRequestV09"}]
message_ids: ["sese.005.001.10", "sese.006.001.09"]
message_families: ["sese.005", "sese.006"]
search_terms: ["Transfer In Cancellation", "Instructing Party", "Executing Party", "sese.005", "sese.006"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0122.md"]
updated: "2026-11-09"
---

# Transfer-in instruction cancellation request

## Purpose, trigger and outcome

Request cancellation of a prior transfer-in instruction.

**Trigger:** An SLA permits cancellation when necessary and in accordance with its conditions.

**Source-defined outcome:** The instructing party sends the cancellation request; this picture and section do not assert completed cancellation.

These statements are grounded in src-000095 P858–P859. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | TransferInInstruction |
| 2 | Instructing Party | Executing Party | TransferInCancellationRequest |


## Ordered narrative, conditions and alternatives

**src-000095 P858** — An instructing party sends a TransferInInstruction message to the executing party. 

**src-000095 P859** — There is an SLA in place between the instructing party and the executing party that allows the instructing party to cancel the transfer instructions, if necessary and if in accordance with the SLA. Subsequently, the instructing party needs to cancel the transfer and sends a TransferInCancellationRequest message to cancel the previously sent TransferInInstruction message.

### Common source context

**src-000095 P806** — This message flow section illustrates the use of the transfer messages in typical message sequencing scenarios. The transfer instruction messages are sent by the instructing party to the executing party to instruct either a transfer out or a transfer in.

**src-000095 P807** — The transfer confirmation messages are sent by the executing party to the instructing party to confirm a transfer out or transfer in.

**src-000095 P808** — The transfer status messages are sent by the executing party to the instructing party to provide the status of the transfer instructions.

**src-000095 P809** — There may be one or more intermediaries in the transaction chain.

**src-000095 P810** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| TransferInCancellationRequest | [sese.006.001.09](../../../../messages/sese.006.001.09/index.md) | src-000096 file page 689; 29 sese.006.001.09 TransferInCancellationRequestV09 |
| TransferInInstruction | [sese.005.001.10](../../../../messages/sese.005.001.10/index.md) | src-000096 file page 608; 28 sese.005.001.10 TransferInInstructionV10 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0122.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
