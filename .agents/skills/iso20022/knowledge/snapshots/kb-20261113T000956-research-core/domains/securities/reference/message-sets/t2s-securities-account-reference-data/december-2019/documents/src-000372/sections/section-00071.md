---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 SecuritiesAccountAuditTrailReport <SctiesAcctAudtTrlRpt>", "10.4.2.1.2 DatePeriod <DtPrd>", "10.4.2.1.2.4 EqualDate <EQDt>"]
file_pages: [77]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.037.001.01"]
---

# 10.4.2.1.2.4 EqualDate <EQDt>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 77 to 77.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 77

```text
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 79 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 80
   ToDate <ToDt> [1..1] Date 80
10.4.2.1.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 97
10.4.2.1.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 97
10.4.2.1.3  SecuritiesAccountIdentification <SctiesAcctId>
Presence: [1..1]
Definition: Identifies the securities account for which the audit trail is provided.
SecuritiesAccountIdentification <SctiesAcctId> contains the following elements (see
"SecuritiesAccount19" on page 79 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 79
   Type <Tp> [0..1] ± 79
   Name <Nm> [0..1] Text 79
10.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Provides details about an operational error.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  77
{Or     Code <Cd> [1..1] CodeSet 78
Or}     Proprietary <Prtry> [1..1] Text 78
   Description <Desc> [0..1] Text 78
10.4.2.2.1  Error <Err>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities - Securities Account Reference Data 77 December 2019
```

