---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["3 reda.019.001.01 SecuritiesAccountQueryV01", "3.4 Message Building Blocks", "3.4.2 SearchCriteria <SchCrit>", "3.4.2.6 ClosingDate <ClsgDt>", "3.4.2.6.1 FromDate <FrDt>"]
file_pages: [21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 3.4.2.6.1 FromDate <FrDt>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 21 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
Definition: Legal closing date for the securities account.
ClosingDate <ClsgDt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 21
Or   ToDate <ToDt> [1..1] Date 21
Or   FromToDate <FrToDt> [1..1] ± 21
Or   EqualDate <EQDt> [1..1] Date 21
Or}   NotEqualDate <NEQDt> [1..1] Date 21
3.4.2.6.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 97
3.4.2.6.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 97
3.4.2.6.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 79 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 80
   ToDate <ToDt> [1..1] Date 80
3.4.2.6.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 97
3.4.2.6.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 97
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities - Securities Account Reference Data 21 December 2019
```

