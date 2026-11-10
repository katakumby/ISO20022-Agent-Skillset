---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C70 SettlementChainGuideline"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C70"
source_locations: [{"source_id": "src-000197", "file_pages": [506], "printed_pages": [506], "heading": "17.3 Constraints", "constraint": "C70"}]
---

# C70 SettlementChainGuideline

Source wording: [src-000197](<../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf>), §17.3, file/printed page(s) 506. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.

[Constraint index](<../rules-business.md>)
