---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.69 OpeningClosing3Choice", "35.1.16.69.2 Proprietary <Prtry>"]
file_pages: [1609]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.69.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1609 to 1609.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1609

```text
35.1.16.69.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Opening closing information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.70  Statement73
Definition: Characteristics of the statement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] ± 1609
   QueryReference <QryRef> [0..1] Text 1610
   StatementIdentification <StmtId> [0..1] Text 1610
   StatementDateTime <StmtDtTm> [1..1] ± 1610
   Frequency <Frqcy> [1..1] ± 1610
   UpdateType <UpdTp> [1..1] ± 1610
   StatementBasis <StmtBsis> [1..1] ± 1611
   ActivityIndicator <ActvtyInd> [1..1] Indicator 1611
   SubAccountIndicator <SubAcctInd> [1..1] Indicator 1611
   SecurityInterestOrSetOff <SctyIntrstOrSetOff> [0..1] Indicator 1611
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002, etc.
35.1.16.70.1  ReportNumber <RptNb>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1609 March 2026
```

