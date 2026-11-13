---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["5 auth.032.001.01 FinancialInstrumentReportingEquityTransparencyDataReportV01", "5.4 Message Building Blocks", "5.4.2 EquityTransparencyData <EqtyTrnsprncyData>", "5.4.2.1 TechnicalRecordIdentification <TechRcrdId>"]
file_pages: [51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.032.001.01"]
---

# 5.4.2.1 TechnicalRecordIdentification <TechRcrdId>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 51 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
EquityTransparencyData <EqtyTrnsprncyData> contains the following TransparencyDataReport11
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 51
   Identification <Id> [1..1] IdentifierSet 51
   FullName <FullNm> [0..1] Text 51
   TradingVenue <TradgVn> [0..1] IdentifierSet 52
   ReportingDate <RptgDt> [0..1] Date 52
   FinancialInstrumentClassification <FinInstrmClssfctn> [1..1] CodeSet 52
   NumberOutstandingInstruments <NbOutsdngInstrms> [0..1] Quantity 52
   HoldingsExceedingTotalVotingRightThreshold
<HldgsExcdgTtlVtngRghtThrshld>
[0..1] Quantity 52
   IssuanceSize <IssncSz> [0..1] Amount C1, C3 53
   InstrumentPrice <InstrmPric> [0..1] Amount C1 53
Constraints
• ValidISINRule
ISIN code must pass checksum validation.
• ValidMICRule
Where reported, Market Identification code must be an active market for that reporting period.
5.4.2.1  TechnicalRecordIdentification <TechRcrdId>
Presence: [0..1]
Definition: Unique identifier of a record in a message used as part of error management and status
advice messages.
Usage:
This identification will be used in the status advice report sent back.
Datatype: "Max35Text" on page 456
5.4.2.2  Identification <Id>
Presence: [1..1]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
5.4.2.3  FullName <FullNm>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 auth.032.001.01
FinancialInstrumentReportingEquityTransparencyD
ataReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
51 July 2025
```

