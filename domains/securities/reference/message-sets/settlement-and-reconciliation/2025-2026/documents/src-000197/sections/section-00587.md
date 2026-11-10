---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks"]
file_pages: [895]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 895 to 895.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 895

```text
C70 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
27.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
27.4.1 TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: "Max35Text" on page 2192
27.4.2 TransactionTypeAndAdditionalParameters
<TxTpAndAddtlParams>
Presence: [1..1]
Definition: Securities financing transaction identification information, type (repurchase agreement,
reverse repurchase agreement, securities lending or securities borrowing) and other parameters.
TransactionTypeAndAdditionalParameters <TxTpAndAddtlParams> contains the following
elements (see "TransactionTypeAndAdditionalParameters21" on page 1519 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesFinancingTransactionType <SctiesFincgTxTp> [1..1] CodeSet 1519
   Payment <Pmt> [1..1] CodeSet 1519
   CommonIdentification <CmonId> [0..1] Text 1520
   NonceIdentification <NonceId> [0..1] Text 1520
   ReconciliationIndicator <RcncltnInd> [0..1] Indicator 1520
27.4.3 NumberCounts <NbCounts>
Presence: [0..1]
Definition: Count of the number of transactions linked.
Impacted by: C18 "CurrentInstructionNumberRule"
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 895 March 2026
```

