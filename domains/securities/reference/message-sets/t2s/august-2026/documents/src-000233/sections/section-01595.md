---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["53 reda.033.001.01 SecuritiesAuditTrailQueryV01", "53.4 Message Building Blocks", "53.4.2 SearchCriteria <SchCrit>", "53.4.2.2 DatePeriod <DtPrd>"]
file_pages: [2222]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.033.001.01"]
---

# 53.4.2.2 DatePeriod <DtPrd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2222 to 2222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2222

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
53.4.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Describes date period for querying information.
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2222
Or   ToDate <ToDt> [1..1] Date 2222
Or   FromToDate <FrToDt> [1..1] ± 2222
Or   EqualDate <EQDt> [1..1] Date 2223
Or}   NotEqualDate <NEQDt> [1..1] Date 2223
53.4.2.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
53.4.2.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 3319
53.4.2.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.033.001.01 SecuritiesAuditTrailQueryV01
Target2-Securities 2222 August 2026
```

