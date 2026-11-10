---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.12 Date Period", "66.1.12.4 DateTimePeriod2", "66.1.12.4.1 FromDateTime <FrDtTm>"]
file_pages: [4466]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.12.4.1 FromDateTime <FrDtTm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4466 to 4466.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4466

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 4466
   ToDateTime <ToDtTm> [0..1] DateTime 4466
66.1.12.4.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 5388
66.1.12.4.2  ToDateTime <ToDtTm>
Presence: [0..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 5388
66.1.13 Date Time
66.1.13.1  DateAndDateTimeChoice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4466
Or}   DateTime <DtTm> [1..1] DateTime 4466
66.1.13.1.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 5388
66.1.13.1.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 5388
66.1.13.2  DateAndDateTime1Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4467
Or}   DateTime <DtTm> [1..1] DateTime 4467
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4466 May 2026
```

