---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.023.001.01"
message_family: "reda.023"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.023.001.01"
source_ids: ["src-000278"]
source_editions: ["december-2019"]
---

# reda.023.001.01 structure

[src-000278](../../../../../raw-input/target2securities_t2s/reda.023.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.023.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.023.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}DataModification1Code | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}Document | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}Exact4AlphaNumericText | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}GenericIdentification30 | 22 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}ISODate | 29 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}ISODateTime | 32 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}MarketSpecificAttribute1 | 35 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}Max350Text | 41 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}Max35Text | 47 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}Max70Text | 53 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}MessageHeader1 | 59 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}SecuritiesAccount19 | 65 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}SecuritiesAccountModification2 | 72 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}SecuritiesAccountModification2Choice | 78 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}SecuritiesAccountModificationRequestV01 | 85 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}SupplementaryData1 | 93 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}SupplementaryDataEnvelope1 | 99 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}SystemRestriction1 | 104 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}SystemSecuritiesAccount5 | 111 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.023.001.01}TrueFalseIndicator | 120 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 1 |
| complexType | 12 |
| element | 31 |
| enumeration | 3 |
| maxLength | 3 |
| minLength | 3 |
| pattern | 1 |
| restriction | 8 |
| schema | 1 |
| sequence | 11 |
| simpleType | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
