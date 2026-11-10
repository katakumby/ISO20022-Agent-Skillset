---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2 Balance <Bal>", "2.4.2.2.2.4 ValueDate <ValDt>", "2.4.2.2.2.4.1 DateTime <DtTm>"]
file_pages: [17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.2.4.1 DateTime <DtTm>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 17 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
ValueDate <ValDt> contains one of the following DateAndDateTimeSearch4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DateTime <DtTm> [1..1]  17
{Or     FromDateTime <FrDtTm> [1..1] DateTime 17
Or     ToDateTime <ToDtTm> [1..1] DateTime 17
Or     FromToDateTime <FrToDtTm> [1..1] ± 18
Or     EqualDateTime <EQDtTm> [1..1] DateTime 18
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 18
Or}   Date <Dt> [1..1]  18
{Or     FromDate <FrDt> [1..1] Date 18
Or     ToDate <ToDt> [1..1] Date 18
Or     FromToDate <FrToDt> [1..1] ± 19
Or     EqualDate <EQDt> [1..1] Date 19
Or}     NotEqualDate <NEQDt> [1..1] Date 19
2.4.2.2.2.4.1  DateTime <DtTm>
Presence: [1..1]
Definition: Patterns to search a date time.
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 17
Or   ToDateTime <ToDtTm> [1..1] DateTime 17
Or   FromToDateTime <FrToDtTm> [1..1] ± 18
Or   EqualDateTime <EQDtTm> [1..1] DateTime 18
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 18
2.4.2.2.2.4.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 66
2.4.2.2.2.4.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 66
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
17 March 2024
```

