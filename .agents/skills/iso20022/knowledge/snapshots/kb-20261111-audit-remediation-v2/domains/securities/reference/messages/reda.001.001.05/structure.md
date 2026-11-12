---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.001.001.05"
message_family: "reda.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.001.001.05"
source_ids: ["src-000109"]
source_editions: ["2025-2026"]
---

# reda.001.001.05 structure

[src-000109](../../../../../raw-input/investment_funds/reda.001.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.001.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.001.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ActiveCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ActiveCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ActiveOrHistoricCurrencyAndAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ActiveOrHistoricCurrencyAndAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}AdditionalReference10 | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}AddressType2Code | 64 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}AlternateSecurityIdentification7 | 74 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}AnyBICDec2014Identifier | 80 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}BelgianIdentifier | 85 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Bloomberg2Identifier | 88 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}CUSIPIdentifier | 93 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}CalculationBasis2Choice | 96 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}CalculationBasis2Code | 102 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Charge33 | 110 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ChargeType11Choice | 117 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ChargeType9Code | 123 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ConsolidatedTapeAssociationIdentifier | 136 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}CountryCode | 142 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}DTI2024Identifier | 147 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}DateAndDateTime2Choice | 152 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}DateFormat42Choice | 158 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}DateOrDateTimePeriod4Choice | 164 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}DatePeriod2 | 170 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}DateTimePeriod1 | 176 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}DecimalNumber | 182 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}DistributionPolicy1Code | 188 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Document | 194 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}DutchIdentifier | 199 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}EUCapitalGain2Code | 202 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}EUCapitalGainType4Choice | 209 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}EUDividendStatus1Code | 215 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}EUDividendStatusType3Choice | 222 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}EuroclearClearstreamIdentifier | 228 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}EventFrequency1Code | 234 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Extension1 | 251 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}FinancialInstrument106 | 257 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}FinancialInstrumentQuantity1 | 272 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}FormOfSecurity1Code | 277 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}GenericIdentification1 | 283 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ISINOct2015Identifier | 290 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ISODate | 295 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ISODateTime | 298 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ISOYearMonth | 301 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}IdentificationSource1Choice | 304 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}LEIIdentifier | 310 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Max140Text | 315 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Max16Text | 321 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Max350Text | 327 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Max35Text | 333 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Max5NumericText | 339 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Max70Text | 344 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}MessageIdentification1 | 350 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}NameAndAddress5 | 356 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Number | 362 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Pagination1 | 368 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PartyIdentification125Choice | 374 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PartyIdentification139 | 381 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PercentageRate | 387 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PerformanceFactors5 | 393 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PlusOrMinusIndicator | 401 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PostalAddress1 | 404 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceMethod1Code | 416 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceRateOrAmount3Choice | 422 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceReportFunction1Code | 428 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceReportV05 | 435 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceType2 | 449 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceType6Choice | 455 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceValuation5 | 461 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceValue1 | 481 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceValue5 | 486 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}PriceValueChange1 | 491 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}QUICKIdentifier | 498 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}RICIdentifier | 501 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}SEDOLIdentifier | 507 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}SecurityIdentification46Choice | 510 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Series1 | 530 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}SicovamIdentifier | 536 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}StatisticsByPredefinedTimePeriods2 | 539 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}StatisticsByUserDefinedTimePeriod3 | 548 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}Tax43 | 557 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}TaxCalculationInformation12 | 566 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}TaxType12Code | 575 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}TaxType4Choice | 585 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}TaxableIncomePerShareCalculated2Code | 591 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}TaxableIncomePerShareCalculated3Choice | 598 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}TickerIdentifier | 604 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}TypeOfPrice6Code | 610 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}TypeOfPrice9Code | 628 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}UnitPrice24 | 647 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ValorenIdentifier | 667 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ValuationStatistics4 | 670 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}ValuationTiming1Code | 680 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}WertpapierIdentifier | 687 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.001.001.05}YesNoIndicator | 690 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 3 |
| choice | 14 |
| complexType | 46 |
| element | 171 |
| enumeration | 88 |
| extension | 3 |
| fractionDigits | 6 |
| maxLength | 9 |
| minInclusive | 3 |
| minLength | 9 |
| pattern | 9 |
| restriction | 52 |
| schema | 1 |
| sequence | 29 |
| simpleContent | 3 |
| simpleType | 52 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
