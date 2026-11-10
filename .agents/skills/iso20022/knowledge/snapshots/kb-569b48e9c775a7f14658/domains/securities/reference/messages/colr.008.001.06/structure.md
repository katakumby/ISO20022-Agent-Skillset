---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "colr.008.001.06"
message_family: "colr.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.008.001.06"
source_ids: ["src-000070"]
source_editions: []
---

# colr.008.001.06 structure

[src-000070](../../../../../raw-input/collateral_management_collateral_management/colr.008.001.06.xsd); `urn:iso:std:iso:20022:tech:xsd:colr.008.001.06`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:colr.008.001.06 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}AnyBICDec2014Identifier | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}BlockChainAddressWallet5 | 22 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CashCollateralResponse3 | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CollateralAccount3 | 39 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CollateralAccountIdentificationType3Choice | 46 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CollateralAccountType1Code | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CollateralProposalResponse1Code | 61 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CollateralProposalResponse4 | 67 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CollateralProposalResponse4Choice | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CollateralProposalResponseType4 | 79 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CollateralProposalResponseV06 | 86 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CollateralResponse3 | 94 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}CountryCode | 101 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}DateAndDateTime2Choice | 106 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Document | 112 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}ExposureType11Code | 117 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}ExternalAccountIdentification1Code | 157 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}GenericAccountIdentification1 | 163 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}GenericIdentification36 | 170 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}IBAN2007Identifier | 177 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}ISODate | 182 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}ISODateTime | 185 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Max140Text | 188 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Max16Text | 194 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Max34Text | 200 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Max350Text | 206 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Max35Text | 212 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Max70Text | 218 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}NameAndAddress6 | 224 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Obligation9 | 230 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}OtherCollateralResponse3 | 242 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}PartyIdentification178Choice | 251 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}PostalAddress2 | 258 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}RejectionReason68Code | 267 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}SecuritiesCollateralResponse2 | 279 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}Status4Code | 288 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}SupplementaryData1 | 294 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.008.001.06}SupplementaryDataEnvelope1 | 300 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 6 |
| complexType | 23 |
| element | 72 |
| enumeration | 53 |
| maxLength | 7 |
| minLength | 7 |
| pattern | 3 |
| restriction | 17 |
| schema | 1 |
| sequence | 17 |
| simpleType | 17 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
