---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.2 OperationalError <OprlErr>", "18.4.2.2.1 Error <Err>"]
file_pages: [556, 557]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.2.1 Error <Err>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 556 to 557.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 556

```text
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  556
{Or     Code <Cd> [1..1] CodeSet 556
Or}     Proprietary <Prtry> [1..1] Text 556
   Description <Desc> [0..1] Text 556
18.4.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 556
Or}   Proprietary <Prtry> [1..1] Text 556
18.4.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 857
18.4.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 889
18.4.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 888
18.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 556 February 2025
```

## File page 557

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 557 February 2025
```

