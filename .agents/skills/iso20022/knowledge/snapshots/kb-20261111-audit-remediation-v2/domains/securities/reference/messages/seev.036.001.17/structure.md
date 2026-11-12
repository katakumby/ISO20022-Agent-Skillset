---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.036.001.17"
message_family: "seev.036"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.036.001.17"
source_ids: ["src-000087"]
source_editions: ["2025-2026"]
---

# seev.036.001.17 structure

[src-000087](../../../../../raw-input/corporate_actions/seev.036.001.17.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.036.001.17`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.036.001.17 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Account10Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AccountAndBalance58 | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ActiveCurrencyAnd13DecimalAmount_SimpleType | 21 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ActiveCurrencyAnd13DecimalAmount | 28 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ActiveCurrencyAndAmount_SimpleType | 35 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ActiveCurrencyAndAmount | 42 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ActiveCurrencyCode | 49 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AdditionalBusinessProcess12Code | 54 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AdditionalBusinessProcessFormat23Choice | 70 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AddressType2Code | 76 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AlternatePartyIdentification7 | 86 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AmountAndQuantityRatio4 | 93 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AmountAndRateStatus1 | 99 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AmountPrice2 | 105 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AmountPrice3 | 111 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AmountPricePerAmount2 | 117 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AmountPricePerFinancialInstrumentQuantity10 | 124 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AmountPriceType1Code | 131 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AmountPriceType2Code | 139 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AmountToAmountRatio2 | 144 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}AnyBICDec2014Identifier | 150 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}BICFIDec2014Identifier | 155 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}BalanceFormat11Choice | 160 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}BalanceFormat12Choice | 167 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}BaseOne14Rate | 176 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}BlockChainAddressWallet3 | 182 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CashAccountIdentification5Choice | 189 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CashAccountIdentification9Choice | 195 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CashOption118 | 202 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CashParties43 | 221 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateAction92 | 228 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionAmounts60 | 237 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionAmounts79 | 243 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionBalanceDetails41 | 304 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionDate86 | 325 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionDate88 | 331 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionDate99 | 337 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionEventReference3 | 346 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionEventReference3Choice | 352 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionEventStage4Code | 358 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionEventStageFormat14Choice | 365 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionEventType109Choice | 371 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionEventType37Code | 377 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionGeneralInformation179 | 449 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionMovementConfirmationV17 | 459 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionNarrative31 | 480 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionOption12Code | 488 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionOption253 | 515 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionOption33Choice | 530 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionPrice83 | 536 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionPrice84 | 545 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionRate125 | 551 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CorporateActionRate141 | 565 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CountryCode | 578 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}CreditDebitCode | 583 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DTI2024Identifier | 589 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DateAndDateTime2Choice | 594 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DateCode19Choice | 600 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DateFormat30Choice | 606 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DateFormat43Choice | 612 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DateType8Code | 618 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DecimalNumber | 624 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DeemedRateType1Choice | 630 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DeemedRateType1Code | 636 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DividendRateType1Code | 644 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Document | 649 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DocumentIdentification31 | 654 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DocumentIdentification32 | 660 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DocumentIdentification3Choice | 667 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DocumentIdentification9 | 673 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}DocumentNumber5Choice | 678 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Exact3NumericText | 685 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Exact4AlphaNumericText | 690 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ExternalFinancialInstrumentIdentificationType1Code | 695 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}FinancialInstrumentQuantity33Choice | 701 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ForeignExchangeTerms40 | 709 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}FractionDispositionType11Code | 717 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}FractionDispositionType27Choice | 727 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}GenericIdentification30 | 733 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}GenericIdentification36 | 740 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}GenericIdentification78 | 747 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}GrossDividendRateFormat35Choice | 753 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}GrossDividendRateFormat37Choice | 760 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}GrossDividendRateType6Code | 767 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}GrossDividendRateType7Code | 784 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}IBAN2007Identifier | 803 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ISINOct2015Identifier | 808 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ISO20022MessageIdentificationText | 813 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ISODate | 818 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ISODateTime | 821 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}IdentificationSource3Choice | 824 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}IdentificationType42Choice | 830 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ImpliedCurrencyAndAmount | 836 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}IndicativeOrMarketPrice13Choice | 843 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}InterestRateUsedForPaymentFormat12Choice | 849 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}IntermediateSecuritiesDistributionTypeFormat19Choice | 856 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}IntermediateSecurityDistributionType6Code | 862 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}IssuerOfferorTaxabilityIndicator2Choice | 882 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}IssuerTaxability2Code | 888 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}LotteryType1Code | 893 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}LotteryTypeFormat4Choice | 899 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}MICIdentifier | 905 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}MarketIdentification1Choice | 910 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}MarketIdentification84 | 916 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}MarketType2Code | 922 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}MarketType8Choice | 931 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Max140Text | 937 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Max16Text | 943 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Max30DecimalNumber | 949 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Max34Text | 955 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Max350Text | 961 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Max35Text | 967 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Max5NumericText | 973 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Max70Text | 978 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}NameAndAddress5 | 984 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}NetDividendRateFormat37Choice | 990 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}NetDividendRateFormat40Choice | 997 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}NetDividendRateType6Code | 1004 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}NetDividendRateType7Code | 1019 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}NewSecuritiesIssuanceType6Code | 1036 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}OptionFeatures14Code | 1044 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}OptionFeaturesFormat29Choice | 1056 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}OptionNumber1Choice | 1062 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}OptionNumber1Code | 1068 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}OriginalAndCurrentQuantities1 | 1073 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}OriginalAndCurrentQuantities6 | 1079 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}OtherIdentification1 | 1086 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Pagination1 | 1093 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PartyIdentification120Choice | 1099 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PartyIdentification127Choice | 1106 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PartyIdentification133Choice | 1112 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PartyIdentification257Choice | 1119 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PartyIdentification316 | 1127 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PartyIdentificationAndAccount204 | 1134 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PartyIdentificationAndAccount225 | 1143 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PartyIdentificationAndAccount226 | 1151 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Payment1Code | 1159 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Percentage14Rate | 1165 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PercentagePrice2 | 1171 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PostalAddress1 | 1177 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PriceDetails37 | 1189 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PriceFormat75Choice | 1196 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PriceFormat76Choice | 1203 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PriceFormat77Choice | 1212 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}PriceRateType3Code | 1218 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ProcessingPosition3Code | 1226 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ProcessingPosition7Choice | 1234 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ProprietaryQuantity7 | 1240 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ProprietaryQuantity8 | 1249 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Quantity48Choice | 1257 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Quantity49Choice | 1263 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Quantity50Choice | 1269 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Quantity51Choice | 1275 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}QuantityToQuantityRatio1 | 1281 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}Rate51 | 1287 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateAndAmountFormat55Choice | 1309 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateAndAmountFormat59Choice | 1316 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateAndAmountFormat62Choice | 1322 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateFormat27Choice | 1330 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateFormat31Choice | 1336 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateFormat32Choice | 1343 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateStatus1Code | 1349 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateStatus3Choice | 1355 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType14Code | 1361 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType33Choice | 1367 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType36Choice | 1373 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType42Choice | 1379 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType5Code | 1385 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType76Choice | 1390 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType77Choice | 1396 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType78Choice | 1402 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType79Choice | 1408 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateType7Code | 1414 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateTypeAndAmountAndStatus24 | 1420 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateTypeAndAmountAndStatus26 | 1427 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateTypeAndAmountAndStatus37 | 1434 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateTypeAndAmountAndStatus55 | 1441 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateTypeAndAmountAndStatus56 | 1448 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateTypeAndAmountAndStatus57 | 1455 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateTypeAndAmountAndStatus58 | 1462 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateTypeAndPercentageRate12 | 1469 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RateTypeAndPercentageRate14 | 1475 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RatioFormat19Choice | 1481 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}RatioFormat20Choice | 1489 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SafekeepingPlace1Code | 1495 |
| [type-0187](types/type-0187.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SafekeepingPlace2Code | 1503 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SafekeepingPlace3Code | 1509 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SafekeepingPlaceFormat41Choice | 1514 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SafekeepingPlaceFormat42Choice | 1523 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SafekeepingPlaceTypeAndIdentification1 | 1532 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SafekeepingPlaceTypeAndText6 | 1538 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SafekeepingPlaceTypeAndText8 | 1544 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SecuritiesOption112 | 1550 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SecurityDate25 | 1573 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SecurityIdentification19 | 1583 |
| [type-0197](types/type-0197.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SettlementParties129 | 1590 |
| [type-0198](types/type-0198.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}ShortLong1Code | 1598 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SignedQuantityFormat10 | 1604 |
| [type-0200](types/type-0200.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SignedQuantityFormat11 | 1610 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SolicitationFeeRateFormat12Choice | 1616 |
| [type-0202](types/type-0202.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SupplementaryData1 | 1623 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}SupplementaryDataEnvelope1 | 1629 |
| [type-0204](types/type-0204.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}TaxVoucher6 | 1634 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}TemporaryFinancialInstrumentIndicator3Choice | 1641 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}TotalEligibleBalanceFormat10 | 1647 |
| [type-0207](types/type-0207.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}TransactionIdentification15 | 1654 |
| [type-0208](types/type-0208.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}TypeOfIdentification1Code | 1659 |
| [type-0209](types/type-0209.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}WithholdingTaxRateType1Code | 1670 |
| [type-0210](types/type-0210.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.036.001.17}YesNoIndicator | 1677 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 66 |
| complexType | 144 |
| element | 536 |
| enumeration | 257 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 7 |
| minInclusive | 3 |
| minLength | 7 |
| pattern | 12 |
| restriction | 65 |
| schema | 1 |
| sequence | 76 |
| simpleContent | 2 |
| simpleType | 65 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
