---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.013.001.04"
message_family: "camt.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.013.001.04"
source_ids: ["src-000027"]
source_editions: ["2024-2025"]
---

# camt.013.001.04 structure

[src-000027](../../../../../raw-input/cash_management/camt.013.001.04.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.013.001.04`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.013.001.04 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}BICFIDec2014Identifier | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}ClearingSystemIdentification2Choice | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}ClearingSystemMemberIdentification2 | 16 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}Document | 22 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}ExternalClearingSystemIdentification1Code | 27 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}ExternalEnquiryRequestType1Code | 33 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}ExternalFinancialInstitutionIdentification1Code | 39 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}ExternalPaymentControlRequestType1Code | 45 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}ExternalSystemMemberType1Code | 51 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}FinancialIdentificationSchemeName1Choice | 57 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}GenericFinancialIdentification1 | 63 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}GenericIdentification1 | 70 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}GetMemberV04 | 77 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}ISODateTime | 84 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}Max350Text | 87 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}Max35Text | 93 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}MemberCriteria4 | 99 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}MemberCriteriaDefinition2Choice | 106 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}MemberIdentification3Choice | 112 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}MemberQueryDefinition4 | 119 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}MemberReturnCriteria1 | 125 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}MemberSearchCriteria4 | 136 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}MemberStatus1Code | 143 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}MessageHeader9 | 151 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}QueryType2Code | 158 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}RequestType4Choice | 166 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}RequestedIndicator | 173 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}SupplementaryData1 | 176 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}SupplementaryDataEnvelope1 | 182 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}SystemMemberStatus1Choice | 187 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.013.001.04}SystemMemberType1Choice | 193 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 7 |
| complexType | 19 |
| element | 49 |
| enumeration | 8 |
| maxLength | 7 |
| minLength | 7 |
| pattern | 1 |
| restriction | 12 |
| schema | 1 |
| sequence | 12 |
| simpleType | 12 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/a7bfc8dbb9b874e4ddf208c3.md) · [Message](index.md)
