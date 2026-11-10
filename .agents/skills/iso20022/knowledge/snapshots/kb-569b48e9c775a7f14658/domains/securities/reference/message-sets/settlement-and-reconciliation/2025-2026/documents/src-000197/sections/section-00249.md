---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks"]
file_pages: [373, 374]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 373 to 374.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 373

```text
Collateral (taker) In Return
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
10.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
10.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 1538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 1539
   LastPageIndicator <LastPgInd> [1..1] Indicator 1539
10.4.2 StatementGeneralDetails <StmtGnlDtls>
Presence: [1..1]
Definition: General information related to the report.
Impacted by: C34 "ReportNumberRule"
StatementGeneralDetails <StmtGnlDtls> contains the following elements (see "Statement63" on
page 1536 for details)
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
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 373 March 2026
```

## File page 374

```text
Constraints
• ReportNumberRule
If Long number (Exact5NumericTest) is used, then the report must be a delta reports (UpdateType:
DELT).
If the report has multiple pages, then the ReportNumber must remain the same through all the
pages. It is a unique number to the report.
Two reports of the same type sent one after the other to the same receiver in relation to the same
safekeeping account must have different ReportNumbers. For example, a daily report sent on day 1
would have ReportNumber 001, on day 2, 002.
10.4.3 AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
10.4.4 SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 1340 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1341
   Type <Tp> [0..1] ± 1341
   Name <Nm> [0..1] Text 1341
10.4.5 BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 374 March 2026
```

