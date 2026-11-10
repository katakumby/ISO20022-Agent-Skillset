---
template: false
review_status: "needs-review"
document_kind: "business-concept"
concept_id: "bc-91a5d9ebe4b64b30a1ea"
title: "PersonIdentification"
business_component_name: "PersonIdentification"
aliases: []
domain: "shared"
domains: ["payments", "securities"]
message_sets: ["bank-to-customer-cash-management", "ccp-clearing", "corporate-actions", "fitrr", "investment-funds", "payments-clearing-and-settlement", "payments-initiation", "settlement-and-reconciliation", "t2s-billing", "t2s-cash-account-query-and-report", "t2s-securities-and-penalty-reporting", "t2s-settlement-restrictions"]
applicability: "source-publication-provenance; message usage requires Traces evidence"
source_ids: ["src-000006", "src-000054", "src-000081", "src-000097", "src-000164", "src-000175", "src-000198", "src-000322", "src-000348", "src-000352", "src-000376", "src-000382"]
source_editions: ["2025", "2025-2026", "august-2026", "december-2025", "march-2026", "september-2025"]
source_locations: [{"source_id": "src-000006", "worksheet": "FullBusinessModel", "ranges": ["A3299:F3308"]}, {"source_id": "src-000054", "worksheet": "FullBusinessModel", "ranges": ["A3299:F3308"]}, {"source_id": "src-000081", "worksheet": "FullBusinessModel", "ranges": ["A3299:F3308"]}, {"source_id": "src-000097", "worksheet": "FullBusinessModel", "ranges": ["A3299:F3308"]}, {"source_id": "src-000164", "worksheet": "FullBusinessModel", "ranges": ["A3299:F3308"]}, {"source_id": "src-000175", "worksheet": "FullBusinessModel", "ranges": ["A3299:F3308"]}, {"source_id": "src-000198", "worksheet": "FullBusinessModel", "ranges": ["A3299:F3308"]}, {"source_id": "src-000322", "worksheet": "FullBusinessModel", "ranges": ["A3274:F3283"]}, {"source_id": "src-000348", "worksheet": "FullBusinessModel", "ranges": ["A3274:F3283"]}, {"source_id": "src-000352", "worksheet": "FullBusinessModel", "ranges": ["A3299:F3308"]}, {"source_id": "src-000376", "worksheet": "FullBusinessModel", "ranges": ["A3299:F3308"]}, {"source_id": "src-000382", "worksheet": "FullBusinessModel", "ranges": ["A3274:F3283"]}]
content_sha256: "91a5d9ebe4b64b30a1ea328d5477ea2e2284c02d87f818243d50fc81e7512b1b"
parent_names: ["PartyIdentificationInformation"]
related_component_names: ["Max35Text", "NPIIdentifier", "Person", "PersonName"]
limitations: ["Conceptual business model; not an XML type, database definition or institutional participant assignment.", "Cardinalities, composition and ownership are not inferred from this six-column table.", "Same-name components with different complete row content remain separate.", "Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage."]
---

# PersonIdentification

## Definition

Unique and unambiguous way to identify a person.

## Complete component rows

`∅` marks a blank source value. Component rows are preserved in source order; the row ordinal maps to every occurrence listed below. The component header and every field, definition, parent, type and opposite-end value remain intact.

