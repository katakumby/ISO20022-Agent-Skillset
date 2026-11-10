---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p687-bulk"
title: "Subscription confirmation cancellation — bulk"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P671", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[671]"}, {"source_id": "src-000095", "paragraph_id": "P672", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[672]"}, {"source_id": "src-000095", "paragraph_id": "P673", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[673]"}, {"source_id": "src-000095", "paragraph_id": "P674", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[674]"}, {"source_id": "src-000095", "paragraph_id": "P675", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation "], "xml_path": "/w:document/w:body/w:p[675]"}, {"source_id": "src-000095", "paragraph_id": "P688", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Subscription ", "Bulk"], "xml_path": "/w:document/w:body/w:p[688]"}, {"source_id": "src-000095", "paragraph_id": "P689", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Subscription ", "Bulk"], "xml_path": "/w:document/w:body/w:p[689]"}, {"source_id": "src-000095", "paragraph_id": "P690", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Subscription ", "Bulk"], "xml_path": "/w:document/w:body/w:p[690]"}, {"source_id": "src-000095", "paragraph_id": "P691", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Subscription ", "Bulk"], "xml_path": "/w:document/w:body/w:p[691]"}, {"source_id": "src-000095", "paragraph_id": "P692", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Subscription ", "Bulk"], "xml_path": "/w:document/w:body/w:p[692]"}, {"source_id": "src-000095", "paragraph_id": "P693", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Subscription ", "Bulk"], "xml_path": "/w:document/w:body/w:p[693]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P694", "heading_path": ["BusinessTransactions", "Order Confirmation Cancellation ", "Subscription ", "Bulk"], "xml_path": "/w:document/w:body/w:p[694]", "figure_id": "fig-0097"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[8]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2523; 47 setr.007.001.05 SubscriptionBulkOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[10]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2766; 49 setr.009.001.05 SubscriptionBulkOrderConfirmationV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[11]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3001; 50 setr.010.001.05 SubscriptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[13]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3248; 52 setr.012.001.06 SubscriptionOrderConfirmationV06"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[17]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 4253; 59 setr.047.001.03 SubscriptionOrderConfirmationCancellationInstructionV03"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[18]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 4259; 60 setr.049.001.03 SubscriptionBulkOrderConfirmationCancellationInstructionV03"}]
message_ids: ["setr.007.001.05", "setr.009.001.05", "setr.010.001.05", "setr.012.001.06", "setr.047.001.03", "setr.049.001.03"]
message_families: ["setr.007", "setr.009", "setr.010", "setr.012", "setr.047", "setr.049"]
search_terms: ["Bulk", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "setr.007", "setr.009", "setr.010", "setr.012", "setr.047", "setr.049"]
limitations: ["The two instructing-party lifelines are separate instances of one functional role. Orders for the same financial instrument are grouped into a bulk order, and confirmation information is split according to the originating chain. The picture sends the individual confirmations to party 2 before party 1; that visible order is preserved.", "The cancellation narrative uses the phrase “confirmation amendment message” at P693, while its message names and picture are confirmation cancellation instructions. The wording is retained, not treated as a separate amendment message.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0097.md"]
updated: "2026-11-09"
---

# Subscription confirmation cancellation — bulk

## Purpose, trigger and outcome

Cancel a previously sent subscription confirmation.

**Trigger:** The executing party determines that the prior confirmation needs to be cancelled.

**Source-defined outcome:** The executing party sends the confirmation cancellation instruction; intermediaries relay it along the originating instruction chain where shown.

