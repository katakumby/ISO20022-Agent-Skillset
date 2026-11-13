---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.001.001.13"
message_family: "seev.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.001.001.13"
source_ids: ["src-000188"]
source_editions: []
---

# seev.001.001.13 structure

[src-000188](../../../../../raw-input/securities_events_general_meeting_proxy_voting/seev.001.001.13.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.001.001.13`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.001.001.13 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ActiveOrHistoricCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ActiveOrHistoricCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}AdditionalRight1Code | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}AdditionalRightCode1Choice | 31 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}AdditionalRightThreshold2Choice | 37 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}AdditionalRights4 | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}AddressType2Code | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}AgentRole1Code | 62 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}AnyBICDec2014Identifier | 68 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Attendance2 | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}AttendanceAdmissionConditions2 | 81 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}AttendanceAdmissionConditions2Code | 87 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}CommunicationAddress11 | 100 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}CommunicationAddress12 | 106 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ContactIdentification1 | 111 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}CorporateEventNarrative4 | 122 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}CountryCode | 128 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DTI2024Identifier | 133 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateAndDateTime2Choice | 138 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateAndPlaceOfBirth2 | 144 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateCode34Choice | 152 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateFormat1 | 158 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateFormat3Choice | 164 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateFormat58Choice | 170 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateFormat60Choice | 176 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateMode1Code | 182 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateType10Code | 188 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DateType1Code | 197 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}DecimalNumber | 202 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Document | 208 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}EligiblePosition18 | 213 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Entitlement1Choice | 222 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}EventCompletenessStatus1Code | 228 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}EventConfirmationStatus1Code | 234 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}EventStatus1 | 240 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Exact4AlphaNumericText | 246 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ExternalFinancialInstrumentIdentificationType1Code | 251 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}FinancialInstrumentQuantity18Choice | 257 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}FinancialInstrumentQuantity45Choice | 263 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}GenericIdentification13 | 270 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}GenericIdentification30 | 277 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}GenericIdentification36 | 284 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}GenericIdentification78 | 291 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}HoldingBalance14 | 297 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ISINOct2015Identifier | 305 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ISO2ALanguageCode | 310 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ISODate | 315 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ISODateTime | 318 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}IdentificationSource3Choice | 321 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}IdentificationType45Choice | 327 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ImpliedCurrencyAndAmount | 333 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}IncentivePremium6 | 340 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}IncentivePremiumType2Choice | 348 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}IndividualPerson43 | 355 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}InvestorClassificationType1Code | 361 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}InvestorTypeIdentification1 | 370 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}IssuerAgent3 | 376 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}IssuerInformation3 | 382 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ItemDescription2 | 388 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}LEIIdentifier | 395 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}LanguageSpecifiedNarrative1 | 400 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}LocationFormat1Choice | 406 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MICIdentifier | 412 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MailAddress1 | 417 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max1025Text | 423 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max140Text | 429 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max16Text | 435 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max2048Text | 441 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max256Text | 447 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max30DecimalNumber | 453 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max350Text | 459 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max35Text | 465 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max4AlphaNumericText | 471 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max50Text | 478 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max5NumericText | 484 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max70Text | 489 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Max8000Text | 495 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Meeting7 | 501 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MeetingContactPerson3 | 511 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MeetingDateStatus2Code | 518 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MeetingEventReference1 | 524 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MeetingEventReference1Choice | 530 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MeetingNotice10 | 536 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MeetingNotificationV13 | 563 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MeetingType4Code | 581 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MeetingTypeClassification2Choice | 591 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}MeetingTypeClassification2Code | 597 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}NameAndAddress5 | 606 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}NamePrefix1Code | 612 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}NamePrefix2Code | 620 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}NaturalPersonIdentification1 | 629 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}NotificationGeneralInformation4 | 635 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}NotificationType3Code | 644 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}NotificationUpdate2 | 651 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Number | 657 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}NumberOrPercentage2Choice | 663 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}OtherIdentification1 | 669 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Pagination1 | 676 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ParticipationMethod3 | 682 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ParticipationMethod3Choice | 692 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PartyIdentification129Choice | 698 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PartyIdentification198Choice | 706 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PartyIdentification221 | 715 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PartyIdentification231Choice | 722 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PartyIdentification232Choice | 728 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PartyIdentification238 | 734 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PartyIdentification246Choice | 743 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PartyIdentification250 | 749 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PartyIdentification269 | 759 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Percentage14Rate | 768 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PersonName2 | 774 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PersonName3 | 780 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PhoneNumber | 788 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PlaceType1Code | 793 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PostalAddress1 | 798 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PostalAddress26 | 810 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PowerOfAttorneyLegalisation1Code | 823 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PowerOfAttorneyRequirements4 | 831 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}PriceRateOrAmount8Choice | 838 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ProcessingPosition3Code | 844 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Proxy11 | 852 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Proxy5Choice | 858 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ProxyAppointmentInformation6 | 864 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ProxyNotAllowed1Code | 872 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ProxyType3Code | 877 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}QuorumQuantity2Choice | 885 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}Resolution8 | 891 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ResolutionStatus1Code | 910 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ResolutionType2Code | 916 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SafekeepingPlace1Code | 922 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SafekeepingPlace2Code | 930 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SafekeepingPlaceFormat42Choice | 936 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SafekeepingPlaceTypeAndIdentification1 | 945 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SafekeepingPlaceTypeAndText6 | 951 |
| [type-0137](types/type-0137.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SecuritiesEntryType2Code | 957 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SecurityIdentification19 | 976 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SecurityPosition20 | 983 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ShortLong1Code | 989 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SignedQuantityFormat14 | 995 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SupplementaryData1 | 1001 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}SupplementaryDataEnvelope1 | 1007 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ThresholdBasis1Choice | 1012 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}ThresholdBasis1Code | 1018 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}TypeOfIdentification4Code | 1025 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteChannel1Code | 1038 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteInstruction5Code | 1044 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteInstruction6Code | 1059 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteInstructionType1 | 1076 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteInstructionType1Choice | 1082 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteMethods5 | 1088 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteParameters10 | 1096 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteThroughNetwork1Choice | 1119 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteType1Code | 1125 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VoteTypeAndQuantity1 | 1131 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VotingParticipationMethod3Code | 1137 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}VotingRightsThreshold2 | 1147 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.001.001.13}YesNoIndicator | 1153 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 30 |
| complexType | 92 |
| element | 320 |
| enumeration | 149 |
| extension | 1 |
| fractionDigits | 6 |
| maxLength | 12 |
| minInclusive | 2 |
| minLength | 12 |
| pattern | 12 |
| restriction | 66 |
| schema | 1 |
| sequence | 61 |
| simpleContent | 1 |
| simpleType | 66 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/aa6321b886559a8ce8a906c2.md) · [Message](index.md)
