---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.4 Date Period", "16.1.4.2 DatePeriod2"]
file_pages: [842]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.4.2 DatePeriod2

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 842 to 842.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 842

```text
16.1.4.2  DatePeriod2
Definition: Range of time defined by a start date and an end date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 842
   ToDate <ToDt> [1..1] Date 842
16.1.4.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 1243
16.1.4.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 1243
16.1.5 Date Time
16.1.5.1  DateFormat30Choice
Definition: Choice between an ISODate format or a date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
16.1.5.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Datatype: "ISODate" on page 1243
16.1.5.1.2  DateCode <DtCd>
Presence: [1..1]
Definition: Specifies the type of date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 842 February 2026
```

