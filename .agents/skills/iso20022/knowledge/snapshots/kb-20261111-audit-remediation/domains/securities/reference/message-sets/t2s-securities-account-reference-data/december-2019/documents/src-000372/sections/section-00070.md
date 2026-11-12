---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["10 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "10.4 Message Building Blocks", "10.4.2 ReportOrError <RptOrErr>", "10.4.2.1 SecuritiesAccountAuditTrailReport <SctiesAcctAudtTrlRpt>", "10.4.2.1.1 SecuritiesAccountAuditTrailOrError <SctiesAcctAudtTrlOrErr>", "10.4.2.1.1.2 BusinessError <BizErr>", "10.4.2.1.1.2.1 Error <Err>", "10.4.2.1.1.2.1.1 Code <Cd>"]
file_pages: [76]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.037.001.01"]
---

# 10.4.2.1.1.2.1.1 Code <Cd>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 76 to 76.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 76

```text
10.4.2.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ExternalSystemErrorHandling1Code" on page 95
10.4.2.1.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 100
10.4.2.1.1.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 99
10.4.2.1.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Period in dates for which the audit trail is provided.
DatePeriod <DtPrd> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 76
Or   ToDate <ToDt> [1..1] Date 76
Or   FromToDate <FrToDt> [1..1] ± 76
Or   EqualDate <EQDt> [1..1] Date 77
Or}   NotEqualDate <NEQDt> [1..1] Date 77
10.4.2.1.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 97
10.4.2.1.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 97
10.4.2.1.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities - Securities Account Reference Data 76 December 2019
```

