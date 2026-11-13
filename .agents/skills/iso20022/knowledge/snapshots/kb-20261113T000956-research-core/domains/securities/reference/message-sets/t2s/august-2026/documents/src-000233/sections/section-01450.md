---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.4 Message Building Blocks", "35.4.2 SearchCriteria <SchCrit>", "35.4.2.7 RestrictionIssueDate <RstrctnIsseDt>", "35.4.2.7.1 DateTime <DtTm>"]
file_pages: [2064]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.4.2.7.1 DateTime <DtTm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2064 to 2064.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2064

```text
RestrictionIssueDate <RstrctnIsseDt> contains one of the following
DateAndDateTimeSearch4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DateTime <DtTm> [1..1]  2064
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2064
Or     ToDateTime <ToDtTm> [1..1] DateTime 2064
Or     FromToDateTime <FrToDtTm> [1..1] ± 2065
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2065
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2065
Or}   Date <Dt> [1..1]  2065
{Or     FromDate <FrDt> [1..1] Date 2065
Or     ToDate <ToDt> [1..1] Date 2065
Or     FromToDate <FrToDt> [1..1] ± 2066
Or     EqualDate <EQDt> [1..1] Date 2066
Or}     NotEqualDate <NEQDt> [1..1] Date 2066
35.4.2.7.1  DateTime <DtTm>
Presence: [1..1]
Definition: Patterns to search a date time.
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 2064
Or   ToDateTime <ToDtTm> [1..1] DateTime 2064
Or   FromToDateTime <FrToDtTm> [1..1] ± 2065
Or   EqualDateTime <EQDtTm> [1..1] DateTime 2065
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 2065
35.4.2.7.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 3320
35.4.2.7.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2064 August 2026
```

