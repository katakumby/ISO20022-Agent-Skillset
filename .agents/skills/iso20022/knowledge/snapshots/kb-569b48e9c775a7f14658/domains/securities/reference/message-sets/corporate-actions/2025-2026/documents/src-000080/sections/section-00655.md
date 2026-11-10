---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.5 Date Time", "16.1.5.4 DateFormat46Choice"]
file_pages: [846]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.5.4 DateFormat46Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 846 to 846.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 846

```text
16.1.5.4  DateFormat46Choice
Definition: Choice between an ISODate or ISODateTime format or a date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 846
Or}   DateCode <DtCd> [1..1]  846
{Or     Code <Cd> [1..1] CodeSet 846
Or}     Proprietary <Prtry> [1..1] ± 846
16.1.5.4.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 848 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
16.1.5.4.2  DateCode <DtCd>
Presence: [1..1]
Definition: Specifies the type of date.
DateCode <DtCd> contains one of the following DateCode20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 846
Or}   Proprietary <Prtry> [1..1] ± 846
16.1.5.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to indicate the date is unknown.
Datatype: "DateType1Code" on page 1205
CodeName Name Definition
UKWN Unknown Date is unknown by the sender or has
not been established.
16.1.5.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the type of date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 846 February 2026
```

