---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.10 StandingOrder <StgOrdr>", "3.4.2.1.2.1.10.14 ExecutionType <ExctnTp>", "3.4.2.1.2.1.10.14.1 Time <Tm>"]
file_pages: [87]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.10.14.1 Time <Tm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 87 to 87.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 87

```text
ExecutionType <ExctnTp> contains one of the following ExecutionType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Time <Tm> [1..1] Time 87
Or}   Event <Evt> [1..1]  87
{Or     Code <Cd> [1..1] CodeSet 87
Or}     Proprietary <Prtry> [1..1] Text 87
3.4.2.1.2.1.10.14.1  Time <Tm>
Presence: [1..1]
Definition: Execution type is executed based on a time trigger.
Datatype: "ISOTime" on page 891
3.4.2.1.2.1.10.14.2  Event <Evt>
Presence: [1..1]
Definition: Execution type is executed based on an event driven trigger.
Event <Evt> contains one of the following EventType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 87
Or}   Proprietary <Prtry> [1..1] Text 87
3.4.2.1.2.1.10.14.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of the event, in a coded form as published in an external list.
Datatype: "ExternalSystemEventType1Code" on page 857
3.4.2.1.2.1.10.14.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of the event, in a free text form.
Datatype: "Max35Text" on page 889
3.4.2.1.2.1.10.15  Creditor <Cdtr>
Presence: [0..1]
Definition: Party to which an amount of money is due.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 87 February 2025
```

