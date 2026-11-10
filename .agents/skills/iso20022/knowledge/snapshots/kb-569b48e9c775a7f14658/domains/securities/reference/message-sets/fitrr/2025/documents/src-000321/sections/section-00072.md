---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["7 auth.035.001.01 FinancialInstrumentReportingTradingVolumeCapDataReportV01", "7.4 Message Building Blocks", "7.4.2 VolumeCapData <VolCapData>", "7.4.2.1 ReportingPeriod <RptgPrd>"]
file_pages: [88]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.035.001.01"]
---

# 7.4.2.1 ReportingPeriod <RptgPrd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 88 to 88.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 88

```text
Constraints
• ValidMICRule
Where populated, the market identification code must be an active market at the time of reporting.
7.4.2.1  ReportingPeriod <RptgPrd>
Presence: [0..1]
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
7.4.2.2  TradingVenue <TradgVn>
Presence: [0..1]
Definition: The venue this report is in relation to specified as {MIC} (segment MIC, where available,
otherwise operational MIC).
Datatype: "MICIdentifier" on page 451
7.4.2.3  InstrumentReport <InstrmRpt>
Presence: [1..*]
Definition: Volume cap data specific to a reporting period.
Impacted by: C4 "ValidISINRule"
InstrumentReport <InstrmRpt> contains the following VolumeCapReport2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
88 July 2025
```

