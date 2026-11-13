---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.049.001.03"
message_family: "setr.049"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.049.001.03"
source_ids: ["src-000156"]
source_editions: ["2025-2026"]
---

# setr.049.001.03 structure

[src-000156](../../../../../raw-input/investment_funds/setr.049.001.03.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.049.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.049.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}AdditionalReference10 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}AdditionalReference11 | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}AddressType2Code | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}AnyBICDec2014Identifier | 29 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}CancellationReason31Choice | 34 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}ConfirmationCancellationReason1Code | 40 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}CopyInformation5 | 66 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}CountryCode | 72 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}Document | 77 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}Exact4AlphaNumericText | 82 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}GenericIdentification1 | 87 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}GenericIdentification47 | 94 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}ISODateTime | 101 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}InvestmentFundOrder14 | 104 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}LEIIdentifier | 114 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}Max16Text | 119 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}Max350Text | 125 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}Max35Text | 131 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}Max4AlphaNumericText | 137 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}Max70Text | 144 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}MessageIdentification1 | 150 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}NameAndAddress5 | 156 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}PartyIdentification125Choice | 162 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}PartyIdentification139 | 169 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}PostalAddress1 | 175 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}SubscriptionBulkOrderConfirmationCancellationInstructionV03 | 187 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.049.001.03}YesNoIndicator | 199 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| choice | 2 |
| complexType | 14 |
| element | 49 |
| enumeration | 28 |
| maxLength | 5 |
| minLength | 5 |
| pattern | 5 |
| restriction | 13 |
| schema | 1 |
| sequence | 12 |
| simpleType | 13 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/4a3338243e7abc9ebebe4451.md) · [Message](index.md)
