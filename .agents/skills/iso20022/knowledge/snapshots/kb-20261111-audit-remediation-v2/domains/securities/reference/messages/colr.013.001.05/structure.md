---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "colr.013.001.05"
message_family: "colr.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.013.001.05"
source_ids: ["src-000075"]
source_editions: []
---

# colr.013.001.05 structure

[src-000075](../../../../../raw-input/collateral_management_collateral_management/colr.013.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:colr.013.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:colr.013.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Agreement4 | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}AgreementFramework1Choice | 33 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}AgreementFramework1Code | 39 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}AnyBICDec2014Identifier | 48 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}BlockChainAddressWallet5 | 53 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}CalculationMethod1Code | 60 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}CollateralAccount3 | 66 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}CollateralAccountIdentificationType3Choice | 73 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}CollateralAccountType1Code | 79 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}CollateralBalance1 | 88 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}CollateralPurpose1Choice | 94 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}CollateralPurpose1Code | 100 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}CountryCode | 106 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}DateAndDateTime2Choice | 111 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}DatePeriod2 | 117 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Document | 123 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Exact4AlphaNumericText | 128 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}ExposureType11Code | 133 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Frequency1Code | 173 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}GenericIdentification30 | 185 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}GenericIdentification36 | 192 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}ISODate | 199 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}ISODateTime | 202 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}InterestAmount4 | 205 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}InterestComputationMethod2Code | 225 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}InterestMethod1Code | 244 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}InterestPaymentRequestV05 | 250 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}InterestRate1Choice | 261 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}InterestRequestSequence1Code | 267 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}InterestResult1 | 273 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Max140Text | 283 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Max16Text | 289 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Max210Text | 295 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Max350Text | 301 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Max35Text | 307 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Max70Text | 313 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}NameAndAddress6 | 319 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Number | 325 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Obligation9 | 331 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}PartyIdentification178Choice | 343 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}PercentageRate | 350 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}PostalAddress2 | 356 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}Reference20 | 365 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}SupplementaryData1 | 371 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}SupplementaryDataEnvelope1 | 377 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}VariableInterest1Rate | 382 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.013.001.05}YesNoIndicator | 388 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 6 |
| complexType | 25 |
| element | 86 |
| enumeration | 77 |
| extension | 1 |
| fractionDigits | 3 |
| maxLength | 6 |
| minInclusive | 1 |
| minLength | 6 |
| pattern | 4 |
| restriction | 25 |
| schema | 1 |
| sequence | 18 |
| simpleContent | 1 |
| simpleType | 25 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
