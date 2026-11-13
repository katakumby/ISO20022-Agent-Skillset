---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2 Balance <Bal>", "2.4.2.2.2.4 ValueDate <ValDt>", "2.4.2.2.2.4.1 DateTime <DtTm>"]
file_pages: [47]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.2.4.1 DateTime <DtTm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 47 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 47

```text
ValueDate <ValDt> contains one of the following DateAndDateTimeSearch4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DateTime <DtTm> [1..1]  47
{Or     FromDateTime <FrDtTm> [1..1] DateTime 47
Or     ToDateTime <ToDtTm> [1..1] DateTime 47
Or     FromToDateTime <FrToDtTm> [1..1] ± 48
Or     EqualDateTime <EQDtTm> [1..1] DateTime 48
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 48
Or}   Date <Dt> [1..1]  48
{Or     FromDate <FrDt> [1..1] Date 48
Or     ToDate <ToDt> [1..1] Date 48
Or     FromToDate <FrToDt> [1..1] ± 49
Or     EqualDate <EQDt> [1..1] Date 49
Or}     NotEqualDate <NEQDt> [1..1] Date 49
2.4.2.2.2.4.1  DateTime <DtTm>
Presence: [1..1]
Definition: Patterns to search a date time.
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 47
Or   ToDateTime <ToDtTm> [1..1] DateTime 47
Or   FromToDateTime <FrToDtTm> [1..1] ± 48
Or   EqualDateTime <EQDtTm> [1..1] DateTime 48
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 48
2.4.2.2.2.4.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 3320
2.4.2.2.2.4.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 47 August 2026
```

