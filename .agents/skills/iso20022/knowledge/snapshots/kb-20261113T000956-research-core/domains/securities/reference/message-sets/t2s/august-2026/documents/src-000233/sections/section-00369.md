---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["19 camt.081.001.02 IntraBalanceMovementModificationReportV02", "19.4 Message Building Blocks", "19.4.4 ReportOrError <RptOrErr>", "19.4.4.2 OperationalError <OprlErr>", "19.4.4.2.2 Description <Desc>"]
file_pages: [476]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.081.001.02"]
---

# 19.4.4.2.2 Description <Desc>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 476 to 476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 476

```text
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 3328
19.4.4.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 3326
19.4.5 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C25 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.081.001.02
IntraBalanceMovementModificationReportV02
Target2-Securities 476 August 2026
```

