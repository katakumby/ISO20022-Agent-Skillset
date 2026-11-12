---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.022.001.08"
message_family: "sese.022"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.022.001.08"
source_ids: ["src-000213"]
source_editions: ["2025-2026"]
---

# sese.022.001.08 structure

[src-000213](../../../../../raw-input/settlement_and_reconciliation/sese.022.001.08.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.022.001.08`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.022.001.08 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}AcknowledgedAcceptedStatus24Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}AcknowledgementReason12 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}AcknowledgementReason15Choice | 17 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}AcknowledgementReason3Code | 23 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}AnyBICDec2014Identifier | 30 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}BlockChainAddressWallet3 | 35 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Document | 42 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}DocumentIdentification54 | 47 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}DocumentNumber13 | 53 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}DocumentNumber22 | 58 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}DocumentNumber5Choice | 64 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Exact3NumericText | 71 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Exact4AlphaNumericText | 76 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}GenericIdentification30 | 81 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}GenericIdentification36 | 88 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}ISO20022MessageIdentificationText | 95 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Identification32 | 100 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}LEIIdentifier | 119 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Max140Text | 124 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Max210Text | 130 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Max350Text | 136 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Max35Text | 142 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}Max70Text | 148 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}NoReasonCode | 154 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}PartyIdentification127Choice | 159 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}PartyIdentification144 | 165 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}ProcessingStatus89Choice | 171 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}ProprietaryReason4 | 178 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}ProprietaryStatusAndReason6 | 184 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}RejectionAndRepairReason39Choice | 190 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}RejectionOrRepairReason39 | 196 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}RejectionOrRepairStatus44Choice | 202 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}RejectionReason77Code | 208 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}SecuritiesAccount19 | 219 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}SecuritiesStatusOrStatementQueryStatusAdviceV08 | 226 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}StatusOrStatement14Choice | 237 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}SupplementaryData1 | 243 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}SupplementaryDataEnvelope1 | 249 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.022.001.08}UTIIdentifier | 254 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 8 |
| complexType | 25 |
| element | 71 |
| enumeration | 11 |
| maxLength | 5 |
| minLength | 5 |
| pattern | 6 |
| restriction | 14 |
| schema | 1 |
| sequence | 17 |
| simpleType | 14 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
