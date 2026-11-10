---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.7 AutoBorrowing1Code"]
file_pages: [615]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.7 AutoBorrowing1Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 615 to 615.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 615

```text
CodeName Name Definition
DELI Deliverable Physical certificates exist.
NDEL NotDeliverable Not yet deliverable contract.
LIMI Limited Limited or partial deliverability.
BENT BookEntry Security exists only as an electronic
record, ie, there are no physical
certificates representing the security.
DFBE DeferredBookEntry Deferred printing, book entry.
DLBE DeliverableBookEntry Deliverable, book entry.
TMPG TemporaryGlobal Deferred printing, global certificate.
GLOB Global Not deliverable, global certificate.
7.2.2.7  AutoBorrowing1Code
Definition: Specifies the condition under which automatic borrowing is allowed.
Type: CodeSet
CodeName Name Definition
LAMI LastResort Only last resort borrowing should be
considered to make settlement occur.
NBOR NoAutomatic No automatic borrowing should take
place.
YBOR Automatic Automatic borrowing should take place.
7.2.2.8  AwaitingAffirmationReason1Code
Definition: Specifies the reason why the instruction has an awaiting affirmation status.
Type: CodeSet
CodeName Name Definition
WAFF AwaitingAffirmation Affirmation has not been received yet.
7.2.2.9  AwaitingCancellationReason1Code
Definition: Specifies the reason why the instruction has an awaiting cancellation status.
Type: CodeSet
CodeName Name Definition
WCAN AwaitingCancellation Cancellation has not been received yet.
7.2.2.10  BlockTrade1Code
Definition: Specifies whether the instruction is the parent or a children of a block trade.
Type: CodeSet
CodeName Name Definition
BLPA Parent Transaction is a block trade parent.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 615 February 2025
```

