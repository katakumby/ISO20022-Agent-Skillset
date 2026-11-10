---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-2ec6ceb3eba4a954f1a0"
title: "SecuritiesAccount"
business_component_name: "SecuritiesAccount"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A3889:F3909"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A3819:F3839"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A3889:F3909"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A3889:F3909"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A3889:F3909"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A3889:F3909"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A3889:F3909"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A3819:F3839"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A3889:F3909"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A3858:F3878"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A764:F784"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A3858:F3878"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A3889:F3909"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A3797:F3817"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A764:F784"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A764:F784"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A3797:F3817"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A3797:F3817"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A764:F784"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A764:F784"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A3889:F3909"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A764:F784"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A3858:F3878"]}]
content_sha256: "2ec6ceb3eba4a954f1a0b4fd86fe8f590f3ce813de5af956471a4e4e7adc1987"
parent_names: ["Account"]
related_component_names: ["AccountLink", "Allocation", "ClearingAccountTypeCode", "ClearingMemberRole", "CorporateActionServicing", "DisclosedListTrading", "InstructionForMeeting", "InvestmentAccount", "PowerOfAttorney", "RegistrarRole", "SafekeepingPlace", "SecuritiesAccountPurposeTypeCode", "SecuritiesBalance", "SecuritiesEntry", "SecuritiesOrder", "SecuritiesPartyRole", "SecuritiesTransfer", "Security"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# SecuritiesAccount

## Definition

Account to or from which a securities entry is made.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SecuritiesAccount | ∅ | Account | Account to or from which a securities entry is made. | ∅ | ∅ |
| 2 | SecuritiesAccount | SecuritiesAccountType | ∅ | Specifies the type of securities account. | SecuritiesAccountPurposeTypeCode | ∅ |
| 3 | SecuritiesAccount | RelatedInvestmentAccount | ∅ | Investment account which contains a securities account to make securities movements. | InvestmentAccount | SecuritiesAccount |
| 4 | SecuritiesAccount | RelatedTransfer | ∅ | Specifies the process which moves securities out of an account to another one. | SecuritiesTransfer | Account |
| 5 | SecuritiesAccount | SecuritiesPartyRole | ∅ | Specifies the role which uses a securities account. | SecuritiesPartyRole | SecuritiesAccount |
| 6 | SecuritiesAccount | Security | ∅ | Security which is held on the securities account. | Security | SecuritiesAccount |
| 7 | SecuritiesAccount | RelatedRegistrar | ∅ | Specifies where the financial instruments are registered. | RegistrarRole | RegistrarAccount |
| 8 | SecuritiesAccount | SafekeepingPlace | ∅ | Location where the financial instruments are safekept. | SafekeepingPlace | RelatedSecuritiesAccount |
| 9 | SecuritiesAccount | SecuritiesBalance | ∅ | Value of financial assets held by a person or an organisation. It is derived from the association between Account and Balance. | SecuritiesBalance | SecuritiesAccount |
| 10 | SecuritiesAccount | CorporateActionServicing | ∅ | Actions taken in relation with the securities account in the context of the corporate action. | CorporateActionServicing | SecuritiesAccount |
| 11 | SecuritiesAccount | RelatedAllocation | ∅ | Allocation process for which an account is specified. | Allocation | AllocationAccount |
| 12 | SecuritiesAccount | SecuritiesEntry | ∅ | Record of the movements into or out of an account. | SecuritiesEntry | SecuritiesAccount |
| 13 | SecuritiesAccount | ClearingAccountOwner | ∅ | Clearing member which holds a clearing account at a CCP. | ClearingMemberRole | ClearingAccount |
| 14 | SecuritiesAccount | MarginAccountOwner | ∅ | Clearing member which holds a margin account at a CCP. | ClearingMemberRole | MarginAccount |
| 15 | SecuritiesAccount | DeliveryAccountOwner | ∅ | Clearing member which holds a delivery account at a CCP. | ClearingMemberRole | DeliveryAccount |
| 16 | SecuritiesAccount | RelatedPowerOfAttorney | ∅ | Power of attorney related to the securities account. | PowerOfAttorney | AuthorisedAccount |
| 17 | SecuritiesAccount | RelatedMeetingInstruction | ∅ | Meeting instruction which specifies an account. | InstructionForMeeting | SafekeepingAccount |
| 18 | SecuritiesAccount | ClearingAccountType | ∅ | Specifies the clearing account type. | ClearingAccountTypeCode | ∅ |
| 19 | SecuritiesAccount | RelatedOrder | ∅ | Order process for which an ordering account is specified. | SecuritiesOrder | OrderingAccount |
| 20 | SecuritiesAccount | DisclosedListTrading | ∅ | Disclosed list trading process for which a trading account is specified. | DisclosedListTrading | DisclosedListTradingAccount |
| 21 | SecuritiesAccount | AccountLink | ∅ | Defines the link between a cash account and a securities account. | AccountLink | SecuritiesAccount |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `2ec6ceb3eba4a954f1a0b4fd86fe8f590f3ce813de5af956471a4e4e7adc1987`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A3889:F3909 | 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A3819:F3839 | 3819, 3820, 3821, 3822, 3823, 3824, 3825, 3826, 3827, 3828, 3829, 3830, 3831, 3832, 3833, 3834, 3835, 3836, 3837, 3838, 3839 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A3889:F3909 | 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A3889:F3909 | 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A3889:F3909 | 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A3889:F3909 | 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A3889:F3909 | 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A3819:F3839 | 3819, 3820, 3821, 3822, 3823, 3824, 3825, 3826, 3827, 3828, 3829, 3830, 3831, 3832, 3833, 3834, 3835, 3836, 3837, 3838, 3839 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A3889:F3909 | 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A3858:F3878 | 3858, 3859, 3860, 3861, 3862, 3863, 3864, 3865, 3866, 3867, 3868, 3869, 3870, 3871, 3872, 3873, 3874, 3875, 3876, 3877, 3878 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000345 | FullBusinessModel!A764:F784 | 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000348 | FullBusinessModel!A3858:F3878 | 3858, 3859, 3860, 3861, 3862, 3863, 3864, 3865, 3866, 3867, 3868, 3869, 3870, 3871, 3872, 3873, 3874, 3875, 3876, 3877, 3878 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A3889:F3909 | 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A3797:F3817 | 3797, 3798, 3799, 3800, 3801, 3802, 3803, 3804, 3805, 3806, 3807, 3808, 3809, 3810, 3811, 3812, 3813, 3814, 3815, 3816, 3817 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A764:F784 | 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A764:F784 | 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A3797:F3817 | 3797, 3798, 3799, 3800, 3801, 3802, 3803, 3804, 3805, 3806, 3807, 3808, 3809, 3810, 3811, 3812, 3813, 3814, 3815, 3816, 3817 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A3797:F3817 | 3797, 3798, 3799, 3800, 3801, 3802, 3803, 3804, 3805, 3806, 3807, 3808, 3809, 3810, 3811, 3812, 3813, 3814, 3815, 3816, 3817 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A764:F784 | 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A764:F784 | 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000376 | FullBusinessModel!A3889:F3909 | 3889, 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000379 | FullBusinessModel!A764:F784 | 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |
| src-000382 | FullBusinessModel!A3858:F3878 | 3858, 3859, 3860, 3861, 3862, 3863, 3864, 3865, 3866, 3867, 3868, 3869, 3870, 3871, 3872, 3873, 3874, 3875, 3876, 3877, 3878 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C3889 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000006 | field-type | E3890 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E3891 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000006 | field-type | E3892 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000006 | field-type | E3893 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000006 | field-type | E3894 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000006 | field-type | E3895 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000006 | field-type | E3896 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000006 | field-type | E3897 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000006 | field-type | E3898 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000006 | field-type | E3899 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000006 | field-type | E3900 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000006 | field-type | E3901 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000006 | field-type | E3902 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000006 | field-type | E3903 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000006 | field-type | E3904 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000006 | field-type | E3905 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000006 | field-type | E3906 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E3907 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000006 | field-type | E3908 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000006 | field-type | E3909 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000016 | parent | C3819 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000016 | field-type | E3820 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E3821 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000016 | field-type | E3822 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000016 | field-type | E3823 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000016 | field-type | E3824 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000016 | field-type | E3825 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000016 | field-type | E3826 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000016 | field-type | E3827 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000016 | field-type | E3828 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000016 | field-type | E3829 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000016 | field-type | E3830 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000016 | field-type | E3831 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000016 | field-type | E3832 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000016 | field-type | E3833 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000016 | field-type | E3834 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000016 | field-type | E3835 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000016 | field-type | E3836 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E3837 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000016 | field-type | E3838 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000016 | field-type | E3839 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000054 | parent | C3889 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000054 | field-type | E3890 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E3891 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000054 | field-type | E3892 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000054 | field-type | E3893 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000054 | field-type | E3894 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000054 | field-type | E3895 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000054 | field-type | E3896 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000054 | field-type | E3897 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000054 | field-type | E3898 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000054 | field-type | E3899 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000054 | field-type | E3900 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000054 | field-type | E3901 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000054 | field-type | E3902 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000054 | field-type | E3903 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000054 | field-type | E3904 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000054 | field-type | E3905 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000054 | field-type | E3906 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E3907 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000054 | field-type | E3908 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000054 | field-type | E3909 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000081 | parent | C3889 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000081 | field-type | E3890 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E3891 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000081 | field-type | E3892 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000081 | field-type | E3893 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000081 | field-type | E3894 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000081 | field-type | E3895 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000081 | field-type | E3896 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000081 | field-type | E3897 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000081 | field-type | E3898 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000081 | field-type | E3899 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000081 | field-type | E3900 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000081 | field-type | E3901 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000081 | field-type | E3902 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000081 | field-type | E3903 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000081 | field-type | E3904 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000081 | field-type | E3905 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000081 | field-type | E3906 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E3907 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000081 | field-type | E3908 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000081 | field-type | E3909 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000097 | parent | C3889 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000097 | field-type | E3890 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E3891 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000097 | field-type | E3892 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000097 | field-type | E3893 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000097 | field-type | E3894 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000097 | field-type | E3895 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000097 | field-type | E3896 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000097 | field-type | E3897 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000097 | field-type | E3898 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000097 | field-type | E3899 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000097 | field-type | E3900 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000097 | field-type | E3901 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000097 | field-type | E3902 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000097 | field-type | E3903 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000097 | field-type | E3904 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000097 | field-type | E3905 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000097 | field-type | E3906 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E3907 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000097 | field-type | E3908 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000097 | field-type | E3909 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000164 | parent | C3889 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000164 | field-type | E3890 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E3891 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000164 | field-type | E3892 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000164 | field-type | E3893 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000164 | field-type | E3894 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000164 | field-type | E3895 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000164 | field-type | E3896 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000164 | field-type | E3897 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000164 | field-type | E3898 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000164 | field-type | E3899 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000164 | field-type | E3900 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000164 | field-type | E3901 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000164 | field-type | E3902 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000164 | field-type | E3903 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000164 | field-type | E3904 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000164 | field-type | E3905 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000164 | field-type | E3906 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E3907 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000164 | field-type | E3908 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000164 | field-type | E3909 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000175 | parent | C3889 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000175 | field-type | E3890 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E3891 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000175 | field-type | E3892 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000175 | field-type | E3893 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000175 | field-type | E3894 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000175 | field-type | E3895 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000175 | field-type | E3896 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000175 | field-type | E3897 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000175 | field-type | E3898 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000175 | field-type | E3899 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000175 | field-type | E3900 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000175 | field-type | E3901 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000175 | field-type | E3902 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000175 | field-type | E3903 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000175 | field-type | E3904 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000175 | field-type | E3905 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000175 | field-type | E3906 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E3907 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000175 | field-type | E3908 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000175 | field-type | E3909 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000182 | parent | C3819 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000182 | field-type | E3820 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E3821 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000182 | field-type | E3822 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000182 | field-type | E3823 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000182 | field-type | E3824 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000182 | field-type | E3825 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000182 | field-type | E3826 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000182 | field-type | E3827 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000182 | field-type | E3828 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000182 | field-type | E3829 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000182 | field-type | E3830 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000182 | field-type | E3831 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000182 | field-type | E3832 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000182 | field-type | E3833 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000182 | field-type | E3834 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000182 | field-type | E3835 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000182 | field-type | E3836 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E3837 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000182 | field-type | E3838 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000182 | field-type | E3839 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000198 | parent | C3889 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000198 | field-type | E3890 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E3891 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000198 | field-type | E3892 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000198 | field-type | E3893 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000198 | field-type | E3894 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000198 | field-type | E3895 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000198 | field-type | E3896 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000198 | field-type | E3897 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000198 | field-type | E3898 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000198 | field-type | E3899 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000198 | field-type | E3900 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000198 | field-type | E3901 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000198 | field-type | E3902 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000198 | field-type | E3903 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000198 | field-type | E3904 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000198 | field-type | E3905 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000198 | field-type | E3906 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E3907 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000198 | field-type | E3908 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000198 | field-type | E3909 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000322 | parent | C3858 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000322 | field-type | E3859 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000322 | field-type | E3860 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000322 | field-type | E3861 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000322 | field-type | E3862 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000322 | field-type | E3863 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000322 | field-type | E3864 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000322 | field-type | E3865 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000322 | field-type | E3866 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000322 | field-type | E3867 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000322 | field-type | E3868 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000322 | field-type | E3869 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000322 | field-type | E3870 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000322 | field-type | E3871 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000322 | field-type | E3872 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000322 | field-type | E3873 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000322 | field-type | E3874 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000322 | field-type | E3875 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000322 | field-type | E3876 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000322 | field-type | E3877 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000322 | field-type | E3878 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000345 | parent | C764 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000345 | field-type | E765 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E766 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000345 | field-type | E767 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000345 | field-type | E768 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000345 | field-type | E769 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000345 | field-type | E770 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000345 | field-type | E771 | SafekeepingPlace | [SafekeepingPlace](<bc-d7537dec2f3ab540e9a6.md>) |
| src-000345 | field-type | E772 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000345 | field-type | E773 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000345 | field-type | E774 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000345 | field-type | E775 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000345 | field-type | E776 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000345 | field-type | E777 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000345 | field-type | E778 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000345 | field-type | E779 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000345 | field-type | E780 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000345 | field-type | E781 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E782 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000345 | field-type | E783 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000345 | field-type | E784 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000348 | parent | C3858 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000348 | field-type | E3859 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000348 | field-type | E3860 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000348 | field-type | E3861 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000348 | field-type | E3862 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000348 | field-type | E3863 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000348 | field-type | E3864 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000348 | field-type | E3865 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000348 | field-type | E3866 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000348 | field-type | E3867 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000348 | field-type | E3868 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000348 | field-type | E3869 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000348 | field-type | E3870 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000348 | field-type | E3871 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000348 | field-type | E3872 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000348 | field-type | E3873 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000348 | field-type | E3874 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000348 | field-type | E3875 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000348 | field-type | E3876 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000348 | field-type | E3877 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000348 | field-type | E3878 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000352 | parent | C3889 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000352 | field-type | E3890 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E3891 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000352 | field-type | E3892 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000352 | field-type | E3893 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000352 | field-type | E3894 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000352 | field-type | E3895 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000352 | field-type | E3896 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000352 | field-type | E3897 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000352 | field-type | E3898 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000352 | field-type | E3899 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000352 | field-type | E3900 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000352 | field-type | E3901 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000352 | field-type | E3902 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000352 | field-type | E3903 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000352 | field-type | E3904 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000352 | field-type | E3905 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000352 | field-type | E3906 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E3907 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000352 | field-type | E3908 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000352 | field-type | E3909 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000355 | parent | C3797 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000355 | field-type | E3798 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E3799 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000355 | field-type | E3800 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000355 | field-type | E3801 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000355 | field-type | E3802 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000355 | field-type | E3803 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000355 | field-type | E3804 | SafekeepingPlace | [SafekeepingPlace](<bc-d7537dec2f3ab540e9a6.md>) |
| src-000355 | field-type | E3805 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000355 | field-type | E3806 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000355 | field-type | E3807 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000355 | field-type | E3808 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000355 | field-type | E3809 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000355 | field-type | E3810 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000355 | field-type | E3811 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000355 | field-type | E3812 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000355 | field-type | E3813 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000355 | field-type | E3814 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E3815 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000355 | field-type | E3816 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000355 | field-type | E3817 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000358 | parent | C764 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000358 | field-type | E765 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E766 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000358 | field-type | E767 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000358 | field-type | E768 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000358 | field-type | E769 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000358 | field-type | E770 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000358 | field-type | E771 | SafekeepingPlace | [SafekeepingPlace](<bc-d7537dec2f3ab540e9a6.md>) |
| src-000358 | field-type | E772 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000358 | field-type | E773 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000358 | field-type | E774 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000358 | field-type | E775 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000358 | field-type | E776 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000358 | field-type | E777 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000358 | field-type | E778 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000358 | field-type | E779 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000358 | field-type | E780 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000358 | field-type | E781 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E782 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000358 | field-type | E783 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000358 | field-type | E784 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000361 | parent | C764 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000361 | field-type | E765 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E766 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000361 | field-type | E767 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000361 | field-type | E768 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000361 | field-type | E769 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000361 | field-type | E770 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000361 | field-type | E771 | SafekeepingPlace | [SafekeepingPlace](<bc-d7537dec2f3ab540e9a6.md>) |
| src-000361 | field-type | E772 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000361 | field-type | E773 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000361 | field-type | E774 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000361 | field-type | E775 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000361 | field-type | E776 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000361 | field-type | E777 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000361 | field-type | E778 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000361 | field-type | E779 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000361 | field-type | E780 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000361 | field-type | E781 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E782 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000361 | field-type | E783 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000361 | field-type | E784 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000364 | parent | C3797 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000364 | field-type | E3798 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E3799 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000364 | field-type | E3800 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000364 | field-type | E3801 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000364 | field-type | E3802 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000364 | field-type | E3803 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000364 | field-type | E3804 | SafekeepingPlace | [SafekeepingPlace](<bc-d7537dec2f3ab540e9a6.md>) |
| src-000364 | field-type | E3805 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000364 | field-type | E3806 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000364 | field-type | E3807 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000364 | field-type | E3808 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000364 | field-type | E3809 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000364 | field-type | E3810 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000364 | field-type | E3811 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000364 | field-type | E3812 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000364 | field-type | E3813 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000364 | field-type | E3814 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E3815 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000364 | field-type | E3816 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000364 | field-type | E3817 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000367 | parent | C3797 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000367 | field-type | E3798 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E3799 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000367 | field-type | E3800 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000367 | field-type | E3801 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000367 | field-type | E3802 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000367 | field-type | E3803 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000367 | field-type | E3804 | SafekeepingPlace | [SafekeepingPlace](<bc-d7537dec2f3ab540e9a6.md>) |
| src-000367 | field-type | E3805 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000367 | field-type | E3806 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000367 | field-type | E3807 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000367 | field-type | E3808 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000367 | field-type | E3809 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000367 | field-type | E3810 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000367 | field-type | E3811 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000367 | field-type | E3812 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000367 | field-type | E3813 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000367 | field-type | E3814 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E3815 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000367 | field-type | E3816 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000367 | field-type | E3817 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000370 | parent | C764 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000370 | field-type | E765 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E766 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000370 | field-type | E767 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000370 | field-type | E768 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000370 | field-type | E769 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000370 | field-type | E770 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000370 | field-type | E771 | SafekeepingPlace | [SafekeepingPlace](<bc-d7537dec2f3ab540e9a6.md>) |
| src-000370 | field-type | E772 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000370 | field-type | E773 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000370 | field-type | E774 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000370 | field-type | E775 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000370 | field-type | E776 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000370 | field-type | E777 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000370 | field-type | E778 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000370 | field-type | E779 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000370 | field-type | E780 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000370 | field-type | E781 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E782 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000370 | field-type | E783 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000370 | field-type | E784 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000373 | parent | C764 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000373 | field-type | E765 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E766 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000373 | field-type | E767 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000373 | field-type | E768 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000373 | field-type | E769 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000373 | field-type | E770 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000373 | field-type | E771 | SafekeepingPlace | [SafekeepingPlace](<bc-d7537dec2f3ab540e9a6.md>) |
| src-000373 | field-type | E772 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000373 | field-type | E773 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000373 | field-type | E774 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000373 | field-type | E775 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000373 | field-type | E776 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000373 | field-type | E777 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000373 | field-type | E778 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000373 | field-type | E779 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000373 | field-type | E780 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000373 | field-type | E781 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E782 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000373 | field-type | E783 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000373 | field-type | E784 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000376 | parent | C3889 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000376 | field-type | E3890 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E3891 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000376 | field-type | E3892 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000376 | field-type | E3893 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000376 | field-type | E3894 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000376 | field-type | E3895 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000376 | field-type | E3896 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000376 | field-type | E3897 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000376 | field-type | E3898 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000376 | field-type | E3899 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000376 | field-type | E3900 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000376 | field-type | E3901 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000376 | field-type | E3902 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000376 | field-type | E3903 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000376 | field-type | E3904 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000376 | field-type | E3905 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000376 | field-type | E3906 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E3907 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000376 | field-type | E3908 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000376 | field-type | E3909 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000379 | parent | C764 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000379 | field-type | E765 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E766 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000379 | field-type | E767 | SecuritiesTransfer | [SecuritiesTransfer](<bc-8137c6561b8000e1a45e.md>) |
| src-000379 | field-type | E768 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000379 | field-type | E769 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000379 | field-type | E770 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000379 | field-type | E771 | SafekeepingPlace | [SafekeepingPlace](<bc-d7537dec2f3ab540e9a6.md>) |
| src-000379 | field-type | E772 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000379 | field-type | E773 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000379 | field-type | E774 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000379 | field-type | E775 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000379 | field-type | E776 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000379 | field-type | E777 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000379 | field-type | E778 | ClearingMemberRole | [ClearingMemberRole](<bc-d7b585ddae042395e959.md>) |
| src-000379 | field-type | E779 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000379 | field-type | E780 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000379 | field-type | E781 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E782 | SecuritiesOrder | [SecuritiesOrder](<bc-e970e1551622c18cea65.md>) |
| src-000379 | field-type | E783 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000379 | field-type | E784 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |
| src-000382 | parent | C3858 | Account | [Account](<bc-4e495b8419942b04fd71.md>) |
| src-000382 | field-type | E3859 | SecuritiesAccountPurposeTypeCode | Not a component record in this worksheet |
| src-000382 | field-type | E3860 | InvestmentAccount | [InvestmentAccount](<bc-18c510d816a88eb4a3fe.md>) |
| src-000382 | field-type | E3861 | SecuritiesTransfer | [SecuritiesTransfer](<bc-17225eaf2b81671def32.md>) |
| src-000382 | field-type | E3862 | SecuritiesPartyRole | [SecuritiesPartyRole](<bc-56720c17e9574f824ae7.md>) |
| src-000382 | field-type | E3863 | Security | [Security](<bc-4f8addc5d017fd073013.md>) |
| src-000382 | field-type | E3864 | RegistrarRole | [RegistrarRole](<bc-c9c2cba992a32805f9e9.md>) |
| src-000382 | field-type | E3865 | SafekeepingPlace | [SafekeepingPlace](<bc-894cef4becec0f8593f7.md>) |
| src-000382 | field-type | E3866 | SecuritiesBalance | [SecuritiesBalance](<bc-be8dc03e8889f0ff1fc6.md>) |
| src-000382 | field-type | E3867 | CorporateActionServicing | [CorporateActionServicing](<bc-92131eba5c74bd43c091.md>) |
| src-000382 | field-type | E3868 | Allocation | [Allocation](<bc-a201cdfff93bef35735d.md>) |
| src-000382 | field-type | E3869 | SecuritiesEntry | [SecuritiesEntry](<bc-beb7a2225ae8ab2fb3e7.md>) |
| src-000382 | field-type | E3870 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000382 | field-type | E3871 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000382 | field-type | E3872 | ClearingMemberRole | [ClearingMemberRole](<bc-b5bcbb60167e6c9a39ff.md>) |
| src-000382 | field-type | E3873 | PowerOfAttorney | [PowerOfAttorney](<bc-4fbe43e9818845f1327e.md>) |
| src-000382 | field-type | E3874 | InstructionForMeeting | [InstructionForMeeting](<bc-1168baba1ba305d6574f.md>) |
| src-000382 | field-type | E3875 | ClearingAccountTypeCode | Not a component record in this worksheet |
| src-000382 | field-type | E3876 | SecuritiesOrder | [SecuritiesOrder](<bc-c938575f0889cb96215f.md>) |
| src-000382 | field-type | E3877 | DisclosedListTrading | [DisclosedListTrading](<bc-27717f0901a882368508.md>) |
| src-000382 | field-type | E3878 | AccountLink | [AccountLink](<bc-5ec8793014d770d068f2.md>) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
