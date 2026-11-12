---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "14.4 Message Building Blocks", "14.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "14.4.2.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [221]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.044.001.03"]
---

# 14.4.2.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 221 to 221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 221

```text
14.4.2.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice messages.
Usage:
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
14.4.2.2  Identification <Id>
Presence: [1..1]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
14.4.2.3  FinancialInstrumentClassification <FinInstrmClssfctn>
Presence: [0..1]
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
14.4.2.4  FullName <FullNm>
Presence: [0..1]
Definition: Full name of the reporting entity.
Datatype: "Max350Text" on page 455
14.4.2.5  TradingVenue <TradgVn>
Presence: [0..1]
Definition: Segment MIC for the trading venue where applicable, otherwise the operational MIC.
Datatype: "MICIdentifier" on page 451
14.4.2.6  ReportingPeriod <RptgPrd>
Presence: [0..1]
Definition: Period to which the quantitative data fields relate.
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
221 July 2025
```

