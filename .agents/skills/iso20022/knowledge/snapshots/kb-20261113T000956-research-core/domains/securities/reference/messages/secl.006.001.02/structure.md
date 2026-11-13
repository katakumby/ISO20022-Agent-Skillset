---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "secl.006.001.02"
message_family: "secl.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.006.001.02"
source_ids: ["src-000060"]
source_editions: ["2025-2026"]
---

# secl.006.001.02 structure

[src-000060](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/secl.006.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:secl.006.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:secl.006.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}AccountSchemeName1Choice | 13 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ActiveCurrencyAndAmount_SimpleType | 21 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ActiveCurrencyAndAmount | 28 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ActiveCurrencyCode | 35 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ActiveOrHistoricCurrencyAndAmount_SimpleType | 40 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ActiveOrHistoricCurrencyAndAmount | 47 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ActiveOrHistoricCurrencyCode | 54 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}AlternatePartyIdentification4 | 59 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}AmountAndDirection21 | 66 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}AnyBICIdentifier | 72 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ClearingAccountType1Code | 77 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Collateral3 | 84 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}CollateralType2Code | 91 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Contribution1 | 97 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}CountryCode | 105 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}CreditDebitCode | 110 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}CurrencyCode | 116 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}DateAndDateTimeChoice | 121 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}DefaultFund1 | 129 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}DefaultFundContributionReportV02 | 137 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}DefaultFundReport1 | 145 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Document | 152 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}EventFrequency6Code | 157 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Exact4AlphaNumericText | 164 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ExternalAccountIdentification1Code | 169 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}GenericAccountIdentification1 | 175 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}GenericIdentification29 | 182 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}GenericIdentification30 | 189 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}IBAN2007Identifier | 196 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ISODate | 201 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ISODateTime | 204 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}IdentificationType6Choice | 207 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Max140Text | 215 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Max16Text | 221 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Max34Text | 227 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Max350Text | 233 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Max35Text | 239 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}Max70Text | 245 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}NameAndAddress6 | 251 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}PartyIdentification33Choice | 257 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}PartyIdentification35Choice | 266 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}PartyIdentificationAndAccount31 | 274 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}PartyTextInformation1 | 282 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}PostalAddress2 | 289 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}ReportParameters2 | 298 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}SecuritiesAccount18 | 307 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}SupplementaryData1 | 314 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}SupplementaryDataEnvelope1 | 320 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.006.001.02}TypeOfIdentification1Code | 325 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 6 |
| complexType | 27 |
| element | 71 |
| enumeration | 17 |
| extension | 2 |
| fractionDigits | 2 |
| maxLength | 7 |
| minInclusive | 2 |
| minLength | 7 |
| pattern | 7 |
| restriction | 23 |
| schema | 1 |
| sequence | 25 |
| simpleContent | 2 |
| simpleType | 23 |
| totalDigits | 2 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/85e857844d2b29ad267691a7.md) · [Message](index.md)
