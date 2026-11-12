---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Cancellation and Status ", "Redemption ", "Request and Status - Intermediary"]
content_origin: "source-transcription"
---

# Request and Status - Intermediary

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Cancellation and Status  / Redemption  / Request and Status - Intermediary.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P539** Request and Status - Intermediary

**P540** The instructing party sends a RedemptionOrder message to the intermediary party. The intermediary party sends a RedemptionOrder message to the executing party. 

**P541** Subsequently, the instructing party sends a RedemptionOrderCancellationRequest message to the intermediary party. The intermediary party sends a RedemptionOrderCancellationRequest message to the executing party. 

**P542** The executing party responds by sending an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the intermediary party. In turn, the intermediary party sends an OrderCancellationStatusReport message, with the status CancellationCompleted (CAND), to the instructing party.

[fig-0076 - original figure evidence](../diagrams/fig-0076.md)

