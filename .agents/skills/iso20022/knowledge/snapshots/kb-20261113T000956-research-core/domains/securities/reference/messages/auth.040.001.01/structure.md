---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "auth.040.001.01"
message_family: "auth.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.040.001.01"
source_ids: ["src-000331"]
source_editions: ["2025"]
---

# auth.040.001.01 structure

[src-000331](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.040.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:auth.040.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:auth.040.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}ActiveOrHistoricCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}ActiveOrHistoricCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}ActiveOrHistoricCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}CountryCode | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}DecimalNumberFraction5 | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}Document | 35 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}FinancialInstrumentReportingEquityTradingActivityReportV01 | 40 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}ISINOct2015Identifier | 47 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}ISODate | 52 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}ISODateTime | 55 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}MICIdentifier | 58 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}Max350Text | 63 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}Max35Text | 69 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}Max50Text | 75 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}NumberAndVolume2 | 81 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}Period2 | 87 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}Period4Choice | 93 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}SecuritiesMarketReportHeader1 | 101 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}SupplementaryData1 | 108 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}SupplementaryDataEnvelope1 | 114 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}TradingVenue2Code | 119 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}TradingVenueIdentification1Choice | 125 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}TradingVenueIdentification2 | 132 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}TransparencyDataReport13 | 138 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.040.001.01}TrueFalseIndicator | 150 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 2 |
| complexType | 12 |
| element | 31 |
| enumeration | 2 |
| extension | 1 |
| fractionDigits | 2 |
| maxLength | 3 |
| minInclusive | 1 |
| minLength | 3 |
| pattern | 4 |
| restriction | 13 |
| schema | 1 |
| sequence | 9 |
| simpleContent | 1 |
| simpleType | 13 |
| totalDigits | 2 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/f472bec0a44113661ab92fd8.md) · [Message](index.md)
