---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.044.001.04"
message_family: "setr.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.044.001.04"
source_ids: ["src-000187"]
source_editions: ["2024-2025"]
---

# setr.044.001.04 structure

[src-000187](../../../../../raw-input/post_trade_matching/setr.044.001.04.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.044.001.04`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.044.001.04 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AccountIdentification55Choice | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ActiveCurrencyAndAmount_SimpleType | 13 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ActiveCurrencyAndAmount | 20 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ActiveCurrencyCode | 27 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 32 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ActiveOrHistoricCurrencyAnd13DecimalAmount | 39 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ActiveOrHistoricCurrencyAndAmount_SimpleType | 46 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ActiveOrHistoricCurrencyAndAmount | 53 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ActiveOrHistoricCurrencyCode | 60 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AddressType2Code | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AffirmationReason2 | 75 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AffirmationReason2Choice | 81 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AffirmationStatus11Choice | 87 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AllegementMatchingReason2 | 94 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AllegementReason1Code | 100 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AllegementReason2Choice | 105 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AlternatePartyIdentification8 | 111 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AmountAndDirection29 | 118 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AmountOrRate2Choice | 126 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AnyBICDec2014Identifier | 132 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AwaitingAffirmationReason1Code | 137 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AwaitingAffirmationReason2 | 142 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AwaitingAffirmationReason2Choice | 148 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AwaitingCancellationReason1Code | 154 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AwaitingCancellationReason2 | 159 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}AwaitingCancellationReason2Choice | 165 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}BBANIdentifier | 171 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}BaseOneRate | 176 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}BusinessProcessType1Code | 182 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}BusinessProcessType2Choice | 194 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CalculationType1Code | 200 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CallIn1Code | 237 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CancellationProcessingStatus10Choice | 244 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CancellationReason39Choice | 252 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CashAccountIdentification5Choice | 258 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CashMarginOrder1Code | 264 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ChargeTaxBasis1Code | 271 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ChargeTaxBasisType2Choice | 277 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Commission25 | 283 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CommissionType6Choice | 294 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CommissionType9Code | 300 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ConfirmationParties9 | 315 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ConfirmationPartyDetails11 | 332 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ConfirmationPartyDetails12 | 340 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ConfirmationPartyDetails14 | 350 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ConfirmationPartyDetails16 | 361 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CountryCode | 373 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CreditDebitCode | 378 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}CurrencyToBuyOrSell1Choice | 384 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}DateAndDateTime1Choice | 390 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}DateTimePeriod1 | 396 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}DateTimePeriod1Choice | 402 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}DecimalNumber | 409 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}DeliveryReceiptType2Code | 415 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Document | 421 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}DocumentNumber17Choice | 426 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}EUCapitalGain2Code | 433 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}EUCapitalGainType3Choice | 440 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Eligibility1Code | 446 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Exact3NumericText | 453 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Exact4AlphaNumericText | 458 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ExternalFinancialInstrumentIdentificationType1Code | 463 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ExternalTradeTransactionCondition1Code | 469 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}FinancialInstrumentQuantity1Choice | 475 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ForeignExchangeTerms18 | 482 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}GenericIdentification30 | 490 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}GenericIdentification36 | 497 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}GenericIdentification37 | 504 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}IBAN2007Identifier | 510 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ISINOct2015Identifier | 515 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ISO20022MessageIdentificationText | 520 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ISODate | 525 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ISODateTime | 528 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}IdentificationReference16Choice | 531 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}IdentificationSource3Choice | 550 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}IdentificationType43Choice | 556 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ImpliedCurrencyAndAmount | 562 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}InstructionProcessingReason3Choice | 569 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}InstructionProcessingReason4Choice | 575 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}InterestType2Code | 581 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}InvestorCapacity4Choice | 587 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Linkages77 | 593 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MICIdentifier | 599 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MarketIdentification3Choice | 604 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MarketIdentification93 | 610 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MarketIdentification97 | 616 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MarketType18Choice | 622 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MarketType2Code | 628 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MarketType6Code | 637 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MarketType8Choice | 644 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MatchingReason5Choice | 650 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MatchingReason6Choice | 656 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MatchingStatus1Code | 662 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MatchingStatus27Choice | 668 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}MatchingStatus35Choice | 674 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Max140Text | 683 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Max16Text | 689 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Max210Text | 695 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Max34Text | 701 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Max350Text | 707 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Max35Text | 713 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Max3Number | 719 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Max70Text | 725 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}NameAndAddress13 | 731 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}NoReasonCode | 737 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Order23 | 742 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}OriginalAndCurrentQuantities1 | 790 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}OtherIdentification1 | 796 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PartialFill4 | 803 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PartyIdentification240Choice | 815 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PartyIdentification244Choice | 822 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PartyIdentification267 | 829 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PartyIdentification268 | 836 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PartyIdentificationAndAccount218 | 843 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PartyIdentificationAndAccount220 | 851 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PartyTextInformation1 | 862 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PartyTextInformation5 | 869 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PendingProcessing2Choice | 875 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PercentageRate | 881 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PositionEffect2Code | 887 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PostalAddress8 | 896 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Price14 | 908 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PriceRateOrAmount3Choice | 914 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PriceValueType7Code | 920 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ProcessingStatus98Choice | 937 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ProprietaryReason4 | 960 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ProprietaryStatusAndReason6 | 966 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}PurposeCode9Choice | 972 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Quantity6Choice | 978 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}QuantityBreakdown76 | 984 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}QuantityOrAmount2Choice | 992 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}RegistrationParameters3 | 998 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}RejectionReason52Choice | 1006 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}RejectionReason67 | 1012 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}RejectionReason78Code | 1018 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}RepairReason14 | 1083 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}RepairReason19Choice | 1089 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}RepairReason7Code | 1095 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}ReplacementProcessingStatus10Choice | 1140 |
| [type-0141](types/type-0141.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Reporting2Code | 1155 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Reporting6Choice | 1162 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SecuritiesAccount35 | 1168 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SecuritiesAccountPurposeType1Code | 1175 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SecuritiesCertificate3 | 1185 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SecuritiesTradeConfirmationStatusAdviceV04 | 1192 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SecurityIdentification19 | 1209 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SettlementDate16Choice | 1216 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SettlementDate5Code | 1222 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SettlementDateCode12Choice | 1239 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SettlementParties121 | 1245 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}Side3Code | 1255 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SimpleIdentificationInformation2 | 1275 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SupplementaryData1 | 1280 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}SupplementaryDataEnvelope1 | 1286 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradeDate7Choice | 1291 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradeRegulatoryConditions1Code | 1297 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradeTransactionCondition9Choice | 1303 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradeType3Code | 1309 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradeType4Choice | 1337 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradingCapacity4Code | 1343 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradingCapacity6Code | 1362 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradingDate1Code | 1373 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradingDateCode2Choice | 1378 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradingPartyCapacity3Choice | 1384 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TradingPartyCapacity4Choice | 1390 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TransactiontIdentification4 | 1396 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TypeOfIdentification2Code | 1401 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TypeOfPrice3Code | 1410 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}TypeOfPrice47Choice | 1421 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}UPICIdentifier | 1427 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}UTIIdentifier | 1432 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}UnaffirmedReason1Code | 1437 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}UnaffirmedReason3Choice | 1442 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}UnmatchedReason23 | 1448 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}UnmatchedReason32Choice | 1454 |
| [type-0177](types/type-0177.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}UnmatchedReason4Code | 1460 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}YesNoIndicator | 1528 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.044.001.04}YieldCalculation7 | 1531 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 55 |
| complexType | 109 |
| element | 391 |
| enumeration | 376 |
| extension | 3 |
| fractionDigits | 8 |
| maxLength | 9 |
| minInclusive | 4 |
| minLength | 9 |
| pattern | 13 |
| restriction | 69 |
| schema | 1 |
| sequence | 51 |
| simpleContent | 3 |
| simpleType | 69 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/c3045429df57b1ce52aa594d.md) · [Message](index.md)
