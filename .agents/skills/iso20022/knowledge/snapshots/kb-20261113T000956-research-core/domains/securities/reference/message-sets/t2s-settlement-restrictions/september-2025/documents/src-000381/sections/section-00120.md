---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["7 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "7.4 Message Building Blocks", "7.4.2 ReportGeneralDetails <RptGnlDtls>"]
file_pages: [150]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 7.4.2 ReportGeneralDetails <RptGnlDtls>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 150 to 150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 150

```text
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 229 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 229
   LastPageIndicator <LastPgInd> [1..1] Indicator 229
7.4.2 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: General characteristics related to the report information.
Impacted by: C21 "ReportNumberRule"
ReportGeneralDetails <RptGnlDtls> contains the following SecuritiesTransactionReport5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 150
   QueryReference <QryRef> [0..1] Text 151
   ReportIdentification <RptId> [0..1] Text 151
   ReportDateTime <RptDtTm> [0..1] ± 151
   ReportPeriod <RptPrd> [0..1] ± 151
   QueryType <QryTp> [0..1] CodeSet 151
   Frequency <Frqcy> [0..1] ± 152
   UpdateType <UpdTp> [1..1] ± 152
   ActivityIndicator <ActvtyInd> [1..1] Indicator 152
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
7.4.2.1  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the report.
Approved by the Securities SEG on 21 August 2025 semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities - Settlement Restrictions 150 September 2025
```

