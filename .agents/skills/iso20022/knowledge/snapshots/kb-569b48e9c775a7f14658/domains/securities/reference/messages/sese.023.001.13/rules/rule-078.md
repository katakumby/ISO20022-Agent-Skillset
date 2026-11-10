---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C78 TwoLegTransactionOpeningClosing2Rule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C78"
source_locations: [{"source_id": "src-000197", "file_pages": [509, 510], "printed_pages": [509, 510], "heading": "17.3 Constraints", "constraint": "C78"}]
---

# C78 TwoLegTransactionOpeningClosing2Rule

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 509, 510. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

For settlement of two part transactions (buy-sell back, sell buy-back, collateral in and out), the
opening/initiation and closing/return of the transaction is instructed by sending the following
combination of SettlementTypeAndAdditionalParameters/SecuritiesMovementType codes and
SettlementParameters/SecuritiesTransactionType codes:
Sell-Buy Back: Sell
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SellBuyBack (SBBK)
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

[Constraint index](../rules-business.md)
