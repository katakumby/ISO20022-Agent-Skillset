---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.006.001.12"
message_family: "seev.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.006.001.12"
source_ids: ["src-000193"]
source_editions: []
---

# seev.006.001.12 structure

[src-000193](../../../../../raw-input/securities_events_general_meeting_proxy_voting/seev.006.001.12.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.006.001.12`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.006.001.12 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}AnyBICDec2014Identifier | 15 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}CancellationProcessingStatus2 | 20 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}CancellationStatus34Choice | 26 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}CancellationStatus35Choice | 32 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}CancellationStatus6Code | 39 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}CountryCode | 46 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}DateAndPlaceOfBirth2 | 51 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}DecimalNumber | 59 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}DetailedInstructionCancellationStatus16 | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}DetailedInstructionStatus23 | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Document | 81 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}EligiblePosition17 | 86 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Exact4AlphaNumericText | 94 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}ExternalFinancialInstrumentIdentificationType1Code | 99 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}FinancialInstrumentQuantity45Choice | 105 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}GenericIdentification13 | 112 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}GenericIdentification30 | 119 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}GenericIdentification36 | 126 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}HoldingBalance13 | 133 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}ISINOct2015Identifier | 139 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}ISODate | 144 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}ISODateTime | 147 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}IdentificationSource3Choice | 150 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}IdentificationType45Choice | 156 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}ImpliedCurrencyAndAmount | 162 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}InstructionProcessingStatus6 | 169 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}InstructionStatus14Choice | 176 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}InstructionType2Choice | 183 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}InstructionTypeStatus8Choice | 189 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}LEIIdentifier | 195 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Max140Text | 200 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Max16Text | 206 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Max256Text | 212 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Max30DecimalNumber | 218 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Max350Text | 224 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Max35Text | 230 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Max4AlphaNumericText | 236 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Max50Text | 243 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Max70Text | 249 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}MeetingInstructionStatusV12 | 255 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}MeetingReference10 | 268 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}MeetingType4Code | 279 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}MeetingTypeClassification2Choice | 289 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}MeetingTypeClassification2Code | 295 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}NameAndAddress5 | 304 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}NamePrefix2Code | 310 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}NaturalPersonIdentification1 | 319 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}NoReasonCode | 325 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}OtherIdentification1 | 330 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification129Choice | 337 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification198Choice | 345 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification221 | 354 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification222 | 361 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification224 | 368 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification226Choice | 375 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification231Choice | 381 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification238 | 387 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification246Choice | 396 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification250 | 402 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PartyIdentification269 | 412 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PendingCancellationReason6Code | 421 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PendingCancellationReason7Choice | 429 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PendingCancellationStatus19Choice | 435 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PendingCancellationStatusReason14 | 441 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PendingReason41Code | 447 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PendingReason81Choice | 466 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PendingStatus84Choice | 472 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PendingStatusReason34 | 478 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PersonName1 | 484 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PersonName2 | 491 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PersonName3 | 497 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PostalAddress1 | 505 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}PostalAddress26 | 517 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}RejectedReason29Choice | 530 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}RejectedReason70Choice | 536 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}RejectedStatus31Choice | 542 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}RejectedStatus66Choice | 548 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}RejectedStatusReason28 | 554 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}RejectedStatusReason65 | 560 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}RejectionReason51Code | 566 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}RejectionReason91Code | 582 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}SecuritiesEntryType3Code | 618 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}SecurityIdentification19 | 625 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}ShortLong1Code | 632 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}SignedQuantityFormat14 | 638 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}Status11Code | 644 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}SupplementaryData1 | 657 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}SupplementaryDataEnvelope1 | 663 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.006.001.12}TypeOfIdentification4Code | 668 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 22 |
| complexType | 57 |
| element | 175 |
| enumeration | 112 |
| fractionDigits | 3 |
| maxLength | 9 |
| minInclusive | 1 |
| minLength | 9 |
| pattern | 6 |
| restriction | 33 |
| schema | 1 |
| sequence | 35 |
| simpleType | 33 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/fdf942907d7a6f0bf287c3fb.md) · [Message](index.md)
