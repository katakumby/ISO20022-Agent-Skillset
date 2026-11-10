---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["21 semt.005.001.02 AccountingStatementOfHoldingsCancellationV02"]
file_pages: [403]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.005.001.02"]
---

# 21 semt.005.001.02 AccountingStatementOfHoldingsCancellationV02

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 403 to 403.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 403

```text
21 semt.005.001.02
AccountingStatementOfHoldingsCancellation
V02
21.1 MessageDefinition Functionality
Scope
An account servicer, for example, a transfer agent, sends the
AccountingStatementofHoldingsCancellation message to the account owner, for example, a fund
manager or an account owner's designated agent, to notify the cancellation of a previously sent
AccountingStatementOfHoldings message.
Usage
The AccountingStatementOfHoldingsCancellation message is used to cancel a previously sent
AccountingStatementOfHoldings message. This message must contain the reference of the message to
be cancelled.
This message may also contain all the details of the message to be cancelled, but this is not
recommended.
Outline
The AccountingStatementOfHoldingsCancellationV02 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. RelatedReference
Reference to a linked message that was previously received.
D. MessagePagination
Pagination of the message.
E. StatementToBeCancelled
The Accounting Statement of Holdings message to cancel.
Approved by the Securities SEG on 27 January 2026 semt.005.001.02
AccountingStatementOfHoldingsCancellationV02
Investment Funds - Maintenance 2025 - 2026 403 May 2026
```

