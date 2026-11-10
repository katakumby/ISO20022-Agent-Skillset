---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04"]
file_pages: [126, 127]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.043.001.04"]
---

# 10 camt.043.001.04 FundDetailedConfirmedCashForecastReportV04

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 126 to 127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 126

```text
10 camt.043.001.04
FundDetailedConfirmedCashForecastReport
V04
10.1 MessageDefinition Functionality
Scope
A report provider, such as a transfer agent, sends the FundDetailedConfirmedCashForecastReport
message to the report user, such as an investment manager or pricing agent, to report the confirmed
cash incomings and outgoings, sorted by country, institution name or other criteria defined by the user
of one or more share classes of an investment fund on one or more trade dates.
The cash movements may result from, for example, redemption, subscription, switch transactions or
reinvestment of dividends.
Usage
The FundDetailedConfirmedCashForecastReport is used to provide definitive cash movements, that is,
it is sent after the cut-off time and/or the price valuation of the fund.
If the price is not yet definitive, then the FundDetailedEstimatedCashForecastReport message must be
used.
The message structure allows for the following uses:
- to provide cash in and cash out amounts for a fund/sub fund and one or more share classes (a
FundOrSubFundDetails sequence and one or FundCashForecastDetails sequences are used),
- to provide cash in and cash out amounts for one or more share classes (one or more
FundCashForecastDetails sequences are used).
If the report is to provide cash in and cash out for a fund/sub fund only and not for one or more share
classes, then the FundConfirmedCashForecastReport message must be used.
The FundDetailedConfirmedCashForecastReport message is used to report cash movements in or out
of a fund, organised by party, such as fund management company, country, currency or by some other
criteria defined by the report provider. If the report is used to given the cash-in and cash-out for a party,
then additional criteria, such as currency and country, can be specified.
In addition, the underlying transaction type for the cash-in or cash-out movement can be specified, as
well as information about the cash movement's underlying orders, such as commission and charges.
Outline
The FundDetailedConfirmedCashForecastReportV04 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. MessageIdentification
Identifies the message.
B. PoolReference
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 126 May 2026
```

## File page 127

```text
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
The information provided is sorted by pre-defined criteria such as country, institution, currency or
user defined criteria.
H. ConsolidatedNetCashForecast
Net cash as a result of the cash-in and cash-out flows specified in the fund cash forecast details.
I. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 camt.043.001.04
FundDetailedConfirmedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 127 May 2026
```

