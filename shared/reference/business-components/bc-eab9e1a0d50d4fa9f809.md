---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-eab9e1a0d50d4fa9f809"
title: "Pension"
business_component_name: "Pension"
aliases: []
domain: "shared"
domains: ["payments", "securities"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-link-reference-data", "t2s-securities-and-penalty-reporting", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000348", "src-000352", "src-000355", "src-000367", "src-000376", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2024", "december-2025", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A3253:F3266"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A3207:F3220"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A3253:F3266"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A3253:F3266"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A3253:F3266"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A3253:F3266"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A3253:F3266"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A3207:F3220"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A3253:F3266"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A3229:F3242"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A3229:F3242"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A3253:F3266"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A3193:F3206"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A3193:F3206"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A3253:F3266"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A3229:F3242"]}]
content_sha256: "eab9e1a0d50d4fa9f8090c0f6d8e871cc3fa9d067495137d579dcf4ec166821a"
parent_names: []
related_component_names: ["AmountAndPeriod", "DecimalNumber", "Drawdown", "GenericIdentification", "InvestmentPlan", "LumpSumTypeCode", "PensionOrderTypeCode", "PensionSchemeTypeCode", "PensionTransferScopeCode", "PersonIdentificationTypeCode", "YesNoIndicator"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# Pension

## Definition

Attributes of a pension.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Pension | ∅ | ∅ | Attributes of a pension. | ∅ | ∅ |
| 2 | Pension | ValueOfPensionPolicy | ∅ | Value of the pension policy, plan or scheme. | AmountAndPeriod | ∅ |
| 3 | Pension | RelatedInvestmentPlan | ∅ | Plan that allows investors to schedule periodical investments or divestments, according to pre-defined criteria. | InvestmentPlan | Pension |
| 4 | Pension | EstimatedValue | ∅ | Estimated value of the pension policy, plan or scheme. | AmountAndPeriod | ∅ |
| 5 | Pension | TransferScope | ∅ | Scope of the pension policy, plan or scheme transfer. | PensionTransferScopeCode | ∅ |
| 6 | Pension | Drawdown | ∅ | Details of a drawdown tranche. | Drawdown | Pension |
| 7 | Pension | PensionOrderType | ∅ | Type of order attached to the pension policy, plan or scheme. | PensionOrderTypeCode | ∅ |
| 8 | Pension | RetirementAge | ∅ | Age at which the pension policy, plan or scheme holder retires. | DecimalNumber | ∅ |
| 9 | Pension | Identification | ∅ | Identification of the pension policy, plan or scheme. | GenericIdentification | ∅ |
| 10 | Pension | Type | ∅ | Type of pension policy, plan or scheme. | PensionSchemeTypeCode | ∅ |
| 11 | Pension | TaxFreeCashAmount | ∅ | Amount of cash that is tax free. | AmountAndPeriod | ∅ |
| 12 | Pension | LumpSumType | ∅ | Type of lump sum paid to a member of the pension policy, plan or scheme. | LumpSumTypeCode | ∅ |
| 13 | Pension | TaxReference | ∅ | Tax reference issued to the pension policy, plan or scheme by a central organisation. | PersonIdentificationTypeCode | ∅ |
| 14 | Pension | ClientLifetimeAllowanceProtection | ∅ | Indicates whether the client has any lifetime allowance protection. | YesNoIndicator | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `eab9e1a0d50d4fa9f8090c0f6d8e871cc3fa9d067495137d579dcf4ec166821a`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A3253:F3266 | 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A3207:F3220 | 3207, 3208, 3209, 3210, 3211, 3212, 3213, 3214, 3215, 3216, 3217, 3218, 3219, 3220 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A3253:F3266 | 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A3253:F3266 | 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A3253:F3266 | 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A3253:F3266 | 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A3253:F3266 | 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A3207:F3220 | 3207, 3208, 3209, 3210, 3211, 3212, 3213, 3214, 3215, 3216, 3217, 3218, 3219, 3220 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A3253:F3266 | 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A3229:F3242 | 3229, 3230, 3231, 3232, 3233, 3234, 3235, 3236, 3237, 3238, 3239, 3240, 3241, 3242 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000348 | FullBusinessModel!A3229:F3242 | 3229, 3230, 3231, 3232, 3233, 3234, 3235, 3236, 3237, 3238, 3239, 3240, 3241, 3242 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A3253:F3266 | 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A3193:F3206 | 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200, 3201, 3202, 3203, 3204, 3205, 3206 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000367 | FullBusinessModel!A3193:F3206 | 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200, 3201, 3202, 3203, 3204, 3205, 3206 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000376 | FullBusinessModel!A3253:F3266 | 3253, 3254, 3255, 3256, 3257, 3258, 3259, 3260, 3261, 3262, 3263, 3264, 3265, 3266 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000382 | FullBusinessModel!A3229:F3242 | 3229, 3230, 3231, 3232, 3233, 3234, 3235, 3236, 3237, 3238, 3239, 3240, 3241, 3242 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E3254 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000006 | field-type | E3255 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000006 | field-type | E3256 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000006 | field-type | E3257 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000006 | field-type | E3258 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000006 | field-type | E3259 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E3260 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E3261 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000006 | field-type | E3262 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E3263 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000006 | field-type | E3264 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E3265 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E3266 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E3208 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000016 | field-type | E3209 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000016 | field-type | E3210 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000016 | field-type | E3211 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000016 | field-type | E3212 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000016 | field-type | E3213 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E3214 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E3215 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000016 | field-type | E3216 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E3217 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000016 | field-type | E3218 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E3219 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E3220 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E3254 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000054 | field-type | E3255 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000054 | field-type | E3256 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000054 | field-type | E3257 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000054 | field-type | E3258 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000054 | field-type | E3259 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E3260 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E3261 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000054 | field-type | E3262 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E3263 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000054 | field-type | E3264 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E3265 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E3266 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E3254 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000081 | field-type | E3255 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000081 | field-type | E3256 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000081 | field-type | E3257 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000081 | field-type | E3258 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000081 | field-type | E3259 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E3260 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E3261 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000081 | field-type | E3262 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E3263 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000081 | field-type | E3264 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E3265 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E3266 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E3254 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000097 | field-type | E3255 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000097 | field-type | E3256 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000097 | field-type | E3257 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000097 | field-type | E3258 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000097 | field-type | E3259 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E3260 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E3261 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000097 | field-type | E3262 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E3263 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000097 | field-type | E3264 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E3265 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E3266 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E3254 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000164 | field-type | E3255 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000164 | field-type | E3256 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000164 | field-type | E3257 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000164 | field-type | E3258 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000164 | field-type | E3259 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E3260 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E3261 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000164 | field-type | E3262 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E3263 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000164 | field-type | E3264 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E3265 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E3266 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E3254 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000175 | field-type | E3255 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000175 | field-type | E3256 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000175 | field-type | E3257 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000175 | field-type | E3258 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000175 | field-type | E3259 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E3260 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E3261 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000175 | field-type | E3262 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E3263 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000175 | field-type | E3264 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E3265 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E3266 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E3208 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000182 | field-type | E3209 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000182 | field-type | E3210 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000182 | field-type | E3211 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000182 | field-type | E3212 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000182 | field-type | E3213 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E3214 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E3215 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000182 | field-type | E3216 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E3217 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000182 | field-type | E3218 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E3219 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E3220 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E3254 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000198 | field-type | E3255 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000198 | field-type | E3256 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000198 | field-type | E3257 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000198 | field-type | E3258 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000198 | field-type | E3259 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E3260 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E3261 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000198 | field-type | E3262 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E3263 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000198 | field-type | E3264 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E3265 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E3266 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E3230 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000322 | field-type | E3231 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000322 | field-type | E3232 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000322 | field-type | E3233 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000322 | field-type | E3234 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000322 | field-type | E3235 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000322 | field-type | E3236 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E3237 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000322 | field-type | E3238 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000322 | field-type | E3239 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000322 | field-type | E3240 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000322 | field-type | E3241 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000322 | field-type | E3242 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E3230 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000348 | field-type | E3231 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000348 | field-type | E3232 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000348 | field-type | E3233 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000348 | field-type | E3234 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000348 | field-type | E3235 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000348 | field-type | E3236 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E3237 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000348 | field-type | E3238 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000348 | field-type | E3239 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000348 | field-type | E3240 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000348 | field-type | E3241 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000348 | field-type | E3242 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E3254 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000352 | field-type | E3255 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000352 | field-type | E3256 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000352 | field-type | E3257 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000352 | field-type | E3258 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000352 | field-type | E3259 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E3260 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E3261 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000352 | field-type | E3262 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E3263 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000352 | field-type | E3264 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E3265 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E3266 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E3194 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000355 | field-type | E3195 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000355 | field-type | E3196 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000355 | field-type | E3197 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000355 | field-type | E3198 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000355 | field-type | E3199 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E3200 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E3201 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000355 | field-type | E3202 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E3203 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000355 | field-type | E3204 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E3205 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E3206 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E3194 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000367 | field-type | E3195 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000367 | field-type | E3196 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000367 | field-type | E3197 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000367 | field-type | E3198 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000367 | field-type | E3199 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E3200 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E3201 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000367 | field-type | E3202 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E3203 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000367 | field-type | E3204 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E3205 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E3206 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E3254 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000376 | field-type | E3255 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000376 | field-type | E3256 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000376 | field-type | E3257 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000376 | field-type | E3258 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000376 | field-type | E3259 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E3260 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E3261 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000376 | field-type | E3262 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E3263 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000376 | field-type | E3264 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E3265 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E3266 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E3230 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000382 | field-type | E3231 | InvestmentPlan | [InvestmentPlan](<bc-3e6c5f3d5f23fafb2fe9.md>) |
| src-000382 | field-type | E3232 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000382 | field-type | E3233 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000382 | field-type | E3234 | Drawdown | [Drawdown](<bc-099ad98b127d26a7141e.md>) |
| src-000382 | field-type | E3235 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000382 | field-type | E3236 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E3237 | GenericIdentification | [GenericIdentification](<bc-52a5f70d1af9b4453d6c.md>) |
| src-000382 | field-type | E3238 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000382 | field-type | E3239 | AmountAndPeriod | [AmountAndPeriod](<bc-02a0ff31c36dc262f753.md>) |
| src-000382 | field-type | E3240 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000382 | field-type | E3241 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000382 | field-type | E3242 | YesNoIndicator | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
