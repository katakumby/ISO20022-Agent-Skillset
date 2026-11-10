---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.018.001.05"
message_family: "setr.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.018.001.05"
source_ids: ["src-000154"]
source_editions: ["2025-2026"]
---

# setr.018.001.05 structure

[src-000154](../../../../../raw-input/investment_funds/setr.018.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.018.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.018.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}AdditionalReference10 | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}AddressType2Code | 12 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}AlternateSecurityIdentification7 | 22 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}AnyBICDec2014Identifier | 28 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}BelgianIdentifier | 33 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}BlockChainAddressWallet3 | 36 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Bloomberg2Identifier | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}CUSIPIdentifier | 48 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}ConsolidatedTapeAssociationIdentifier | 51 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}CountryCode | 57 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}DTI2024Identifier | 62 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}DateFormat42Choice | 67 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}DistributionPolicy1Code | 73 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Document | 79 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}DutchIdentifier | 84 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}EuroclearClearstreamIdentifier | 87 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Exact4AlphaNumericText | 93 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Extension1 | 98 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}FinancialInstrument107 | 104 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}FormOfSecurity1Code | 117 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}GenericIdentification1 | 123 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}GenericIdentification30 | 130 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}ISINOct2015Identifier | 137 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}ISODate | 142 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}ISODateTime | 145 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}ISOYearMonth | 148 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}IdentificationSource1Choice | 151 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}InvestmentAccount81 | 157 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}InvestmentFundOrder12 | 169 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}LEIIdentifier | 181 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Max140Text | 186 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Max16Text | 192 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Max350Text | 198 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Max35Text | 204 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Max70Text | 210 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}MessageAndBusinessReference15 | 216 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}MessageIdentification1 | 223 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}NameAndAddress5 | 229 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}OrderOriginatorEligibility1Code | 235 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}PartyIdentification125Choice | 242 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}PartyIdentification139 | 249 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}PostalAddress1 | 255 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}QUICKIdentifier | 267 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}RICIdentifier | 270 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}References87Choice | 276 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}RequestForOrderStatusReportV05 | 282 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}SEDOLIdentifier | 289 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}SecurityIdentification46Choice | 292 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}Series1 | 312 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}SicovamIdentifier | 318 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}SubAccount6 | 321 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}TickerIdentifier | 329 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}ValorenIdentifier | 335 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.018.001.05}WertpapierIdentifier | 338 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| choice | 5 |
| complexType | 23 |
| element | 94 |
| enumeration | 13 |
| maxLength | 9 |
| minLength | 9 |
| pattern | 7 |
| restriction | 31 |
| schema | 1 |
| sequence | 18 |
| simpleType | 31 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
