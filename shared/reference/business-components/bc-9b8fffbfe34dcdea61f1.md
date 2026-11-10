---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-9b8fffbfe34dcdea61f1"
title: "SystemClosureInformation"
business_component_name: "SystemClosureInformation"
aliases: []
domain: "shared"
domains: ["securities", "shared"]
message_sets: ["t2s-administration", "t2s-collateral-reporting", "t2s-intra-balance-movement", "t2s-limit-utilisation-journal", "t2s-party-reference-data", "t2s-securities-account-reference-data", "t2s-securities-reference-data"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000345", "src-000358", "src-000361", "src-000364", "src-000370", "src-000373", "src-000379"]
source_editions: ["december-2019", "february-2025", "june-2021", "march-2024"]
source_locations: [{"source_id": "src-000345", "worksheet": "FullBusinessModel", "ranges": ["A2044:F2047"]}, {"source_id": "src-000358", "worksheet": "FullBusinessModel", "ranges": ["A2044:F2047"]}, {"source_id": "src-000361", "worksheet": "FullBusinessModel", "ranges": ["A2044:F2047"]}, {"source_id": "src-000364", "worksheet": "FullBusinessModel", "ranges": ["A4837:F4840"]}, {"source_id": "src-000370", "worksheet": "FullBusinessModel", "ranges": ["A2044:F2047"]}, {"source_id": "src-000373", "worksheet": "FullBusinessModel", "ranges": ["A2044:F2047"]}, {"source_id": "src-000379", "worksheet": "FullBusinessModel", "ranges": ["A2044:F2047"]}]
content_sha256: "9b8fffbfe34dcdea61f1f0cc3ea46c058d89c620b7e334b631f1b88648b31d67"
parent_names: []
related_component_names: ["SystemAvailability", "SystemClosureReasonCode"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# SystemClosureInformation

## Definition

Information about inactivity of a system.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SystemClosureInformation | ∅ | ∅ | Information about inactivity of a system. | ∅ | ∅ |
| 2 | SystemClosureInformation | Period | ∅ | Period of time when the system is closed/not operating. | ∅ | ∅ |
| 3 | SystemClosureInformation | SystemAvailability | ∅ | System for which closure information is specified. | SystemAvailability | ClosureInformation |
| 4 | SystemClosureInformation | ClosureReason | ∅ | Reason the system is closed/not operating. | SystemClosureReasonCode | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `9b8fffbfe34dcdea61f1f0cc3ea46c058d89c620b7e334b631f1b88648b31d67`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000345 | FullBusinessModel!A2044:F2047 | 2044, 2045, 2046, 2047 | [src-000345 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart3_Target2Securities_Administration_2023_2024_v1.xlsx` | [Lookup](<../message-sets/t2s-administration/march-2024/workbooks/src-000345/components.md>) |
| src-000358 | FullBusinessModel!A2044:F2047 | 2044, 2045, 2046, 2047 | [src-000358 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_CollateralReporting_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-collateral-reporting/march-2024/workbooks/src-000358/components.md>) |
| src-000361 | FullBusinessModel!A2044:F2047 | 2044, 2045, 2046, 2047 | [src-000361 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart3_Target2Securities_IntraBalanceMovement_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-intra-balance-movement/march-2024/workbooks/src-000361/components.md>) |
| src-000364 | FullBusinessModel!A4837:F4840 | 4837, 4838, 4839, 4840 | [src-000364 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart3_Target2Securities_LimitUtilisationJournal_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-limit-utilisation-journal/february-2025/workbooks/src-000364/components.md>) |
| src-000370 | FullBusinessModel!A2044:F2047 | 2044, 2045, 2046, 2047 | [src-000370 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_PartyReferenceData_2023_2024_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-party-reference-data/march-2024/workbooks/src-000370/components.md>) |
| src-000373 | FullBusinessModel!A2044:F2047 | 2044, 2045, 2046, 2047 | [src-000373 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAccountReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-account-reference-data/december-2019/workbooks/src-000373/components.md>) |
| src-000379 | FullBusinessModel!A2044:F2047 | 2044, 2045, 2046, 2047 | [src-000379 original](<../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip>) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesReferenceData_v1.xlsx` | [Lookup](<../../../domains/securities/reference/message-sets/t2s-securities-reference-data/june-2021/workbooks/src-000379/components.md>) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000345 | field-type | E2046 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000345 | field-type | E2047 | SystemClosureReasonCode | Not a component record in this worksheet |
| src-000358 | field-type | E2046 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000358 | field-type | E2047 | SystemClosureReasonCode | Not a component record in this worksheet |
| src-000361 | field-type | E2046 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000361 | field-type | E2047 | SystemClosureReasonCode | Not a component record in this worksheet |
| src-000364 | field-type | E4839 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000364 | field-type | E4840 | SystemClosureReasonCode | Not a component record in this worksheet |
| src-000370 | field-type | E2046 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000370 | field-type | E2047 | SystemClosureReasonCode | Not a component record in this worksheet |
| src-000373 | field-type | E2046 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000373 | field-type | E2047 | SystemClosureReasonCode | Not a component record in this worksheet |
| src-000379 | field-type | E2046 | SystemAvailability | [SystemAvailability](<bc-3f4f3b88d6e42219c056.md>) |
| src-000379 | field-type | E2047 | SystemClosureReasonCode | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](<index.md>) · [Known limitations and issues](<../../../tracking/issues.md>)
