---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Date Period", "7.1.8.1 DatePeriod1Choice", "7.1.8.1.1 Date <Dt>"]
file_pages: [316]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.1.1 Date <Dt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 316 to 316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 316
Or   DateMonth <DtMnth> [1..1] YearMonth 316
Or}   FromDateToDate <FrDtToDt> [1..1] ± 316
7.1.8.1.1  Date <Dt>
Presence: [1..1]
Definition: Time span defined by a specific date.
Datatype: "ISODate" on page 550
7.1.8.1.2  DateMonth <DtMnth>
Presence: [1..1]
Definition: Time span defined by a month and a year.
Datatype: "ISOYearMonth" on page 558
7.1.8.1.3  FromDateToDate <FrDtToDt>
Presence: [1..1]
Definition: Time span defined by a start date and an end date.
FromDateToDate <FrDtToDt> contains the following elements (see "Period2" on page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 322
   ToDate <ToDt> [1..1] Date 322
7.1.8.2  DatePeriod2
Definition: Range of time defined by a start date and an end date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 316
   ToDate <ToDt> [1..1] Date 316
7.1.8.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 550
7.1.8.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 316 March 2026
```

