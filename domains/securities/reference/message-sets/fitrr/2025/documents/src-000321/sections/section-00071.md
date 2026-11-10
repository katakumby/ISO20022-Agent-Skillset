---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["7 auth.035.001.01 FinancialInstrumentReportingTradingVolumeCapDataReportV01", "7.4 Message Building Blocks"]
file_pages: [87]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.035.001.01"]
---

# 7.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 87 to 87.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 87

```text
C6 ValidMICRule
Where populated, the market identification code must be an active market at the time of
reporting.
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 ReportHeader <RptHdr>
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
7.4.2 VolumeCapData <VolCapData>
Presence: [1..*]
Definition: Provides details on the volume of trades of financial instruments.
Impacted by: C6 "ValidMICRule"
VolumeCapData <VolCapData> contains the following VolumeCapReport1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportingPeriod <RptgPrd> [0..1] ± 88
   TradingVenue <TradgVn> [0..1] IdentifierSet 88
   InstrumentReport <InstrmRpt> [1..*]  C4 88
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 89
     Identification <Id> [1..1] IdentifierSet 89
     Currency <Ccy> [1..1] CodeSet C1 89
     TotalTradingVolume <TtlTradgVol> [1..1] Amount 89
     TotalReferencePriceTradingVolume
<TtlRefPricTradgVol>
[1..1] Amount 89
     TotalNegotiatedTransactionsTradingVolume
<TtlNgtdTxsTradgVol>
[1..1] Amount 90
Approved by the Securities SEG on 17 July 2025 auth.035.001.01
FinancialInstrumentReportingTradingVolumeCapDa
taReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
87 July 2025
```

