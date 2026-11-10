---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p828-two-account-owners-direct-slt-market-practice"
title: "Two-owner asset transfer — SLT market practice"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P806", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[806]"}, {"source_id": "src-000095", "paragraph_id": "P807", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[807]"}, {"source_id": "src-000095", "paragraph_id": "P808", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[808]"}, {"source_id": "src-000095", "paragraph_id": "P809", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[809]"}, {"source_id": "src-000095", "paragraph_id": "P810", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[810]"}, {"source_id": "src-000095", "paragraph_id": "P829", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – SLT Market Practice"], "xml_path": "/w:document/w:body/w:p[829]"}, {"source_id": "src-000095", "paragraph_id": "P830", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – SLT Market Practice"], "xml_path": "/w:document/w:body/w:p[830]"}, {"source_id": "src-000095", "paragraph_id": "P831", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – SLT Market Practice"], "xml_path": "/w:document/w:body/w:p[831]"}, {"source_id": "src-000095", "paragraph_id": "P832", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – SLT Market Practice"], "xml_path": "/w:document/w:body/w:p[832]"}, {"source_id": "src-000095", "paragraph_id": "P833", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – SLT Market Practice"], "xml_path": "/w:document/w:body/w:p[833]"}, {"source_id": "src-000095", "paragraph_id": "P834", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – SLT Market Practice"], "xml_path": "/w:document/w:body/w:p[834]"}, {"source_id": "src-000095", "paragraph_id": "P835", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – SLT Market Practice"], "xml_path": "/w:document/w:body/w:p[835]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P836", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Direct – SLT Market Practice"], "xml_path": "/w:document/w:body/w:p[836]", "figure_id": "fig-0117"}]
participants: ["participant-src-000095-transfer-agent", "participant-src-000095-transferor", "participant-src-000095-transferee"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[4]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 519; 26 sese.003.001.10 TransferOutConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 608; 28 sese.005.001.10 TransferInInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[8]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 695; 30 sese.007.001.10 TransferInConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000096", "locator": "file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10"}]
message_ids: ["sese.001.001.10", "sese.003.001.10", "sese.005.001.10", "sese.007.001.10", "sese.011.001.10"]
message_families: ["sese.001", "sese.003", "sese.005", "sese.007", "sese.011"]
search_terms: ["Two Account Owners – Direct – SLT Market Practice", "Transfer Agent", "Transferor", "Transferee", "sese.001", "sese.003", "sese.005", "sese.007", "sese.011"]
limitations: ["The paired confirmations share the same vertical position in the source picture. Separate Mermaid rows are for legibility and do not establish an order between these two confirmations.", "The picture sends TransferInInstruction from the transferor’s bank to the transferee’s bank and the first status back; P829–P830 specify the opposite two directions. The original arrow directions remain visible. No inferred correction is applied.", "P830 and P832 specify Accepted (PACK), but the picture’s two status labels have no status qualifier.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-end-client", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent", "participant-src-000095-transferee", "participant-src-000095-transferee-s-bank-instructing-party", "participant-src-000095-transferor", "participant-src-000095-transferor-s-bank-instructing-party"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0117.md"]
updated: "2026-11-09"
---

# Two-owner asset transfer — SLT market practice

## Purpose, trigger and outcome

Coordinate a transfer between transferor’s bank, transferee’s bank and transfer agent under the source SLT market-practice scenario.

**Trigger:** P829 says the transferee’s bank instructs the transferor’s bank to deliver the end client’s instrument to the transferee bank account at the transfer agent.

**Source-defined outcome:** The transfer agent effects the transfer and confirms out to the transferor’s bank and in to the transferee’s bank.

These statements are grounded in src-000095 P829–P835. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Transferor’s Bank / Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-transferor-s-bank-instructing-party.md)
- [Transfer Agent / Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
- [Transferee’s Bank / Instructing Party 2](../../../../../../../shared/reference/participants/participant-src-000095-transferee-s-bank-instructing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Transferor’s Bank / Instructing Party 1 | Transferee’s Bank / Instructing Party 2 | TransferInInstruction |
| 2 | Transferee’s Bank / Instructing Party 2 | Transferor’s Bank / Instructing Party 1 | TransferInstructionStatusReport |
| 3 | Transferor’s Bank / Instructing Party 1 | Transfer Agent / Executing Party | TransferOutInstruction |
| 4 | Transfer Agent / Executing Party | Transferor’s Bank / Instructing Party 1 | TransferInstructionStatusReport |
| 5 | Transfer Agent / Executing Party | Transferor’s Bank / Instructing Party 1 | TransferOutConfirmation |
| 6 | Transfer Agent / Executing Party | Transferee’s Bank / Instructing Party 2 | TransferInConfirmation |


## Ordered narrative, conditions and alternatives

**src-000095 P829** — The transferee's bank sends a TransferInInstruction message to the transferor's bank. The message instructs the transferor's bank party to withdraw a quantity of financial instrument from the end client's account and deliver the financial instrument to the account of the transferee's bank at the transfer agent. 

**src-000095 P830** — The transferor replies with a TransferInstructionStatusReport message with the status Accepted (PACK).

**src-000095 P831** — The transferor's bank then actions the transfer by sending a Transfer Out Instruction message to the transfer agent.

**src-000095 P832** — The transfer agent replies with a TransferInstructionStatusReport message with the status Accepted (PACK).

**src-000095 P833** — The transfer agent carries out the transfer and sends:

**src-000095 P834** — a TransferOutConfirmation message to the transferor's bank 

**src-000095 P835** — a TransferInConfirmation message to the transferee's bank

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
| TransferInstructionStatusReport | [sese.011.001.10](../../../../messages/sese.011.001.10/index.md) | src-000096 file page 816; 34 sese.011.001.10 TransferInstructionStatusReportV10 |
| TransferOutConfirmation | [sese.003.001.10](../../../../messages/sese.003.001.10/index.md) | src-000096 file page 519; 26 sese.003.001.10 TransferOutConfirmationV10 |
| TransferOutInstruction | [sese.001.001.10](../../../../messages/sese.001.001.10/index.md) | src-000096 file page 433; 24 sese.001.001.10 TransferOutInstructionV10 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0117.md)

- The paired confirmations share the same vertical position in the source picture. Separate Mermaid rows are for legibility and do not establish an order between these two confirmations.
- The picture sends TransferInInstruction from the transferor’s bank to the transferee’s bank and the first status back; P829–P830 specify the opposite two directions. The original arrow directions remain visible. No inferred correction is applied.
- P830 and P832 specify Accepted (PACK), but the picture’s two status labels have no status qualifier.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [End Client](../../../../../../../shared/reference/participants/participant-src-000095-end-client.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)
- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transferee](../../../../../../../shared/reference/participants/participant-src-000095-transferee.md)
- [Transferor](../../../../../../../shared/reference/participants/participant-src-000095-transferor.md)
