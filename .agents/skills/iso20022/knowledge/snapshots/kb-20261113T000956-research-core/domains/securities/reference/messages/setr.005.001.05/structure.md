---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.005.001.05"
message_family: "setr.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.005.001.05"
source_ids: ["src-000141"]
source_editions: ["2025-2026"]
---

# setr.005.001.05 structure

[src-000141](../../../../../raw-input/investment_funds/setr.005.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.005.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.005.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}AdditionalReference10 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}AdditionalReference11 | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}AddressType2Code | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}AnyBICDec2014Identifier | 29 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}CancellationReason32Choice | 34 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}CopyInformation5 | 40 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}CountryCode | 46 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}Document | 51 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}Exact4AlphaNumericText | 56 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}GenericIdentification1 | 61 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}GenericIdentification30 | 68 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}ISODateTime | 75 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}InvestmentFundOrder13 | 78 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}LEIIdentifier | 87 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}Max16Text | 92 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}Max350Text | 98 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}Max35Text | 104 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}Max70Text | 110 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}MessageIdentification1 | 116 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}NameAndAddress5 | 122 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}PartyIdentification125Choice | 128 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}PartyIdentification139 | 135 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}PostalAddress1 | 141 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}RedemptionOrderCancellationRequestV05 | 153 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.005.001.05}YesNoIndicator | 163 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| choice | 2 |
| complexType | 14 |
| element | 46 |
| enumeration | 6 |
| maxLength | 4 |
| minLength | 4 |
| pattern | 4 |
| restriction | 11 |
| schema | 1 |
| sequence | 12 |
| simpleType | 11 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/13dd3a45b5dbec6321226555.md) · [Message](index.md)
