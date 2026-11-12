---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "auth.044.001.03"
message_family: "auth.044"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.044.001.03"
source_ids: ["src-000335"]
source_editions: ["2025"]
---

# auth.044.001.03 structure

[src-000335](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.044.001.03_1.xsd); `urn:iso:std:iso:20022:tech:xsd:auth.044.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:auth.044.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}CountryCode | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}DecimalNumber | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}Document | 35 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}EquityInstrumentReportingClassification1Code | 40 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}FinancialInstrumentReportingEquityTradingActivityResultV03 | 49 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}ISINOct2015Identifier | 56 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}ISODate | 61 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}ISODateTime | 64 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}MICIdentifier | 67 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}MarketDetail2 | 72 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}Max350Text | 78 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}Max35Text | 84 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}Max50Text | 90 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}Number | 96 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}Period2 | 102 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}Period4Choice | 108 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}SecuritiesMarketReportHeader1 | 116 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}StatisticsTransparency3 | 123 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}SupplementaryData1 | 135 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}SupplementaryDataEnvelope1 | 141 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}TradingVenue2Code | 146 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}TradingVenueIdentification1Choice | 152 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}TradingVenueIdentification2 | 159 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}TransparencyDataReport22 | 165 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}TransparencyMethodology2Code | 180 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.044.001.03}TrueFalseIndicator | 188 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 2 |
| complexType | 13 |
| element | 42 |
| enumeration | 11 |
| extension | 1 |
| fractionDigits | 3 |
| maxLength | 3 |
| minInclusive | 1 |
| minLength | 3 |
| pattern | 4 |
| restriction | 16 |
| schema | 1 |
| sequence | 10 |
| simpleContent | 1 |
| simpleType | 16 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
