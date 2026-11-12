---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p639-direct"
title: "Redemption confirmation amendment — direct"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P613", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[613]"}, {"source_id": "src-000095", "paragraph_id": "P614", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[614]"}, {"source_id": "src-000095", "paragraph_id": "P615", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[615]"}, {"source_id": "src-000095", "paragraph_id": "P616", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[616]"}, {"source_id": "src-000095", "paragraph_id": "P617", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[617]"}, {"source_id": "src-000095", "paragraph_id": "P640", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Direct "], "xml_path": "/w:document/w:body/w:p[640]"}, {"source_id": "src-000095", "paragraph_id": "P641", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Direct "], "xml_path": "/w:document/w:body/w:p[641]"}, {"source_id": "src-000095", "paragraph_id": "P642", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Direct "], "xml_path": "/w:document/w:body/w:p[642]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P643", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Redemption ", "Direct "], "xml_path": "/w:document/w:body/w:p[643]", "figure_id": "fig-0090"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[5]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2101; 44 setr.004.001.05 RedemptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[7]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 2310; 46 setr.006.001.06 RedemptionOrderConfirmationV06"}]
message_ids: ["setr.004.001.05", "setr.006.001.06"]
message_families: ["setr.004", "setr.006"]
search_terms: ["Direct", "Instructing Party", "Executing Party", "setr.004", "setr.006"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0090.md"]
updated: "2026-11-09"
---

# Redemption confirmation amendment — direct

## Purpose, trigger and outcome

Amend details of a previously sent redemption confirmation.

**Trigger:** Details of the previously sent confirmation need to be amended.

**Source-defined outcome:** The executing party sends another confirmation with AmendmentIndicator true or 1; intermediaries relay amended confirmations along the originating instruction chain where shown.

These statements are grounded in src-000095 P640–P642. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | RedemptionOrder |
| 2 | Executing Party | Instructing Party | RedemptionOrderConfirmation |
| 3 | Executing Party | Instructing Party | RedemptionOrderConfirmation &lt;AmdmntInd&gt; true |


## Ordered narrative, conditions and alternatives

**src-000095 P640** — An instructing party sends a RedemptionOrder message to the executing party. 

**src-000095 P641** — To confirm execution of the order, the executing party sends a RedemptionOrderConfirmation message to the instructing party. 

**src-000095 P642** — As an amendment has to be made to the RedemptionOrderConfirmation message details, another RedemptionOrderConfirmation message is sent with the AmendmentIndicator set to 'true' or '1' 

### Common source context

**src-000095 P613** — This message flow section illustrates the use of the messages for the amendment of an order confirmation in typical message sequencing scenarios.

**src-000095 P614** — More than one message detail can be amended. The order confirmation, when sent as an amendment (AmendmentIndicator set to 'true' or '1'), might follow an order confirmation cancellation instruction message, if, in the order confirmation cancellation instruction message, the AmendmentIndicator is set to 'true' or '1' (see sequence diagrams related to order confirmation cancellation instruction messages).

**src-000095 P615** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P616** — The intermediary party is, for example, a distributor.

**src-000095 P617** — There may be one or more intermediaries in the transaction chain

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| RedemptionOrder | [setr.004.001.05](../../../../messages/setr.004.001.05/index.md) | src-000096 file page 2101; 44 setr.004.001.05 RedemptionOrderV05 |
| RedemptionOrderConfirmation | [setr.006.001.06](../../../../messages/setr.006.001.06/index.md) | src-000096 file page 2310; 46 setr.006.001.06 RedemptionOrderConfirmationV06 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0090.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md)
- [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
