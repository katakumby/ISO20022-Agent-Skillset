---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.043.001.02"
message_family: "reda.043"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.043.001.02"
source_ids: ["src-000298"]
source_editions: ["march-2024"]
---

# reda.043.001.02 structure

[src-000298](../../../../../raw-input/target2securities_t2s/reda.043.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.043.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.043.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}AddressType3Choice | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}AnyBICDec2014Identifier | 21 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}BICFIDec2014Identifier | 26 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}CodeOrProprietary1Choice | 31 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Contact14 | 37 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}CountryCode | 56 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}DatePeriod2 | 61 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}DatePeriod3Choice | 67 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Document | 75 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}ErrorHandling3Choice | 80 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}ErrorHandling5 | 86 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Exact4AlphaNumericText | 92 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}ExternalSystemErrorHandling1Code | 97 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}ExternalSystemPartyType1Code | 103 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}GenericIdentification13 | 109 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}GenericIdentification30 | 116 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}GenericIdentification36 | 123 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}ISODate | 130 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}ISODateTime | 133 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}LEIIdentifier | 136 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}LockStatus1Code | 141 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}MarketSpecificAttribute1 | 147 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max128Text | 153 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max140Text | 159 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max16Text | 165 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max2048Text | 171 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max256Text | 177 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max350Text | 183 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max35Text | 189 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max4AlphaNumericText | 195 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max4Text | 202 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Max70Text | 208 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}MessageHeader12 | 214 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}NameAndAddress5 | 221 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}NamePrefix2Code | 227 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}OriginalBusinessInstruction1 | 236 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}OtherContact1 | 243 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PartyAuditTrail2 | 249 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PartyAuditTrailOrError3Choice | 257 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PartyAuditTrailOrError4Choice | 263 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PartyAuditTrailReport4 | 269 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PartyAuditTrailReportV02 | 276 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PartyIdentification120Choice | 283 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PartyIdentification136 | 290 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PartyLockStatus1 | 296 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PartyName4 | 303 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PhoneNumber | 310 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PostalAddress1 | 315 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PostalAddress28 | 327 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}PreferredContactMethod2Code | 350 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}ResidenceType1Code | 360 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}Restriction1 | 367 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}SupplementaryData1 | 374 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}SupplementaryDataEnvelope1 | 380 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}SystemPartyIdentification8 | 385 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}SystemPartyType1Choice | 391 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}TechnicalIdentification2Choice | 397 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogAddress2 | 403 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogContact2 | 409 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogDate1 | 415 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogMarketSpecificAttribute1 | 421 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogPartyLockStatus1 | 427 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogPartyName1 | 433 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogPartyRecord2Choice | 439 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogProprietary1 | 455 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogResidenceType1 | 462 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogRestriction1 | 468 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogSystemPartyType1 | 474 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.043.001.02}UpdateLogTechnicalAddress1 | 480 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 10 |
| complexType | 45 |
| element | 150 |
| enumeration | 22 |
| maxLength | 12 |
| minLength | 12 |
| pattern | 7 |
| restriction | 25 |
| schema | 1 |
| sequence | 35 |
| simpleType | 25 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
