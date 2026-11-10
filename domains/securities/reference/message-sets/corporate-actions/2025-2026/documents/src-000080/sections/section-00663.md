---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.6 Date Time Period", "16.1.6.3 DateOrDateTimePeriod1Choice", "16.1.6.3.1 Date <Dt>"]
file_pages: [854]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.6.3.1 Date <Dt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 854 to 854.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 854

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 854
Or}   DateTime <DtTm> [1..1] ± 854
16.1.6.3.1  Date <Dt>
Presence: [1..1]
Definition: Period expressed with dates.
Date <Dt> contains the following elements (see "DatePeriod2" on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 842
   ToDate <ToDt> [1..1] Date 842
16.1.6.3.2  DateTime <DtTm>
Presence: [1..1]
Definition: Period expressed a dates and times.
DateTime <DtTm> contains the following elements (see "DateTimePeriod1" on page 853 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 853
   ToDateTime <ToDtTm> [1..1] DateTime 853
16.1.6.4  Period6Choice
Definition: Choice between a period or a period code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 854
Or}   PeriodCode <PrdCd> [1..1] CodeSet 855
16.1.6.4.1  Period <Prd>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 854 February 2026
```

