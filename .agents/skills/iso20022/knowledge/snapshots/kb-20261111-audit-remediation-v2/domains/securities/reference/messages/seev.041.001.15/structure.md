---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.041.001.15"
message_family: "seev.041"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.041.001.15"
source_ids: ["src-000092"]
source_editions: ["2025-2026"]
---

# seev.041.001.15 structure

[src-000092](../../../../../raw-input/corporate_actions/seev.041.001.15.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.041.001.15`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.041.001.15 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}AnyBICDec2014Identifier | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}BlockChainAddressWallet3 | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CancelledReason9Choice | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CancelledStatus11Choice | 42 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CancelledStatusReason12 | 48 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CancelledStatusReason5Code | 54 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CashAccountIdentification9Choice | 60 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CorporateActionEventType112Choice | 67 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CorporateActionEventType40Code | 73 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CorporateActionGeneralInformation182 | 142 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CorporateActionInstructionCancellationRequestStatusAdviceV15 | 150 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CorporateActionNarrative10 | 162 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CorporateActionOption17Code | 168 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CorporateActionOption239 | 197 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CorporateActionOption41Choice | 216 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}CountryCode | 222 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}DTI2024Identifier | 227 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}DecimalNumber | 232 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Document | 238 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}DocumentIdentification33 | 243 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}DocumentIdentification3Choice | 249 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}DocumentIdentification9 | 255 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}DocumentNumber5Choice | 260 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Exact3NumericText | 267 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Exact4AlphaNumericText | 272 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ExternalFinancialInstrumentIdentificationType1Code | 277 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}FinancialInstrumentQuantity18Choice | 283 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}FinancialInstrumentQuantity33Choice | 289 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}GenericIdentification30 | 297 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}GenericIdentification36 | 304 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}GenericIdentification78 | 311 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}IBAN2007Identifier | 317 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ISINOct2015Identifier | 322 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ISO20022MessageIdentificationText | 327 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ISODate | 332 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}IdentificationSource3Choice | 335 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ImpliedCurrencyAndAmount | 341 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}InstructionCancellationRequestStatus21Choice | 348 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Max140Text | 357 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Max15Text | 363 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Max16Text | 369 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Max210Text | 375 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Max30DecimalNumber | 381 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Max34Text | 387 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Max350Text | 393 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Max35Text | 399 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Max70Text | 405 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}NoReasonCode | 411 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}NoSpecifiedReason1 | 416 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}OptionFeatures12Code | 421 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}OptionFeaturesFormat25Choice | 426 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}OptionNumber1Choice | 432 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}OptionNumber1Code | 438 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}OriginalAndCurrentQuantities1 | 443 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}OtherIdentification1 | 449 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}PartyIdentification127Choice | 456 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}PendingCancellationReason10Choice | 462 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}PendingCancellationReason9Code | 468 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}PendingCancellationStatus18Choice | 478 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}PendingCancellationStatusReason13 | 484 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ProprietaryQuantity8 | 490 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ProprietaryReason4 | 498 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ProprietaryStatusAndReason6 | 504 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ProtectInstruction4 | 510 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ProtectInstructionStatus4Code | 519 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ProtectTransactionType3Code | 524 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Quantity48Choice | 529 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}Quantity51Choice | 535 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}RejectedReason69Choice | 541 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}RejectedStatus65Choice | 547 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}RejectedStatusReason64 | 553 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}RejectionReason90Code | 559 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}SafekeepingPlace1Code | 581 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}SafekeepingPlace2Code | 589 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}SafekeepingPlaceFormat42Choice | 595 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}SafekeepingPlaceTypeAndIdentification1 | 604 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}SafekeepingPlaceTypeAndText6 | 610 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}SecurityIdentification19 | 616 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}ShortLong1Code | 623 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}SignedQuantityFormat11 | 629 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}SupplementaryData1 | 635 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.041.001.15}SupplementaryDataEnvelope1 | 641 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 21 |
| complexType | 49 |
| element | 133 |
| enumeration | 129 |
| extension | 1 |
| fractionDigits | 4 |
| maxLength | 9 |
| minInclusive | 2 |
| minLength | 9 |
| pattern | 9 |
| restriction | 36 |
| schema | 1 |
| sequence | 27 |
| simpleContent | 1 |
| simpleType | 36 |
| totalDigits | 4 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
