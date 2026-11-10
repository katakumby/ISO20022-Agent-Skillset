---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "How to use the Cash Management Messages", "Building a Return Message"]
content_origin: "source-transcription"
---

# Building a Return Message

Source: [src-000014](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart1_CashManagement_2024_2025_v2.docx). Locator: heading path BusinessTransactions / How to use the Cash Management Messages / Building a Return Message.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P141** Building a Return Message

**P142** The Return message contains the result of the Get message processing. Depending on the success or failure of the processing, the Return message may or may not contain an error notification.

**P143** As explained earlier, Return messages could also be sent spontaneously by the transaction administrator.

**P144** The agreement between the parties may stipulate, where relevant, the size and the maximum number of items to be returned within the Return message. The maximum size of the Return message, or the maximum number of occurrences allowed, have to take into account technical constraints, such as the maximum payload size on the communication network. These characteristics are considered external to the standards design and are therefore not explained in this document.

