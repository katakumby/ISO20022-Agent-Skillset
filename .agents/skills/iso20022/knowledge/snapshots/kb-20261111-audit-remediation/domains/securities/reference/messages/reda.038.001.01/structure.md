---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.038.001.01"
message_family: "reda.038"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.038.001.01"
source_ids: ["src-000293"]
source_editions: ["august-2026"]
---

# reda.038.001.01 structure

[src-000293](../../../../../raw-input/target2securities_t2s/reda.038.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.038.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.038.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}Document | 18 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}Document | 18 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}AccountIdentification4Choice | 19 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}AccountSchemeName1Choice | 39 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}ActiveOrHistoricCurrencyCode | 59 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}CashAccount40 | 68 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}CashAccountActivityAdviceV01 | 111 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}CashAccountReferenceDataChange3 | 140 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}CashAccountStatement3 | 178 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}CashAccountType2Choice | 198 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}Document | 218 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}ExternalAccountIdentification1Code | 223 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}ExternalCashAccountType1Code | 235 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}ExternalProxyAccountType1Code | 247 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}GenericAccountIdentification1 | 258 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}IBAN2007Identifier | 284 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}ISODate | 293 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}ISODateTime | 300 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}Max2048Text | 313 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}Max34Text | 323 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}Max350Text | 333 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}Max35Text | 343 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}Max70Text | 353 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}MessageHeader1 | 363 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}ProxyAccountIdentification1 | 384 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}ProxyAccountType1Choice | 404 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}SupplementaryData1 | 424 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.038.001.01}SupplementaryDataEnvelope1 | 445 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| annotation | 57 |
| any | 1 |
| choice | 4 |
| complexType | 14 |
| documentation | 114 |
| element | 34 |
| maxLength | 8 |
| minLength | 8 |
| pattern | 2 |
| restriction | 12 |
| schema | 1 |
| sequence | 10 |
| simpleType | 12 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
