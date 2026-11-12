---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.057.001.03"
message_family: "setr.057"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.057.001.03"
source_ids: ["src-000160"]
source_editions: ["2025-2026"]
---

# setr.057.001.03 structure

[src-000160](../../../../../raw-input/investment_funds/setr.057.001.03.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.057.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.057.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}AdditionalReference10 | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}AddressType2Code | 12 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}AlternateSecurityIdentification7 | 22 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}AnyBICDec2014Identifier | 28 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}BelgianIdentifier | 33 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}BlockChainAddressWallet3 | 36 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Bloomberg2Identifier | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}CUSIPIdentifier | 48 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}ConfirmationRejectedReason1Choice | 51 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}ConfirmationRejectedStatus2 | 57 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}ConfirmationStatus1Choice | 63 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}ConsolidatedTapeAssociationIdentifier | 70 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}CountryCode | 76 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}DTI2024Identifier | 81 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}DateFormat42Choice | 86 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}DistributionPolicy1Code | 92 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Document | 98 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}DutchIdentifier | 103 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}EuroclearClearstreamIdentifier | 106 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Exact4AlphaNumericText | 112 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Extension1 | 117 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}FinancialInstrument107 | 123 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}FormOfSecurity1Code | 136 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}GenericIdentification1 | 142 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}GenericIdentification30 | 149 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}ISINOct2015Identifier | 156 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}ISODate | 161 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}ISODateTime | 164 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}ISOYearMonth | 167 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}IdentificationSource1Choice | 170 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}IndividualOrderConfirmationStatusAndReason3 | 176 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}InvestmentAccount81 | 189 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}LEIIdentifier | 201 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Max140Text | 206 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Max16Text | 212 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Max350Text | 218 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Max35Text | 224 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Max70Text | 230 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}MessageIdentification1 | 236 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}NameAndAddress5 | 242 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}OrderConfirmationStatus1Code | 248 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}OrderConfirmationStatusReportV03 | 256 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}OrderOriginatorEligibility1Code | 264 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}PartyIdentification125Choice | 271 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}PartyIdentification139 | 278 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}PostalAddress1 | 284 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}QUICKIdentifier | 296 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}RICIdentifier | 299 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}References64Choice | 305 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}RejectedConfirmationStatusReason1Code | 311 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}SEDOLIdentifier | 371 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}SecurityIdentification46Choice | 374 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}Series1 | 394 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}SicovamIdentifier | 400 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}SubAccount6 | 403 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}TickerIdentifier | 411 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}ValorenIdentifier | 417 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.057.001.03}WertpapierIdentifier | 420 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| choice | 7 |
| complexType | 25 |
| element | 100 |
| enumeration | 73 |
| maxLength | 9 |
| minLength | 9 |
| pattern | 7 |
| restriction | 33 |
| schema | 1 |
| sequence | 18 |
| simpleType | 33 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
