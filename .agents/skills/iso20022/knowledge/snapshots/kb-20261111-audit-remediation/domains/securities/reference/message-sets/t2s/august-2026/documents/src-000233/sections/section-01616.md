---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["56 reda.036.001.01 SecuritiesAccountAuditTrailQueryV01", "56.4 Message Building Blocks", "56.4.2 SearchCriteria <SchCrit>", "56.4.2.2 DatePeriod <DtPrd>"]
file_pages: [2243]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.036.001.01"]
---

# 56.4.2.2 DatePeriod <DtPrd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2243 to 2243.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2243

```text
SecuritiesAccountIdentification <SctiesAcctId> contains the following elements (see
"SecuritiesAccount19" on page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
56.4.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Specifies the period for querying information.
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2243
Or   ToDate <ToDt> [1..1] Date 2243
Or   FromToDate <FrToDt> [1..1] ± 2243
Or   EqualDate <EQDt> [1..1] Date 2244
Or}   NotEqualDate <NEQDt> [1..1] Date 2244
56.4.2.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
56.4.2.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 3319
56.4.2.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.036.001.01
SecuritiesAccountAuditTrailQueryV01
Target2-Securities 2243 August 2026
```

