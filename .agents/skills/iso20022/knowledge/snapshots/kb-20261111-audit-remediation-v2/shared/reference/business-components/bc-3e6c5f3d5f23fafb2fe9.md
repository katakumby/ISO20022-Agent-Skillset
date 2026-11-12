---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-3e6c5f3d5f23fafb2fe9"
title: "InvestmentPlan"
business_component_name: "InvestmentPlan"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A2415:F2429"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A2380:F2394"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A2415:F2429"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A2415:F2429"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A2415:F2429"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A2415:F2429"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A2415:F2429"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A2380:F2394"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A2415:F2429"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A2393:F2407"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A1114:F1128"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A2393:F2407"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A2415:F2429"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A2368:F2382"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A1114:F1128"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A1114:F1128"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A2368:F2382"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A2368:F2382"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A1114:F1128"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A1114:F1128"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A2415:F2429"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A1114:F1128"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A2393:F2407"]}]
content_sha256: "3e6c5f3d5f23fafb2fe9cbd4aa7d1f8d78f29b8ace322fede729167bc01e975c"
parent_names: []
related_component_names: ["Asset", "CurrencyAndAmount", "CurrencyCode", "DateTimePeriod", "FrequencyCode", "Instalment", "InsuranceCertificate", "InvestmentAccountService", "InvestmentFundOrder", "Pension", "PlanStatusCode", "Portfolio", "TaxEfficientProduct", "YesNoIndicator"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# InvestmentPlan

## Definition

Plan that allows investors to schedule periodical investments or divestments, according to pre-defined criteria.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | InvestmentPlan | ∅ | ∅ | Plan that allows investors to schedule periodical investments or divestments, according to pre-defined criteria. | ∅ | ∅ |
| 2 | InvestmentPlan | Frequency | ∅ | Frequency of the investment or divestment, eg, daily, weekly, or monthly. | FrequencyCode | ∅ |
| 3 | InvestmentPlan | Amount | ∅ | Currency and amount of the periodical payments. When the standing order is related to a fund investment plan, this is the cash part of the invested amount. | CurrencyAndAmount | ∅ |
| 4 | InvestmentPlan | Asset | ∅ | Security that an investment plan invests in, or from which the investment plan divests. | Asset | InvestmentPlan |
| 5 | InvestmentPlan | Instalment | ∅ | Specifies information on the successive payments in an investment plan. | Instalment | InvestmentPlan |
| 6 | InvestmentPlan | RelatedService | ∅ | Service which provides a systematic investment plan. | InvestmentAccountService | SystematicInvestmentPlan |
| 7 | InvestmentPlan | Insurance | ∅ | Insurance contract which covers the investment plan. | InsuranceCertificate | RelatedInvestmentPlan |
| 8 | InvestmentPlan | StandingOrder | ∅ | Order generated automatically, according to the terms of the investment plan. | InvestmentFundOrder | InvestmentPlan |
| 9 | InvestmentPlan | MultiCurrency | ∅ | Specifies whether the investment plan is multi currency or not. | YesNoIndicator | ∅ |
| 10 | InvestmentPlan | Currency | ∅ | Currency of the investment plan. | CurrencyCode | ∅ |
| 11 | InvestmentPlan | Portfolio | ∅ | Portfolio for which the investment plan invests or divests. | Portfolio | InvestmentPlan |
| 12 | InvestmentPlan | InvestmentPeriod | ∅ | Period during which an investment plan has to be executed. | DateTimePeriod | RelatedInvestmentPlan |
| 13 | InvestmentPlan | PlanStatus | ∅ | Status of the savings or withdrawal investment plan.  | PlanStatusCode | ∅ |
| 14 | InvestmentPlan | Pension | ∅ | Attributes of a pension. | Pension | RelatedInvestmentPlan |
| 15 | InvestmentPlan | TaxEfficientProduct | ∅ | Characteristics of a tax efficient product. | TaxEfficientProduct | RelatedInvestmentPlan |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `3e6c5f3d5f23fafb2fe9cbd4aa7d1f8d78f29b8ace322fede729167bc01e975c`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A2415:F2429 | 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A2380:F2394 | 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A2415:F2429 | 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A2415:F2429 | 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A2415:F2429 | 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A2415:F2429 | 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A2415:F2429 | 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A2380:F2394 | 2380, 2381, 2382, 2383, 2384, 2385, 2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A2415:F2429 | 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A2393:F2407 | 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401, 2402, 2403, 2404, 2405, 2406, 2407 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A1114:F1128 | 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A2393:F2407 | 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401, 2402, 2403, 2404, 2405, 2406, 2407 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A2415:F2429 | 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A2368:F2382 | 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A1114:F1128 | 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A1114:F1128 | 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A2368:F2382 | 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A2368:F2382 | 2368, 2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A1114:F1128 | 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A1114:F1128 | 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A2415:F2429 | 2415, 2416, 2417, 2418, 2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A1114:F1128 | 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A2393:F2407 | 2393, 2394, 2395, 2396, 2397, 2398, 2399, 2400, 2401, 2402, 2403, 2404, 2405, 2406, 2407 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E2416 | FrequencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E2417 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E2418 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000006 | field-type | E2419 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000006 | field-type | E2420 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000006 | field-type | E2421 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000006 | field-type | E2422 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000006 | field-type | E2423 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E2424 | CurrencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E2425 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000006 | field-type | E2426 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000006 | field-type | E2427 | PlanStatusCode | Not a component record in this worksheet |
| src-000006 | field-type | E2428 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000006 | field-type | E2429 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000016 | field-type | E2381 | FrequencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E2382 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E2383 | Asset | [Asset](bc-87860832834678110ffe.md) |
| src-000016 | field-type | E2384 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000016 | field-type | E2385 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000016 | field-type | E2386 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000016 | field-type | E2387 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000016 | field-type | E2388 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E2389 | CurrencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E2390 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000016 | field-type | E2391 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000016 | field-type | E2392 | PlanStatusCode | Not a component record in this worksheet |
| src-000016 | field-type | E2393 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000016 | field-type | E2394 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000054 | field-type | E2416 | FrequencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E2417 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E2418 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000054 | field-type | E2419 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000054 | field-type | E2420 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000054 | field-type | E2421 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000054 | field-type | E2422 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000054 | field-type | E2423 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E2424 | CurrencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E2425 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000054 | field-type | E2426 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000054 | field-type | E2427 | PlanStatusCode | Not a component record in this worksheet |
| src-000054 | field-type | E2428 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000054 | field-type | E2429 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000081 | field-type | E2416 | FrequencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E2417 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E2418 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000081 | field-type | E2419 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000081 | field-type | E2420 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000081 | field-type | E2421 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000081 | field-type | E2422 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000081 | field-type | E2423 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E2424 | CurrencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E2425 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000081 | field-type | E2426 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000081 | field-type | E2427 | PlanStatusCode | Not a component record in this worksheet |
| src-000081 | field-type | E2428 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000081 | field-type | E2429 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000097 | field-type | E2416 | FrequencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E2417 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E2418 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000097 | field-type | E2419 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000097 | field-type | E2420 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000097 | field-type | E2421 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000097 | field-type | E2422 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000097 | field-type | E2423 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E2424 | CurrencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E2425 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000097 | field-type | E2426 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000097 | field-type | E2427 | PlanStatusCode | Not a component record in this worksheet |
| src-000097 | field-type | E2428 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000097 | field-type | E2429 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000164 | field-type | E2416 | FrequencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E2417 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E2418 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000164 | field-type | E2419 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000164 | field-type | E2420 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000164 | field-type | E2421 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000164 | field-type | E2422 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000164 | field-type | E2423 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E2424 | CurrencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E2425 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000164 | field-type | E2426 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000164 | field-type | E2427 | PlanStatusCode | Not a component record in this worksheet |
| src-000164 | field-type | E2428 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000164 | field-type | E2429 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000175 | field-type | E2416 | FrequencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E2417 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E2418 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000175 | field-type | E2419 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000175 | field-type | E2420 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000175 | field-type | E2421 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000175 | field-type | E2422 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000175 | field-type | E2423 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E2424 | CurrencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E2425 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000175 | field-type | E2426 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000175 | field-type | E2427 | PlanStatusCode | Not a component record in this worksheet |
| src-000175 | field-type | E2428 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000175 | field-type | E2429 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000182 | field-type | E2381 | FrequencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E2382 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E2383 | Asset | [Asset](bc-87860832834678110ffe.md) |
| src-000182 | field-type | E2384 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000182 | field-type | E2385 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000182 | field-type | E2386 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000182 | field-type | E2387 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000182 | field-type | E2388 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E2389 | CurrencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E2390 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000182 | field-type | E2391 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000182 | field-type | E2392 | PlanStatusCode | Not a component record in this worksheet |
| src-000182 | field-type | E2393 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000182 | field-type | E2394 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000198 | field-type | E2416 | FrequencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E2417 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E2418 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000198 | field-type | E2419 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000198 | field-type | E2420 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000198 | field-type | E2421 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000198 | field-type | E2422 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000198 | field-type | E2423 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E2424 | CurrencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E2425 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000198 | field-type | E2426 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000198 | field-type | E2427 | PlanStatusCode | Not a component record in this worksheet |
| src-000198 | field-type | E2428 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000198 | field-type | E2429 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000322 | field-type | E2394 | FrequencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E2395 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E2396 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000322 | field-type | E2397 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000322 | field-type | E2398 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000322 | field-type | E2399 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000322 | field-type | E2400 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000322 | field-type | E2401 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E2402 | CurrencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E2403 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000322 | field-type | E2404 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000322 | field-type | E2405 | PlanStatusCode | Not a component record in this worksheet |
| src-000322 | field-type | E2406 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000322 | field-type | E2407 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000345 | field-type | E1115 | FrequencyCode | Not a component record in this worksheet |
| src-000345 | field-type | E1116 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E1117 | Asset | [Asset](bc-b6605fb2de1fb99567ff.md) |
| src-000345 | field-type | E1118 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000345 | field-type | E1119 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000345 | field-type | E1120 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000345 | field-type | E1121 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000345 | field-type | E1122 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E1123 | CurrencyCode | Not a component record in this worksheet |
| src-000345 | field-type | E1124 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000345 | field-type | E1125 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000345 | field-type | E1126 | PlanStatusCode | Not a component record in this worksheet |
| src-000345 | field-type | E1127 | Pension | [Pension](bc-0bc5cadf5e468aed509b.md) |
| src-000345 | field-type | E1128 | TaxEfficientProduct | [TaxEfficientProduct](bc-c292860e0b62a43b4b93.md) |
| src-000348 | field-type | E2394 | FrequencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E2395 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E2396 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000348 | field-type | E2397 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000348 | field-type | E2398 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000348 | field-type | E2399 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000348 | field-type | E2400 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000348 | field-type | E2401 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E2402 | CurrencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E2403 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000348 | field-type | E2404 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000348 | field-type | E2405 | PlanStatusCode | Not a component record in this worksheet |
| src-000348 | field-type | E2406 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000348 | field-type | E2407 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000352 | field-type | E2416 | FrequencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E2417 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E2418 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000352 | field-type | E2419 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000352 | field-type | E2420 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000352 | field-type | E2421 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000352 | field-type | E2422 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000352 | field-type | E2423 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E2424 | CurrencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E2425 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000352 | field-type | E2426 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000352 | field-type | E2427 | PlanStatusCode | Not a component record in this worksheet |
| src-000352 | field-type | E2428 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000352 | field-type | E2429 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000355 | field-type | E2369 | FrequencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E2370 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E2371 | Asset | [Asset](bc-87860832834678110ffe.md) |
| src-000355 | field-type | E2372 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000355 | field-type | E2373 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000355 | field-type | E2374 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000355 | field-type | E2375 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000355 | field-type | E2376 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E2377 | CurrencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E2378 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000355 | field-type | E2379 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000355 | field-type | E2380 | PlanStatusCode | Not a component record in this worksheet |
| src-000355 | field-type | E2381 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000355 | field-type | E2382 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000358 | field-type | E1115 | FrequencyCode | Not a component record in this worksheet |
| src-000358 | field-type | E1116 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E1117 | Asset | [Asset](bc-b6605fb2de1fb99567ff.md) |
| src-000358 | field-type | E1118 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000358 | field-type | E1119 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000358 | field-type | E1120 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000358 | field-type | E1121 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000358 | field-type | E1122 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E1123 | CurrencyCode | Not a component record in this worksheet |
| src-000358 | field-type | E1124 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000358 | field-type | E1125 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000358 | field-type | E1126 | PlanStatusCode | Not a component record in this worksheet |
| src-000358 | field-type | E1127 | Pension | [Pension](bc-0bc5cadf5e468aed509b.md) |
| src-000358 | field-type | E1128 | TaxEfficientProduct | [TaxEfficientProduct](bc-c292860e0b62a43b4b93.md) |
| src-000361 | field-type | E1115 | FrequencyCode | Not a component record in this worksheet |
| src-000361 | field-type | E1116 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E1117 | Asset | [Asset](bc-b6605fb2de1fb99567ff.md) |
| src-000361 | field-type | E1118 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000361 | field-type | E1119 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000361 | field-type | E1120 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000361 | field-type | E1121 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000361 | field-type | E1122 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E1123 | CurrencyCode | Not a component record in this worksheet |
| src-000361 | field-type | E1124 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000361 | field-type | E1125 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000361 | field-type | E1126 | PlanStatusCode | Not a component record in this worksheet |
| src-000361 | field-type | E1127 | Pension | [Pension](bc-0bc5cadf5e468aed509b.md) |
| src-000361 | field-type | E1128 | TaxEfficientProduct | [TaxEfficientProduct](bc-c292860e0b62a43b4b93.md) |
| src-000364 | field-type | E2369 | FrequencyCode | Not a component record in this worksheet |
| src-000364 | field-type | E2370 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E2371 | Asset | [Asset](bc-b6605fb2de1fb99567ff.md) |
| src-000364 | field-type | E2372 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000364 | field-type | E2373 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000364 | field-type | E2374 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000364 | field-type | E2375 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000364 | field-type | E2376 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E2377 | CurrencyCode | Not a component record in this worksheet |
| src-000364 | field-type | E2378 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000364 | field-type | E2379 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000364 | field-type | E2380 | PlanStatusCode | Not a component record in this worksheet |
| src-000364 | field-type | E2381 | Pension | [Pension](bc-0bc5cadf5e468aed509b.md) |
| src-000364 | field-type | E2382 | TaxEfficientProduct | [TaxEfficientProduct](bc-c292860e0b62a43b4b93.md) |
| src-000367 | field-type | E2369 | FrequencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E2370 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E2371 | Asset | [Asset](bc-87860832834678110ffe.md) |
| src-000367 | field-type | E2372 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000367 | field-type | E2373 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000367 | field-type | E2374 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000367 | field-type | E2375 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000367 | field-type | E2376 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E2377 | CurrencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E2378 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000367 | field-type | E2379 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000367 | field-type | E2380 | PlanStatusCode | Not a component record in this worksheet |
| src-000367 | field-type | E2381 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000367 | field-type | E2382 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000370 | field-type | E1115 | FrequencyCode | Not a component record in this worksheet |
| src-000370 | field-type | E1116 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E1117 | Asset | [Asset](bc-b6605fb2de1fb99567ff.md) |
| src-000370 | field-type | E1118 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000370 | field-type | E1119 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000370 | field-type | E1120 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000370 | field-type | E1121 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000370 | field-type | E1122 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E1123 | CurrencyCode | Not a component record in this worksheet |
| src-000370 | field-type | E1124 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000370 | field-type | E1125 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000370 | field-type | E1126 | PlanStatusCode | Not a component record in this worksheet |
| src-000370 | field-type | E1127 | Pension | [Pension](bc-0bc5cadf5e468aed509b.md) |
| src-000370 | field-type | E1128 | TaxEfficientProduct | [TaxEfficientProduct](bc-c292860e0b62a43b4b93.md) |
| src-000373 | field-type | E1115 | FrequencyCode | Not a component record in this worksheet |
| src-000373 | field-type | E1116 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E1117 | Asset | [Asset](bc-b6605fb2de1fb99567ff.md) |
| src-000373 | field-type | E1118 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000373 | field-type | E1119 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000373 | field-type | E1120 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000373 | field-type | E1121 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000373 | field-type | E1122 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E1123 | CurrencyCode | Not a component record in this worksheet |
| src-000373 | field-type | E1124 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000373 | field-type | E1125 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000373 | field-type | E1126 | PlanStatusCode | Not a component record in this worksheet |
| src-000373 | field-type | E1127 | Pension | [Pension](bc-0bc5cadf5e468aed509b.md) |
| src-000373 | field-type | E1128 | TaxEfficientProduct | [TaxEfficientProduct](bc-c292860e0b62a43b4b93.md) |
| src-000376 | field-type | E2416 | FrequencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E2417 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E2418 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000376 | field-type | E2419 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000376 | field-type | E2420 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000376 | field-type | E2421 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000376 | field-type | E2422 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000376 | field-type | E2423 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E2424 | CurrencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E2425 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000376 | field-type | E2426 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000376 | field-type | E2427 | PlanStatusCode | Not a component record in this worksheet |
| src-000376 | field-type | E2428 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000376 | field-type | E2429 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |
| src-000379 | field-type | E1115 | FrequencyCode | Not a component record in this worksheet |
| src-000379 | field-type | E1116 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E1117 | Asset | [Asset](bc-b6605fb2de1fb99567ff.md) |
| src-000379 | field-type | E1118 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000379 | field-type | E1119 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000379 | field-type | E1120 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000379 | field-type | E1121 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000379 | field-type | E1122 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E1123 | CurrencyCode | Not a component record in this worksheet |
| src-000379 | field-type | E1124 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000379 | field-type | E1125 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000379 | field-type | E1126 | PlanStatusCode | Not a component record in this worksheet |
| src-000379 | field-type | E1127 | Pension | [Pension](bc-0bc5cadf5e468aed509b.md) |
| src-000379 | field-type | E1128 | TaxEfficientProduct | [TaxEfficientProduct](bc-c292860e0b62a43b4b93.md) |
| src-000382 | field-type | E2394 | FrequencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E2395 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E2396 | Asset | [Asset](bc-ce11847d7df25ab37c5a.md) |
| src-000382 | field-type | E2397 | Instalment | [Instalment](bc-45a409f655552d1e6dba.md) |
| src-000382 | field-type | E2398 | InvestmentAccountService | [InvestmentAccountService](bc-f222f67b3f4b17a64420.md) |
| src-000382 | field-type | E2399 | InsuranceCertificate | [InsuranceCertificate](bc-c138afb1fb16a9abe8af.md) |
| src-000382 | field-type | E2400 | InvestmentFundOrder | [InvestmentFundOrder](bc-6aec42483ef15d38c88f.md) |
| src-000382 | field-type | E2401 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E2402 | CurrencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E2403 | Portfolio | [Portfolio](bc-b8df7f55e50344a17d19.md) |
| src-000382 | field-type | E2404 | DateTimePeriod | [DateTimePeriod](bc-420f6b7b61cb1a61affe.md) |
| src-000382 | field-type | E2405 | PlanStatusCode | Not a component record in this worksheet |
| src-000382 | field-type | E2406 | Pension | [Pension](bc-eab9e1a0d50d4fa9f809.md) |
| src-000382 | field-type | E2407 | TaxEfficientProduct | [TaxEfficientProduct](bc-a2914ad2e706e1981a26.md) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
