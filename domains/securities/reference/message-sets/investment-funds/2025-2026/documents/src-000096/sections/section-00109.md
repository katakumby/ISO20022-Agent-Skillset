---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["12 camt.045.001.03 FundDetailedConfirmedCashForecastReportCancellationV03", "13.1 MessageDefinition Functionality"]
file_pages: [159, 160]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.001.001.05"]
---

# 13.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 159 to 160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 159

```text
13 reda.001.001.05
PriceReportV05
13.1 MessageDefinition Functionality
SCOPE
A report provider, for example, a transfer agent, fund accountant or market data provider, sends the
PriceReport message to the report recipient, for example, a fund management company, transfer agent,
market data provider, regulator or any other interested party to provide the net asset value and price
information for financial instruments on specific trade dates and, optionally, to quote price variation
information.
USAGE
The PriceReport message is sent by the report provider to the report recipient to:
- report prices for one or several different financial instruments for one or several different trade dates,
- report statistical information about the valuation of a financial instrument,
- inform another party that the quotation of a financial instrument is suspended,
- report prices that are used for other purposes than the execution of investment funds orders.
.
Outline
The PriceReportV05 MessageDefinition is composed of 10 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies a message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. MessagePagination
Pagination of the message.
F. PriceReportIdentification
Unique and unambiguous identifier for the price report, as assigned by the reporting party.
G. Function
Function of the price report, that is, whether the price report is a new price report or a replacement
of some kind.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 159 May 2026
```

## File page 160

```text
H. CancellationIdentification
Unique and unambiguous identifier for the cancellation of the previous price report, as assigned by
the reporting party.
I. PriceValuationDetails
Information related to the price valuation of a financial instrument.
J. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 reda.001.001.05 PriceReportV05
Investment Funds - Maintenance 2025 - 2026 160 May 2026
```

