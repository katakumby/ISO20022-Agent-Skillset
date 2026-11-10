---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.65 PurposeCode7Choice", "35.1.16.65.2 Proprietary <Prtry>"]
file_pages: [1604]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.65.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1604 to 1604.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1604

```text
35.1.16.65.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities account purpose as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.66  Statement83
Definition: Characteristics of the statement.
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
35.1.16.66.1  StatementDateOrPeriod <StmtDtOrPrd>
Presence: [0..1]
Definition: Date or period of the statement.
StatementDateOrPeriod <StmtDtOrPrd> contains one of the following elements (see
"DateAndPeriod3Choice" on page 1442 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementDate <StmtDt> [1..1] ± 1442
Or}   StatementPeriod <StmtPrd> [1..1] ± 1443
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1604 March 2026
```

