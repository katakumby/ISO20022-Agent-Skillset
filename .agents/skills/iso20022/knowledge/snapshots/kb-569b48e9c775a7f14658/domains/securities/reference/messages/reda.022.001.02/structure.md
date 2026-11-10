---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.022.001.02"
message_family: "reda.022"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.022.001.02"
source_ids: ["src-000277"]
source_editions: ["march-2024"]
---

# reda.022.001.02 structure

[src-000277](../../../../../raw-input/target2securities_t2s/reda.022.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.022.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.022.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}AddressType3Choice | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}AnyBICDec2014Identifier | 21 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}BICFIDec2014Identifier | 26 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Contact14 | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}CountryCode | 50 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}DataModification1Code | 55 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Document | 62 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Exact4AlphaNumericText | 67 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}GenericIdentification30 | 72 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}GenericIdentification36 | 79 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}ISODate | 86 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}ISODateTime | 89 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}LEIIdentifier | 92 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}LockStatus1Code | 97 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}MarketSpecificAttribute1 | 103 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Max128Text | 109 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Max140Text | 115 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Max16Text | 121 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Max2048Text | 127 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Max256Text | 133 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Max350Text | 139 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Max35Text | 145 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Max4Text | 151 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}Max70Text | 157 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}MessageHeader1 | 163 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}NameAndAddress5 | 169 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}NamePrefix2Code | 175 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}OtherContact1 | 184 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}PartyIdentification120Choice | 190 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}PartyIdentification136 | 197 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}PartyLockStatus1 | 203 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}PartyModificationRequestV02 | 210 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}PartyName3 | 218 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}PhoneNumber | 225 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}PostalAddress1 | 230 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}PostalAddress28 | 242 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}PreferredContactMethod2Code | 265 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}ResidenceType1Code | 275 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}SupplementaryData1 | 282 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}SupplementaryDataEnvelope1 | 288 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}SystemParty2 | 293 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}SystemPartyIdentification10 | 299 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}SystemPartyIdentification8 | 305 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}SystemPartyModification3 | 311 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}SystemPartyModification3Choice | 317 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}SystemRestriction1 | 331 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.022.001.02}TechnicalIdentification2Choice | 338 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 4 |
| complexType | 25 |
| element | 100 |
| enumeration | 25 |
| maxLength | 9 |
| minLength | 9 |
| pattern | 6 |
| restriction | 23 |
| schema | 1 |
| sequence | 21 |
| simpleType | 23 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
