---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.4 Message Building Blocks", "30.4.1 TransactionTypeAndModificationAdditionalParameters <TxTpAndModAddtlParams>"]
file_pages: [1067]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.4.1 TransactionTypeAndModificationAdditionalParameters <TxTpAndModAddtlParams>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1067 to 1067.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1067

```text
30.4.1 TransactionTypeAndModificationAdditionalParamete
rs <TxTpAndModAddtlParams>
Presence: [1..1]
Definition: Securities financing transaction identification information, type (repurchase agreement,
reverse repurchase agreement, securities lending or securities borrowing), modification information and
other parameters.
TransactionTypeAndModificationAdditionalParameters <TxTpAndModAddtlParams> contains the
following elements (see "TransactionTypeAndAdditionalParameters23" on page 1481 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [1..1] Text 1481
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1481
   SecuritiesFinancingTransactionType <SctiesFincgTxTp> [1..1] CodeSet 1481
   Payment <Pmt> [1..1] CodeSet 1482
   ModificationType <ModTp> [0..1] ± 1482
   CommonIdentification <CmonId> [0..1] Text 1482
   PoolIdentification <PoolId> [0..1] Text 1482
   NonceIdentification <NonceId> [0..1] Text 1483
30.4.2 TradeDetails <TradDtls>
Presence: [1..1]
Definition: Details of the securities financing deal.
Impacted by: C3 "AdditionalDetailsRule", C36 "TradeDateTimeUTCRule"
TradeDetails <TradDtls> contains the following elements (see "SecuritiesTradeDetails100" on
page 1562 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeDate <TradDt> [0..1] ± 1563
   OpeningSettlementDate <OpngSttlmDt> [1..1] ± 1563
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C20 1563
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 1563
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1067 March 2026
```

