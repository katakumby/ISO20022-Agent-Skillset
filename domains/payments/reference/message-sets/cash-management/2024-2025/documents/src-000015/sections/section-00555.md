---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>", "31.4.2.1.2.1 StandingOrder <StgOrdr>", "31.4.2.1.2.1.14 ExecutionType <ExctnTp>", "31.4.2.1.2.1.14.1 Time <Tm>"]
file_pages: [727]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.2.1.14.1 Time <Tm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 727 to 727.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 727

```text
ExecutionType <ExctnTp> contains one of the following ExecutionType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Time <Tm> [1..1] Time 727
Or}   Event <Evt> [1..1]  727
{Or     Code <Cd> [1..1] CodeSet 727
Or}     Proprietary <Prtry> [1..1] Text 727
31.4.2.1.2.1.14.1  Time <Tm>
Presence: [1..1]
Definition: Execution type is executed based on a time trigger.
Datatype: "ISOTime" on page 891
31.4.2.1.2.1.14.2  Event <Evt>
Presence: [1..1]
Definition: Execution type is executed based on an event driven trigger.
Event <Evt> contains one of the following EventType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 727
Or}   Proprietary <Prtry> [1..1] Text 727
31.4.2.1.2.1.14.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of the event, in a coded form as published in an external list.
Datatype: "ExternalSystemEventType1Code" on page 857
31.4.2.1.2.1.14.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of the event, in a free text form.
Datatype: "Max35Text" on page 889
31.4.2.1.2.1.15  Creditor <Cdtr>
Presence: [0..1]
Definition: Party to which an amount of money is due.
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 727 February 2025
```

