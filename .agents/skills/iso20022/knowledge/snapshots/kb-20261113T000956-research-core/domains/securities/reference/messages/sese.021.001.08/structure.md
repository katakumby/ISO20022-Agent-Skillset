---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.021.001.08"
message_family: "sese.021"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.021.001.08"
source_ids: ["src-000212"]
source_editions: ["2025-2026"]
---

# sese.021.001.08 structure

[src-000212](../../../../../raw-input/settlement_and_reconciliation/sese.021.001.08.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.021.001.08`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.021.001.08 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}AnyBICDec2014Identifier | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}BlockChainAddressWallet3 | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Document | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}DocumentNumber22 | 22 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}DocumentNumber5Choice | 28 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Exact3NumericText | 35 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Exact4AlphaNumericText | 40 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}GenericIdentification30 | 45 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}GenericIdentification36 | 52 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}ISO20022MessageIdentificationText | 59 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Identification32 | 64 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}LEIIdentifier | 83 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Max140Text | 88 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Max350Text | 94 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Max35Text | 100 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}Max70Text | 106 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}PartyIdentification127Choice | 112 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}PartyIdentification144 | 118 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}SecuritiesAccount22 | 124 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}SecuritiesTransactionStatusQueryV08 | 131 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}SupplementaryData1 | 140 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}SupplementaryDataEnvelope1 | 146 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.021.001.08}UTIIdentifier | 151 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 2 |
| complexType | 13 |
| element | 45 |
| maxLength | 4 |
| minLength | 4 |
| pattern | 6 |
| restriction | 10 |
| schema | 1 |
| sequence | 11 |
| simpleType | 10 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/3966768c1967797ba0663de9.md) · [Message](index.md)
