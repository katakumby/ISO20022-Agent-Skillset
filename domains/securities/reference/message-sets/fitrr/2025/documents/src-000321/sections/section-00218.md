---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["20 auth.053.001.01 FinancialInstrumentReportingTradingVolumeCapResultReportV01", "20.4 Message Building Blocks"]
file_pages: [264]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.053.001.01"]
---

# 20.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 264 to 264.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 264

```text
20.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
20.4.1 ReportHeader <RptHdr>
Presence: [1..1]
Definition: Header information related to the global report.
ReportHeader <RptHdr> contains the following elements (see "SecuritiesMarketReportHeader1" on
page 411 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportingEntity <RptgNtty> [1..1] ± C19 411
   ReportingPeriod <RptgPrd> [1..1] ± 411
   SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 411
20.4.2 VolumeCapResult <VolCapRslt>
Presence: [1..*]
Definition: Provides details on the volume of trades and percentage of trading under waivers of financial
instruments.
VolumeCapResult <VolCapRslt> contains the following VolumeCapResult1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet 264
   ReportingPeriod <RptgPrd> [1..1] ± 265
   LastUpdateDate <LastUpdDt> [0..1] Date 265
   TotalTradingVolume <TtlTradgVol> [1..1] Amount C1, C3 265
   TradingUnderWaiverPercentage <TradgUdrWvrPctg> [1..1] Rate 265
   TradingUnderWaiverBreakdown
<TradgUdrWvrBrkdwn>
[0..*]  265
     TradingUnderWaiverPercentage <TradgUdrWvrPctg> [1..1] Rate 266
     TradingVenue <TradgVn> [1..1] IdentifierSet 266
     Disclaimer <Dsclmr> [0..1] Text 266
   Disclaimer <Dsclmr> [0..1] Text 266
20.4.2.1  Identification <Id>
Presence: [1..1]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
Approved by the Securities SEG on 17 July 2025 auth.053.001.01
FinancialInstrumentReportingTradingVolumeCapRe
sultReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
264 July 2025
```