| Row ordinal | Business Component Name | Business Element Name | Business Component Parent Name | Documentation | Business Element Type Name | Name of Opposite End |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | PersonIdentification | ∅ | PartyIdentificationInformation | Unique and unambiguous way to identify a person. | ∅ | ∅ |
| 2 | PersonIdentification | SocialSecurityNumber | ∅ | Number assigned by a social security agency. | Max35Text | ∅ |
| 3 | PersonIdentification | Person | ∅ | Person for which an identification is provided. | Person | PersonIdentification |
| 4 | PersonIdentification | PersonName | ∅ | Name by which a person is known and which is usually used to identify that person. It is derived from PartyName (association between PartyIdentificationInformation and PartyName). | PersonName | Identification |
| 5 | PersonIdentification | DriversLicenseNumber | ∅ | Number assigned by a license authority to a driver's license. | Max35Text | ∅ |
| 6 | PersonIdentification | AlienRegistrationNumber | ∅ | Number assigned by a government agency to identify foreign nationals. | Max35Text | ∅ |
| 7 | PersonIdentification | PassportNumber | ∅ | Number assigned by a passport authority to a passport. | Max35Text | ∅ |
| 8 | PersonIdentification | IdentityCardNumber | ∅ | Number assigned by a national authority to an identity card. | Max35Text | ∅ |
| 9 | PersonIdentification | EmployerIdentificationNumber | ∅ | Number assigned to an employer by a registration authority. | Max35Text | ∅ |
| 10 | PersonIdentification | NPI | ∅ | Natural person is identified through the natural person identifier. | NPIIdentifier | ∅ |

## Provenance and all equivalent occurrences

Complete row-content SHA-256: `91a5d9ebe4b64b30a1ea328d5477ea2e2284c02d87f818243d50fc81e7512b1b`. Equivalence includes exact typed values, formula/cache values and number formats; position and style IDs are not a claim of business difference. No alias equivalence is inferred.

