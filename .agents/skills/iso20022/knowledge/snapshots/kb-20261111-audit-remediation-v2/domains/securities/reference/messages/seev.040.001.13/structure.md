---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.040.001.13"
message_family: "seev.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.040.001.13"
source_ids: ["src-000091"]
source_editions: ["2025-2026"]
---

# seev.040.001.13 structure

[src-000091](../../../../../raw-input/corporate_actions/seev.040.001.13.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.040.001.13`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.040.001.13 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}AccountIdentification69 | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}AnyBICDec2014Identifier | 13 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}CorporateActionEventType112Choice | 18 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}CorporateActionEventType40Code | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}CorporateActionGeneralInformation183 | 93 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}CorporateActionInstructionCancellationRequestV13 | 101 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}CorporateActionNarrative10 | 113 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}CorporateActionOption16Code | 119 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}CorporateActionOption200 | 149 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}CorporateActionOption40Choice | 156 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}CountryCode | 162 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}DTI2024Identifier | 167 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}DecimalNumber | 172 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Document | 178 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}DocumentIdentification31 | 183 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Exact3NumericText | 189 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Exact4AlphaNumericText | 194 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}ExternalFinancialInstrumentIdentificationType1Code | 199 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}FinancialInstrumentQuantity33Choice | 205 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}GenericIdentification30 | 213 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}GenericIdentification36 | 220 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}GenericIdentification78 | 227 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}ISINOct2015Identifier | 233 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}ISODate | 238 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}IdentificationSource3Choice | 241 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}ImpliedCurrencyAndAmount | 247 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Max140Text | 254 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Max15Text | 260 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Max16Text | 266 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Max30DecimalNumber | 272 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Max350Text | 278 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Max35Text | 284 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}OptionNumber1Choice | 290 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}OptionNumber1Code | 296 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}OriginalAndCurrentQuantities1 | 301 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}OtherIdentification1 | 307 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}PartyIdentification127Choice | 314 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}ProcessingPosition3Code | 320 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}ProcessingPosition7Choice | 328 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}ProtectInstruction3 | 334 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}ProtectTransactionType3Code | 341 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Quantity1Code | 346 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}Quantity52Choice | 351 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}SafekeepingPlace1Code | 358 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}SafekeepingPlace2Code | 366 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}SafekeepingPlaceFormat42Choice | 372 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}SafekeepingPlaceTypeAndIdentification1 | 381 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}SafekeepingPlaceTypeAndText6 | 387 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}SecurityIdentification19 | 393 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}SupplementaryData1 | 400 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}SupplementaryDataEnvelope1 | 406 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.040.001.13}YesNoIndicator | 411 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 9 |
| complexType | 27 |
| element | 74 |
| enumeration | 104 |
| fractionDigits | 3 |
| maxLength | 6 |
| minInclusive | 1 |
| minLength | 6 |
| pattern | 6 |
| restriction | 25 |
| schema | 1 |
| sequence | 18 |
| simpleType | 25 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
