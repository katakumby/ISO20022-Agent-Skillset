---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.032.001.09"
message_family: "seev.032"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.032.001.09"
source_ids: ["src-000083"]
source_editions: ["2025-2026"]
---

# seev.032.001.09 structure

[src-000083](../../../../../raw-input/corporate_actions/seev.032.001.09.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.032.001.09`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.032.001.09 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}CorporateActionEventProcessingStatusAdviceV09 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}CorporateActionEventType112Choice | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}CorporateActionEventType40Code | 21 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}CorporateActionGeneralInformation182 | 90 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}CorporateActionNarrative10 | 98 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}Document | 104 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}DocumentIdentification33 | 109 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}DocumentIdentification3Choice | 115 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}DocumentIdentification9 | 121 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}DocumentNumber5Choice | 126 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}EventProcessingStatus7Choice | 133 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}Exact3NumericText | 141 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}Exact4AlphaNumericText | 146 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}GenericIdentification30 | 151 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}GenericIdentification36 | 158 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}ISO20022MessageIdentificationText | 165 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}Max210Text | 170 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}Max350Text | 176 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}Max35Text | 182 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}NoReasonCode | 188 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}NoSpecifiedReason1 | 193 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}PendingReason29Code | 198 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}PendingReason70Choice | 206 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}PendingStatus74Choice | 212 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}PendingStatusReason29 | 218 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}ProprietaryReason4 | 224 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}ProprietaryStatusAndReason6 | 230 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}SupplementaryData1 | 236 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.032.001.09}SupplementaryDataEnvelope1 | 242 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 6 |
| complexType | 20 |
| element | 47 |
| enumeration | 70 |
| maxLength | 3 |
| minLength | 3 |
| pattern | 3 |
| restriction | 9 |
| schema | 1 |
| sequence | 14 |
| simpleType | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
