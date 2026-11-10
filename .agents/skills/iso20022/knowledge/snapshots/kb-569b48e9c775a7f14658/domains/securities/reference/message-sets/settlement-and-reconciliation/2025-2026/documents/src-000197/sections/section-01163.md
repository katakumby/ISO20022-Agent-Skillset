---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.70 Statement73", "35.1.16.70.2 QueryReference <QryRef>"]
file_pages: [1610]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.70.2 QueryReference <QryRef>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1610 to 1610.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1610

```text
Definition: Sequential number of the report.
ReportNumber <RptNb> contains one of the following elements (see "Number3Choice" on page 1536
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 1536
Or}   Long <Lng> [1..1] Text 1536
35.1.16.70.2  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the SecuritiesStatementQuery message sent to request this statement.
Datatype: "Max35Text" on page 2192
35.1.16.70.3  StatementIdentification <StmtId>
Presence: [0..1]
Definition: Reference common to all pages of a statement.
Datatype: "Max35Text" on page 2192
35.1.16.70.4  StatementDateTime <StmtDtTm>
Presence: [1..1]
Definition: Date and time of the statement.
StatementDateTime <StmtDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.16.70.5  Frequency <Frqcy>
Presence: [1..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 1480
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1480
Or}   Proprietary <Prtry> [1..1] ± 1480
35.1.16.70.6  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the statement is complete or contains changes only.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1610 March 2026
```

