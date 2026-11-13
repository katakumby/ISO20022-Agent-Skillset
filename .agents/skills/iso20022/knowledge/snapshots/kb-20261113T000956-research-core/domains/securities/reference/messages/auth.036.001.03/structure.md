---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "auth.036.001.03"
message_family: "auth.036"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.036.001.03"
source_ids: ["src-000329"]
source_editions: ["2025"]
---

# auth.036.001.03 structure

[src-000329](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.036.001.03.xsd); `urn:iso:std:iso:20022:tech:xsd:auth.036.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:auth.036.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}ActiveCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}ActiveCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}ActiveOrHistoricCurrencyAndAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}ActiveOrHistoricCurrencyAndAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}ActiveOrHistoricCurrencyCode | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AgriculturalCommodityDairy1 | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AgriculturalCommodityForestry1 | 49 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AgriculturalCommodityGrain1 | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AgriculturalCommodityLiveStock1 | 62 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AgriculturalCommodityOilSeed1 | 68 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AgriculturalCommodityOliveOil1 | 75 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AgriculturalCommodityPotato1 | 82 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AgriculturalCommoditySeafood1 | 88 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AgriculturalCommoditySoft1 | 94 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AmountAndDirection61 | 101 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClass2 | 107 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodity3Choice | 114 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityAgricultural1Choice | 132 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityEnergy1Choice | 145 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityEnvironmental1Choice | 157 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityFertilizer1Choice | 164 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityFreight1Choice | 174 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityIndustrialProduct1Choice | 181 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityInflation1 | 187 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityMetal1Choice | 192 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityMultiCommodityExotic1 | 198 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityOfficialEconomicStatistics1 | 203 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityOther1 | 208 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityOtherC102Choice | 213 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityPaper1Choice | 219 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassCommodityPolypropylene1Choice | 227 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType10Code | 232 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType11Code | 249 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType12Code | 258 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType14Code | 263 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType15Code | 268 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType1Code | 273 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType2Code | 283 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType4Code | 292 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType5Code | 297 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType6Code | 306 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType7Code | 315 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassDetailedSubProductType8Code | 343 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType11Code | 352 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType12Code | 357 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType13Code | 362 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType14Code | 367 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType15Code | 372 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType1Code | 377 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType2Code | 382 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType3Code | 387 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType4Code | 392 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType5Code | 397 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType6Code | 402 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType7Code | 407 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType8Code | 412 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassProductType9Code | 417 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType10Code | 422 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType15Code | 427 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType16Code | 432 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType18Code | 437 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType1Code | 442 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType20Code | 447 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType21Code | 452 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType22Code | 457 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType23Code | 462 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType24Code | 467 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType25Code | 472 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType26Code | 477 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType27Code | 482 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType28Code | 487 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType29Code | 492 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType2Code | 497 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType30Code | 502 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType31Code | 507 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType32Code | 512 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType33Code | 517 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType34Code | 522 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType35Code | 527 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType36Code | 532 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType37Code | 537 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType38Code | 542 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType39Code | 547 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType3Code | 552 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType40Code | 557 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType41Code | 562 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType42Code | 567 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType43Code | 572 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType44Code | 577 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType45Code | 582 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType46Code | 587 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType47Code | 592 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType48Code | 597 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType5Code | 602 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType6Code | 607 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType7Code | 612 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassSubProductType8Code | 617 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetClassTransactionType1Code | 622 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetFXSubProductType1Code | 636 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}AssetPriceType1Code | 643 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}BenchmarkCurveName2Code | 654 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}BenchmarkCurveName5Choice | 684 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}BenchmarkCurveName6Choice | 690 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}CFIOct2015Identifier | 697 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}CountryCode | 702 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}DebtInstrument2 | 707 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}DebtInstrumentSeniorityType1Code | 716 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}DecimalNumber | 724 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}DerivativeCommodity2 | 730 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}DerivativeForeignExchange3 | 737 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}DerivativeInstrument5 | 743 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}DerivativeInterest3 | 755 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Document | 763 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnergyCommodityCoal1 | 768 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnergyCommodityDistillates1 | 774 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnergyCommodityElectricity1 | 780 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnergyCommodityInterEnergy1 | 787 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnergyCommodityLightEnd1 | 793 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnergyCommodityNaturalGas1 | 799 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnergyCommodityOil1 | 806 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnergyCommodityRenewableEnergy1 | 813 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnvironmentalCommodityCarbonRelated1 | 819 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnvironmentalCommodityEmission1 | 825 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}EnvironmentalCommodityWeather1 | 832 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FertilizerCommodityAmmonia1 | 838 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FertilizerCommodityDiammoniumPhosphate1 | 844 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FertilizerCommodityPotash1 | 850 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FertilizerCommoditySulphur1 | 856 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FertilizerCommodityUrea1 | 862 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FertilizerCommodityUreaAndAmmoniumNitrate1 | 868 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FinancialInstrument48Choice | 874 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FinancialInstrument53 | 881 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FinancialInstrument58 | 887 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FinancialInstrumentIdentification5Choice | 893 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FinancialInstrumentReportingReferenceDataDeltaReportV03 | 899 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FloatingInterestRate6 | 906 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FloatingInterestRate8 | 913 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FreightCommodityContainerShip1 | 919 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FreightCommodityDry1 | 925 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}FreightCommodityWet1 | 932 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}ISINOct2015Identifier | 939 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}ISODate | 944 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}ISODateTime | 947 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}IndustrialProductCommodityConstruction1 | 950 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}IndustrialProductCommodityManufacturing1 | 956 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}InterestRate6Choice | 962 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}InterestRate8Choice | 968 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}InterestRateContractTerm2 | 974 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}LEIIdentifier | 980 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}MICIdentifier | 985 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Max25Text | 990 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Max350Text | 996 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Max35Text | 1002 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Max3Number | 1008 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Max50Text | 1014 |
| [type-0158](types/type-0158.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Max5Number | 1020 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}MetalCommodityNonPrecious1 | 1026 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}MetalCommodityPrecious1 | 1033 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}NonNegativeDecimalNumber | 1040 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}OptionStyle7Code | 1047 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}OptionType2Code | 1056 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}OtherC10CommodityDeliverable2 | 1063 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}OtherC10CommodityNonDeliverable2 | 1069 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}PaperCommodityContainerBoard1 | 1075 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}PaperCommodityNewsprint1 | 1081 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}PaperCommodityPulp1 | 1087 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}PaperCommodityRecoveredPaper1 | 1093 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}PercentageRate | 1099 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Period2 | 1105 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}Period4Choice | 1111 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}PhysicalTransferType4Code | 1119 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}PlusOrMinusIndicator | 1126 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}PolypropyleneCommodityPlastic1 | 1129 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}PriceStatus1Code | 1135 |
| [type-0177](types/type-0177.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}RateBasis1Code | 1141 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}RecordTechnicalData4 | 1149 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SecuritiesMarketReportHeader1 | 1160 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SecuritiesReferenceDataReport6 | 1167 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SecuritiesReferenceDataReport7 | 1178 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SecuritiesReferenceDeltaStatusReport5Choice | 1189 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SecuritiesTransactionPrice1 | 1197 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SecuritiesTransactionPrice2Choice | 1203 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SecuritiesTransactionPrice4Choice | 1211 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SecurityInstrumentDescription17 | 1217 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SecurityInstrumentDescription9 | 1227 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SupplementaryData1 | 1237 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}SupplementaryDataEnvelope1 | 1243 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}TradingVenue2Code | 1248 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}TradingVenueAttributes1 | 1254 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}TradingVenueAttributes2 | 1264 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}TradingVenueIdentification1Choice | 1274 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}TradingVenueIdentification2 | 1281 |
| [type-0195](types/type-0195.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.036.001.03}TrueFalseIndicator | 1287 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 22 |
| complexType | 95 |
| element | 280 |
| enumeration | 195 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 4 |
| minInclusive | 3 |
| minLength | 4 |
| pattern | 7 |
| restriction | 99 |
| schema | 1 |
| sequence | 71 |
| simpleContent | 2 |
| simpleType | 99 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/711171b90cb3da84d6f4709e.md) · [Message](index.md)
