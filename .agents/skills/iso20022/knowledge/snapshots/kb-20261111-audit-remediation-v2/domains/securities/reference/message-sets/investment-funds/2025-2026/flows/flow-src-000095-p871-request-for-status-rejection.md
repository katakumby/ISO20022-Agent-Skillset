---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p871-request-for-status-rejection"
title: "Transfer instruction status query rejected"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P862", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "xml_path": "/w:document/w:body/w:p[862]"}, {"source_id": "src-000095", "paragraph_id": "P863", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "xml_path": "/w:document/w:body/w:p[863]"}, {"source_id": "src-000095", "paragraph_id": "P864", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "xml_path": "/w:document/w:body/w:p[864]"}, {"source_id": "src-000095", "paragraph_id": "P865", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "xml_path": "/w:document/w:body/w:p[865]"}, {"source_id": "src-000095", "paragraph_id": "P866", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status "], "xml_path": "/w:document/w:body/w:p[866]"}, {"source_id": "src-000095", "paragraph_id": "P872", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Request for Status Rejection"], "xml_path": "/w:document/w:body/w:p[872]"}, {"source_id": "src-000095", "paragraph_id": "P873", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Request for Status Rejection"], "xml_path": "/w:document/w:body/w:p[873]"}, {"source_id": "src-000095", "paragraph_id": "P874", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Request for Status Rejection"], "xml_path": "/w:document/w:body/w:p[874]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P875", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Request for Transfer Status and Transfer Status ", "Request for Status Rejection"], "xml_path": "/w:document/w:body/w:p[875]", "figure_id": "fig-0124"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 608; 28 sese.005.001.10 TransferInInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[2]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 784; 32 sese.009.001.09 RequestForTransferStatusReportV09"}]
message_ids: ["semt.001.001.03", "sese.001.001.10", "sese.005.001.10", "sese.009.001.09", "sese.010.001.07", "sese.011.001.10"]
message_families: ["sese.001", "sese.005", "sese.009"]
search_terms: ["Request for Status Rejection", "Instructing Party", "Executing Party", "Transfer Agent", "sese.001", "sese.005", "sese.009"]
limitations: ["P873 uses investor and transfer agent as scenario participants; the picture uses functional Instructing Party and Executing Party. This is a source-described example, not a universal institutional equivalence.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0124.md"]
updated: "2026-11-09"
---

# Transfer instruction status query rejected

## Purpose, trigger and outcome

Reject a transfer status query whose referenced transfer cannot be identified.

**Trigger:** The requesting investor misquotes the transfer instruction reference.

**Source-defined outcome:** P873 says the transfer agent replies with a Rejection and UnknownOrInvalidReference; the picture names SecuritiesMessageRejection. The same flow applies to transfer-in.

These statements are grounded in src-000095 P872–P874. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | TransferOutInstruction |
| 2 | Instructing Party | Executing Party | RequestForTransferStatusReport |
| 3 | Executing Party | Instructing Party | SecuritiesMessageRejection |


## Ordered narrative, conditions and alternatives

**src-000095 P872** — An instructing party sends a transfer instruction, for example, a TransferOutInstruction message, to the executing party.

**src-000095 P873** — Subsequently, the investor sends a RequestForTransferStatusReport message but, for example, it misquotes the message reference of the TransferOutInstruction message. The transfer agent cannot process the RequestForTransferStatusReport message because it does not know to which transfer instruction the investor is referring. Therefore, the transfer agent replies with a Rejection message with the reason 'UnknownOrInvalidReference'. 

**src-000095 P874** — The message flow works in a similar way when a TransferInInstruction message is sent.

### Common source context

**src-000095 P862** — This message flow section illustrates the use of the transfer status messages in typical message sequencing scenarios. 

**src-000095 P863** — The RequestForTransferStatusReport message is sent by an instructing party to the executing party to request the status of a transfer instruction. The response to a RequestForTransferStatusReport is a TransferInstructionStatusReport or a TransferCancellationStatusReport message.

**src-000095 P864** — The TransferInstructionStatusReport is sent by the executing party to the instructing party. There may be one or more intermediaries in the transaction chain.

**src-000095 P865** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P866** — If the Service Level Agreement (SLA) allows it, a TransferInstructionStatusReport or a TransferCancellationStatusReport message may be sent by the executing party to the instructing party even though no RequestForTransferStatusReport message has been received by the executing party.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| RequestForTransferStatusReport | [sese.009.001.09](../../../../messages/sese.009.001.09/index.md) | src-000096 file page 784; 32 sese.009.001.09 RequestForTransferStatusReportV09 |
| SecuritiesMessageRejection | [semt.001.001.03](../../../../messages/semt.001.001.03/index.md) | src-000096 file page 371; 17 semt.001.001.03 SecuritiesMessageRejectionV03 |
| TransferCancellationStatusReport | [sese.010.001.07](../../../../messages/sese.010.001.07/index.md) | src-000096 file page 809; 33 sese.010.001.07 TransferCancellationStatusReportV07 |
| TransferInInstruction | [sese.005.001.10](../../../../messages/sese.005.001.10/index.md) | src-000096 file page 608; 28 sese.005.001.10 TransferInInstructionV10 |
| TransferInstructionStatusReport | [sese.011.001.10](../../../../messages/sese.011.001.10/index.md) | src-000096 file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10 |
| TransferOutInstruction | [sese.001.001.10](../../../../messages/sese.001.001.10/index.md) | src-000096 file page 433; 24 sese.001.001.10 TransferOutInstructionV10 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0124.md)

- P873 uses investor and transfer agent as scenario participants; the picture uses functional Instructing Party and Executing Party. This is a source-described example, not a universal institutional equivalence.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
