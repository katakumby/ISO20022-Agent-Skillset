---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.2.4 Balance <Bal>", "2.4.2.2.2.2.4.4 ValueDate <ValDt>", "2.4.2.2.2.2.4.4.1 DateTime <DtTm>", "2.4.2.2.2.2.4.4.1.3 FromToDateTime <FrToDtTm>"]
file_pages: [35]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.2.4.4.1.3 FromToDateTime <FrToDtTm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 35 to 35.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 35

```text
2.4.2.2.2.2.4.4.1.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on page 801
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 802
   ToDateTime <ToDtTm> [1..1] DateTime 802
2.4.2.2.2.2.4.4.1.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 883
2.4.2.2.2.2.4.4.1.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 883
2.4.2.2.2.2.4.4.2  Date <Dt>
Presence: [1..1]
Definition: Patterns to search a date.
Date <Dt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 35
Or   ToDate <ToDt> [1..1] Date 35
Or   FromToDate <FrToDt> [1..1] ± 36
Or   EqualDate <EQDt> [1..1] Date 36
Or}   NotEqualDate <NEQDt> [1..1] Date 36
2.4.2.2.2.2.4.4.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 883
2.4.2.2.2.2.4.4.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 35 February 2025
```

