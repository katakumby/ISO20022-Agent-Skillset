---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Cancellation ", "Redemption ", "Bulk"]
content_origin: "source-transcription"
---

# Bulk

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Confirmation Cancellation  / Redemption  / Bulk.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P707** Bulk

**P708** Instructing party 1 sends a RedemptionOrder message to the intermediary party. Instructing party 2 sends a RedemptionOrder message to the intermediary party. 

**P709** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a RedemptionBulkOrder message to the transfer agent. 

**P710** The executing party sends a RedemptionBulkOrderConfirmation message to the intermediary party. 

**P711** The intermediary party splits up the confirmation according to the originating chain of instructions and sends a RedemptionOrderConfirmation message to instructing party 1 and a RedemptionOrderConfirmation message to instructing party 2. 

**P712** As the confirmation needs to be cancelled, a RedemptionBulkOrderConfirmationCancellationInstruction message is sent by the executing party to inform the intermediary. 

**P713** In turn, the intermediary party splits up the confirmation amendment message according to the originating chain of instructions and sends a RedemptionOrderConfirmationCancellationInstruction message to instructing party 1 and a RedemptionOrderConfirmationCancellationInstruction message to instructing party 2

[fig-0100 - original figure evidence](../diagrams/fig-0100.md)

