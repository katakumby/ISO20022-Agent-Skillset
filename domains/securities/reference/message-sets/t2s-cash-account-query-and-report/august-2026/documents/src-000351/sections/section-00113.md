---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["6 reda.040.001.01 CashAccountAuditTrailReportV01", "6.4 Message Building Blocks", "6.4.2 ReportOrError <RptOrErr>", "6.4.2.1 CashAccountAuditTrailReport <CshAcctAudtTrlRpt>", "6.4.2.1.2 DatePeriod <DtPrd>", "6.4.2.1.2.4 EqualDate <EQDt>"]
file_pages: [127]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.040.001.01"]
---

# 6.4.2.1.2.4 EqualDate <EQDt>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 127 to 127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 127

```text
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 137 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 138
   ToDate <ToDt> [1..1] Date 138
6.4.2.1.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 179
6.4.2.1.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 179
6.4.2.1.3  CashAccountIdentification <CshAcctId>
Presence: [1..1]
Definition: Identifies the cash account for which the audit trail is provided.
Impacted by: C4 "IdentificationOrProxyPresenceRule", C3 "IdentificationAndProxyGuideline"
CashAccountIdentification <CshAcctId> contains the following elements (see "CashAccount40" on
page 130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 130
   Type <Tp> [0..1] ± 130
   Currency <Ccy> [0..1] CodeSet C2 131
   Name <Nm> [0..1] Text 131
   Proxy <Prxy> [0..1] ± 131
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.040.001.01 CashAccountAuditTrailReportV01
Target2-Securities - Cash Account Query and Report 127 August 2026
```

