---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-ec3cbff5782546ebc9a8"
title: "PaymentTracker"
business_component_name: "PaymentTracker"
aliases: []
domain: "shared"
domains: ["payments", "securities", "shared"]
message_sets: ["cash-management", "post-trade-matching", "t2s-administration", "t2s-collateral-management-reference-data", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-link-reference-data", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-reference-data"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000016", "src-000182", "src-000345", "src-000355", "src-000358", "src-000361", "src-000364", "src-000367", "src-000370", "src-000373", "src-000379"]
source_editions: ["2024-2025", "december-2019", "december-2024", "february-2025", "june-2021", "march-2024", "may-2025"]
source_locations: [{"source_id": "src-000016", "worksheet": "FullBusinessModel", "ranges": ["A3200:F3204"]}, {"source_id": "src-000182", "worksheet": "FullBusinessModel", "ranges": ["A3200:F3204"]}, {"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A5201:F5205"]}, {"source_id": "src-000355", "worksheet": "FullBusinessModel", "ranges": ["A3186:F3190"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A5201:F5205"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A5201:F5205"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A3186:F3190"]}, {"source_id": "src-000367", "worksheet": "FullBusinessModel", "ranges": ["A3186:F3190"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A5201:F5205"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A5201:F5205"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A5201:F5205"]}]
content_sha256: "ec3cbff5782546ebc9a8f79462d5c2b28f7806a87e4fe309ccec4e6b36207df5"
parent_names: []
related_component_names: ["ChargeBearerTypeCode", "CurrencyAndAmount", "CurrencyExchange", "FinancialInstitution"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# PaymentTracker

## Definition

Specifies the agent specific tracking system information of a payment transaction.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | PaymentTracker | ∅ | ∅ | Specifies the agent specific tracking system information of a payment transaction. | ∅ | ∅ |
| 2 | PaymentTracker | Agent | ∅ | Identification of an agent in the tracker. | FinancialInstitution | RelatedPaymentTracker |
| 3 | PaymentTracker | ChargesAmount | ∅ | Transaction charges to be paid by the charge bearer. | CurrencyAndAmount | ∅ |
| 4 | PaymentTracker | ChargeBearer | ∅ | Specifies which party/parties will bear the charges associated with the processing of the payment transaction. | ChargeBearerTypeCode | ∅ |
| 5 | PaymentTracker | ExchangeRateData | ∅ | Provides details of the rate and the currencies used in the foreign exchange. | CurrencyExchange | RelatedPaymentTracker |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `ec3cbff5782546ebc9a8f79462d5c2b28f7806a87e4fe309ccec4e6b36207df5`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000016 | FullBusinessModel!A3200:F3204 | 3200, 3201, 3202, 3203, 3204 | [src-000016 original](<../../../raw-input/cash_management/ISO20022_MDRPart3_CashManagement_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/payments/reference/message-sets/cash-management/2024-2025/workbooks/src-000016/components.md>) |
| src-000182 | FullBusinessModel!A3200:F3204 | 3200, 3201, 3202, 3203, 3204 | [src-000182 original](<../../../raw-input/post_trade_matching/ISO20022_MDRPart3_PostTradeMatching_2024_2025_v1.xlsx>) | [Lookup](<../../../domains/securities/reference/message-sets/post-trade-matching/2024-2025/workbooks/src-000182/components.md>) |
| src-000345 | FullBusinessModel!A5201:F5205 | 5201, 5202, 5203, 5204, 5205 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000355 | FullBusinessModel!A3186:F3190 | 3186, 3187, 3188, 3189, 3190 | [src-000355 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralManagementReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-management-reference-data/may-2025/workbooks/src-000355/components.md>) |
| src-000358 | FullBusinessModel!A5201:F5205 | 5201, 5202, 5203, 5204, 5205 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A5201:F5205 | 5201, 5202, 5203, 5204, 5205 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A3186:F3190 | 3186, 3187, 3188, 3189, 3190 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000367 | FullBusinessModel!A3186:F3190 | 3186, 3187, 3188, 3189, 3190 | [src-000367 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_LinkReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-link-reference-data/december-2024/workbooks/src-000367/components.md>) |
| src-000370 | FullBusinessModel!A5201:F5205 | 5201, 5202, 5203, 5204, 5205 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A5201:F5205 | 5201, 5202, 5203, 5204, 5205 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000379 | FullBusinessModel!A5201:F5205 | 5201, 5202, 5203, 5204, 5205 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000016 | field-type | E3201 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000016 | field-type | E3202 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000016 | field-type | E3203 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000016 | field-type | E3204 | CurrencyExchange | [CurrencyExchange](<bc-34731f533c7e6210a4f1.md>) |
| src-000182 | field-type | E3201 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000182 | field-type | E3202 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000182 | field-type | E3203 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000182 | field-type | E3204 | CurrencyExchange | [CurrencyExchange](<bc-34731f533c7e6210a4f1.md>) |
| src-000345 | field-type | E5202 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000345 | field-type | E5203 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000345 | field-type | E5204 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E5205 | CurrencyExchange | [CurrencyExchange](<bc-6d0ca75e01a4ac88622b.md>) |
| src-000355 | field-type | E3187 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000355 | field-type | E3188 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000355 | field-type | E3189 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000355 | field-type | E3190 | CurrencyExchange | [CurrencyExchange](<bc-6d0ca75e01a4ac88622b.md>) |
| src-000358 | field-type | E5202 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000358 | field-type | E5203 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000358 | field-type | E5204 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E5205 | CurrencyExchange | [CurrencyExchange](<bc-6d0ca75e01a4ac88622b.md>) |
| src-000361 | field-type | E5202 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000361 | field-type | E5203 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000361 | field-type | E5204 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E5205 | CurrencyExchange | [CurrencyExchange](<bc-6d0ca75e01a4ac88622b.md>) |
| src-000364 | field-type | E3187 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000364 | field-type | E3188 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000364 | field-type | E3189 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E3190 | CurrencyExchange | [CurrencyExchange](<bc-6d0ca75e01a4ac88622b.md>) |
| src-000367 | field-type | E3187 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000367 | field-type | E3188 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000367 | field-type | E3189 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000367 | field-type | E3190 | CurrencyExchange | [CurrencyExchange](<bc-6d0ca75e01a4ac88622b.md>) |
| src-000370 | field-type | E5202 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000370 | field-type | E5203 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000370 | field-type | E5204 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E5205 | CurrencyExchange | [CurrencyExchange](<bc-6d0ca75e01a4ac88622b.md>) |
| src-000373 | field-type | E5202 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000373 | field-type | E5203 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000373 | field-type | E5204 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E5205 | CurrencyExchange | [CurrencyExchange](<bc-6d0ca75e01a4ac88622b.md>) |
| src-000379 | field-type | E5202 | FinancialInstitution | [FinancialInstitution](<bc-2406e73d218d9e4cdf9e.md>) |
| src-000379 | field-type | E5203 | CurrencyAndAmount | Not a component record in this worksheet |
| src-000379 | field-type | E5204 | ChargeBearerTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E5205 | CurrencyExchange | [CurrencyExchange](<bc-6d0ca75e01a4ac88622b.md>) |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
