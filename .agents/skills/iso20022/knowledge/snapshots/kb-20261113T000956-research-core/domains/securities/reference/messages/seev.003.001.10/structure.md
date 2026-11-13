---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.003.001.10"
message_family: "seev.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.003.001.10"
source_ids: ["src-000190"]
source_editions: []
---

# seev.003.001.10 structure

[src-000190](../../../../../raw-input/securities_events_general_meeting_proxy_voting/seev.003.001.10.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.003.001.10`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.003.001.10 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}AnyBICDec2014Identifier | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}CountryCode | 20 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}DTI2024Identifier | 25 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}DateAndPlaceOfBirth2 | 30 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}DecimalNumber | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Document | 44 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}EligibilityDates1 | 49 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}EligiblePosition19 | 54 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Exact4AlphaNumericText | 63 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}ExternalFinancialInstrumentIdentificationType1Code | 68 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}FinancialInstrumentQuantity45Choice | 74 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}GenericIdentification13 | 81 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}GenericIdentification30 | 88 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}GenericIdentification36 | 95 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}GenericIdentification78 | 102 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}HoldingBalance14 | 108 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}ISINOct2015Identifier | 116 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}ISODate | 121 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}ISODateTime | 124 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}IdentificationSource3Choice | 127 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}IdentificationType45Choice | 133 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}ImpliedCurrencyAndAmount | 139 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}LEIIdentifier | 146 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Max140Text | 151 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Max16Text | 157 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Max256Text | 163 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Max30DecimalNumber | 169 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Max350Text | 175 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Max35Text | 181 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Max4AlphaNumericText | 187 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Max50Text | 194 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}Max70Text | 200 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}MeetingEntitlementNotificationV10 | 206 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}MeetingReference10 | 219 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}MeetingType4Code | 230 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}MeetingTypeClassification2Choice | 240 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}MeetingTypeClassification2Code | 246 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}NameAndAddress5 | 255 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}NamePrefix2Code | 261 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}NaturalPersonIdentification1 | 270 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}NotificationType2Code | 276 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}OrganisationIdentification5 | 282 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}OtherIdentification1 | 288 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyAdditionalIdentification2Choice | 295 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification129Choice | 301 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification198Choice | 309 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification221 | 318 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification231Choice | 325 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification232Choice | 331 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification238 | 337 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification241 | 346 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification246Choice | 352 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification250 | 358 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification269 | 368 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PartyIdentification270 | 377 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PersonName2 | 383 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PersonName3 | 389 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PostalAddress1 | 397 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}PostalAddress26 | 409 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SafekeepingPlace1Code | 422 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SafekeepingPlace2Code | 430 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SafekeepingPlaceFormat42Choice | 436 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SafekeepingPlaceTypeAndIdentification1 | 445 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SafekeepingPlaceTypeAndText6 | 451 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SecuritiesEntryType2Code | 457 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SecurityIdentification19 | 476 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SecurityPosition21 | 483 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}ShortLong1Code | 489 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SignedQuantityFormat14 | 495 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SupplementaryData1 | 501 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}SupplementaryDataEnvelope1 | 507 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.003.001.10}TypeOfIdentification4Code | 512 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 11 |
| complexType | 43 |
| element | 142 |
| enumeration | 56 |
| fractionDigits | 3 |
| maxLength | 9 |
| minInclusive | 1 |
| minLength | 9 |
| pattern | 7 |
| restriction | 30 |
| schema | 1 |
| sequence | 32 |
| simpleType | 30 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/51bb32450d96be999c0a9d8a.md) · [Message](index.md)
