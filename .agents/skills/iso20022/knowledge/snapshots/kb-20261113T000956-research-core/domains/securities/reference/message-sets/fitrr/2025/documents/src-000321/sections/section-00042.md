---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["5 auth.032.001.01 FinancialInstrumentReportingEquityTransparencyDataReportV01", "5.4 Message Building Blocks", "5.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "5.4.2.4 TradingVenue <TradgVn>"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.032.001.01"]
---

# 5.4.2.4 TradingVenue <TradgVn>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 52

```text
Definition: Full name or description of the financial instrument.
Datatype: "Max350Text" on page 455
5.4.2.4  TradingVenue <TradgVn>
Presence: [0..1]
Definition: Segment MIC for the trading venue where applicable, otherwise the operational MIC.
Datatype: "MICIdentifier" on page 451
5.4.2.5  ReportingDate <RptgDt>
Presence: [0..1]
Definition: Date for which the data is provided.
Datatype: "ISODate" on page 449
5.4.2.6  FinancialInstrumentClassification <FinInstrmClssfctn>
Presence: [1..1]
Definition: Specifies the classification of the equity instrument.
Datatype: "EquityInstrumentReportingClassification1Code" on page 435
CodeName Name Definition
SHRS Share Contract is of type shares.
OTHR Other Contract is of type other equity-like
financial instrument.
ETFS ElectronicTradedFund Contract is of type electronic traded
funds.
DPRS DepositaryReceipt Contract is of type depositary receipt.
CRFT Certificate Contract is of type certificates.
5.4.2.7  NumberOutstandingInstruments <NbOutsdngInstrms>
Presence: [0..1]
Definition: For shares and depositary receipts, the total number of outstanding instruments.
For ETFs, the number of units issued for trading.
Datatype: "DecimalNumberFraction5" on page 452
5.4.2.8  HoldingsExceedingTotalVotingRightThreshold
<HldgsExcdgTtlVtngRghtThrshld>
Presence: [0..1]
Definition: The total number of shares corresponding to holdings exceeding 5% of total voting rights of
the issuer unless such a holding is held by a collective investment undertaking or a pension fund. This
field is to be populated only when actual information is known.
Datatype: "DecimalNumberFraction5" on page 452
Approved by the Securities SEG on 17 July 2025 auth.032.001.01
FinancialInstrumentReportingEquityTransparencyD
ataReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
52 July 2025
```

