---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.6 Date Time Period", "16.1.6.1 Period18", "16.1.6.1.2 EndDate <EndDt>", "16.1.6.1.2.1 Date <Dt>"]
file_pages: [853]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.6.1.2.1 Date <Dt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 853 to 853.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 853

```text
EndDate <EndDt> contains one of the following DateFormat73Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 853
Or}   NotSpecifiedDate <NotSpcfdDt> [1..1] CodeSet 853
16.1.6.1.2.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as an ISO Date.
Datatype: "ISODate" on page 1243
16.1.6.1.2.2  NotSpecifiedDate <NotSpcfdDt>
Presence: [1..1]
Definition: Date not specified, for example, the date is unknown.
Datatype: "DateType8Code" on page 1206
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
ONGO Ongoing Ongoing basis, which indicates that the
date is determined by "ongoing basis"
process, for example "au fil de l'eau".
16.1.6.2  DateTimePeriod1
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 853
   ToDateTime <ToDtTm> [1..1] DateTime 853
16.1.6.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the period starts.
Datatype: "ISODateTime" on page 1243
16.1.6.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the period ends.
Datatype: "ISODateTime" on page 1243
16.1.6.3  DateOrDateTimePeriod1Choice
Definition: Choice between a date or a date and time format for a period.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 853 February 2026
```

