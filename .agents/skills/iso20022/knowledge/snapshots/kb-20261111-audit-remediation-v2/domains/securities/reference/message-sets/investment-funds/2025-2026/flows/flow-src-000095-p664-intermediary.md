---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p664-intermediary"
title: "Switch confirmation amendment — intermediary"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P613", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[613]"}, {"source_id": "src-000095", "paragraph_id": "P614", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[614]"}, {"source_id": "src-000095", "paragraph_id": "P615", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[615]"}, {"source_id": "src-000095", "paragraph_id": "P616", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[616]"}, {"source_id": "src-000095", "paragraph_id": "P617", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment "], "xml_path": "/w:document/w:body/w:p[617]"}, {"source_id": "src-000095", "paragraph_id": "P665", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[665]"}, {"source_id": "src-000095", "paragraph_id": "P666", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[666]"}, {"source_id": "src-000095", "paragraph_id": "P667", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[667]"}, {"source_id": "src-000095", "paragraph_id": "P668", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[668]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P669", "heading_path": ["BusinessTransactions", "Order Confirmation Amendment ", "Switch ", "Intermediary"], "xml_path": "/w:document/w:body/w:p[669]", "figure_id": "fig-0094"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party", "participant-src-000095-intermediary"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[14]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3487; 53 setr.013.001.05 SwitchOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[16]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3802; 55 setr.015.001.05 SwitchOrderConfirmationV05"}]
message_ids: ["setr.013.001.05", "setr.015.001.05"]
message_families: ["setr.013", "setr.015"]
search_terms: ["Intermediary", "Instructing Party", "Executing Party", "Intermediary", "setr.013", "setr.015"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0094.md"]
updated: "2026-11-09"
---

# Switch confirmation amendment — intermediary

## Purpose, trigger and outcome

Amend details of a previously sent switch confirmation.

**Trigger:** Details of the previously sent confirmation need to be amended.

**Source-defined outcome:** The executing party sends another confirmation with AmendmentIndicator true or 1; intermediaries relay amended confirmations along the originating instruction chain where shown.

These statements are grounded in src-000095 P665–P668. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

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
| 5 | Executing Party | Intermediary | SwitchOrderConfirmation &lt;AmdmntInd&gt; true |
| 6 | Intermediary | Instructing Party | SwitchOrderConfirmation &lt;AmdmntInd&gt; true |


## Ordered narrative, conditions and alternatives

**src-000095 P665** — The instructing party sends a SwitchOrder message to the intermediary party. In turn, the intermediary party sends the SwitchOrder message to the executing party. 

**src-000095 P666** — The executing party sends the SwitchOrderConfirmation message to the intermediary party. The intermediary party sends the SwitchOrderConfirmation message to the instructing party. 

**src-000095 P667** — As an amendment has to be made to the SwitchOrderConfirmation message details, another SwitchOrderConfirmation message is sent by the executing party to inform the intermediary about the amended details, with the AmendmentIndicator set to 'true' or '1'. 

**src-000095 P668** — In turn, the intermediary party sends a SwitchOrderConfirmation message to the instructing party, with the AmendmentIndicator set to 'true' or '1'. 

### Common source context

**src-000095 P613** — This message flow section illustrates the use of the messages for the amendment of an order confirmation in typical message sequencing scenarios.

**src-000095 P614** — More than one message detail can be amended. The order confirmation, when sent as an amendment (AmendmentIndicator set to 'true' or '1'), might follow an order confirmation cancellation instruction message, if, in the order confirmation cancellation instruction message, the AmendmentIndicator is set to 'true' or '1' (see sequence diagrams related to order confirmation cancellation instruction messages).

**src-000095 P615** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P616** — The intermediary party is, for example, a distributor.

**src-000095 P617** — There may be one or more intermediaries in the transaction chain

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| SwitchOrder | [setr.013.001.05](../../../../messages/setr.013.001.05/index.md) | src-000096 file page 3487; 53 setr.013.001.05 SwitchOrderV05 |
| SwitchOrderConfirmation | [setr.015.001.05](../../../../messages/setr.015.001.05/index.md) | src-000096 file page 3802; 55 setr.015.001.05 SwitchOrderConfirmationV05 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0094.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
