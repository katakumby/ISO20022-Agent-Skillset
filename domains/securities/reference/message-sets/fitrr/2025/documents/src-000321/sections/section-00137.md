---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["10 auth.040.001.01 FinancialInstrumentReportingEquityTradingActivityReportV01", "10.2 Structure"]
file_pages: [171]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.040.001.01"]
---

# 10.2 Structure

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 171 to 171.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 171

```text
10.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgEqtyTradgActvtyRpt> [1..1]  
   ReportHeader <RptHdr> [1..1] ± 172
   EquityTransparencyData <EqtyTrnsprncyData> [1..*]  C5, C7 172
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 173
     Identification <Id> [1..1] IdentifierSet 173
     ReportingDate <RptgDt> [0..1] Date 174
     TradingVenue <TradgVn> [0..1] IdentifierSet 174
     Suspension <Sspnsn> [1..1] Indicator 174
     TransactionsExecuted <TxsExctd> [1..1]  174
       Number <Nb> [1..1] Quantity 174
       Volume <Vol> [1..1] Amount C1, C3 174
     TransactionsExecutedExcludingPreTradeWaiver
<TxsExctdExclgPreTradWvr>
[1..1]  175
       Number <Nb> [1..1] Quantity 175
       Volume <Vol> [1..1] Amount C1, C3 175
     TransactionsExecutedExcludingPostTradeLargeInScaleWai
ver <TxsExctdExclgPstTradLrgInScaleWvr>
[1..1]  176
       Number <Nb> [1..1] Quantity 176
       Volume <Vol> [1..1] Amount C1, C3 176
   SupplementaryData <SplmtryData> [0..*] ± C4 176
10.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 17 July 2025 auth.040.001.01
FinancialInstrumentReportingEquityTradingActivityR
eportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
171 July 2025
```

