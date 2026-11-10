---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04"]
file_pages: [116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.042.001.04"]
---

# 9 camt.042.001.04 FundDetailedEstimatedCashForecastReportV04

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 116 to 116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 116

```text
9 camt.042.001.04
FundDetailedEstimatedCashForecastReportV
04
9.1 MessageDefinition Functionality
Scope
A report provider, such as a transfer agent, sends the FundDetailedEstimatedCashForecastReport
message to the report user, such as an investment manager or pricing agent, to report the estimated
cash incomings and outgoings, sorted by country, institution name or other criteria defined by the user
of one or more share classes of an investment fund on one or more trade dates.
The cash movements may result from, for example, redemption, subscription, switch transactions or
reinvestment of dividends.
Usage
The FundDetailedEstimatedCashForecastReport is used to provide estimated cash movements, that is,
it is sent prior to the cut-off time and/or the price valuation of the fund. The message contains incoming
and outgoing cash flows that are estimated, that is, the price has not been applied. If the price is
definitive, then the FundDetailedConfirmedCashForecastReport message must be used.
The message structure allows for the following uses:
- to provide cash in and cash out amounts for a fund/sub fund and one or more share classes (a
FundOrSubFundDetails sequence and one or more EstimatedFundCashForecastDetails sequences are
used),
- to provide cash in and cash out amounts for one or more share classes (one or more
EstimatedFundCashForecastDetails sequences are used).
If the report is to provide estimated cash in and cash out for a fund/sub fund only and not for one or
more share classes, then the FundEstimatedCashForecastReport message must be used.
The FundDetailedEstimatedCashForecastReport message is used to report cash movements in or out
of a fund, organised by party, such as fund management company, country, currency or by some other
criteria defined by the report provider. If the report is used to give the cash-in and cash-out for a party,
then additional criteria, such as currency and country, can be specified.
In addition, the underlying transaction type for the cash-in or cash-out movement can be specified, as
well as information about the cash movement's underlying orders, such as commission and charges.
Outline
The FundDetailedEstimatedCashForecastReportV04 MessageDefinition is composed of 9
MessageBuildingBlocks:
A. MessageIdentification
Identifies the message.
B. PoolReference
Approved by the Securities SEG on 27 January 2026 camt.042.001.04
FundDetailedEstimatedCashForecastReportV04
Investment Funds - Maintenance 2025 - 2026 116 May 2026
```

