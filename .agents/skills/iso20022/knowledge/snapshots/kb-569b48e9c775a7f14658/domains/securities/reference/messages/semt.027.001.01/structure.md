---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.027.001.01"
message_family: "semt.027"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.027.001.01"
source_ids: ["src-000310"]
source_editions: ["march-2026"]
---

# semt.027.001.01 structure

[src-000310](../../../../../raw-input/target2securities_t2s/semt.027.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.027.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.027.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}AcknowledgedAcceptedStatus21Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}AcknowledgementReason12Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}AcknowledgementReason5Code | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}AcknowledgementReason9 | 30 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ActiveOrHistoricCurrencyCode | 50 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}AddressType2Code | 55 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}AmountAndDirection20 | 65 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}AnyBICDec2014Identifier | 71 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}AutoBorrowing1Code | 76 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}AutomaticBorrowing6Choice | 83 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}BeneficialOwnership4Choice | 89 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}BlockTrade1Code | 95 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}BlockTrade4Choice | 101 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CancellationReason22 | 107 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CancellationReason36Choice | 113 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CancellationStatus24Choice | 119 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CancelledStatusReason16Code | 125 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CashSettlementSystem2Code | 142 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CashSettlementSystem4Choice | 148 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CentralCounterPartyEligibility4Choice | 154 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CorporateActionEventType28Code | 160 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CorporateActionEventType73Choice | 233 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CountryCode | 239 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}CreditDebitCode | 244 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}DateAndDateTime2Choice | 250 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}DateType3Code | 256 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}DateType4Code | 261 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}DecimalNumber | 267 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}DeliveryReceiptType2Code | 273 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}DeliveryReturn1Code | 279 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}DeliveryReturn3Choice | 290 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Document | 296 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}DocumentNumber5Choice | 301 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Exact3NumericText | 308 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Exact4AlphaNumericText | 313 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Exact4NumericText | 318 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ExposureType15Code | 323 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ExposureType25Choice | 361 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ExternalFinancialInstrumentIdentificationType1Code | 367 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}FXStandingInstruction4Choice | 373 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}FailingReason13 | 379 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}FailingReason18Choice | 385 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}FailingReason5Code | 391 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}FailingStatus15Choice | 459 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}FinancialInstrumentQuantity1Choice | 465 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}GeneratedReason3Code | 472 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}GeneratedReason5 | 483 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}GeneratedReasons5Choice | 489 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}GeneratedStatus7Choice | 495 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}GenericIdentification30 | 501 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}GenericIdentification36 | 508 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}GenericIdentification78 | 515 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}HoldIndicator6 | 521 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ISINOct2015Identifier | 527 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ISO20022MessageIdentificationText | 532 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ISODate | 537 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ISODateTime | 540 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}IdentificationSource3Choice | 543 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ImpliedCurrencyAndAmount | 549 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}InstructionProcessingStatus63Choice | 556 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}LEIIdentifier | 568 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}LetterOfGuarantee4Choice | 573 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Linkages57 | 579 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}MICIdentifier | 587 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}MarketClientSide1Code | 592 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}MarketClientSide6Choice | 598 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}MarketIdentification1Choice | 604 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}MarketIdentification84 | 610 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}MarketType2Code | 616 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}MarketType8Choice | 625 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}MatchingStatus24Choice | 631 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Max140Text | 638 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Max16Text | 644 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Max210Text | 650 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Max350Text | 656 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Max35Text | 662 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Max3Number | 668 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Max5NumericText | 674 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Max70Text | 679 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ModificationCancellationAllowed4Choice | 685 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}NameAndAddress5 | 691 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}NettingEligibility4Choice | 697 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}NoReasonCode | 703 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}OtherIdentification1 | 708 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}OwnershipLegalRestrictions1Code | 715 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Pagination1 | 722 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PartyIdentification120Choice | 728 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PartyIdentification122Choice | 735 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PartyIdentification127Choice | 742 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PartyIdentification136 | 748 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PartyIdentification148 | 754 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PartyIdentificationAndAccount170 | 761 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingProcessingReason17 | 769 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingProcessingReason19Choice | 775 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingProcessingReason5Code | 781 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingProcessingStatus20Choice | 812 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingReason28Code | 818 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingReason32 | 884 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingReason32Code | 890 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingReason35 | 900 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingReason69Choice | 906 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingReason77Choice | 912 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingStatus73Choice | 918 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PendingStatus81Choice | 924 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PlaceOfClearingIdentification2 | 930 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PlaceOfTradeIdentification1 | 936 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PostalAddress1 | 942 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}PriorityNumeric4Choice | 954 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ProcessingPosition3Code | 960 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ProcessingPosition7Choice | 968 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ProprietaryReason4 | 974 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ProprietaryStatusAndReason6 | 980 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}ReceiveDelivery1Code | 986 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}References34Choice | 992 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Registration10Choice | 1003 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Registration1Code | 1009 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Registration2Code | 1015 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Registration9Choice | 1023 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}RegistrationReason5 | 1029 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}RepairReason10Choice | 1035 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}RepairReason4Code | 1041 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}RepairReason8 | 1074 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}RepairStatus12Choice | 1080 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}RepurchaseType10Code | 1086 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}RepurchaseType23Choice | 1097 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Restriction5Choice | 1103 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SafeKeepingPlace3 | 1109 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SafekeepingPlace1Code | 1115 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SafekeepingPlace3Code | 1123 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SafekeepingPlaceFormat29Choice | 1128 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SafekeepingPlaceTypeAndIdentification1 | 1136 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SafekeepingPlaceTypeAndText8 | 1142 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SecuritiesAccount19 | 1148 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SecuritiesRTGS4Choice | 1155 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SecuritiesReport2 | 1161 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SecuritiesSettlementTransactionQueryResponseV01 | 1169 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SecuritiesSettlementTransactions6 | 1176 |
| [type-0141](types/type-0141.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SecuritiesTransactionType27Code | 1184 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SecuritiesTransactionType48Choice | 1234 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SecurityIdentification19 | 1240 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementDate19Choice | 1247 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementDateCode8Choice | 1253 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementDetails235 | 1259 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementOrCorporateActionEvent26Choice | 1293 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementParties78 | 1299 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementQueryType1Code | 1309 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementStatus32Choice | 1316 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementSystemMethod1Code | 1323 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementSystemMethod4Choice | 1329 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementTransactionCondition12Code | 1335 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementTransactionCondition34Choice | 1365 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlementTransactionCondition5Code | 1371 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlingCapacity2Code | 1379 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SettlingCapacity7Choice | 1387 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}StatusAndReason52 | 1393 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SupplementaryData1 | 1403 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SupplementaryDataEnvelope1 | 1409 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}SystemPartyIdentification8 | 1414 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}TaxCapacityParty4Choice | 1420 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}TaxLiability1Code | 1426 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Tracking4Choice | 1432 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}TradeDate8Choice | 1438 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}TradeDateCode3Choice | 1444 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}Transaction169 | 1450 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}TransactionActivity1Code | 1472 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}TransactionActivity3Choice | 1481 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}TransactionDetails187 | 1487 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}UTIIdentifier | 1528 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}UnmatchedReason11Code | 1533 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}UnmatchedReason15 | 1577 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}UnmatchedReason21Choice | 1583 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}UnmatchedStatus16Choice | 1589 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.027.001.01}YesNoIndicator | 1595 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 64 |
| complexType | 110 |
| element | 343 |
| enumeration | 512 |
| extension | 1 |
| fractionDigits | 4 |
| maxLength | 8 |
| minInclusive | 2 |
| minLength | 8 |
| pattern | 12 |
| restriction | 65 |
| schema | 1 |
| sequence | 45 |
| simpleContent | 1 |
| simpleType | 65 |
| totalDigits | 4 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
