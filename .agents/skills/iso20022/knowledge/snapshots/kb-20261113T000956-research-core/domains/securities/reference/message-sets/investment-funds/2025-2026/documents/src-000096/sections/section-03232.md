---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.13 Date Time", "66.1.13.4 FiscalYear1Choice", "66.1.13.4.2 EndDate <EndDt>"]
file_pages: [4468]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.13.4.2 EndDate <EndDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4468 to 4468.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4468

```text
66.1.13.4.2  EndDate <EndDt>
Presence: [1..1]
Definition: End date of the fiscal year.
Datatype: "ISODate" on page 5388
66.1.13.5  DateAndDateTime2Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
66.1.13.5.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 5388
66.1.13.5.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 5388
66.1.14 Date Time Period
66.1.14.1  TimeHorizon2Choice
Definition: Choice of formats for a time horizon.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NumberOfYears <NbOfYrs> [1..1] Quantity 4468
Or}   TimeFrame <TmFrame> [1..1]  4468
{Or     Code <Cd> [1..1] CodeSet 4469
Or}     Proprietary <Prtry> [1..1] ± 4469
66.1.14.1.1  NumberOfYears <NbOfYrs>
Presence: [1..1]
Definition: Minimum recommended holding (RHP) period.
Datatype: "DecimalNumber" on page 5400
66.1.14.1.2  TimeFrame <TmFrame>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4468 May 2026
```

