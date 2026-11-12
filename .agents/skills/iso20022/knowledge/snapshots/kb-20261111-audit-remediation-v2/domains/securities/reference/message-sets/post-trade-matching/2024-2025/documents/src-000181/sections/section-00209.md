---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.11 Date Time", "7.1.11.2 DateAndDateTime1Choice"]
file_pages: [263]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.11.2 DateAndDateTime1Choice

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 263 to 263.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 263

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.11.2  DateAndDateTime1Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 263
Or}   DateTime <DtTm> [1..1] DateTime 263
7.1.11.2.1  Date <Dt>
Presence: [1..1]
Definition: Numeric representation of the day of the month and year.
Datatype: "ISODate" on page 662
7.1.11.2.2  DateTime <DtTm>
Presence: [1..1]
Definition: Numeric representation of time of the day and the day of the month and year.
Datatype: "ISODateTime" on page 662
7.1.11.3  ClosingDate4Choice
Definition: Choice between a date or a code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 263
Or}   Code <Cd> [1..1]  264
{Or     Code <Cd> [1..1] CodeSet 264
Or}     Proprietary <Prtry> [1..1] ± 264
7.1.11.3.1  Date <Dt>
Presence: [1..1]
Definition: Closing date is defined as a choice between a date or a date and time format.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 263 February 2025
```

