---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.036.001.01"
message_family: "reda.036"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.036.001.01"
source_ids: ["src-000291"]
source_editions: ["december-2019"]
---

# reda.036.001.01 structure

[src-000291](../../../../../raw-input/target2securities_t2s/reda.036.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.036.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.036.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}DatePeriod2 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}DatePeriodSearch1Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}Document | 20 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}Exact4AlphaNumericText | 25 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}GenericIdentification30 | 30 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}ISODate | 37 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}ISODateTime | 40 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}Max350Text | 43 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}Max35Text | 49 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}Max70Text | 55 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}MessageHeader1 | 61 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}SecuritiesAccount19 | 67 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}SecuritiesAccountAuditTrailQueryV01 | 74 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}SecuritiesAccountAuditTrailSearchCriteria3 | 81 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}SupplementaryData1 | 87 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.036.001.01}SupplementaryDataEnvelope1 | 93 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 1 |
| complexType | 10 |
| element | 24 |
| maxLength | 3 |
| minLength | 3 |
| pattern | 1 |
| restriction | 6 |
| schema | 1 |
| sequence | 9 |
| simpleType | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/7db3586230d9452c121b7ce4.md) · [Message](index.md)
