---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["5 reda.039.001.01 CashAccountAuditTrailQueryV01", "5.4 Message Building Blocks", "5.4.2 SearchCriteria <SchCrit>", "5.4.2.1 CashAccountIdentification <CshAcctId>"]
file_pages: [115]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.039.001.01"]
---

# 5.4.2.1 CashAccountIdentification <CshAcctId>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 115 to 115.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 115

```text
SearchCriteria <SchCrit> contains the following CashAccountAuditTrailSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountIdentification <CshAcctId> [0..1] ± C4, C3 115
   DatePeriod <DtPrd> [0..1]  115
{Or     FromDate <FrDt> [1..1] Date 116
Or     ToDate <ToDt> [1..1] Date 116
Or     FromToDate <FrToDt> [1..1] ± 116
Or     EqualDate <EQDt> [1..1] Date 116
Or}     NotEqualDate <NEQDt> [1..1] Date 116
5.4.2.1  CashAccountIdentification <CshAcctId>
Presence: [0..1]
Definition: Describes cash account to be queried.
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
5.4.2.2  DatePeriod <DtPrd>
Presence: [0..1]
Definition: Describes date period for querying information.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
reda.039.001.01 CashAccountAuditTrailQueryV01
Target2-Securities - Cash Account Query and Report 115 August 2026
```

