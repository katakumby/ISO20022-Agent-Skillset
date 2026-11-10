---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-e0d8c8a6b6dcf6ed6248"
title: "LifeCalculation"
business_component_name: "LifeCalculation"
aliases: []
domain: "shared"
domains: ["securities", "shared"]
message_sets: ["t2s-administration", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-reference-data"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000345", "src-000358", "src-000361", "src-000364", "src-000370", "src-000373", "src-000379"]
source_editions: ["december-2019", "february-2025", "june-2021", "march-2024"]
source_locations: [{"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A4882:F4888"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A4882:F4888"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A4882:F4888"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A2505:F2511"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A4882:F4888"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A4882:F4888"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A4882:F4888"]}]
content_sha256: "e0d8c8a6b6dcf6ed62483c18a7f039eb08a1f7c589e87a4edd429538d84b543f"
parent_names: []
related_component_names: ["CalculationTypeCode", "ISODateTime", "Number", "SecuritiesPricing", "VariableInterest"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# LifeCalculation

## Definition

Estimate of the number of terms to maturity, taking the possibility of early payments into account.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LifeCalculation | ∅ | ∅ | Estimate of the number of terms to maturity, taking the possibility of early payments into account. | ∅ | ∅ |
| 2 | LifeCalculation | SecuritiesPricing | ∅ | Securities pricing for which a life calculation is specified. | SecuritiesPricing | LifeCalculation |
| 3 | LifeCalculation | VariableInterest | ∅ | Variable interest used for the calculation. | VariableInterest | LifeCalculation |
| 4 | LifeCalculation | Years | ∅ | Result of the life calculation measured in number of years. | Number | ∅ |
| 5 | LifeCalculation | CalculationType | ∅ | Specifies the type of calculation. | CalculationTypeCode | ∅ |
| 6 | LifeCalculation | ValueDate | ∅ | Date/time on which the calculation is based, for example, valuation on October 1 (price date) based on price of September 19 ( value date). | ISODateTime | ∅ |
| 7 | LifeCalculation | ValuePeriod | ∅ | Period on which the calculation is based. | ∅ | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `e0d8c8a6b6dcf6ed62483c18a7f039eb08a1f7c589e87a4edd429538d84b543f`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000345 | FullBusinessModel!A4882:F4888 | 4882, 4883, 4884, 4885, 4886, 4887, 4888 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000358 | FullBusinessModel!A4882:F4888 | 4882, 4883, 4884, 4885, 4886, 4887, 4888 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A4882:F4888 | 4882, 4883, 4884, 4885, 4886, 4887, 4888 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A2505:F2511 | 2505, 2506, 2507, 2508, 2509, 2510, 2511 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000370 | FullBusinessModel!A4882:F4888 | 4882, 4883, 4884, 4885, 4886, 4887, 4888 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A4882:F4888 | 4882, 4883, 4884, 4885, 4886, 4887, 4888 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000379 | FullBusinessModel!A4882:F4888 | 4882, 4883, 4884, 4885, 4886, 4887, 4888 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000345 | field-type | E4883 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000345 | field-type | E4884 | VariableInterest | [VariableInterest](bc-eb256a646170ab59deca.md) |
| src-000345 | field-type | E4885 | Number | Not a component record in this worksheet |
| src-000345 | field-type | E4886 | CalculationTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E4887 | ISODateTime | Not a component record in this worksheet |
| src-000358 | field-type | E4883 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000358 | field-type | E4884 | VariableInterest | [VariableInterest](bc-eb256a646170ab59deca.md) |
| src-000358 | field-type | E4885 | Number | Not a component record in this worksheet |
| src-000358 | field-type | E4886 | CalculationTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E4887 | ISODateTime | Not a component record in this worksheet |
| src-000361 | field-type | E4883 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000361 | field-type | E4884 | VariableInterest | [VariableInterest](bc-eb256a646170ab59deca.md) |
| src-000361 | field-type | E4885 | Number | Not a component record in this worksheet |
| src-000361 | field-type | E4886 | CalculationTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E4887 | ISODateTime | Not a component record in this worksheet |
| src-000364 | field-type | E2506 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000364 | field-type | E2507 | VariableInterest | [VariableInterest](bc-eb256a646170ab59deca.md) |
| src-000364 | field-type | E2508 | Number | Not a component record in this worksheet |
| src-000364 | field-type | E2509 | CalculationTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E2510 | ISODateTime | Not a component record in this worksheet |
| src-000370 | field-type | E4883 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000370 | field-type | E4884 | VariableInterest | [VariableInterest](bc-eb256a646170ab59deca.md) |
| src-000370 | field-type | E4885 | Number | Not a component record in this worksheet |
| src-000370 | field-type | E4886 | CalculationTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E4887 | ISODateTime | Not a component record in this worksheet |
| src-000373 | field-type | E4883 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000373 | field-type | E4884 | VariableInterest | [VariableInterest](bc-eb256a646170ab59deca.md) |
| src-000373 | field-type | E4885 | Number | Not a component record in this worksheet |
| src-000373 | field-type | E4886 | CalculationTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E4887 | ISODateTime | Not a component record in this worksheet |
| src-000379 | field-type | E4883 | SecuritiesPricing | [SecuritiesPricing](bc-7300499c86791ac12ffd.md) |
| src-000379 | field-type | E4884 | VariableInterest | [VariableInterest](bc-eb256a646170ab59deca.md) |
| src-000379 | field-type | E4885 | Number | Not a component record in this worksheet |
| src-000379 | field-type | E4886 | CalculationTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E4887 | ISODateTime | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
