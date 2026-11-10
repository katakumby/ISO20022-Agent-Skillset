---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-08c5faaf30167bb67ecd"
title: "LineItem"
business_component_name: "LineItem"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A2577:F2598"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A2542:F2563"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A2577:F2598"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A2577:F2598"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A2577:F2598"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A2577:F2598"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A2577:F2598"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A2542:F2563"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A2577:F2598"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A2555:F2576"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A4165:F4186"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A2555:F2576"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A2577:F2598"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A2530:F2551"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A4165:F4186"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A4165:F4186"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A2530:F2551"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A2530:F2551"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A4165:F4186"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A4165:F4186"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A2577:F2598"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A4165:F4186"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A2555:F2576"]}]
content_sha256: "08c5faaf30167bb67ecdd4668ecf71737a5ee34d19ff97d7c06b204acd137b17"
parent_names: []
related_component_names: ["Adjustment", "Charges", "CurrencyAndAmount", "ISODateTime", "Invoice", "Max35Text", "Packaging", "Product", "ProductQuantity"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# LineItem

## Definition

Unit of information  showing the related  provision of products and/or services and monetary summations reported as a discrete line item.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LineItem | ∅ | ∅ | Unit of information  showing the related  provision of products and/or services and monetary summations reported as a discrete line item. | ∅ | ∅ |
| 2 | LineItem | FinancialAdjustment | ∅ | Modification on the value of goods and / or services taking into account discounts, allowances and charges. | Adjustment | RelatedLineItem |
| 3 | LineItem | LogisticsCharge | ∅ | Logistics service charge for this line item. | Charges | LogisticsChargeLineItem |
| 4 | LineItem | GrossAmount | ∅ | Monetary value of the line amount total being reported for this settlement. | CurrencyAndAmount | ∅ |
| 5 | LineItem | Identification | ∅ | Uniquely identifies a line item. | Max35Text | ∅ |
| 6 | LineItem | InvoicedProduct | ∅ | Specifies the product and the quantity for which an invoice is generated. | Product | LineItem |
| 7 | LineItem | NetWeight | ∅ | Net weight of the physical item which is invoiced. | ProductQuantity | NetWeightRelatedLineItem |
| 8 | LineItem | BilledQuantity | ∅ | Quantity billed for this line item. | ProductQuantity | BilledQuantityRelatedLineItem |
| 9 | LineItem | ChargeFreeQuantity | ∅ | Quantity that is free of charge for this line item. | ProductQuantity | ChargeFreeQuantityRelatedLineItem |
| 10 | LineItem | MeasureQuantityStartRelatedLineItem | ∅ | Line item for which a measure quantity end is specified. | ProductQuantity | MeasureQuantityStart |
| 11 | LineItem | MeasureQuantityEndRelatedLineItem | ∅ | Line item for which a measure quantity end is specified. | ProductQuantity | MeasureQuantityEnd |
| 12 | LineItem | MeasureDateTimeStart | ∅ | Date/time on which the clock time measure started for a line item. | ISODateTime | ∅ |
| 13 | LineItem | MeasureDateTimeEnd | ∅ | Date/time on which the clock time measure ended for a line item. | ISODateTime | ∅ |
| 14 | LineItem | Invoice | ∅ | Specifies the invoice in which the line item is included. | Invoice | LineItem |
| 15 | LineItem | NetAmount | ∅ | Total amount resulting from the gross amount plus freight charges, tax and plus/minus Adjustments. | CurrencyAndAmount | ∅ |
| 16 | LineItem | Packaging | ∅ | Physical packaging of the product. | Packaging | RelatedLineItem |
| 17 | LineItem | DeliveryDateTime | ∅ | Actual delivery date/time of the products and/or services for this line item. | ISODateTime | ∅ |
| 18 | LineItem | Charges | ∅ | Charges specified for this line item. | Charges | LineItem |
| 19 | LineItem | NetPriceCharge | ∅ | Allowance or charge applied to the net price. When the charge amount is added (credit) | Charges | NetPriceChargeLineItem |
| 20 | LineItem | GrossPriceQuantity | ∅ | Quantity and conversion factor on which the gross price is based for this line item product and/or service. | ProductQuantity | GrossPriceQuantityRelatedLineItem |
| 21 | LineItem | NetPriceQuantity | ∅ | Quantity and conversion factor on which the net price is based for this line item product and/or service. | ProductQuantity | NetPriceQuantityRelatedLineItem |
| 22 | LineItem | GrossWeight | ∅ | Gross weight of the physical item which is invoiced. | ProductQuantity | GrossWeightRelatedLineItem |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `08c5faaf30167bb67ecdd4668ecf71737a5ee34d19ff97d7c06b204acd137b17`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A2577:F2598 | 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A2542:F2563 | 2542, 2543, 2544, 2545, 2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A2577:F2598 | 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A2577:F2598 | 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A2577:F2598 | 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A2577:F2598 | 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A2577:F2598 | 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A2542:F2563 | 2542, 2543, 2544, 2545, 2546, 2547, 2548, 2549, 2550, 2551, 2552, 2553, 2554, 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A2577:F2598 | 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A2555:F2576 | 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A4165:F4186 | 4165, 4166, 4167, 4168, 4169, 4170, 4171, 4172, 4173, 4174, 4175, 4176, 4177, 4178, 4179, 4180, 4181, 4182, 4183, 4184, 4185, 4186 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A2555:F2576 | 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A2577:F2598 | 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A2530:F2551 | 2530, 2531, 2532, 2533, 2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543, 2544, 2545, 2546, 2547, 2548, 2549, 2550, 2551 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A4165:F4186 | 4165, 4166, 4167, 4168, 4169, 4170, 4171, 4172, 4173, 4174, 4175, 4176, 4177, 4178, 4179, 4180, 4181, 4182, 4183, 4184, 4185, 4186 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A4165:F4186 | 4165, 4166, 4167, 4168, 4169, 4170, 4171, 4172, 4173, 4174, 4175, 4176, 4177, 4178, 4179, 4180, 4181, 4182, 4183, 4184, 4185, 4186 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A2530:F2551 | 2530, 2531, 2532, 2533, 2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543, 2544, 2545, 2546, 2547, 2548, 2549, 2550, 2551 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A2530:F2551 | 2530, 2531, 2532, 2533, 2534, 2535, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2543, 2544, 2545, 2546, 2547, 2548, 2549, 2550, 2551 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A4165:F4186 | 4165, 4166, 4167, 4168, 4169, 4170, 4171, 4172, 4173, 4174, 4175, 4176, 4177, 4178, 4179, 4180, 4181, 4182, 4183, 4184, 4185, 4186 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A4165:F4186 | 4165, 4166, 4167, 4168, 4169, 4170, 4171, 4172, 4173, 4174, 4175, 4176, 4177, 4178, 4179, 4180, 4181, 4182, 4183, 4184, 4185, 4186 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A2577:F2598 | 2577, 2578, 2579, 2580, 2581, 2582, 2583, 2584, 2585, 2586, 2587, 2588, 2589, 2590, 2591, 2592, 2593, 2594, 2595, 2596, 2597, 2598 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A4165:F4186 | 4165, 4166, 4167, 4168, 4169, 4170, 4171, 4172, 4173, 4174, 4175, 4176, 4177, 4178, 4179, 4180, 4181, 4182, 4183, 4184, 4185, 4186 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A2555:F2576 | 2555, 2556, 2557, 2558, 2559, 2560, 2561, 2562, 2563, 2564, 2565, 2566, 2567, 2568, 2569, 2570, 2571, 2572, 2573, 2574, 2575, 2576 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | field-type | E2578 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000006 | field-type | E2579 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000006 | field-type | E2580 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E2581 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E2582 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000006 | field-type | E2583 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000006 | field-type | E2584 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000006 | field-type | E2585 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000006 | field-type | E2586 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000006 | field-type | E2587 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000006 | field-type | E2588 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E2589 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E2590 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000006 | field-type | E2591 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E2592 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000006 | field-type | E2593 | ISODateTime | Not a component record in this worksheet |
| src-000006 | field-type | E2594 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000006 | field-type | E2595 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000006 | field-type | E2596 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000006 | field-type | E2597 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000006 | field-type | E2598 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000016 | field-type | E2543 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000016 | field-type | E2544 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000016 | field-type | E2545 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E2546 | Max35Text | Not a component record in this worksheet |
| src-000016 | field-type | E2547 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000016 | field-type | E2548 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000016 | field-type | E2549 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000016 | field-type | E2550 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000016 | field-type | E2551 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000016 | field-type | E2552 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000016 | field-type | E2553 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E2554 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E2555 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000016 | field-type | E2556 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E2557 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000016 | field-type | E2558 | ISODateTime | Not a component record in this worksheet |
| src-000016 | field-type | E2559 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000016 | field-type | E2560 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000016 | field-type | E2561 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000016 | field-type | E2562 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000016 | field-type | E2563 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000054 | field-type | E2578 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000054 | field-type | E2579 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000054 | field-type | E2580 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E2581 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E2582 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000054 | field-type | E2583 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000054 | field-type | E2584 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000054 | field-type | E2585 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000054 | field-type | E2586 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000054 | field-type | E2587 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000054 | field-type | E2588 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E2589 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E2590 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000054 | field-type | E2591 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E2592 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000054 | field-type | E2593 | ISODateTime | Not a component record in this worksheet |
| src-000054 | field-type | E2594 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000054 | field-type | E2595 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000054 | field-type | E2596 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000054 | field-type | E2597 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000054 | field-type | E2598 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000081 | field-type | E2578 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000081 | field-type | E2579 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000081 | field-type | E2580 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E2581 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E2582 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000081 | field-type | E2583 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000081 | field-type | E2584 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000081 | field-type | E2585 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000081 | field-type | E2586 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000081 | field-type | E2587 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000081 | field-type | E2588 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E2589 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E2590 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000081 | field-type | E2591 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E2592 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000081 | field-type | E2593 | ISODateTime | Not a component record in this worksheet |
| src-000081 | field-type | E2594 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000081 | field-type | E2595 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000081 | field-type | E2596 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000081 | field-type | E2597 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000081 | field-type | E2598 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000097 | field-type | E2578 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000097 | field-type | E2579 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000097 | field-type | E2580 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E2581 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E2582 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000097 | field-type | E2583 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000097 | field-type | E2584 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000097 | field-type | E2585 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000097 | field-type | E2586 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000097 | field-type | E2587 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000097 | field-type | E2588 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E2589 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E2590 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000097 | field-type | E2591 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E2592 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000097 | field-type | E2593 | ISODateTime | Not a component record in this worksheet |
| src-000097 | field-type | E2594 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000097 | field-type | E2595 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000097 | field-type | E2596 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000097 | field-type | E2597 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000097 | field-type | E2598 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000164 | field-type | E2578 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000164 | field-type | E2579 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000164 | field-type | E2580 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E2581 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E2582 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000164 | field-type | E2583 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000164 | field-type | E2584 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000164 | field-type | E2585 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000164 | field-type | E2586 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000164 | field-type | E2587 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000164 | field-type | E2588 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E2589 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E2590 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000164 | field-type | E2591 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E2592 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000164 | field-type | E2593 | ISODateTime | Not a component record in this worksheet |
| src-000164 | field-type | E2594 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000164 | field-type | E2595 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000164 | field-type | E2596 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000164 | field-type | E2597 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000164 | field-type | E2598 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000175 | field-type | E2578 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000175 | field-type | E2579 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000175 | field-type | E2580 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E2581 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E2582 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000175 | field-type | E2583 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000175 | field-type | E2584 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000175 | field-type | E2585 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000175 | field-type | E2586 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000175 | field-type | E2587 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000175 | field-type | E2588 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E2589 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E2590 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000175 | field-type | E2591 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E2592 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000175 | field-type | E2593 | ISODateTime | Not a component record in this worksheet |
| src-000175 | field-type | E2594 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000175 | field-type | E2595 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000175 | field-type | E2596 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000175 | field-type | E2597 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000175 | field-type | E2598 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000182 | field-type | E2543 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000182 | field-type | E2544 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000182 | field-type | E2545 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E2546 | Max35Text | Not a component record in this worksheet |
| src-000182 | field-type | E2547 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000182 | field-type | E2548 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000182 | field-type | E2549 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000182 | field-type | E2550 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000182 | field-type | E2551 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000182 | field-type | E2552 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000182 | field-type | E2553 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E2554 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E2555 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000182 | field-type | E2556 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E2557 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000182 | field-type | E2558 | ISODateTime | Not a component record in this worksheet |
| src-000182 | field-type | E2559 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000182 | field-type | E2560 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000182 | field-type | E2561 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000182 | field-type | E2562 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000182 | field-type | E2563 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000198 | field-type | E2578 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000198 | field-type | E2579 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000198 | field-type | E2580 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E2581 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E2582 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000198 | field-type | E2583 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000198 | field-type | E2584 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000198 | field-type | E2585 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000198 | field-type | E2586 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000198 | field-type | E2587 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000198 | field-type | E2588 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E2589 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E2590 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000198 | field-type | E2591 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E2592 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000198 | field-type | E2593 | ISODateTime | Not a component record in this worksheet |
| src-000198 | field-type | E2594 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000198 | field-type | E2595 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000198 | field-type | E2596 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000198 | field-type | E2597 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000198 | field-type | E2598 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000322 | field-type | E2556 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000322 | field-type | E2557 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000322 | field-type | E2558 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E2559 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E2560 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000322 | field-type | E2561 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000322 | field-type | E2562 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000322 | field-type | E2563 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000322 | field-type | E2564 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000322 | field-type | E2565 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000322 | field-type | E2566 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E2567 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E2568 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000322 | field-type | E2569 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E2570 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000322 | field-type | E2571 | ISODateTime | Not a component record in this worksheet |
| src-000322 | field-type | E2572 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000322 | field-type | E2573 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000322 | field-type | E2574 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000322 | field-type | E2575 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000322 | field-type | E2576 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000345 | field-type | E4166 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000345 | field-type | E4167 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000345 | field-type | E4168 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E4169 | Max35Text | Not a component record in this worksheet |
| src-000345 | field-type | E4170 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000345 | field-type | E4171 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000345 | field-type | E4172 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000345 | field-type | E4173 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000345 | field-type | E4174 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000345 | field-type | E4175 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000345 | field-type | E4176 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E4177 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E4178 | Invoice | [Invoice](bc-486d470ade846a71a268.md) |
| src-000345 | field-type | E4179 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E4180 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000345 | field-type | E4181 | ISODateTime | Not a component record in this worksheet |
| src-000345 | field-type | E4182 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000345 | field-type | E4183 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000345 | field-type | E4184 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000345 | field-type | E4185 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000345 | field-type | E4186 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000348 | field-type | E2556 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000348 | field-type | E2557 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000348 | field-type | E2558 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E2559 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E2560 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000348 | field-type | E2561 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000348 | field-type | E2562 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000348 | field-type | E2563 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000348 | field-type | E2564 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000348 | field-type | E2565 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000348 | field-type | E2566 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E2567 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E2568 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000348 | field-type | E2569 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E2570 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000348 | field-type | E2571 | ISODateTime | Not a component record in this worksheet |
| src-000348 | field-type | E2572 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000348 | field-type | E2573 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000348 | field-type | E2574 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000348 | field-type | E2575 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000348 | field-type | E2576 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000352 | field-type | E2578 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000352 | field-type | E2579 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000352 | field-type | E2580 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E2581 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E2582 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000352 | field-type | E2583 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000352 | field-type | E2584 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000352 | field-type | E2585 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000352 | field-type | E2586 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000352 | field-type | E2587 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000352 | field-type | E2588 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E2589 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E2590 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000352 | field-type | E2591 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E2592 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000352 | field-type | E2593 | ISODateTime | Not a component record in this worksheet |
| src-000352 | field-type | E2594 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000352 | field-type | E2595 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000352 | field-type | E2596 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000352 | field-type | E2597 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000352 | field-type | E2598 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000355 | field-type | E2531 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000355 | field-type | E2532 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000355 | field-type | E2533 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E2534 | Max35Text | Not a component record in this worksheet |
| src-000355 | field-type | E2535 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000355 | field-type | E2536 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000355 | field-type | E2537 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000355 | field-type | E2538 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000355 | field-type | E2539 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000355 | field-type | E2540 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000355 | field-type | E2541 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E2542 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E2543 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000355 | field-type | E2544 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E2545 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000355 | field-type | E2546 | ISODateTime | Not a component record in this worksheet |
| src-000355 | field-type | E2547 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000355 | field-type | E2548 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000355 | field-type | E2549 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000355 | field-type | E2550 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000355 | field-type | E2551 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000358 | field-type | E4166 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000358 | field-type | E4167 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000358 | field-type | E4168 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E4169 | Max35Text | Not a component record in this worksheet |
| src-000358 | field-type | E4170 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000358 | field-type | E4171 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000358 | field-type | E4172 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000358 | field-type | E4173 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000358 | field-type | E4174 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000358 | field-type | E4175 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000358 | field-type | E4176 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E4177 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E4178 | Invoice | [Invoice](bc-486d470ade846a71a268.md) |
| src-000358 | field-type | E4179 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E4180 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000358 | field-type | E4181 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E4182 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000358 | field-type | E4183 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000358 | field-type | E4184 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000358 | field-type | E4185 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000358 | field-type | E4186 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000361 | field-type | E4166 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000361 | field-type | E4167 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000361 | field-type | E4168 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E4169 | Max35Text | Not a component record in this worksheet |
| src-000361 | field-type | E4170 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000361 | field-type | E4171 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000361 | field-type | E4172 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000361 | field-type | E4173 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000361 | field-type | E4174 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000361 | field-type | E4175 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000361 | field-type | E4176 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E4177 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E4178 | Invoice | [Invoice](bc-486d470ade846a71a268.md) |
| src-000361 | field-type | E4179 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E4180 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000361 | field-type | E4181 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E4182 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000361 | field-type | E4183 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000361 | field-type | E4184 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000361 | field-type | E4185 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000361 | field-type | E4186 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000364 | field-type | E2531 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000364 | field-type | E2532 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000364 | field-type | E2533 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E2534 | Max35Text | Not a component record in this worksheet |
| src-000364 | field-type | E2535 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000364 | field-type | E2536 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000364 | field-type | E2537 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000364 | field-type | E2538 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000364 | field-type | E2539 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000364 | field-type | E2540 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000364 | field-type | E2541 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E2542 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E2543 | Invoice | [Invoice](bc-486d470ade846a71a268.md) |
| src-000364 | field-type | E2544 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E2545 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000364 | field-type | E2546 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E2547 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000364 | field-type | E2548 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000364 | field-type | E2549 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000364 | field-type | E2550 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000364 | field-type | E2551 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000367 | field-type | E2531 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000367 | field-type | E2532 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000367 | field-type | E2533 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E2534 | Max35Text | Not a component record in this worksheet |
| src-000367 | field-type | E2535 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000367 | field-type | E2536 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000367 | field-type | E2537 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000367 | field-type | E2538 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000367 | field-type | E2539 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000367 | field-type | E2540 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000367 | field-type | E2541 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E2542 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E2543 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000367 | field-type | E2544 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E2545 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000367 | field-type | E2546 | ISODateTime | Not a component record in this worksheet |
| src-000367 | field-type | E2547 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000367 | field-type | E2548 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000367 | field-type | E2549 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000367 | field-type | E2550 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000367 | field-type | E2551 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000370 | field-type | E4166 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000370 | field-type | E4167 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000370 | field-type | E4168 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E4169 | Max35Text | Not a component record in this worksheet |
| src-000370 | field-type | E4170 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000370 | field-type | E4171 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000370 | field-type | E4172 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000370 | field-type | E4173 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000370 | field-type | E4174 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000370 | field-type | E4175 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000370 | field-type | E4176 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E4177 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E4178 | Invoice | [Invoice](bc-486d470ade846a71a268.md) |
| src-000370 | field-type | E4179 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E4180 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000370 | field-type | E4181 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E4182 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000370 | field-type | E4183 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000370 | field-type | E4184 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000370 | field-type | E4185 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000370 | field-type | E4186 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000373 | field-type | E4166 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000373 | field-type | E4167 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000373 | field-type | E4168 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E4169 | Max35Text | Not a component record in this worksheet |
| src-000373 | field-type | E4170 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000373 | field-type | E4171 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000373 | field-type | E4172 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000373 | field-type | E4173 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000373 | field-type | E4174 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000373 | field-type | E4175 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000373 | field-type | E4176 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E4177 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E4178 | Invoice | [Invoice](bc-486d470ade846a71a268.md) |
| src-000373 | field-type | E4179 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E4180 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000373 | field-type | E4181 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E4182 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000373 | field-type | E4183 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000373 | field-type | E4184 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000373 | field-type | E4185 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000373 | field-type | E4186 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000376 | field-type | E2578 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000376 | field-type | E2579 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000376 | field-type | E2580 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E2581 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E2582 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000376 | field-type | E2583 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000376 | field-type | E2584 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000376 | field-type | E2585 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000376 | field-type | E2586 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000376 | field-type | E2587 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000376 | field-type | E2588 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E2589 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E2590 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000376 | field-type | E2591 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E2592 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000376 | field-type | E2593 | ISODateTime | Not a component record in this worksheet |
| src-000376 | field-type | E2594 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000376 | field-type | E2595 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000376 | field-type | E2596 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000376 | field-type | E2597 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000376 | field-type | E2598 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000379 | field-type | E4166 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000379 | field-type | E4167 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000379 | field-type | E4168 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E4169 | Max35Text | Not a component record in this worksheet |
| src-000379 | field-type | E4170 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000379 | field-type | E4171 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000379 | field-type | E4172 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000379 | field-type | E4173 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000379 | field-type | E4174 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000379 | field-type | E4175 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000379 | field-type | E4176 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E4177 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E4178 | Invoice | [Invoice](bc-486d470ade846a71a268.md) |
| src-000379 | field-type | E4179 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E4180 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000379 | field-type | E4181 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E4182 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000379 | field-type | E4183 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000379 | field-type | E4184 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000379 | field-type | E4185 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000379 | field-type | E4186 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000382 | field-type | E2556 | Adjustment | [Adjustment](bc-04aa963ac0863527945c.md) |
| src-000382 | field-type | E2557 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000382 | field-type | E2558 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E2559 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E2560 | Product | [Product](bc-86182b694045b095a4e3.md) |
| src-000382 | field-type | E2561 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000382 | field-type | E2562 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000382 | field-type | E2563 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000382 | field-type | E2564 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000382 | field-type | E2565 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000382 | field-type | E2566 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E2567 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E2568 | Invoice | [Invoice](bc-58d9698dd014ab423e8e.md) |
| src-000382 | field-type | E2569 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E2570 | Packaging | [Packaging](bc-4cbfebacfb7c7d4bfb7d.md) |
| src-000382 | field-type | E2571 | ISODateTime | Not a component record in this worksheet |
| src-000382 | field-type | E2572 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000382 | field-type | E2573 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000382 | field-type | E2574 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000382 | field-type | E2575 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |
| src-000382 | field-type | E2576 | ProductQuantity | [ProductQuantity](bc-3e7f06eb80c28bb3545a.md) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
