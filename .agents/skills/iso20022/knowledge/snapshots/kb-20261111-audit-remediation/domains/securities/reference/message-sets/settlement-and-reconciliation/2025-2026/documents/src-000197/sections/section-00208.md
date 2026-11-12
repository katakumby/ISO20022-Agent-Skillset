---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.2 Transaction <Tx>", "9.4.6.2.15 TransactionDetails <TxDtls>", "9.4.6.2.15.1 TransactionActivity <TxActvty>"]
file_pages: [314]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.2.15.1 TransactionActivity <TxActvty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 314 to 314.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 314

```text
Collateral (giver) Out Initiation
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (giver) Out Return
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (taker) In Initiation
SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI)
Collateral (taker) In Return
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
9.4.6.2.15.1  TransactionActivity <TxActvty>
Presence: [1..1]
Definition: Specifies the type of activity to which this instruction relates.
TransactionActivity <TxActvty> contains one of the following elements (see
"TransactionActivity3Choice" on page 2034 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2034
Or}   Proprietary <Prtry> [1..1] ± 2034
9.4.6.2.15.2  SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp>
Presence: [0..1]
Definition: Choice of type for the transaction reported.
SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp> contains one of
the following elements (see "SettlementOrCorporateActionEvent34Choice" on page 1645 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1645
Or}   CorporateActionEventType <CorpActnEvtTp> [1..1] ± C13 1645
9.4.6.2.15.3  SecuritiesMovementType <SctiesMvmntTp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 314 March 2026
```

