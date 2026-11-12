---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000014"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["BusinessTransactions", "How to use the Cash Management Messages", "Features of Get and Return Messages"]
content_origin: "source-transcription"
---

# Features of Get and Return Messages

Source: [src-000014](../../../../../../../../../evidence/omitted/335a400e27e5efca9fdafbb5.md). Locator: heading path BusinessTransactions / How to use the Cash Management Messages / Features of Get and Return Messages.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P145** Features of Get and Return Messages

**P146** Reconciling Get and Return Messages

**P147** The reconciliation of the Get and Return messages takes place via the QueryReference element of the Return message.

**P148** This element contains the message identification of the Get message to which it is replying and, optionally the name of the query.

**P149** Reusing a Query

**P150** In all the Get messages, an element NewQueryName makes it possible to assign a name to the particular combination of search and return criteria that are included in the message. This name may then be used in the element QueryName of subsequent Get messages to simply refer to this combination. Thanks to this option, the account owner may define a query either by selecting the appropriate search and return criteria, or by referring to a previous query by its name.

**P151** This allows the execution of routine queries, ie, the regular submission of Get messages that have the same desired output.

