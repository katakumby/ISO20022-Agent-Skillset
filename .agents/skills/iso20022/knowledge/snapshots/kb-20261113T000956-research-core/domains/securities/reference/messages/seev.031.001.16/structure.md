---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.031.001.16"
message_family: "seev.031"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.031.001.16"
source_ids: ["src-000082"]
source_editions: ["2025-2026"]
---

# seev.031.001.16 structure

[src-000082](../../../../../raw-input/corporate_actions/seev.031.001.16.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.031.001.16`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.031.001.16 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AccountAndBalance60 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AccountIdentification10 | 14 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AccountIdentification71Choice | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ActiveCurrencyAnd13DecimalAmount_SimpleType | 25 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ActiveCurrencyAnd13DecimalAmount | 32 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ActiveCurrencyAndAmount_SimpleType | 39 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ActiveCurrencyAndAmount | 46 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ActiveCurrencyCode | 53 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ActiveOrHistoricCurrencyCode | 58 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AdditionalBusinessProcess9Code | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AdditionalBusinessProcessFormat17Choice | 79 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AddressType2Code | 85 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountAndQuantityRatio4 | 95 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountAndRateStatus1 | 101 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountPrice2 | 107 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountPrice3 | 113 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountPrice6 | 119 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountPricePerAmount2 | 125 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountPricePerFinancialInstrumentQuantity10 | 132 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountPriceType1Code | 139 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountPriceType2Code | 147 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountPriceType3Code | 152 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AmountToAmountRatio2 | 158 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}AnyBICDec2014Identifier | 164 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}BalanceFormat11Choice | 169 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}BalanceFormat12Choice | 176 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}BaseOne14Rate | 185 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}BeneficiaryCertificationType13Choice | 191 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}BeneficiaryCertificationType6Code | 197 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}BidRangeType1Choice | 212 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}BidRangeType1Code | 218 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}BlockChainAddressWallet3 | 225 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}BorrowerLendingDeadline5 | 232 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CFIOct2015Identifier | 238 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CapitalGainFormat3Choice | 243 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CashAccountIdentification9Choice | 249 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CashOption116 | 256 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CertificationFormatType1Code | 275 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CertificationTypeFormat3Choice | 281 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ClassificationType32Choice | 287 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ConsentType1Code | 293 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ConsentTypeFormat4Choice | 299 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateAction94 | 305 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionAmounts60 | 345 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionAmounts77 | 351 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionBalanceDetails43 | 404 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionChangeType1Code | 427 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionChangeTypeFormat5Choice | 442 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionDate110 | 448 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionDate83 | 464 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionDate84 | 503 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionEventProcessingType1Code | 511 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionEventProcessingType2Choice | 518 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionEventReference3 | 524 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionEventReference3Choice | 530 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionEventStage3Code | 536 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionEventStageFormat13Choice | 550 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionEventStatus1 | 556 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionEventType107Choice | 562 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionEventType35Code | 568 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionFrequencyType5Code | 640 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionGeneralInformation176 | 650 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionInformationType1Code | 661 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionMandatoryVoluntary1Code | 666 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionMandatoryVoluntary3Choice | 673 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionNarrative58 | 679 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionNarrative59 | 687 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionNarrative60 | 699 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionNotification9 | 715 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionNotificationType1Code | 722 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionNotificationV16 | 729 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionOption15Code | 758 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionOption251 | 784 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionOption37Choice | 814 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionPeriod17 | 820 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionPeriod18 | 839 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionPrice82 | 850 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionPrice85 | 859 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionPrice87 | 867 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionProcessingStatus5Choice | 880 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionQuantity15 | 886 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionRate122 | 899 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionRate128 | 915 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionRate139 | 930 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CorporateActionTaxableIncomePerShareCalculated1Code | 946 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CountryCode | 953 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}CreditDebitCode | 958 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DTI2024Identifier | 964 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateAndDateTime2Choice | 969 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateCode19Choice | 975 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateCode20Choice | 981 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateCode21Choice | 987 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateCode33Choice | 993 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateCodeAndTimeFormat3 | 999 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateFormat30Choice | 1005 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateFormat43Choice | 1011 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateFormat44Choice | 1017 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateFormat45Choice | 1024 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateFormat46Choice | 1030 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateFormat57Choice | 1036 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateFormat59Choice | 1042 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateFormat73Choice | 1048 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateType1Code | 1054 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateType7Code | 1059 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateType8Code | 1064 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DateType9Code | 1070 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DecimalNumber | 1082 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DeemedRateType1Choice | 1088 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DeemedRateType1Code | 1094 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DefaultProcessingOrStandingInstruction2Choice | 1102 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DistributionType3Code | 1108 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DistributionTypeFormat7Choice | 1116 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DividendRateType1Code | 1122 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DividendTypeFormat9Choice | 1127 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Document | 1133 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DocumentIdentification31 | 1138 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DocumentIdentification32 | 1144 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DocumentIdentification3Choice | 1151 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DocumentIdentification9 | 1157 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DocumentNumber5Choice | 1162 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DutchAuctionType1Code | 1169 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}DutchAuctionTypeFormat1Choice | 1175 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}EUCapitalGain2Code | 1181 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ElectionMovementType2Code | 1188 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ElectionTypeFormat3Choice | 1194 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}EventCompletenessStatus1Code | 1200 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}EventConfirmationStatus1Code | 1206 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}EventSequenceType1Code | 1212 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}EventSequenceTypeFormat1Choice | 1218 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Exact3NumericText | 1224 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Exact3UpperCaseAlphaNumericText | 1229 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Exact4AlphaNumericText | 1234 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ExternalFinancialInstrumentIdentificationType1Code | 1239 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FinancialInstrumentAttributes128 | 1245 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FinancialInstrumentAttributes129 | 1272 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FinancialInstrumentAttributes139 | 1299 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FinancialInstrumentQuantity33Choice | 1314 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FinancialInstrumentQuantity34Choice | 1322 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FinancialInstrumentQuantity35Choice | 1331 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ForeignExchangeTerms38 | 1340 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ForeignExchangeTerms39 | 1347 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FractionDispositionType25Choice | 1355 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FractionDispositionType26Choice | 1361 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FractionDispositionType8Code | 1367 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}FractionDispositionType9Code | 1378 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}GenericIdentification30 | 1387 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}GenericIdentification36 | 1394 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}GenericIdentification78 | 1401 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}GrossDividendRateFormat36Choice | 1407 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}GrossDividendRateFormat38Choice | 1415 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}GrossDividendRateType6Code | 1423 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}GrossDividendRateType7Code | 1440 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}IBAN2007Identifier | 1459 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ISINOct2015Identifier | 1464 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ISO20022MessageIdentificationText | 1469 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ISO2ALanguageCode | 1474 |
| [type-0158](types/type-0158.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ISODate | 1479 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ISODateTime | 1482 |
| [type-0160](types/type-0160.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ISOTime | 1485 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}IdentificationFormat3Choice | 1488 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}IdentificationSource3Choice | 1495 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ImpliedCurrencyAndAmount | 1501 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}IndicativeOrMarketPrice12Choice | 1508 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}InformationTypeFormat4Choice | 1514 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}InterestComputationMethod2Code | 1520 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}InterestComputationMethodFormat4Choice | 1539 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}InterestRateUsedForPaymentFormat11Choice | 1545 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}IntermediateSecuritiesDistributionTypeFormat19Choice | 1553 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}IntermediateSecurityDistributionType6Code | 1559 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}IssuerOfferorTaxabilityIndicator2Choice | 1579 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}IssuerTaxability2Code | 1585 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}LEIIdentifier | 1590 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}LotteryType1Code | 1595 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}LotteryTypeFormat4Choice | 1601 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}MICIdentifier | 1607 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}MarketIdentification3Choice | 1612 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max140Text | 1618 |
| [type-0179](types/type-0179.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max16Text | 1624 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max2048Text | 1630 |
| [type-0181](types/type-0181.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max30DecimalNumber | 1636 |
| [type-0182](types/type-0182.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max30Text | 1642 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max34Text | 1647 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max350Text | 1653 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max35Text | 1659 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max3Number | 1665 |
| [type-0187](types/type-0187.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max5NumericText | 1671 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max70Text | 1676 |
| [type-0189](types/type-0189.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Max8000Text | 1682 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}NameAndAddress5 | 1688 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}NetDividendRateFormat38Choice | 1694 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}NetDividendRateFormat39Choice | 1702 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}NetDividendRateType6Code | 1710 |
| [type-0194](types/type-0194.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}NetDividendRateType7Code | 1725 |
| [type-0195](types/type-0195.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}NewSecuritiesIssuanceType5Code | 1742 |
| [type-0196](types/type-0196.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}NonEligibleProceedsIndicator2Code | 1753 |
| [type-0197](types/type-0197.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}NonEligibleProceedsIndicator5Choice | 1761 |
| [type-0198](types/type-0198.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OfferType7Code | 1767 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OfferTypeFormat18Choice | 1778 |
| [type-0200](types/type-0200.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OptionAvailabilityStatus1Code | 1784 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OptionAvailabilityStatus3Choice | 1790 |
| [type-0202](types/type-0202.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OptionFeatures15Code | 1796 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OptionFeaturesFormat32Choice | 1816 |
| [type-0204](types/type-0204.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OptionStyle2Code | 1822 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OptionStyle8Choice | 1828 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OriginalAndCurrentQuantities1 | 1834 |
| [type-0207](types/type-0207.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OriginalAndCurrentQuantities6 | 1840 |
| [type-0208](types/type-0208.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}OtherIdentification1 | 1847 |
| [type-0209](types/type-0209.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Pagination1 | 1854 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PartyIdentification120Choice | 1860 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PartyIdentification127Choice | 1867 |
| [type-0212](types/type-0212.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PartyIdentification129Choice | 1873 |
| [type-0213](types/type-0213.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Payment2Code | 1881 |
| [type-0214](types/type-0214.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Percentage14Rate | 1886 |
| [type-0215](types/type-0215.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PercentagePrice2 | 1892 |
| [type-0216](types/type-0216.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Period11 | 1898 |
| [type-0217](types/type-0217.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Period12Choice | 1904 |
| [type-0218](types/type-0218.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Period18 | 1910 |
| [type-0219](types/type-0219.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Period6Choice | 1916 |
| [type-0220](types/type-0220.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PostalAddress1 | 1922 |
| [type-0221](types/type-0221.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceCalculationMethod1Code | 1934 |
| [type-0222](types/type-0222.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceCalculationMethod2Choice | 1943 |
| [type-0223](types/type-0223.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceDetails38 | 1949 |
| [type-0224](types/type-0224.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceFormat46Choice | 1956 |
| [type-0225](types/type-0225.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceFormat61Choice | 1962 |
| [type-0226](types/type-0226.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceFormat72Choice | 1968 |
| [type-0227](types/type-0227.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceFormat73Choice | 1978 |
| [type-0228](types/type-0228.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceFormat74Choice | 1986 |
| [type-0229](types/type-0229.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceRateType3Code | 1993 |
| [type-0230](types/type-0230.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceValueType10Code | 2001 |
| [type-0231](types/type-0231.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}PriceValueType8Code | 2006 |
| [type-0232](types/type-0232.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ProcessingPosition3Code | 2014 |
| [type-0233](types/type-0233.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ProcessingPosition7Choice | 2022 |
| [type-0234](types/type-0234.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ProprietaryQuantity7 | 2028 |
| [type-0235](types/type-0235.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ProprietaryQuantity8 | 2037 |
| [type-0236](types/type-0236.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ProrationBelowMinimumQuantity2Code | 2045 |
| [type-0237](types/type-0237.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ProrationBelowMinimumQuantity3Choice | 2055 |
| [type-0238](types/type-0238.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Quantity48Choice | 2061 |
| [type-0239](types/type-0239.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Quantity49Choice | 2067 |
| [type-0240](types/type-0240.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Quantity4Code | 2073 |
| [type-0241](types/type-0241.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Quantity50Choice | 2079 |
| [type-0242](types/type-0242.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Quantity51Choice | 2085 |
| [type-0243](types/type-0243.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Quantity5Code | 2091 |
| [type-0244](types/type-0244.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}QuantityToQuantityRatio1 | 2096 |
| [type-0245](types/type-0245.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}Rate48 | 2102 |
| [type-0246](types/type-0246.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateAndAmountFormat42Choice | 2124 |
| [type-0247](types/type-0247.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateAndAmountFormat56Choice | 2130 |
| [type-0248](types/type-0248.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateAndAmountFormat57Choice | 2138 |
| [type-0249](types/type-0249.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateAndAmountFormat58Choice | 2145 |
| [type-0250](types/type-0250.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateAndAmountFormat59Choice | 2153 |
| [type-0251](types/type-0251.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateAndAmountFormat60Choice | 2159 |
| [type-0252](types/type-0252.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateAndAmountFormat61Choice | 2167 |
| [type-0253](types/type-0253.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateFormat12Choice | 2176 |
| [type-0254](types/type-0254.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateFormat24Choice | 2182 |
| [type-0255](types/type-0255.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateFormat25Choice | 2188 |
| [type-0256](types/type-0256.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateFormat26Choice | 2194 |
| [type-0257](types/type-0257.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateFormat31Choice | 2201 |
| [type-0258](types/type-0258.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateFormat32Choice | 2208 |
| [type-0259](types/type-0259.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateStatus1Code | 2214 |
| [type-0260](types/type-0260.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateStatus3Choice | 2220 |
| [type-0261](types/type-0261.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType10Code | 2226 |
| [type-0262](types/type-0262.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType13Code | 2232 |
| [type-0263](types/type-0263.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType14Code | 2238 |
| [type-0264](types/type-0264.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType33Choice | 2244 |
| [type-0265](types/type-0265.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType36Choice | 2250 |
| [type-0266](types/type-0266.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType42Choice | 2256 |
| [type-0267](types/type-0267.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType5Code | 2262 |
| [type-0268](types/type-0268.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType76Choice | 2267 |
| [type-0269](types/type-0269.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType77Choice | 2273 |
| [type-0270](types/type-0270.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType78Choice | 2279 |
| [type-0271](types/type-0271.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType79Choice | 2285 |
| [type-0272](types/type-0272.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateType7Code | 2291 |
| [type-0273](types/type-0273.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndAmountAndStatus24 | 2297 |
| [type-0274](types/type-0274.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndAmountAndStatus26 | 2304 |
| [type-0275](types/type-0275.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndAmountAndStatus37 | 2311 |
| [type-0276](types/type-0276.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndAmountAndStatus55 | 2318 |
| [type-0277](types/type-0277.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndAmountAndStatus56 | 2325 |
| [type-0278](types/type-0278.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndAmountAndStatus57 | 2332 |
| [type-0279](types/type-0279.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndAmountAndStatus58 | 2339 |
| [type-0280](types/type-0280.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndPercentageRate12 | 2346 |
| [type-0281](types/type-0281.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndPercentageRate13 | 2352 |
| [type-0282](types/type-0282.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateTypeAndPercentageRate14 | 2358 |
| [type-0283](types/type-0283.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RateValueType7Code | 2364 |
| [type-0284](types/type-0284.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RatioFormat17Choice | 2369 |
| [type-0285](types/type-0285.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RatioFormat18Choice | 2376 |
| [type-0286](types/type-0286.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RenounceableEntitlementStatusTypeFormat3Choice | 2385 |
| [type-0287](types/type-0287.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}RenounceableStatus1Code | 2391 |
| [type-0288](types/type-0288.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SafekeepingAccountIdentification1Code | 2397 |
| [type-0289](types/type-0289.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SafekeepingPlace1Code | 2402 |
| [type-0290](types/type-0290.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SafekeepingPlace2Code | 2410 |
| [type-0291](types/type-0291.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SafekeepingPlace3Code | 2416 |
| [type-0292](types/type-0292.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SafekeepingPlaceFormat41Choice | 2421 |
| [type-0293](types/type-0293.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SafekeepingPlaceFormat42Choice | 2430 |
| [type-0294](types/type-0294.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SafekeepingPlaceTypeAndIdentification1 | 2439 |
| [type-0295](types/type-0295.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SafekeepingPlaceTypeAndText6 | 2445 |
| [type-0296](types/type-0296.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SafekeepingPlaceTypeAndText8 | 2451 |
| [type-0297](types/type-0297.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SecuritiesOption121 | 2457 |
| [type-0298](types/type-0298.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SecuritiesOption81 | 2480 |
| [type-0299](types/type-0299.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SecurityDate20 | 2491 |
| [type-0300](types/type-0300.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SecurityIdentification19 | 2501 |
| [type-0301](types/type-0301.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}ShortLong1Code | 2508 |
| [type-0302](types/type-0302.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SignedQuantityFormat10 | 2514 |
| [type-0303](types/type-0303.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SignedQuantityFormat11 | 2520 |
| [type-0304](types/type-0304.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SolicitationFeeRateFormat11Choice | 2526 |
| [type-0305](types/type-0305.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SupplementaryData1 | 2534 |
| [type-0306](types/type-0306.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}SupplementaryDataEnvelope1 | 2540 |
| [type-0307](types/type-0307.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}TaxableIncomePerShareCalculatedFormat3Choice | 2545 |
| [type-0308](types/type-0308.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}TemporaryFinancialInstrumentIndicator3Choice | 2551 |
| [type-0309](types/type-0309.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}TotalEligibleBalanceFormat10 | 2557 |
| [type-0310](types/type-0310.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}UpdatedAdditionalInformation19 | 2564 |
| [type-0311](types/type-0311.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}UpdatedAdditionalInformation20 | 2570 |
| [type-0312](types/type-0312.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}UpdatedAdditionalInformation21 | 2576 |
| [type-0313](types/type-0313.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}UpdatedURLlnformation6 | 2582 |
| [type-0314](types/type-0314.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}WithholdingTaxRateType1Code | 2588 |
| [type-0315](types/type-0315.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.031.001.16}YesNoIndicator | 2595 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 111 |
| complexType | 204 |
| element | 881 |
| enumeration | 400 |
| extension | 2 |
| fractionDigits | 8 |
| maxLength | 10 |
| minInclusive | 3 |
| minLength | 9 |
| pattern | 16 |
| restriction | 110 |
| schema | 1 |
| sequence | 91 |
| simpleContent | 2 |
| simpleType | 110 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/e4c3bec1fffcb3ec1bb881d6.md) · [Message](index.md)
