---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p720-intermediary"
title: "Switch confirmation cancellation — intermediary"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P671", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[671]"}, {"source_id": "src-000095", "paragraph_id": "P672", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[672]"}, {"source_id": "src-000095", "paragraph_id": "P673", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[673]"}, {"source_id": "src-000095", "paragraph_id": "P674", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[674]"}, {"source_id": "src-000095", "paragraph_id": "P675", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[675]"}, {"source_id": "src-000095", "paragraph_id": "P721", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[721]"}, {"source_id": "src-000095", "paragraph_id": "P722", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[722]"}, {"source_id": "src-000095", "paragraph_id": "P723", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[723]"}, {"source_id": "src-000095", "paragraph_id": "P724", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[724]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P725", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[725]", "figure_id": "fig-0102"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-intermediary"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[14]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3487; 53 setr.013.001.05 SwitchOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[16]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3802; 55 setr.015.001.05 SwitchOrderConfirmationV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[21]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 4277; 63 setr.055.001.03 SwitchOrderConfirmationCancellationInstructionV03"}]
message_ids: ["setr.013.001.05", "setr.015.001.05", "setr.055.001.03"]
message_families: ["setr.013", "setr.015", "setr.055"]
search_terms: ["Intermediary", "Instructing Party", "Executing Party", "Intermediary", "setr.013", "setr.015", "setr.055"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0102.md"]
updated: "2026-11-09"
---

# Switch confirmation cancellation — intermediary

## Purpose, trigger and outcome

Cancel a previously sent switch confirmation.

**Trigger:** The executing party determines that the prior confirmation needs to be cancelled.

**Source-defined outcome:** The executing party sends the confirmation cancellation instruction; intermediaries relay it along the originating instruction chain where shown.

These statements are grounded in src-000095 P721–P724. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Intermediary | SwitchOrder |
| 2 | Intermediary | Executing Party | SwitchOrder |
| 3 | Executing Party | Intermediary | SwitchOrderConfirmation |
| 4 | Intermediary | Instructing Party | SwitchOrderConfirmation |
| 5 | Executing Party | Intermediary | SwitchOrderConfirmationCancellationInstruction |
| 6 | Intermediary | Instructing Party | SwitchOrderConfirmationCancellationInstruction |


## Ordered narrative, conditions and alternatives

**src-000095 P721** — The instructing party sends a SwitchOrder message to the intermediary party. 

**src-000095 P722** — The intermediary party sends the SwitchOrder message to the executing party. 

**src-000095 P723** — The executing party sends the SwitchOrderConfirmation message to the intermediary party. The intermediary party sends the SwitchOrderConfirmation message to the instructing party. 

**src-000095 P724** — As the confirmation needs to be cancelled, a SwitchOrderConfirmationCancellationInstruction message is sent by the executing party to inform the intermediary. In turn, the intermediary party sends a SwitchOrderConfirmationCancellationInstruction message to the instructing party. 

### Common source context

**src-000095 P671** — This message flow section illustrates the use of the order confirmation cancellation messages in typical message sequencing scenarios. The different order confirmation cancellation instruction messages are sent by the executing party to the instructing party to cancel a previously sent subscription, redemption or order confirmation message. 

**src-000095 P672** — There may be one or more intermediaries in the transaction chain.

**src-000095 P673** — The order confirmation cancellation instruction message might be followed by an order confirmation message sent as an amendment (AmendmentIndicator set to 'true' or '1'), (see sequence diagrams related to order confirmation amendment).

**src-000095 P674** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P675** — The intermediary party is, for example, a distributor.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| SwitchOrder | [setr.013.001.05](../../../../messages/setr.013.001.05/index.md) | src-000096 file page 3487; 53 setr.013.001.05 SwitchOrderV05 |
| SwitchOrderConfirmation | [setr.015.001.05](../../../../messages/setr.015.001.05/index.md) | src-000096 file page 3802; 55 setr.015.001.05 SwitchOrderConfirmationV05 |
| SwitchOrderConfirmationCancellationInstruction | [setr.055.001.03](../../../../messages/setr.055.001.03/index.md) | src-000096 file page 4277; 63 setr.055.001.03 SwitchOrderConfirmationCancellationInstructionV03 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0102.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
