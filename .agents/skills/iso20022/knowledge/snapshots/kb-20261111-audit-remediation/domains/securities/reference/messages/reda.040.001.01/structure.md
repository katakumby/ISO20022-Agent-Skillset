---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.040.001.01"
message_family: "reda.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.040.001.01"
source_ids: ["src-000295"]
source_editions: ["august-2026"]
---

# reda.040.001.01 structure

[src-000295](../../../../../raw-input/target2securities_t2s/reda.040.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.040.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.040.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Document | 18 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Document | 18 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}AccountIdentification4Choice | 19 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}AccountSchemeName1Choice | 39 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ActiveOrHistoricCurrencyCode | 59 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}AuditTrail1 | 68 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}AuditTrailOrBusinessError6Choice | 112 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}CashAccount40 | 132 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}CashAccountAuditTrailOrOperationalError4Choice | 175 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}CashAccountAuditTrailReport4 | 195 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}CashAccountAuditTrailReportV01 | 221 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}CashAccountType2Choice | 247 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}DatePeriod2 | 267 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}DatePeriodSearch1Choice | 287 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Document | 325 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ErrorHandling3Choice | 330 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ErrorHandling5 | 350 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ExternalAccountIdentification1Code | 370 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ExternalCashAccountType1Code | 382 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ExternalProxyAccountType1Code | 394 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ExternalSystemErrorHandling1Code | 405 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}GenericAccountIdentification1 | 416 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}IBAN2007Identifier | 442 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ISODate | 451 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ISODateTime | 458 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Max140Text | 471 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Max2048Text | 481 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Max256Text | 491 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Max34Text | 501 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Max350Text | 511 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Max35Text | 521 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}Max70Text | 531 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}MessageHeader12 | 541 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}OriginalBusinessInstruction1 | 568 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ProxyAccountIdentification1 | 594 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}ProxyAccountType1Choice | 614 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}SupplementaryData1 | 634 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.040.001.01}SupplementaryDataEnvelope1 | 655 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| annotation | 88 |
| any | 1 |
| choice | 8 |
| complexType | 21 |
| documentation | 176 |
| element | 55 |
| maxLength | 11 |
| minLength | 11 |
| pattern | 2 |
| restriction | 15 |
| schema | 1 |
| sequence | 13 |
| simpleType | 15 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