| Source | Worksheet/range | Source row order | Original occurrence | Workbook component lookup |
| --- | --- | --- | --- | --- |
| src-000006 | FullBusinessModel!A3299:F3308 | 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308 | [src-000006 original](../../../evidence/omitted/5e0f6b7d43fcbbe816624756.md) | [Lookup](../../../domains/payments/reference/message-sets/bank-to-customer-cash-management/2025-2026/workbooks/src-000006/components.md) |
| src-000054 | FullBusinessModel!A3299:F3308 | 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308 | [src-000054 original](../../../evidence/omitted/ea96e6afbf1f8819d68ca6f6.md) | [Lookup](../../../domains/securities/reference/message-sets/ccp-clearing/2025-2026/workbooks/src-000054/components.md) |
| src-000081 | FullBusinessModel!A3299:F3308 | 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308 | [src-000081 original](../../../evidence/omitted/5d05ada13720516836bc5043.md) | [Lookup](../../../domains/securities/reference/message-sets/corporate-actions/2025-2026/workbooks/src-000081/components.md) |
| src-000097 | FullBusinessModel!A3299:F3308 | 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308 | [src-000097 original](../../../evidence/omitted/3ea6002607634c1b65cb5c88.md) | [Lookup](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/workbooks/src-000097/components.md) |
| src-000164 | FullBusinessModel!A3299:F3308 | 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308 | [src-000164 original](../../../evidence/omitted/87020353dd81a550a7b6ed6f.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-clearing-and-settlement/2025-2026/workbooks/src-000164/components.md) |
| src-000175 | FullBusinessModel!A3299:F3308 | 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308 | [src-000175 original](../../../evidence/omitted/807236f9f4d5f25826f3ba17.md) | [Lookup](../../../domains/payments/reference/message-sets/payments-initiation/2025-2026/workbooks/src-000175/components.md) |
| src-000198 | FullBusinessModel!A3299:F3308 | 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308 | [src-000198 original](../../../evidence/omitted/c6a84c22fb63cab3b848bd88.md) | [Lookup](../../../domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/workbooks/src-000198/components.md) |
| src-000322 | FullBusinessModel!A3274:F3283 | 3274, 3275, 3276, 3277, 3278, 3279, 3280, 3281, 3282, 3283 | [src-000322 original](../../../evidence/omitted/f39eee3c04bb287d206cc6a3.md) | [Lookup](../../../domains/securities/reference/message-sets/fitrr/2025/workbooks/src-000322/components.md) |
| src-000348 | FullBusinessModel!A3274:F3283 | 3274, 3275, 3276, 3277, 3278, 3279, 3280, 3281, 3282, 3283 | [src-000348 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart3_Target2Securities_Billing_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-billing/december-2025/workbooks/src-000348/components.md) |
| src-000352 | FullBusinessModel!A3299:F3308 | 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308 | [src-000352 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart3_Target2Securities_CashAccountQueryAndReport_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/workbooks/src-000352/components.md) |
| src-000376 | FullBusinessModel!A3299:F3308 | 3299, 3300, 3301, 3302, 3303, 3304, 3305, 3306, 3307, 3308 | [src-000376 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart3_Target2Securities_SecuritiesAndPenaltyReporting_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/workbooks/src-000376/components.md) |
| src-000382 | FullBusinessModel!A3274:F3283 | 3274, 3275, 3276, 3277, 3278, 3279, 3280, 3281, 3282, 3283 | [src-000382 original](../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart3_Target2Securities_SettlementRestrictions_v1.xlsx` | [Lookup](../../../domains/securities/reference/message-sets/t2s-settlement-restrictions/september-2025/workbooks/src-000382/components.md) |

## Parent and field-type relationships by source context

Targets are resolved only inside the same supplied worksheet. A matching label in another edition is not a substitute. A target absent from this component table may be a datatype or another model item; this index does not invent its definition. Opposite-end labels remain in the complete rows above.

| Source | Relationship | Source row/cell | Referenced name | Same-source target |
| --- | --- | --- | --- | --- |
| src-000006 | parent | C3299 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-388f466e73d406c114c3.md) |
| src-000006 | field-type | E3300 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E3301 | Person | [Person](bc-53d82c5b4a902489b3c9.md) |
| src-000006 | field-type | E3302 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000006 | field-type | E3303 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E3304 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E3305 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E3306 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E3307 | Max35Text | Not a component record in this worksheet |
| src-000006 | field-type | E3308 | NPIIdentifier | Not a component record in this worksheet |
| src-000054 | parent | C3299 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-388f466e73d406c114c3.md) |
| src-000054 | field-type | E3300 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E3301 | Person | [Person](bc-53d82c5b4a902489b3c9.md) |
| src-000054 | field-type | E3302 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000054 | field-type | E3303 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E3304 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E3305 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E3306 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E3307 | Max35Text | Not a component record in this worksheet |
| src-000054 | field-type | E3308 | NPIIdentifier | Not a component record in this worksheet |
| src-000081 | parent | C3299 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-388f466e73d406c114c3.md) |
| src-000081 | field-type | E3300 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E3301 | Person | [Person](bc-53d82c5b4a902489b3c9.md) |
| src-000081 | field-type | E3302 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000081 | field-type | E3303 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E3304 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E3305 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E3306 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E3307 | Max35Text | Not a component record in this worksheet |
| src-000081 | field-type | E3308 | NPIIdentifier | Not a component record in this worksheet |
| src-000097 | parent | C3299 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-388f466e73d406c114c3.md) |
| src-000097 | field-type | E3300 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E3301 | Person | [Person](bc-53d82c5b4a902489b3c9.md) |
| src-000097 | field-type | E3302 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000097 | field-type | E3303 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E3304 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E3305 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E3306 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E3307 | Max35Text | Not a component record in this worksheet |
| src-000097 | field-type | E3308 | NPIIdentifier | Not a component record in this worksheet |
| src-000164 | parent | C3299 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-388f466e73d406c114c3.md) |
| src-000164 | field-type | E3300 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E3301 | Person | [Person](bc-53d82c5b4a902489b3c9.md) |
| src-000164 | field-type | E3302 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000164 | field-type | E3303 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E3304 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E3305 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E3306 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E3307 | Max35Text | Not a component record in this worksheet |
| src-000164 | field-type | E3308 | NPIIdentifier | Not a component record in this worksheet |
| src-000175 | parent | C3299 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-388f466e73d406c114c3.md) |
| src-000175 | field-type | E3300 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E3301 | Person | [Person](bc-53d82c5b4a902489b3c9.md) |
| src-000175 | field-type | E3302 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000175 | field-type | E3303 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E3304 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E3305 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E3306 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E3307 | Max35Text | Not a component record in this worksheet |
| src-000175 | field-type | E3308 | NPIIdentifier | Not a component record in this worksheet |
| src-000198 | parent | C3299 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-388f466e73d406c114c3.md) |
| src-000198 | field-type | E3300 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E3301 | Person | [Person](bc-53d82c5b4a902489b3c9.md) |
| src-000198 | field-type | E3302 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000198 | field-type | E3303 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E3304 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E3305 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E3306 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E3307 | Max35Text | Not a component record in this worksheet |
| src-000198 | field-type | E3308 | NPIIdentifier | Not a component record in this worksheet |
| src-000322 | parent | C3274 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-96b43f368fbd43460ca2.md) |
| src-000322 | field-type | E3275 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E3276 | Person | [Person](bc-b0e73da769738001743d.md) |
| src-000322 | field-type | E3277 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000322 | field-type | E3278 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E3279 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E3280 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E3281 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E3282 | Max35Text | Not a component record in this worksheet |
| src-000322 | field-type | E3283 | NPIIdentifier | Not a component record in this worksheet |
| src-000348 | parent | C3274 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-96b43f368fbd43460ca2.md) |
| src-000348 | field-type | E3275 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E3276 | Person | [Person](bc-b0e73da769738001743d.md) |
| src-000348 | field-type | E3277 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000348 | field-type | E3278 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E3279 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E3280 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E3281 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E3282 | Max35Text | Not a component record in this worksheet |
| src-000348 | field-type | E3283 | NPIIdentifier | Not a component record in this worksheet |
| src-000352 | parent | C3299 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-388f466e73d406c114c3.md) |
| src-000352 | field-type | E3300 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E3301 | Person | [Person](bc-53d82c5b4a902489b3c9.md) |
| src-000352 | field-type | E3302 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000352 | field-type | E3303 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E3304 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E3305 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E3306 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E3307 | Max35Text | Not a component record in this worksheet |
| src-000352 | field-type | E3308 | NPIIdentifier | Not a component record in this worksheet |
| src-000376 | parent | C3299 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-388f466e73d406c114c3.md) |
| src-000376 | field-type | E3300 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E3301 | Person | [Person](bc-53d82c5b4a902489b3c9.md) |
| src-000376 | field-type | E3302 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000376 | field-type | E3303 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E3304 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E3305 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E3306 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E3307 | Max35Text | Not a component record in this worksheet |
| src-000376 | field-type | E3308 | NPIIdentifier | Not a component record in this worksheet |
| src-000382 | parent | C3274 | PartyIdentificationInformation | [PartyIdentificationInformation](bc-96b43f368fbd43460ca2.md) |
| src-000382 | field-type | E3275 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E3276 | Person | [Person](bc-b0e73da769738001743d.md) |
| src-000382 | field-type | E3277 | PersonName | [PersonName](bc-ce96637841107f789d63.md) |
| src-000382 | field-type | E3278 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E3279 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E3280 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E3281 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E3282 | Max35Text | Not a component record in this worksheet |
| src-000382 | field-type | E3283 | NPIIdentifier | Not a component record in this worksheet |

## Interpretation and review

- Conceptual business model; not an XML type, database definition or institutional participant assignment.
- Cardinalities, composition and ownership are not inferred from this six-column table.
- Same-name components with different complete row content remain separate.
- Source message-set/domain metadata records publication provenance, not proof that every component is used by every message in those sets. Consult the workbook Traces for message-component usage.

The presence of a role-like name does not make every component a participant. Field types refer to conceptual business elements, not automatically to XSD declaration names. Source records were checked for exact input fingerprints and complete nonblank-row assignment. Visual diagram reconciliation is tracked independently.

[Business-component index](index.md) · [Known limitations and issues](../../../tracking/issues.md)
