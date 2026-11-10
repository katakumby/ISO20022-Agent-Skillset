---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01", "11.4 Message Building Blocks", "11.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "11.4.2.6 NumberTransactions <NbTxs>"]
file_pages: [182]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.041.001.01"]
---

# 11.4.2.6 NumberTransactions <NbTxs>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 182 to 182.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 182

```text
11.4.2.6  NumberTransactions <NbTxs>
Presence: [0..1]
Definition: Total number of transactions executed on the reporting day for the instrument.
Datatype: "Number" on page 453
11.4.2.7  AggregatedQuantitativeData <AggtdQttvData>
Presence: [0..*]
Definition: Aggregated quantitative data on the non-equity instrument being reported. Details
aggregated against the specific range that is defined. Transactions that have been cancelled should be
excluded from the reported figure.
AggregatedQuantitativeData <AggtdQttvData> contains the following TransactionsBin2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NumberOfTransactions <NbOfTxs> [1..1] Quantity 182
   TotalNotionalAmount <TtlNtnlAmt> [1..1] Quantity 182
   Range <Rg> [1..1]  182
     FromQuantity <FrQty> [1..1] Quantity 183
     ToQuantity <ToQty> [1..1] Quantity 183
11.4.2.7.1  NumberOfTransactions <NbOfTxs>
Presence: [1..1]
Definition: Total number of transactions executed for that bin. Transactions that have been cancelled
should be excluded from the reported figure.
Datatype: "Number" on page 453
11.4.2.7.2  TotalNotionalAmount <TtlNtnlAmt>
Presence: [1..1]
Definition: Total notional amount traded represented by all transactions executed on the reporting day
which size lies in the bin's range, expressed in the currency as specified in the local regulation (except
for emission allowances and emission allowance derivatives: tons of carbon dioxide). Transactions that
have been cancelled should be excluded from the reported figure.
Datatype: "DecimalNumber" on page 451
11.4.2.7.3  Range <Rg>
Presence: [1..1]
Definition: Specific range the quantitative data relates to. Only allowed ranges must be used.
Approved by the Securities SEG on 17 July 2025 auth.041.001.01
FinancialInstrumentReportingNonEquityTradingActi
vityReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
182 July 2025
```

