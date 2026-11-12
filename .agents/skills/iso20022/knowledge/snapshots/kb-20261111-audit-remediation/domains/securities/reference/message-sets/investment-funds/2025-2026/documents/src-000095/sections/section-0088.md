---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Instruction Status Reporting", "Subscription", "Bulk"]
content_origin: "source-transcription"
---

# Bulk

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Instruction Status Reporting / Subscription / Bulk.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P436** Bulk

**P437** Instructing party 1 sends a SubscriptionOrder message to the intermediary party. Instructing party 2 sends a SubscriptionOrder to the intermediary party. 

**P438** There may be more than two instructing parties sending SubscriptionOrder messages to the intermediary party. 

**P439** The intermediary party collects the individual orders. As the orders sent by instructing parties 1 and 2 are for the same financial instrument, the orders are grouped together and the intermediary sends a SubscriptionBulkOrder message to the executing party.

**P440** The intermediary sends OrderInstructionStatusReport messages, with the status Received (RECE) or SentToNextParty (STNP), to instructing party 1 and instructing party 2.

**P441** When the orders in the bulk have been accepted, the executing party responds with an OrderInstructionStatusReport message, with the status Accepted (PACK), to the intermediary party.

**P442** Likewise, the intermediary sends OrderInstructionStatusReport messages, with the status Accepted (PACK), to instructing party 1 and instructing party 2.

[fig-0060 - original figure evidence](../diagrams/fig-0060.md)

