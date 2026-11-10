---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.024.001.01"
message_family: "reda.024"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.024.001.01"
source_ids: ["src-000279"]
source_editions: ["may-2025"]
---

# reda.024.001.01 structure

[src-000279](../../../../../raw-input/target2securities_t2s/reda.024.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.024.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.024.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ActiveOrHistoricCurrencyAndAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ActiveOrHistoricCurrencyAndAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ActiveOrHistoricCurrencyCode | 38 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}AddressType2Code | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}AmountOrCoefficientPrice2Choice | 53 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}AnyBICDec2014Identifier | 60 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}BaseOneRate | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}CollateralValue5 | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}CollateralValueCreationRequestV01 | 86 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}CountryCode | 94 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}DecimalNumber | 99 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}Document | 105 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ExternalFinancialInstrumentIdentificationType1Code | 110 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ForeignExchangeTerms23 | 116 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}GenericIdentification36 | 124 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ISINOct2015Identifier | 131 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ISODate | 136 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ISODateTime | 139 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}IdentificationSource3Choice | 142 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}ImpliedCurrencyAndAmount | 148 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}LEIIdentifier | 155 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}Max140Text | 160 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}Max16Text | 166 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}Max350Text | 172 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}Max35Text | 178 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}Max70Text | 184 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}MessageHeader1 | 190 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}NameAndAddress5 | 196 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}OtherIdentification1 | 202 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}PartyIdentification120Choice | 209 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}PartyIdentification136 | 216 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}PercentageRate | 222 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}PostalAddress1 | 228 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}PriceRateOrAmount6Choice | 240 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}SecurityIdentification19 | 247 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}SupplementaryData1 | 254 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}SupplementaryDataEnvelope1 | 260 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}SystemPartyIdentification2Choice | 265 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.024.001.01}SystemPartyIdentification8 | 271 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 5 |
| complexType | 21 |
| element | 61 |
| enumeration | 6 |
| extension | 2 |
| fractionDigits | 6 |
| maxLength | 6 |
| minInclusive | 3 |
| minLength | 6 |
| pattern | 6 |
| restriction | 21 |
| schema | 1 |
| sequence | 14 |
| simpleContent | 2 |
| simpleType | 21 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
