---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "colr.003.001.05"
message_family: "colr.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.003.001.05"
source_ids: ["src-000065"]
source_editions: []
---

# colr.003.001.05 structure

[src-000065](../../../../../raw-input/collateral_management_collateral_management/colr.003.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:colr.003.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:colr.003.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}AggregatedIndependentAmount1 | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Agreement4 | 32 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}AgreementFramework1Choice | 41 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}AgreementFramework1Code | 47 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}AnyBICDec2014Identifier | 56 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}BlockChainAddressWallet5 | 61 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Collateral1 | 68 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}CollateralAccount3 | 74 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}CollateralAccountIdentificationType3Choice | 81 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}CollateralAccountType1Code | 87 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}CollateralBalance1Choice | 96 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}CollateralMovement9 | 103 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}CollateralType1Code | 109 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}CountryCode | 117 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}DateAndDateTime2Choice | 122 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Document | 128 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Exact4AlphaNumericText | 133 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ExpectedCollateral2 | 138 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ExpectedCollateral2Choice | 144 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ExpectedCollateralMovement2 | 150 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ExposureConventionType1Code | 156 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ExposureType11Code | 162 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}GenericIdentification30 | 202 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}GenericIdentification36 | 209 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ISODate | 216 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ISODateTime | 219 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}IndependentAmount1 | 222 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}IndependentAmount2 | 228 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}IndependentAmountConventionType1Code | 235 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Margin1 | 242 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginCall1 | 248 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginCall3 | 259 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginCallRequestV05 | 272 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginCallResult2 | 288 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginCallResult2Choice | 294 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginCallResult3 | 301 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginCollateral1 | 307 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginRequirement1 | 317 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginRequirement1Choice | 323 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}MarginTerms1Choice | 329 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Max140Text | 335 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Max16Text | 341 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Max210Text | 347 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Max350Text | 353 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Max35Text | 359 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Max70Text | 365 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}NameAndAddress6 | 371 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Obligation9 | 377 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}PartyIdentification178Choice | 389 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}PostalAddress2 | 396 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Requirement1 | 405 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}Result1 | 411 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}RoundingMethod1Code | 418 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}SegregatedIndependentAmountMargin1 | 426 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}SupplementaryData1 | 433 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}SupplementaryDataEnvelope1 | 439 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}ThresholdType1Code | 444 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.003.001.05}VariationMargin1 | 450 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 9 |
| complexType | 40 |
| element | 129 |
| enumeration | 61 |
| extension | 1 |
| fractionDigits | 1 |
| maxLength | 6 |
| minInclusive | 1 |
| minLength | 6 |
| pattern | 4 |
| restriction | 21 |
| schema | 1 |
| sequence | 30 |
| simpleContent | 1 |
| simpleType | 21 |
| totalDigits | 1 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/1b1e61955c2e00dd6d4949f8.md) · [Message](index.md)
