---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["7 camt.040.001.04 FundEstimatedCashForecastReportV04"]
file_pages: [94, 95]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.040.001.04"]
---

# 7 camt.040.001.04 FundEstimatedCashForecastReportV04

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 94 to 95.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 94

```text
7 camt.040.001.04
FundEstimatedCashForecastReportV04
7.1 MessageDefinition Functionality
Scope
A report provider, such as a transfer agent, sends the FundEstimatedCashForecastReport message to
the report user, such as an investment manager or pricing agent, to report the estimated cash
incomings and outgoings of one or more share classes of an investment fund on one or more trade
dates.
The cash movements may result from, for example, redemption, subscription, switch transactions or
reinvestment of dividends.
Usage
The FundEstimatedCashForecastReport is used to report estimated cash movements, that is, it is sent
prior to the cut-off time and/or the price valuation of the fund.
The message contains incoming and outgoing cash flows that are estimated, that is, the price has not
been applied. If the price is definitive, then the FundConfirmedCashForecastReport message must be
used.
The message structure allows for the following uses:
- to provide cash in and cash out amounts for a fund/sub fund (FundOrSubFundDetails sequence is
used),
- to provide cash in and cash out amounts for a fund/sub fund and one or more share classes (a
FundOrSubFundDetails sequence and one or more EstimatedFundCashForecastDetails sequences are
used),
- to provide cash in and cash out amounts for one or more share classes (one or more
EstimatedFundCashForecastDetails sequences are used).
- to provide cash in and cash out amounts for more than one fund/sub fund, and more than one share
classes (two or more FundOrSubFundDetails sequences and two or more
EstimatedFundCashForecastDetails sequences and used); however, it should be noted that, in this
usage, there is no way to determine which share class belongs to which fund/sub fund from the
message content itself, which may not be desirable and the use of this kind of combination should be
bilaterally agreed.
This message allows the report provider to report estimated cash movements in or out of a fund, but
does not allow the Sender to categorise these movements, for example by country, or to give details of
the underlying orders, commission or charges. If the report provider wishes to give detailed information
related to estimated cash movements, then the FundDetailedEstimatedCashForecastReport message
must be used.
Outline
Approved by the Securities SEG on 27 January 2026 camt.040.001.04
FundEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 94 May 2026
```

## File page 95

```text
The FundEstimatedCashForecastReportV04 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. MessageIdentification
Identifies the message.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. MessagePagination
Pagination of the message.
F. FundOrSubFundDetails
Information about the fund/sub fund when the report either specifies cash flow for the fund/sub fund
or for a share class of the fund/sub fund.
G. EstimatedFundCashForecastDetails
Information related to the estimated cash-in and cash-out flows for a specific trade date as a result
of transactions in shares in an investment fund, for example, subscriptions, redemptions or
switches.
H. ConsolidatedNetCashForecast
Estimated net cash as a result of the cash-in and cash-out flows.
I. Extension
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 camt.040.001.04
FundEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 95 May 2026
```

