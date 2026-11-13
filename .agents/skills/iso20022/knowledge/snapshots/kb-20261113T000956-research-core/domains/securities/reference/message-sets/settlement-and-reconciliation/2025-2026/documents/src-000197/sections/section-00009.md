---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.3 AccountOwner <AcctOwnr>"]
file_pages: [29]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.3 AccountOwner <AcctOwnr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 29 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 29

```text
StatementGeneralDetails <StmtGnlDtls> contains the following elements (see "Statement73" on
page 1609 for details)
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
2.4.3 AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
2.4.4 AccountServicer <AcctSvcr>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 29 March 2026
```