These statements are grounded in src-000095 P688–P693. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party 1](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Instructing Party 2](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party 1 | Intermediary | SubscriptionOrder |
| 2 | Instructing Party 2 | Intermediary | SubscriptionOrder |
| 3 | Intermediary | Executing Party | SubscriptionBulkOrder |
| 4 | Executing Party | Intermediary | SubscriptionBulkOrderConfirmation |
| 5 | Intermediary | Instructing Party 2 | SubscriptionOrderConfirmation |
| 6 | Intermediary | Instructing Party 1 | SubscriptionOrderConfirmation |
| 7 | Executing Party | Intermediary | SubscriptionBulkOrderConfirmationCancellationInstruction |
| 8 | Intermediary | Instructing Party 2 | SubscriptionOrderConfirmationCancellationInstruction |
| 9 | Intermediary | Instructing Party 1 | SubscriptionOrderConfirmationCancellationInstruction |


## Ordered narrative, conditions and alternatives

**src-000095 P688** — Instructing party 1 sends a SubscriptionOrder message to the intermediary party. Instructing party 2 sends a SubscriptionOrder message to the intermediary party. 

**src-000095 P689** — The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a SubscriptionBulkOrder message to the transfer agent. 

**src-000095 P690** — The executing party sends a SubscriptionBulkOrderConfirmation message to the intermediary party. 

**src-000095 P691** — The intermediary party splits up the confirmation according to the originating chain of instructions and sends a SubscriptionOrderConfirmation message to instructing party 1 and a SubscriptionOrderConfirmation message to instructing party 2. 

**src-000095 P692** — As the confirmation needs to be cancelled, a SubscriptionBulkOrderConfirmationCancellationInstruction message is sent by the executing party to inform the intermediary. 

**src-000095 P693** — In turn, the intermediary party splits up the confirmation amendment message according to the originating chain of instructions and sends a SubscriptionOrderConfirmationCancellationInstruction message to instructing party 1 and a SubscriptionOrderConfirmationCancellationInstruction message to instructing party 2.

### Common source context

**src-000095 P671** — This message flow section illustrates the use of the order confirmation cancellation messages in typical message sequencing scenarios. The different order confirmation cancellation instruction messages are sent by the executing party to the instructing party to cancel a previously sent subscription, redemption or order confirmation message. 

**src-000095 P672** — There may be one or more intermediaries in the transaction chain.

**src-000095 P673** — The order confirmation cancellation instruction message might be followed by an order confirmation message sent as an amendment (AmendmentIndicator set to 'true' or '1'), (see sequence diagrams related to order confirmation amendment).

**src-000095 P674** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P675** — The intermediary party is, for example, a distributor.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| SubscriptionBulkOrder | [setr.007.001.05](../../../../messages/setr.007.001.05/index.md) | src-000096 file page 2523; 47 setr.007.001.05 SubscriptionBulkOrderV05 |
| SubscriptionBulkOrderConfirmation | [setr.009.001.05](../../../../messages/setr.009.001.05/index.md) | src-000096 file page 2766; 49 setr.009.001.05 SubscriptionBulkOrderConfirmationV05 |
| SubscriptionBulkOrderConfirmationCancellationInstruction | [setr.049.001.03](../../../../messages/setr.049.001.03/index.md) | src-000096 file page 4259; 60 setr.049.001.03 SubscriptionBulkOrderConfirmationCancellationInstructionV03 |
| SubscriptionOrder | [setr.010.001.05](../../../../messages/setr.010.001.05/index.md) | src-000096 file page 3001; 50 setr.010.001.05 SubscriptionOrderV05 |
| SubscriptionOrderConfirmation | [setr.012.001.06](../../../../messages/setr.012.001.06/index.md) | src-000096 file page 3248; 52 setr.012.001.06 SubscriptionOrderConfirmationV06 |
| SubscriptionOrderConfirmationCancellationInstruction | [setr.047.001.03](../../../../messages/setr.047.001.03/index.md) | src-000096 file page 4253; 59 setr.047.001.03 SubscriptionOrderConfirmationCancellationInstructionV03 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0097.md)

- The two instructing-party lifelines are separate instances of one functional role. Orders for the same financial instrument are grouped into a bulk order, and confirmation information is split according to the originating chain. The picture sends the individual confirmations to party 2 before party 1; that visible order is preserved.
- The cancellation narrative uses the phrase “confirmation amendment message” at P693, while its message names and picture are confirmation cancellation instructions. The wording is retained, not treated as a separate amendment message.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
