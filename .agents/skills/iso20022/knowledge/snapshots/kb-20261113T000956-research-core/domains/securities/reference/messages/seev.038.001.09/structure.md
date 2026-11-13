---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.038.001.09"
message_family: "seev.038"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.038.001.09"
source_ids: ["src-000089"]
source_editions: ["2025-2026"]
---

# seev.038.001.09 structure

[src-000089](../../../../../raw-input/corporate_actions/seev.038.001.09.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.038.001.09`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.038.001.09 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}AccountIdentification10 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}AccountIdentification71 | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}AccountIdentification72Choice | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}AnyBICDec2014Identifier | 25 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}BalanceFormat11Choice | 30 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}CorporateActionGeneralInformation92 | 37 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}CorporateActionNarrative1Code | 44 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}CorporateActionNarrative3Choice | 54 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}CorporateActionNarrativeV09 | 60 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}CountryCode | 69 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}DTI2024Identifier | 74 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}DecimalNumber | 79 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Document | 85 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Exact4AlphaNumericText | 90 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}ExternalFinancialInstrumentIdentificationType1Code | 95 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}FinancialInstrumentQuantity33Choice | 101 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}GenericIdentification30 | 109 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}GenericIdentification36 | 116 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}GenericIdentification78 | 123 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}ISINOct2015Identifier | 129 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}IdentificationSource3Choice | 134 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}ImpliedCurrencyAndAmount | 140 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Max140Text | 147 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Max16Text | 153 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Max30DecimalNumber | 159 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Max350Text | 165 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Max35Text | 171 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Max8000Text | 177 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}OtherIdentification1 | 183 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}PartyIdentification127Choice | 190 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}ProprietaryQuantity8 | 196 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}Quantity48Choice | 204 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SafekeepingAccountIdentification1Code | 210 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SafekeepingPlace1Code | 215 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SafekeepingPlace2Code | 223 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SafekeepingPlaceFormat42Choice | 229 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SafekeepingPlaceTypeAndIdentification1 | 238 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SafekeepingPlaceTypeAndText6 | 244 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SecurityIdentification19 | 250 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}ShortLong1Code | 257 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SignedQuantityFormat10 | 263 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SignedQuantityFormat11 | 269 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SupplementaryData1 | 275 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.038.001.09}SupplementaryDataEnvelope1 | 281 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 8 |
| complexType | 25 |
| element | 66 |
| enumeration | 15 |
| fractionDigits | 3 |
| maxLength | 6 |
| minInclusive | 1 |
| minLength | 6 |
| pattern | 5 |
| restriction | 19 |
| schema | 1 |
| sequence | 17 |
| simpleType | 19 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/254f1525eebe5bb847e23494.md) · [Message](index.md)
