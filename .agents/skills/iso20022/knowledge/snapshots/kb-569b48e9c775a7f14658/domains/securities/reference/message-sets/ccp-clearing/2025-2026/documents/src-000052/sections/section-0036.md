---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000052"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["BusinessTransactions", "Buy-in BusinessTransaction"]
content_origin: "source-transcription"
---

# Buy-in BusinessTransaction

Source: [src-000052](../../../../../../../../../evidence/omitted/b45c53bac2be08dee677b607.md). Locator: heading path BusinessTransactions / Buy-in BusinessTransaction.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P250** Buy-in BusinessTransaction

**P251** The buy-in process is a process by which the central counterparty (CCP) buys in stock to cover failed transactions.

**P252** The BuyInNotification message is sent by a central counterparty (CCP) to the clearing member to notify the start of the buy-in process. This message can also be sent, as a warning, some days before the buy-in process actually starts.

**P253** The BuyInResponse message is sent by the clearing member to the CCP as a response to the previously sent buy-in notification message. The use of this message in the buy-in process is optional and depends on the rules set out by each central counterparty.

**P254** The BuyInConfirmation message is sent by the CCP to the clearing member to confirm the details of the transaction resulting from the buy-in process.

[fig-0018 - original figure evidence](../diagrams/fig-0018.md)

**P264**   


