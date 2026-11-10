---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["20 auth.053.001.01 FinancialInstrumentReportingTradingVolumeCapResultReportV01", "20.4 Message Building Blocks", "20.4.2 VolumeCapResult <VolCapRslt>", "20.4.2.2 ReportingPeriod <RptgPrd>"]
file_pages: [265]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.053.001.01"]
---

# 20.4.2.2 ReportingPeriod <RptgPrd>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 265 to 265.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 265

```text
20.4.2.2  ReportingPeriod <RptgPrd>
Presence: [1..1]
Definition: Date or date range the report relates to.
ReportingPeriod <RptgPrd> contains one of the following elements (see "Period4Choice" on
page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 322
Or   FromDate <FrDt> [1..1] Date 323
Or   ToDate <ToDt> [1..1] Date 323
Or}   FromDateToDate <FrDtToDt> [1..1] ± 323
20.4.2.3  LastUpdateDate <LastUpdDt>
Presence: [0..1]
Definition: Last date for which the data was updated for this instrument and reporting period.
Datatype: "ISODate" on page 449
20.4.2.4  TotalTradingVolume <TtlTradgVol>
Presence: [1..1]
Definition: Total traded volume of the instrument in this specific reporting period.
Impacted by: C1 "ActiveCurrency", C3 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 415
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
20.4.2.5  TradingUnderWaiverPercentage <TradgUdrWvrPctg>
Presence: [1..1]
Definition: Total percentage of trading under waiver of the instrument in this specific reporting period.
Datatype: "PercentageRate" on page 454
20.4.2.6  TradingUnderWaiverBreakdown <TradgUdrWvrBrkdwn>
Presence: [0..*]
Approved by the Securities SEG on 17 July 2025 auth.053.001.01
FinancialInstrumentReportingTradingVolumeCapRe
sultReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
265 July 2025
```

