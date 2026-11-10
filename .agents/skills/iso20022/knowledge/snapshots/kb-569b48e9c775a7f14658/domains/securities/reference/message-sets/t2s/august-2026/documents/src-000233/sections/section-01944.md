---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.2 ReportGeneralDetails <RptGnlDtls>", "76.4.2.1 ReportNumber <RptNb>"]
file_pages: [2659]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.2.1 ReportNumber <RptNb>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2659 to 2659.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2659

```text
ReportGeneralDetails <RptGnlDtls> contains the following SecuritiesTransactionReport5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 2659
   QueryReference <QryRef> [0..1] Text 2659
   ReportIdentification <RptId> [0..1] Text 2660
   ReportDateTime <RptDtTm> [0..1] ± 2660
   ReportPeriod <RptPrd> [0..1] ± 2660
   QueryType <QryTp> [0..1] CodeSet 2660
   Frequency <Frqcy> [0..1] ± 2660
   UpdateType <UpdTp> [1..1] ± 2661
   ActivityIndicator <ActvtyInd> [1..1] Indicator 2661
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
76.4.2.1  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the report.
ReportNumber <RptNb> contains one of the following elements (see "Number3Choice" on page 2979
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 2980
Or}   Long <Lng> [1..1] Text 2980
76.4.2.2  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the settlement and intra-position query message sent to request this report.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2659 August 2026
```

