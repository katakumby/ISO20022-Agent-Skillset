---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "14.4 Message Building Blocks", "14.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "14.4.2.10 Statistics <Sttstcs>", "14.4.2.10.7 TotalVolumeOfTransactionsExecuted <TtlVolOfTxsExctd>"]
file_pages: [225, 226]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.044.001.03"]
---

# 14.4.2.10.7 TotalVolumeOfTransactionsExecuted <TtlVolOfTxsExctd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 225 to 226.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 225

```text
14.4.2.10.7  TotalVolumeOfTransactionsExecuted <TtlVolOfTxsExctd>
Presence: [0..1]
Definition: Total volume of transactions that have been performed on this market.
Datatype: "DecimalNumber" on page 451
14.4.2.10.8  TotalNumberOfTradingDays <TtlNbOfTradgDays>
Presence: [0..1]
Definition: The total number of trading days for which the data is provided.
Datatype: "Number" on page 453
14.4.2.11  RelevantMarket <RlvntMkt>
Presence: [0..1]
Definition: Specific market details related to the most relevant market in terms of liquidity.
Impacted by: C8 "ValidMICRule"
RelevantMarket <RlvntMkt> contains the following MarketDetail2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] IdentifierSet 225
   AverageDailyNumberOfTransactions
<AvrgDalyNbOfTxs>
[0..1] Quantity 225
Constraints
• ValidMICRule
Market Identification code must be an active market at the time of reporting.
14.4.2.11.1  Identification <Id>
Presence: [1..1]
Definition: Most relevant market in terms of liquidity as defined in the local regulation.
Datatype: "MICIdentifier" on page 451
14.4.2.11.2  AverageDailyNumberOfTransactions <AvrgDalyNbOfTxs>
Presence: [0..1]
Definition: Average daily number of transactions that have been performed on the most relevant market
in terms of liquidity.
Datatype: "DecimalNumber" on page 451
14.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C4 "SupplementaryDataRule"
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
225 July 2025
```

## File page 226

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
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
226 July 2025
```

