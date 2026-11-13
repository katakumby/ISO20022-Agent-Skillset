---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["10 auth.040.001.01 FinancialInstrumentReportingEquityTradingActivityReportV01", "10.4 Message Building Blocks", "10.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "10.4.2.8 TransactionsExecutedExcludingPostTradeLargeInScaleWaiver <TxsExctdExclgPstTradLrgInScaleWvr>"]
file_pages: [176, 177]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.040.001.01"]
---

# 10.4.2.8 TransactionsExecutedExcludingPostTradeLargeInScaleWaiver <TxsExctdExclgPstTradLrgInScaleWvr>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 176 to 177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 176

```text
Note: The decimal separator is a dot.
10.4.2.8  TransactionsExecutedExcludingPostTradeLargeInScaleWaiver
<TxsExctdExclgPstTradLrgInScaleWvr>
Presence: [1..1]
Definition: Details all transactions that have been performed under a post-trade large in scale waivers.
TransactionsExecutedExcludingPostTradeLargeInScaleWaiver
<TxsExctdExclgPstTradLrgInScaleWvr> contains the following NumberAndVolume2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] Quantity 176
   Volume <Vol> [1..1] Amount C1, C3 176
10.4.2.8.1  Number <Nb>
Presence: [1..1]
Definition: Total number of specific transaction types executed on the reporting day.
Datatype: "DecimalNumberFraction5" on page 452
10.4.2.8.2  Volume <Vol>
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
Note: The decimal separator is a dot.
10.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C4 "SupplementaryDataRule"
Approved by the Securities SEG on 17 July 2025 auth.040.001.01
FinancialInstrumentReportingEquityTradingActivityR
eportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
176 July 2025
```

## File page 177

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 341
   Envelope <Envlp> [1..1] (External Schema) 341
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 July 2025 auth.040.001.01
FinancialInstrumentReportingEquityTradingActivityR
eportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
177 July 2025
```

