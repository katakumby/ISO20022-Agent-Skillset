---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["2 auth.016.001.03 FinancialInstrumentReportingTransactionReportV03", "2.4 Message Building Blocks", "2.4.2 SupplementaryData <SplmtryData>"]
file_pages: [14]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.016.001.03"]
---

# 2.4.2 SupplementaryData <SplmtryData>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 14 to 14.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 14

```text
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C12 "SupplementaryDataRule"
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
2.4.2 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C12 "SupplementaryDataRule"
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
Approved by the Securities SEG on 17 July 2025 auth.016.001.03
FinancialInstrumentReportingTransactionReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
14 July 2025
```

