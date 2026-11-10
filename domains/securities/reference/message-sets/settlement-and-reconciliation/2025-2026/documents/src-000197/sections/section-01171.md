---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.76 Statement62"]
file_pages: [1621]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.76 Statement62

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1621 to 1621.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1621

```text
35.1.16.76  Statement62
Definition: Characteristics of the statement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CounterpartyPortfolioTransferNotificationReference
<CtrPtyPrtflTrfNtfctnRef>
[0..1] Text 1621
   ReportNumber <RptNb> [0..1] ± 1621
   StatementIdentification <StmtId> [0..1] Text 1621
   StatementDateTime <StmtDtTm> [1..1] ± 1621
   UpdateType <UpdTp> [0..1] ± 1622
   ActivityIndicator <ActvtyInd> [1..1] Indicator 1622
35.1.16.76.1  CounterpartyPortfolioTransferNotificationReference <CtrPtyPrtflTrfNtfctnRef>
Presence: [0..1]
Definition: Identification assigned by the portfolio transfer counterpart to unambiguously identify a
portfolio transfer notification.
Datatype: "Max35Text" on page 2192
35.1.16.76.2  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the report.
ReportNumber <RptNb> contains one of the following elements (see "Number3Choice" on page 1536
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 1536
Or}   Long <Lng> [1..1] Text 1536
35.1.16.76.3  StatementIdentification <StmtId>
Presence: [0..1]
Definition: Reference common to all pages of a statement.
Datatype: "Max35Text" on page 2192
35.1.16.76.4  StatementDateTime <StmtDtTm>
Presence: [1..1]
Definition: Date and time of the statement.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1621 March 2026
```

