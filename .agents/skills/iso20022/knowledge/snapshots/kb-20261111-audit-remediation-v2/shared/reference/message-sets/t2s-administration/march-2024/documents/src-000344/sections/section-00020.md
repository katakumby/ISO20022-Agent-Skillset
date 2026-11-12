---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.7 DateSearch <DtSch>", "2.4.2.2.7.4 EqualDate <EQDt>"]
file_pages: [24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.7.4 EqualDate <EQDt>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 24 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 40 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 40
   ToDate <ToDt> [1..1] Date 40
2.4.2.2.7.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 66
2.4.2.2.7.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 66
2.4.2.2.8  ScheduledTime <SchdldTm>
Presence: [0..1]
Definition: Time when the (business) event, which triggered the report, was scheduled.
ScheduledTime <SchdldTm> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 24
Or   ToDateTime <ToDtTm> [1..1] DateTime 24
Or}   DateTimeRange <DtTmRg> [1..1] ± 24
2.4.2.2.8.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 66
2.4.2.2.8.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 66
2.4.2.2.8.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
24 March 2024
```

