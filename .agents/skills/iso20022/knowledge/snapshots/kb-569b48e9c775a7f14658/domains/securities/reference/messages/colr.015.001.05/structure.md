---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "colr.015.001.05"
message_family: "colr.015"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.015.001.05"
source_ids: ["src-000077"]
source_editions: []
---

# colr.015.001.05 structure

[src-000077](../../../../../raw-input/collateral_management_collateral_management/colr.015.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:colr.015.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:colr.015.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}ActiveOrHistoricCurrencyAndAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}ActiveOrHistoricCurrencyAndAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}ActiveOrHistoricCurrencyCode | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Agreement4 | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}AgreementFramework1Choice | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}AgreementFramework1Code | 58 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}AmountAndDirection20 | 67 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}AnyBICDec2014Identifier | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}BlockChainAddressWallet5 | 78 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}CollateralAccount3 | 85 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}CollateralAccountIdentificationType3Choice | 92 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}CollateralAccountType1Code | 98 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}CountryCode | 107 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}CreditDebitCode | 112 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}DateAndDateTime2Choice | 118 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}DatePeriod2 | 124 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Document | 130 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Exact4AlphaNumericText | 135 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}ExposureType11Code | 140 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Frequency1Code | 180 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}GenericIdentification30 | 192 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}GenericIdentification36 | 199 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}ISODate | 206 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}ISODateTime | 209 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}InterestCalculation5 | 212 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}InterestPaymentStatementV05 | 228 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}InterestStatement5 | 239 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Max140Text | 249 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Max16Text | 255 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Max350Text | 261 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Max35Text | 267 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Max5NumericText | 273 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Max70Text | 278 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}NameAndAddress6 | 284 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Number | 290 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Obligation9 | 296 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Pagination1 | 308 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}PartyIdentification178Choice | 314 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}PercentageRate | 321 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}PostalAddress2 | 327 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}Statement85 | 336 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}SupplementaryData1 | 344 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}SupplementaryDataEnvelope1 | 350 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.015.001.05}YesNoIndicator | 355 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 4 |
| complexType | 24 |
| element | 80 |
| enumeration | 56 |
| extension | 2 |
| fractionDigits | 4 |
| maxLength | 5 |
| minInclusive | 2 |
| minLength | 5 |
| pattern | 6 |
| restriction | 23 |
| schema | 1 |
| sequence | 18 |
| simpleContent | 2 |
| simpleType | 23 |
| totalDigits | 4 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
