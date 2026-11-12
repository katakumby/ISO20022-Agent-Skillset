---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p768-portfolio-transfer-instruction"
title: "Portfolio transfer instruction and completion"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P760", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "xml_path": "/w:document/w:body/w:p[760]"}, {"source_id": "src-000095", "paragraph_id": "P761", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "xml_path": "/w:document/w:body/w:p[761]"}, {"source_id": "src-000095", "paragraph_id": "P762", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "xml_path": "/w:document/w:body/w:p[762]"}, {"source_id": "src-000095", "paragraph_id": "P763", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management"], "xml_path": "/w:document/w:body/w:p[763]"}, {"source_id": "src-000095", "paragraph_id": "P769", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"], "xml_path": "/w:document/w:body/w:p[769]"}, {"source_id": "src-000095", "paragraph_id": "P770", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"], "xml_path": "/w:document/w:body/w:p[770]"}, {"source_id": "src-000095", "paragraph_id": "P771", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"], "xml_path": "/w:document/w:body/w:p[771]"}, {"source_id": "src-000095", "paragraph_id": "P772", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"], "xml_path": "/w:document/w:body/w:p[772]"}, {"source_id": "src-000095", "paragraph_id": "P773", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"], "xml_path": "/w:document/w:body/w:p[773]"}, {"source_id": "src-000095", "paragraph_id": "P774", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"], "xml_path": "/w:document/w:body/w:p[774]"}, {"source_id": "src-000095", "paragraph_id": "P775", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"], "xml_path": "/w:document/w:body/w:p[775]"}, {"source_id": "src-000095", "paragraph_id": "P776", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"], "xml_path": "/w:document/w:body/w:p[776]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P777", "heading_path": ["BusinessTransactions", "Portfolio Transfer Management", "Portfolio Transfer Instruction"], "xml_path": "/w:document/w:body/w:p[777]", "figure_id": "fig-0108"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transferor", "participant-src-000095-transferee"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[2]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000096", "locator": "file page 1308; 38 sese.018.001.10 AccountHoldingInformationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[10]/w:tr[3]", "paragraph_id": null, "table_id": "T10"}, {"source_id": "src-000096", "locator": "file page 1442; 39 sese.019.001.09 AccountHoldingInformationRequestV09"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[2]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000096", "locator": "file page 943; 35 sese.012.001.12 PortfolioTransferInstructionV12"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[3]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000096", "locator": "file page 1106; 36 sese.013.001.12 PortfolioTransferConfirmationV12"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[11]/w:tr[5]", "paragraph_id": null, "table_id": "T11"}, {"source_id": "src-000096", "locator": "file page 1489; 40 sese.043.001.02 PortfolioTransferCompletionV02"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}]
message_ids: ["sese.009.001.09", "sese.011.001.10", "sese.012.001.12", "sese.013.001.12", "sese.014.001.09", "sese.018.001.10", "sese.019.001.09", "sese.043.001.02"]
message_families: ["sese.001", "sese.012", "sese.013", "sese.018", "sese.019", "sese.043"]
search_terms: ["Portfolio Transfer Instruction", "Instructing Party", "Executing Party", "Transferor", "Transferee", "sese.001", "sese.012", "sese.013", "sese.018", "sese.019", "sese.043"]
limitations: ["The source shaded “Individual Asset Transfers” band occurs after PortfolioTransferConfirmation and before PortfolioTransferCompletion. It is retained as a spanning note, not invented as an exchanged message. Fund units use transfer-out instruction/confirmation; cash uses a payment flow; liquidation requires redemption and payment flows (P775).", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-transferee", "participant-src-000095-transferor"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0108.md"]
updated: "2026-11-09"
---

# Portfolio transfer instruction and completion

## Purpose, trigger and outcome

Instruct transfer of a portfolio and report intent, then completion after its individual asset transfers.

**Trigger:** The transferee discovers the individual products and instructs their transfer.

**Source-defined outcome:** Once all individual asset transfers are executed and settled, the transferor reports completion. Per-asset alternatives are in-specie transfer, liquidation and cash transfer, or conversion followed by in-specie transfer.

These statements are grounded in src-000095 P769–P776. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Transferee / New Plan Manager / Instructing Party / Acquiring Party](../../../../../../../shared/reference/participants/participant-src-000095-transferee.md)
- [Transferor / Old Plan Manager / Executing Party / Ceding Party](../../../../../../../shared/reference/participants/participant-src-000095-transferor.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Transferee / New Plan Manager / Instructing Party / Acquiring Party | Transferor / Old Plan Manager / Executing Party / Ceding Party | AccountHoldingInformationRequest |
| 2 | Transferor / Old Plan Manager / Executing Party / Ceding Party | Transferee / New Plan Manager / Instructing Party / Acquiring Party | AccountHoldingInformation |
| 3 | Transferee / New Plan Manager / Instructing Party / Acquiring Party | Transferor / Old Plan Manager / Executing Party / Ceding Party | PortfolioTransferInstruction |
| 4 | Transferor / Old Plan Manager / Executing Party / Ceding Party | Transferee / New Plan Manager / Instructing Party / Acquiring Party | PortfolioTransferConfirmation |
| 5 | Transferor / Old Plan Manager / Executing Party / Ceding Party | Transferee / New Plan Manager / Instructing Party / Acquiring Party | PortfolioTransferCompletion |


## Ordered narrative, conditions and alternatives

**src-000095 P769** — A transferee (new plan manager or instructing party) sends the AccountHoldingInformationRequest message to the transferor (old plan manager or executing party) to request information about financial instruments held on behalf of the client.

**src-000095 P770** — The transferor responds by sending an AccountHoldingInformation message, specifying the individual products in the portfolio.

**src-000095 P771** — The transferee now instructs the transfer of the portfolio by sending a PortfolioTransferInstruction message to the transferor. This instructs the transfer of the individual products in the portfolio, such as fund units, cash, equities and other assets such as property. For each individual asset, the transferee will instruct one of the following:

**src-000095 P772** — transfer 'as is' (in specie)

**src-000095 P773** — liquidate and transfer as cash

**src-000095 P774** — convert to another instrument and then transfer 'as is' (in specie).

**src-000095 P775** — The transferor sends a PortfolioTransferConfirmation message to confirm its intent to transfer the assets. The actual transfer and confirmation of the individual assets, if fund units, is carried out using the transfer out instruction and confirmation. If the portfolio contains cash, then there will be a payment flow. If an asset is to be liquidated and transferred as cash, there will be a redemption flow and a payment flow.

**src-000095 P776** — Once all individual asset transfers are executed and settled, a PortfolioTransferCompletion message is sent by the transferor, to the transferee, to confirm that the transfer of financial instruments from the client’s account at the transferor to the clients account at the transferee has been completed.

### Common source context

**src-000095 P760** — This message flow section illustrates the use of the portfolio transfer messages in typical message sequencing scenarios. The portfolio transfer instruction and confirmation messages are exchanged between a transferee (new plan manager) and the transferor (old plan manager).

**src-000095 P761** — The PortfolioTransferInstruction message is sent by the transferee and may be accepted or rejected by the transferor. The transferor may report on the status of a PortfolioTransferInstruction message with the TransferInstructionStatusReport message.

**src-000095 P762** — The PortfolioTransferInstruction message may be cancelled by the transferee with the PortfolioTransferCancellationRequest message. The transferor may report on the status of a PortfolioTransferCancellationRequest message with the TransferInstructionStatusReport message.

**src-000095 P763** — The transferee may query the status of a previously sent PortfolioTransferInstruction message with a RequestForTransferStatusReport message.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| AccountHoldingInformation | [sese.018.001.10](../../../../messages/sese.018.001.10/index.md) | src-000096 file page 1308; 38 sese.018.001.10 AccountHoldingInformationV10 |
| AccountHoldingInformationRequest | [sese.019.001.09](../../../../messages/sese.019.001.09/index.md) | src-000096 file page 1442; 39 sese.019.001.09 AccountHoldingInformationRequestV09 |
| PortfolioTransferCancellationRequest | [sese.014.001.09](../../../../messages/sese.014.001.09/index.md) | src-000096 file page 1302; 37 sese.014.001.09 PortfolioTransferCancellationRequestV09 |
| PortfolioTransferCompletion | [sese.043.001.02](../../../../messages/sese.043.001.02/index.md) | src-000096 file page 1489; 40 sese.043.001.02 PortfolioTransferCompletionV02 |
| PortfolioTransferConfirmation | [sese.013.001.12](../../../../messages/sese.013.001.12/index.md) | src-000096 file page 1106; 36 sese.013.001.12 PortfolioTransferConfirmationV12 |
| PortfolioTransferInstruction | [sese.012.001.12](../../../../messages/sese.012.001.12/index.md) | src-000096 file page 943; 35 sese.012.001.12 PortfolioTransferInstructionV12 |
| RequestForTransferStatusReport | [sese.009.001.09](../../../../messages/sese.009.001.09/index.md) | src-000096 file page 784; 32 sese.009.001.09 RequestForTransferStatusReportV09 |
| TransferInstructionStatusReport | [sese.011.001.10](../../../../messages/sese.011.001.10/index.md) | src-000096 file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0108.md)

- The source shaded “Individual Asset Transfers” band occurs after PortfolioTransferConfirmation and before PortfolioTransferCompletion. It is retained as a spanning note, not invented as an exchanged message. Fund units use transfer-out instruction/confirmation; cash uses a payment flow; liquidation requires redemption and payment flows (P775).
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)
- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
