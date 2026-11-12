---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["19 auth.050.001.01 FinancialInstrumentReportingInstrumentClassificationReportV01", "19.4 Message Building Blocks", "19.4.1 InstrumentClassification <InstrmClssfctn>", "19.4.1.4 LastUpdated <LastUpdtd>"]
file_pages: [261]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.050.001.01"]
---

# 19.4.1.4 LastUpdated <LastUpdtd>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 261 to 261.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 261

```text
ValidityPeriod <VldtyPrd> contains one of the following elements (see "Period4Choice" on page 322
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 322
Or   FromDate <FrDt> [1..1] Date 323
Or   ToDate <ToDt> [1..1] Date 323
Or}   FromDateToDate <FrDtToDt> [1..1] ± 323
19.4.1.4  LastUpdated <LastUpdtd>
Presence: [0..1]
Definition: Date when this record was last modified.
Datatype: "ISODate" on page 449
19.4.2 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C1 "SupplementaryDataRule"
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
Approved by the Securities SEG on 17 July 2025 auth.050.001.01
FinancialInstrumentReportingInstrumentClassificatio
nReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
261 July 2025
```

