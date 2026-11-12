---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p837-two-account-owners-intermediary-double-leg"
title: "Two-owner asset transfer — intermediary double leg"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P806", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[806]"}, {"source_id": "src-000095", "paragraph_id": "P807", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[807]"}, {"source_id": "src-000095", "paragraph_id": "P808", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[808]"}, {"source_id": "src-000095", "paragraph_id": "P809", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[809]"}, {"source_id": "src-000095", "paragraph_id": "P810", "heading_path": ["BusinessTransactions", "Individual Asset Transfer"], "xml_path": "/w:document/w:body/w:p[810]"}, {"source_id": "src-000095", "paragraph_id": "P838", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Intermediary - Double Leg"], "xml_path": "/w:document/w:body/w:p[838]"}, {"source_id": "src-000095", "paragraph_id": "P839", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Intermediary - Double Leg"], "xml_path": "/w:document/w:body/w:p[839]"}, {"source_id": "src-000095", "paragraph_id": "P840", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Intermediary - Double Leg"], "xml_path": "/w:document/w:body/w:p[840]"}, {"source_id": "src-000095", "paragraph_id": "P841", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Intermediary - Double Leg"], "xml_path": "/w:document/w:body/w:p[841]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P842", "heading_path": ["BusinessTransactions", "Individual Asset Transfer", "Two Account Owners – Intermediary - Double Leg"], "xml_path": "/w:document/w:body/w:p[842]", "figure_id": "fig-0118"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-intermediary"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[2]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 433; 24 sese.001.001.10 TransferOutInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[4]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 519; 26 sese.003.001.10 TransferOutConfirmationV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 608; 28 sese.005.001.10 TransferInInstructionV10"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Portfolio Transfer Management"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[8]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000096", "locator": "file page 695; 30 sese.007.001.10 TransferInConfirmationV10"}]
message_ids: ["sese.001.001.10", "sese.003.001.10", "sese.005.001.10", "sese.007.001.10"]
message_families: ["sese.001", "sese.003", "sese.005", "sese.007"]
search_terms: ["Two Account Owners – Intermediary - Double Leg", "Instructing Party", "Executing Party", "Intermediary", "sese.001", "sese.003", "sese.005", "sese.007"]
limitations: ["The source draws the two sides of each relay stage at the same height, and P840 says the incoming leg is instructed at the same time. Mermaid’s separate rows do not impose ordering between the two sides.", "Intermediary 1 and 2 are separate instances of the same source-defined functional role; the narrative specifies their account relationships without permanently assigning that role to one institution.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0118.md"]
updated: "2026-11-09"
---

# Two-owner asset transfer — intermediary double leg

## Purpose, trigger and outcome

Transfer assets between two instructing parties through separate intermediaries and a common executing party.

**Trigger:** Each instructing party instructs its own intermediary; each intermediary relays its transfer leg to the executing party.

**Source-defined outcome:** Out and in confirmations return along their respective instruction chains.

These statements are grounded in src-000095 P838–P841. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Intermediary 1](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)
- [Intermediary 2](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [Instructing Party 2](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party 1 | Intermediary 1 | TransferOutInstruction |
| 2 | Instructing Party 2 | Intermediary 2 | TransferInInstruction |
| 3 | Intermediary 1 | Executing Party | TransferOutInstruction |
| 4 | Intermediary 2 | Executing Party | TransferInInstruction |
| 5 | Executing Party | Intermediary 1 | TransferOutConfirmation |
| 6 | Executing Party | Intermediary 2 | TransferInConfirmation |
| 7 | Intermediary 1 | Instructing Party 1 | TransferOutConfirmation |
| 8 | Intermediary 2 | Instructing Party 2 | TransferInConfirmation |


## Ordered narrative, conditions and alternatives

**src-000095 P838** — Instructing party 1 sends a TransferOutInstruction message to intermediary 1. 

**src-000095 P839** — The message requests intermediary 1 to withdraw a quantity of financial instrument from the account of instructing party 1 and deliver the financial instrument to instructing party 2, which has its account at intermediary 2. Intermediary 1, in turn, has an account at the executing party and sends a TransferOutInstruction message to the executing party. 

**src-000095 P840** — At the same time, instructing party 2 sends a TransferInInstruction message to intermediary 2. The message requests intermediary 2 to receive the financial instrument from instructing party 1, via intermediary 1, via the executing party. Intermediary 2, in turn, sends a TransferInInstruction message to the executing party. 

**src-000095 P841** — The executing party sends a TransferOutConfirmation message to intermediary 1 to confirm the delivery. Intermediary 1, in turn, sends a TransferOutConfirmation message to instructing party 1 to confirm the delivery. The executing party sends a TransferInConfirmation message to intermediary 2 to confirm the receipt. Intermediary 2, in turn, sends a TransferInConfirmation message to instructing party 2 to confirm the receipt.

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

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0118.md)

- The source draws the two sides of each relay stage at the same height, and P840 says the incoming leg is instructed at the same time. Mermaid’s separate rows do not impose ordering between the two sides.
- Intermediary 1 and 2 are separate instances of the same source-defined functional role; the narrative specifies their account relationships without permanently assigning that role to one institution.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
