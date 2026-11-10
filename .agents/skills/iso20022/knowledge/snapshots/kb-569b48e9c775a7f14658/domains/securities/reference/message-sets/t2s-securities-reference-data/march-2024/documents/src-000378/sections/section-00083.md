---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["11 reda.033.001.01 SecuritiesAuditTrailQueryV01", "11.4 Message Building Blocks", "11.4.2 SearchCriteria <SchCrit>", "11.4.2.2 DatePeriod <DtPrd>"]
file_pages: [132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.033.001.01"]
---

# 11.4.2.2 DatePeriod <DtPrd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 132 to 132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 132

```text
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
11.4.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Describes date period for querying information.
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 132
Or   ToDate <ToDt> [1..1] Date 132
Or   FromToDate <FrToDt> [1..1] ± 132
Or   EqualDate <EQDt> [1..1] Date 133
Or}   NotEqualDate <NEQDt> [1..1] Date 133
11.4.2.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 529
11.4.2.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 529
11.4.2.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.033.001.01 SecuritiesAuditTrailQueryV01
Target2-Securities - Securities Reference Data 132 March 2024
```

