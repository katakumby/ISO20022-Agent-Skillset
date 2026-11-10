---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.4 SecuritiesMarketReportHeader1"]
file_pages: [411]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.4 SecuritiesMarketReportHeader1

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 411 to 411.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 411

```text
22.1.13.4  SecuritiesMarketReportHeader1
Definition: Provides the securities market transaction report related header details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportingEntity <RptgNtty> [1..1] ± C19 411
   ReportingPeriod <RptgPrd> [1..1] ± 411
   SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 411
22.1.13.4.1  ReportingEntity <RptgNtty>
Presence: [1..1]
Definition: Identification of the venue which generates the report.
Impacted by: C19 "ValidMICRule"
ReportingEntity <RptgNtty> contains one of the following elements (see
"TradingVenueIdentification1Choice" on page 337 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentificationCode <MktIdCd> [1..1] IdentifierSet 337
Or   NationalCompetentAuthority <NtlCmptntAuthrty> [1..1] CodeSet C4 337
Or}   Other <Othr> [1..1] ± 338
Constraints
• ValidMICRule
Market Identification code must be an active market at the time of reporting.
22.1.13.4.2  ReportingPeriod <RptgPrd>
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
22.1.13.4.3  SubmissionDateTime <SubmissnDtTm>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
411 July 2025
```

