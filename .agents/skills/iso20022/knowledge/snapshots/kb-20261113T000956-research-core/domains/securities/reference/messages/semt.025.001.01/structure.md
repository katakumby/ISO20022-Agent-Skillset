---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.025.001.01"
message_family: "semt.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.025.001.01"
source_ids: ["src-000308"]
source_editions: ["march-2026"]
---

# semt.025.001.01 structure

[src-000308](../../../../../raw-input/target2securities_t2s/semt.025.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.025.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.025.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}AlternatePartyIdentification7 | 15 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}AnyBICDec2014Identifier | 22 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}CountryCode | 27 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}DateAndDateTime2Choice | 32 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}DateAndPeriod3Choice | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}DateTimePeriod1 | 44 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Document | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Exact4AlphaNumericText | 55 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}ExternalFinancialInstrumentIdentificationType1Code | 60 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}ExternalSecuritiesStatementType1Code | 66 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}GenericIdentification30 | 72 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}GenericIdentification36 | 79 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}ISINOct2015Identifier | 86 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}ISODate | 91 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}ISODateTime | 94 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}IdentificationSource3Choice | 97 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}IdentificationType42Choice | 103 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}LEIIdentifier | 109 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Max140Text | 114 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Max16Text | 120 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Max350Text | 126 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Max35Text | 132 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Max70Text | 138 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}NameAndAddress5 | 144 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}OtherIdentification1 | 150 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}OtherParties46 | 157 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}PartyIdentification120Choice | 162 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}PartyIdentification136 | 169 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}PartyIdentificationAndAccount197 | 175 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}PartyTextInformation1 | 187 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Period2 | 194 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Period7Choice | 200 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}PositionSearchCriteria4 | 206 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}PostalAddress1 | 218 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}SecuritiesAccount19 | 230 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}SecuritiesAccount2Choice | 237 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}SecuritiesAccountPositionQueryV01 | 243 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}SecuritiesAccountRange2 | 250 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}SecuritiesBalanceType13Code | 256 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}SecuritiesBalanceType7Choice | 273 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}SecurityIdentification19 | 279 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}Statement89 | 286 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}StatementType7Choice | 293 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}SupplementaryData1 | 299 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}SupplementaryDataEnvelope1 | 305 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}TrueFalseIndicator | 310 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.025.001.01}TypeOfIdentification1Code | 313 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 9 |
| complexType | 30 |
| element | 85 |
| enumeration | 26 |
| maxLength | 7 |
| minLength | 7 |
| pattern | 5 |
| restriction | 18 |
| schema | 1 |
| sequence | 21 |
| simpleType | 18 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/30ef90c31c3a9796592e47d8.md) · [Message](index.md)
