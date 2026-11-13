---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.021.001.06"
message_family: "camt.021"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.021.001.06"
source_ids: ["src-000035"]
source_editions: ["2024-2025"]
---

# camt.021.001.06 structure

[src-000035](../../../../../raw-input/cash_management/camt.021.001.06.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.021.001.06`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.021.001.06 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}Document | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}ErrorHandling3Choice | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}ErrorHandling5 | 16 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}ExternalEnquiryRequestType1Code | 22 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}ExternalPaymentControlRequestType1Code | 28 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}ExternalSystemErrorHandling1Code | 34 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}GeneralBusinessInformation1 | 40 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}GeneralBusinessOrError7Choice | 47 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}GeneralBusinessOrError8Choice | 53 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}GeneralBusinessReport6 | 59 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}GenericIdentification1 | 65 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}ISODateTime | 72 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}InformationQualifierType1 | 75 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}Max140Text | 81 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}Max350Text | 87 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}Max35Text | 93 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}MessageHeader7 | 99 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}OriginalBusinessQuery1 | 108 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}Priority1Code | 115 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}RequestType4Choice | 122 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}ReturnGeneralBusinessInformationV06 | 129 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}SupplementaryData1 | 136 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}SupplementaryDataEnvelope1 | 142 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.021.001.06}YesNoIndicator | 147 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 4 |
| complexType | 15 |
| element | 36 |
| enumeration | 3 |
| maxLength | 6 |
| minLength | 6 |
| restriction | 9 |
| schema | 1 |
| sequence | 11 |
| simpleType | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/5efca5bdd9d71a317817c6e8.md) · [Message](index.md)
