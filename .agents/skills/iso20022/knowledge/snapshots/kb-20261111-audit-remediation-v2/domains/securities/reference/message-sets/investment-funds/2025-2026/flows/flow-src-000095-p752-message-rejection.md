---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p752-message-rejection"
title: "Transfer status request rejected for an unknown reference"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P753", "heading_path": ["BusinessTransactions", "Message Rejection"], "xml_path": "/w:document/w:body/w:p[753]"}, {"source_id": "src-000095", "paragraph_id": "P754", "heading_path": ["BusinessTransactions", "Message Rejection"], "xml_path": "/w:document/w:body/w:p[754]"}, {"source_id": "src-000095", "paragraph_id": "P755", "heading_path": ["BusinessTransactions", "Message Rejection"], "xml_path": "/w:document/w:body/w:p[755]"}, {"source_id": "src-000095", "paragraph_id": "P756", "heading_path": ["BusinessTransactions", "Message Rejection"], "xml_path": "/w:document/w:body/w:p[756]"}, {"source_id": "src-000095", "paragraph_id": "P757", "heading_path": ["BusinessTransactions", "Message Rejection"], "xml_path": "/w:document/w:body/w:p[757]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P758", "heading_path": ["BusinessTransactions", "Message Rejection"], "xml_path": "/w:document/w:body/w:p[758]", "figure_id": "fig-0106"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 608; 28 sese.005.001.10 TransferInInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[2]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 784; 32 sese.009.001.09 RequestForTransferStatusReportV09"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10"}, {"source_id": "src-000096", "locator": "file page 371; 17 semt.001.001.03 SecuritiesMessageRejectionV03"}]
message_ids: ["semt.001.001.03", "sese.001.001.10", "sese.005.001.10", "sese.009.001.09"]
message_families: ["semt.001", "sese.001", "sese.005", "sese.009", "sese.011"]
search_terms: ["Message Rejection", "Instructing Party", "Executing Party", "semt.001", "sese.001", "sese.005", "sese.009", "sese.011"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0106.md"]
updated: "2026-11-09"
---

# Transfer status request rejected for an unknown reference

## Purpose, trigger and outcome

Reject a transfer status request whose transfer reference cannot be recognised.

**Trigger:** The instructing party misquotes the reference of its prior transfer out instruction.

**Source-defined outcome:** The executing party returns SecuritiesMessageRejection with UnknownOrInvalidReference. The narrative permits an equivalent transfer-in scenario.

These statements are grounded in src-000095 P753–P757. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | TransferOutInstruction |
| 2 | Instructing Party | Executing Party | RequestForTransferStatusReport |
| 3 | Executing Party | Instructing Party | SecuritiesMessageRejection |


## Ordered narrative, conditions and alternatives

**src-000095 P753** — The SecuritiesMessageRejection message can be used to reject any securities message. One example of the use of the SecuritiesMessageRejection is illustrated below.

**src-000095 P754** — An instructing party sends a TransferOutInstruction message to the executing party. 

**src-000095 P755** — Subsequently, the instructing party sends a RequestForTransferStatusReport message to the executing party but, for example, it misquotes the message reference of the TransferOutInstruction message. 

**src-000095 P756** — The executing party cannot process the RequestForTransferStatusReport message because it does not know to which transfer instruction the instructing party is referring. Therefore, the executing party replies with a SecuritiesMessageRejection message with the reason 'UnknownOrInvalidReference'. 

**src-000095 P757** — The message flow works in a similar way when a TransferInInstruction is sent and a transfer instruction status report is subsequently requested with, for example, a misquoted reference.

### Common source context

**src-000095 P753** — The SecuritiesMessageRejection message can be used to reject any securities message. One example of the use of the SecuritiesMessageRejection is illustrated below.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| RequestForTransferStatusReport | [sese.009.001.09](../../../../messages/sese.009.001.09/index.md) | src-000096 file page 784; 32 sese.009.001.09 RequestForTransferStatusReportV09 |
| SecuritiesMessageRejection | [semt.001.001.03](../../../../messages/semt.001.001.03/index.md) | src-000096 file page 371; 17 semt.001.001.03 SecuritiesMessageRejectionV03 |
| TransferInInstruction | [sese.005.001.10](../../../../messages/sese.005.001.10/index.md) | src-000096 file page 608; 28 sese.005.001.10 TransferInInstructionV10 |
| TransferOutInstruction | [sese.001.001.10](../../../../messages/sese.001.001.10/index.md) | src-000096 file page 433; 24 sese.001.001.10 TransferOutInstructionV10 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0106.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.
