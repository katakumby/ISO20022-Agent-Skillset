---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-investment-manager"
title: "Investment Manager"
source_labels: ["Investment Manager"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessRoles and Participants"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[7]", "paragraph_id": null, "table_id": "T7"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[3]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "Through Type"], "locator": "/w:document/w:body/w:tbl[9]/w:tr[4]", "paragraph_id": null, "table_id": "T9"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[3]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Local Matching", "End of Process Report for Listed Derivatives"], "locator": "/w:document/w:body/w:tbl[12]/w:tr[6]", "paragraph_id": null, "table_id": "T12"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[3]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching Without Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[13]/w:tr[4]", "paragraph_id": null, "table_id": "T13"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[3]", "paragraph_id": null, "table_id": "T14"}, {"source_id": "src-000180", "heading_path": ["Description of BusinessActivities", "BusinessProcess – Central Matching", "Tripartite Central Matching With Confirmation Distribution Service"], "locator": "/w:document/w:body/w:tbl[14]/w:tr[4]", "paragraph_id": null, "table_id": "T14"}]
flows: ["flow-src-000180-p146-through-type", "flow-src-000180-p165-end-of-process-report-for-listed-derivatives", "flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service", "flow-src-000180-p185-bilateral-central-matching", "flow-src-000180-p194-through-type", "flow-src-000180-p198-through-type-cancellation", "flow-src-000180-p227-end-of-process-report-for-listed-derivatives", "flow-src-000180-p232-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p237-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p241-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p245-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p249-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p255-tripartite-central-matching-with-confirmation-distribution-service", "flow-src-000180-p260-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p265-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p269-tripartite-central-matching-with-confirmation-distribution-service-rej", "flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report"]
process_sections: ["flow-src-000180-p194-through-type", "flow-src-000180-p198-through-type-cancellation", "flow-src-000180-p227-end-of-process-report-for-listed-derivatives", "flow-src-000180-p232-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p237-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p241-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p245-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p249-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p255-tripartite-central-matching-with-confirmation-distribution-service", "flow-src-000180-p260-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p265-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p269-tripartite-central-matching-with-confirmation-distribution-service-rej", "flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report"]
message_ids: ["semt.023.001.02", "setr.027.001.05", "setr.029.001.02", "setr.044.001.04"]
message_families: []
search_terms: ["Investment Manager"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---











































# Investment Manager

Business context: Post-Trade Matching. Source classification: business role.

## Definition

Partners with the broker / dealer to communicate details, execute modifications and settle financial instrument transactions.

Evidence: [T7](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0007.md), source row 7.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

| Activity | Source description | Source responsibility column | Evidence |
| --- | --- | --- | --- |
| Source activity row 3 | Confirmation: The investment manager sends a confirmation of the trade to JASDEC. | Investment Manager | [T9](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0009.md) row 3 |
| Source activity row 4 | Cancel Confirmation: The investment manager and broker may decide to cancel the confirmation and a new confirmation may be sent. Cancellation of the confirmation may also imply the cancellation of the trade, in which case a new confirmation will not be sent. | Investment Manager | [T9](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0009.md) row 4 |
| Source activity row 3 | Confirmation: The investment manager sends a confirmation of the trade to JASDEC. | Investment Manager | [T12](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0012.md) row 3 |
| Source activity row 6 | End of Day Report of Confirmation: The investment manager sends an end of day report of the confirmation to JASDEC. | Investment Manager | [T12](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0012.md) row 6 |
| Source activity row 3 | Confirmation: The investment manager sends a trade confirmation to the CMU (JASDEC). | Investment Manager | [T13](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0013.md) row 3 |
| Source activity row 4 | Cancel Confirmation: If unmatched, the investment manager may send a new confirmation or may, upon mutual agreement, send a confirmation cancellation. | Investment Manager | [T13](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0013.md) row 4 |
| Source activity row 3 | Confirmation: The investment manager compares the details of the trade to its own details and sends a trade confirmation to the CMU.  | Investment Manager | [T14](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0014.md) row 3 |
| Source activity row 4 | Cancel Confirmation: If unmatched, the investment manager may send a confirmation cancellation message to the CMU or it may send a new confirmation to the CMU. | Investment Manager | [T14](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0014.md) row 4 |

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000180-instructing-party.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 3, column 2 |

## Flows, source process sections and messages

| Flow | Participation evidence |
| --- | --- |
| [Through Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p146-through-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [End of Process Report for Listed Derivatives](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p165-end-of-process-report-for-listed-derivatives.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching Without Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Tripartite Central Matching With Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Bilateral Central Matching](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p185-bilateral-central-matching.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Through Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p194-through-type.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
| [Through Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p198-through-type-cancellation.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |
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
| [Tripartite Central Matching With End of Process Report](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report.md) | Role label occurs in this source segment. Responsibilities/direction remain those explicitly stated in the evidence. |

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Investment Manager`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md).

Post-trade matching scenario: [Through Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p194-through-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0014.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Through Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p198-through-type-cancellation.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0015.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [End of Process Report for Listed Derivatives](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p227-end-of-process-report-for-listed-derivatives.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0021.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p232-tripartite-central-matching-without-confirmation-distribution-service.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0022.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p237-tripartite-central-matching-without-confirmation-distribution-service-.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0023.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Executing Broker](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p241-tripartite-central-matching-without-confirmation-distribution-service-.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0024.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Investment Manager](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p245-tripartite-central-matching-without-confirmation-distribution-service-.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0025.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service Rejection](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p249-tripartite-central-matching-without-confirmation-distribution-service-.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0026.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p255-tripartite-central-matching-with-confirmation-distribution-service.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0027.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p260-tripartite-central-matching-with-confirmation-distribution-service-can.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0028.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p265-tripartite-central-matching-with-confirmation-distribution-service-can.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0029.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With Confirmation Distribution Service Rejection](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p269-tripartite-central-matching-with-confirmation-distribution-service-rej.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0030.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With End of Process Report](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0033.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Source context: [Post-trade communication scope](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0001.md).

Source context: [Post-trade business-actor context](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0002.md).

Source context: [Through-type local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0007.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p146-through-type.md).

Source context: [Tripartite central matching without distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md).

Source context: [Tripartite central matching with distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0012.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md).

Source context: [Listed-derivatives end-of-process reporting activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0010.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p165-end-of-process-report-for-listed-derivatives.md).
