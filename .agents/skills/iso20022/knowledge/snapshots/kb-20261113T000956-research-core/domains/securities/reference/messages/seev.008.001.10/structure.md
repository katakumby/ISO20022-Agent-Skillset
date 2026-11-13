---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.008.001.10"
message_family: "seev.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.008.001.10"
source_ids: ["src-000195"]
source_editions: []
---

# seev.008.001.10 structure

[src-000195](../../../../../raw-input/securities_events_general_meeting_proxy_voting/seev.008.001.10.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.008.001.10`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.008.001.10 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}AnyBICDec2014Identifier | 15 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}CommunicationAddress11 | 20 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}CountryCode | 26 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}DTI2024Identifier | 31 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}DateAndPlaceOfBirth2 | 36 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}DecimalNumber | 44 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Document | 50 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}EligiblePosition20 | 55 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Exact4AlphaNumericText | 64 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ExternalFinancialInstrumentIdentificationType1Code | 69 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}FinancialInstrumentQuantity18Choice | 75 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}FinancialInstrumentQuantity45Choice | 81 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}GenericIdentification13 | 88 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}GenericIdentification30 | 95 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}GenericIdentification36 | 102 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}GenericIdentification78 | 109 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}HoldingBalance14 | 115 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ISINOct2015Identifier | 123 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ISO2ALanguageCode | 128 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ISODate | 133 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ISODateTime | 136 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}IdentificationSource3Choice | 139 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}IdentificationType45Choice | 145 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ImpliedCurrencyAndAmount | 151 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ItemDescription2 | 158 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}LEIIdentifier | 165 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max1025Text | 170 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max140Text | 176 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max16Text | 182 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max2048Text | 188 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max256Text | 194 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max30DecimalNumber | 200 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max350Text | 206 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max35Text | 212 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max4AlphaNumericText | 218 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max50Text | 225 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max5NumericText | 231 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max70Text | 236 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Max8000Text | 242 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}MeetingReference10 | 248 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}MeetingResultDisseminationV10 | 259 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}MeetingType4Code | 273 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}MeetingTypeClassification2Choice | 283 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}MeetingTypeClassification2Code | 289 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}NameAndAddress5 | 298 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}NamePrefix2Code | 304 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}NaturalPersonIdentification1 | 313 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}NotificationType2Code | 319 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Number | 325 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}OtherIdentification1 | 331 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Pagination1 | 338 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Participation6 | 344 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PartyIdentification129Choice | 352 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PartyIdentification198Choice | 360 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PartyIdentification221 | 369 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PartyIdentification231Choice | 376 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PartyIdentification238 | 382 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PartyIdentification246Choice | 391 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PartyIdentification250 | 397 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PartyIdentification269 | 407 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Percentage14Rate | 416 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PersonName2 | 422 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PersonName3 | 428 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PostalAddress1 | 436 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}PostalAddress26 | 448 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ProprietaryVote2 | 461 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ResolutionStatus2Code | 467 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ResolutionSubStatus1Code | 474 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SafekeepingPlace1Code | 480 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SafekeepingPlace2Code | 488 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SafekeepingPlaceFormat42Choice | 494 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SafekeepingPlaceTypeAndIdentification1 | 503 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SafekeepingPlaceTypeAndText6 | 509 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SecuritiesEntryType2Code | 515 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SecurityIdentification19 | 534 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SecurityPosition22 | 541 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}ShortLong1Code | 547 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SignedQuantityFormat14 | 553 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SupplementaryData1 | 559 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}SupplementaryDataEnvelope1 | 565 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}TypeOfIdentification4Code | 570 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}Vote20 | 583 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.008.001.10}YesNoIndicator | 604 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 10 |
| complexType | 44 |
| element | 164 |
| enumeration | 61 |
| fractionDigits | 5 |
| maxLength | 12 |
| minInclusive | 1 |
| minLength | 12 |
| pattern | 9 |
| restriction | 40 |
| schema | 1 |
| sequence | 34 |
| simpleType | 40 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/67fc79c71a98fd012efc7184.md) · [Message](index.md)
