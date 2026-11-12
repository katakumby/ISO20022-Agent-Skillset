---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.4 Message Building Blocks", "35.4.2 SearchCriteria <SchCrit>", "35.4.2.7 RestrictionIssueDate <RstrctnIsseDt>", "35.4.2.7.1 DateTime <DtTm>", "35.4.2.7.1.3 FromToDateTime <FrToDtTm>"]
file_pages: [2065]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.4.2.7.1.3 FromToDateTime <FrToDtTm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2065 to 2065.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2065

```text
35.4.2.7.1.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on
page 2916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2916
   ToDateTime <ToDtTm> [1..1] DateTime 2916
35.4.2.7.1.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 3320
35.4.2.7.1.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 3320
35.4.2.7.2  Date <Dt>
Presence: [1..1]
Definition: Patterns to search a date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2065
Or   ToDate <ToDt> [1..1] Date 2065
Or   FromToDate <FrToDt> [1..1] ± 2066
Or   EqualDate <EQDt> [1..1] Date 2066
Or}   NotEqualDate <NEQDt> [1..1] Date 2066
35.4.2.7.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
35.4.2.7.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2065 August 2026
```

