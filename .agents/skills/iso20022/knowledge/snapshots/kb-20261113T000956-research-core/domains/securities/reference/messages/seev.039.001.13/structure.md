---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.039.001.13"
message_family: "seev.039"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.039.001.13"
source_ids: ["src-000090"]
source_editions: ["2025-2026"]
---

# seev.039.001.13 structure

[src-000090](../../../../../raw-input/corporate_actions/seev.039.001.13.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.039.001.13`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.039.001.13 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}AccountIdentification10 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}AccountIdentification69 | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}AccountIdentification73Choice | 18 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}AdditionalBusinessProcess8Code | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}AdditionalBusinessProcessFormat15Choice | 32 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}AddressType2Code | 38 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}AnyBICDec2014Identifier | 48 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateAction72 | 53 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionCancellation3 | 61 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionCancellationAdviceV13 | 68 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionCancellationReason1Code | 87 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionDate86 | 93 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionEventStage4Code | 99 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionEventStageFormat14Choice | 106 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionEventStatus1 | 112 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionEventType107Choice | 118 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionEventType35Code | 124 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionGeneralInformation174 | 196 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionMandatoryVoluntary1Code | 206 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CorporateActionMandatoryVoluntary3Choice | 213 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}CountryCode | 219 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}DTI2024Identifier | 224 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}DateCode19Choice | 229 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}DateFormat30Choice | 235 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}DateType8Code | 241 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Document | 247 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}EventCompletenessStatus1Code | 252 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}EventConfirmationStatus1Code | 258 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Exact4AlphaNumericText | 264 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}ExternalFinancialInstrumentIdentificationType1Code | 269 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}GenericIdentification30 | 275 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}GenericIdentification36 | 282 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}GenericIdentification78 | 289 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}ISINOct2015Identifier | 295 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}ISODate | 300 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}IdentificationSource3Choice | 303 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}LotteryType1Code | 309 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}LotteryTypeFormat4Choice | 315 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Max140Text | 321 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Max16Text | 327 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Max350Text | 333 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Max35Text | 339 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Max70Text | 345 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}Max8000Text | 351 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}NameAndAddress5 | 357 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}OtherIdentification1 | 363 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}PartyIdentification120Choice | 370 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}PartyIdentification127Choice | 377 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}PostalAddress1 | 383 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}SafekeepingAccountIdentification1Code | 395 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}SafekeepingPlace1Code | 400 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}SafekeepingPlace2Code | 408 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}SafekeepingPlaceFormat42Choice | 414 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}SafekeepingPlaceTypeAndIdentification1 | 423 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}SafekeepingPlaceTypeAndText6 | 429 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}SecurityIdentification19 | 435 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}SupplementaryData1 | 442 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.039.001.13}SupplementaryDataEnvelope1 | 448 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 12 |
| complexType | 32 |
| element | 97 |
| enumeration | 101 |
| maxLength | 7 |
| minLength | 7 |
| pattern | 5 |
| restriction | 26 |
| schema | 1 |
| sequence | 20 |
| simpleType | 26 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/17be5d35e311c32ca456d2e0.md) · [Message](index.md)
