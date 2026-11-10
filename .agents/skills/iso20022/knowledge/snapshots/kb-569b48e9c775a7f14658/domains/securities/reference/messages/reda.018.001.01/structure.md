---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.018.001.01"
message_family: "reda.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.018.001.01"
source_ids: ["src-000273"]
source_editions: ["december-2019"]
---

# reda.018.001.01 structure

[src-000273](../../../../../raw-input/target2securities_t2s/reda.018.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.018.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.018.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}AnyBICDec2014Identifier | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}CountryCode | 20 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}Document | 25 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}Exact4AlphaNumericText | 30 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}GenericIdentification30 | 35 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}GenericIdentification36 | 42 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}ISODate | 49 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}ISODateTime | 52 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}LEIIdentifier | 55 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}MarketSpecificAttribute1 | 60 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}Max16Text | 66 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}Max350Text | 72 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}Max35Text | 78 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}Max70Text | 84 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}MessageHeader1 | 90 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}NameAndAddress5 | 96 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}PartyIdentification120Choice | 102 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}PartyIdentification136 | 109 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}PostalAddress1 | 115 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}SecuritiesAccountCreationRequestV01 | 127 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}SupplementaryData1 | 134 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}SupplementaryDataEnvelope1 | 140 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}SystemPartyIdentification8 | 145 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}SystemRestriction1 | 151 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}SystemSecuritiesAccount7 | 158 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}SystemSecuritiesAccountType1Choice | 173 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}SystemSecuritiesAccountType1Code | 179 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.018.001.01}TrueFalseIndicator | 189 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 2 |
| complexType | 16 |
| element | 50 |
| enumeration | 12 |
| maxLength | 4 |
| minLength | 4 |
| pattern | 4 |
| restriction | 13 |
| schema | 1 |
| sequence | 14 |
| simpleType | 13 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
