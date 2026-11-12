---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.101.001.02"
message_family: "camt.101"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.101.001.02"
source_ids: ["src-000048"]
source_editions: ["2024-2025"]
---

# camt.101.001.02 structure

[src-000048](../../../../../raw-input/cash_management/camt.101.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.101.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.101.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}AddressType2Code | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}AddressType3Choice | 46 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Amount2Choice | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}BICFIDec2014Identifier | 58 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}BranchAndFinancialInstitutionIdentification8 | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}BranchData5 | 69 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ClearingSystemIdentification2Choice | 77 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ClearingSystemMemberIdentification2 | 83 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}CountryCode | 89 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}CreateLimitV02 | 94 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}CreditDebitCode | 101 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}DateAndDateTime2Choice | 107 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Document | 113 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Exact4AlphaNumericText | 118 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ExternalAccountIdentification1Code | 123 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ExternalClearingSystemIdentification1Code | 129 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ExternalFinancialInstitutionIdentification1Code | 135 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ExternalMarketInfrastructure1Code | 141 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}FinancialIdentificationSchemeName1Choice | 147 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}FinancialInstitutionIdentification23 | 153 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}GenericAccountIdentification1 | 163 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}GenericFinancialIdentification1 | 170 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}GenericIdentification30 | 177 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}IBAN2007Identifier | 184 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ISODate | 189 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ISODateTime | 192 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}ImpliedCurrencyAndAmount | 195 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}LEIIdentifier | 202 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}LimitIdentification8 | 207 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}LimitStructure6 | 216 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}LimitType1Choice | 224 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}LimitType3Code | 230 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}MarketInfrastructureIdentification1Choice | 249 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Max140Text | 255 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Max16Text | 261 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Max34Text | 267 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Max350Text | 273 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Max35Text | 279 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}Max70Text | 285 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}MessageHeader1 | 291 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}PostalAddress27 | 297 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}SupplementaryData1 | 319 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}SupplementaryDataEnvelope1 | 325 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.101.001.02}SystemIdentification2Choice | 330 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 10 |
| complexType | 26 |
| element | 79 |
| enumeration | 23 |
| extension | 1 |
| fractionDigits | 2 |
| maxLength | 10 |
| minInclusive | 2 |
| minLength | 10 |
| pattern | 6 |
| restriction | 23 |
| schema | 1 |
| sequence | 15 |
| simpleContent | 1 |
| simpleType | 23 |
| totalDigits | 2 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
