---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-1f9faee2c115bc82feb8"
title: "SecuritiesProceedsDefinition"
business_component_name: "SecuritiesProceedsDefinition"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A4329:F4349"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A4259:F4279"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A4329:F4349"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A4329:F4349"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A4329:F4349"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A4329:F4349"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A4329:F4349"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A4259:F4279"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A4329:F4349"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A4298:F4318"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A2721:F2741"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A4298:F4318"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A4329:F4349"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A4237:F4257"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A2721:F2741"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A2721:F2741"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A4237:F4257"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A4237:F4257"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A2721:F2741"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A2721:F2741"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A4329:F4349"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A2721:F2741"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A4298:F4318"]}]
content_sha256: "1f9faee2c115bc82feb8d2665b2ea1bbdef047703fe2907a993128d4000af501"
parent_names: ["ProceedsDefinition"]
related_component_names: ["CurrencyAndAmount", "DateTimePeriod", "ISODateTime", "IntermediateSecurityDistributionTypeCode", "PercentageRate", "QuantityRatio", "SecuritiesQuantity", "ShareRankingCode"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# SecuritiesProceedsDefinition

## Definition

The definition of the securities proceeds for a corporate action in generic terms; that is, before applying it to specific securities holding. An example would be the definition of a  bonus rights issue where all the information will be given in general on a per share basis.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SecuritiesProceedsDefinition | ∅ | ProceedsDefinition | The definition of the securities proceeds for a corporate action in generic terms; that is, before applying it to specific securities holding. An example would be the definition of a  bonus rights issue where all the information will be given in general on a per share basis. | ∅ | ∅ |
| 2 | SecuritiesProceedsDefinition | SecuritiesQuantity | ∅ | The quantity of financial instruments that is posted. | SecuritiesQuantity | SecuritiesProceedsDefinition |
| 3 | SecuritiesProceedsDefinition | ConditionalQuantity | ∅ | Minimum quantity of securities to be accepted (used in the framework of conditional privilege on election). In case of proration, if this minimum quantity is not reached then the instruction is void. | SecuritiesQuantity | ConditionalQuantitySecuritiesProceeds |
| 4 | SecuritiesProceedsDefinition | OverAndAboveNormalEnsuredEntitlementQuantity | ∅ | Quantity instructed to be received over and above normal ensured entitlement. | SecuritiesQuantity | OverAndAboveQuantitySecuritiesProceeds |
| 5 | SecuritiesProceedsDefinition | QuantityToReceive | ∅ | Quantity of the benefits that the account owner wants to receive, for example, as a result of dividend reinvestment. | SecuritiesQuantity | ExpectedQuantitySecuritiesProceeds |
| 6 | SecuritiesProceedsDefinition | StatusQuantity | ∅ | Quantity of securities that has been assigned the status indicated. | SecuritiesQuantity | StatusRelatedSecuritiesProceeds |
| 7 | SecuritiesProceedsDefinition | ParallelTradingPeriod | ∅ | Period during which both old and new equity may be traded simultaneously, eg, consolidation of equity or splitting of equity. | DateTimePeriod | ParallelTradingProceedsDefinition |
| 8 | SecuritiesProceedsDefinition | AdditionalQuantityForSubscribedResultantSecurities | ∅ | Quantity of additional intermediate securities/new equities awarded for a given quantity of securities derived from subscription. | QuantityRatio | AdditionalQuantityForResultantSecuritiesProceedsDefinition |
| 9 | SecuritiesProceedsDefinition | AdditionalQuantityForExistingSecurities | ∅ | Quantity of additional securities for a given quantity of underlying securities where underlying securities are not exchanged or debited, eg, 1 for 1: 1 new equity credited for every 1 underlying equity = 2 resulting equities. | QuantityRatio | AdditionalQuantityForSubscribedSecuritiesProceedsDefinition |
| 10 | SecuritiesProceedsDefinition | NewToOld | ∅ | Quantity of new securities for a given quantity of underlying securities, where the underlying securities will be exchanged or debited, eg, 2 for 1: 2 new equities credited for every 1 underlying equity debited = 2 resulting equities. | QuantityRatio | NewToOldProceedsDefinition |
| 11 | SecuritiesProceedsDefinition | NewSecuritiesToUnderlyingSecurities | ∅ | Quantity of new equities that will be derived by the exercise of a given quantity of intermediate securities. | QuantityRatio | NewToUnderlyingProceedsDefinition |
| 12 | SecuritiesProceedsDefinition | ReinvestmentAmount | ∅ | Amount of money reinvested in additional securities. | CurrencyAndAmount | ∅ |
| 13 | SecuritiesProceedsDefinition | IntermediateSecuritiesDistributionType | ∅ | Type of intermediate securities distribution, eg, stock dividend, reverse right. | IntermediateSecurityDistributionTypeCode | ∅ |
| 14 | SecuritiesProceedsDefinition | BoardLotSecuritiesQuantity | ∅ | Quantity of equity that makes up a board lot. | SecuritiesQuantity | BoardLotSecuritiesProceeds |
| 15 | SecuritiesProceedsDefinition | NewDenominationSecuritiesQuantity | ∅ | New denomination of the financial instrument following, eg, an increase or decrease in nominal value. | SecuritiesQuantity | NewDenominationSecuritiesProceeds |
| 16 | SecuritiesProceedsDefinition | IntermediateSecuritiesToUnderlyingRatio | ∅ | Quantity of intermediate securities awarded for a given quantity of underlying security. | QuantityRatio | IntermediateSecuritiesProceedsDefinition |
| 17 | SecuritiesProceedsDefinition | ReinvestmentDiscountToMarket | ∅ | Rate of discount for securities purchased through a reinvestment scheme as compared to the current market price of security. | PercentageRate | ∅ |
| 18 | SecuritiesProceedsDefinition | RedemptionDate | ∅ | Date on which the securities will be redeemed (early) for payment of principal. | ISODateTime | ∅ |
| 19 | SecuritiesProceedsDefinition | AssentedLinePeriod | ∅ | Period during which the assented line is available. | DateTimePeriod | AssentedLinePeriodProceedsDefinition |
| 20 | SecuritiesProceedsDefinition | SellThruIssuerPeriod | ∅ | Period (last day included) during which an account owner can surrender or sell securities to the issuer and receive the sale proceeds. | DateTimePeriod | SellThruIssuerProceedsDefinition |
| 21 | SecuritiesProceedsDefinition | ShareRanking | ∅ | Specifies whether the shares are ranking for dividend or pari passu. | ShareRankingCode | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `1f9faee2c115bc82feb8d2665b2ea1bbdef047703fe2907a993128d4000af501`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A4329:F4349 | 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4349 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A4259:F4279 | 4259, 4260, 4261, 4262, 4263, 4264, 4265, 4266, 4267, 4268, 4269, 4270, 4271, 4272, 4273, 4274, 4275, 4276, 4277, 4278, 4279 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A4329:F4349 | 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4349 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A4329:F4349 | 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4349 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A4329:F4349 | 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4349 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A4329:F4349 | 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4349 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A4329:F4349 | 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4349 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A4259:F4279 | 4259, 4260, 4261, 4262, 4263, 4264, 4265, 4266, 4267, 4268, 4269, 4270, 4271, 4272, 4273, 4274, 4275, 4276, 4277, 4278, 4279 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A4329:F4349 | 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4349 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A4298:F4318 | 4298, 4299, 4300, 4301, 4302, 4303, 4304, 4305, 4306, 4307, 4308, 4309, 4310, 4311, 4312, 4313, 4314, 4315, 4316, 4317, 4318 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000345 | FullBusinessModel!A2721:F2741 | 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000348 | FullBusinessModel!A4298:F4318 | 4298, 4299, 4300, 4301, 4302, 4303, 4304, 4305, 4306, 4307, 4308, 4309, 4310, 4311, 4312, 4313, 4314, 4315, 4316, 4317, 4318 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A4329:F4349 | 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4349 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A4237:F4257 | 4237, 4238, 4239, 4240, 4241, 4242, 4243, 4244, 4245, 4246, 4247, 4248, 4249, 4250, 4251, 4252, 4253, 4254, 4255, 4256, 4257 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A2721:F2741 | 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A2721:F2741 | 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A4237:F4257 | 4237, 4238, 4239, 4240, 4241, 4242, 4243, 4244, 4245, 4246, 4247, 4248, 4249, 4250, 4251, 4252, 4253, 4254, 4255, 4256, 4257 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A4237:F4257 | 4237, 4238, 4239, 4240, 4241, 4242, 4243, 4244, 4245, 4246, 4247, 4248, 4249, 4250, 4251, 4252, 4253, 4254, 4255, 4256, 4257 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A2721:F2741 | 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A2721:F2741 | 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000376 | FullBusinessModel!A4329:F4349 | 4329, 4330, 4331, 4332, 4333, 4334, 4335, 4336, 4337, 4338, 4339, 4340, 4341, 4342, 4343, 4344, 4345, 4346, 4347, 4348, 4349 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000379 | FullBusinessModel!A2721:F2741 | 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2729, 2730, 2731, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2741 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |
| src-000382 | FullBusinessModel!A4298:F4318 | 4298, 4299, 4300, 4301, 4302, 4303, 4304, 4305, 4306, 4307, 4308, 4309, 4310, 4311, 4312, 4313, 4314, 4315, 4316, 4317, 4318 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C4329 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000006 | field-type | E4330 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E4331 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E4332 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E4333 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E4334 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E4335 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000006 | field-type | E4336 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000006 | field-type | E4337 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000006 | field-type | E4338 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000006 | field-type | E4339 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000006 | field-type | E4340 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E4341 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000006 | field-type | E4342 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E4343 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000006 | field-type | E4344 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000006 | field-type | E4345 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E4346 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E4347 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000006 | field-type | E4348 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000006 | field-type | E4349 | ShareRankingCode | Not a component record in this worksheet |
| src-000016 | parent | C4259 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000016 | field-type | E4260 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E4261 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E4262 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E4263 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E4264 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E4265 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000016 | field-type | E4266 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000016 | field-type | E4267 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000016 | field-type | E4268 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000016 | field-type | E4269 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000016 | field-type | E4270 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E4271 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E4272 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E4273 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000016 | field-type | E4274 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000016 | field-type | E4275 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E4276 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E4277 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000016 | field-type | E4278 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000016 | field-type | E4279 | ShareRankingCode | Not a component record in this worksheet |
| src-000054 | parent | C4329 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000054 | field-type | E4330 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E4331 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E4332 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E4333 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E4334 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E4335 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000054 | field-type | E4336 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000054 | field-type | E4337 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000054 | field-type | E4338 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000054 | field-type | E4339 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000054 | field-type | E4340 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E4341 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000054 | field-type | E4342 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E4343 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000054 | field-type | E4344 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000054 | field-type | E4345 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E4346 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E4347 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000054 | field-type | E4348 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000054 | field-type | E4349 | ShareRankingCode | Not a component record in this worksheet |
| src-000081 | parent | C4329 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000081 | field-type | E4330 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E4331 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E4332 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E4333 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E4334 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E4335 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000081 | field-type | E4336 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000081 | field-type | E4337 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000081 | field-type | E4338 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000081 | field-type | E4339 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000081 | field-type | E4340 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E4341 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000081 | field-type | E4342 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E4343 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000081 | field-type | E4344 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000081 | field-type | E4345 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E4346 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E4347 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000081 | field-type | E4348 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000081 | field-type | E4349 | ShareRankingCode | Not a component record in this worksheet |
| src-000097 | parent | C4329 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000097 | field-type | E4330 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E4331 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E4332 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E4333 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E4334 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E4335 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000097 | field-type | E4336 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000097 | field-type | E4337 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000097 | field-type | E4338 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000097 | field-type | E4339 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000097 | field-type | E4340 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E4341 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000097 | field-type | E4342 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E4343 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000097 | field-type | E4344 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000097 | field-type | E4345 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E4346 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E4347 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000097 | field-type | E4348 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000097 | field-type | E4349 | ShareRankingCode | Not a component record in this worksheet |
| src-000164 | parent | C4329 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000164 | field-type | E4330 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E4331 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E4332 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E4333 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E4334 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E4335 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000164 | field-type | E4336 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000164 | field-type | E4337 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000164 | field-type | E4338 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000164 | field-type | E4339 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000164 | field-type | E4340 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E4341 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000164 | field-type | E4342 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E4343 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000164 | field-type | E4344 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000164 | field-type | E4345 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E4346 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E4347 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000164 | field-type | E4348 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000164 | field-type | E4349 | ShareRankingCode | Not a component record in this worksheet |
| src-000175 | parent | C4329 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000175 | field-type | E4330 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E4331 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E4332 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E4333 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E4334 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E4335 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000175 | field-type | E4336 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000175 | field-type | E4337 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000175 | field-type | E4338 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000175 | field-type | E4339 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000175 | field-type | E4340 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E4341 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000175 | field-type | E4342 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E4343 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000175 | field-type | E4344 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000175 | field-type | E4345 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E4346 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E4347 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000175 | field-type | E4348 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000175 | field-type | E4349 | ShareRankingCode | Not a component record in this worksheet |
| src-000182 | parent | C4259 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000182 | field-type | E4260 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E4261 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E4262 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E4263 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E4264 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E4265 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000182 | field-type | E4266 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000182 | field-type | E4267 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000182 | field-type | E4268 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000182 | field-type | E4269 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000182 | field-type | E4270 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E4271 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E4272 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E4273 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000182 | field-type | E4274 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000182 | field-type | E4275 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E4276 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E4277 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000182 | field-type | E4278 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000182 | field-type | E4279 | ShareRankingCode | Not a component record in this worksheet |
| src-000198 | parent | C4329 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000198 | field-type | E4330 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E4331 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E4332 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E4333 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E4334 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E4335 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000198 | field-type | E4336 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000198 | field-type | E4337 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000198 | field-type | E4338 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000198 | field-type | E4339 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000198 | field-type | E4340 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E4341 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000198 | field-type | E4342 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E4343 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000198 | field-type | E4344 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000198 | field-type | E4345 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E4346 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E4347 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000198 | field-type | E4348 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000198 | field-type | E4349 | ShareRankingCode | Not a component record in this worksheet |
| src-000322 | parent | C4298 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000322 | field-type | E4299 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E4300 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E4301 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E4302 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E4303 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E4304 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000322 | field-type | E4305 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000322 | field-type | E4306 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000322 | field-type | E4307 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000322 | field-type | E4308 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000322 | field-type | E4309 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E4310 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000322 | field-type | E4311 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E4312 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000322 | field-type | E4313 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000322 | field-type | E4314 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E4315 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E4316 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000322 | field-type | E4317 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000322 | field-type | E4318 | ShareRankingCode | Not a component record in this worksheet |
| src-000345 | parent | C2721 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000345 | field-type | E2722 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000345 | field-type | E2723 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000345 | field-type | E2724 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000345 | field-type | E2725 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000345 | field-type | E2726 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000345 | field-type | E2727 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000345 | field-type | E2728 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000345 | field-type | E2729 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000345 | field-type | E2730 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000345 | field-type | E2731 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000345 | field-type | E2732 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E2733 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E2734 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000345 | field-type | E2735 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000345 | field-type | E2736 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000345 | field-type | E2737 | PercentageRate | Not a component record in this worksheet |
| src-000345 | field-type | E2738 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E2739 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000345 | field-type | E2740 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000345 | field-type | E2741 | ShareRankingCode | Not a component record in this worksheet |
| src-000348 | parent | C4298 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000348 | field-type | E4299 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E4300 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E4301 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E4302 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E4303 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E4304 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000348 | field-type | E4305 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000348 | field-type | E4306 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000348 | field-type | E4307 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000348 | field-type | E4308 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000348 | field-type | E4309 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E4310 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000348 | field-type | E4311 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E4312 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000348 | field-type | E4313 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000348 | field-type | E4314 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E4315 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E4316 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000348 | field-type | E4317 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000348 | field-type | E4318 | ShareRankingCode | Not a component record in this worksheet |
| src-000352 | parent | C4329 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000352 | field-type | E4330 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E4331 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E4332 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E4333 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E4334 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E4335 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000352 | field-type | E4336 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000352 | field-type | E4337 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000352 | field-type | E4338 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000352 | field-type | E4339 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000352 | field-type | E4340 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E4341 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000352 | field-type | E4342 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E4343 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000352 | field-type | E4344 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000352 | field-type | E4345 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E4346 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E4347 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000352 | field-type | E4348 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000352 | field-type | E4349 | ShareRankingCode | Not a component record in this worksheet |
| src-000355 | parent | C4237 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000355 | field-type | E4238 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E4239 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E4240 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E4241 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E4242 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E4243 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000355 | field-type | E4244 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000355 | field-type | E4245 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000355 | field-type | E4246 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000355 | field-type | E4247 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000355 | field-type | E4248 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E4249 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E4250 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E4251 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000355 | field-type | E4252 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000355 | field-type | E4253 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E4254 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E4255 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000355 | field-type | E4256 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000355 | field-type | E4257 | ShareRankingCode | Not a component record in this worksheet |
| src-000358 | parent | C2721 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000358 | field-type | E2722 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000358 | field-type | E2723 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000358 | field-type | E2724 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000358 | field-type | E2725 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000358 | field-type | E2726 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000358 | field-type | E2727 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000358 | field-type | E2728 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000358 | field-type | E2729 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000358 | field-type | E2730 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000358 | field-type | E2731 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000358 | field-type | E2732 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E2733 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E2734 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000358 | field-type | E2735 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000358 | field-type | E2736 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000358 | field-type | E2737 | PercentageRate | Not a component record in this worksheet |
| src-000358 | field-type | E2738 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E2739 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000358 | field-type | E2740 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000358 | field-type | E2741 | ShareRankingCode | Not a component record in this worksheet |
| src-000361 | parent | C2721 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000361 | field-type | E2722 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000361 | field-type | E2723 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000361 | field-type | E2724 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000361 | field-type | E2725 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000361 | field-type | E2726 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000361 | field-type | E2727 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000361 | field-type | E2728 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000361 | field-type | E2729 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000361 | field-type | E2730 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000361 | field-type | E2731 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000361 | field-type | E2732 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E2733 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E2734 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000361 | field-type | E2735 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000361 | field-type | E2736 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000361 | field-type | E2737 | PercentageRate | Not a component record in this worksheet |
| src-000361 | field-type | E2738 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E2739 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000361 | field-type | E2740 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000361 | field-type | E2741 | ShareRankingCode | Not a component record in this worksheet |
| src-000364 | parent | C4237 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000364 | field-type | E4238 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000364 | field-type | E4239 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000364 | field-type | E4240 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000364 | field-type | E4241 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000364 | field-type | E4242 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000364 | field-type | E4243 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000364 | field-type | E4244 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000364 | field-type | E4245 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000364 | field-type | E4246 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000364 | field-type | E4247 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000364 | field-type | E4248 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E4249 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E4250 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000364 | field-type | E4251 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000364 | field-type | E4252 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000364 | field-type | E4253 | PercentageRate | Not a component record in this worksheet |
| src-000364 | field-type | E4254 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E4255 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000364 | field-type | E4256 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000364 | field-type | E4257 | ShareRankingCode | Not a component record in this worksheet |
| src-000367 | parent | C4237 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000367 | field-type | E4238 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E4239 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E4240 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E4241 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E4242 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E4243 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000367 | field-type | E4244 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000367 | field-type | E4245 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000367 | field-type | E4246 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000367 | field-type | E4247 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000367 | field-type | E4248 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E4249 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E4250 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E4251 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000367 | field-type | E4252 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000367 | field-type | E4253 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E4254 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E4255 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000367 | field-type | E4256 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000367 | field-type | E4257 | ShareRankingCode | Not a component record in this worksheet |
| src-000370 | parent | C2721 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000370 | field-type | E2722 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000370 | field-type | E2723 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000370 | field-type | E2724 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000370 | field-type | E2725 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000370 | field-type | E2726 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000370 | field-type | E2727 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000370 | field-type | E2728 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000370 | field-type | E2729 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000370 | field-type | E2730 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000370 | field-type | E2731 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000370 | field-type | E2732 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E2733 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E2734 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000370 | field-type | E2735 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000370 | field-type | E2736 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000370 | field-type | E2737 | PercentageRate | Not a component record in this worksheet |
| src-000370 | field-type | E2738 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E2739 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000370 | field-type | E2740 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000370 | field-type | E2741 | ShareRankingCode | Not a component record in this worksheet |
| src-000373 | parent | C2721 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000373 | field-type | E2722 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000373 | field-type | E2723 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000373 | field-type | E2724 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000373 | field-type | E2725 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000373 | field-type | E2726 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000373 | field-type | E2727 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000373 | field-type | E2728 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000373 | field-type | E2729 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000373 | field-type | E2730 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000373 | field-type | E2731 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000373 | field-type | E2732 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E2733 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E2734 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000373 | field-type | E2735 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000373 | field-type | E2736 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000373 | field-type | E2737 | PercentageRate | Not a component record in this worksheet |
| src-000373 | field-type | E2738 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E2739 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000373 | field-type | E2740 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000373 | field-type | E2741 | ShareRankingCode | Not a component record in this worksheet |
| src-000376 | parent | C4329 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000376 | field-type | E4330 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E4331 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E4332 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E4333 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E4334 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E4335 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000376 | field-type | E4336 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000376 | field-type | E4337 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000376 | field-type | E4338 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000376 | field-type | E4339 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000376 | field-type | E4340 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E4341 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000376 | field-type | E4342 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E4343 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000376 | field-type | E4344 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000376 | field-type | E4345 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E4346 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E4347 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000376 | field-type | E4348 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000376 | field-type | E4349 | ShareRankingCode | Not a component record in this worksheet |
| src-000379 | parent | C2721 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000379 | field-type | E2722 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000379 | field-type | E2723 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000379 | field-type | E2724 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000379 | field-type | E2725 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000379 | field-type | E2726 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000379 | field-type | E2727 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000379 | field-type | E2728 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000379 | field-type | E2729 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000379 | field-type | E2730 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000379 | field-type | E2731 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000379 | field-type | E2732 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E2733 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E2734 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000379 | field-type | E2735 | SecuritiesQuantity | [SecuritiesQuantity](<bc-8cbba10ca914faa6cd02.md>) |
| src-000379 | field-type | E2736 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000379 | field-type | E2737 | PercentageRate | Not a component record in this worksheet |
| src-000379 | field-type | E2738 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E2739 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000379 | field-type | E2740 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000379 | field-type | E2741 | ShareRankingCode | Not a component record in this worksheet |
| src-000382 | parent | C4298 | ProceedsDefinition | [ProceedsDefinition](<bc-0d37063b05a28beafae9.md>) |
| src-000382 | field-type | E4299 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E4300 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E4301 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E4302 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E4303 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E4304 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000382 | field-type | E4305 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000382 | field-type | E4306 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000382 | field-type | E4307 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000382 | field-type | E4308 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000382 | field-type | E4309 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E4310 | IntermediateSecurityDistributionTypeCode | Not a component record in this worksheet |
| src-000382 | field-type | E4311 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E4312 | SecuritiesQuantity | [SecuritiesQuantity](<bc-eb3fa0c6a18cb359935a.md>) |
| src-000382 | field-type | E4313 | QuantityRatio | [QuantityRatio](<bc-8234b2b7721d738c5f07.md>) |
| src-000382 | field-type | E4314 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E4315 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E4316 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000382 | field-type | E4317 | DateTimePeriod | [DateTimePeriod](<bc-420f6b7b61cb1a61affe.md>) |
| src-000382 | field-type | E4318 | ShareRankingCode | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
