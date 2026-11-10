---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-b0ebfc4418fb9fb1bce3"
title: "NetAssetValueCalculation"
business_component_name: "NetAssetValueCalculation"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A2846:F2867"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A2810:F2831"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A2846:F2867"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A2846:F2867"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A2846:F2867"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A2846:F2867"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A2846:F2867"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A2810:F2831"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A2846:F2867"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A2823:F2844"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A288:F309"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A2823:F2844"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A2846:F2867"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A2798:F2819"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A288:F309"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A288:F309"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A2798:F2819"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A2798:F2819"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A288:F309"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A288:F309"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A2846:F2867"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A288:F309"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A2823:F2844"]}]
content_sha256: "b0ebfc4418fb9fb1bce32a4b19a4704e12b2a65804d83eb79cef7ff9376a6beb"
parent_names: []
related_component_names: ["CurrencyAndAmount", "EventFrequencyCode", "FundsCashFlow", "ISODate", "ISODateTime", "Interest", "InvestmentFundClass", "Max35Text", "PerformanceFactors", "SecuritiesPricing", "SecuritiesQuantity", "Tax", "ValuationStatistics", "ValuationTimingCode", "YesNoIndicator"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# NetAssetValueCalculation

## Definition

Calculation of the net asset value for an investment fund/fund class.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | NetAssetValueCalculation | ∅ | ∅ | Calculation of the net asset value for an investment fund/fund class. | ∅ | ∅ |
| 2 | NetAssetValueCalculation | ValuationFrequency | ∅ | Frequency of the valuation. | EventFrequencyCode | ∅ |
| 3 | NetAssetValueCalculation | ValuationDateTime | ∅ | Date and time of the price valuation for the investment fund/fund class. | ISODateTime | ∅ |
| 4 | NetAssetValueCalculation | NetAssetValue | ∅ | Value of all the holdings, less the fund's liabilities, attributable to a specific investment fund class. | CurrencyAndAmount | ∅ |
| 5 | NetAssetValueCalculation | RelatedFund | ∅ | Specifies the fund for which the NAV is calculated (per fund unit). | InvestmentFundClass | NetAssetValueCalculation |
| 6 | NetAssetValueCalculation | ValuationType | ∅ | Specifies how the valuation is done, based on the schedule stated in the prospectus. | ValuationTimingCode | ∅ |
| 7 | NetAssetValueCalculation | SuspendedIndicator | ∅ | Indicates whether the valuation of the investment fund class is suspended. | YesNoIndicator | ∅ |
| 8 | NetAssetValueCalculation | ForExecutionIndicator | ∅ | Indicates whether the price information can be used for the execution of a transaction. | YesNoIndicator | ∅ |
| 9 | NetAssetValueCalculation | TaxLiability | ∅ | Information related to taxes that are due. | Tax | TaxLiabilityValueCalculation |
| 10 | NetAssetValueCalculation | TaxRefund | ∅ | Information related to taxes that are paid back. | Tax | TaxRefundValueCalculation |
| 11 | NetAssetValueCalculation | OfficialValuationIndicator | ∅ | Indicates whether the valuation is an official valuation. | YesNoIndicator | ∅ |
| 12 | NetAssetValueCalculation | EstimatedPriceIndicator | ∅ | Indicates whether the price is an estimated price. | YesNoIndicator | ∅ |
| 13 | NetAssetValueCalculation | ValuationStatistics | ∅ | Information related to the price variations of an investment fund class. | ValuationStatistics | NetAssetValueCalculation |
| 14 | NetAssetValueCalculation | InvestmentFundPerformanceFactors | ∅ | Factors that give indications about the performance of a fund. | PerformanceFactors | NetAssetValueCalculation |
| 15 | NetAssetValueCalculation | Price | ∅ | Price derived from the net asset value. | SecuritiesPricing | NetAssetValueCalculation |
| 16 | NetAssetValueCalculation | SecuritiesQuantity | ∅ | Quantity on which the NAV is calculated. | SecuritiesQuantity | NetAssetValueCalculation |
| 17 | NetAssetValueCalculation | Interest | ∅ | Interest that has accumulated between the most recent payment of interest and the sale of the financial instrument. | Interest | RelatedNetAssetValueCalculation |
| 18 | NetAssetValueCalculation | FundsCashFlow | ∅ | Net cash flow for a valuation date, which is incorporated in the NAV. | FundsCashFlow | NetAssetValueCalculation |
| 19 | NetAssetValueCalculation | DeclarationChannel | ∅ | Means of the net asset value publication, for example, a newspaper. | Max35Text | ∅ |
| 20 | NetAssetValueCalculation | DeclarationDate | ∅ | Date/time of the net asset value publication. | ISODateTime | ∅ |
| 21 | NetAssetValueCalculation | FirstValuationDate | ∅ | Date on which the investment fund class was first priced. | ISODate | ∅ |
| 22 | NetAssetValueCalculation | HistoricPricingIndicator | ∅ | Indicates whether the price is historic or forward. | YesNoIndicator | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `b0ebfc4418fb9fb1bce32a4b19a4704e12b2a65804d83eb79cef7ff9376a6beb`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A2846:F2867 | 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A2810:F2831 | 2810, 2811, 2812, 2813, 2814, 2815, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A2846:F2867 | 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A2846:F2867 | 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A2846:F2867 | 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A2846:F2867 | 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A2846:F2867 | 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A2810:F2831 | 2810, 2811, 2812, 2813, 2814, 2815, 2816, 2817, 2818, 2819, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A2846:F2867 | 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A2823:F2844 | 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840, 2841, 2842, 2843, 2844 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A288:F309 | 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A2823:F2844 | 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840, 2841, 2842, 2843, 2844 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A2846:F2867 | 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A2798:F2819 | 2798, 2799, 2800, 2801, 2802, 2803, 2804, 2805, 2806, 2807, 2808, 2809, 2810, 2811, 2812, 2813, 2814, 2815, 2816, 2817, 2818, 2819 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A288:F309 | 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A288:F309 | 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A2798:F2819 | 2798, 2799, 2800, 2801, 2802, 2803, 2804, 2805, 2806, 2807, 2808, 2809, 2810, 2811, 2812, 2813, 2814, 2815, 2816, 2817, 2818, 2819 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A2798:F2819 | 2798, 2799, 2800, 2801, 2802, 2803, 2804, 2805, 2806, 2807, 2808, 2809, 2810, 2811, 2812, 2813, 2814, 2815, 2816, 2817, 2818, 2819 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A288:F309 | 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A288:F309 | 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A2846:F2867 | 2846, 2847, 2848, 2849, 2850, 2851, 2852, 2853, 2854, 2855, 2856, 2857, 2858, 2859, 2860, 2861, 2862, 2863, 2864, 2865, 2866, 2867 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A288:F309 | 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A2823:F2844 | 2823, 2824, 2825, 2826, 2827, 2828, 2829, 2830, 2831, 2832, 2833, 2834, 2835, 2836, 2837, 2838, 2839, 2840, 2841, 2842, 2843, 2844 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E2847 | EventFrequencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E2848 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E2849 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E2850 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000006 | field-type | E2851 | ValuationTimingCode | Not a component record in this worksheet |
| src-000006 | field-type | E2852 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E2853 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E2854 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000006 | field-type | E2855 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000006 | field-type | E2856 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E2857 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E2858 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000006 | field-type | E2859 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000006 | field-type | E2860 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000006 | field-type | E2861 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000006 | field-type | E2862 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000006 | field-type | E2863 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000006 | field-type | E2864 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E2865 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E2866 | ISODate | Not a component record in this worksheet |
| src-000006 | field-type | E2867 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E2811 | EventFrequencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E2812 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E2813 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E2814 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000016 | field-type | E2815 | ValuationTimingCode | Not a component record in this worksheet |
| src-000016 | field-type | E2816 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E2817 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E2818 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000016 | field-type | E2819 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000016 | field-type | E2820 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E2821 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E2822 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000016 | field-type | E2823 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000016 | field-type | E2824 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000016 | field-type | E2825 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000016 | field-type | E2826 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000016 | field-type | E2827 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000016 | field-type | E2828 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E2829 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E2830 | ISODate | Not a component record in this worksheet |
| src-000016 | field-type | E2831 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E2847 | EventFrequencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E2848 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E2849 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E2850 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000054 | field-type | E2851 | ValuationTimingCode | Not a component record in this worksheet |
| src-000054 | field-type | E2852 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E2853 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E2854 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000054 | field-type | E2855 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000054 | field-type | E2856 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E2857 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E2858 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000054 | field-type | E2859 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000054 | field-type | E2860 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000054 | field-type | E2861 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000054 | field-type | E2862 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000054 | field-type | E2863 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000054 | field-type | E2864 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E2865 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E2866 | ISODate | Not a component record in this worksheet |
| src-000054 | field-type | E2867 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E2847 | EventFrequencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E2848 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E2849 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E2850 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000081 | field-type | E2851 | ValuationTimingCode | Not a component record in this worksheet |
| src-000081 | field-type | E2852 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E2853 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E2854 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000081 | field-type | E2855 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000081 | field-type | E2856 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E2857 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E2858 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000081 | field-type | E2859 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000081 | field-type | E2860 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000081 | field-type | E2861 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000081 | field-type | E2862 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000081 | field-type | E2863 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000081 | field-type | E2864 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E2865 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E2866 | ISODate | Not a component record in this worksheet |
| src-000081 | field-type | E2867 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E2847 | EventFrequencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E2848 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E2849 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E2850 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000097 | field-type | E2851 | ValuationTimingCode | Not a component record in this worksheet |
| src-000097 | field-type | E2852 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E2853 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E2854 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000097 | field-type | E2855 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000097 | field-type | E2856 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E2857 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E2858 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000097 | field-type | E2859 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000097 | field-type | E2860 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000097 | field-type | E2861 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000097 | field-type | E2862 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000097 | field-type | E2863 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000097 | field-type | E2864 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E2865 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E2866 | ISODate | Not a component record in this worksheet |
| src-000097 | field-type | E2867 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E2847 | EventFrequencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E2848 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E2849 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E2850 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000164 | field-type | E2851 | ValuationTimingCode | Not a component record in this worksheet |
| src-000164 | field-type | E2852 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E2853 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E2854 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000164 | field-type | E2855 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000164 | field-type | E2856 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E2857 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E2858 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000164 | field-type | E2859 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000164 | field-type | E2860 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000164 | field-type | E2861 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000164 | field-type | E2862 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000164 | field-type | E2863 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000164 | field-type | E2864 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E2865 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E2866 | ISODate | Not a component record in this worksheet |
| src-000164 | field-type | E2867 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E2847 | EventFrequencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E2848 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E2849 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E2850 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000175 | field-type | E2851 | ValuationTimingCode | Not a component record in this worksheet |
| src-000175 | field-type | E2852 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E2853 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E2854 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000175 | field-type | E2855 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000175 | field-type | E2856 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E2857 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E2858 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000175 | field-type | E2859 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000175 | field-type | E2860 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000175 | field-type | E2861 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000175 | field-type | E2862 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000175 | field-type | E2863 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000175 | field-type | E2864 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E2865 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E2866 | ISODate | Not a component record in this worksheet |
| src-000175 | field-type | E2867 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E2811 | EventFrequencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E2812 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E2813 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E2814 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000182 | field-type | E2815 | ValuationTimingCode | Not a component record in this worksheet |
| src-000182 | field-type | E2816 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E2817 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E2818 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000182 | field-type | E2819 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000182 | field-type | E2820 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E2821 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E2822 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000182 | field-type | E2823 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000182 | field-type | E2824 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000182 | field-type | E2825 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000182 | field-type | E2826 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000182 | field-type | E2827 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000182 | field-type | E2828 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E2829 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E2830 | ISODate | Not a component record in this worksheet |
| src-000182 | field-type | E2831 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E2847 | EventFrequencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E2848 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E2849 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E2850 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000198 | field-type | E2851 | ValuationTimingCode | Not a component record in this worksheet |
| src-000198 | field-type | E2852 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E2853 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E2854 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000198 | field-type | E2855 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000198 | field-type | E2856 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E2857 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E2858 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000198 | field-type | E2859 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000198 | field-type | E2860 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000198 | field-type | E2861 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000198 | field-type | E2862 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000198 | field-type | E2863 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000198 | field-type | E2864 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E2865 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E2866 | ISODate | Not a component record in this worksheet |
| src-000198 | field-type | E2867 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E2824 | EventFrequencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E2825 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E2826 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E2827 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000322 | field-type | E2828 | ValuationTimingCode | Not a component record in this worksheet |
| src-000322 | field-type | E2829 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E2830 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E2831 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000322 | field-type | E2832 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000322 | field-type | E2833 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E2834 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E2835 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000322 | field-type | E2836 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000322 | field-type | E2837 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000322 | field-type | E2838 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000322 | field-type | E2839 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000322 | field-type | E2840 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000322 | field-type | E2841 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E2842 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E2843 | ISODate | Not a component record in this worksheet |
| src-000322 | field-type | E2844 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E289 | EventFrequencyCode | Not a component record in this worksheet |
| src-000345 | field-type | E290 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E291 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E292 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000345 | field-type | E293 | ValuationTimingCode | Not a component record in this worksheet |
| src-000345 | field-type | E294 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E295 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E296 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000345 | field-type | E297 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000345 | field-type | E298 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E299 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E300 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000345 | field-type | E301 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000345 | field-type | E302 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000345 | field-type | E303 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000345 | field-type | E304 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000345 | field-type | E305 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000345 | field-type | E306 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E307 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E308 | ISODate | Not a component record in this worksheet |
| src-000345 | field-type | E309 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E2824 | EventFrequencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E2825 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E2826 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E2827 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000348 | field-type | E2828 | ValuationTimingCode | Not a component record in this worksheet |
| src-000348 | field-type | E2829 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E2830 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E2831 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000348 | field-type | E2832 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000348 | field-type | E2833 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E2834 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E2835 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000348 | field-type | E2836 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000348 | field-type | E2837 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000348 | field-type | E2838 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000348 | field-type | E2839 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000348 | field-type | E2840 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000348 | field-type | E2841 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E2842 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E2843 | ISODate | Not a component record in this worksheet |
| src-000348 | field-type | E2844 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E2847 | EventFrequencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E2848 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E2849 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E2850 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000352 | field-type | E2851 | ValuationTimingCode | Not a component record in this worksheet |
| src-000352 | field-type | E2852 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E2853 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E2854 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000352 | field-type | E2855 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000352 | field-type | E2856 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E2857 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E2858 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000352 | field-type | E2859 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000352 | field-type | E2860 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000352 | field-type | E2861 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000352 | field-type | E2862 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000352 | field-type | E2863 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000352 | field-type | E2864 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E2865 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E2866 | ISODate | Not a component record in this worksheet |
| src-000352 | field-type | E2867 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E2799 | EventFrequencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E2800 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E2801 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E2802 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000355 | field-type | E2803 | ValuationTimingCode | Not a component record in this worksheet |
| src-000355 | field-type | E2804 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E2805 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E2806 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000355 | field-type | E2807 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000355 | field-type | E2808 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E2809 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E2810 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000355 | field-type | E2811 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000355 | field-type | E2812 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000355 | field-type | E2813 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000355 | field-type | E2814 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000355 | field-type | E2815 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000355 | field-type | E2816 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E2817 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E2818 | ISODate | Not a component record in this worksheet |
| src-000355 | field-type | E2819 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E289 | EventFrequencyCode | Not a component record in this worksheet |
| src-000358 | field-type | E290 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E291 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E292 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000358 | field-type | E293 | ValuationTimingCode | Not a component record in this worksheet |
| src-000358 | field-type | E294 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E295 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E296 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000358 | field-type | E297 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000358 | field-type | E298 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E299 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E300 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000358 | field-type | E301 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000358 | field-type | E302 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000358 | field-type | E303 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000358 | field-type | E304 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000358 | field-type | E305 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000358 | field-type | E306 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E307 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E308 | ISODate | Not a component record in this worksheet |
| src-000358 | field-type | E309 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E289 | EventFrequencyCode | Not a component record in this worksheet |
| src-000361 | field-type | E290 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E291 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E292 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000361 | field-type | E293 | ValuationTimingCode | Not a component record in this worksheet |
| src-000361 | field-type | E294 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E295 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E296 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000361 | field-type | E297 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000361 | field-type | E298 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E299 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E300 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000361 | field-type | E301 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000361 | field-type | E302 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000361 | field-type | E303 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000361 | field-type | E304 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000361 | field-type | E305 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000361 | field-type | E306 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E307 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E308 | ISODate | Not a component record in this worksheet |
| src-000361 | field-type | E309 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E2799 | EventFrequencyCode | Not a component record in this worksheet |
| src-000364 | field-type | E2800 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E2801 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E2802 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000364 | field-type | E2803 | ValuationTimingCode | Not a component record in this worksheet |
| src-000364 | field-type | E2804 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E2805 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E2806 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000364 | field-type | E2807 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000364 | field-type | E2808 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E2809 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E2810 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000364 | field-type | E2811 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000364 | field-type | E2812 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000364 | field-type | E2813 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000364 | field-type | E2814 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000364 | field-type | E2815 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000364 | field-type | E2816 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E2817 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E2818 | ISODate | Not a component record in this worksheet |
| src-000364 | field-type | E2819 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E2799 | EventFrequencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E2800 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E2801 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E2802 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000367 | field-type | E2803 | ValuationTimingCode | Not a component record in this worksheet |
| src-000367 | field-type | E2804 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E2805 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E2806 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000367 | field-type | E2807 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000367 | field-type | E2808 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E2809 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E2810 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000367 | field-type | E2811 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000367 | field-type | E2812 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000367 | field-type | E2813 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000367 | field-type | E2814 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000367 | field-type | E2815 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000367 | field-type | E2816 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E2817 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E2818 | ISODate | Not a component record in this worksheet |
| src-000367 | field-type | E2819 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E289 | EventFrequencyCode | Not a component record in this worksheet |
| src-000370 | field-type | E290 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E291 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E292 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000370 | field-type | E293 | ValuationTimingCode | Not a component record in this worksheet |
| src-000370 | field-type | E294 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E295 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E296 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000370 | field-type | E297 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000370 | field-type | E298 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E299 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E300 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000370 | field-type | E301 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000370 | field-type | E302 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000370 | field-type | E303 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000370 | field-type | E304 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000370 | field-type | E305 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000370 | field-type | E306 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E307 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E308 | ISODate | Not a component record in this worksheet |
| src-000370 | field-type | E309 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E289 | EventFrequencyCode | Not a component record in this worksheet |
| src-000373 | field-type | E290 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E291 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E292 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000373 | field-type | E293 | ValuationTimingCode | Not a component record in this worksheet |
| src-000373 | field-type | E294 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E295 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E296 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000373 | field-type | E297 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000373 | field-type | E298 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E299 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E300 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000373 | field-type | E301 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000373 | field-type | E302 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000373 | field-type | E303 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000373 | field-type | E304 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000373 | field-type | E305 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000373 | field-type | E306 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E307 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E308 | ISODate | Not a component record in this worksheet |
| src-000373 | field-type | E309 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E2847 | EventFrequencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E2848 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E2849 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E2850 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000376 | field-type | E2851 | ValuationTimingCode | Not a component record in this worksheet |
| src-000376 | field-type | E2852 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E2853 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E2854 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000376 | field-type | E2855 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000376 | field-type | E2856 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E2857 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E2858 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000376 | field-type | E2859 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000376 | field-type | E2860 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000376 | field-type | E2861 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000376 | field-type | E2862 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000376 | field-type | E2863 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000376 | field-type | E2864 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E2865 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E2866 | ISODate | Not a component record in this worksheet |
| src-000376 | field-type | E2867 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E289 | EventFrequencyCode | Not a component record in this worksheet |
| src-000379 | field-type | E290 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E291 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E292 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000379 | field-type | E293 | ValuationTimingCode | Not a component record in this worksheet |
| src-000379 | field-type | E294 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E295 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E296 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000379 | field-type | E297 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000379 | field-type | E298 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E299 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E300 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000379 | field-type | E301 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000379 | field-type | E302 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000379 | field-type | E303 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000379 | field-type | E304 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000379 | field-type | E305 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000379 | field-type | E306 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E307 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E308 | ISODate | Not a component record in this worksheet |
| src-000379 | field-type | E309 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E2824 | EventFrequencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E2825 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E2826 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E2827 | InvestmentFundClass | [InvestmentFundClass](bc-1089e9d8af2a0cd64ee7.md) |
| src-000382 | field-type | E2828 | ValuationTimingCode | Not a component record in this worksheet |
| src-000382 | field-type | E2829 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E2830 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E2831 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000382 | field-type | E2832 | Tax | [Tax](bc-b7e53c3a57e16730ee76.md) |
| src-000382 | field-type | E2833 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E2834 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E2835 | ValuationStatistics | [ValuationStatistics](bc-58d1f3577205956e2c3b.md) |
| src-000382 | field-type | E2836 | PerformanceFactors | [PerformanceFactors](bc-823eb2a8e1fa344f1e2a.md) |
| src-000382 | field-type | E2837 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000382 | field-type | E2838 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000382 | field-type | E2839 | Interest | [Interest](bc-5a1033f0a369596d5a63.md) |
| src-000382 | field-type | E2840 | FundsCashFlow | [FundsCashFlow](bc-04400270b3df0ca87f1e.md) |
| src-000382 | field-type | E2841 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E2842 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E2843 | ISODate | Not a component record in this worksheet |
| src-000382 | field-type | E2844 | YesNoIndicator | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
