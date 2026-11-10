---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks"]
file_pages: [1007, 1008]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1007 to 1008.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1007

```text
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: SecuritiesBorrowing (SECB).
C57 VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
29.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
29.4.1 TransactionIdentificationDetails <TxIdDtls>
Presence: [1..1]
Definition: Securities financing transaction identification information, type (repurchase agreement,
reverse repurchase agreement, securities lending or securities borrowing) and other parameters.
Impacted by: C56 "TwoLegTransactionOpeningClosingRule"
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1007 March 2026
```

## File page 1008

```text
TransactionIdentificationDetails <TxIdDtls> contains the following elements (see
"TransactionTypeAndAdditionalParameters22" on page 1509 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1511
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1511
   SecuritiesFinancingTransactionType <SctiesFincgTxTp> [1..1] CodeSet 1511
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 1512
   Payment <Pmt> [1..1] CodeSet 1512
   CommonIdentification <CmonId> [0..1] Text 1512
   PoolIdentification <PoolId> [0..1] Text 1512
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1512
   NonceIdentification <NonceId> [0..1] Text 1513
Constraints
• TwoLegTransactionOpeningClosingRule
For transactions settling in two legs (Securities Financing), the opening/initiation and closing/return
information of the transaction is provided by sending the below combination of
SecuritiesMovementType codes and SecuritiesFinancingTransactionType codes:
Repo Opening
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: Repo (REPU)
Repo Closing
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: Repo (REPU)
Reverse Repo Opening
SecuritiesMovementType: Receive (RECE)
SecuritiesFinancingTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
SecuritiesMovementType: Delivery (DELI)
SecuritiesFinancingTransactionType: ReverseRepo (RVPO)
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1008 March 2026
```

