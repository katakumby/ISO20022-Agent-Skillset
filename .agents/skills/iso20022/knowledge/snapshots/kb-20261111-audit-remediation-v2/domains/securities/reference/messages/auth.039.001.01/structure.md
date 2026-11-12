---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "auth.039.001.01"
message_family: "auth.039"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.039.001.01"
source_ids: ["src-000330"]
source_editions: ["2025"]
---

# auth.039.001.01 structure

[src-000330](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.039.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:auth.039.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:auth.039.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}CountryCode | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}Document | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}FinancialInstrumentReportingNonWorkingDayReportV01 | 15 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}ISODate | 22 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}ISODateTime | 25 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}MICIdentifier | 28 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}Max350Text | 33 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}Max35Text | 39 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}Max50Text | 45 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}NonTradingDayReason1Code | 51 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}Period2 | 61 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}Period4Choice | 67 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}SecuritiesMarketReportHeader1 | 75 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}SecuritiesNonTradingDay1 | 82 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}SecuritiesNonTradingDayReport1 | 89 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}SupplementaryData1 | 95 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}SupplementaryDataEnvelope1 | 101 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}TradingVenue2Code | 106 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}TradingVenueIdentification1Choice | 112 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.039.001.01}TradingVenueIdentification2 | 119 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 2 |
| complexType | 11 |
| element | 26 |
| enumeration | 8 |
| maxLength | 3 |
| minLength | 3 |
| pattern | 2 |
| restriction | 9 |
| schema | 1 |
| sequence | 9 |
| simpleType | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
