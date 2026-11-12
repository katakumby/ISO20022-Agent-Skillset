---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.007.001.10"
message_family: "camt.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10"
source_ids: ["src-000021"]
source_editions: ["2024-2025"]
---

# camt.007.001.10 structure

[src-000021](../../../../../raw-input/cash_management/camt.007.001.10.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.007.001.10`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.007.001.10 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}AddressType3Choice | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}BICFIDec2014Identifier | 21 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}BranchAndFinancialInstitutionIdentification8 | 26 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}BranchData5 | 32 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}ClearingSystemIdentification2Choice | 40 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}ClearingSystemMemberIdentification2 | 46 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}CountryCode | 52 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}DateTimePeriod1 | 57 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}DateTimePeriod1Choice | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Document | 70 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}EntryTypeIdentifier | 75 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Exact4AlphaNumericText | 80 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}ExternalClearingSystemIdentification1Code | 85 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}ExternalFinancialInstitutionIdentification1Code | 91 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}FinancialIdentificationSchemeName1Choice | 97 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}FinancialInstitutionIdentification23 | 103 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}GenericFinancialIdentification1 | 113 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}GenericIdentification30 | 120 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}ISODate | 127 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}ISODateTime | 130 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}ImpliedCurrencyAndAmount | 133 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Instruction1Code | 140 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}LEIIdentifier | 147 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}LongPaymentIdentification4 | 152 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Max140Text | 165 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Max16Text | 171 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Max350Text | 177 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Max35Text | 183 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Max3NumericText | 189 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Max70Text | 194 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}MessageHeader1 | 200 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}ModifyTransactionV10 | 206 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}PaymentIdentification8Choice | 213 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}PaymentInstruction33 | 223 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}PaymentInstrument1Code | 231 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}PaymentOrigin1Choice | 245 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}PaymentType3Code | 253 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}PaymentType4Choice | 281 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}PostalAddress27 | 287 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Priority1Choice | 309 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}Priority5Code | 315 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}QueueTransactionIdentification1 | 323 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}ShortPaymentIdentification4 | 329 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}SupplementaryData1 | 337 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}SupplementaryDataEnvelope1 | 343 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}TransactionModification7 | 348 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.007.001.10}UUIDv4Identifier | 354 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 8 |
| complexType | 26 |
| element | 93 |
| enumeration | 47 |
| fractionDigits | 1 |
| maxLength | 7 |
| minInclusive | 1 |
| minLength | 7 |
| pattern | 7 |
| restriction | 22 |
| schema | 1 |
| sequence | 18 |
| simpleType | 22 |
| totalDigits | 1 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
