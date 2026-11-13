---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "auth.045.001.03"
message_family: "auth.045"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.045.001.03"
source_ids: ["src-000336"]
source_editions: ["2025"]
---

# auth.045.001.03 structure

[src-000336](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.045.001.03.xsd); `urn:iso:std:iso:20022:tech:xsd:auth.045.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:auth.045.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}ActiveOrHistoricCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}ActiveOrHistoricCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}ActiveOrHistoricCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}AssetClassAndSubClassIdentification2 | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}CountryCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}DecimalNumber | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Document | 42 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}FinancialInstrumentReportingNonEquityTradingActivityResultV03 | 47 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}ISINOct2015Identifier | 54 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}ISODate | 59 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}ISODateTime | 62 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}InstrumentAndSubClassIdentification2 | 65 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}InstrumentOrSubClassIdentification2Choice | 72 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}MICIdentifier | 78 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Max1000Text | 83 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Max350Text | 89 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Max35Text | 95 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Max50Text | 101 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}NonEquityAssetClass1Code | 107 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}NonEquityInstrumentReportingClassification1Code | 125 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}NonEquitySubClass1 | 136 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}NonEquitySubClassSegmentationCriteria1Code | 142 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}NonEquitySubClassSegmentationCriterion1 | 182 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Number | 188 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Period2 | 194 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}Period4Choice | 200 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}SecuritiesMarketReportHeader1 | 208 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}StatisticsTransparency2 | 215 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}SupplementaryData1 | 221 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}SupplementaryDataEnvelope1 | 227 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}TonsOrCurrency2Choice | 232 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}TradingVenue2Code | 238 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}TradingVenueIdentification1Choice | 244 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}TradingVenueIdentification2 | 251 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}TransparencyDataReport20 | 257 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.045.001.03}TrueFalseIndicator | 272 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 4 |
| complexType | 18 |
| element | 48 |
| enumeration | 59 |
| extension | 1 |
| fractionDigits | 3 |
| maxLength | 4 |
| minInclusive | 1 |
| minLength | 4 |
| pattern | 4 |
| restriction | 18 |
| schema | 1 |
| sequence | 13 |
| simpleContent | 1 |
| simpleType | 18 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/9e1ff6801a8caf29a624c71d.md) · [Message](index.md)
