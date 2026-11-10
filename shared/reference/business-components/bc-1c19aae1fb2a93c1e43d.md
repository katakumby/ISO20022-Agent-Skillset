---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-1c19aae1fb2a93c1e43d"
title: "ExposureCalculation"
business_component_name: "ExposureCalculation"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A1871:F1882"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A1836:F1847"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A1871:F1882"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A1871:F1882"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A1871:F1882"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A1871:F1882"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A1871:F1882"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A1836:F1847"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A1871:F1882"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A1849:F1860"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A4396:F4407"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A1849:F1860"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A1871:F1882"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A1825:F1836"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A4396:F4407"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A4396:F4407"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A1825:F1836"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A1825:F1836"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A4396:F4407"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A4396:F4407"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A1871:F1882"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A4396:F4407"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A1849:F1860"]}]
content_sha256: "1c19aae1fb2a93c1e43d7c9c8b906763b375603e83820387ac5eee14151bbbbc"
parent_names: []
related_component_names: ["CollateralBalance", "CollateralManagement", "CounterpartyRisk", "CurrencyAndAmount", "IndependentAmount", "MarginAmountRequirement", "TransactionRisk"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# ExposureCalculation

## Definition

Description of the calculation of the amounts representing the risk that needs to be covered, together with the calculation of the existing coverage.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ExposureCalculation | ∅ | ∅ | Description of the calculation of the amounts representing the risk that needs to be covered, together with the calculation of the existing coverage. | ∅ | ∅ |
| 2 | ExposureCalculation | TotalCollateralCurrentValue | ∅ | Total value of the collateral derived from the sum of the current independent amounts and variation margins held, agreed and in transit. | CurrencyAndAmount | ∅ |
| 3 | ExposureCalculation | TotalExposedAmount | ∅ | The sum of the exposures of all transactions which are in favour of a Party. That is, all transactions which would have an amount payable by the counterparty if they were being terminated. | CurrencyAndAmount | ∅ |
| 4 | ExposureCalculation | CurrentIndependentAmount | ∅ | Amount applied as an add-on to the exposure usually intended to cover a possible increase in exposure before the next valuation date. | IndependentAmount | RelatedRiskCalculation |
| 5 | ExposureCalculation | CurrentVariationMargin | ∅ | Provides details about the collateral held, in transit or that still needs to be agreed by both parties, against the variation margin. | CollateralBalance | VariationMarginRelatedRiskCalculation |
| 6 | ExposureCalculation | CurrentSegregatedIndependentAmount | ∅ | Provides details about the collateral held, in transit or that still needs to be agreed by both parties, against the segregated independent amount only. | CollateralBalance | SegregatedIndependentAmountRelatedRiskCalculation |
| 7 | ExposureCalculation | VariationMarginAmountRequirement | ∅ | Amount of expected margin required by any of the parties of the margin calculation. | MarginAmountRequirement | VariationMarginAmountRequirementCalculation |
| 8 | ExposureCalculation | SegregatedAmountRequirement | ∅ | Margin requirements for the segregated independent amount. | MarginAmountRequirement | SegregatedAmountRequirementCalculation |
| 9 | ExposureCalculation | CollateralManagement | ∅ | Specifies the collateral management actions resulting from the calculation of the risk. | CollateralManagement | RiskToCover |
| 10 | ExposureCalculation | CounterpartyRisk | ∅ | Calculation of the exposure amount that one party has vis-a-vis one counterparty or a central system, based on its credit risk. | CounterpartyRisk | ExposureCalculation |
| 11 | ExposureCalculation | TransactionRisk | ∅ | Calculation of the exposure amount that one party has vis-a-vis one counterparty or a central system, based on the transactions that are not yet settled. | TransactionRisk | ExposureCalculation |
| 12 | ExposureCalculation | TotalCollateralAfterHaircut | ∅ | Collateral currently received (+)/delivered (-) in the base currency. This amount is after the haircut has been applied. | CurrencyAndAmount | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `1c19aae1fb2a93c1e43d7c9c8b906763b375603e83820387ac5eee14151bbbbc`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A1871:F1882 | 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882 | [src-000006 original](<../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart3_BanktoCustomerCashManagement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md>) |
| src-000016 | FullBusinessModel!A1836:F1847 | 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000054 | FullBusinessModel!A1871:F1882 | 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882 | [src-000054 original](<../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart3_CentralCounterParty_SecuritiesClearing_Maintenance_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md>) |
| src-000081 | FullBusinessModel!A1871:F1882 | 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882 | [src-000081 original](<../../../raw-input/corporate_actions/ISO20022_MDRPart3_CorporateActions_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md>) |
| src-000097 | FullBusinessModel!A1871:F1882 | 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882 | [src-000097 original](<../../../raw-input/investment_funds/ISO20022_MDRPart3_Investment-Funds_2025_2026_v2.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md>) |
| src-000164 | FullBusinessModel!A1871:F1882 | 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882 | [src-000164 original](<../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart3_PaymentsClearingandSettlement_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md>) |
| src-000175 | FullBusinessModel!A1871:F1882 | 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882 | [src-000175 original](<../../../raw-input/payments_initiation/ISO20022_MDRPart3_PaymentsInitiation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md>) |
| src-000182 | FullBusinessModel!A1836:F1847 | 1836, 1837, 1838, 1839, 1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000198 | FullBusinessModel!A1871:F1882 | 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882 | [src-000198 original](<../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart3_SettlementAndReconciliation_2025_2026_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md>) |
| src-000322 | FullBusinessModel!A1849:F1860 | 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860 | [src-000322 original](<../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart3_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md>) |
| src-000345 | FullBusinessModel!A4396:F4407 | 4396, 4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000348 | FullBusinessModel!A1849:F1860 | 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860 | [src-000348 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md>) |
| src-000352 | FullBusinessModel!A1871:F1882 | 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882 | [src-000352 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md>) |
| src-000355 | FullBusinessModel!A1825:F1836 | 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A4396:F4407 | 4396, 4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A4396:F4407 | 4396, 4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A1825:F1836 | 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A1825:F1836 | 1825, 1826, 1827, 1828, 1829, 1830, 1831, 1832, 1833, 1834, 1835, 1836 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A4396:F4407 | 4396, 4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A4396:F4407 | 4396, 4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000376 | FullBusinessModel!A1871:F1882 | 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879, 1880, 1881, 1882 | [src-000376 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md>) |
| src-000379 | FullBusinessModel!A4396:F4407 | 4396, 4397, 4398, 4399, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |
| src-000382 | FullBusinessModel!A1849:F1860 | 1849, 1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859, 1860 | [src-000382 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E1872 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E1873 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E1874 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000006 | field-type | E1875 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000006 | field-type | E1876 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000006 | field-type | E1877 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000006 | field-type | E1878 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000006 | field-type | E1879 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000006 | field-type | E1880 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000006 | field-type | E1881 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000006 | field-type | E1882 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E1837 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E1838 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E1839 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000016 | field-type | E1840 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000016 | field-type | E1841 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000016 | field-type | E1842 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000016 | field-type | E1843 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000016 | field-type | E1844 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000016 | field-type | E1845 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000016 | field-type | E1846 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000016 | field-type | E1847 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E1872 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E1873 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E1874 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000054 | field-type | E1875 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000054 | field-type | E1876 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000054 | field-type | E1877 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000054 | field-type | E1878 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000054 | field-type | E1879 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000054 | field-type | E1880 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000054 | field-type | E1881 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000054 | field-type | E1882 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E1872 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E1873 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E1874 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000081 | field-type | E1875 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000081 | field-type | E1876 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000081 | field-type | E1877 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000081 | field-type | E1878 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000081 | field-type | E1879 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000081 | field-type | E1880 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000081 | field-type | E1881 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000081 | field-type | E1882 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E1872 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E1873 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E1874 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000097 | field-type | E1875 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000097 | field-type | E1876 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000097 | field-type | E1877 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000097 | field-type | E1878 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000097 | field-type | E1879 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000097 | field-type | E1880 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000097 | field-type | E1881 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000097 | field-type | E1882 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E1872 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E1873 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E1874 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000164 | field-type | E1875 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000164 | field-type | E1876 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000164 | field-type | E1877 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000164 | field-type | E1878 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000164 | field-type | E1879 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000164 | field-type | E1880 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000164 | field-type | E1881 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000164 | field-type | E1882 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E1872 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E1873 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E1874 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000175 | field-type | E1875 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000175 | field-type | E1876 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000175 | field-type | E1877 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000175 | field-type | E1878 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000175 | field-type | E1879 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000175 | field-type | E1880 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000175 | field-type | E1881 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000175 | field-type | E1882 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E1837 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E1838 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E1839 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000182 | field-type | E1840 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000182 | field-type | E1841 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000182 | field-type | E1842 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000182 | field-type | E1843 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000182 | field-type | E1844 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000182 | field-type | E1845 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000182 | field-type | E1846 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000182 | field-type | E1847 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E1872 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E1873 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E1874 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000198 | field-type | E1875 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000198 | field-type | E1876 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000198 | field-type | E1877 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000198 | field-type | E1878 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000198 | field-type | E1879 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000198 | field-type | E1880 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000198 | field-type | E1881 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000198 | field-type | E1882 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E1850 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E1851 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E1852 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000322 | field-type | E1853 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000322 | field-type | E1854 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000322 | field-type | E1855 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000322 | field-type | E1856 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000322 | field-type | E1857 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000322 | field-type | E1858 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000322 | field-type | E1859 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000322 | field-type | E1860 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E4397 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E4398 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E4399 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000345 | field-type | E4400 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000345 | field-type | E4401 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000345 | field-type | E4402 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000345 | field-type | E4403 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000345 | field-type | E4404 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000345 | field-type | E4405 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000345 | field-type | E4406 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000345 | field-type | E4407 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E1850 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E1851 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E1852 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000348 | field-type | E1853 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000348 | field-type | E1854 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000348 | field-type | E1855 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000348 | field-type | E1856 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000348 | field-type | E1857 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000348 | field-type | E1858 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000348 | field-type | E1859 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000348 | field-type | E1860 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E1872 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E1873 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E1874 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000352 | field-type | E1875 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000352 | field-type | E1876 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000352 | field-type | E1877 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000352 | field-type | E1878 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000352 | field-type | E1879 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000352 | field-type | E1880 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000352 | field-type | E1881 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000352 | field-type | E1882 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E1826 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E1827 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E1828 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000355 | field-type | E1829 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000355 | field-type | E1830 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000355 | field-type | E1831 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000355 | field-type | E1832 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000355 | field-type | E1833 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000355 | field-type | E1834 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000355 | field-type | E1835 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000355 | field-type | E1836 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E4397 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E4398 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E4399 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000358 | field-type | E4400 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000358 | field-type | E4401 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000358 | field-type | E4402 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000358 | field-type | E4403 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000358 | field-type | E4404 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000358 | field-type | E4405 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000358 | field-type | E4406 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000358 | field-type | E4407 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E4397 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E4398 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E4399 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000361 | field-type | E4400 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000361 | field-type | E4401 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000361 | field-type | E4402 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000361 | field-type | E4403 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000361 | field-type | E4404 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000361 | field-type | E4405 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000361 | field-type | E4406 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000361 | field-type | E4407 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E1826 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E1827 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E1828 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000364 | field-type | E1829 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000364 | field-type | E1830 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000364 | field-type | E1831 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000364 | field-type | E1832 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000364 | field-type | E1833 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000364 | field-type | E1834 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000364 | field-type | E1835 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000364 | field-type | E1836 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E1826 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E1827 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E1828 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000367 | field-type | E1829 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000367 | field-type | E1830 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000367 | field-type | E1831 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000367 | field-type | E1832 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000367 | field-type | E1833 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000367 | field-type | E1834 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000367 | field-type | E1835 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000367 | field-type | E1836 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E4397 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E4398 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E4399 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000370 | field-type | E4400 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000370 | field-type | E4401 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000370 | field-type | E4402 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000370 | field-type | E4403 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000370 | field-type | E4404 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000370 | field-type | E4405 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000370 | field-type | E4406 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000370 | field-type | E4407 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E4397 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E4398 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E4399 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000373 | field-type | E4400 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000373 | field-type | E4401 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000373 | field-type | E4402 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000373 | field-type | E4403 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000373 | field-type | E4404 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000373 | field-type | E4405 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000373 | field-type | E4406 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000373 | field-type | E4407 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E1872 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E1873 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E1874 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000376 | field-type | E1875 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000376 | field-type | E1876 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000376 | field-type | E1877 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000376 | field-type | E1878 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000376 | field-type | E1879 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000376 | field-type | E1880 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000376 | field-type | E1881 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000376 | field-type | E1882 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E4397 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E4398 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E4399 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000379 | field-type | E4400 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000379 | field-type | E4401 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000379 | field-type | E4402 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000379 | field-type | E4403 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000379 | field-type | E4404 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000379 | field-type | E4405 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000379 | field-type | E4406 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000379 | field-type | E4407 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E1850 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E1851 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E1852 | IndependentAmount | [IndependentAmount](<bc-066b8c6fc1242e183799.md>) |
| src-000382 | field-type | E1853 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000382 | field-type | E1854 | CollateralBalance | [CollateralBalance](<bc-a95e63c10dbbd2279e8b.md>) |
| src-000382 | field-type | E1855 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000382 | field-type | E1856 | MarginAmountRequirement | [MarginAmountRequirement](<bc-059a25b2d2150170700b.md>) |
| src-000382 | field-type | E1857 | CollateralManagement | [CollateralManagement](<bc-8e354388788dacd125dc.md>) |
| src-000382 | field-type | E1858 | CounterpartyRisk | [CounterpartyRisk](<bc-ae7a272e414a169621a3.md>) |
| src-000382 | field-type | E1859 | TransactionRisk | [TransactionRisk](<bc-55c0c1a7a5148615ebb4.md>) |
| src-000382 | field-type | E1860 | CurrencyAndAmount | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
