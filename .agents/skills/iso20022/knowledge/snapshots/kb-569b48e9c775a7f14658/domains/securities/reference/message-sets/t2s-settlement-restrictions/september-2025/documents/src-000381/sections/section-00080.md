---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.2 ReportGeneralDetails <RptGnlDtls>", "5.4.2.1 ReportNumber <RptNb>"]
file_pages: [104]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.2.1 ReportNumber <RptNb>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 104 to 104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 104

```text
ReportGeneralDetails <RptGnlDtls> contains the following SecuritiesTransactionReport5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 104
   QueryReference <QryRef> [0..1] Text 104
   ReportIdentification <RptId> [0..1] Text 105
   ReportDateTime <RptDtTm> [0..1] ± 105
   ReportPeriod <RptPrd> [0..1] ± 105
   QueryType <QryTp> [0..1] CodeSet 105
   Frequency <Frqcy> [0..1] ± 105
   UpdateType <UpdTp> [1..1] ± 106
   ActivityIndicator <ActvtyInd> [1..1] Indicator 106
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
5.4.2.1  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the report.
ReportNumber <RptNb> contains one of the following elements (see "Number3Choice" on page 228
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 229
Or}   Long <Lng> [1..1] Text 229
5.4.2.2  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the settlement and intra-position query message sent to request this report.
Datatype: "Max35Text" on page 345
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 104 September 2025
```

