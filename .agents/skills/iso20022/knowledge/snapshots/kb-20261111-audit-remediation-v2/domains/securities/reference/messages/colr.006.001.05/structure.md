---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "colr.006.001.05"
message_family: "colr.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.006.001.05"
source_ids: ["src-000068"]
source_editions: []
---

# colr.006.001.05 structure

[src-000068](../../../../../raw-input/collateral_management_collateral_management/colr.006.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:colr.006.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:colr.006.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}AnyBICDec2014Identifier | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}BlockChainAddressWallet5 | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}CollateralAccount3 | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}CollateralAccountIdentificationType3Choice | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}CollateralAccountType1Code | 30 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}CollateralCancellationStatus2 | 39 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}CollateralManagementCancellationStatusV05 | 46 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}CountryCode | 55 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}DateAndDateTime2Choice | 60 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Document | 66 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}ExposureType11Code | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}GenericIdentification36 | 111 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}ISODate | 118 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}ISODateTime | 121 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Max140Text | 124 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Max16Text | 130 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Max350Text | 136 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Max35Text | 142 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Max70Text | 148 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}NameAndAddress6 | 154 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Obligation9 | 160 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}PartyIdentification178Choice | 172 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}PostalAddress2 | 179 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Reference16 | 188 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}RejectionReason68Code | 193 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}RejectionStatus3 | 205 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}Status4Code | 211 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}SupplementaryData1 | 217 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.006.001.05}SupplementaryDataEnvelope1 | 223 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 3 |
| complexType | 16 |
| element | 46 |
| enumeration | 51 |
| maxLength | 5 |
| minLength | 5 |
| pattern | 2 |
| restriction | 13 |
| schema | 1 |
| sequence | 13 |
| simpleType | 13 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
