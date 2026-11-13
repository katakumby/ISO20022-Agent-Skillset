---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-broker"
title: "Broker"
source_labels: ["Broker"]
role_type: "activity participant named in responsibility column"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[4]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[3]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[5]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[8]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[3]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[3]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[4]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[3]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[4]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[3]", "paragraph_id": null, "table_id": "T15"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Bilateral Central Matching"], "locator": "/w:document/w:body/w:tbl[15]/w:tr[4]", "paragraph_id": null, "table_id": "T15"}]
flows: ["flow-src-000180-p146-through-type", "flow-src-000180-p153-own-account-trade-type", "flow-src-000180-p165-end-of-process-report-for-listed-derivatives", "flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service", "flow-src-000180-p185-bilateral-central-matching"]
process_sections: ["flow-src-000180-p194-through-type", "flow-src-000180-p198-through-type-cancellation", "flow-src-000180-p203-own-account-trade-type", "flow-src-000180-p208-own-account-trade-type-cancellation", "flow-src-000180-p227-end-of-process-report-for-listed-derivatives", "flow-src-000180-p232-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p237-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p241-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p245-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p249-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p255-tripartite-central-matching-with-confirmation-distribution-service", "flow-src-000180-p260-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p265-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p269-tripartite-central-matching-with-confirmation-distribution-service-rej", "flow-src-000180-p274-bilateral-central-matching", "flow-src-000180-p278-bilateral-central-matching-cancellation", "flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report"]
message_ids: []
message_families: []
search_terms: ["Broker"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---

















# Broker

Business context: Post-Trade Matching. Source classification: activity participant named in responsibility column.

## Definition

The source names this actor in an activity or role matrix; a separate definition has not been established. This limitation remains open for review.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Source activity row 3 | Confirmation: The broker sends a confirmation to JASDEC . | Broker | [T9](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0009.md) row 3 |
| Source activity row 4 | Cancel Confirmation: The broker and investment manager may, for whatever reason, decide to cancel the confirmation and a new confirmation may be sent. Cancellation of the confirmation may also imply the cancellation of the trade, in which case a new confirmation will not be sent. | Broker | [T9](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0009.md) row 4 |
| Source activity row 3 | Confirmation The broker sends a confirmation of the trade to JASDEC . | Broker | [T12](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0012.md) row 3 |
| Source activity row 5 | Delivery Amount Report: The broker sends a delivery amount report to JASDEC. | Broker | [T12](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0012.md) row 5 |
| Source activity row 6 | End of Day Report of Confirmation: The broker sends an end of day report of the confirmation to JASDEC. | Broker | [T12](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0012.md) row 6 |
| Source activity row 8 | End of Day Report of Delivery Amount: The broker sends an end of day report of delivery amount to JASDEC. | Broker | [T12](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0012.md) row 8 |
| Source activity row 3 | Confirmation: The broker sends a trade confirmation to the CMU (JASDEC).  | Broker | [T13](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0013.md) row 3 |
| Source activity row 4 | Cancel Confirmation: If unmatched, the broker may send a new confirmation or may, upon mutual agreement, send a confirmation cancellation. | Broker | [T13](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0013.md) row 4 |
| Source activity row 3 | Confirmation: The broker sends a trade confirmation to the CMU (JASDEC). | Broker | [T14](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0014.md) row 3 |
| Source activity row 4 | Cancel Confirmation: If unmatched, the broker may send a confirmation cancellation message to the CMU or it may send a new confirmation to the CMU. | Broker | [T14](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0014.md) row 4 |
| Source activity row 3 | Confirmation: Broker 1 sends a confirmation to the CMU (JASDEC).  | Broker | [T15](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0015.md) row 3 |
| Source activity row 4 | Cancel Confirmation: If the confirmation is unmatched, it may lead to the sending of a confirmation cancellation from the broker to the CMU or to the sending of a new confirmation from the broker to the CMU. | Broker | [T15](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0015.md) row 4 |
| Source activity row 3 | Confirmation: Broker 2 sends a confirmation to the CMU (JASDEC).  | Broker | [T15](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0015.md) row 3 |
| Source activity row 4 | Cancel Confirmation: If the confirmation is unmatched, it may lead to the sending of a confirmation cancellation from the broker to the CMU or to the sending of a new confirmation from the broker to the CMU. | Broker | [T15](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0015.md) row 4 |

## Relationships

No role-matrix relationship was extracted for this label; this does not establish that none exists.

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Through Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p146-through-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Own Account Trade Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p153-own-account-trade-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [End of Process Report for Listed Derivatives](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p165-end-of-process-report-for-listed-derivatives.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching Without Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching With Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bilateral Central Matching](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p185-bilateral-central-matching.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Through Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p194-through-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Through Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p198-through-type-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Own Account Trade Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p203-own-account-trade-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Own Account Trade Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p208-own-account-trade-type-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [End of Process Report for Listed Derivatives](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p227-end-of-process-report-for-listed-derivatives.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching Without Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p232-tripartite-central-matching-without-confirmation-distribution-service.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching Without Confirmation Distribution Service Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p237-tripartite-central-matching-without-confirmation-distribution-service-.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Executing Broker](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p241-tripartite-central-matching-without-confirmation-distribution-service-.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Investment Manager](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p245-tripartite-central-matching-without-confirmation-distribution-service-.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching Without Confirmation Distribution Service Rejection](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p249-tripartite-central-matching-without-confirmation-distribution-service-.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching With Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p255-tripartite-central-matching-with-confirmation-distribution-service.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p260-tripartite-central-matching-with-confirmation-distribution-service-can.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p265-tripartite-central-matching-with-confirmation-distribution-service-can.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching With Confirmation Distribution Service Rejection](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p269-tripartite-central-matching-with-confirmation-distribution-service-rej.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bilateral Central Matching](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p274-bilateral-central-matching.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bilateral Central Matching Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p278-bilateral-central-matching-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching With End of Process Report](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Broker`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md).

Source context: [Post-trade communication scope](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0001.md).

Source context: [Through-type local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0007.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p146-through-type.md).

Source context: [Own-account local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p153-own-account-trade-type.md).

Source context: [Tripartite central matching without distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md).

Source context: [Tripartite central matching with distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0012.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md).

Source context: [Bilateral central matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0013.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p185-bilateral-central-matching.md).

Source context: [Listed-derivatives end-of-process reporting activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0010.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p165-end-of-process-report-for-listed-derivatives.md).
