---
template: false
document_kind: "participant"
review_status: "needs-review"
manual_curated: true
domain: "securities"
domains: ["securities"]
participant_id: "participant-src-000180-trustee"
title: "Trustee"
source_labels: ["Trustee"]
role_type: "source-scoped business actor in flow"
source_ids: ["src-000180"]
source_editions: ["February 2025"]
source_locations: [{"source_id": "src-000180", "locator": "P147/P195; image11/P196; P233-P284"}]
message_sets: ["post-trade-matching"]
message_ids: ["semt.023.001.02", "setr.027.001.05", "setr.029.001.02", "setr.030.001.03"]
flows: ["flow-src-000180-p146-through-type", "flow-src-000180-p165-end-of-process-report-for-listed-derivatives", "flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service", "flow-src-000180-p194-through-type", "flow-src-000180-p198-through-type-cancellation", "flow-src-000180-p227-end-of-process-report-for-listed-derivatives", "flow-src-000180-p232-tripartite-central-matching-without-confirmation-distribution-service", "flow-src-000180-p237-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p241-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p245-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p249-tripartite-central-matching-without-confirmation-distribution-service-", "flow-src-000180-p255-tripartite-central-matching-with-confirmation-distribution-service", "flow-src-000180-p260-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p265-tripartite-central-matching-with-confirmation-distribution-service-can", "flow-src-000180-p269-tripartite-central-matching-with-confirmation-distribution-service-rej", "flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report"]
aliases: []
search_terms: ["Trustee"]
limitations: ["The label Trustee in these diagrams is not automatically merged with Custodian or Trust Bank; no institution-level equivalence is established.", "No identifier scheme is specified in these source passages."]
---



































# Trustee

## Definition and context

The participant that receives forwarded trade confirmations and, if it agrees with the trade details, returns an affirmation to the central matching utility. Other scenarios describe disaffirmation, cancellation receipt, and end-of-process reporting.

## Responsibilities and relationships

Receives confirmations from the CMU; compares the details; affirms or disaffirms; receives forwarded cancellations and end-of-process reports.

The label Trustee in these diagrams is not automatically merged with Custodian or Trust Bank; no institution-level equivalence is established.

Source: [src-000180](../../../evidence/omitted/620693d01e301c06503cea9a.md); P147/P195; image11/P196; P233-P284. No identifier scheme is specified.

Post-trade matching scenario: [Through Type](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p194-through-type.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0014.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Through Type Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p198-through-type-cancellation.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0015.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [End of Process Report for Listed Derivatives](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p227-end-of-process-report-for-listed-derivatives.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0021.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p232-tripartite-central-matching-without-confirmation-distribution-service.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0022.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service Cancellation](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p237-tripartite-central-matching-without-confirmation-distribution-service-.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0023.md). The source identifies this participant as an inactive lifeline or narrative alternative in this scenario.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Executing Broker](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p241-tripartite-central-matching-without-confirmation-distribution-service-.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0024.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service Cancellation by Investment Manager](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p245-tripartite-central-matching-without-confirmation-distribution-service-.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0025.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching Without Confirmation Distribution Service Rejection](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p249-tripartite-central-matching-without-confirmation-distribution-service-.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0026.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With Confirmation Distribution Service](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p255-tripartite-central-matching-with-confirmation-distribution-service.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0027.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With Confirmation Distribution Service Cancellation by Executing Broker](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p260-tripartite-central-matching-with-confirmation-distribution-service-can.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0028.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With Confirmation Distribution Service Cancellation by Investment Manager](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p265-tripartite-central-matching-with-confirmation-distribution-service-can.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0029.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With Confirmation Distribution Service Rejection](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p269-tripartite-central-matching-with-confirmation-distribution-service-rej.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0030.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Post-trade matching scenario: [Tripartite Central Matching With End of Process Report](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p283-tripartite-central-matching-with-end-of-process-report.md); [source sequence](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/business-transactions/fig-0033.md). The source diagram shows this participant as sender/receiver in the ordered exchange.

Source context: [Through-type local matching activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0007.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p146-through-type.md).

Source context: [Tripartite central matching without distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0011.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p173-tripartite-central-matching-without-confirmation-distribution-service.md).

Source context: [Tripartite central matching with distribution](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0012.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p180-tripartite-central-matching-with-confirmation-distribution-service.md).

Source context: [Listed-derivatives end-of-process reporting activity](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/diagrams/processes/fig-0010.md). [Reusable flow](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/flows/flow-src-000180-p165-end-of-process-report-for-listed-derivatives.md).
