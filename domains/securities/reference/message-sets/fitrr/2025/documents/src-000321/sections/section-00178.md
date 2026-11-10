---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "14.2 Structure"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.044.001.03"]
---

# 14.2 Structure

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

```text
14.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgEqtyTradgActvtyRslt> [1..1]  
   ReportHeader <RptHdr> [1..1] ± 219
   EquityTransparencyData <EqtyTrnsprncyData> [1..*]  C5, C7 219
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 221
     Identification <Id> [1..1] IdentifierSet 221
     FinancialInstrumentClassification <FinInstrmClssfctn> [0..1] CodeSet 221
     FullName <FullNm> [0..1] Text 221
     TradingVenue <TradgVn> [0..1] IdentifierSet 221
     ReportingPeriod <RptgPrd> [0..1] ± 221
     ApplicationPeriod <ApplPrd> [0..1] ± 222
     Liquidity <Lqdty> [0..1] Indicator 222
     Methodology <Mthdlgy> [0..1] CodeSet 222
     Statistics <Sttstcs> [0..1]  223
       AverageDailyTurnover <AvrgDalyTrnvr> [0..1] Amount C1, C3 223
       AverageTransactionValue <AvrgTxVal> [0..1] Amount C1, C3 224
       LargeInScale <LrgInScale> [0..1] Quantity 224
       StandardMarketSize <StdMktSz> [0..1] Quantity 224
       AverageDailyNumberOfTransactions <AvrgDalyNbOfTxs> [0..1] Quantity 224
       TotalNumberOfTransactionsExecuted <TtlNbOfTxsExctd> [0..1] Quantity 224
       TotalVolumeOfTransactionsExecuted <TtlVolOfTxsExctd> [0..1] Quantity 225
       TotalNumberOfTradingDays <TtlNbOfTradgDays> [0..1] Quantity 225
     RelevantMarket <RlvntMkt> [0..1]  C8 225
       Identification <Id> [1..1] IdentifierSet 225
       AverageDailyNumberOfTransactions <AvrgDalyNbOfTxs> [0..1] Quantity 225
   SupplementaryData <SplmtryData> [0..*] ± C4 225
14.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
218 July 2025
```

