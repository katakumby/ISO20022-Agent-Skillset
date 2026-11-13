---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "auth.047.001.01"
message_family: "auth.047"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.047.001.01"
source_ids: ["src-000337"]
source_editions: ["2025"]
---

# auth.047.001.01 structure

[src-000337](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.047.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:auth.047.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:auth.047.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}CountryCode | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}CountryCodeAndName3 | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}Document | 16 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}FinancialInstrumentReportingCountryCodeReportV01 | 21 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}ISODate | 27 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}Max350Text | 30 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}Max70Text | 36 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}Modification1Code | 42 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}Period2 | 50 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}Period4Choice | 56 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}SecuritiesCountryIdentification2 | 64 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}SupplementaryData1 | 73 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}SupplementaryDataEnvelope1 | 79 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.047.001.01}TrueFalseIndicator | 84 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 1 |
| complexType | 8 |
| element | 19 |
| enumeration | 4 |
| maxLength | 2 |
| minLength | 2 |
| pattern | 1 |
| restriction | 6 |
| schema | 1 |
| sequence | 7 |
| simpleType | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/66a25eb3b8e0daa2eeb4288d.md) · [Message](index.md)
