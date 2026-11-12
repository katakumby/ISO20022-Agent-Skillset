---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.040.001.01"
message_family: "semt.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.040.001.01"
source_ids: ["src-000318"]
source_editions: ["march-2026"]
---

# semt.040.001.01 structure

[src-000318](../../../../../raw-input/target2securities_t2s/semt.040.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.040.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.040.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ActiveCurrencyCode | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ActiveOrHistoricCurrencyAnd13DecimalAmount | 17 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ActiveOrHistoricCurrencyAndAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ActiveOrHistoricCurrencyAndAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ActiveOrHistoricCurrencyCode | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}AdditionalBalanceBreakdown1 | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}AdditionalBalanceInformation18 | 51 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}AddressType2Code | 59 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}AggregateBalanceInformation47 | 69 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}AggregateBalancePerSafekeepingPlace44 | 94 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}AlternatePartyIdentification7 | 114 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}AmountAndDirection6 | 121 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}AnyBICDec2014Identifier | 127 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Balance30 | 132 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Balance6 | 140 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Balance7 | 146 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Balance8 | 152 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Balance9 | 158 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}BalanceAmounts3 | 164 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}BalanceQuantity8Choice | 173 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}BalanceQuantity9Choice | 179 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}BaseOneRate | 185 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}BasicCollateralValuation1Details | 191 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}CFIOct2015Identifier | 197 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ClassificationType32Choice | 202 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}CorporateActionOption5Code | 208 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}CountryCode | 214 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}DateAndDateTime1Choice | 219 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}DateAndDateTime2Choice | 225 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}DecimalNumber | 231 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}DistributionPolicy1Code | 237 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Document | 243 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}EventFrequency3Code | 248 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Exact3NumericText | 257 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Exact4AlphaNumericText | 262 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ExposureType15Code | 267 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ExposureType25Choice | 305 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ExternalFinancialInstrumentIdentificationType1Code | 311 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}FinancialInstrument21 | 317 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}FinancialInstrumentAttributes138 | 332 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}FinancialInstrumentQuantity1Choice | 376 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ForeignExchangeTerms34 | 383 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}FormOfSecurity1Code | 392 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}FormOfSecurity6Choice | 398 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Frequency23Choice | 404 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}GenericIdentification1 | 410 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}GenericIdentification30 | 417 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}GenericIdentification36 | 424 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}GenericIdentification37 | 431 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}GenericIdentification56 | 437 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}GenericIdentification78 | 445 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}GenericIdentification80 | 451 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ISINOct2015Identifier | 457 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ISODate | 462 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ISODateTime | 465 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}IdentificationSource3Choice | 468 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}IdentificationType42Choice | 474 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ImpliedCurrencyAndAmount | 480 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}InterestComputationMethod2Code | 487 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}InterestComputationMethodFormat4Choice | 506 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}LEIIdentifier | 512 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}MICIdentifier | 517 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}MarketIdentification1Choice | 522 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}MarketIdentification3Choice | 528 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}MarketIdentification89 | 534 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}MarketType15Choice | 540 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}MarketType4Code | 546 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Max140Text | 554 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Max16Text | 560 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Max350Text | 566 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Max35Text | 572 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Max5NumericText | 578 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Max70Text | 583 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}NameAndAddress5 | 589 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Number | 595 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Number22Choice | 601 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}OptionStyle2Code | 607 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}OptionStyle8Choice | 613 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}OptionType1Code | 619 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}OptionType6Choice | 625 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}OriginalAndCurrentQuantities1 | 631 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}OtherIdentification1 | 637 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}OtherParties46 | 644 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Pagination1 | 649 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PartyIdentification120Choice | 655 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PartyIdentification122Choice | 662 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PartyIdentification136 | 669 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PartyIdentification15 | 675 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PartyIdentificationAndAccount197 | 681 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PartyTextInformation1 | 693 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PercentageRate | 700 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Pledgee3 | 706 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PledgeeFormat5Choice | 712 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PledgeeType1Code | 719 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PledgeeTypeAndAnyBICIdentifier2 | 725 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PledgeeTypeAndText1 | 731 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PlusOrMinusIndicator | 737 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PostalAddress1 | 740 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Price7 | 752 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PriceInformation20 | 758 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PriceRateOrAmount3Choice | 767 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PriceRateOrAmountOrUnknown2Choice | 773 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PriceType4Choice | 780 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}PriceValueType1Code | 786 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Quantity6Choice | 793 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}QuantityAndAvailability1 | 799 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}QuantityBreakdown54 | 805 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SafeKeepingPlace3 | 814 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SafekeepingPlace1Code | 820 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SafekeepingPlace3Code | 828 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SafekeepingPlaceFormat29Choice | 833 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SafekeepingPlaceTypeAndIdentification1 | 841 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SafekeepingPlaceTypeAndText8 | 847 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SecuritiesAccount19 | 853 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SecuritiesAccountPositionResponseV01 | 860 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SecuritiesBalanceType12Code | 871 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SecuritiesBalanceType7Code | 901 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SecuritiesPaymentStatus1Code | 914 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SecuritiesPaymentStatus5Choice | 921 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SecurityIdentification19 | 927 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}ShortLong1Code | 934 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}Statement58 | 940 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SubAccountIdentification75 | 949 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SubBalanceInformation18 | 957 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SubBalanceQuantity6Choice | 966 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SubBalanceType11Choice | 973 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SubBalanceType12Choice | 979 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SupplementaryData1 | 985 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}SupplementaryDataEnvelope1 | 991 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}TotalValueInPageAndStatement1 | 996 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}TrueFalseIndicator | 1004 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}TypeOfIdentification1Code | 1007 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}TypeOfPrice11Code | 1018 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}TypeOfPrice14Code | 1034 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}TypeOfPrice28Choice | 1039 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}TypeOfPrice29Choice | 1045 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}YesNoIndicator | 1051 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.040.001.01}YieldedOrValueType1Choice | 1054 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 33 |
| complexType | 89 |
| element | 314 |
| enumeration | 144 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 6 |
| minInclusive | 3 |
| minLength | 6 |
| pattern | 11 |
| restriction | 50 |
| schema | 1 |
| sequence | 54 |
| simpleContent | 2 |
| simpleType | 50 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
