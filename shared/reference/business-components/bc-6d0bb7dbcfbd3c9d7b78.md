---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-6d0bb7dbcfbd3c9d7b78"
title: "SecuritiesTradeStatusReason"
business_component_name: "SecuritiesTradeStatusReason"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A4627:F4638"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A4557:F4568"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A4627:F4638"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A4627:F4638"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A4627:F4638"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A4627:F4638"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A4627:F4638"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A4557:F4568"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A4627:F4638"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A4596:F4607"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A2154:F2165"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A4596:F4607"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A4627:F4638"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A4531:F4542"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A2154:F2165"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A2154:F2165"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A4531:F4542"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A4531:F4542"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A2154:F2165"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A2154:F2165"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A4627:F4638"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A2154:F2165"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A4596:F4607"]}]
content_sha256: "6d0bb7dbcfbd3c9d7b788354905fc4f354a317bc8fb071c773624190d5857643"
parent_names: ["StatusReason"]
related_component_names: ["AllegementReasonCode", "CounterpartyResponseStatusReasonCode", "DeliveryReturnCode", "DeniedReasonCode", "GeneratedReasonCode", "ModifiedStatusReasonCode", "PendingSettlementStatusReasonCode", "RepairReasonV2Code", "RepoCallAcknowledgementReasonCode", "SecuritiesTradeStatus", "UnmatchedReasonCode"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# SecuritiesTradeStatusReason

## Definition

Specifies the underlying reason for a status of a securities trade.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SecuritiesTradeStatusReason | ∅ | StatusReason | Specifies the underlying reason for a status of a securities trade. | ∅ | ∅ |
| 2 | SecuritiesTradeStatusReason | UnmatchedReason | ∅ | Reason for the unmatched status. | UnmatchedReasonCode | ∅ |
| 3 | SecuritiesTradeStatusReason | DeniedReason | ∅ | Specifies the reason why the request was denied. | DeniedReasonCode | ∅ |
| 4 | SecuritiesTradeStatusReason | SecuritiesTradeStatus | ∅ | Status for which a reason is provided. It is derived from the association between StatusReason and Status. | SecuritiesTradeStatus | Reason |
| 5 | SecuritiesTradeStatusReason | GeneratedReason | ∅ | Specifies the reason why the transaction was generated. | GeneratedReasonCode | ∅ |
| 6 | SecuritiesTradeStatusReason | AllegementReason | ∅ | Reason why the instruction has an allegement status. | AllegementReasonCode | ∅ |
| 7 | SecuritiesTradeStatusReason | PendingSettlementReason | ∅ | Reason for the settlement pending status. | PendingSettlementStatusReasonCode | ∅ |
| 8 | SecuritiesTradeStatusReason | RepoCallAcknowledgementReason | ∅ | Specifies additional information about the processed instruction. | RepoCallAcknowledgementReasonCode | ∅ |
| 9 | SecuritiesTradeStatusReason | RepairReason | ∅ | Specifies the reason why the instruction/request has a repair status. | RepairReasonV2Code | ∅ |
| 10 | SecuritiesTradeStatusReason | DeliveryReturnReason | ∅ | Reason why the trade was returned. | DeliveryReturnCode | ∅ |
| 11 | SecuritiesTradeStatusReason | CounterpartyStatusReason | ∅ | Specifies the counterparty action which is the reason of the trade status. | CounterpartyResponseStatusReasonCode | ∅ |
| 12 | SecuritiesTradeStatusReason | ModifiedStatusReason | ∅ | Specifies the reason why the related instruction is modified. | ModifiedStatusReasonCode | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `6d0bb7dbcfbd3c9d7b788354905fc4f354a317bc8fb071c773624190d5857643`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A4627:F4638 | 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A4557:F4568 | 4557, 4558, 4559, 4560, 4561, 4562, 4563, 4564, 4565, 4566, 4567, 4568 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A4627:F4638 | 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A4627:F4638 | 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A4627:F4638 | 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A4627:F4638 | 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A4627:F4638 | 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A4557:F4568 | 4557, 4558, 4559, 4560, 4561, 4562, 4563, 4564, 4565, 4566, 4567, 4568 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A4627:F4638 | 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A4596:F4607 | 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000345 | FullBusinessModel!A2154:F2165 | 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000348 | FullBusinessModel!A4596:F4607 | 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A4627:F4638 | 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A4531:F4542 | 4531, 4532, 4533, 4534, 4535, 4536, 4537, 4538, 4539, 4540, 4541, 4542 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A2154:F2165 | 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A2154:F2165 | 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A4531:F4542 | 4531, 4532, 4533, 4534, 4535, 4536, 4537, 4538, 4539, 4540, 4541, 4542 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A4531:F4542 | 4531, 4532, 4533, 4534, 4535, 4536, 4537, 4538, 4539, 4540, 4541, 4542 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A2154:F2165 | 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A2154:F2165 | 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000376 | FullBusinessModel!A4627:F4638 | 4627, 4628, 4629, 4630, 4631, 4632, 4633, 4634, 4635, 4636, 4637, 4638 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000379 | FullBusinessModel!A2154:F2165 | 2154, 2155, 2156, 2157, 2158, 2159, 2160, 2161, 2162, 2163, 2164, 2165 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |
| src-000382 | FullBusinessModel!A4596:F4607 | 4596, 4597, 4598, 4599, 4600, 4601, 4602, 4603, 4604, 4605, 4606, 4607 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C4627 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000006 | field-type | E4628 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000006 | field-type | E4629 | DeniedReasonCode | Not a component record in this worksheet |
| src-000006 | field-type | E4630 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000006 | field-type | E4631 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000006 | field-type | E4632 | AllegementReasonCode | Not a component record in this worksheet |
| src-000006 | field-type | E4633 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000006 | field-type | E4634 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000006 | field-type | E4635 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000006 | field-type | E4636 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000006 | field-type | E4637 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000006 | field-type | E4638 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000016 | parent | C4557 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000016 | field-type | E4558 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000016 | field-type | E4559 | DeniedReasonCode | Not a component record in this worksheet |
| src-000016 | field-type | E4560 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000016 | field-type | E4561 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000016 | field-type | E4562 | AllegementReasonCode | Not a component record in this worksheet |
| src-000016 | field-type | E4563 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000016 | field-type | E4564 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000016 | field-type | E4565 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000016 | field-type | E4566 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000016 | field-type | E4567 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000016 | field-type | E4568 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000054 | parent | C4627 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000054 | field-type | E4628 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000054 | field-type | E4629 | DeniedReasonCode | Not a component record in this worksheet |
| src-000054 | field-type | E4630 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000054 | field-type | E4631 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000054 | field-type | E4632 | AllegementReasonCode | Not a component record in this worksheet |
| src-000054 | field-type | E4633 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000054 | field-type | E4634 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000054 | field-type | E4635 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000054 | field-type | E4636 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000054 | field-type | E4637 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000054 | field-type | E4638 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000081 | parent | C4627 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000081 | field-type | E4628 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000081 | field-type | E4629 | DeniedReasonCode | Not a component record in this worksheet |
| src-000081 | field-type | E4630 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000081 | field-type | E4631 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000081 | field-type | E4632 | AllegementReasonCode | Not a component record in this worksheet |
| src-000081 | field-type | E4633 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000081 | field-type | E4634 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000081 | field-type | E4635 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000081 | field-type | E4636 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000081 | field-type | E4637 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000081 | field-type | E4638 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000097 | parent | C4627 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000097 | field-type | E4628 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000097 | field-type | E4629 | DeniedReasonCode | Not a component record in this worksheet |
| src-000097 | field-type | E4630 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000097 | field-type | E4631 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000097 | field-type | E4632 | AllegementReasonCode | Not a component record in this worksheet |
| src-000097 | field-type | E4633 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000097 | field-type | E4634 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000097 | field-type | E4635 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000097 | field-type | E4636 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000097 | field-type | E4637 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000097 | field-type | E4638 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000164 | parent | C4627 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000164 | field-type | E4628 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000164 | field-type | E4629 | DeniedReasonCode | Not a component record in this worksheet |
| src-000164 | field-type | E4630 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000164 | field-type | E4631 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000164 | field-type | E4632 | AllegementReasonCode | Not a component record in this worksheet |
| src-000164 | field-type | E4633 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000164 | field-type | E4634 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000164 | field-type | E4635 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000164 | field-type | E4636 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000164 | field-type | E4637 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000164 | field-type | E4638 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000175 | parent | C4627 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000175 | field-type | E4628 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000175 | field-type | E4629 | DeniedReasonCode | Not a component record in this worksheet |
| src-000175 | field-type | E4630 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000175 | field-type | E4631 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000175 | field-type | E4632 | AllegementReasonCode | Not a component record in this worksheet |
| src-000175 | field-type | E4633 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000175 | field-type | E4634 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000175 | field-type | E4635 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000175 | field-type | E4636 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000175 | field-type | E4637 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000175 | field-type | E4638 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000182 | parent | C4557 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000182 | field-type | E4558 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000182 | field-type | E4559 | DeniedReasonCode | Not a component record in this worksheet |
| src-000182 | field-type | E4560 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000182 | field-type | E4561 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000182 | field-type | E4562 | AllegementReasonCode | Not a component record in this worksheet |
| src-000182 | field-type | E4563 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000182 | field-type | E4564 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000182 | field-type | E4565 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000182 | field-type | E4566 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000182 | field-type | E4567 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000182 | field-type | E4568 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000198 | parent | C4627 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000198 | field-type | E4628 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000198 | field-type | E4629 | DeniedReasonCode | Not a component record in this worksheet |
| src-000198 | field-type | E4630 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000198 | field-type | E4631 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000198 | field-type | E4632 | AllegementReasonCode | Not a component record in this worksheet |
| src-000198 | field-type | E4633 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000198 | field-type | E4634 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000198 | field-type | E4635 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000198 | field-type | E4636 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000198 | field-type | E4637 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000198 | field-type | E4638 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000322 | parent | C4596 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000322 | field-type | E4597 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000322 | field-type | E4598 | DeniedReasonCode | Not a component record in this worksheet |
| src-000322 | field-type | E4599 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000322 | field-type | E4600 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000322 | field-type | E4601 | AllegementReasonCode | Not a component record in this worksheet |
| src-000322 | field-type | E4602 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000322 | field-type | E4603 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000322 | field-type | E4604 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000322 | field-type | E4605 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000322 | field-type | E4606 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000322 | field-type | E4607 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000345 | parent | C2154 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000345 | field-type | E2155 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000345 | field-type | E2156 | DeniedReasonCode | Not a component record in this worksheet |
| src-000345 | field-type | E2157 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000345 | field-type | E2158 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000345 | field-type | E2159 | AllegementReasonCode | Not a component record in this worksheet |
| src-000345 | field-type | E2160 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000345 | field-type | E2161 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000345 | field-type | E2162 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000345 | field-type | E2163 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000345 | field-type | E2164 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000345 | field-type | E2165 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000348 | parent | C4596 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000348 | field-type | E4597 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000348 | field-type | E4598 | DeniedReasonCode | Not a component record in this worksheet |
| src-000348 | field-type | E4599 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000348 | field-type | E4600 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000348 | field-type | E4601 | AllegementReasonCode | Not a component record in this worksheet |
| src-000348 | field-type | E4602 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000348 | field-type | E4603 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000348 | field-type | E4604 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000348 | field-type | E4605 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000348 | field-type | E4606 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000348 | field-type | E4607 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000352 | parent | C4627 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000352 | field-type | E4628 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000352 | field-type | E4629 | DeniedReasonCode | Not a component record in this worksheet |
| src-000352 | field-type | E4630 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000352 | field-type | E4631 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000352 | field-type | E4632 | AllegementReasonCode | Not a component record in this worksheet |
| src-000352 | field-type | E4633 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000352 | field-type | E4634 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000352 | field-type | E4635 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000352 | field-type | E4636 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000352 | field-type | E4637 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000352 | field-type | E4638 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000355 | parent | C4531 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000355 | field-type | E4532 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000355 | field-type | E4533 | DeniedReasonCode | Not a component record in this worksheet |
| src-000355 | field-type | E4534 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000355 | field-type | E4535 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000355 | field-type | E4536 | AllegementReasonCode | Not a component record in this worksheet |
| src-000355 | field-type | E4537 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000355 | field-type | E4538 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000355 | field-type | E4539 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000355 | field-type | E4540 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000355 | field-type | E4541 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000355 | field-type | E4542 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000358 | parent | C2154 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000358 | field-type | E2155 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000358 | field-type | E2156 | DeniedReasonCode | Not a component record in this worksheet |
| src-000358 | field-type | E2157 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000358 | field-type | E2158 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000358 | field-type | E2159 | AllegementReasonCode | Not a component record in this worksheet |
| src-000358 | field-type | E2160 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000358 | field-type | E2161 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000358 | field-type | E2162 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000358 | field-type | E2163 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000358 | field-type | E2164 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000358 | field-type | E2165 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000361 | parent | C2154 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000361 | field-type | E2155 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000361 | field-type | E2156 | DeniedReasonCode | Not a component record in this worksheet |
| src-000361 | field-type | E2157 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000361 | field-type | E2158 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000361 | field-type | E2159 | AllegementReasonCode | Not a component record in this worksheet |
| src-000361 | field-type | E2160 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000361 | field-type | E2161 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000361 | field-type | E2162 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000361 | field-type | E2163 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000361 | field-type | E2164 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000361 | field-type | E2165 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000364 | parent | C4531 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000364 | field-type | E4532 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000364 | field-type | E4533 | DeniedReasonCode | Not a component record in this worksheet |
| src-000364 | field-type | E4534 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000364 | field-type | E4535 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000364 | field-type | E4536 | AllegementReasonCode | Not a component record in this worksheet |
| src-000364 | field-type | E4537 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000364 | field-type | E4538 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000364 | field-type | E4539 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000364 | field-type | E4540 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000364 | field-type | E4541 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000364 | field-type | E4542 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000367 | parent | C4531 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000367 | field-type | E4532 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000367 | field-type | E4533 | DeniedReasonCode | Not a component record in this worksheet |
| src-000367 | field-type | E4534 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000367 | field-type | E4535 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000367 | field-type | E4536 | AllegementReasonCode | Not a component record in this worksheet |
| src-000367 | field-type | E4537 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000367 | field-type | E4538 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000367 | field-type | E4539 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000367 | field-type | E4540 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000367 | field-type | E4541 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000367 | field-type | E4542 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000370 | parent | C2154 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000370 | field-type | E2155 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000370 | field-type | E2156 | DeniedReasonCode | Not a component record in this worksheet |
| src-000370 | field-type | E2157 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000370 | field-type | E2158 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000370 | field-type | E2159 | AllegementReasonCode | Not a component record in this worksheet |
| src-000370 | field-type | E2160 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000370 | field-type | E2161 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000370 | field-type | E2162 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000370 | field-type | E2163 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000370 | field-type | E2164 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000370 | field-type | E2165 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000373 | parent | C2154 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000373 | field-type | E2155 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000373 | field-type | E2156 | DeniedReasonCode | Not a component record in this worksheet |
| src-000373 | field-type | E2157 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000373 | field-type | E2158 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000373 | field-type | E2159 | AllegementReasonCode | Not a component record in this worksheet |
| src-000373 | field-type | E2160 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000373 | field-type | E2161 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000373 | field-type | E2162 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000373 | field-type | E2163 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000373 | field-type | E2164 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000373 | field-type | E2165 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000376 | parent | C4627 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000376 | field-type | E4628 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000376 | field-type | E4629 | DeniedReasonCode | Not a component record in this worksheet |
| src-000376 | field-type | E4630 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000376 | field-type | E4631 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000376 | field-type | E4632 | AllegementReasonCode | Not a component record in this worksheet |
| src-000376 | field-type | E4633 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000376 | field-type | E4634 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000376 | field-type | E4635 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000376 | field-type | E4636 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000376 | field-type | E4637 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000376 | field-type | E4638 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000379 | parent | C2154 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000379 | field-type | E2155 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000379 | field-type | E2156 | DeniedReasonCode | Not a component record in this worksheet |
| src-000379 | field-type | E2157 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000379 | field-type | E2158 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000379 | field-type | E2159 | AllegementReasonCode | Not a component record in this worksheet |
| src-000379 | field-type | E2160 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000379 | field-type | E2161 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000379 | field-type | E2162 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000379 | field-type | E2163 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000379 | field-type | E2164 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000379 | field-type | E2165 | ModifiedStatusReasonCode | Not a component record in this worksheet |
| src-000382 | parent | C4596 | StatusReason | [StatusReason](<bc-16aa02c25edbb2a74395.md>) |
| src-000382 | field-type | E4597 | UnmatchedReasonCode | Not a component record in this worksheet |
| src-000382 | field-type | E4598 | DeniedReasonCode | Not a component record in this worksheet |
| src-000382 | field-type | E4599 | SecuritiesTradeStatus | [SecuritiesTradeStatus](<bc-5c133c4441f802345a48.md>) |
| src-000382 | field-type | E4600 | GeneratedReasonCode | Not a component record in this worksheet |
| src-000382 | field-type | E4601 | AllegementReasonCode | Not a component record in this worksheet |
| src-000382 | field-type | E4602 | PendingSettlementStatusReasonCode | Not a component record in this worksheet |
| src-000382 | field-type | E4603 | RepoCallAcknowledgementReasonCode | Not a component record in this worksheet |
| src-000382 | field-type | E4604 | RepairReasonV2Code | Not a component record in this worksheet |
| src-000382 | field-type | E4605 | DeliveryReturnCode | Not a component record in this worksheet |
| src-000382 | field-type | E4606 | CounterpartyResponseStatusReasonCode | Not a component record in this worksheet |
| src-000382 | field-type | E4607 | ModifiedStatusReasonCode | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
