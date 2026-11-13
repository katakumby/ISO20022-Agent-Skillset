---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.11 Date Time Period"]
file_pages: [827]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.11 Date Time Period

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 827 to 827.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 827

```text
6.1.11 Date Time Period
6.1.11.1  DateOrDateTimePeriod1Choice
Definition: Choice between a date or a date and time format for a period.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 827
Or}   DateTime <DtTm> [1..1] ± 827
6.1.11.1.1  Date <Dt>
Presence: [1..1]
Definition: Period expressed with dates.
Date <Dt> contains the following elements (see "DatePeriod2" on page 826 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 826
   ToDate <ToDt> [1..1] Date 826
6.1.11.1.2  DateTime <DtTm>
Presence: [1..1]
Definition: Period expressed a dates and times.
DateTime <DtTm> contains the following elements (see "DateTimePeriod1" on page 828 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 828
   ToDateTime <ToDtTm> [1..1] DateTime 828
6.1.11.2  TimePeriodDetails1
Definition: Particular time span specified between a start time and an end time. The time period cannot
exceed 24 hours.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromTime <FrTm> [1..1] Time 827
   ToTime <ToTm> [0..1] Time 828
6.1.11.2.1  FromTime <FrTm>
Presence: [1..1]
Definition: Time at which the time span starts.
Datatype: "ISOTime" on page 918
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
827 March 2026
```

