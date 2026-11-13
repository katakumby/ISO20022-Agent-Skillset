---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p707-bulk"
title: "Redemption confirmation cancellation — bulk"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P671", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[671]"}, {"source_id": "src-000095", "paragraph_id": "P672", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[672]"}, {"source_id": "src-000095", "paragraph_id": "P673", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[673]"}, {"source_id": "src-000095", "paragraph_id": "P674", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[674]"}, {"source_id": "src-000095", "paragraph_id": "P675", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[675]"}, {"source_id": "src-000095", "paragraph_id": "P708", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Redemption ", "Bulk"], "xml_path": "/w:document/w:body/w:p[708]"}, {"source_id": "src-000095", "paragraph_id": "P709", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Redemption ", "Bulk"], "xml_path": "/w:document/w:body/w:p[709]"}, {"source_id": "src-000095", "paragraph_id": "P710", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Redemption ", "Bulk"], "xml_path": "/w:document/w:body/w:p[710]"}, {"source_id": "src-000095", "paragraph_id": "P711", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Redemption ", "Bulk"], "xml_path": "/w:document/w:body/w:p[711]"}, {"source_id": "src-000095", "paragraph_id": "P712", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Redemption ", "Bulk"], "xml_path": "/w:document/w:body/w:p[712]"}, {"source_id": "src-000095", "paragraph_id": "P713", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Redemption ", "Bulk"], "xml_path": "/w:document/w:body/w:p[713]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P714", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Redemption ", "Bulk"], "xml_path": "/w:document/w:body/w:p[714]", "figure_id": "fig-0100"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[2]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 1685; 41 setr.001.001.05 RedemptionBulkOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[4]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 1892; 43 setr.003.001.05 RedemptionBulkOrderConfirmationV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[5]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2101; 44 setr.004.001.05 RedemptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[7]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2310; 46 setr.006.001.06 RedemptionOrderConfirmationV06"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[19]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 4265; 61 setr.051.001.03 RedemptionOrderConfirmationCancellationInstructionV03"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[20]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 4271; 62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03"}]
message_ids: ["setr.001.001.05", "setr.003.001.05", "setr.004.001.05", "setr.006.001.06", "setr.051.001.03", "setr.053.001.03"]
message_families: ["setr.001", "setr.003", "setr.004", "setr.006", "setr.051", "setr.053"]
search_terms: ["Bulk", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "setr.001", "setr.003", "setr.004", "setr.006", "setr.051", "setr.053"]
limitations: ["The two instructing-party lifelines are separate instances of one functional role. Orders for the same financial instrument are grouped into a bulk order, and confirmation information is split according to the originating chain. The picture sends the individual confirmations to party 2 before party 1; that visible order is preserved.", "The cancellation narrative uses the phrase “confirmation amendment message” at P713, while its message names and picture are confirmation cancellation instructions. The wording is retained, not treated as a separate amendment message.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0100.md"]
updated: "2026-11-09"
---

# Redemption confirmation cancellation — bulk

## Purpose, trigger and outcome

Cancel a previously sent redemption confirmation.

**Trigger:** The executing party determines that the prior confirmation needs to be cancelled.

**Source-defined outcome:** The executing party sends the confirmation cancellation instruction; intermediaries relay it along the originating instruction chain where shown.

These statements are grounded in src-000095 P708–P713. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Instructing Party 2](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party 1 | Intermediary | RedemptionOrder |
| 2 | Instructing Party 2 | Intermediary | RedemptionOrder |
| 3 | Intermediary | Executing Party | RedemptionBulkOrder |
| 4 | Executing Party | Intermediary | RedemptionBulkOrderConfirmation |
| 5 | Intermediary | Instructing Party 2 | RedemptionOrderConfirmation |
| 6 | Intermediary | Instructing Party 1 | RedemptionOrderConfirmation |
| 7 | Executing Party | Intermediary | RedemptionBulkOrderConfirmationCancellationInstruction |
| 8 | Intermediary | Instructing Party 2 | RedemptionOrderConfirmationCancellationInstruction |
| 9 | Intermediary | Instructing Party 1 | RedemptionOrderConfirmationCancellationInstruction |


## Ordered narrative, conditions and alternatives

**src-000095 P708** — Instructing party 1 sends a RedemptionOrder message to the intermediary party. Instructing party 2 sends a RedemptionOrder message to the intermediary party. 

**src-000095 P709** — The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a RedemptionBulkOrder message to the transfer agent. 

**src-000095 P710** — The executing party sends a RedemptionBulkOrderConfirmation message to the intermediary party. 

**src-000095 P711** — The intermediary party splits up the confirmation according to the originating chain of instructions and sends a RedemptionOrderConfirmation message to instructing party 1 and a RedemptionOrderConfirmation message to instructing party 2. 

**src-000095 P712** — As the confirmation needs to be cancelled, a RedemptionBulkOrderConfirmationCancellationInstruction message is sent by the executing party to inform the intermediary. 

**src-000095 P713** — In turn, the intermediary party splits up the confirmation amendment message according to the originating chain of instructions and sends a RedemptionOrderConfirmationCancellationInstruction message to instructing party 1 and a RedemptionOrderConfirmationCancellationInstruction message to instructing party 2

### Common source context

**src-000095 P671** — This message flow section illustrates the use of the order confirmation cancellation messages in typical message sequencing scenarios. The different order confirmation cancellation instruction messages are sent by the executing party to the instructing party to cancel a previously sent subscription, redemption or order confirmation message. 

**src-000095 P672** — There may be one or more intermediaries in the transaction chain.

**src-000095 P673** — The order confirmation cancellation instruction message might be followed by an order confirmation message sent as an amendment (AmendmentIndicator set to 'true' or '1'), (see sequence diagrams related to order confirmation amendment).

**src-000095 P674** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P675** — The intermediary party is, for example, a distributor.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| RedemptionBulkOrder | [setr.001.001.05](../../../../messages/setr.001.001.05/index.md) | src-000096 file page 1685; 41 setr.001.001.05 RedemptionBulkOrderV05 |
| RedemptionBulkOrderConfirmation | [setr.003.001.05](../../../../messages/setr.003.001.05/index.md) | src-000096 file page 1892; 43 setr.003.001.05 RedemptionBulkOrderConfirmationV05 |
| RedemptionBulkOrderConfirmationCancellationInstruction | [setr.053.001.03](../../../../messages/setr.053.001.03/index.md) | src-000096 file page 4271; 62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03 |
| RedemptionOrder | [setr.004.001.05](../../../../messages/setr.004.001.05/index.md) | src-000096 file page 2101; 44 setr.004.001.05 RedemptionOrderV05 |
| RedemptionOrderConfirmation | [setr.006.001.06](../../../../messages/setr.006.001.06/index.md) | src-000096 file page 2310; 46 setr.006.001.06 RedemptionOrderConfirmationV06 |
| RedemptionOrderConfirmationCancellationInstruction | [setr.051.001.03](../../../../messages/setr.051.001.03/index.md) | src-000096 file page 4265; 61 setr.051.001.03 RedemptionOrderConfirmationCancellationInstructionV03 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0100.md)

- The two instructing-party lifelines are separate instances of one functional role. Orders for the same financial instrument are grouped into a bulk order, and confirmation information is split according to the originating chain. The picture sends the individual confirmations to party 2 before party 1; that visible order is preserved.
- The cancellation narrative uses the phrase “confirmation amendment message” at P713, while its message names and picture are confirmation cancellation instructions. The wording is retained, not treated as a separate amendment message.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
