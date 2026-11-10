---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.7 DateSearch <DtSch>", "2.4.2.2.7.4 EqualDate <EQDt>"]
file_pages: [54]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.7.4 EqualDate <EQDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 54 to 54.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 54

```text
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
2.4.2.2.7.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 3319
2.4.2.2.7.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 3319
2.4.2.2.8  ScheduledTime <SchdldTm>
Presence: [0..1]
Definition: Time when the (business) event, which triggered the report, was scheduled.
ScheduledTime <SchdldTm> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 54
Or   ToDateTime <ToDtTm> [1..1] DateTime 54
Or}   DateTimeRange <DtTmRg> [1..1] ± 54
2.4.2.2.8.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 3320
2.4.2.2.8.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 3320
2.4.2.2.8.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 54 August 2026
```

