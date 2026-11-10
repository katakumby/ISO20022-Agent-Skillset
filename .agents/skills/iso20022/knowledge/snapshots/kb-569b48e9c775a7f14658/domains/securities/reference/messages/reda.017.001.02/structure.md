---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.017.001.02"
message_family: "reda.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.017.001.02"
source_ids: ["src-000272"]
source_editions: ["march-2024"]
---

# reda.017.001.02 structure

[src-000272](../../../../../raw-input/target2securities_t2s/reda.017.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.017.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.017.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}AddressType3Choice | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}AnyBICDec2014Identifier | 21 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}BICFIDec2014Identifier | 26 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Contact14 | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}CountryCode | 50 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Document | 55 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ErrorHandling1Code | 60 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ErrorHandling2Choice | 67 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ErrorHandling3Choice | 73 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ErrorHandling4 | 79 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ErrorHandling5 | 85 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Exact4AlphaNumericText | 91 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ExternalSystemErrorHandling1Code | 96 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ExternalSystemPartyType1Code | 102 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}GenericIdentification1 | 108 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}GenericIdentification30 | 115 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}GenericIdentification36 | 122 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ISODate | 129 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ISODateTime | 132 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}LEIIdentifier | 135 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}LockStatus1Code | 140 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}MarketSpecificAttribute1 | 146 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Max128Text | 152 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Max140Text | 158 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Max16Text | 164 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Max2048Text | 170 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Max256Text | 176 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Max350Text | 182 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Max35Text | 188 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Max4Text | 194 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}Max70Text | 200 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}MessageHeader3 | 206 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}NameAndAddress5 | 215 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}NamePrefix2Code | 221 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}OriginalBusinessQuery1 | 230 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}OtherContact1 | 237 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PartyIdentification120Choice | 243 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PartyIdentification136 | 250 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PartyLockStatus1 | 256 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PartyName4 | 263 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PartyOrBusinessError4Choice | 270 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PartyOrOperationalError4Choice | 276 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PartyReport4 | 282 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PartyReportV02 | 288 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PhoneNumber | 295 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PostalAddress1 | 300 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PostalAddress28 | 312 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}PreferredContactMethod2Code | 335 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}RequestType1Code | 345 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}RequestType2Choice | 354 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}RequestType2Code | 361 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}ResidenceType1Code | 370 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}SupplementaryData1 | 377 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}SupplementaryDataEnvelope1 | 383 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}SystemParty6 | 388 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}SystemPartyIdentification8 | 404 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}SystemPartyIdentification9 | 410 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}SystemPartyType1Choice | 417 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}SystemRestriction1 | 423 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.017.001.02}TechnicalIdentification2Choice | 430 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 9 |
| complexType | 34 |
| element | 126 |
| enumeration | 35 |
| maxLength | 11 |
| minLength | 11 |
| pattern | 6 |
| restriction | 27 |
| schema | 1 |
| sequence | 25 |
| simpleType | 27 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
