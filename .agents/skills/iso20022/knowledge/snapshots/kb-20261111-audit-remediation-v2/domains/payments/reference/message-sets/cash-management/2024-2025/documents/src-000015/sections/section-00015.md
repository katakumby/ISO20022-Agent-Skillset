---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.2.4 Balance <Bal>", "2.4.2.2.2.2.4.4 ValueDate <ValDt>", "2.4.2.2.2.2.4.4.1 DateTime <DtTm>"]
file_pages: [34]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.2.4.4.1 DateTime <DtTm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 34 to 34.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

```text
ValueDate <ValDt> contains one of the following DateAndDateTimeSearch4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   DateTime <DtTm> [1..1]  34
{Or     FromDateTime <FrDtTm> [1..1] DateTime 34
Or     ToDateTime <ToDtTm> [1..1] DateTime 34
Or     FromToDateTime <FrToDtTm> [1..1] ± 35
Or     EqualDateTime <EQDtTm> [1..1] DateTime 35
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 35
Or}   Date <Dt> [1..1]  35
{Or     FromDate <FrDt> [1..1] Date 35
Or     ToDate <ToDt> [1..1] Date 35
Or     FromToDate <FrToDt> [1..1] ± 36
Or     EqualDate <EQDt> [1..1] Date 36
Or}     NotEqualDate <NEQDt> [1..1] Date 36
2.4.2.2.2.2.4.4.1  DateTime <DtTm>
Presence: [1..1]
Definition: Patterns to search a date time.
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 34
Or   ToDateTime <ToDtTm> [1..1] DateTime 34
Or   FromToDateTime <FrToDtTm> [1..1] ± 35
Or   EqualDateTime <EQDtTm> [1..1] DateTime 35
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 35
2.4.2.2.2.2.4.4.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 883
2.4.2.2.2.2.4.4.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 883
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 34 February 2025
```

