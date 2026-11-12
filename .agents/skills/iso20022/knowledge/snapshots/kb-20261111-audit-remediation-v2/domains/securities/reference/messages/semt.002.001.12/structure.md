---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.002.001.12"
message_family: "semt.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.002.001.12"
source_ids: ["src-000199"]
source_editions: ["2025-2026"]
---

# semt.002.001.12 structure

[src-000199](../../../../../raw-input/settlement_and_reconciliation/semt.002.001.12.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.002.001.12`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.002.001.12 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Account29 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}AccountIdentification26 | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ActiveCurrencyCode | 16 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 21 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ActiveOrHistoricCurrencyAnd13DecimalAmount | 28 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ActiveOrHistoricCurrencyAndAmount_SimpleType | 35 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ActiveOrHistoricCurrencyAndAmount | 42 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ActiveOrHistoricCurrencyCode | 49 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}AdditionalBalanceInformation20 | 54 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}AddressType2Code | 62 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}AggregateBalanceInformation46 | 72 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}AggregateBalancePerSafekeepingPlace43 | 96 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}AmountAndDirection6 | 116 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}AnyBICDec2014Identifier | 122 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Balance16 | 127 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Balance17 | 133 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Balance18 | 139 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Balance21 | 145 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}BalanceAmounts3 | 151 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}BalanceQuantity13Choice | 160 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}BalanceQuantity14Choice | 166 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}BaseOneRate | 172 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}BasicCollateralValuation1Details | 178 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}BlockChainAddressWallet1 | 184 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}BlockChainAddressWallet2 | 192 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}CFIOct2015Identifier | 199 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ClassificationType32Choice | 204 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}CorporateActionOption5Code | 210 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}CountryCode | 216 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}DTI2024Identifier | 221 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}DateAndDateTime2Choice | 226 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}DecimalNumber | 232 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}DistributionPolicy1Code | 238 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Document | 244 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}EventFrequency3Code | 249 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}EventFrequency7Code | 258 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Exact3NumericText | 275 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Exact4AlphaNumericText | 280 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Exact5NumericText | 285 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ExposureType15Code | 290 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ExposureType25Choice | 328 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ExternalFinancialInstrumentIdentificationType1Code | 334 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}FinancialInstrument21 | 340 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}FinancialInstrumentAttributes111 | 355 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}FinancialInstrumentQuantity33Choice | 399 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ForeignExchangeTerms34 | 407 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}FormOfSecurity1Code | 416 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}FormOfSecurity6Choice | 422 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Frequency22Choice | 428 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Frequency23Choice | 434 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}GenericIdentification1 | 440 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}GenericIdentification30 | 447 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}GenericIdentification36 | 454 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}GenericIdentification37 | 461 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}GenericIdentification56 | 467 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}GenericIdentification78 | 475 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}GenericIdentification80 | 481 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ISINOct2015Identifier | 487 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ISODate | 492 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ISODateTime | 495 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}IdentificationSource3Choice | 498 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ImpliedCurrencyAndAmount | 504 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}InterestComputationMethod2Code | 511 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}InterestComputationMethodFormat4Choice | 530 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Intermediary44 | 536 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}InvestmentFundRole2Code | 543 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}LEIIdentifier | 556 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}MICIdentifier | 561 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}MarketIdentification3Choice | 566 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}MarketIdentification5Choice | 572 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}MarketIdentification98 | 578 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}MarketType19Choice | 584 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}MarketType9Code | 590 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Max140Text | 599 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Max16Text | 605 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Max30DecimalNumber | 611 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Max350Text | 617 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Max35Text | 623 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Max5NumericText | 629 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Max70Text | 634 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}NameAndAddress5 | 640 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Number | 646 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Number22Choice | 652 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Number3Choice | 658 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}OptionStyle2Code | 664 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}OptionStyle8Choice | 670 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}OptionType1Code | 676 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}OptionType6Choice | 682 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}OriginalAndCurrentQuantities1 | 688 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}OtherIdentification1 | 694 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Pagination1 | 701 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PartyIdentification120Choice | 707 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PartyIdentification127Choice | 714 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PartyIdentification136 | 720 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PartyIdentification144 | 726 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PartyIdentification15 | 732 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PercentageRate | 738 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Pledgee3 | 744 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PledgeeFormat5Choice | 750 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PledgeeType1Code | 757 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PledgeeTypeAndAnyBICIdentifier2 | 763 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PledgeeTypeAndText1 | 769 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PlusOrMinusIndicator | 775 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PostalAddress1 | 778 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Price7 | 790 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PriceInformation29 | 796 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PriceRateOrAmount3Choice | 805 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PriceRateOrAmountOrUnknown2Choice | 811 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PriceType4Choice | 818 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PriceValueType1Code | 824 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}PurposeCode7Choice | 831 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Quantity51Choice | 837 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}QuantityAndAvailability3 | 843 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}QuantityBreakdown57 | 849 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Role6Choice | 858 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SafeKeepingPlace5 | 865 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SafekeepingPlace1Code | 871 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SafekeepingPlace3Code | 879 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SafekeepingPlaceFormat41Choice | 884 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SafekeepingPlaceTypeAndIdentification1 | 893 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SafekeepingPlaceTypeAndText8 | 899 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SecuritiesAccount25 | 905 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SecuritiesAccount26 | 912 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SecuritiesAccountPurposeType1Code | 920 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SecuritiesBalanceCustodyReportV12 | 930 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SecuritiesBalanceType12Code | 944 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SecuritiesBalanceType7Code | 974 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SecuritiesPaymentStatus1Code | 987 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SecuritiesPaymentStatus5Choice | 994 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SecurityIdentification19 | 1000 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}ShortLong1Code | 1007 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SimpleIdentificationInformation4 | 1013 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}Statement73 | 1018 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}StatementBasis1Code | 1032 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}StatementBasis7Choice | 1039 |
| [type-0137](types/type-0137.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}StatementUpdateType1Code | 1045 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SubAccountIdentification71 | 1051 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SubBalanceInformation20 | 1060 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SubBalanceQuantity8Choice | 1069 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SubBalanceType11Choice | 1076 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SubBalanceType12Choice | 1082 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SupplementaryData1 | 1088 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}SupplementaryDataEnvelope1 | 1094 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}TotalValueInPageAndStatement1 | 1099 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}TypeOfPrice11Code | 1107 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}TypeOfPrice14Code | 1123 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}TypeOfPrice28Choice | 1128 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}TypeOfPrice29Choice | 1134 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}UpdateType15Choice | 1140 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}YesNoIndicator | 1146 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.12}YieldedOrValueType1Choice | 1149 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 37 |
| complexType | 95 |
| element | 329 |
| enumeration | 171 |
| extension | 2 |
| fractionDigits | 8 |
| maxLength | 6 |
| minInclusive | 3 |
| minLength | 6 |
| pattern | 13 |
| restriction | 56 |
| schema | 1 |
| sequence | 56 |
| simpleContent | 2 |
| simpleType | 56 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
