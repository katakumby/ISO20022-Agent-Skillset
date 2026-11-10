---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "colr.011.001.05"
message_family: "colr.011"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.011.001.05"
source_ids: ["src-000073"]
source_editions: []
---

# colr.011.001.05 structure

[src-000073](../../../../../raw-input/collateral_management_collateral_management/colr.011.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:colr.011.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:colr.011.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Agreement4 | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}AgreementFramework1Choice | 33 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}AgreementFramework1Code | 39 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}AnyBICDec2014Identifier | 48 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}BlockChainAddressWallet5 | 53 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}CollateralAccount3 | 60 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}CollateralAccountIdentificationType3Choice | 67 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}CollateralAccountType1Code | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}CollateralSubstitutionResponse1 | 82 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}CollateralSubstitutionResponse3 | 88 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}CollateralSubstitutionResponseV05 | 96 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}CountryCode | 105 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}DateAndDateTime2Choice | 110 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Document | 116 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Exact4AlphaNumericText | 121 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}ExposureType11Code | 126 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}GenericIdentification30 | 166 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}GenericIdentification36 | 173 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}ISODate | 180 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}ISODateTime | 183 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Max140Text | 186 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Max16Text | 192 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Max350Text | 198 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Max35Text | 204 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Max70Text | 210 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}NameAndAddress6 | 216 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Obligation9 | 222 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}PartyIdentification178Choice | 234 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}PostalAddress2 | 241 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}RejectionReason68Code | 250 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}Status4Code | 262 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}SubstitutionResponse2 | 268 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}SupplementaryData1 | 275 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.011.001.05}SupplementaryDataEnvelope1 | 281 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 4 |
| complexType | 20 |
| element | 59 |
| enumeration | 56 |
| extension | 1 |
| fractionDigits | 1 |
| maxLength | 5 |
| minInclusive | 1 |
| minLength | 5 |
| pattern | 4 |
| restriction | 17 |
| schema | 1 |
| sequence | 15 |
| simpleContent | 1 |
| simpleType | 17 |
| totalDigits | 1 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
