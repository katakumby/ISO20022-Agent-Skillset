---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["18 camt.019.001.07 ReturnBusinessDayInformationV07", "18.4 Message Building Blocks", "18.4.2 ReportOrError <RptOrErr>", "18.4.2.1 BusinessReport <BizRpt>", "18.4.2.1.2 BusinessDayOrError <BizDayOrErr>", "18.4.2.1.2.2 BusinessError <BizErr>", "18.4.2.1.2.2.1 Error <Err>"]
file_pages: [555]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.019.001.07"]
---

# 18.4.2.1.2.2.1 Error <Err>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 555 to 555.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 555

```text
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  555
{Or     Code <Cd> [1..1] CodeSet 555
Or}     Proprietary <Prtry> [1..1] Text 555
   Description <Desc> [0..1] Text 555
18.4.2.1.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 555
Or}   Proprietary <Prtry> [1..1] Text 555
18.4.2.1.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 857
18.4.2.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 889
18.4.2.1.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 888
18.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Indicates that an operational error has been issued during the processing of the related
request.
Approved by the Payments SEG on 04 February 2025 camt.019.001.07
ReturnBusinessDayInformationV07
Cash Management - Maintenance 2024 - 2025 555 February 2025
```

