---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.020.001.04"
message_family: "camt.020"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.020.001.04"
source_ids: ["src-000034"]
source_editions: ["2024-2025"]
---

# camt.020.001.04 structure

[src-000034](../../../../../raw-input/cash_management/camt.020.001.04.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.020.001.04`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.020.001.04 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}BusinessInformationCriteria1 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}BusinessInformationQueryDefinition3 | 12 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}CharacterSearch1Choice | 18 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}Document | 26 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}GeneralBusinessInformationCriteriaDefinition1Choice | 31 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}GeneralBusinessInformationReturnCriteria1 | 37 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}GeneralBusinessInformationSearchCriteria1 | 44 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}GetGeneralBusinessInformationV04 | 51 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}ISODateTime | 58 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}InformationQualifierType1 | 61 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}Max350Text | 67 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}Max35Text | 73 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}MessageHeader1 | 79 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}Priority1Code | 85 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}QueryType2Code | 92 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}RequestedIndicator | 100 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}SupplementaryData1 | 103 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}SupplementaryDataEnvelope1 | 109 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.020.001.04}YesNoIndicator | 114 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 2 |
| complexType | 12 |
| element | 28 |
| enumeration | 7 |
| maxLength | 2 |
| minLength | 2 |
| restriction | 7 |
| schema | 1 |
| sequence | 10 |
| simpleType | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/06fa00bd98676f18bc0b42af.md) · [Message](index.md)
