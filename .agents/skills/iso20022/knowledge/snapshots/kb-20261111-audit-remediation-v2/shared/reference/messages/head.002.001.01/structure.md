---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "shared"
message_id: "head.002.001.01"
message_family: "head.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:head.002.001.01"
source_ids: ["src-000261"]
source_editions: ["june-2024"]
---

# head.002.001.01 structure

[src-000261](../../../../raw-input/target2securities_t2s/head.002.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:head.002.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:head.002.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Xchg | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}BusinessFileHeaderV01 | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}Xchg | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}ApplicationSpecifics1 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}BusinessFileHeaderV01 | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}ISODateTime | 18 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}LaxPayload | 21 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}ManifestData2 | 26 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}Max140Text | 32 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}Max256Text | 38 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}Max35Text | 44 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}Number | 50 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}PayloadData2 | 56 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}PayloadDescription2 | 63 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}SignatureEnvelope | 71 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.002.001.01}TrueFalseIndicator | 76 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 2 |
| complexType | 7 |
| element | 15 |
| fractionDigits | 1 |
| maxLength | 3 |
| minLength | 3 |
| restriction | 6 |
| schema | 1 |
| sequence | 7 |
| simpleType | 6 |
| totalDigits | 1 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
