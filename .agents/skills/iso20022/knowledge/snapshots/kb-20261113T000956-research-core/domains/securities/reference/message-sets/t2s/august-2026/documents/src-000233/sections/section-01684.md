---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["60 reda.043.001.02 PartyAuditTrailReportV02", "60.4 Message Building Blocks", "60.4.2 ReportOrError <RptOrErr>", "60.4.2.1 PartyAuditTrailReport <PtyAudtTrlRpt>", "60.4.2.1.2 DatePeriod <DtPrd>", "60.4.2.1.2.1 FromDate <FrDt>"]
file_pages: [2332]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.043.001.02"]
---

# 60.4.2.1.2.1 FromDate <FrDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2332 to 2332.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2332

```text
DatePeriod <DtPrd> contains one of the following DatePeriod3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2332
Or   ToDate <ToDt> [1..1] Date 2332
Or   FromToDate <FrToDt> [1..1] ± 2332
Or}   Date <Dt> [1..1] Date 2332
60.4.2.1.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
60.4.2.1.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 3319
60.4.2.1.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Range of time between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
60.4.2.1.2.4  Date <Dt>
Presence: [1..1]
Definition: Single date entry
Datatype: "ISODate" on page 3319
60.4.2.1.3  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Identifies the party for which the audit trail is provided.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.043.001.02 PartyAuditTrailReportV02
Target2-Securities 2332 August 2026
```

