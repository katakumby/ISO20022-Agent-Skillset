---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.4 Message Building Blocks"]
file_pages: [416, 417]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 416 to 417.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 416

```text
C11 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C12 StatementBasisRule
If StatementBasis is used, then the statement requested must be a
SecuritiesBalanceAccountingReport or a SecuritiesBalanceCustodyReport.
C13 StatementTypeRule
If StatementType is used, then the statement requested must be a
SecuritiesBalanceAccountingReport, a SecuritiesBalanceCustodyReport or a
SecuritiesTransactionPostingReport.
C14 StatusRule
If a specific Status is requested, then it must be in line with the statuses available for the
message type requested.
C15 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
12.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
12.4.1 StatementRequested <StmtReqd>
Presence: [1..1]
Definition: Description of the statement requested.
StatementRequested <StmtReqd> contains the following elements (see "DocumentNumber13" on
page 1443 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] ± C20 1444
12.4.2 StatementGeneralDetails <StmtGnlDtls>
Presence: [0..1]
Definition: General information related to the report.
Impacted by: C12 "StatementBasisRule", C13 "StatementTypeRule"
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 416 March 2026
```

## File page 417

```text
StatementGeneralDetails <StmtGnlDtls> contains the following elements (see "Statement83" on
page 1604 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatementDateOrPeriod <StmtDtOrPrd> [0..1] ± 1604
   Frequency <Frqcy> [0..1] ± 1605
   UpdateType <UpdTp> [0..1] ± 1605
   StatementBasis <StmtBsis> [0..1] ± 1605
   StatementType <StmtTp> [0..1] ± 1605
Constraints
• StatementBasisRule
If StatementBasis is used, then the statement requested must be a
SecuritiesBalanceAccountingReport or a SecuritiesBalanceCustodyReport.
• StatementTypeRule
If StatementType is used, then the statement requested must be a
SecuritiesBalanceAccountingReport, a SecuritiesBalanceCustodyReport or a
SecuritiesTransactionPostingReport.
12.4.3 AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
12.4.4 SafekeepingAccount <SfkpgAcct>
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
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 417 March 2026
```

