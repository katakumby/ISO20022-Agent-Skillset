---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "14.4 Message Building Blocks", "14.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "14.4.2.10 Statistics <Sttstcs>", "14.4.2.10.2 AverageTransactionValue <AvrgTxVal>"]
file_pages: [224]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.044.001.03"]
---

# 14.4.2.10.2 AverageTransactionValue <AvrgTxVal>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 224 to 224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 224

```text
14.4.2.10.2  AverageTransactionValue <AvrgTxVal>
Presence: [0..1]
Definition: Average value of the transactions for the instrument in Euro.
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
14.4.2.10.3  LargeInScale <LrgInScale>
Presence: [0..1]
Definition: Large in scale order in respect of a share, depositary receipt, certificate or other similar
financial instrument shall be considered large in scale compared with normal market size if, on the basis
of the average daily turnover for that financial instrument, the order is equal to or larger than the
minimum size of orders set out in the local regulation.
Datatype: "DecimalNumber" on page 451
14.4.2.10.4  StandardMarketSize <StdMktSz>
Presence: [0..1]
Definition: Standard market size for shares, depositary receipts, ETFs, certificates and other similar
financial instruments for which there is a liquid market shall be determined on the basis of the average
value of transactions for each financial instrument and in accordance with the local regulation.
Datatype: "DecimalNumber" on page 451
14.4.2.10.5  AverageDailyNumberOfTransactions <AvrgDalyNbOfTxs>
Presence: [0..1]
Definition: Average daily number of transactions that have been performed on this market.
Datatype: "DecimalNumber" on page 451
14.4.2.10.6  TotalNumberOfTransactionsExecuted <TtlNbOfTxsExctd>
Presence: [0..1]
Definition: Total number of transactions that have been performed on this market.
Datatype: "DecimalNumber" on page 451
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
224 July 2025
```

