---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-be8dc03e8889f0ff1fc6"
title: "SecuritiesBalance"
business_component_name: "SecuritiesBalance"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A3921:F3945"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A3851:F3875"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A3921:F3945"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A3921:F3945"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A3921:F3945"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A3921:F3945"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A3921:F3945"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A3851:F3875"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A3921:F3945"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A3890:F3914"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A2561:F2585"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A3890:F3914"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A3921:F3945"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A3829:F3853"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A2561:F2585"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A2561:F2585"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A3829:F3853"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A3829:F3853"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A2561:F2585"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A2561:F2585"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A3921:F3945"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A2561:F2585"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A3890:F3914"]}]
content_sha256: "be8dc03e8889f0ff1fc67d918a3bddac0bcb36b7db188ffebed036b7900d2dc8"
parent_names: ["Balance"]
related_component_names: ["CorporateActionEntitlement", "CurrencyAndAmount", "CurrencyExchange", "IntraPositionTransfer", "MeetingEntitlement", "Pledgee", "SafekeepingPlace", "SecuritiesAccount", "SecuritiesBalance", "SecuritiesBalanceTypeV2Code", "SecuritiesEntry", "SecuritiesQuantity", "Security", "ShortLongCode", "YesNoIndicator"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# SecuritiesBalance

## Definition

Net position of a segregated holding, in a single security, within the overall position held in a securities account. A securities balance is calculated from the sum of securities' receipts minus the sum of securities' deliveries.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SecuritiesBalance | ∅ | Balance | Net position of a segregated holding, in a single security, within the overall position held in a securities account. A securities balance is calculated from the sum of securities' receipts minus the sum of securities' deliveries. | ∅ | ∅ |
| 2 | SecuritiesBalance | NetGainLoss | ∅ | Amount representing the difference between the cost and the current price of a security. In the context of securities settlement, it is the amount paid or received when the instructions are netted or paired off. | CurrencyAndAmount | ∅ |
| 3 | SecuritiesBalance | SecuritiesAccount | ∅ | Account or sub-account for which a balance is calculated. It is derived from the association between Balance and Account. | SecuritiesAccount | SecuritiesBalance |
| 4 | SecuritiesBalance | EligibleBalanceRelatedEntitlement | ∅ | Corporate action entitlement for which an eligible balance is specified. | CorporateActionEntitlement | EligibleBalance |
| 5 | SecuritiesBalance | ShortLong | ∅ | Indication that the position is short or long. | ShortLongCode | ∅ |
| 6 | SecuritiesBalance | AggregateQuantity | ∅ | Total quantity of financial instruments of the balance. | SecuritiesQuantity | AggregateQuantityBalance |
| 7 | SecuritiesBalance | CorporateActionEntitlement | ∅ | Corporate action entitlement for which a balance is specified. | CorporateActionEntitlement | SecuritiesBalance |
| 8 | SecuritiesBalance | InstructedBalanceRelatedEntitlement | ∅ | Corporate action entitlement for which an instructed balance is specified. | CorporateActionEntitlement | InstructedBalance |
| 9 | SecuritiesBalance | UninstructedBalanceRelatedEntitlement | ∅ | Corporate action entitlement for which an uninstructed balance is specified. | CorporateActionEntitlement | UninstructedBalance |
| 10 | SecuritiesBalance | MainSecuritiesBalance | ∅ | Balance which is divided in sub-balances. | SecuritiesBalance | SecuritiesSubBalance |
| 11 | SecuritiesBalance | SecuritiesSubBalance | ∅ | Net position of a segregated holding of a single security within the overall position held in an account, eg, sub-balance per status. | SecuritiesBalance | MainSecuritiesBalance |
| 12 | SecuritiesBalance | SecuritiesBalanceType | ∅ | Reason a security is not available or additional information about the financial instrument for which the balance is given, for example, unregistered, registered in nominee name. | SecuritiesBalanceTypeV2Code | ∅ |
| 13 | SecuritiesBalance | SubBalanceQuantity | ∅ | Net position of a segregated holding of a single security within the overall position held in a securities account, for instance. sub-balance per type. | SecuritiesQuantity | RelatedSubBalance |
| 14 | SecuritiesBalance | Security | ∅ | Security for which a balance is calculated. | Security | Balance |
| 15 | SecuritiesBalance | ExchangeRate | ∅ | Specifies the exchange rate used to convert the balance value in another currency. | CurrencyExchange | CurrencyExchangeForSecuritiesBalance |
| 16 | SecuritiesBalance | AvailabilityIndicator | ∅ | Indicates whether the quantity of securities on the balance is available. | YesNoIndicator | ∅ |
| 17 | SecuritiesBalance | AvailableQuantity | ∅ | Total quantity of financial instruments of the balance that is available. | SecuritiesQuantity | AvailableQuantityBalance |
| 18 | SecuritiesBalance | RelatedMeetingEntitlement | ∅ | Entitlement for which an eligible posistion is specified. | MeetingEntitlement | EligiblePosition |
| 19 | SecuritiesBalance | UnavailableQuantity | ∅ | Total quantity of financial instruments of the balance that is not available. | SecuritiesQuantity | UnavailableQuantityBalance |
| 20 | SecuritiesBalance | SafekeepingPlace | ∅ | Safekeeping place at which the securities are held. | SafekeepingPlace | SecuritiesBalance |
| 21 | SecuritiesBalance | SecuritiesEntry | ∅ | Postings used to calculate a balance. It is derived from the association between Balance and Entry | SecuritiesEntry | SecuritiesBalance |
| 22 | SecuritiesBalance | NotEligibleBalanceRelatedEntitlement | ∅ | Corporate action entitlement for which a non eligible balance is specified. | CorporateActionEntitlement | NotEligibleBalance |
| 23 | SecuritiesBalance | RelatedIntraPositionTransfer | ∅ | Transfer between two balances or sub balances. | IntraPositionTransfer | SecuritiesBalance |
| 24 | SecuritiesBalance | CostAdjustment | ∅ | Specifies the amount added or substracted to the original cost of a transaction. | CurrencyAndAmount | ∅ |
| 25 | SecuritiesBalance | Pledgee | ∅ | Pledgee at which the securities are held. | Pledgee | SecuritiesBalance |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `be8dc03e8889f0ff1fc67d918a3bddac0bcb36b7db188ffebed036b7900d2dc8`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A3921:F3945 | 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A3851:F3875 | 3851, 3852, 3853, 3854, 3855, 3856, 3857, 3858, 3859, 3860, 3861, 3862, 3863, 3864, 3865, 3866, 3867, 3868, 3869, 3870, 3871, 3872, 3873, 3874, 3875 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A3921:F3945 | 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A3921:F3945 | 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A3921:F3945 | 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A3921:F3945 | 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A3921:F3945 | 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A3851:F3875 | 3851, 3852, 3853, 3854, 3855, 3856, 3857, 3858, 3859, 3860, 3861, 3862, 3863, 3864, 3865, 3866, 3867, 3868, 3869, 3870, 3871, 3872, 3873, 3874, 3875 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A3921:F3945 | 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A3890:F3914 | 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909, 3910, 3911, 3912, 3913, 3914 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A2561:F2585 | 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A3890:F3914 | 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909, 3910, 3911, 3912, 3913, 3914 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A3921:F3945 | 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A3829:F3853 | 3829, 3830, 3831, 3832, 3833, 3834, 3835, 3836, 3837, 3838, 3839, 3840, 3841, 3842, 3843, 3844, 3845, 3846, 3847, 3848, 3849, 3850, 3851, 3852, 3853 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A2561:F2585 | 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A2561:F2585 | 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A3829:F3853 | 3829, 3830, 3831, 3832, 3833, 3834, 3835, 3836, 3837, 3838, 3839, 3840, 3841, 3842, 3843, 3844, 3845, 3846, 3847, 3848, 3849, 3850, 3851, 3852, 3853 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A3829:F3853 | 3829, 3830, 3831, 3832, 3833, 3834, 3835, 3836, 3837, 3838, 3839, 3840, 3841, 3842, 3843, 3844, 3845, 3846, 3847, 3848, 3849, 3850, 3851, 3852, 3853 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A2561:F2585 | 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A2561:F2585 | 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A3921:F3945 | 3921, 3922, 3923, 3924, 3925, 3926, 3927, 3928, 3929, 3930, 3931, 3932, 3933, 3934, 3935, 3936, 3937, 3938, 3939, 3940, 3941, 3942, 3943, 3944, 3945 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A2561:F2585 | 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A3890:F3914 | 3890, 3891, 3892, 3893, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3901, 3902, 3903, 3904, 3905, 3906, 3907, 3908, 3909, 3910, 3911, 3912, 3913, 3914 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C3921 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000006 | field-type | E3922 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E3923 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000006 | field-type | E3924 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000006 | field-type | E3925 | ShortLongCode | Not a component record in this worksheet |
| src-000006 | field-type | E3926 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000006 | field-type | E3927 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000006 | field-type | E3928 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000006 | field-type | E3929 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000006 | field-type | E3930 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000006 | field-type | E3931 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000006 | field-type | E3932 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000006 | field-type | E3933 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000006 | field-type | E3934 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000006 | field-type | E3935 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000006 | field-type | E3936 | YesNoIndicator | Not a component record in this worksheet |
| src-000006 | field-type | E3937 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000006 | field-type | E3938 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000006 | field-type | E3939 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000006 | field-type | E3940 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000006 | field-type | E3941 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000006 | field-type | E3942 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000006 | field-type | E3943 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000006 | field-type | E3944 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E3945 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000016 | parent | C3851 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000016 | field-type | E3852 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E3853 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000016 | field-type | E3854 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000016 | field-type | E3855 | ShortLongCode | Not a component record in this worksheet |
| src-000016 | field-type | E3856 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000016 | field-type | E3857 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000016 | field-type | E3858 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000016 | field-type | E3859 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000016 | field-type | E3860 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000016 | field-type | E3861 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000016 | field-type | E3862 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000016 | field-type | E3863 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000016 | field-type | E3864 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000016 | field-type | E3865 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000016 | field-type | E3866 | YesNoIndicator | Not a component record in this worksheet |
| src-000016 | field-type | E3867 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000016 | field-type | E3868 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000016 | field-type | E3869 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000016 | field-type | E3870 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000016 | field-type | E3871 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000016 | field-type | E3872 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000016 | field-type | E3873 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000016 | field-type | E3874 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E3875 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000054 | parent | C3921 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000054 | field-type | E3922 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E3923 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000054 | field-type | E3924 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000054 | field-type | E3925 | ShortLongCode | Not a component record in this worksheet |
| src-000054 | field-type | E3926 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000054 | field-type | E3927 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000054 | field-type | E3928 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000054 | field-type | E3929 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000054 | field-type | E3930 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000054 | field-type | E3931 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000054 | field-type | E3932 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000054 | field-type | E3933 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000054 | field-type | E3934 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000054 | field-type | E3935 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000054 | field-type | E3936 | YesNoIndicator | Not a component record in this worksheet |
| src-000054 | field-type | E3937 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000054 | field-type | E3938 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000054 | field-type | E3939 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000054 | field-type | E3940 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000054 | field-type | E3941 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000054 | field-type | E3942 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000054 | field-type | E3943 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000054 | field-type | E3944 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E3945 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000081 | parent | C3921 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000081 | field-type | E3922 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E3923 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000081 | field-type | E3924 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000081 | field-type | E3925 | ShortLongCode | Not a component record in this worksheet |
| src-000081 | field-type | E3926 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000081 | field-type | E3927 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000081 | field-type | E3928 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000081 | field-type | E3929 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000081 | field-type | E3930 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000081 | field-type | E3931 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000081 | field-type | E3932 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000081 | field-type | E3933 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000081 | field-type | E3934 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000081 | field-type | E3935 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000081 | field-type | E3936 | YesNoIndicator | Not a component record in this worksheet |
| src-000081 | field-type | E3937 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000081 | field-type | E3938 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000081 | field-type | E3939 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000081 | field-type | E3940 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000081 | field-type | E3941 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000081 | field-type | E3942 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000081 | field-type | E3943 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000081 | field-type | E3944 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E3945 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000097 | parent | C3921 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000097 | field-type | E3922 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E3923 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000097 | field-type | E3924 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000097 | field-type | E3925 | ShortLongCode | Not a component record in this worksheet |
| src-000097 | field-type | E3926 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000097 | field-type | E3927 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000097 | field-type | E3928 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000097 | field-type | E3929 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000097 | field-type | E3930 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000097 | field-type | E3931 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000097 | field-type | E3932 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000097 | field-type | E3933 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000097 | field-type | E3934 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000097 | field-type | E3935 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000097 | field-type | E3936 | YesNoIndicator | Not a component record in this worksheet |
| src-000097 | field-type | E3937 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000097 | field-type | E3938 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000097 | field-type | E3939 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000097 | field-type | E3940 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000097 | field-type | E3941 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000097 | field-type | E3942 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000097 | field-type | E3943 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000097 | field-type | E3944 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E3945 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000164 | parent | C3921 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000164 | field-type | E3922 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E3923 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000164 | field-type | E3924 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000164 | field-type | E3925 | ShortLongCode | Not a component record in this worksheet |
| src-000164 | field-type | E3926 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000164 | field-type | E3927 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000164 | field-type | E3928 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000164 | field-type | E3929 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000164 | field-type | E3930 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000164 | field-type | E3931 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000164 | field-type | E3932 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000164 | field-type | E3933 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000164 | field-type | E3934 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000164 | field-type | E3935 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000164 | field-type | E3936 | YesNoIndicator | Not a component record in this worksheet |
| src-000164 | field-type | E3937 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000164 | field-type | E3938 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000164 | field-type | E3939 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000164 | field-type | E3940 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000164 | field-type | E3941 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000164 | field-type | E3942 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000164 | field-type | E3943 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000164 | field-type | E3944 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E3945 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000175 | parent | C3921 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000175 | field-type | E3922 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E3923 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000175 | field-type | E3924 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000175 | field-type | E3925 | ShortLongCode | Not a component record in this worksheet |
| src-000175 | field-type | E3926 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000175 | field-type | E3927 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000175 | field-type | E3928 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000175 | field-type | E3929 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000175 | field-type | E3930 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000175 | field-type | E3931 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000175 | field-type | E3932 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000175 | field-type | E3933 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000175 | field-type | E3934 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000175 | field-type | E3935 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000175 | field-type | E3936 | YesNoIndicator | Not a component record in this worksheet |
| src-000175 | field-type | E3937 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000175 | field-type | E3938 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000175 | field-type | E3939 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000175 | field-type | E3940 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000175 | field-type | E3941 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000175 | field-type | E3942 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000175 | field-type | E3943 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000175 | field-type | E3944 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E3945 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000182 | parent | C3851 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000182 | field-type | E3852 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E3853 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000182 | field-type | E3854 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000182 | field-type | E3855 | ShortLongCode | Not a component record in this worksheet |
| src-000182 | field-type | E3856 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000182 | field-type | E3857 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000182 | field-type | E3858 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000182 | field-type | E3859 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000182 | field-type | E3860 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000182 | field-type | E3861 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000182 | field-type | E3862 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000182 | field-type | E3863 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000182 | field-type | E3864 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000182 | field-type | E3865 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000182 | field-type | E3866 | YesNoIndicator | Not a component record in this worksheet |
| src-000182 | field-type | E3867 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000182 | field-type | E3868 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000182 | field-type | E3869 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000182 | field-type | E3870 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000182 | field-type | E3871 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000182 | field-type | E3872 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000182 | field-type | E3873 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000182 | field-type | E3874 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E3875 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000198 | parent | C3921 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000198 | field-type | E3922 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E3923 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000198 | field-type | E3924 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000198 | field-type | E3925 | ShortLongCode | Not a component record in this worksheet |
| src-000198 | field-type | E3926 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000198 | field-type | E3927 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000198 | field-type | E3928 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000198 | field-type | E3929 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000198 | field-type | E3930 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000198 | field-type | E3931 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000198 | field-type | E3932 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000198 | field-type | E3933 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000198 | field-type | E3934 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000198 | field-type | E3935 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000198 | field-type | E3936 | YesNoIndicator | Not a component record in this worksheet |
| src-000198 | field-type | E3937 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000198 | field-type | E3938 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000198 | field-type | E3939 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000198 | field-type | E3940 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000198 | field-type | E3941 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000198 | field-type | E3942 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000198 | field-type | E3943 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000198 | field-type | E3944 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E3945 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000322 | parent | C3890 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000322 | field-type | E3891 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E3892 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000322 | field-type | E3893 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000322 | field-type | E3894 | ShortLongCode | Not a component record in this worksheet |
| src-000322 | field-type | E3895 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000322 | field-type | E3896 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000322 | field-type | E3897 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000322 | field-type | E3898 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000322 | field-type | E3899 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000322 | field-type | E3900 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000322 | field-type | E3901 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000322 | field-type | E3902 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000322 | field-type | E3903 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000322 | field-type | E3904 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000322 | field-type | E3905 | YesNoIndicator | Not a component record in this worksheet |
| src-000322 | field-type | E3906 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000322 | field-type | E3907 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000322 | field-type | E3908 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000322 | field-type | E3909 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000322 | field-type | E3910 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000322 | field-type | E3911 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000322 | field-type | E3912 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000322 | field-type | E3913 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E3914 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000345 | parent | C2561 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000345 | field-type | E2562 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E2563 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000345 | field-type | E2564 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000345 | field-type | E2565 | ShortLongCode | Not a component record in this worksheet |
| src-000345 | field-type | E2566 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000345 | field-type | E2567 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000345 | field-type | E2568 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000345 | field-type | E2569 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000345 | field-type | E2570 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000345 | field-type | E2571 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000345 | field-type | E2572 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000345 | field-type | E2573 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000345 | field-type | E2574 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000345 | field-type | E2575 | CurrencyExchange | [CurrencyExchange](bc-6d0ca75e01a4ac88622b.md) |
| src-000345 | field-type | E2576 | YesNoIndicator | Not a component record in this worksheet |
| src-000345 | field-type | E2577 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000345 | field-type | E2578 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000345 | field-type | E2579 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000345 | field-type | E2580 | SafekeepingPlace | [SafekeepingPlace](bc-d7537dec2f3ab540e9a6.md) |
| src-000345 | field-type | E2581 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000345 | field-type | E2582 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000345 | field-type | E2583 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000345 | field-type | E2584 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E2585 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000348 | parent | C3890 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000348 | field-type | E3891 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E3892 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000348 | field-type | E3893 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000348 | field-type | E3894 | ShortLongCode | Not a component record in this worksheet |
| src-000348 | field-type | E3895 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000348 | field-type | E3896 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000348 | field-type | E3897 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000348 | field-type | E3898 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000348 | field-type | E3899 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000348 | field-type | E3900 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000348 | field-type | E3901 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000348 | field-type | E3902 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000348 | field-type | E3903 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000348 | field-type | E3904 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000348 | field-type | E3905 | YesNoIndicator | Not a component record in this worksheet |
| src-000348 | field-type | E3906 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000348 | field-type | E3907 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000348 | field-type | E3908 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000348 | field-type | E3909 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000348 | field-type | E3910 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000348 | field-type | E3911 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000348 | field-type | E3912 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000348 | field-type | E3913 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E3914 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000352 | parent | C3921 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000352 | field-type | E3922 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E3923 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000352 | field-type | E3924 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000352 | field-type | E3925 | ShortLongCode | Not a component record in this worksheet |
| src-000352 | field-type | E3926 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000352 | field-type | E3927 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000352 | field-type | E3928 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000352 | field-type | E3929 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000352 | field-type | E3930 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000352 | field-type | E3931 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000352 | field-type | E3932 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000352 | field-type | E3933 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000352 | field-type | E3934 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000352 | field-type | E3935 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000352 | field-type | E3936 | YesNoIndicator | Not a component record in this worksheet |
| src-000352 | field-type | E3937 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000352 | field-type | E3938 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000352 | field-type | E3939 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000352 | field-type | E3940 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000352 | field-type | E3941 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000352 | field-type | E3942 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000352 | field-type | E3943 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000352 | field-type | E3944 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E3945 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000355 | parent | C3829 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000355 | field-type | E3830 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E3831 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000355 | field-type | E3832 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000355 | field-type | E3833 | ShortLongCode | Not a component record in this worksheet |
| src-000355 | field-type | E3834 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000355 | field-type | E3835 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000355 | field-type | E3836 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000355 | field-type | E3837 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000355 | field-type | E3838 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000355 | field-type | E3839 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000355 | field-type | E3840 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000355 | field-type | E3841 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000355 | field-type | E3842 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000355 | field-type | E3843 | CurrencyExchange | [CurrencyExchange](bc-6d0ca75e01a4ac88622b.md) |
| src-000355 | field-type | E3844 | YesNoIndicator | Not a component record in this worksheet |
| src-000355 | field-type | E3845 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000355 | field-type | E3846 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000355 | field-type | E3847 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000355 | field-type | E3848 | SafekeepingPlace | [SafekeepingPlace](bc-d7537dec2f3ab540e9a6.md) |
| src-000355 | field-type | E3849 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000355 | field-type | E3850 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000355 | field-type | E3851 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000355 | field-type | E3852 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E3853 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000358 | parent | C2561 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000358 | field-type | E2562 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E2563 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000358 | field-type | E2564 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000358 | field-type | E2565 | ShortLongCode | Not a component record in this worksheet |
| src-000358 | field-type | E2566 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000358 | field-type | E2567 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000358 | field-type | E2568 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000358 | field-type | E2569 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000358 | field-type | E2570 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000358 | field-type | E2571 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000358 | field-type | E2572 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000358 | field-type | E2573 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000358 | field-type | E2574 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000358 | field-type | E2575 | CurrencyExchange | [CurrencyExchange](bc-6d0ca75e01a4ac88622b.md) |
| src-000358 | field-type | E2576 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E2577 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000358 | field-type | E2578 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000358 | field-type | E2579 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000358 | field-type | E2580 | SafekeepingPlace | [SafekeepingPlace](bc-d7537dec2f3ab540e9a6.md) |
| src-000358 | field-type | E2581 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000358 | field-type | E2582 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000358 | field-type | E2583 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000358 | field-type | E2584 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E2585 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000361 | parent | C2561 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000361 | field-type | E2562 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E2563 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000361 | field-type | E2564 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000361 | field-type | E2565 | ShortLongCode | Not a component record in this worksheet |
| src-000361 | field-type | E2566 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000361 | field-type | E2567 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000361 | field-type | E2568 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000361 | field-type | E2569 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000361 | field-type | E2570 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000361 | field-type | E2571 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000361 | field-type | E2572 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000361 | field-type | E2573 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000361 | field-type | E2574 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000361 | field-type | E2575 | CurrencyExchange | [CurrencyExchange](bc-6d0ca75e01a4ac88622b.md) |
| src-000361 | field-type | E2576 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E2577 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000361 | field-type | E2578 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000361 | field-type | E2579 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000361 | field-type | E2580 | SafekeepingPlace | [SafekeepingPlace](bc-d7537dec2f3ab540e9a6.md) |
| src-000361 | field-type | E2581 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000361 | field-type | E2582 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000361 | field-type | E2583 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000361 | field-type | E2584 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E2585 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000364 | parent | C3829 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000364 | field-type | E3830 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E3831 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000364 | field-type | E3832 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000364 | field-type | E3833 | ShortLongCode | Not a component record in this worksheet |
| src-000364 | field-type | E3834 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000364 | field-type | E3835 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000364 | field-type | E3836 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000364 | field-type | E3837 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000364 | field-type | E3838 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000364 | field-type | E3839 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000364 | field-type | E3840 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000364 | field-type | E3841 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000364 | field-type | E3842 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000364 | field-type | E3843 | CurrencyExchange | [CurrencyExchange](bc-6d0ca75e01a4ac88622b.md) |
| src-000364 | field-type | E3844 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E3845 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000364 | field-type | E3846 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000364 | field-type | E3847 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000364 | field-type | E3848 | SafekeepingPlace | [SafekeepingPlace](bc-d7537dec2f3ab540e9a6.md) |
| src-000364 | field-type | E3849 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000364 | field-type | E3850 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000364 | field-type | E3851 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000364 | field-type | E3852 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E3853 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000367 | parent | C3829 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000367 | field-type | E3830 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E3831 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000367 | field-type | E3832 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000367 | field-type | E3833 | ShortLongCode | Not a component record in this worksheet |
| src-000367 | field-type | E3834 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000367 | field-type | E3835 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000367 | field-type | E3836 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000367 | field-type | E3837 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000367 | field-type | E3838 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000367 | field-type | E3839 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000367 | field-type | E3840 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000367 | field-type | E3841 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000367 | field-type | E3842 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000367 | field-type | E3843 | CurrencyExchange | [CurrencyExchange](bc-6d0ca75e01a4ac88622b.md) |
| src-000367 | field-type | E3844 | YesNoIndicator | Not a component record in this worksheet |
| src-000367 | field-type | E3845 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000367 | field-type | E3846 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000367 | field-type | E3847 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000367 | field-type | E3848 | SafekeepingPlace | [SafekeepingPlace](bc-d7537dec2f3ab540e9a6.md) |
| src-000367 | field-type | E3849 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000367 | field-type | E3850 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000367 | field-type | E3851 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000367 | field-type | E3852 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E3853 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000370 | parent | C2561 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000370 | field-type | E2562 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E2563 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000370 | field-type | E2564 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000370 | field-type | E2565 | ShortLongCode | Not a component record in this worksheet |
| src-000370 | field-type | E2566 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000370 | field-type | E2567 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000370 | field-type | E2568 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000370 | field-type | E2569 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000370 | field-type | E2570 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000370 | field-type | E2571 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000370 | field-type | E2572 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000370 | field-type | E2573 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000370 | field-type | E2574 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000370 | field-type | E2575 | CurrencyExchange | [CurrencyExchange](bc-6d0ca75e01a4ac88622b.md) |
| src-000370 | field-type | E2576 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E2577 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000370 | field-type | E2578 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000370 | field-type | E2579 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000370 | field-type | E2580 | SafekeepingPlace | [SafekeepingPlace](bc-d7537dec2f3ab540e9a6.md) |
| src-000370 | field-type | E2581 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000370 | field-type | E2582 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000370 | field-type | E2583 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000370 | field-type | E2584 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E2585 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000373 | parent | C2561 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000373 | field-type | E2562 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E2563 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000373 | field-type | E2564 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000373 | field-type | E2565 | ShortLongCode | Not a component record in this worksheet |
| src-000373 | field-type | E2566 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000373 | field-type | E2567 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000373 | field-type | E2568 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000373 | field-type | E2569 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000373 | field-type | E2570 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000373 | field-type | E2571 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000373 | field-type | E2572 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000373 | field-type | E2573 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000373 | field-type | E2574 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000373 | field-type | E2575 | CurrencyExchange | [CurrencyExchange](bc-6d0ca75e01a4ac88622b.md) |
| src-000373 | field-type | E2576 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E2577 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000373 | field-type | E2578 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000373 | field-type | E2579 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000373 | field-type | E2580 | SafekeepingPlace | [SafekeepingPlace](bc-d7537dec2f3ab540e9a6.md) |
| src-000373 | field-type | E2581 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000373 | field-type | E2582 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000373 | field-type | E2583 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000373 | field-type | E2584 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E2585 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000376 | parent | C3921 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000376 | field-type | E3922 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E3923 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000376 | field-type | E3924 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000376 | field-type | E3925 | ShortLongCode | Not a component record in this worksheet |
| src-000376 | field-type | E3926 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000376 | field-type | E3927 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000376 | field-type | E3928 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000376 | field-type | E3929 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000376 | field-type | E3930 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000376 | field-type | E3931 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000376 | field-type | E3932 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000376 | field-type | E3933 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000376 | field-type | E3934 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000376 | field-type | E3935 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000376 | field-type | E3936 | YesNoIndicator | Not a component record in this worksheet |
| src-000376 | field-type | E3937 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000376 | field-type | E3938 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000376 | field-type | E3939 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000376 | field-type | E3940 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000376 | field-type | E3941 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000376 | field-type | E3942 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000376 | field-type | E3943 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000376 | field-type | E3944 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E3945 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000379 | parent | C2561 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000379 | field-type | E2562 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E2563 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000379 | field-type | E2564 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000379 | field-type | E2565 | ShortLongCode | Not a component record in this worksheet |
| src-000379 | field-type | E2566 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000379 | field-type | E2567 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000379 | field-type | E2568 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000379 | field-type | E2569 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000379 | field-type | E2570 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000379 | field-type | E2571 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000379 | field-type | E2572 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000379 | field-type | E2573 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000379 | field-type | E2574 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000379 | field-type | E2575 | CurrencyExchange | [CurrencyExchange](bc-6d0ca75e01a4ac88622b.md) |
| src-000379 | field-type | E2576 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E2577 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000379 | field-type | E2578 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000379 | field-type | E2579 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000379 | field-type | E2580 | SafekeepingPlace | [SafekeepingPlace](bc-d7537dec2f3ab540e9a6.md) |
| src-000379 | field-type | E2581 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000379 | field-type | E2582 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000379 | field-type | E2583 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000379 | field-type | E2584 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E2585 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |
| src-000382 | parent | C3890 | Balance | [Balance](bc-e26eac9ccf22d3001504.md) |
| src-000382 | field-type | E3891 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E3892 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000382 | field-type | E3893 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000382 | field-type | E3894 | ShortLongCode | Not a component record in this worksheet |
| src-000382 | field-type | E3895 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000382 | field-type | E3896 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000382 | field-type | E3897 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000382 | field-type | E3898 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000382 | field-type | E3899 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000382 | field-type | E3900 | SecuritiesBalance | [SecuritiesBalance](bc-be8dc03e8889f0ff1fc6.md) |
| src-000382 | field-type | E3901 | SecuritiesBalanceTypeV2Code | Not a component record in this worksheet |
| src-000382 | field-type | E3902 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000382 | field-type | E3903 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000382 | field-type | E3904 | CurrencyExchange | [CurrencyExchange](bc-34731f533c7e6210a4f1.md) |
| src-000382 | field-type | E3905 | YesNoIndicator | Not a component record in this worksheet |
| src-000382 | field-type | E3906 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000382 | field-type | E3907 | MeetingEntitlement | [MeetingEntitlement](bc-8d160a82dced798e6f0d.md) |
| src-000382 | field-type | E3908 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000382 | field-type | E3909 | SafekeepingPlace | [SafekeepingPlace](bc-894cef4becec0f8593f7.md) |
| src-000382 | field-type | E3910 | SecuritiesEntry | [SecuritiesEntry](bc-beb7a2225ae8ab2fb3e7.md) |
| src-000382 | field-type | E3911 | CorporateActionEntitlement | [CorporateActionEntitlement](bc-0bc0234d0219c7cbd309.md) |
| src-000382 | field-type | E3912 | IntraPositionTransfer | [IntraPositionTransfer](bc-74ad20ffa998ed7d03c6.md) |
| src-000382 | field-type | E3913 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E3914 | Pledgee | [Pledgee](bc-3d7538f0a6c837db03fa.md) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
