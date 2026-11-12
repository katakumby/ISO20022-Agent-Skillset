---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.4 Message Building Blocks", "16.4.3 ReportGeneralDetails <RptGnlDtls>"]
file_pages: [365]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.4.3 ReportGeneralDetails <RptGnlDtls>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 365 to 365.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 365

```text
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 412 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 412
   LastPageIndicator <LastPgInd> [1..1] Indicator 412
16.4.3 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: General characteristics related to the report information.
Impacted by: C15 "ReportNumberRule"
ReportGeneralDetails <RptGnlDtls> contains the following IntraBalanceReport6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 365
   QueryReference <QryRef> [0..1] Text 366
   ReportIdentification <RptId> [0..1] Text 366
   ReportDateTime <RptDtTm> [0..1] ± 366
   ReportPeriod <RptPrd> [0..1] ± 366
   Frequency <Frqcy> [0..1] ± 366
   UpdateType <UpdTp> [1..1] ± 367
   ActivityIndicator <ActvtyInd> [1..1] Indicator 367
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
16.4.3.1  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the report.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
365 March 2024
```

