---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "Order Confirmation Cancellation "]
content_origin: "source-transcription"
---

# Order Confirmation Cancellation 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path BusinessTransactions / Order Confirmation Cancellation .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P670** Order Confirmation Cancellation 

**P671** This message flow section illustrates the use of the order confirmation cancellation messages in typical message sequencing scenarios. The different order confirmation cancellation instruction messages are sent by the executing party to the instructing party to cancel a previously sent subscription, redemption or order confirmation message. 

**P672** There may be one or more intermediaries in the transaction chain.

**P673** The order confirmation cancellation instruction message might be followed by an order confirmation message sent as an amendment (AmendmentIndicator set to 'true' or '1'), (see sequence diagrams related to order confirmation amendment).

**P674** The instructing party is, for example, an investment manager. The executing party is, for example, a transfer agent. 

**P675** The intermediary party is, for example, a distributor.

