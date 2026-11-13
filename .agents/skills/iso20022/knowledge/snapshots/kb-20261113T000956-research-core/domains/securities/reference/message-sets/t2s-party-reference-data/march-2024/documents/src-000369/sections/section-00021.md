---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 reda.015.001.01 PartyQueryV01", "3.4 Message Building Blocks", "3.4.2 SearchCriteria <SchCrit>", "3.4.2.7 RestrictionIssueDate <RstrctnIsseDt>", "3.4.2.7.1 DateTime <DtTm>"]
file_pages: [27]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 3.4.2.7.1 DateTime <DtTm>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 27 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 27

```text
RestrictionIssueDate <RstrctnIsseDt> contains one of the following
DateAndDateTimeSearch4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DateTime <DtTm> [1..1]  27
{Or     FromDateTime <FrDtTm> [1..1] DateTime 27
Or     ToDateTime <ToDtTm> [1..1] DateTime 27
Or     FromToDateTime <FrToDtTm> [1..1] ± 28
Or     EqualDateTime <EQDtTm> [1..1] DateTime 28
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 28
Or}   Date <Dt> [1..1]  28
{Or     FromDate <FrDt> [1..1] Date 28
Or     ToDate <ToDt> [1..1] Date 28
Or     FromToDate <FrToDt> [1..1] ± 29
Or     EqualDate <EQDt> [1..1] Date 29
Or}     NotEqualDate <NEQDt> [1..1] Date 29
3.4.2.7.1  DateTime <DtTm>
Presence: [1..1]
Definition: Patterns to search a date time.
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 27
Or   ToDateTime <ToDtTm> [1..1] DateTime 27
Or   FromToDateTime <FrToDtTm> [1..1] ± 28
Or   EqualDateTime <EQDtTm> [1..1] DateTime 28
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 28
3.4.2.7.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 185
3.4.2.7.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 185
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.015.001.01 PartyQueryV01
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
27 March 2024
```

