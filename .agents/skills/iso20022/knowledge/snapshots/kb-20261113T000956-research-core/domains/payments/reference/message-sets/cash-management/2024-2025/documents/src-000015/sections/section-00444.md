---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["22 camt.024.001.08 ModifyStandingOrderV08", "22.4 Message Building Blocks", "22.4.3 NewStandingOrderValueSet <NewStgOrdrValSet>", "22.4.3.6 ExecutionType <ExctnTp>", "22.4.3.6.2 Event <Evt>", "22.4.3.6.2.1 Code <Cd>"]
file_pages: [601]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.024.001.08"]
---

# 22.4.3.6.2.1 Code <Cd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 601 to 601.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 601

```text
Definition: Execution type is executed based on an event driven trigger.
Event <Evt> contains one of the following EventType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 601
Or}   Proprietary <Prtry> [1..1] Text 601
22.4.3.6.2.1  Code <Cd>
Presence: [1..1]
Definition: Type of the event, in a coded form as published in an external list.
Datatype: "ExternalSystemEventType1Code" on page 857
22.4.3.6.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of the event, in a free text form.
Datatype: "Max35Text" on page 889
22.4.3.7  Frequency <Frqcy>
Presence: [0..1]
Definition: Regularity with which payment instructions are to be created and processed as a result of the
standing order, such as daily, weekly, or monthly.
Datatype: "Frequency2Code" on page 858
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QURT Quarterly Event takes place every three months or
four times a year.
MIAN SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place on request or as
necessary.
INDA IntraDay Event takes place several times a day.
OVNG Overnight Event takes place overnight.
22.4.3.8  ValidityPeriod <VldtyPrd>
Presence: [0..1]
Definition: Dates during which the standing order is in effect.
Approved by the Payments SEG on 04 February 2025 camt.024.001.08 ModifyStandingOrderV08
Cash Management - Maintenance 2024 - 2025 601 February 2025
```

