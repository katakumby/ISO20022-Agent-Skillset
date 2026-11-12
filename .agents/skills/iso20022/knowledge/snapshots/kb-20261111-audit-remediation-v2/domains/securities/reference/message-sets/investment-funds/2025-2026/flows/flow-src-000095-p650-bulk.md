---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p650-bulk"
title: "Redemption confirmation amendment — bulk"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P613", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[613]"}, {"source_id": "src-000095", "paragraph_id": "P614", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[614]"}, {"source_id": "src-000095", "paragraph_id": "P615", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[615]"}, {"source_id": "src-000095", "paragraph_id": "P616", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[616]"}, {"source_id": "src-000095", "paragraph_id": "P617", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[617]"}, {"source_id": "src-000095", "paragraph_id": "P651", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Bulk "], "xml_path": "/w:document/w:body/w:p[651]"}, {"source_id": "src-000095", "paragraph_id": "P652", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Bulk "], "xml_path": "/w:document/w:body/w:p[652]"}, {"source_id": "src-000095", "paragraph_id": "P653", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Bulk "], "xml_path": "/w:document/w:body/w:p[653]"}, {"source_id": "src-000095", "paragraph_id": "P654", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Bulk "], "xml_path": "/w:document/w:body/w:p[654]"}, {"source_id": "src-000095", "paragraph_id": "P655", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Bulk "], "xml_path": "/w:document/w:body/w:p[655]"}, {"source_id": "src-000095", "paragraph_id": "P656", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Bulk "], "xml_path": "/w:document/w:body/w:p[656]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P657", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Bulk "], "xml_path": "/w:document/w:body/w:p[657]", "figure_id": "fig-0092"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-transfer-agent", "participant-src-000095-intermediary"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[2]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 1685; 41 setr.001.001.05 RedemptionBulkOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[4]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 1892; 43 setr.003.001.05 RedemptionBulkOrderConfirmationV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[5]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2101; 44 setr.004.001.05 RedemptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[7]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2310; 46 setr.006.001.06 RedemptionOrderConfirmationV06"}]
message_ids: ["setr.001.001.05", "setr.003.001.05", "setr.004.001.05", "setr.006.001.06"]
message_families: ["setr.001", "setr.003", "setr.004", "setr.006"]
search_terms: ["Bulk", "Instructing Party", "Executing Party", "Transfer Agent", "Intermediary", "setr.001", "setr.003", "setr.004", "setr.006"]
limitations: ["The two instructing-party lifelines are separate instances of one functional role. Orders for the same financial instrument are grouped into a bulk order, and confirmation information is split according to the originating chain. The picture sends the individual confirmations to party 2 before party 1; that visible order is preserved.", "The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0092.md"]
updated: "2026-11-09"
---

# Redemption confirmation amendment — bulk

## Purpose, trigger and outcome

Amend details of a previously sent redemption confirmation.

**Trigger:** Details of the previously sent confirmation need to be amended.

**Source-defined outcome:** The executing party sends another confirmation with AmendmentIndicator true or 1; intermediaries relay amended confirmations along the originating instruction chain where shown.

These statements are grounded in src-000095 P651–P656. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

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
| 7 | Executing Party | Intermediary | RedemptionBulkOrderConfirmation &lt;AmdmntInd&gt; true |
| 8 | Intermediary | Instructing Party 2 | RedemptionOrderConfirmation &lt;AmdmntInd&gt; true |
| 9 | Intermediary | Instructing Party 1 | RedemptionOrderConfirmation &lt;AmdmntInd&gt; true |


## Ordered narrative, conditions and alternatives

**src-000095 P651** — Instructing party 1 sends a RedemptionOrder message to the intermediary party. Instructing party 2 sends a RedemptionOrder message to the intermediary party. 

**src-000095 P652** — The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a RedemptionBulkOrder message to the transfer agent. 

**src-000095 P653** — The executing party sends a RedemptionBulkOrderConfirmation message to the intermediary party. 

**src-000095 P654** — The intermediary party splits up the confirmation according to the originating chain of instructions and sends a RedemptionOrderConfirmation message to instructing party 1 and a RedemptionOrderConfirmation message to instructing party 2. 

**src-000095 P655** — As an amendment has to be made to the RedemptionBulkOrderConfirmation message details, another RedemptionBulkOrderConfirmation message is sent by the executing party to inform the intermediary about the amended details, with the AmendmentIndicator set to 'true' or '1'.. 

**src-000095 P656** — In turn, the intermediary party splits up the confirmation message according to the originating chain of instructions and sends a RedemptionOrderConfirmation message to instructing party 1 with the AmendmentIndicator set to 'true' or '1' and a RedemptionOrderConfirmation message to instructing party 2 with the AmendmentIndicator set to 'true' or '1'.

### Common source context

**src-000095 P613** — This message flow section illustrates the use of the messages for the amendment of an order confirmation in typical message sequencing scenarios.

**src-000095 P614** — More than one message detail can be amended. The order confirmation, when sent as an amendment (AmendmentIndicator set to 'true' or '1'), might follow an order confirmation cancellation instruction message, if, in the order confirmation cancellation instruction message, the AmendmentIndicator is set to 'true' or '1' (see sequence diagrams related to order confirmation cancellation instruction messages).

**src-000095 P615** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P616** — The intermediary party is, for example, a distributor.

**src-000095 P617** — There may be one or more intermediaries in the transaction chain

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| RedemptionBulkOrder | [setr.001.001.05](../../../../messages/setr.001.001.05/index.md) | src-000096 file page 1685; 41 setr.001.001.05 RedemptionBulkOrderV05 |
| RedemptionBulkOrderConfirmation | [setr.003.001.05](../../../../messages/setr.003.001.05/index.md) | src-000096 file page 1892; 43 setr.003.001.05 RedemptionBulkOrderConfirmationV05 |
| RedemptionOrder | [setr.004.001.05](../../../../messages/setr.004.001.05/index.md) | src-000096 file page 2101; 44 setr.004.001.05 RedemptionOrderV05 |
| RedemptionOrderConfirmation | [setr.006.001.06](../../../../messages/setr.006.001.06/index.md) | src-000096 file page 2310; 46 setr.006.001.06 RedemptionOrderConfirmationV06 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0092.md)

- The two instructing-party lifelines are separate instances of one functional role. Orders for the same financial instrument are grouped into a bulk order, and confirmation information is split according to the originating chain. The picture sends the individual confirmations to party 2 before party 1; that visible order is preserved.
- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
