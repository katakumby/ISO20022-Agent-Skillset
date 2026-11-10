---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-0bc5cadf5e468aed509b"
title: "Pension"
business_component_name: "Pension"
aliases: []
domain: "shared"
domains: ["securities", "shared"]
message_sets: ["t2s-administration", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-reference-data"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000345", "src-000358", "src-000361", "src-000364", "src-000370", "src-000373", "src-000379"]
source_editions: ["december-2019", "february-2025", "june-2021", "march-2024"]
source_locations: [{"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A5239:F5252"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A5239:F5252"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A5239:F5252"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A3193:F3206"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A5239:F5252"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A5239:F5252"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A5239:F5252"]}]
content_sha256: "0bc5cadf5e468aed509bb73e04d9419e75016b174e2468b9bc89abd801e7afd0"
parent_names: []
related_component_names: ["DecimalNumber", "Drawdown", "InvestmentPlan", "LumpSumTypeCode", "PensionOrderTypeCode", "PensionSchemeTypeCode", "PensionTransferScopeCode", "PersonIdentificationTypeCode", "YesNoIndicator"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# Pension

## Definition

Attributes of a pension.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Pension | ∅ | ∅ | Attributes of a pension. | ∅ | ∅ |
| 2 | Pension | ValueOfPensionPolicy | ∅ | Value of the pension policy, plan or scheme. | ∅ | ∅ |
| 3 | Pension | RelatedInvestmentPlan | ∅ | Plan that allows investors to schedule periodical investments or divestments, according to pre-defined criteria. | InvestmentPlan | Pension |
| 4 | Pension | EstimatedValue | ∅ | Estimated value of the pension policy, plan or scheme. | ∅ | ∅ |
| 5 | Pension | TransferScope | ∅ | Scope of the pension policy, plan or scheme transfer. | PensionTransferScopeCode | ∅ |
| 6 | Pension | Drawdown | ∅ | Details of a drawdown tranche. | Drawdown | Pension |
| 7 | Pension | PensionOrderType | ∅ | Type of order attached to the pension policy, plan or scheme. | PensionOrderTypeCode | ∅ |
| 8 | Pension | RetirementAge | ∅ | Age at which the pension policy, plan or scheme holder retires. | DecimalNumber | ∅ |
| 9 | Pension | Identification | ∅ | Identification of the pension policy, plan or scheme. | ∅ | ∅ |
| 10 | Pension | Type | ∅ | Type of pension policy, plan or scheme. | PensionSchemeTypeCode | ∅ |
| 11 | Pension | TaxFreeCashAmount | ∅ | Amount of cash that is tax free. | ∅ | ∅ |
| 12 | Pension | LumpSumType | ∅ | Type of lump sum paid to a member of the pension policy, plan or scheme. | LumpSumTypeCode | ∅ |
| 13 | Pension | TaxReference | ∅ | Tax reference issued to the pension policy, plan or scheme by a central organisation. | PersonIdentificationTypeCode | ∅ |
| 14 | Pension | ClientLifetimeAllowanceProtection | ∅ | Indicates whether the client has any lifetime allowance protection. | YesNoIndicator | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `0bc5cadf5e468aed509bb73e04d9419e75016b174e2468b9bc89abd801e7afd0`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000345 | FullBusinessModel!A5239:F5252 | 5239, 5240, 5241, 5242, 5243, 5244, 5245, 5246, 5247, 5248, 5249, 5250, 5251, 5252 | [src-000345 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md) |
| src-000358 | FullBusinessModel!A5239:F5252 | 5239, 5240, 5241, 5242, 5243, 5244, 5245, 5246, 5247, 5248, 5249, 5250, 5251, 5252 | [src-000358 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md) |
| src-000361 | FullBusinessModel!A5239:F5252 | 5239, 5240, 5241, 5242, 5243, 5244, 5245, 5246, 5247, 5248, 5249, 5250, 5251, 5252 | [src-000361 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md) |
| src-000364 | FullBusinessModel!A3193:F3206 | 3193, 3194, 3195, 3196, 3197, 3198, 3199, 3200, 3201, 3202, 3203, 3204, 3205, 3206 | [src-000364 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md) |
| src-000370 | FullBusinessModel!A5239:F5252 | 5239, 5240, 5241, 5242, 5243, 5244, 5245, 5246, 5247, 5248, 5249, 5250, 5251, 5252 | [src-000370 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md) |
| src-000373 | FullBusinessModel!A5239:F5252 | 5239, 5240, 5241, 5242, 5243, 5244, 5245, 5246, 5247, 5248, 5249, 5250, 5251, 5252 | [src-000373 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md) |
| src-000379 | FullBusinessModel!A5239:F5252 | 5239, 5240, 5241, 5242, 5243, 5244, 5245, 5246, 5247, 5248, 5249, 5250, 5251, 5252 | [src-000379 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000345 | field-type | E5241 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000345 | field-type | E5243 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000345 | field-type | E5244 | Drawdown | [Drawdown](bc-2326e730cbb638390369.md) |
| src-000345 | field-type | E5245 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E5246 | DecimalNumber | Not a component record in this worksheet |
| src-000345 | field-type | E5248 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E5250 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E5251 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000345 | field-type | E5252 | YesNoIndicator | Not a component record in this worksheet |
| src-000358 | field-type | E5241 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000358 | field-type | E5243 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000358 | field-type | E5244 | Drawdown | [Drawdown](bc-2326e730cbb638390369.md) |
| src-000358 | field-type | E5245 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E5246 | DecimalNumber | Not a component record in this worksheet |
| src-000358 | field-type | E5248 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E5250 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E5251 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000358 | field-type | E5252 | YesNoIndicator | Not a component record in this worksheet |
| src-000361 | field-type | E5241 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000361 | field-type | E5243 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000361 | field-type | E5244 | Drawdown | [Drawdown](bc-2326e730cbb638390369.md) |
| src-000361 | field-type | E5245 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E5246 | DecimalNumber | Not a component record in this worksheet |
| src-000361 | field-type | E5248 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E5250 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E5251 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000361 | field-type | E5252 | YesNoIndicator | Not a component record in this worksheet |
| src-000364 | field-type | E3195 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000364 | field-type | E3197 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000364 | field-type | E3198 | Drawdown | [Drawdown](bc-2326e730cbb638390369.md) |
| src-000364 | field-type | E3199 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E3200 | DecimalNumber | Not a component record in this worksheet |
| src-000364 | field-type | E3202 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E3204 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E3205 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000364 | field-type | E3206 | YesNoIndicator | Not a component record in this worksheet |
| src-000370 | field-type | E5241 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000370 | field-type | E5243 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000370 | field-type | E5244 | Drawdown | [Drawdown](bc-2326e730cbb638390369.md) |
| src-000370 | field-type | E5245 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E5246 | DecimalNumber | Not a component record in this worksheet |
| src-000370 | field-type | E5248 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E5250 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E5251 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000370 | field-type | E5252 | YesNoIndicator | Not a component record in this worksheet |
| src-000373 | field-type | E5241 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000373 | field-type | E5243 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000373 | field-type | E5244 | Drawdown | [Drawdown](bc-2326e730cbb638390369.md) |
| src-000373 | field-type | E5245 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E5246 | DecimalNumber | Not a component record in this worksheet |
| src-000373 | field-type | E5248 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E5250 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E5251 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000373 | field-type | E5252 | YesNoIndicator | Not a component record in this worksheet |
| src-000379 | field-type | E5241 | InvestmentPlan | [InvestmentPlan](bc-3e6c5f3d5f23fafb2fe9.md) |
| src-000379 | field-type | E5243 | PensionTransferScopeCode | Not a component record in this worksheet |
| src-000379 | field-type | E5244 | Drawdown | [Drawdown](bc-2326e730cbb638390369.md) |
| src-000379 | field-type | E5245 | PensionOrderTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E5246 | DecimalNumber | Not a component record in this worksheet |
| src-000379 | field-type | E5248 | PensionSchemeTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E5250 | LumpSumTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E5251 | PersonIdentificationTypeCode | Not a component record in this worksheet |
| src-000379 | field-type | E5252 | YesNoIndicator | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
