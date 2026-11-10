---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.13 Date Time", "66.1.13.2 DateAndDateTime1Choice", "66.1.13.2.1 Date <Dt>"]
file_pages: [4467]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.13.2.1 Date <Dt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4467 to 4467.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4467

```text
66.1.13.2.1  Date <Dt>
Presence: [1..1]
Definition: Numeric representation of the day of the month and year.
Datatype: "ISODate" on page 5388
66.1.13.2.2  DateTime <DtTm>
Presence: [1..1]
Definition: Numeric representation of time of the day and the day of the month and year.
Datatype: "ISODateTime" on page 5388
66.1.13.3  DateFormat42Choice
Definition: Choice of formats for a date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   YearMonth <YrMnth> [1..1] YearMonth 4467
Or}   YearMonthDay <YrMnthDay> [1..1] Date 4467
66.1.13.3.1  YearMonth <YrMnth>
Presence: [1..1]
Definition: Year and month.
Datatype: "ISOYearMonth" on page 5406
66.1.13.3.2  YearMonthDay <YrMnthDay>
Presence: [1..1]
Definition: Year, month and day.
Datatype: "ISODate" on page 5388
66.1.13.4  FiscalYear1Choice
Definition: Choice of start date and end date for the fiscal year.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StartDate <StartDt> [1..1] Date 4467
Or}   EndDate <EndDt> [1..1] Date 4468
66.1.13.4.1  StartDate <StartDt>
Presence: [1..1]
Definition: Start date of the fiscal year.
Datatype: "ISODate" on page 5388
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4467 May 2026
```

