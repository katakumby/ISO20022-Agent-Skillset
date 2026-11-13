---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "auth.033.001.03"
message_family: "auth.033"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.033.001.03"
source_ids: ["src-000327"]
source_editions: ["2025"]
---

# auth.033.001.03 structure

[src-000327](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.033.001.03.xsd); `urn:iso:std:iso:20022:tech:xsd:auth.033.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:auth.033.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}ActiveCurrencyCode | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}ActiveOrHistoricCurrencyCode | 10 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}AssetClassSubProductType19Code | 15 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}BenchmarkCurveName2Code | 21 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}BenchmarkCurveName5Choice | 51 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}BondDerivative2 | 57 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}BondType1Code | 64 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CommodityDerivative2Choice | 74 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CommodityDerivative4 | 80 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CommodityDerivative5 | 86 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CommodityDerivative6 | 92 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}ContractForDifference2 | 97 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CountryCode | 104 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CountrySubDivisionCode | 109 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CreditDefaultSwapDerivative5 | 114 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CreditDefaultSwapDerivative6 | 120 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CreditDefaultSwapIndex3 | 127 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CreditDefaultSwapSingleName2 | 138 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}CreditDefaultSwapsDerivative4Choice | 145 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}DebtInstrument5 | 153 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Derivative3Choice | 159 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}DerivativePartyIdentification1Choice | 170 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Document | 177 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}EmissionAllowanceProductType1Code | 182 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}EquityDerivative2 | 191 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}EquityDerivative3Choice | 197 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}EquityReturnParameter1Code | 205 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}ExternalEmissionAllowanceSubProductType1Code | 213 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}ExternalProductType1Code | 219 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}FinancialInstrumentContractType1Code | 225 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}FinancialInstrumentReportingNonEquityTransparencyDataReportV03 | 242 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}FloatingInterestRate8 | 249 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}ForeignExchangeDerivative2 | 255 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}ISINOct2015Identifier | 260 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}ISODate | 265 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}ISODateTime | 268 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}InflationIndex1Choice | 271 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}InterestRateContractTerm2 | 277 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}InterestRateDerivative2Choice | 283 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}InterestRateDerivative5 | 289 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}LEIIdentifier | 299 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}MICIdentifier | 304 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Max25Text | 309 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Max350Text | 315 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Max35Text | 321 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Max3Number | 327 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Max50Text | 333 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}NonEquityInstrumentReportingClassification1Code | 339 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Number | 350 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Period2 | 356 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}Period4Choice | 362 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}RateBasis1Code | 370 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}RestrictedMonthExact2Number | 378 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}SecuritiesMarketReportHeader1 | 387 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}SupplementaryData1 | 394 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}SupplementaryDataEnvelope1 | 400 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}SwapType1Code | 405 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}TradingVenue2Code | 419 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}TradingVenueIdentification1Choice | 425 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}TradingVenueIdentification2 | 432 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}TransparencyDataReport21 | 438 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}TrueFalseIndicator | 454 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}UnderlyingContractForDifferenceType3Code | 457 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}UnderlyingEquityType3Code | 469 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}UnderlyingEquityType4Code | 474 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}UnderlyingEquityType5Code | 482 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}UnderlyingEquityType6Code | 490 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.033.001.03}UnderlyingInterestRateType3Code | 502 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 10 |
| complexType | 33 |
| element | 100 |
| enumeration | 108 |
| fractionDigits | 3 |
| maxInclusive | 1 |
| maxLength | 6 |
| minInclusive | 1 |
| minLength | 6 |
| pattern | 8 |
| restriction | 35 |
| schema | 1 |
| sequence | 23 |
| simpleType | 35 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/e73ae8a672a43d2c04d4a19f.md) · [Message](index.md)
