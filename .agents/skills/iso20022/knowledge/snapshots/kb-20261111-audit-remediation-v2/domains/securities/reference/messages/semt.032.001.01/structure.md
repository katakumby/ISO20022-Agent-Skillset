---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.032.001.01"
message_family: "semt.032"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.032.001.01"
source_ids: ["src-000315"]
source_editions: ["september-2025"]
---

# semt.032.001.01 structure

[src-000315](../../../../../raw-input/target2securities_t2s/semt.032.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.032.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.032.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}AnyBICDec2014Identifier | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}CancellationProcessingStatus3Code | 20 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}CancellationProcessingStatus9Choice | 30 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}CountryCode | 36 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}DateAndDateTimeSearch5Choice | 41 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}DatePeriod2 | 47 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}DatePeriodSearch1Choice | 53 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}DateTimePeriod1 | 62 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}DateTimeSearch2Choice | 68 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}Document | 77 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}Exact4AlphaNumericText | 82 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}GenericIdentification30 | 87 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}GenericIdentification36 | 94 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}ISODate | 101 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}ISODateTime | 104 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}InstructionQueryType1Code | 107 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}LEIIdentifier | 114 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}Max16Text | 119 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}Max350Text | 125 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}Max35Text | 131 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}Max70Text | 137 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}MovementResponseType1Code | 143 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}NameAndAddress5 | 149 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}PartyIdentification120Choice | 155 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}PartyIdentification136 | 162 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}PostalAddress1 | 168 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}SecuritiesAccount19 | 180 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}SecuritiesCancellationQueryCriteria1 | 187 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}SecuritiesCancellationQueryDefinition1 | 198 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}SecuritiesTransactionCancellationRequestQueryV01 | 204 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}SupplementaryData1 | 210 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}SupplementaryDataEnvelope1 | 216 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.032.001.01}SystemPartyIdentification8 | 221 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 5 |
| complexType | 20 |
| element | 59 |
| enumeration | 17 |
| maxLength | 4 |
| minLength | 4 |
| pattern | 4 |
| restriction | 14 |
| schema | 1 |
| sequence | 15 |
| simpleType | 14 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
