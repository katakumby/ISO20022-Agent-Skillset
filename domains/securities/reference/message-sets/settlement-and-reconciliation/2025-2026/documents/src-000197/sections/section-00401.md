---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks"]
file_pages: [613]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 613 to 613.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 613

```text
Collateral (giver) Out Return
TransactionIdentificationDetails/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralOut (COLO)
Collateral (taker) In Initiation
TransactionIdentificationDetails/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI)
Collateral (taker) In Return
TransactionIdentificationDetails/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
This constraint is defined at the MessageDefinition level.
C64 VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
19.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
19.4.1 TransactionIdentificationDetails <TxIdDtls>
Presence: [1..1]
Definition: Provides transaction type and identification information.
Impacted by: C29 "NoAccountOwnerTransactionIdentificationRule"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 613 March 2026
```

