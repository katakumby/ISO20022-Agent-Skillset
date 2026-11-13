---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.4 Message Building Blocks", "22.4.3 ReportGeneralDetails <RptGnlDtls>"]
file_pages: [529]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.4.3 ReportGeneralDetails <RptGnlDtls>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 529 to 529.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 529

```text
22.4.3 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: General characteristics related to the report information.
Impacted by: C13 "ReportNumberRule"
ReportGeneralDetails <RptGnlDtls> contains the following IntraBalanceReport6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 529
   QueryReference <QryRef> [0..1] Text 529
   ReportIdentification <RptId> [0..1] Text 530
   ReportDateTime <RptDtTm> [0..1] ± 530
   ReportPeriod <RptPrd> [0..1] ± 530
   Frequency <Frqcy> [0..1] ± 530
   UpdateType <UpdTp> [1..1] ± 530
   ActivityIndicator <ActvtyInd> [1..1] Indicator 531
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
22.4.3.1  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the report.
ReportNumber <RptNb> contains one of the following elements (see "Number3Choice" on page 2979
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 2980
Or}   Long <Lng> [1..1] Text 2980
22.4.3.2  QueryReference <QryRef>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 529 August 2026
```

