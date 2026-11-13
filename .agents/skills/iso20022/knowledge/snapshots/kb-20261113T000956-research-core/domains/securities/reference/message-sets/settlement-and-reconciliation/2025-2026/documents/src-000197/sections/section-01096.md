---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.6 Statement63", "35.1.16.6.1 ReportNumber <RptNb>"]
file_pages: [1537]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.6.1 ReportNumber <RptNb>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1537 to 1537.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1537

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 1537
   QueryReference <QryRef> [0..1] Text 1537
   StatementIdentification <StmtId> [0..1] Text 1537
   StatementDateTime <StmtDtTm> [1..1] ± 1538
   Frequency <Frqcy> [0..1] ± 1538
   UpdateType <UpdTp> [0..1] ± 1538
   ActivityIndicator <ActvtyInd> [1..1] Indicator 1538
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002.
35.1.16.6.1  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the report.
ReportNumber <RptNb> contains one of the following elements (see "Number3Choice" on page 1536
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 1536
Or}   Long <Lng> [1..1] Text 1536
35.1.16.6.2  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the SecuritiesStatementQuery message sent to request this statement.
Datatype: "Max35Text" on page 2192
35.1.16.6.3  StatementIdentification <StmtId>
Presence: [0..1]
Definition: Reference common to all pages of a statement.
Datatype: "Max35Text" on page 2192
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1537 March 2026
```

