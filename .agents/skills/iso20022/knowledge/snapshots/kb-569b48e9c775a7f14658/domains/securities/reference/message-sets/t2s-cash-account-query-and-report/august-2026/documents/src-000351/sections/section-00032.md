---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.22 ClosingDate <ClsgDt>", "2.4.5.22.1 FromDate <FrDt>"]
file_pages: [36]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.22.1 FromDate <FrDt>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 36 to 36.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 36

```text
ClosingDate <ClsgDt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 36
Or   ToDate <ToDt> [1..1] Date 36
Or   FromToDate <FrToDt> [1..1] ± 36
Or   EqualDate <EQDt> [1..1] Date 36
Or}   NotEqualDate <NEQDt> [1..1] Date 36
2.4.5.22.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 179
2.4.5.22.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 179
2.4.5.22.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 137 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 138
   ToDate <ToDt> [1..1] Date 138
2.4.5.22.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 179
2.4.5.22.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 179
2.4.5.23  OpeningDate <OpngDt>
Presence: [0..1]
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 36 August 2026
```

