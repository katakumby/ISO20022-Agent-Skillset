---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01", "6.4 Message Building Blocks", "6.4.3 SearchCriteria <SchCrit>", "6.4.3.3 MaturityDate <MtrtyDt>"]
file_pages: [84]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6.4.3.3 MaturityDate <MtrtyDt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 84 to 84.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 84

```text
Datatype: "CFIOct2015Identifier" on page 530
6.4.3.3  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Planned final repayment date at the time of issuance.
MaturityDate <MtrtyDt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 84
Or   ToDate <ToDt> [1..1] Date 84
Or   FromToDate <FrToDt> [1..1] ± 84
Or   EqualDate <EQDt> [1..1] Date 84
Or}   NotEqualDate <NEQDt> [1..1] Date 84
6.4.3.3.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 529
6.4.3.3.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 529
6.4.3.3.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 235 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 235
   ToDate <ToDt> [1..1] Date 236
6.4.3.3.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 529
6.4.3.3.5  NotEqualDate <NEQDt>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 84 March 2024
```

