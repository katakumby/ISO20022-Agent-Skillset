---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p779-rejected"
title: "Portfolio transfer instruction rejected"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P760", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "xml_path": "/w:document/w:body/w:p[760]"}, {"source_id": "src-000095", "paragraph_id": "P761", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "xml_path": "/w:document/w:body/w:p[761]"}, {"source_id": "src-000095", "paragraph_id": "P762", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "xml_path": "/w:document/w:body/w:p[762]"}, {"source_id": "src-000095", "paragraph_id": "P763", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "xml_path": "/w:document/w:body/w:p[763]"}, {"source_id": "src-000095", "paragraph_id": "P780", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Status ", "Rejected "], "xml_path": "/w:document/w:body/w:p[780]"}, {"source_id": "src-000095", "paragraph_id": "P781", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Status ", "Rejected "], "xml_path": "/w:document/w:body/w:p[781]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P782", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Status ", "Rejected "], "xml_path": "/w:document/w:body/w:p[782]", "figure_id": "fig-0109"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transferor", "participant-src-000095-transferee"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[2]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000096", "locator": "file page 943; 35 sese.012.001.12 PortfolioTransferInstructionV12"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10"}]
message_ids: ["sese.009.001.09", "sese.011.001.10", "sese.012.001.12", "sese.014.001.09"]
message_families: ["sese.011", "sese.012"]
search_terms: ["Rejected", "Instructing Party", "Executing Party", "Transferor", "Transferee", "sese.011", "sese.012"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transferee", "participant-src-000095-transferor"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0109.md"]
updated: "2026-11-09"
---

# Portfolio transfer instruction rejected

## Purpose, trigger and outcome

Report rejection of a portfolio transfer instruction.

**Trigger:** The transferee instructs transfer of products on the investor’s account serviced by the transferor.

**Source-defined outcome:** The transferor returns Rejected and a reason.

These statements are grounded in src-000095 P780–P781. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Transferee / New Plan Manager / Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-transferee.md)
- [Transferor / Old Plan Manager / Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-transferor.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Transferee / New Plan Manager / Instructing Party | Transferor / Old Plan Manager / Executing Party | PortfolioTransferInstruction |
| 2 | Transferor / Old Plan Manager / Executing Party | Transferee / New Plan Manager / Instructing Party | TransferInstructionStatusReport &lt;Rjctd&gt; |


## Ordered narrative, conditions and alternatives

**src-000095 P780** — A transferee (new plan manager or instructing party) sends a PortfolioTransferInstruction message to the transferor (old plan manager or executing party) to instruct the transfer the products held by an investor on an account serviced by the transferor.

**src-000095 P781** — The transferor sends a TransferInstructionStatusReport message with the status Rejected and a reason to advise that the request is rejected. 

### Common source context

**src-000095 P760** — This message flow section illustrates the use of the portfolio transfer messages in typical message sequencing scenarios. The portfolio transfer instruction and confirmation messages are exchanged between a transferee (new plan manager) and the transferor (old plan manager).

**src-000095 P761** — The PortfolioTransferInstruction message is sent by the transferee and may be accepted or rejected by the transferor. The transferor may report on the status of a PortfolioTransferInstruction message with the TransferInstructionStatusReport message.

**src-000095 P762** — The PortfolioTransferInstruction message may be cancelled by the transferee with the PortfolioTransferCancellationRequest message. The transferor may report on the status of a PortfolioTransferCancellationRequest message with the TransferInstructionStatusReport message.

**src-000095 P763** — The transferee may query the status of a previously sent PortfolioTransferInstruction message with a RequestForTransferStatusReport message.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| PortfolioTransferCancellationRequest | [sese.014.001.09](../../../../messages/sese.014.001.09/index.md) | src-000096 file page 1302; 37 sese.014.001.09 PortfolioTransferCancellationRequestV09 |
| PortfolioTransferInstruction | [sese.012.001.12](../../../../messages/sese.012.001.12/index.md) | src-000096 file page 943; 35 sese.012.001.12 PortfolioTransferInstructionV12 |
| RequestForTransferStatusReport | [sese.009.001.09](../../../../messages/sese.009.001.09/index.md) | src-000096 file page 784; 32 sese.009.001.09 RequestForTransferStatusReportV09 |
| TransferInstructionStatusReport | [sese.011.001.10](../../../../messages/sese.011.001.10/index.md) | src-000096 file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0109.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)
- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
