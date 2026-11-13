---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.015.001.04"
message_family: "camt.015"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04"
source_ids: ["src-000029"]
source_editions: ["2024-2025"]
---

# camt.015.001.04 structure

[src-000029](../../../../../raw-input/cash_management/camt.015.001.04.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.015.001.04`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.015.001.04 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}BICFIDec2014Identifier | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}ClearingSystemIdentification2Choice | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}ClearingSystemMemberIdentification2 | 16 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}CommunicationAddress8 | 22 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}ContactIdentificationAndAddress1 | 30 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}CountryCode | 37 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}Document | 42 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}ExternalClearingSystemIdentification1Code | 47 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}ExternalFinancialInstitutionIdentification1Code | 53 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}FinancialIdentificationSchemeName1Choice | 59 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}GenericFinancialIdentification1 | 65 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}ISODateTime | 72 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}LongPostalAddress1Choice | 75 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}Max140Text | 81 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}Max16Text | 87 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}Max256Text | 93 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}Max350Text | 99 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}Max35Text | 105 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}Member6 | 111 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}MemberIdentification3Choice | 118 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}MessageHeader1 | 125 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}ModifyMemberV04 | 131 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}PaymentRole1Code | 139 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}PhoneNumber | 149 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}StructuredLongPostalAddress1 | 154 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}SupplementaryData1 | 170 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.015.001.04}SupplementaryDataEnvelope1 | 176 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 4 |
| complexType | 15 |
| element | 46 |
| enumeration | 6 |
| maxLength | 7 |
| minLength | 7 |
| pattern | 3 |
| restriction | 12 |
| schema | 1 |
| sequence | 11 |
| simpleType | 12 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/871e2179b9cf7121e9cd5390.md) · [Message](index.md)
