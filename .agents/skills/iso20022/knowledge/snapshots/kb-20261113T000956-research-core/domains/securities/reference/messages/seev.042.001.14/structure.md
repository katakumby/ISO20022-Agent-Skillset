---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.042.001.14"
message_family: "seev.042"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.042.001.14"
source_ids: ["src-000093"]
source_editions: ["2025-2026"]
---

# seev.042.001.14 structure

[src-000093](../../../../../raw-input/corporate_actions/seev.042.001.14.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.042.001.14`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.042.001.14 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}AccountIdentification77 | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ActiveCurrencyAnd13DecimalAmount_SimpleType | 14 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ActiveCurrencyAnd13DecimalAmount | 21 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ActiveCurrencyCode | 28 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}AmountPrice3 | 33 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}AmountPriceType1Code | 39 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}AnyBICDec2014Identifier | 47 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}BalanceFormat11Choice | 52 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CancelledReason8Choice | 59 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CancelledStatus12Choice | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CancelledStatusReason11 | 71 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CancelledStatusReason6Code | 77 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionBalance52 | 86 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionEventAndBalance28 | 107 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionEventDeadlines3 | 115 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionEventType112Choice | 124 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionEventType40Code | 130 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionInstructionStatementReportV14 | 199 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionMandatoryVoluntary1Code | 207 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionMandatoryVoluntary3Choice | 214 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionOption11Code | 220 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionOption30Choice | 245 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionStatementReportingType1Code | 251 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CorporateActionStatementType2Code | 257 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}CountryCode | 265 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DTI2024Identifier | 270 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateAndDateTime2Choice | 275 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateCode19Choice | 281 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateCode21Choice | 287 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateCodeAndTimeFormat3 | 293 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateFormat43Choice | 299 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateFormat44Choice | 305 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateOrDateTimePeriod1Choice | 312 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DatePeriod2 | 318 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateTimePeriod1 | 324 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateType7Code | 330 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DateType8Code | 335 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DecimalNumber | 341 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DefaultProcessingOrStandingInstruction2Choice | 347 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}DeliveryReceiptType2Code | 353 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Document | 359 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}EventFrequency4Code | 364 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}EventInformation17 | 374 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Exact3NumericText | 383 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Exact4AlphaNumericText | 388 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ExternalFinancialInstrumentIdentificationType1Code | 393 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}FinancialInstrumentQuantity33Choice | 399 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Frequency25Choice | 407 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}GenericIdentification30 | 413 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}GenericIdentification36 | 420 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}GenericIdentification78 | 427 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ISINOct2015Identifier | 433 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ISODate | 438 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ISODateTime | 441 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ISOTime | 444 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}IdentificationSource3Choice | 447 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ImpliedCurrencyAndAmount | 453 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}InstructedBalance22 | 460 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}InstructedCorporateActionOption23 | 471 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}InstructionProcessingStatus62Choice | 487 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max140Text | 500 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max15Text | 506 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max16Text | 512 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max210Text | 518 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max30DecimalNumber | 524 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max350Text | 530 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max35Text | 536 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max3NumericText | 542 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max50Text | 547 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Max5NumericText | 553 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}NoReasonCode | 558 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}NoSpecifiedReason1 | 563 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}NotificationIdentification5 | 568 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}OptionInstructionDetails13 | 574 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}OriginalAndCurrentQuantities6 | 590 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}OtherIdentification1 | 597 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Pagination1 | 604 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PartyIdentification127Choice | 610 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PendingBalance7 | 616 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PendingCancellationReason5Choice | 622 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PendingCancellationReason5Code | 628 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PendingCancellationStatus21Choice | 637 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PendingCancellationStatusReason16 | 643 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PendingReason38Code | 649 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PendingReason82Choice | 671 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PendingStatus85Choice | 677 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PendingStatusReason35 | 683 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Percentage14Rate | 689 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PercentagePrice2 | 695 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PriceFormat74Choice | 701 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PriceRateType3Code | 708 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}PriceValueType10Code | 716 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ProprietaryQuantity7 | 721 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ProprietaryQuantity8 | 730 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ProtectTransactionType2Code | 738 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Quantity48Choice | 745 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Quantity49Choice | 751 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Quantity50Choice | 757 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}RejectedReason58Choice | 763 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}RejectedStatus58Choice | 769 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}RejectedStatusReason57 | 775 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}RejectionReason86Code | 781 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ReturnedReason2Choice | 823 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ReturnedStatus1Code | 829 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ReturnedStatus2Choice | 835 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ReturnedStatusReason2 | 841 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SafekeepingPlace1Code | 847 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SafekeepingPlace2Code | 855 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SafekeepingPlaceFormat42Choice | 861 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SafekeepingPlaceTypeAndIdentification1 | 870 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SafekeepingPlaceTypeAndText6 | 876 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SecurityIdentification19 | 882 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SettlementTypeAndIdentification25 | 889 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}ShortLong1Code | 896 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SignedQuantityFormat10 | 902 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SignedQuantityFormat11 | 908 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}Statement72 | 914 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}StatementUpdateType1Code | 928 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SupplementaryData1 | 934 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}SupplementaryDataEnvelope1 | 940 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}UpdateType15Choice | 945 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.042.001.14}YesNoIndicator | 951 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 32 |
| complexType | 73 |
| element | 228 |
| enumeration | 197 |
| extension | 1 |
| fractionDigits | 5 |
| maxLength | 8 |
| minInclusive | 2 |
| minLength | 8 |
| pattern | 9 |
| restriction | 49 |
| schema | 1 |
| sequence | 40 |
| simpleContent | 1 |
| simpleType | 49 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/08aaa19733522db335eb1a9a.md) · [Message](index.md)
