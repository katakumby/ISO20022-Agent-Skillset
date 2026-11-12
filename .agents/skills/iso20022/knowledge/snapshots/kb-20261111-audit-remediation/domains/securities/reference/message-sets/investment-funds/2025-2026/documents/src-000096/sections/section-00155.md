---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["14 reda.002.001.05 PriceReportCancellationV05"]
file_pages: [222, 223]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.002.001.05"]
---

# 14 reda.002.001.05 PriceReportCancellationV05

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 222 to 223.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 222

```text
14 reda.002.001.05
PriceReportCancellationV05
14.1 MessageDefinition Functionality
SCOPE
A report provider, for example, a transfer agent, fund accountant or market data provider, sends the
PriceReportCancellation message to the report recipient, for example, a fund management company,
transfer agent, market data provider, regulator or any other interested party to cancel previously sent
prices.
USAGE
The PriceReportCancellation message is used to either:
- cancel an entire PriceReport that was previously sent (by quoting the business reference of the
original price report in the PriceReportIdentification element), or,
- cancel one or more individual prices from a previously sent price report (by using the
PriceDetailsToBeCancelled sequence).
Technically, it is possible to cancel all the prices individually by using the PriceDetailsToBeCancelled
sequence, but this is not recommended.
The cancellation should not contain the cancellation of prices for more than one NAV date.
Outline
The PriceReportCancellationV05 MessageDefinition is composed of 11 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. MessagePagination
Pagination of the message.
E. PriceReportIdentification
Unique and unambiguous identifier for the price report, as assigned by the reporting party.
F. CancellationIdentification
Unique and unambiguous identifier for the cancellation of the previous price report, as assigned by
the reporting party.
G. CancellationReason
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 222 May 2026
```

## File page 223

```text
Reason for the cancellation.
H. ExpectedPriceCorrectionDate
Date or date and time the price will be corrected.
I. CompletePriceCancellation
Indicates whether or not all the prices of the referenced price report are cancelled.
J. CancelledPriceValuationDetails
Details of prices to be cancelled.
K. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 reda.002.001.05 PriceReportCancellationV05
Investment Funds - Maintenance 2025 - 2026 223 May 2026
```

