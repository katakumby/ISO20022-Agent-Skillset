---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "57.4 Message Building Blocks", "57.4.2 ReportOrError <RptOrErr>", "57.4.2.1 SecuritiesAccountAuditTrailReport <SctiesAcctAudtTrlRpt>", "57.4.2.1.2 DatePeriod <DtPrd>", "57.4.2.1.2.4 EqualDate <EQDt>"]
file_pages: [2254]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.037.001.01"]
---

# 57.4.2.1.2.4 EqualDate <EQDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2254 to 2254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2254

```text
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
57.4.2.1.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 3319
57.4.2.1.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 3319
57.4.2.1.3  SecuritiesAccountIdentification <SctiesAcctId>
Presence: [1..1]
Definition: Identifies the securities account for which the audit trail is provided.
SecuritiesAccountIdentification <SctiesAcctId> contains the following elements (see
"SecuritiesAccount19" on page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
57.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Provides details about an operational error.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  2254
{Or     Code <Cd> [1..1] CodeSet 2255
Or}     Proprietary <Prtry> [1..1] Text 2255
   Description <Desc> [0..1] Text 2255
57.4.2.2.1  Error <Err>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities 2254 August 2026
```

