---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["20 semt.004.001.02 CustodyStatementOfHoldingsCancellationV02"]
file_pages: [398]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.004.001.02"]
---

# 20 semt.004.001.02 CustodyStatementOfHoldingsCancellationV02

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 398 to 398.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 398

```text
20 semt.004.001.02
CustodyStatementOfHoldingsCancellationV0
2
20.1 MessageDefinition Functionality
Scope
An account servicer, for example, a transfer agent, sends the
CustodyStatementOfHoldingsCancellation message to the account owner, for example, an investment
manager or its authorised representative to cancel a previously sent CustodyStatementOfHoldings
message.
Usage
The CustodyStatementOfHoldingsCancellation message is used to cancel a previously sent
CustodyStatementOfHoldings message. This message must contain the reference of the message to
be cancelled.
This message may also contain details of the message to be cancelled, but this is not recommended.
Outline
The CustodyStatementOfHoldingsCancellationV02 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PreviousReference
Reference to a linked message that was previously sent.
C. RelatedReference
Reference to a linked message that was previously received.
D. MessagePagination
Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
E. StatementToBeCancelled
The Custody Statement of Holdings message to cancel.
Approved by the Securities SEG on 27 January 2026 semt.004.001.02
CustodyStatementOfHoldingsCancellationV02
Investment Funds - Maintenance 2025 - 2026 398 May 2026
```

