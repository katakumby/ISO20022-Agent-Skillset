---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C77 TwoLegTransactionOpeningClosing1Rule"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C77"
source_locations: [{"source_id": "src-000197", "file_pages": [507, 508, 509], "printed_pages": [507, 508, 509], "heading": "17.3 Constraints", "constraint": "C77"}]
---

# C77 TwoLegTransactionOpeningClosing1Rule

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 507, 508, 509. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

For settlement of two part transactions (Securities Financing), the opening/initiation and closing/
return of the transaction is confirmed by sending the following combination of
TransactionIdentificationDetails/SecuritiesMovementType codes and SettlementParameters/
SecuritiesTransactionType codes:
Repo Opening
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Repo Closing
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: Repo (REPU)
Reverse Repo Opening
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
Reverse Repo Closing
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: ReverseRepo (RVPO)
TriParty Repo Opening
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Repo Closing
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyRepo (TRPO)
TriParty Reverse Repo Opening
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
TriParty Reverse Repo Closing
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: TriPartyReverseRepo (TRVO)
Securities Lending Initiation
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Lending Return
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesLending (SECL)
Securities Borrowing Initiation
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Receive (RECE)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB)
Securities Borrowing Return
SettlementTypeAndAdditionalParameters/SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: SecuritiesBorrowing (SECB).
This constraint is defined at the MessageDefinition level.

[Constraint index](../rules-business.md)
