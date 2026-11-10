---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["11 auth.041.001.01 FinancialInstrumentReportingNonEquityTradingActivityReportV01", "11.4 Message Building Blocks", "11.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "11.4.2.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [181]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.041.001.01"]
---

# 11.4.2.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 181 to 181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 181

```text
Constraints
• ValidISINRule
ISIN code must pass checksum validation.
• ValidMICRule
Market Identification code must be an active market at the time of reporting.
11.4.2.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice messages.
Usage:
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
11.4.2.2  Identification <Id>
Presence: [1..1]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
11.4.2.3  ReportingDate <RptgDt>
Presence: [0..1]
Definition: Date to which the quantitative data fields below relate.
Datatype: "ISODate" on page 449
11.4.2.4  TradingVenue <TradgVn>
Presence: [0..1]
Definition: Segment MIC for the trading venue where applicable, otherwise the operational MIC.
Datatype: "MICIdentifier" on page 451
11.4.2.5  Suspension <Sspnsn>
Presence: [1..1]
Definition: Indicates whether the instrument was suspended for trading on that trading venue on the
reporting day.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
Approved by the Securities SEG on 17 July 2025 auth.041.001.01
FinancialInstrumentReportingNonEquityTradingActi
vityReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
181 July 2025
```

