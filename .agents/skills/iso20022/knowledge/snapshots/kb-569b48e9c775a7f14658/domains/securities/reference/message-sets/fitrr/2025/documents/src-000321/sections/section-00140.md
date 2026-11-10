---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["10 auth.040.001.01 FinancialInstrumentReportingEquityTradingActivityReportV01", "10.4 Message Building Blocks", "10.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "10.4.2.3 ReportingDate <RptgDt>"]
file_pages: [174]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.040.001.01"]
---

# 10.4.2.3 ReportingDate <RptgDt>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 174 to 174.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 174

```text
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
10.4.2.3  ReportingDate <RptgDt>
Presence: [0..1]
Definition: Date to which the quantitative data fields below relate.
Datatype: "ISODate" on page 449
10.4.2.4  TradingVenue <TradgVn>
Presence: [0..1]
Definition: Segment MIC for the trading venue where applicable, otherwise the operational MIC.
Datatype: "MICIdentifier" on page 451
10.4.2.5  Suspension <Sspnsn>
Presence: [1..1]
Definition: Indicates whether the instrument was suspended for trading on that Trading Venue for the
whole day on the given reporting day.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
10.4.2.6  TransactionsExecuted <TxsExctd>
Presence: [1..1]
Definition: Total number of transactions executed on the reporting day. 
TransactionsExecuted <TxsExctd> contains the following NumberAndVolume2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] Quantity 174
   Volume <Vol> [1..1] Amount C1, C3 174
10.4.2.6.1  Number <Nb>
Presence: [1..1]
Definition: Total number of specific transaction types executed on the reporting day.
Datatype: "DecimalNumberFraction5" on page 452
10.4.2.6.2  Volume <Vol>
Presence: [1..1]
Definition: Total volume of specific transactions executed on the reporting day.
Impacted by: C1 "ActiveOrHistoricCurrency", C3 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 416
Approved by the Securities SEG on 17 July 2025 auth.040.001.01
FinancialInstrumentReportingEquityTradingActivityR
eportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
174 July 2025
```

