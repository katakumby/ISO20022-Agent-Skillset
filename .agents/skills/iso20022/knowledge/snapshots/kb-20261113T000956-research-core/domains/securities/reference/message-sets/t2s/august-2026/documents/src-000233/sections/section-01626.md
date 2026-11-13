---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "57.4 Message Building Blocks", "57.4.2 ReportOrError <RptOrErr>", "57.4.2.1 SecuritiesAccountAuditTrailReport <SctiesAcctAudtTrlRpt>", "57.4.2.1.1 SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr>", "57.4.2.1.1.2 BusinessError <BizErr>", "57.4.2.1.1.2.1 Error <Err>", "57.4.2.1.1.2.1.1 Code <Cd>"]
file_pages: [2253]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.037.001.01"]
---

# 57.4.2.1.1.2.1.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2253 to 2253.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2253

```text
57.4.2.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 3246
57.4.2.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 3328
57.4.2.1.1.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 3326
57.4.2.1.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Period in dates for which the audit trail is provided.
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2253
Or   ToDate <ToDt> [1..1] Date 2253
Or   FromToDate <FrToDt> [1..1] ± 2253
Or   EqualDate <EQDt> [1..1] Date 2254
Or}   NotEqualDate <NEQDt> [1..1] Date 2254
57.4.2.1.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
57.4.2.1.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 3319
57.4.2.1.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities 2253 August 2026
```

