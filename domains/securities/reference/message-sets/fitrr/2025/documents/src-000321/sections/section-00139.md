---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["10 auth.040.001.01 FinancialInstrumentReportingEquityTradingActivityReportV01", "10.4 Message Building Blocks", "10.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "10.4.2.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [173]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.040.001.01"]
---

# 10.4.2.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 173 to 173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 173

```text
EquityTransparencyData <EqtyTrnsprncyData> contains the following TransparencyDataReport13
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   TransactionsExecutedExcludingPostTradeLargeInSc
aleWaiver <TxsExctdExclgPstTradLrgInScaleWvr>
[1..1]  176
     Number <Nb> [1..1] Quantity 176
     Volume <Vol> [1..1] Amount C1, C3 176
Constraints
• ValidISINRule
ISIN code must pass checksum validation.
• ValidMICRule
Market Identification code must be an active market at the time of reporting.
10.4.2.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice messages.
Usage:
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
10.4.2.2  Identification <Id>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 auth.040.001.01
FinancialInstrumentReportingEquityTradingActivityR
eportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
173 July 2025
```

