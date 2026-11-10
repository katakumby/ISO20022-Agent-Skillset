---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "shared"
message_id: "head.001.001.04"
message_family: "head.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"
source_ids: ["src-000013"]
source_editions: ["march-2024"]
---

# head.001.001.04 structure

[src-000013](../../../../raw-input/business_application_header/head.001.001.04.xsd); `urn:iso:std:iso:20022:tech:xsd:head.001.001.04`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:head.001.001.04 |

| Root | Type | Line |
| --- | --- | --- |
| AppHdr | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}BusinessApplicationHeaderV04 | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}AppHdr | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}AddressType3Choice | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}AnyBICDec2014Identifier | 21 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}BICFIDec2014Identifier | 26 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}BranchAndFinancialInstitutionIdentification8 | 31 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}BranchData5 | 37 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}BusinessApplicationHeader8 | 45 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}BusinessApplicationHeaderV04 | 62 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}BusinessMessagePriorityCode | 80 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}ClearingSystemIdentification2Choice | 83 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}ClearingSystemMemberIdentification2 | 89 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Contact13 | 95 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}CopyDuplicate1Code | 112 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}CountryCode | 119 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}DateAndPlaceOfBirth1 | 124 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Exact4AlphaNumericText | 132 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}ExternalClearingSystemIdentification1Code | 137 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}ExternalFinancialInstitutionIdentification1Code | 143 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}ExternalOrganisationIdentification1Code | 149 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}ExternalPersonIdentification1Code | 155 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}FinancialIdentificationSchemeName1Choice | 161 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}FinancialInstitutionIdentification23 | 167 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}GenericFinancialIdentification1 | 177 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}GenericIdentification30 | 184 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}GenericOrganisationIdentification3 | 191 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}GenericPersonIdentification2 | 198 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}ISODate | 205 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}ISODateTime | 208 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}ImplementationSpecification1 | 211 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}LEIIdentifier | 217 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Max128Text | 222 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Max140Text | 228 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Max16Text | 234 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Max2048Text | 240 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Max256Text | 246 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Max350Text | 252 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Max35Text | 258 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Max4Text | 264 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Max70Text | 270 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}NamePrefix2Code | 276 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}OrganisationIdentification39 | 285 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}OrganisationIdentificationSchemeName1Choice | 292 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}OtherContact1 | 298 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Party51Choice | 304 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}Party52Choice | 310 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}PartyIdentification272 | 316 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}PersonIdentification18 | 325 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}PersonIdentificationSchemeName1Choice | 331 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}PhoneNumber | 337 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}PostalAddress27 | 342 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}PreferredContactMethod2Code | 364 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}SignatureEnvelope | 374 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}UnicodeChartsCode | 379 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:head.001.001.04}YesNoIndicator | 382 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 7 |
| complexType | 26 |
| element | 117 |
| enumeration | 20 |
| maxLength | 13 |
| minLength | 13 |
| pattern | 6 |
| restriction | 28 |
| schema | 1 |
| sequence | 19 |
| simpleType | 28 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
