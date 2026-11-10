---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.002.001.05"
message_family: "reda.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.002.001.05"
source_ids: ["src-000110"]
source_editions: ["2025-2026"]
---

# reda.002.001.05 structure

[src-000110](../../../../../raw-input/investment_funds/reda.002.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.002.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.002.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ActiveCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ActiveCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ActiveOrHistoricCurrencyAndAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ActiveOrHistoricCurrencyAndAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}AdditionalReference10 | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}AddressType2Code | 64 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}AlternateSecurityIdentification7 | 74 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}AnyBICDec2014Identifier | 80 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}BelgianIdentifier | 85 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Bloomberg2Identifier | 88 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}CUSIPIdentifier | 93 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}CalculationBasis2Choice | 96 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}CalculationBasis2Code | 102 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Charge33 | 110 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ChargeType11Choice | 117 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ChargeType9Code | 123 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ConsolidatedTapeAssociationIdentifier | 136 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}CountryCode | 142 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DTI2024Identifier | 147 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DateAndDateTime1Choice | 152 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DateAndDateTime2Choice | 158 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DateFormat42Choice | 164 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DateOrDateTimePeriod4Choice | 170 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DatePeriod2 | 176 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DateTimePeriod1 | 182 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DecimalNumber | 188 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DistributionPolicy1Code | 194 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Document | 200 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}DutchIdentifier | 205 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}EUCapitalGain2Code | 208 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}EUCapitalGainType4Choice | 215 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}EUDividendStatus1Code | 221 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}EUDividendStatusType3Choice | 228 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}EuroclearClearstreamIdentifier | 234 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}EventFrequency1Code | 240 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Extension1 | 257 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}FinancialInstrument106 | 263 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}FinancialInstrumentQuantity1 | 278 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}FormOfSecurity1Code | 283 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}GenericIdentification1 | 289 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ISINOct2015Identifier | 296 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ISODate | 301 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ISODateTime | 304 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ISOYearMonth | 307 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}IdentificationSource1Choice | 310 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}LEIIdentifier | 316 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Max140Text | 321 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Max16Text | 327 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Max350Text | 333 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Max35Text | 339 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Max5NumericText | 345 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Max70Text | 350 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}MessageIdentification1 | 356 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}NameAndAddress5 | 362 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Number | 368 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Pagination1 | 374 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PartyIdentification125Choice | 380 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PartyIdentification139 | 387 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PercentageRate | 393 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PerformanceFactors5 | 399 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PlusOrMinusIndicator | 407 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PostalAddress1 | 410 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceMethod1Code | 422 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceRateOrAmount3Choice | 428 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceReport4 | 434 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceReportCancellationV05 | 439 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceType2 | 454 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceType6Choice | 460 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceValuation5 | 466 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceValue1 | 486 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceValue5 | 491 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}PriceValueChange1 | 496 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}QUICKIdentifier | 503 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}RICIdentifier | 506 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}SEDOLIdentifier | 512 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}SecurityIdentification46Choice | 515 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Series1 | 535 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}SicovamIdentifier | 541 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}StatisticsByPredefinedTimePeriods2 | 544 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}StatisticsByUserDefinedTimePeriod3 | 553 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}Tax43 | 562 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}TaxCalculationInformation12 | 571 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}TaxType12Code | 580 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}TaxType4Choice | 590 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}TaxableIncomePerShareCalculated2Code | 596 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}TaxableIncomePerShareCalculated3Choice | 603 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}TickerIdentifier | 609 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}TypeOfPrice6Code | 615 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}TypeOfPrice9Code | 633 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}UnitPrice24 | 652 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ValorenIdentifier | 672 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ValuationStatistics4 | 675 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}ValuationTiming1Code | 685 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}WertpapierIdentifier | 692 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.002.001.05}YesNoIndicator | 695 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 3 |
| choice | 15 |
| complexType | 48 |
| element | 175 |
| enumeration | 85 |
| extension | 3 |
| fractionDigits | 6 |
| maxLength | 9 |
| minInclusive | 3 |
| minLength | 9 |
| pattern | 9 |
| restriction | 51 |
| schema | 1 |
| sequence | 30 |
| simpleContent | 3 |
| simpleType | 51 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
