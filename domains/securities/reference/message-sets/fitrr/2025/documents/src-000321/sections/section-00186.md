---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.2 Structure"]
file_pages: [228]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.2 Structure

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 228 to 228.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 228

```text
15.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document>
<FinInstrmRptgNonEqtyTradgActvtyRslt>
[1..1]  
   ReportHeader <RptHdr> [1..1] ± 229
   NonEquityTransparencyData <NonEqtyTrnsprncyData> [1..*]  C5, C7 230
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 232
     Identification <Id> [1..1]  232
{Or       ISINAndSubClass <ISINAndSubClss> [1..1]  233
         ISIN <ISIN> [1..1] IdentifierSet 234
         DerivativeSubClass <DerivSubClss> [0..1]  234
           Description <Desc> [0..1] Text 234
           SegmentationCriteria <SgmttnCrit> [1..*]  234
             CriteriaName <CritNm> [1..1] CodeSet 235
             CriteriaValue <CritVal> [1..1] Text 236
         FinancialInstrumentClassification <FinInstrmClssfctn> [0..1] CodeSet 236
Or}       AssetClassAndSubClass <AsstClssAndSubClss> [1..1]  237
         AssetClass <AsstClss> [1..1] CodeSet 237
         DerivativeSubClass <DerivSubClss> [0..1]  237
           Description <Desc> [0..1] Text 238
           SegmentationCriteria <SgmttnCrit> [1..*]  238
             CriteriaName <CritNm> [1..1] CodeSet 238
             CriteriaValue <CritVal> [1..1] Text 240
         FinancialInstrumentClassification <FinInstrmClssfctn> [0..1] CodeSet 240
     FullName <FullNm> [0..1] Text 240
     TradingVenue <TradgVn> [0..1] IdentifierSet 240
     ReportingPeriod <RptgPrd> [0..1] ± 240
     Liquidity <Lqdty> [0..1] Indicator 241
     PreTradeLargeInScaleThreshold <PreTradLrgInScaleThrshld> [0..1] ± 241
     PostTradeLargeInScaleThreshold
<PstTradLrgInScaleThrshld>
[0..1] ± 241
     PreTradeInstrumentSizeSpecificThreshold
<PreTradInstrmSzSpcfcThrshld>
[0..1] ± 242
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
228 July 2025
```

