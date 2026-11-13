---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-a201cdfff93bef35735d"
title: "Allocation"
business_component_name: "Allocation"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A179:F191"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A179:F191"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A3120:F3132"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A179:F191"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A3120:F3132"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A3120:F3132"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A179:F191"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A179:F191"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A3120:F3132"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A3120:F3132"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A3120:F3132"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A190:F202"]}]
content_sha256: "a201cdfff93bef35735da931e56ac196ac95c02130c4b173784a4c62bf84a16a"
parent_names: []
related_component_names: ["CurrencyAndAmount", "CurrencyCode", "DecimalNumber", "Max35Text", "PercentageRate", "RoundingDirectionCode", "SecuritiesAccount", "SecuritiesOrder", "SecuritiesPricing", "SecuritiesQuantity", "SecuritiesSettlement", "SecuritiesTrade"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# Allocation

## Definition

Distribution of the (block) trade (transactions) by the investor or investment manager to different underlying clients, ie, investment funds.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Allocation | ∅ | ∅ | Distribution of the (block) trade (transactions) by the investor or investment manager to different underlying clients, ie, investment funds. | ∅ | ∅ |
| 2 | Allocation | Percentage | ∅ | Percent of the securities quantity that this allocation represents. | PercentageRate | ∅ |
| 3 | Allocation | AllocatedQuantity | ∅ | Quantity of a specific security allocated from a block trade, based upon the distribution of the trade to different accounts. | SecuritiesQuantity | Allocation |
| 4 | Allocation | SettlementCurrency | ∅ | Currency to be used for settlement of the allocation. | CurrencyCode | ∅ |
| 5 | Allocation | AllocationAccount | ∅ | Account to or from which an allocation must be made. | SecuritiesAccount | RelatedAllocation |
| 6 | Allocation | AllocatedPrice | ∅ | Executed price used in an allocation. | SecuritiesPricing | Allocation |
| 7 | Allocation | AllocationAmount | ∅ | Allocated quantity of security multiplied by the allocated price. | CurrencyAndAmount | ∅ |
| 8 | Allocation | Method | ∅ | Indicates the method of pre-allocation, that is the factors that are/were applied in the pre-allocation process. | RoundingDirectionCode | ∅ |
| 9 | Allocation | AveragePricePrecision | ∅ | Number of decimal places used for average pricing. | DecimalNumber | ∅ |
| 10 | Allocation | SettlementExecutionParameters | ∅ | Parameters used to execute the settlement of a securities allocation. | SecuritiesSettlement | SettledAllocation |
| 11 | Allocation | SecuritiesOrder | ∅ | Securites order which is allocated. | SecuritiesOrder | SecuritiesOrderAllocation |
| 12 | Allocation | SecuritiesTrade | ∅ | Trade which is allocated. | SecuritiesTrade | TradeAllocation |
| 13 | Allocation | Identification | ∅ | Identifies the allocation. | Max35Text | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `a201cdfff93bef35735da931e56ac196ac95c02130c4b173784a4c62bf84a16a`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A179:F191 | 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A179:F191 | 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A3120:F3132 | 3120, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130, 3131, 3132 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A179:F191 | 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A3120:F3132 | 3120, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130, 3131, 3132 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A3120:F3132 | 3120, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130, 3131, 3132 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A179:F191 | 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A179:F191 | 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A3120:F3132 | 3120, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130, 3131, 3132 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A3120:F3132 | 3120, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130, 3131, 3132 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A3120:F3132 | 3120, 3121, 3122, 3123, 3124, 3125, 3126, 3127, 3128, 3129, 3130, 3131, 3132 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A190:F202 | 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000006 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000006 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000006 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000006 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000006 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000006 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000006 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000006 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000006 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E180 | PercentageRate | Not a component record in this worksheet |
| src-000016 | field-type | E181 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000016 | field-type | E182 | CurrencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E183 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000016 | field-type | E184 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000016 | field-type | E185 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E186 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000016 | field-type | E187 | DecimalNumber | Not a component record in this worksheet |
| src-000016 | field-type | E188 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000016 | field-type | E189 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000016 | field-type | E190 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000016 | field-type | E191 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000054 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000054 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000054 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000054 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000054 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000054 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000054 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000054 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000054 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000081 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000081 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000081 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000081 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000081 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000081 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000081 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000081 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000081 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000097 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000097 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000097 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000097 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000097 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000097 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000097 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000097 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000097 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000164 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000164 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000164 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000164 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000164 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000164 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000164 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000164 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000164 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000175 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000175 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000175 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000175 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000175 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000175 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000175 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000175 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000175 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E180 | PercentageRate | Not a component record in this worksheet |
| src-000182 | field-type | E181 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000182 | field-type | E182 | CurrencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E183 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000182 | field-type | E184 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000182 | field-type | E185 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E186 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000182 | field-type | E187 | DecimalNumber | Not a component record in this worksheet |
| src-000182 | field-type | E188 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000182 | field-type | E189 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000182 | field-type | E190 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000182 | field-type | E191 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000198 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000198 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000198 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000198 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000198 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000198 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000198 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000198 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000198 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000322 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000322 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000322 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000322 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000322 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000322 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000322 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000322 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000322 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E3121 | PercentageRate | Not a component record in this worksheet |
| src-000345 | field-type | E3122 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000345 | field-type | E3123 | CurrencyCode | Not a component record in this worksheet |
| src-000345 | field-type | E3124 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000345 | field-type | E3125 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000345 | field-type | E3126 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E3127 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000345 | field-type | E3128 | DecimalNumber | Not a component record in this worksheet |
| src-000345 | field-type | E3129 | SecuritiesSettlement | [SecuritiesSettlement](bc-18ee94584decdbdc6961.md) |
| src-000345 | field-type | E3130 | SecuritiesOrder | [SecuritiesOrder](bc-e970e1551622c18cea65.md) |
| src-000345 | field-type | E3131 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000345 | field-type | E3132 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000348 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000348 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000348 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000348 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000348 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000348 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000348 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000348 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000348 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000352 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000352 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000352 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000352 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000352 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000352 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000352 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000352 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000352 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E180 | PercentageRate | Not a component record in this worksheet |
| src-000355 | field-type | E181 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000355 | field-type | E182 | CurrencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E183 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000355 | field-type | E184 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000355 | field-type | E185 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E186 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000355 | field-type | E187 | DecimalNumber | Not a component record in this worksheet |
| src-000355 | field-type | E188 | SecuritiesSettlement | [SecuritiesSettlement](bc-18ee94584decdbdc6961.md) |
| src-000355 | field-type | E189 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000355 | field-type | E190 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000355 | field-type | E191 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E3121 | PercentageRate | Not a component record in this worksheet |
| src-000358 | field-type | E3122 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000358 | field-type | E3123 | CurrencyCode | Not a component record in this worksheet |
| src-000358 | field-type | E3124 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000358 | field-type | E3125 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000358 | field-type | E3126 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E3127 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000358 | field-type | E3128 | DecimalNumber | Not a component record in this worksheet |
| src-000358 | field-type | E3129 | SecuritiesSettlement | [SecuritiesSettlement](bc-18ee94584decdbdc6961.md) |
| src-000358 | field-type | E3130 | SecuritiesOrder | [SecuritiesOrder](bc-e970e1551622c18cea65.md) |
| src-000358 | field-type | E3131 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000358 | field-type | E3132 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E3121 | PercentageRate | Not a component record in this worksheet |
| src-000361 | field-type | E3122 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000361 | field-type | E3123 | CurrencyCode | Not a component record in this worksheet |
| src-000361 | field-type | E3124 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000361 | field-type | E3125 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000361 | field-type | E3126 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E3127 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000361 | field-type | E3128 | DecimalNumber | Not a component record in this worksheet |
| src-000361 | field-type | E3129 | SecuritiesSettlement | [SecuritiesSettlement](bc-18ee94584decdbdc6961.md) |
| src-000361 | field-type | E3130 | SecuritiesOrder | [SecuritiesOrder](bc-e970e1551622c18cea65.md) |
| src-000361 | field-type | E3131 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000361 | field-type | E3132 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E180 | PercentageRate | Not a component record in this worksheet |
| src-000364 | field-type | E181 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000364 | field-type | E182 | CurrencyCode | Not a component record in this worksheet |
| src-000364 | field-type | E183 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000364 | field-type | E184 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000364 | field-type | E185 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E186 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000364 | field-type | E187 | DecimalNumber | Not a component record in this worksheet |
| src-000364 | field-type | E188 | SecuritiesSettlement | [SecuritiesSettlement](bc-18ee94584decdbdc6961.md) |
| src-000364 | field-type | E189 | SecuritiesOrder | [SecuritiesOrder](bc-e970e1551622c18cea65.md) |
| src-000364 | field-type | E190 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000364 | field-type | E191 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E180 | PercentageRate | Not a component record in this worksheet |
| src-000367 | field-type | E181 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000367 | field-type | E182 | CurrencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E183 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000367 | field-type | E184 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000367 | field-type | E185 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E186 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000367 | field-type | E187 | DecimalNumber | Not a component record in this worksheet |
| src-000367 | field-type | E188 | SecuritiesSettlement | [SecuritiesSettlement](bc-18ee94584decdbdc6961.md) |
| src-000367 | field-type | E189 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000367 | field-type | E190 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000367 | field-type | E191 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E3121 | PercentageRate | Not a component record in this worksheet |
| src-000370 | field-type | E3122 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000370 | field-type | E3123 | CurrencyCode | Not a component record in this worksheet |
| src-000370 | field-type | E3124 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000370 | field-type | E3125 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000370 | field-type | E3126 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E3127 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000370 | field-type | E3128 | DecimalNumber | Not a component record in this worksheet |
| src-000370 | field-type | E3129 | SecuritiesSettlement | [SecuritiesSettlement](bc-18ee94584decdbdc6961.md) |
| src-000370 | field-type | E3130 | SecuritiesOrder | [SecuritiesOrder](bc-e970e1551622c18cea65.md) |
| src-000370 | field-type | E3131 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000370 | field-type | E3132 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E3121 | PercentageRate | Not a component record in this worksheet |
| src-000373 | field-type | E3122 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000373 | field-type | E3123 | CurrencyCode | Not a component record in this worksheet |
| src-000373 | field-type | E3124 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000373 | field-type | E3125 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000373 | field-type | E3126 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E3127 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000373 | field-type | E3128 | DecimalNumber | Not a component record in this worksheet |
| src-000373 | field-type | E3129 | SecuritiesSettlement | [SecuritiesSettlement](bc-18ee94584decdbdc6961.md) |
| src-000373 | field-type | E3130 | SecuritiesOrder | [SecuritiesOrder](bc-e970e1551622c18cea65.md) |
| src-000373 | field-type | E3131 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000373 | field-type | E3132 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000376 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000376 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000376 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000376 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000376 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000376 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000376 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000376 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000376 | field-type | E202 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E3121 | PercentageRate | Not a component record in this worksheet |
| src-000379 | field-type | E3122 | SecuritiesQuantity | [SecuritiesQuantity](bc-8cbba10ca914faa6cd02.md) |
| src-000379 | field-type | E3123 | CurrencyCode | Not a component record in this worksheet |
| src-000379 | field-type | E3124 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000379 | field-type | E3125 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000379 | field-type | E3126 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E3127 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000379 | field-type | E3128 | DecimalNumber | Not a component record in this worksheet |
| src-000379 | field-type | E3129 | SecuritiesSettlement | [SecuritiesSettlement](bc-18ee94584decdbdc6961.md) |
| src-000379 | field-type | E3130 | SecuritiesOrder | [SecuritiesOrder](bc-e970e1551622c18cea65.md) |
| src-000379 | field-type | E3131 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000379 | field-type | E3132 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E191 | PercentageRate | Not a component record in this worksheet |
| src-000382 | field-type | E192 | SecuritiesQuantity | [SecuritiesQuantity](bc-eb3fa0c6a18cb359935a.md) |
| src-000382 | field-type | E193 | CurrencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E194 | SecuritiesAccount | [SecuritiesAccount](bc-2ec6ceb3eba4a954f1a0.md) |
| src-000382 | field-type | E195 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000382 | field-type | E196 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E197 | RoundingDirectionCode | Not a component record in this worksheet |
| src-000382 | field-type | E198 | DecimalNumber | Not a component record in this worksheet |
| src-000382 | field-type | E199 | SecuritiesSettlement | [SecuritiesSettlement](bc-1944a7a14593dde46384.md) |
| src-000382 | field-type | E200 | SecuritiesOrder | [SecuritiesOrder](bc-c938575f0889cb96215f.md) |
| src-000382 | field-type | E201 | SecuritiesTrade | [SecuritiesTrade](bc-cacdabc7b3d47e9b7b24.md) |
| src-000382 | field-type | E202 | Max35Text | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
