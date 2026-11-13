---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.035.001.17"
message_family: "seev.035"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.035.001.17"
source_ids: ["src-000086"]
source_editions: ["2025-2026"]
---

# seev.035.001.17 structure

[src-000086](../../../../../raw-input/corporate_actions/seev.035.001.17.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.035.001.17`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.035.001.17 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AccountAndBalance59 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AccountIdentification10 | 14 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AccountIdentification70Choice | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ActiveCurrencyAnd13DecimalAmount_SimpleType | 25 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ActiveCurrencyAnd13DecimalAmount | 32 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ActiveCurrencyAndAmount_SimpleType | 39 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ActiveCurrencyAndAmount | 46 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ActiveCurrencyCode | 53 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ActiveOrHistoricCurrencyCode | 58 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AdditionalBusinessProcess10Code | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AdditionalBusinessProcessFormat18Choice | 75 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AddressType2Code | 81 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountAndQuantityRatio4 | 91 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountAndRateStatus1 | 97 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountPrice2 | 103 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountPrice3 | 109 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountPrice6 | 115 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountPricePerAmount2 | 121 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountPricePerFinancialInstrumentQuantity10 | 128 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountPriceType1Code | 135 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountPriceType2Code | 143 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountPriceType3Code | 148 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AmountToAmountRatio2 | 154 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}AnyBICDec2014Identifier | 160 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}BalanceFormat11Choice | 165 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}BalanceFormat12Choice | 172 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}BaseOne14Rate | 181 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}BeneficiaryCertificationType13Choice | 187 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}BeneficiaryCertificationType6Code | 193 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}BlockChainAddressWallet3 | 208 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}BorrowerLendingDeadline5 | 215 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CFIOct2015Identifier | 221 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CashAccountIdentification9Choice | 226 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CashOption117 | 233 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ClassificationType32Choice | 251 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateAction91 | 257 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionAmounts60 | 267 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionAmounts78 | 273 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionBalanceDetails43 | 324 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionDate106 | 347 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionDate84 | 362 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionDate85 | 370 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionEventProcessingType1Code | 377 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionEventProcessingType2Choice | 384 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionEventReference3 | 390 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionEventReference3Choice | 396 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionEventStage4Code | 402 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionEventStageFormat14Choice | 409 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionEventType108Choice | 415 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionEventType36Code | 421 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionGeneralInformation178 | 492 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionMandatoryVoluntary1Code | 503 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionMandatoryVoluntary3Choice | 510 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionMovementPreliminaryAdviceFunction1Code | 516 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionMovementPreliminaryAdviceV17 | 522 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionNarrative56 | 553 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionNarrative57 | 568 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionOption15Code | 580 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionOption252 | 606 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionOption37Choice | 634 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionPreliminaryAdviceType1Code | 640 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionPreliminaryAdviceType4 | 646 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionPrice82 | 653 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionPrice86 | 662 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionQuantity12 | 671 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionRate123 | 677 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionRate140 | 692 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionReversalReason10Choice | 706 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionReversalReason3Code | 712 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CorporateActionReversalReason8 | 725 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CountryCode | 731 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}CreditDebitCode | 736 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DTI2024Identifier | 742 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateAndDateTime2Choice | 747 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateCode19Choice | 753 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateCode20Choice | 759 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateCode21Choice | 765 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateCodeAndTimeFormat3 | 771 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateFormat30Choice | 777 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateFormat43Choice | 783 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateFormat44Choice | 789 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateFormat57Choice | 796 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateFormat73Choice | 802 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateType1Code | 808 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateType7Code | 813 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DateType8Code | 818 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DecimalNumber | 824 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DeemedRateType1Choice | 830 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DeemedRateType1Code | 836 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DefaultProcessingOrStandingInstruction2Choice | 844 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DividendRateType1Code | 850 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Document | 855 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DocumentIdentification31 | 860 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DocumentIdentification32 | 866 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DocumentIdentification3Choice | 873 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DocumentIdentification9 | 879 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}DocumentNumber5Choice | 884 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Exact3NumericText | 891 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Exact4AlphaNumericText | 896 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ExternalFinancialInstrumentIdentificationType1Code | 901 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}FinancialInstrumentAttributes128 | 907 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}FinancialInstrumentAttributes129 | 934 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}FinancialInstrumentQuantity33Choice | 961 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}FinancialInstrumentQuantity34Choice | 969 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}FinancialInstrumentQuantity35Choice | 978 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ForeignExchangeTerms39 | 987 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}FractionDispositionType26Choice | 995 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}FractionDispositionType8Code | 1001 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}GenericIdentification30 | 1012 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}GenericIdentification36 | 1019 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}GenericIdentification78 | 1026 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}GrossDividendRateFormat36Choice | 1032 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}GrossDividendRateFormat38Choice | 1040 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}GrossDividendRateType6Code | 1048 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}GrossDividendRateType7Code | 1065 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}IBAN2007Identifier | 1084 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ISINOct2015Identifier | 1089 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ISO20022MessageIdentificationText | 1094 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ISODate | 1099 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ISODateTime | 1102 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ISOTime | 1105 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}IdentificationSource3Choice | 1108 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ImpliedCurrencyAndAmount | 1114 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}IndicativeOrMarketPrice12Choice | 1121 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}InterestComputationMethod2Code | 1127 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}InterestComputationMethodFormat4Choice | 1146 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}InterestRateUsedForPaymentFormat11Choice | 1152 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}IntermediateSecuritiesDistributionTypeFormat19Choice | 1160 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}IntermediateSecurityDistributionType6Code | 1166 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}IssuerOfferorTaxabilityIndicator2Choice | 1186 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}IssuerTaxability2Code | 1192 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}LEIIdentifier | 1197 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}LotteryType1Code | 1202 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}LotteryTypeFormat4Choice | 1208 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}MICIdentifier | 1214 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}MarketIdentification3Choice | 1219 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Max140Text | 1225 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Max16Text | 1231 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Max256Text | 1237 |
| [type-0141](types/type-0141.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Max30DecimalNumber | 1243 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Max34Text | 1249 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Max350Text | 1255 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Max35Text | 1261 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Max5NumericText | 1267 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Max70Text | 1272 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NameAndAddress5 | 1278 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NetDividendRateFormat38Choice | 1284 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NetDividendRateFormat39Choice | 1292 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NetDividendRateType6Code | 1300 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NetDividendRateType7Code | 1315 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NewSecuritiesIssuanceType5Code | 1332 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NonEligibleProceedsIndicator1Code | 1343 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NonEligibleProceedsIndicator2Code | 1350 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NonEligibleProceedsIndicator3Choice | 1358 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}NonEligibleProceedsIndicator5Choice | 1364 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OfferType6Code | 1370 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OfferTypeFormat17Choice | 1380 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OptionAvailabilityStatus1Code | 1386 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OptionAvailabilityStatus3Choice | 1392 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OptionFeatures15Code | 1398 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OptionFeaturesFormat32Choice | 1418 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OptionStyle2Code | 1424 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OptionStyle8Choice | 1430 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OriginalAndCurrentQuantities1 | 1436 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OriginalAndCurrentQuantities6 | 1442 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}OtherIdentification1 | 1449 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Pagination1 | 1456 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PartyIdentification120Choice | 1462 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PartyIdentification127Choice | 1469 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PartyIdentification129Choice | 1475 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Payment1Code | 1483 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Percentage14Rate | 1489 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PercentagePrice2 | 1495 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Period12Choice | 1501 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Period18 | 1507 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PostalAddress1 | 1513 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PriceDetails38 | 1525 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PriceFormat46Choice | 1532 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PriceFormat61Choice | 1538 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PriceFormat72Choice | 1544 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PriceFormat73Choice | 1554 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PriceFormat74Choice | 1562 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PriceRateType3Code | 1569 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PriceValueType10Code | 1577 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}PriceValueType8Code | 1582 |
| [type-0187](types/type-0187.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ProcessingPosition3Code | 1590 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ProcessingPosition7Choice | 1598 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ProprietaryQuantity7 | 1604 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ProprietaryQuantity8 | 1613 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Quantity48Choice | 1621 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Quantity49Choice | 1627 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Quantity4Code | 1633 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Quantity50Choice | 1639 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Quantity51Choice | 1645 |
| [type-0196](types/type-0196.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Quantity5Code | 1651 |
| [type-0197](types/type-0197.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}QuantityToQuantityRatio1 | 1656 |
| [type-0198](types/type-0198.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}Rate50 | 1662 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateAndAmountFormat42Choice | 1684 |
| [type-0200](types/type-0200.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateAndAmountFormat56Choice | 1690 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateAndAmountFormat57Choice | 1698 |
| [type-0202](types/type-0202.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateAndAmountFormat61Choice | 1705 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateFormat12Choice | 1714 |
| [type-0204](types/type-0204.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateFormat24Choice | 1720 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateFormat26Choice | 1726 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateFormat31Choice | 1733 |
| [type-0207](types/type-0207.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateFormat32Choice | 1740 |
| [type-0208](types/type-0208.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateStatus1Code | 1746 |
| [type-0209](types/type-0209.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateStatus3Choice | 1752 |
| [type-0210](types/type-0210.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType13Code | 1758 |
| [type-0211](types/type-0211.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType14Code | 1764 |
| [type-0212](types/type-0212.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType33Choice | 1770 |
| [type-0213](types/type-0213.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType36Choice | 1776 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType42Choice | 1782 |
| [type-0215](types/type-0215.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType5Code | 1788 |
| [type-0216](types/type-0216.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType76Choice | 1793 |
| [type-0217](types/type-0217.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType77Choice | 1799 |
| [type-0218](types/type-0218.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType78Choice | 1805 |
| [type-0219](types/type-0219.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType79Choice | 1811 |
| [type-0220](types/type-0220.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateType7Code | 1817 |
| [type-0221](types/type-0221.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateTypeAndAmountAndStatus24 | 1823 |
| [type-0222](types/type-0222.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateTypeAndAmountAndStatus26 | 1830 |
| [type-0223](types/type-0223.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateTypeAndAmountAndStatus37 | 1837 |
| [type-0224](types/type-0224.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateTypeAndAmountAndStatus55 | 1844 |
| [type-0225](types/type-0225.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateTypeAndAmountAndStatus56 | 1851 |
| [type-0226](types/type-0226.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateTypeAndAmountAndStatus57 | 1858 |
| [type-0227](types/type-0227.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateTypeAndAmountAndStatus58 | 1865 |
| [type-0228](types/type-0228.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateTypeAndPercentageRate12 | 1872 |
| [type-0229](types/type-0229.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateTypeAndPercentageRate14 | 1878 |
| [type-0230](types/type-0230.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RateValueType7Code | 1884 |
| [type-0231](types/type-0231.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RatioFormat17Choice | 1889 |
| [type-0232](types/type-0232.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}RatioFormat18Choice | 1896 |
| [type-0233](types/type-0233.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SafekeepingAccountIdentification1Code | 1905 |
| [type-0234](types/type-0234.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SafekeepingPlace1Code | 1910 |
| [type-0235](types/type-0235.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SafekeepingPlace2Code | 1918 |
| [type-0236](types/type-0236.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SafekeepingPlace3Code | 1924 |
| [type-0237](types/type-0237.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SafekeepingPlaceFormat41Choice | 1929 |
| [type-0238](types/type-0238.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SafekeepingPlaceFormat42Choice | 1938 |
| [type-0239](types/type-0239.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SafekeepingPlaceTypeAndIdentification1 | 1947 |
| [type-0240](types/type-0240.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SafekeepingPlaceTypeAndText6 | 1953 |
| [type-0241](types/type-0241.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SafekeepingPlaceTypeAndText8 | 1959 |
| [type-0242](types/type-0242.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SecuritiesOption122 | 1965 |
| [type-0243](types/type-0243.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SecuritiesOption81 | 1988 |
| [type-0244](types/type-0244.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SecurityDate20 | 1999 |
| [type-0245](types/type-0245.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SecurityIdentification19 | 2009 |
| [type-0246](types/type-0246.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}ShortLong1Code | 2016 |
| [type-0247](types/type-0247.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SignedQuantityFormat10 | 2022 |
| [type-0248](types/type-0248.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SignedQuantityFormat11 | 2028 |
| [type-0249](types/type-0249.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SolicitationFeeRateFormat11Choice | 2034 |
| [type-0250](types/type-0250.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SupplementaryData1 | 2042 |
| [type-0251](types/type-0251.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}SupplementaryDataEnvelope1 | 2048 |
| [type-0252](types/type-0252.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}TemporaryFinancialInstrumentIndicator3Choice | 2053 |
| [type-0253](types/type-0253.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}TotalEligibleBalanceFormat10 | 2059 |
| [type-0254](types/type-0254.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}UpdatedAdditionalInformation17 | 2066 |
| [type-0255](types/type-0255.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}UpdatedAdditionalInformation18 | 2071 |
| [type-0256](types/type-0256.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}WithholdingTaxRateType1Code | 2076 |
| [type-0257](types/type-0257.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.035.001.17}YesNoIndicator | 2083 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 86 |
| complexType | 168 |
| element | 680 |
| enumeration | 328 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 8 |
| minInclusive | 3 |
| minLength | 8 |
| pattern | 14 |
| restriction | 88 |
| schema | 1 |
| sequence | 80 |
| simpleContent | 2 |
| simpleType | 88 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/449b9697e14b28222136bf4f.md) · [Message](index.md)
