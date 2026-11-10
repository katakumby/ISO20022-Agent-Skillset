---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["5 reda.039.001.01 CashAccountAuditTrailQueryV01", "5.4 Message Building Blocks", "5.4.2 SearchCriteria <SchCrit>", "5.4.2.2 DatePeriod <DtPrd>", "5.4.2.2.1 FromDate <FrDt>"]
file_pages: [116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.039.001.01"]
---

# 5.4.2.2.1 FromDate <FrDt>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 116 to 116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 116

```text
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 116
Or   ToDate <ToDt> [1..1] Date 116
Or   FromToDate <FrToDt> [1..1] ± 116
Or   EqualDate <EQDt> [1..1] Date 116
Or}   NotEqualDate <NEQDt> [1..1] Date 116
5.4.2.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 179
5.4.2.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 179
5.4.2.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 137 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 138
   ToDate <ToDt> [1..1] Date 138
5.4.2.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 179
5.4.2.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 179
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.039.001.01 CashAccountAuditTrailQueryV01
Target2-Securities - Cash Account Query and Report 116 August 2026
```

