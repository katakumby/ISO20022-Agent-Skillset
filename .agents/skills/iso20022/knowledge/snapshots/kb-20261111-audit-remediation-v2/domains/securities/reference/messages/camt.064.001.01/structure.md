---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "camt.064.001.01"
message_family: "camt.064"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01"
source_ids: ["src-000240"]
source_editions: ["february-2025"]
---

# camt.064.001.01 structure

[src-000240](../../../../../raw-input/target2securities_t2s/camt.064.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.064.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.064.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}ActiveCurrencyCode | 17 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}AddressType2Code | 22 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}AnyBICDec2014Identifier | 32 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}CountryCode | 37 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}Document | 42 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}ExternalAccountIdentification1Code | 47 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}GenericAccountIdentification1 | 53 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}GenericIdentification36 | 60 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}IBAN2007Identifier | 67 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}ISODate | 72 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}ISODateTime | 75 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}LEIIdentifier | 78 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}LimitType4Code | 83 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}LimitUtilisationJournalQueryV01 | 90 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}LimitUtilisationJournalSearchCriteria2 | 97 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}Max16Text | 107 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}Max34Text | 113 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}Max350Text | 119 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}Max35Text | 125 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}Max70Text | 131 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}MessageHeader1 | 137 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}NameAndAddress5 | 143 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}PartyIdentification120Choice | 149 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}PartyIdentification136 | 156 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}PostalAddress1 | 162 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}SupplementaryData1 | 174 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}SupplementaryDataEnvelope1 | 180 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.064.001.01}SystemPartyIdentification8 | 185 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 3 |
| complexType | 15 |
| element | 42 |
| enumeration | 9 |
| maxLength | 6 |
| minLength | 6 |
| pattern | 5 |
| restriction | 15 |
| schema | 1 |
| sequence | 12 |
| simpleType | 15 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
