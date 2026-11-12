---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks"]
file_pages: [738]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 738 to 738.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 738

```text
Sell-Buy Back: Buy Back
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
Buy-Sell Back: Buy
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Buy-Sell Back: Sell Back
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: BuySellBack (BSBK)
Collateral (giver) Out Initiation
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (giver) Out Return
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (taker) In Initiation
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI)
Collateral (taker) In Return
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
This constraint is defined at the MessageDefinition level.
22.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
22.4.1 TransactionIdentification <TxId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 738 March 2026
```

