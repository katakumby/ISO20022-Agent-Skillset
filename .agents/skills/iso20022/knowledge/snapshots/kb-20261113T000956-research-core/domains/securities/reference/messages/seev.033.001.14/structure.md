---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.033.001.14"
message_family: "seev.033"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.033.001.14"
source_ids: ["src-000084"]
source_editions: ["2025-2026"]
---

# seev.033.001.14 structure

[src-000084](../../../../../raw-input/corporate_actions/seev.033.001.14.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.033.001.14`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.033.001.14 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}AccountAndBalance61 | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ActiveCurrencyAnd13DecimalAmount_SimpleType | 14 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ActiveCurrencyAnd13DecimalAmount | 21 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ActiveCurrencyAndAmount_SimpleType | 28 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ActiveCurrencyAndAmount | 35 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ActiveCurrencyCode | 42 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ActiveOrHistoricCurrencyCode | 47 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}AddressType2Code | 52 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}AlternatePartyIdentification12 | 62 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}AlternatePartyIdentification7 | 70 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}AmountPrice3 | 77 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}AmountPricePerAmount2 | 83 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}AmountPricePerFinancialInstrumentQuantity10 | 90 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}AmountPriceType1Code | 97 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}AnyBICDec2014Identifier | 105 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}BalanceFormat11Choice | 110 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}BaseOne14Rate | 117 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}BeneficiaryCertificationType10Choice | 123 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}BeneficiaryCertificationType5Code | 129 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CFIOct2015Identifier | 136 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ClassificationType32Choice | 141 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionBalanceDetails42 | 147 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionChangeType2Code | 165 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionChangeTypeFormat6Choice | 179 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionEventReference3 | 185 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionEventReference3Choice | 191 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionEventType112Choice | 197 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionEventType40Code | 203 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionGeneralInformation180 | 272 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionInstructionV14 | 280 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionNarrative30 | 296 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionNarrative32 | 303 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionOption16Code | 311 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionOption237 | 341 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionOption40Choice | 362 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionPrice88 | 368 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CorporateActionRate127 | 376 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}CountryCode | 384 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}DTI2024Identifier | 389 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}DateAndDateTime2Choice | 394 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}DecimalNumber | 400 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Document | 406 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}DocumentIdentification31 | 411 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}DocumentIdentification32 | 417 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}DocumentIdentification3Choice | 424 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}DocumentNumber5Choice | 430 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Exact3NumericText | 437 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Exact4AlphaNumericText | 442 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ExternalFinancialInstrumentIdentificationType1Code | 447 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}FinancialInstrumentAttributes132 | 453 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}FinancialInstrumentQuantity33Choice | 477 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}FractionDispositionType10Code | 485 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}FractionDispositionType28Choice | 493 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}GenericIdentification30 | 499 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}GenericIdentification36 | 506 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}GenericIdentification78 | 513 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ISINOct2015Identifier | 519 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ISO20022MessageIdentificationText | 524 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ISODate | 529 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ISODateTime | 532 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}IdentificationSource3Choice | 535 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}IdentificationType42Choice | 541 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ImpliedCurrencyAndAmount | 547 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}IndicativeOrMarketPrice13Choice | 554 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}InterestComputationMethod2Code | 560 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}InterestComputationMethodFormat4Choice | 579 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}LEIIdentifier | 585 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}MICIdentifier | 590 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}MarketIdentification3Choice | 595 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Max140Text | 601 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Max15Text | 607 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Max16Text | 613 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Max25Text | 619 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Max30DecimalNumber | 625 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Max350Text | 631 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Max35Text | 637 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Max70Text | 643 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}NameAndAddress5 | 649 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}OptionFeatures12Code | 655 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}OptionFeaturesFormat25Choice | 660 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}OptionNumber1Choice | 666 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}OptionNumber1Code | 672 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}OriginalAndCurrentQuantities1 | 677 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}OriginalAndCurrentQuantities6 | 683 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}OtherIdentification1 | 690 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}PartyIdentification127Choice | 697 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}PartyIdentification263Choice | 703 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}PartyIdentification340 | 712 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Percentage14Rate | 724 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}PercentagePrice2 | 730 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}PostalAddress1 | 736 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}PriceFormat77Choice | 748 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}PriceFormat78Choice | 754 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}PriceRateType3Code | 764 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}PriceValueType9Code | 772 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ProcessingPosition3Code | 779 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ProcessingPosition7Choice | 787 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ProprietaryQuantity7 | 793 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ProprietaryQuantity8 | 802 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ProtectInstruction1 | 810 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ProtectTransactionType2Code | 818 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Quantity1Code | 825 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Quantity48Choice | 830 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Quantity49Choice | 836 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Quantity50Choice | 842 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}Quantity52Choice | 848 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}RateAndAmountFormat55Choice | 855 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}RateAndAmountFormat57Choice | 862 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}RateAndAmountFormat59Choice | 869 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}RateType42Choice | 875 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}RateTypeAndPercentageRate12 | 881 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}RateValueType7Code | 887 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SafekeepingPlace1Code | 892 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SafekeepingPlace2Code | 900 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SafekeepingPlaceFormat42Choice | 906 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SafekeepingPlaceTypeAndIdentification1 | 915 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SafekeepingPlaceTypeAndText6 | 921 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SecuritiesOption79 | 927 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SecuritiesQuantityOrAmount6Choice | 934 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SecurityIdentification19 | 940 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}ShortLong1Code | 947 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SignedQuantityFormat10 | 953 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SignedQuantityFormat11 | 959 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SupplementaryData1 | 965 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}SupplementaryDataEnvelope1 | 971 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}TypeOfIdentification1Code | 976 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}WithholdingTaxRateType1Code | 987 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.033.001.14}YesNoIndicator | 994 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 34 |
| complexType | 77 |
| element | 263 |
| enumeration | 169 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 8 |
| minInclusive | 3 |
| minLength | 8 |
| pattern | 12 |
| restriction | 51 |
| schema | 1 |
| sequence | 41 |
| simpleContent | 2 |
| simpleType | 51 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/641ed4e81d3163ba14a38817.md) · [Message](index.md)
