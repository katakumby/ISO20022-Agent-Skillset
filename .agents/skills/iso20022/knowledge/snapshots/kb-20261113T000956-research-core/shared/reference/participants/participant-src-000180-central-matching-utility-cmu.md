---
template: false
document_kind: "participant"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
message_sets: ["post-trade-matching"]
participant_id: "participant-src-000180-central-matching-utility-cmu"
title: "Central Matching Utility (CMU)"
source_labels: ["Central Matching Utility (CMU)"]
role_type: "business role"
aliases: []
source_locations: [{"source_id": "src-000180", "heading_path": ["BusinessRoles and Participants"], "locator": "/w:document/w:body/w:tbl[7]/w:tr[12]", "paragraph_id": null, "table_id": "T7"}]
flows: ["flow-src-000180-p120-business-process-diagram", "flow-src-000180-p146-through-type", "flow-src-000180-p153-own-account-trade-type", "flow-src-000180-p159-duplex-type", "flow-src-000180-p165-end-of-process-report-for-listed-derivatives", "flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service", "flow-src-000180-p185-bilateral-central-matching", "flow-src-000180-p194-through-type", "flow-src-000180-p198-through-type-cancellation", "flow-src-000180-p203-own-account-trade-type", "flow-src-000180-p208-own-account-trade-type-cancellation", "flow-src-000180-p214-duplex-type", "flow-src-000180-p218-duplex-type-rejection-by-transfer-agent", "flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent", "flow-src-000180-p227-end-of-process-report-for-listed-derivatives", "flow-src-000180-p232-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p237-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p241-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p245-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p249-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p255-tripartite-central-matching-with-confirmation-distribution-service", "flow-src-000180-p260-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p265-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p269-tripartite-central-matching-with-confirmation-distribution-service-rej", "flow-src-000180-p274-bilateral-central-matching", "flow-src-000180-p278-bilateral-central-matching-cancellation", "flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report"]
process_sections: []
message_ids: ["semt.023.001.02", "setr.027.001.05", "setr.029.001.02", "setr.030.001.03", "setr.044.001.04"]
message_families: []
search_terms: ["Central Matching Utility (CMU)"]
limitations: ["Definition is scoped to this source and message-set context; same labels in other sources remain distinct.", "Aliases and identifier schemes have not been established beyond explicit source labels.", "Narrative-only participants not captured by definition/initiator tables require additional review."]
manual_curated: true
---































































# Central Matching Utility (CMU)

Business context: Post-Trade Matching. Source classification: business role.

## Definition

Mediates communication between the broker / dealer and investment manager to exchange trade details, match settlement criteria and confirm completion of financial instrument transactions. The CMU may be operated as a separate utility or as part of another market utility eg, CSD.

Evidence: [T7](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0007.md), source row 12.

A functional participant role describes involvement in a relationship or transaction. It is not an assertion that a particular institution always plays that role.

## Responsibilities and actions

Responsibilities are described in the definition and linked flows; no separate activity-initiator rows were matched.

## Relationships

| Relationship | Related scoped record | Evidence |
| --- | --- | --- |
| Can play the functional participant role in this source context | [Instructing Party](participant-src-000180-instructing-party.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 8, column 2 |
| Can play the functional participant role in this source context | [Executing/Servicing Party](participant-src-000180-executing-servicing-party.md) | [T8](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000180/tables/tbl-0008.md) row 8, column 3 |

## Flows, source process sections and messages

No flow segment has yet been matched to this role label.

Message families found in these flows: not established. Exact-version applicability requires the linked source locator.

## Aliases, identification and limitations

Source labels: `Central Matching Utility (CMU)`. No external identifier scheme or alias equivalence has been inferred.

- Definition is scoped to this source and message-set context; same labels in other sources remain distinct.
- Aliases and identifier schemes have not been established beyond explicit source labels.
- Narrative-only participants not captured by definition/initiator tables require additional review.

Original: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md).

Post-trade matching scenario: [Through Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p194-through-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0014.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Through Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p198-through-type-cancellation.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0015.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Own Account Trade Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p203-own-account-trade-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0016.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Own Account Trade Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p208-own-account-trade-type-cancellation.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0017.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Duplex Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p214-duplex-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0018.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Duplex Type Rejection by Transfer Agent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p218-duplex-type-rejection-by-transfer-agent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0019.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Duplex Type Rejection by Cash Correspondent](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p222-duplex-type-rejection-by-cash-correspondent.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0020.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

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

Post-trade matching scenario: [Bilateral Central Matching](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p274-bilateral-central-matching.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0031.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Bilateral Central Matching Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p278-bilateral-central-matching-cancellation.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0032.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With End of Process Report](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0033.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Source context: [Post-trade business-actor context](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0002.md).

Source context: [Trade lifecycle process overview](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0003.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p120-business-process-diagram.md).

Source context: [Through-type local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0007.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p146-through-type.md).

Source context: [Own-account local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0008.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p153-own-account-trade-type.md).

Source context: [Duplex local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0009.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p159-duplex-type.md).

Source context: [Tripartite central matching without distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md).

Source context: [Tripartite central matching with distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0012.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md).

Source context: [Bilateral central matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0013.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p185-bilateral-central-matching.md).

Source context: [Listed-derivatives end-of-process reporting activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0010.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p165-end-of-process-report-for-listed-derivatives.md).
