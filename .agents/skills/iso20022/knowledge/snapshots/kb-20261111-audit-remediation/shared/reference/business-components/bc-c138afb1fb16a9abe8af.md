---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-c138afb1fb16a9abe8af"
title: "InsuranceCertificate"
business_component_name: "InsuranceCertificate"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A2119:F2129"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A2084:F2094"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A2119:F2129"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A2119:F2129"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A2119:F2129"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A2119:F2129"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A2119:F2129"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A2084:F2094"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A2119:F2129"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A2097:F2107"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A1544:F1554"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A2097:F2107"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A2119:F2129"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A2072:F2082"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A1544:F1554"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A1544:F1554"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A2072:F2082"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A2072:F2082"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A1544:F1554"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A1544:F1554"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A2119:F2129"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A1544:F1554"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A2097:F2107"]}]
content_sha256: "c138afb1fb16a9abe8aff153f64bbf9b5dea8ddbe1862f018f40598263365b20"
parent_names: ["Document"]
related_component_names: ["CurrencyAndAmount", "CurrencyCode", "ISODate", "InsuranceClausesCode", "InsuranceCode", "InsurancePartyRole", "InvestmentPlan", "Location", "Max350Text", "ProductDelivery"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# InsuranceCertificate

## Definition

Formal document used to record a fact and used as proof of the fact that goods have been insured under an insurance policy.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | InsuranceCertificate | ∅ | Document | Formal document used to record a fact and used as proof of the fact that goods have been insured under an insurance policy. | ∅ | ∅ |
| 2 | InsuranceCertificate | EffectiveDate | ∅ | Date upon which cover under an insurance policy becomes effective. | ISODate | ∅ |
| 3 | InsuranceCertificate | InsuredAmount | ∅ | Value of the goods as insured under the insurance policy. | CurrencyAndAmount | ∅ |
| 4 | InsuranceCertificate | InsuranceConditions | ∅ | Description of the conditions and exclusion clauses under which insurance is granted. | Max350Text | ∅ |
| 5 | InsuranceCertificate | InsuranceClauses | ∅ | Standard insurance clauses defined by the Institute of London Underwriters (or the American Institute of marine Underwriters). | InsuranceClausesCode | ∅ |
| 6 | InsuranceCertificate | ClaimsPayableAt | ∅ | Place where claims under the insurance policy will be paid. | Location | InsuranceCertificate |
| 7 | InsuranceCertificate | ClaimsPayableIn | ∅ | Currency in which claims, if valid, will be paid. | CurrencyCode | ∅ |
| 8 | InsuranceCertificate | InsurancePartyRole | ∅ | Role played by a party in the context of insurance. | InsurancePartyRole | InsuranceCertificate |
| 9 | InsuranceCertificate | ProductDelivery | ∅ | Delivery parameters of a trade. | ProductDelivery | InsuranceCertificate |
| 10 | InsuranceCertificate | InsuranceType | ∅ | Specifies the type of insurance. | InsuranceCode | ∅ |
| 11 | InsuranceCertificate | RelatedInvestmentPlan | ∅ | Investment plan covered by an insurance contract. | InvestmentPlan | Insurance |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `c138afb1fb16a9abe8aff153f64bbf9b5dea8ddbe1862f018f40598263365b20`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A2119:F2129 | 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A2084:F2094 | 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A2119:F2129 | 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A2119:F2129 | 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A2119:F2129 | 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A2119:F2129 | 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A2119:F2129 | 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A2084:F2094 | 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A2119:F2129 | 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A2097:F2107 | 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A1544:F1554 | 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A2097:F2107 | 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A2119:F2129 | 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A2072:F2082 | 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A1544:F1554 | 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A1544:F1554 | 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A2072:F2082 | 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A2072:F2082 | 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A1544:F1554 | 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A1544:F1554 | 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A2119:F2129 | 2119, 2120, 2121, 2122, 2123, 2124, 2125, 2126, 2127, 2128, 2129 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A1544:F1554 | 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551, 1552, 1553, 1554 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A2097:F2107 | 2097, 2098, 2099, 2100, 2101, 2102, 2103, 2104, 2105, 2106, 2107 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C2119 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000006 | field-type | E2120 | ISODate | Not a component record in this worksheet |
| src-000006 | field-type | E2121 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E2122 | Max350Text | Not a component record in this worksheet |
| src-000006 | field-type | E2123 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000006 | field-type | E2124 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000006 | field-type | E2125 | CurrencyCode | Not a component record in this worksheet |
| src-000006 | field-type | E2126 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000006 | field-type | E2127 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000006 | field-type | E2128 | InsuranceCode | Not a component record in this worksheet |
| src-000006 | field-type | E2129 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000016 | parent | C2084 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000016 | field-type | E2085 | ISODate | Not a component record in this worksheet |
| src-000016 | field-type | E2086 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E2087 | Max350Text | Not a component record in this worksheet |
| src-000016 | field-type | E2088 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000016 | field-type | E2089 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000016 | field-type | E2090 | CurrencyCode | Not a component record in this worksheet |
| src-000016 | field-type | E2091 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000016 | field-type | E2092 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000016 | field-type | E2093 | InsuranceCode | Not a component record in this worksheet |
| src-000016 | field-type | E2094 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000054 | parent | C2119 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000054 | field-type | E2120 | ISODate | Not a component record in this worksheet |
| src-000054 | field-type | E2121 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E2122 | Max350Text | Not a component record in this worksheet |
| src-000054 | field-type | E2123 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000054 | field-type | E2124 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000054 | field-type | E2125 | CurrencyCode | Not a component record in this worksheet |
| src-000054 | field-type | E2126 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000054 | field-type | E2127 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000054 | field-type | E2128 | InsuranceCode | Not a component record in this worksheet |
| src-000054 | field-type | E2129 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000081 | parent | C2119 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000081 | field-type | E2120 | ISODate | Not a component record in this worksheet |
| src-000081 | field-type | E2121 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E2122 | Max350Text | Not a component record in this worksheet |
| src-000081 | field-type | E2123 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000081 | field-type | E2124 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000081 | field-type | E2125 | CurrencyCode | Not a component record in this worksheet |
| src-000081 | field-type | E2126 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000081 | field-type | E2127 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000081 | field-type | E2128 | InsuranceCode | Not a component record in this worksheet |
| src-000081 | field-type | E2129 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000097 | parent | C2119 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000097 | field-type | E2120 | ISODate | Not a component record in this worksheet |
| src-000097 | field-type | E2121 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E2122 | Max350Text | Not a component record in this worksheet |
| src-000097 | field-type | E2123 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000097 | field-type | E2124 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000097 | field-type | E2125 | CurrencyCode | Not a component record in this worksheet |
| src-000097 | field-type | E2126 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000097 | field-type | E2127 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000097 | field-type | E2128 | InsuranceCode | Not a component record in this worksheet |
| src-000097 | field-type | E2129 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000164 | parent | C2119 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000164 | field-type | E2120 | ISODate | Not a component record in this worksheet |
| src-000164 | field-type | E2121 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E2122 | Max350Text | Not a component record in this worksheet |
| src-000164 | field-type | E2123 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000164 | field-type | E2124 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000164 | field-type | E2125 | CurrencyCode | Not a component record in this worksheet |
| src-000164 | field-type | E2126 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000164 | field-type | E2127 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000164 | field-type | E2128 | InsuranceCode | Not a component record in this worksheet |
| src-000164 | field-type | E2129 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000175 | parent | C2119 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000175 | field-type | E2120 | ISODate | Not a component record in this worksheet |
| src-000175 | field-type | E2121 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E2122 | Max350Text | Not a component record in this worksheet |
| src-000175 | field-type | E2123 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000175 | field-type | E2124 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000175 | field-type | E2125 | CurrencyCode | Not a component record in this worksheet |
| src-000175 | field-type | E2126 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000175 | field-type | E2127 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000175 | field-type | E2128 | InsuranceCode | Not a component record in this worksheet |
| src-000175 | field-type | E2129 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000182 | parent | C2084 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000182 | field-type | E2085 | ISODate | Not a component record in this worksheet |
| src-000182 | field-type | E2086 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E2087 | Max350Text | Not a component record in this worksheet |
| src-000182 | field-type | E2088 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000182 | field-type | E2089 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000182 | field-type | E2090 | CurrencyCode | Not a component record in this worksheet |
| src-000182 | field-type | E2091 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000182 | field-type | E2092 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000182 | field-type | E2093 | InsuranceCode | Not a component record in this worksheet |
| src-000182 | field-type | E2094 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000198 | parent | C2119 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000198 | field-type | E2120 | ISODate | Not a component record in this worksheet |
| src-000198 | field-type | E2121 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E2122 | Max350Text | Not a component record in this worksheet |
| src-000198 | field-type | E2123 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000198 | field-type | E2124 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000198 | field-type | E2125 | CurrencyCode | Not a component record in this worksheet |
| src-000198 | field-type | E2126 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000198 | field-type | E2127 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000198 | field-type | E2128 | InsuranceCode | Not a component record in this worksheet |
| src-000198 | field-type | E2129 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000322 | parent | C2097 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000322 | field-type | E2098 | ISODate | Not a component record in this worksheet |
| src-000322 | field-type | E2099 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E2100 | Max350Text | Not a component record in this worksheet |
| src-000322 | field-type | E2101 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000322 | field-type | E2102 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000322 | field-type | E2103 | CurrencyCode | Not a component record in this worksheet |
| src-000322 | field-type | E2104 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000322 | field-type | E2105 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000322 | field-type | E2106 | InsuranceCode | Not a component record in this worksheet |
| src-000322 | field-type | E2107 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000345 | parent | C1544 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000345 | field-type | E1545 | ISODate | Not a component record in this worksheet |
| src-000345 | field-type | E1546 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E1547 | Max350Text | Not a component record in this worksheet |
| src-000345 | field-type | E1548 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000345 | field-type | E1549 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000345 | field-type | E1550 | CurrencyCode | Not a component record in this worksheet |
| src-000345 | field-type | E1551 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000345 | field-type | E1552 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000345 | field-type | E1553 | InsuranceCode | Not a component record in this worksheet |
| src-000345 | field-type | E1554 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000348 | parent | C2097 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000348 | field-type | E2098 | ISODate | Not a component record in this worksheet |
| src-000348 | field-type | E2099 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E2100 | Max350Text | Not a component record in this worksheet |
| src-000348 | field-type | E2101 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000348 | field-type | E2102 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000348 | field-type | E2103 | CurrencyCode | Not a component record in this worksheet |
| src-000348 | field-type | E2104 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000348 | field-type | E2105 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000348 | field-type | E2106 | InsuranceCode | Not a component record in this worksheet |
| src-000348 | field-type | E2107 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000352 | parent | C2119 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000352 | field-type | E2120 | ISODate | Not a component record in this worksheet |
| src-000352 | field-type | E2121 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E2122 | Max350Text | Not a component record in this worksheet |
| src-000352 | field-type | E2123 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000352 | field-type | E2124 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000352 | field-type | E2125 | CurrencyCode | Not a component record in this worksheet |
| src-000352 | field-type | E2126 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000352 | field-type | E2127 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000352 | field-type | E2128 | InsuranceCode | Not a component record in this worksheet |
| src-000352 | field-type | E2129 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000355 | parent | C2072 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000355 | field-type | E2073 | ISODate | Not a component record in this worksheet |
| src-000355 | field-type | E2074 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E2075 | Max350Text | Not a component record in this worksheet |
| src-000355 | field-type | E2076 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000355 | field-type | E2077 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000355 | field-type | E2078 | CurrencyCode | Not a component record in this worksheet |
| src-000355 | field-type | E2079 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000355 | field-type | E2080 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000355 | field-type | E2081 | InsuranceCode | Not a component record in this worksheet |
| src-000355 | field-type | E2082 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000358 | parent | C1544 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000358 | field-type | E1545 | ISODate | Not a component record in this worksheet |
| src-000358 | field-type | E1546 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E1547 | Max350Text | Not a component record in this worksheet |
| src-000358 | field-type | E1548 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000358 | field-type | E1549 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000358 | field-type | E1550 | CurrencyCode | Not a component record in this worksheet |
| src-000358 | field-type | E1551 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000358 | field-type | E1552 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000358 | field-type | E1553 | InsuranceCode | Not a component record in this worksheet |
| src-000358 | field-type | E1554 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000361 | parent | C1544 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000361 | field-type | E1545 | ISODate | Not a component record in this worksheet |
| src-000361 | field-type | E1546 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E1547 | Max350Text | Not a component record in this worksheet |
| src-000361 | field-type | E1548 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000361 | field-type | E1549 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000361 | field-type | E1550 | CurrencyCode | Not a component record in this worksheet |
| src-000361 | field-type | E1551 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000361 | field-type | E1552 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000361 | field-type | E1553 | InsuranceCode | Not a component record in this worksheet |
| src-000361 | field-type | E1554 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000364 | parent | C2072 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000364 | field-type | E2073 | ISODate | Not a component record in this worksheet |
| src-000364 | field-type | E2074 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E2075 | Max350Text | Not a component record in this worksheet |
| src-000364 | field-type | E2076 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000364 | field-type | E2077 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000364 | field-type | E2078 | CurrencyCode | Not a component record in this worksheet |
| src-000364 | field-type | E2079 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000364 | field-type | E2080 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000364 | field-type | E2081 | InsuranceCode | Not a component record in this worksheet |
| src-000364 | field-type | E2082 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000367 | parent | C2072 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000367 | field-type | E2073 | ISODate | Not a component record in this worksheet |
| src-000367 | field-type | E2074 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E2075 | Max350Text | Not a component record in this worksheet |
| src-000367 | field-type | E2076 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000367 | field-type | E2077 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000367 | field-type | E2078 | CurrencyCode | Not a component record in this worksheet |
| src-000367 | field-type | E2079 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000367 | field-type | E2080 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000367 | field-type | E2081 | InsuranceCode | Not a component record in this worksheet |
| src-000367 | field-type | E2082 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000370 | parent | C1544 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000370 | field-type | E1545 | ISODate | Not a component record in this worksheet |
| src-000370 | field-type | E1546 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E1547 | Max350Text | Not a component record in this worksheet |
| src-000370 | field-type | E1548 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000370 | field-type | E1549 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000370 | field-type | E1550 | CurrencyCode | Not a component record in this worksheet |
| src-000370 | field-type | E1551 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000370 | field-type | E1552 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000370 | field-type | E1553 | InsuranceCode | Not a component record in this worksheet |
| src-000370 | field-type | E1554 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000373 | parent | C1544 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000373 | field-type | E1545 | ISODate | Not a component record in this worksheet |
| src-000373 | field-type | E1546 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E1547 | Max350Text | Not a component record in this worksheet |
| src-000373 | field-type | E1548 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000373 | field-type | E1549 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000373 | field-type | E1550 | CurrencyCode | Not a component record in this worksheet |
| src-000373 | field-type | E1551 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000373 | field-type | E1552 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000373 | field-type | E1553 | InsuranceCode | Not a component record in this worksheet |
| src-000373 | field-type | E1554 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000376 | parent | C2119 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000376 | field-type | E2120 | ISODate | Not a component record in this worksheet |
| src-000376 | field-type | E2121 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E2122 | Max350Text | Not a component record in this worksheet |
| src-000376 | field-type | E2123 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000376 | field-type | E2124 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000376 | field-type | E2125 | CurrencyCode | Not a component record in this worksheet |
| src-000376 | field-type | E2126 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000376 | field-type | E2127 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000376 | field-type | E2128 | InsuranceCode | Not a component record in this worksheet |
| src-000376 | field-type | E2129 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000379 | parent | C1544 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000379 | field-type | E1545 | ISODate | Not a component record in this worksheet |
| src-000379 | field-type | E1546 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E1547 | Max350Text | Not a component record in this worksheet |
| src-000379 | field-type | E1548 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000379 | field-type | E1549 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000379 | field-type | E1550 | CurrencyCode | Not a component record in this worksheet |
| src-000379 | field-type | E1551 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000379 | field-type | E1552 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000379 | field-type | E1553 | InsuranceCode | Not a component record in this worksheet |
| src-000379 | field-type | E1554 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000382 | parent | C2097 | Document | [Document](bc-9bb15a8768bf14afb330.md) |
| src-000382 | field-type | E2098 | ISODate | Not a component record in this worksheet |
| src-000382 | field-type | E2099 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E2100 | Max350Text | Not a component record in this worksheet |
| src-000382 | field-type | E2101 | InsuranceClausesCode | Not a component record in this worksheet |
| src-000382 | field-type | E2102 | Location | [Location](bc-a24370bfeb7c7f46ec61.md) |
| src-000382 | field-type | E2103 | CurrencyCode | Not a component record in this worksheet |
| src-000382 | field-type | E2104 | InsurancePartyRole | [InsurancePartyRole](bc-d69fc5fc8156c9a52e6b.md) |
| src-000382 | field-type | E2105 | ProductDelivery | [ProductDelivery](bc-6220ee03b66332d3348e.md) |
| src-000382 | field-type | E2106 | InsuranceCode | Not a component record in this worksheet |
| src-000382 | field-type | E2107 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
