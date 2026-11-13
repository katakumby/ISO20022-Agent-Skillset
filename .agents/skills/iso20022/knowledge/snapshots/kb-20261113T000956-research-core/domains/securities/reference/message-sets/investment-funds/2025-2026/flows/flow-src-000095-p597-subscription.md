---
template: false
document_kind: "business-flow"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_sets: ["investment-funds"]
flow_id: "flow-src-000095-p597-subscription"
title: "Subscription confirmation rejected by instructing party"
source_locations: [{"source_id": "src-000095", "paragraph_id": "P593", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting "], "xml_path": "/w:document/w:body/w:p[593]"}, {"source_id": "src-000095", "paragraph_id": "P594", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting "], "xml_path": "/w:document/w:body/w:p[594]"}, {"source_id": "src-000095", "paragraph_id": "P595", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting "], "xml_path": "/w:document/w:body/w:p[595]"}, {"source_id": "src-000095", "paragraph_id": "P596", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting "], "xml_path": "/w:document/w:body/w:p[596]"}, {"source_id": "src-000095", "paragraph_id": "P598", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting ", "Subscription "], "xml_path": "/w:document/w:body/w:p[598]"}, {"source_id": "src-000095", "paragraph_id": "P599", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting ", "Subscription "], "xml_path": "/w:document/w:body/w:p[599]"}, {"source_id": "src-000095", "paragraph_id": "P600", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting ", "Subscription "], "xml_path": "/w:document/w:body/w:p[600]"}, {"source_id": "src-000095", "locator": "direct-body paragraph P601", "heading_path": ["BusinessTransactions", "Order Confirmation Status Reporting ", "Subscription "], "xml_path": "/w:document/w:body/w:p[601]", "figure_id": "fig-0084"}]
participants: ["participant-src-000095-instructing-party", "participant-src-000095-executing-party"]
message_mapping_evidence: [{"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[11]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3001; 50 setr.010.001.05 SubscriptionOrderV05"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[13]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000096", "locator": "file page 3248; 52 setr.012.001.06 SubscriptionOrderConfirmationV06"}, {"source_id": "src-000095", "heading_path": ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Groups", "Order and Confirmation Status Reporting"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[5]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000096", "locator": "file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03"}]
message_ids: ["setr.010.001.05", "setr.012.001.06", "setr.057.001.03"]
message_families: ["setr.010", "setr.012", "setr.057"]
search_terms: ["Subscription", "Instructing Party", "Executing Party", "setr.010", "setr.012", "setr.057"]
limitations: ["The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.", "Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.", "The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit."]
manual_curated: true
participant_ids: ["participant-src-000095-distributor", "participant-src-000095-executing-party", "participant-src-000095-instructing-party", "participant-src-000095-intermediary", "participant-src-000095-investment-manager", "participant-src-000095-transfer-agent"]
diagram_paths: ["domains/securities/reference/message-sets/investment-funds/2025-2026/diagrams/funds-sequences/fig-0084.md"]
updated: "2026-11-09"
---

# Subscription confirmation rejected by instructing party

## Purpose, trigger and outcome

Report rejection of a subscription confirmation because its order reference is unrecognised.

**Trigger:** After order execution, the executing party sends the subscription confirmation with an order reference that the instructing party does not recognise.

**Source-defined outcome:** The instructing party sends OrderConfirmationStatusReport indicating that the confirmation is rejected (P600).

These statements are grounded in src-000095 P598–P600. The common conditions below remain applicable; no additional precondition or SLA deadline is inferred.

## Participants and responsibilities

- [Instructing Party](../../../../../../../shared/reference/participants/participant-src-000095-instructing-party.md)
- [Executing Party](../../../../../../../shared/reference/participants/participant-src-000095-executing-party.md)

| Picture step | Sender / responsible transmitting participant | Receiver | Literal message label |
| --- | --- | --- | --- |
| 1 | Instructing Party | Executing Party | SubscriptionOrder |
| 2 | Executing Party | Instructing Party | SubscriptionOrderConfirmation |
| 3 | Instructing Party | Executing Party | OrderConfirmationStatusReport |


## Ordered narrative, conditions and alternatives

**src-000095 P598** — The instructing party sends a SubscriptionOrder message to the executing party. 

**src-000095 P599** — After execution of the order, the executing party sends a SubscriptionOrderConfirmation message to the instructing party.

**src-000095 P600** — As the executing party has quoted an order reference that is not recognised, the instructing party sends an OrderConfirmationStatusReport message to inform that the confirmation message is rejected.

### Common source context

**src-000095 P593** — This message flow section illustrates the use of the OrderConfirmationStatusReport message in typical message sequencing scenarios. The OrderConfirmationStatusReport message is sent by the instructing party to the executing party to provide the status of a subscription, redemption or switch confirmation or confirmation amendment.

**src-000095 P594** — There may be one or more intermediaries in the transaction chain.

**src-000095 P595** — The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**src-000095 P596** — The intermediary party is, for example, a distributor.

## Exact supplied message references

| Narrative message name | Canonical exact definition | Binding evidence |
| --- | --- | --- |
| OrderConfirmationStatusReport | [setr.057.001.03](../../../../messages/setr.057.001.03/index.md) | src-000096 file page 4283; 64 setr.057.001.03 OrderConfirmationStatusReportV03 |
| SubscriptionOrder | [setr.010.001.05](../../../../messages/setr.010.001.05/index.md) | src-000096 file page 3001; 50 setr.010.001.05 SubscriptionOrderV05 |
| SubscriptionOrderConfirmation | [setr.012.001.06](../../../../messages/setr.012.001.06/index.md) | src-000096 file page 3248; 52 setr.012.001.06 SubscriptionOrderConfirmationV06 |


The Part 1 picture and narrative use unversioned names. The linked full identifiers are supplied Part 2 definitions with exact matching names, not a claim that the picture prints a version.

## Diagram and limitations

[Source reconstruction with original image and review evidence](../diagrams/funds-sequences/fig-0084.md)

- The source uses institutional pictograms for functional participants; native Mermaid lifeline boxes retain the labels without equating a functional role with one institution.
- Open source arrowheads are reproduced with native Mermaid open arrows. This visual notation choice does not establish additional transport or acknowledgement rules.
- The picture itself names messages without version numbers. Exact message references are matched separately through the supplied Part 2 headings; the mapping evidence and publication remain explicit.

## Additional source-narrative participants

These explicit labels occur in the scenario or its common source context, including source-given examples. They are not extra drawn lifelines and no equivalence with a functional role is inferred. The full paragraphs above preserve the applicable qualification.

- [Distributor](../../../../../../../shared/reference/participants/participant-src-000095-distributor.md)
- [Intermediary](../../../../../../../shared/reference/participants/participant-src-000095-intermediary.md)
- [Investment manager](../../../../../../../shared/reference/participants/participant-src-000095-investment-manager.md)
- [Transfer Agent](../../../../../../../shared/reference/participants/participant-src-000095-transfer-agent.md)
