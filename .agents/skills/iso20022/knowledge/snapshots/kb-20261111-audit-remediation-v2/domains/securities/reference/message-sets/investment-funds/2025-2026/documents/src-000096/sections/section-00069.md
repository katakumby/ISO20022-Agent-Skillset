---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["8 camt.041.001.04 FundConfirmedCashForecastReportV04"]
file_pages: [105, 106]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.041.001.04"]
---

# 8 camt.041.001.04 FundConfirmedCashForecastReportV04

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 105 to 106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 105

```text
8 camt.041.001.04
FundConfirmedCashForecastReportV04
8.1 MessageDefinition Functionality
Scope
A report provider, such as a transfer agent, sends the FundConfirmedCashForecastReport message to
the report user, such as an investment manager or pricing agent, to report the confirmed cash
incomings and outgoings of one or more share classes of an investment fund on one or more trade
dates.
The cash movements may result from, for example, redemption, subscription, switch transactions or
reinvestment of dividends.
Usage
The FundConfirmedCashForecastReport is used to report definitive cash movements, that is it is sent
after the cut-off time and/or the price valuation of the fund.
This message contains incoming and outgoing cash flows that are confirmed, that is, the price has been
applied. If the price is not yet definitive, then the FundEstimatedCashForecastReport message must be
used.
The message structure allows for the following uses:
- to provide cash in and cash out amounts for a fund/sub fund (a FundOrSubFundDetails sequence is
used),
- to provide cash in and cash out amounts for a fund/sub fund and one or more share classes
(FundOrSubFundDetails sequence and one or more FundCashForecastDetails sequences are used),
- to provide cash in and cash out amounts for one or more share classes (one or more
FundCashForecastDetails sequences are used).
- to provide cash in and cash out amounts for more than one fund/sub fund, and more than one share
classes (two or more FundOrSubFundDetails sequences and two or more FundCashForecastDetails
sequences and used); however, it should be noted that, in this usage, there is no way to determine
which share class belongs to which fund/sub fund from the message content itself, which may not be
desirable and the use of this kind of combination should be bilaterally agreed.
This message allows the report provider to report cash movements in or out of a fund, but does not
allow the Sender to categorise these movements, for example by country, or to give details of the
underlying orders, commission or charges.
If the report provider wishes to give detailed information related to cash movements, then the
FundDetailedConfirmedCashForecastReport message must be used.
Outline
The FundConfirmedCashForecastReportV04 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. MessageIdentification
Approved by the Securities SEG on 27 January 2026 camt.041.001.04
FundConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 105 May 2026
```

## File page 106

```text
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
G. FundCashForecastDetails
Information related to the cash-in and cash-out flows for a specific trade date as a result of
transactions in shares in an investment fund, for example, subscriptions, redemptions or switches.
H. ConsolidatedNetCashForecast
Estimated net cash as a result of the cash-in and cash-out flows.
I. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 camt.041.001.04
FundConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 106 May 2026
```

