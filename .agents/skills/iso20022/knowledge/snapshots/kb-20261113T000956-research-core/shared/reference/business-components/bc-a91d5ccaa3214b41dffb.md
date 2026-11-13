---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-a91d5ccaa3214b41dffb"
title: "SecuritiesRelatedFees"
business_component_name: "SecuritiesRelatedFees"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["bank-to-customer-cash-management", "cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "post-trade-matching", "settlement-and-reconciliation", "t2s-administration", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-and-penalty-reporting", "t2s-securities-reference-data", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000016", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000182", "src-000198", "src-000322", "src-000345", "src-000348", "src-000352", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000376", "src-000379", "src-000382"]
source_editions: ["2024-2025", "2025", "2025-2026", "august-2026", "december-2019", "december-2024", "december-2025", "february-2025", "june-2021", "march-2024", "march-2026", "may-2025", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A4459:F4464"]}, {"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A4389:F4394"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A4459:F4464"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A4459:F4464"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A4459:F4464"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A4459:F4464"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A4459:F4464"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A4389:F4394"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A4459:F4464"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A4428:F4433"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A1981:F1986"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A4428:F4433"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A4459:F4464"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A4364:F4369"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A1981:F1986"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A1981:F1986"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A4364:F4369"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A4364:F4369"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A1981:F1986"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A1981:F1986"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A4459:F4464"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A1981:F1986"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A4428:F4433"]}]
content_sha256: "a91d5ccaa3214b41dffb85b1fbb4580d4f2985acff0be490de6110ddd94b386d"
parent_names: ["Charges"]
related_component_names: ["CurrencyAndAmount", "Security"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# SecuritiesRelatedFees

## Definition

Fees related to securities trades.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SecuritiesRelatedFees | ∅ | Charges | Fees related to securities trades. | ∅ | ∅ |
| 2 | SecuritiesRelatedFees | Security | ∅ | Security for which fees are specified. | Security | Fees |
| 3 | SecuritiesRelatedFees | PostageFeeAmount | ∅ | Amount of money paid for delivery by regular post mail. | CurrencyAndAmount | ∅ |
| 4 | SecuritiesRelatedFees | RegulatoryFeesAmount | ∅ | Amount of money charged by a regulatory authority, eg, Securities and Exchange fees. | CurrencyAndAmount | ∅ |
| 5 | SecuritiesRelatedFees | ShippingFeesAmount | ∅ | Amount of money (including insurance) paid for delivery by carrier. | CurrencyAndAmount | ∅ |
| 6 | SecuritiesRelatedFees | ResearchFee | ∅ | Charge or commission paid by the investor to a distributor/intermediary or other service provider for the provision of financial research. | CurrencyAndAmount | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `a91d5ccaa3214b41dffb85b1fbb4580d4f2985acff0be490de6110ddd94b386d`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A4459:F4464 | 4459, 4460, 4461, 4462, 4463, 4464 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000016 | FullBusinessModel!A4389:F4394 | 4389, 4390, 4391, 4392, 4393, 4394 | [src-000016 original](../../../evidence/omitted/42cf3c4088baf4d4c6dc07c1.md) | [Lookup](../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md) |
| src-000054 | FullBusinessModel!A4459:F4464 | 4459, 4460, 4461, 4462, 4463, 4464 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A4459:F4464 | 4459, 4460, 4461, 4462, 4463, 4464 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A4459:F4464 | 4459, 4460, 4461, 4462, 4463, 4464 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A4459:F4464 | 4459, 4460, 4461, 4462, 4463, 4464 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A4459:F4464 | 4459, 4460, 4461, 4462, 4463, 4464 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000182 | FullBusinessModel!A4389:F4394 | 4389, 4390, 4391, 4392, 4393, 4394 | [src-000182 original](../../../evidence/omitted/5096efb167050baf43bfb32a.md) | [Lookup](../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md) |
| src-000198 | FullBusinessModel!A4459:F4464 | 4459, 4460, 4461, 4462, 4463, 4464 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A4428:F4433 | 4428, 4429, 4430, 4431, 4432, 4433 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000345 | FullBusinessModel!A1981:F1986 | 1981, 1982, 1983, 1984, 1985, 1986 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000348 | FullBusinessModel!A4428:F4433 | 4428, 4429, 4430, 4431, 4432, 4433 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A4459:F4464 | 4459, 4460, 4461, 4462, 4463, 4464 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000355 | FullBusinessModel!A4364:F4369 | 4364, 4365, 4366, 4367, 4368, 4369 | [src-000355 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md) |
| src-000358 | FullBusinessModel!A1981:F1986 | 1981, 1982, 1983, 1984, 1985, 1986 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A1981:F1986 | 1981, 1982, 1983, 1984, 1985, 1986 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A4364:F4369 | 4364, 4365, 4366, 4367, 4368, 4369 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000367 | FullBusinessModel!A4364:F4369 | 4364, 4365, 4366, 4367, 4368, 4369 | [src-000367 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md) |
| src-000370 | FullBusinessModel!A1981:F1986 | 1981, 1982, 1983, 1984, 1985, 1986 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A1981:F1986 | 1981, 1982, 1983, 1984, 1985, 1986 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000376 | FullBusinessModel!A4459:F4464 | 4459, 4460, 4461, 4462, 4463, 4464 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000379 | FullBusinessModel!A1981:F1986 | 1981, 1982, 1983, 1984, 1985, 1986 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |
| src-000382 | FullBusinessModel!A4428:F4433 | 4428, 4429, 4430, 4431, 4432, 4433 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C4459 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000006 | field-type | E4460 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000006 | field-type | E4461 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E4462 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E4463 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000006 | field-type | E4464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | parent | C4389 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000016 | field-type | E4390 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000016 | field-type | E4391 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E4392 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E4393 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E4394 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | parent | C4459 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000054 | field-type | E4460 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000054 | field-type | E4461 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E4462 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E4463 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000054 | field-type | E4464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | parent | C4459 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000081 | field-type | E4460 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000081 | field-type | E4461 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E4462 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E4463 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000081 | field-type | E4464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | parent | C4459 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000097 | field-type | E4460 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000097 | field-type | E4461 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E4462 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E4463 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000097 | field-type | E4464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | parent | C4459 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000164 | field-type | E4460 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000164 | field-type | E4461 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E4462 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E4463 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000164 | field-type | E4464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | parent | C4459 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000175 | field-type | E4460 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000175 | field-type | E4461 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E4462 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E4463 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000175 | field-type | E4464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | parent | C4389 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000182 | field-type | E4390 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000182 | field-type | E4391 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E4392 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E4393 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E4394 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | parent | C4459 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000198 | field-type | E4460 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000198 | field-type | E4461 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E4462 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E4463 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000198 | field-type | E4464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | parent | C4428 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000322 | field-type | E4429 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000322 | field-type | E4430 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E4431 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E4432 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000322 | field-type | E4433 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | parent | C1981 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000345 | field-type | E1982 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000345 | field-type | E1983 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E1984 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E1985 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E1986 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | parent | C4428 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000348 | field-type | E4429 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000348 | field-type | E4430 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E4431 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E4432 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000348 | field-type | E4433 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | parent | C4459 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000352 | field-type | E4460 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000352 | field-type | E4461 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E4462 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E4463 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000352 | field-type | E4464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | parent | C4364 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000355 | field-type | E4365 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000355 | field-type | E4366 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E4367 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E4368 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E4369 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | parent | C1981 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000358 | field-type | E1982 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000358 | field-type | E1983 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E1984 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E1985 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E1986 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | parent | C1981 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000361 | field-type | E1982 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000361 | field-type | E1983 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E1984 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E1985 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E1986 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | parent | C4364 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000364 | field-type | E4365 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000364 | field-type | E4366 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E4367 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E4368 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E4369 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | parent | C4364 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000367 | field-type | E4365 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000367 | field-type | E4366 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E4367 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E4368 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E4369 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | parent | C1981 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000370 | field-type | E1982 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000370 | field-type | E1983 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E1984 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E1985 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E1986 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | parent | C1981 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000373 | field-type | E1982 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000373 | field-type | E1983 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E1984 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E1985 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E1986 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | parent | C4459 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000376 | field-type | E4460 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000376 | field-type | E4461 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E4462 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E4463 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000376 | field-type | E4464 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | parent | C1981 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000379 | field-type | E1982 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000379 | field-type | E1983 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E1984 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E1985 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E1986 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | parent | C4428 | Charges | [Charges](bc-813965e3665c8b53be80.md) |
| src-000382 | field-type | E4429 | Security | [Security](bc-4f8addc5d017fd073013.md) |
| src-000382 | field-type | E4430 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E4431 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E4432 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000382 | field-type | E4433 | CurrencyAndAmount | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
