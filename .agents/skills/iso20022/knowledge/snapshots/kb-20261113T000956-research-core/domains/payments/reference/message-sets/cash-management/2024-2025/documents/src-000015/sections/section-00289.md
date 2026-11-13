---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>", "9.4.2.1 BusinessReport <BizRpt>", "9.4.2.1.2 DefaultLimit <DfltLmt>", "9.4.2.1.2.2 LimitOrError <LmtOrErr>", "9.4.2.1.2.2.2 BusinessError <BizErr>", "9.4.2.1.2.2.2.1 Error <Err>"]
file_pages: [420]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2.1.2.2.2.1 Error <Err>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 420 to 420.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 420

```text
9.4.2.1.2.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 420
Or}   Proprietary <Prtry> [1..1] Text 420
9.4.2.1.2.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 857
9.4.2.1.2.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 889
9.4.2.1.2.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 888
9.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Indicates that an operational error has been issued during the processing of the related
request.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  420
{Or     Code <Cd> [1..1] CodeSet 421
Or}     Proprietary <Prtry> [1..1] Text 421
   Description <Desc> [0..1] Text 421
9.4.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 420 February 2025
```

