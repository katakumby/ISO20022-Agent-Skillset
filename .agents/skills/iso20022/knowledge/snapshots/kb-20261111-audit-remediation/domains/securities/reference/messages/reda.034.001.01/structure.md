---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.034.001.01"
message_family: "reda.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.034.001.01"
source_ids: ["src-000289"]
source_editions: ["june-2021"]
---

# reda.034.001.01 structure

[src-000289](../../../../../raw-input/target2securities_t2s/reda.034.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.034.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.034.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}AuditTrail1 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}AuditTrailOrBusinessError6Choice | 15 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}DatePeriod2 | 21 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}DatePeriodSearch1Choice | 27 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}Document | 36 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}ErrorHandling3Choice | 41 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}ErrorHandling5 | 47 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}ExternalFinancialInstrumentIdentificationType1Code | 53 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}ExternalSystemErrorHandling1Code | 59 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}ISIN2021Identifier | 65 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}ISODate | 70 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}ISODateTime | 73 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}IdentificationSource3Choice | 76 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}Max140Text | 82 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}Max16Text | 88 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}Max256Text | 94 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}Max350Text | 100 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}Max35Text | 106 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}MessageHeader12 | 112 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}OriginalBusinessInstruction1 | 119 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}OtherIdentification1 | 126 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}SecuritiesAuditTrailOrOperationalError4Choice | 133 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}SecuritiesAuditTrailReport4 | 139 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}SecuritiesAuditTrailReportV01 | 146 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}SecurityIdentification39 | 153 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}SupplementaryData1 | 160 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.034.001.01}SupplementaryDataEnvelope1 | 166 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 5 |
| complexType | 17 |
| element | 45 |
| maxLength | 7 |
| minLength | 7 |
| pattern | 1 |
| restriction | 10 |
| schema | 1 |
| sequence | 12 |
| simpleType | 10 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
