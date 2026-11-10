---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.8 Date Period", "82.1.8.1 DatePeriod1Choice", "82.1.8.1.1 Date <Dt>"]
file_pages: [2908]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.8.1.1 Date <Dt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2908 to 2908.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2908

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2908
Or   DateMonth <DtMnth> [1..1] YearMonth 2908
Or}   FromDateToDate <FrDtToDt> [1..1] ± 2908
82.1.8.1.1  Date <Dt>
Presence: [1..1]
Definition: Time span defined by a specific date.
Datatype: "ISODate" on page 3319
82.1.8.1.2  DateMonth <DtMnth>
Presence: [1..1]
Definition: Time span defined by a month and a year.
Datatype: "ISOYearMonth" on page 3330
82.1.8.1.3  FromDateToDate <FrDtToDt>
Presence: [1..1]
Definition: Time span defined by a start date and an end date.
FromDateToDate <FrDtToDt> contains the following elements (see "Period2" on page 2915 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2915
   ToDate <ToDt> [1..1] Date 2915
82.1.8.2  DatePeriod2
Definition: Range of time defined by a start date and an end date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
82.1.8.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
82.1.8.2.2  ToDate <ToDt>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2908 August 2026
```

