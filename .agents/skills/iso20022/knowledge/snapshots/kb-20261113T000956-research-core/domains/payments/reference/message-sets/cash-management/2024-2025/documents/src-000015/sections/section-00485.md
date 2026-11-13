---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["25 camt.047.001.08 ReturnReservationV08", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.1 CurrentReservation <CurRsvatn>", "25.4.2.1.1.2 ReservationOrError <RsvatnOrErr>", "25.4.2.1.1.2.2 BusinessError <BizErr>", "25.4.2.1.1.2.2.1 Error <Err>", "25.4.2.1.1.2.2.1.1 Code <Cd>"]
file_pages: [647]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.047.001.08"]
---

# 25.4.2.1.1.2.2.1.1 Code <Cd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 647 to 647.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 647

```text
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 647
Or}   Proprietary <Prtry> [1..1] Text 647
25.4.2.1.1.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 857
25.4.2.1.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 889
25.4.2.1.1.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 888
25.4.2.1.2  DefaultReservation <DfltRsvatn>
Presence: [0..*]
Definition: Report is given for a default reservation.
Approved by the Payments SEG on 04 February 2025 camt.047.001.08 ReturnReservationV08
Cash Management - Maintenance 2024 - 2025 647 February 2025
```

