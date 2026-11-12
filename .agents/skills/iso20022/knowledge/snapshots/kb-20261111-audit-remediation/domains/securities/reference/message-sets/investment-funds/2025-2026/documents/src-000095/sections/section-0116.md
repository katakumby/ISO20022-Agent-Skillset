---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Cancellation and Status ", "Order Cancellation Status Request", "Status Request Rejected"]
content_origin: "source-transcription"
---

# Status Request Rejected

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Cancellation and Status  / Order Cancellation Status Request / Status Request Rejected.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P581** Status Request Rejected

**P582** The instructing party sends a RedemptionOrder message to the executing party. 

**P583** Subsequently the instructing party sends a RedemptionOrderCancellationRequest message to the executing party. 

**P584** As the executing party does not recognise the reference in the RedemptionOrderCancellationRequest message, it responds with a SecuritiesMessageRejection message, with the reason InvalidOrUnrecognisedReference.

[fig-0082 - original figure evidence](../diagrams/fig-0082.md)

