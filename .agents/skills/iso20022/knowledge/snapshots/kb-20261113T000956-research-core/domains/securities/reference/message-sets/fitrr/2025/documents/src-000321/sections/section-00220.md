---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["20 auth.053.001.01 FinancialInstrumentReportingTradingVolumeCapResultReportV01", "20.4 Message Building Blocks", "20.4.2 VolumeCapResult <VolCapRslt>", "20.4.2.6 TradingUnderWaiverBreakdown <TradgUdrWvrBrkdwn>", "20.4.2.6.1 TradingUnderWaiverPercentage <TradgUdrWvrPctg>"]
file_pages: [266, 267]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.053.001.01"]
---

# 20.4.2.6.1 TradingUnderWaiverPercentage <TradgUdrWvrPctg>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 266 to 267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 266

```text
Definition: Percentage of trading under waiver of the instrument in this specific reporting period broken
down by trading venue.
TradingUnderWaiverBreakdown <TradgUdrWvrBrkdwn> contains the following
TradingUnderWaiversPercentage1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradingUnderWaiverPercentage <TradgUdrWvrPctg> [1..1] Rate 266
   TradingVenue <TradgVn> [1..1] IdentifierSet 266
   Disclaimer <Dsclmr> [0..1] Text 266
20.4.2.6.1  TradingUnderWaiverPercentage <TradgUdrWvrPctg>
Presence: [1..1]
Definition: Total percentage of trading under waiver of the instrument in this specific reporting period on
this trading venue.
Datatype: "PercentageRate" on page 454
20.4.2.6.2  TradingVenue <TradgVn>
Presence: [1..1]
Definition: The venue this trading under waiver percentage is in relation to.
Datatype: "MICIdentifier" on page 451
20.4.2.6.3  Disclaimer <Dsclmr>
Presence: [0..1]
Definition: Information for interpreting the result.
Datatype: "Max350Text" on page 455
20.4.2.7  Disclaimer <Dsclmr>
Presence: [0..1]
Definition: Information for interpreting the result.
Datatype: "Max350Text" on page 455
20.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C4 "SupplementaryDataRule"
Approved by the Securities SEG on 17 July 2025 auth.053.001.01
FinancialInstrumentReportingTradingVolumeCapRe
sultReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
266 July 2025
```

## File page 267

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
Approved by the Securities SEG on 17 July 2025 auth.053.001.01
FinancialInstrumentReportingTradingVolumeCapRe
sultReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
267 July 2025
```

