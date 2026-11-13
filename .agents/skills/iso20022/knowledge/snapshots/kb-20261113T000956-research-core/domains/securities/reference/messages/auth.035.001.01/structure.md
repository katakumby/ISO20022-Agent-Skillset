---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "auth.035.001.01"
message_family: "auth.035"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.035.001.01"
source_ids: ["src-000328"]
source_editions: ["2025"]
---

# auth.035.001.01 structure

[src-000328](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.035.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:auth.035.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:auth.035.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}ActiveOrHistoricCurrencyCode | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}CountryCode | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}Document | 15 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}FinancialInstrumentReportingTradingVolumeCapDataReportV01 | 20 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}ISINOct2015Identifier | 27 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}ISODate | 32 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}ISODateTime | 35 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}ImpliedCurrencyAndAmount | 38 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}MICIdentifier | 45 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}Max350Text | 50 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}Max35Text | 56 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}Max50Text | 62 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}Period2 | 68 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}Period4Choice | 74 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}SecuritiesMarketReportHeader1 | 82 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}SupplementaryData1 | 89 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}SupplementaryDataEnvelope1 | 95 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}TradingVenue2Code | 100 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}TradingVenueIdentification1Choice | 106 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}TradingVenueIdentification2 | 113 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}VolumeCapReport1 | 119 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.035.001.01}VolumeCapReport2 | 126 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 2 |
| complexType | 11 |
| element | 30 |
| enumeration | 2 |
| fractionDigits | 1 |
| maxLength | 3 |
| minInclusive | 1 |
| minLength | 3 |
| pattern | 4 |
| restriction | 11 |
| schema | 1 |
| sequence | 9 |
| simpleType | 11 |
| totalDigits | 1 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/b366d5e11eab1ea6b89313e0.md) · [Message](index.md)
