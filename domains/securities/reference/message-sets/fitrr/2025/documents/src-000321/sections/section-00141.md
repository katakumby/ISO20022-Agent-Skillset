---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["10 auth.040.001.01 FinancialInstrumentReportingEquityTradingActivityReportV01", "10.4 Message Building Blocks", "10.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "10.4.2.7 TransactionsExecutedExcludingPreTradeWaiver <TxsExctdExclgPreTradWvr>"]
file_pages: [175]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.040.001.01"]
---

# 10.4.2.7 TransactionsExecutedExcludingPreTradeWaiver <TxsExctdExclgPreTradWvr>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 175 to 175.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 175

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
10.4.2.7  TransactionsExecutedExcludingPreTradeWaiver
<TxsExctdExclgPreTradWvr>
Presence: [1..1]
Definition: Details all transactions that have been performed under a pre-trade Waiver.
TransactionsExecutedExcludingPreTradeWaiver <TxsExctdExclgPreTradWvr> contains the
following NumberAndVolume2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] Quantity 175
   Volume <Vol> [1..1] Amount C1, C3 175
10.4.2.7.1  Number <Nb>
Presence: [1..1]
Definition: Total number of specific transaction types executed on the reporting day.
Datatype: "DecimalNumberFraction5" on page 452
10.4.2.7.2  Volume <Vol>
Presence: [1..1]
Definition: Total volume of specific transactions executed on the reporting day.
Impacted by: C1 "ActiveOrHistoricCurrency", C3 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 416
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 17 July 2025 auth.040.001.01
FinancialInstrumentReportingEquityTradingActivityR
eportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
175 July 2025
```

