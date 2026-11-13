---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.034.001.16"
message_family: "seev.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.034.001.16"
source_ids: ["src-000085"]
source_editions: ["2025-2026"]
---

# seev.034.001.16 structure

[src-000085](../../../../../raw-input/corporate_actions/seev.034.001.16.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.034.001.16`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.034.001.16 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}AcceptedReason10Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}AcceptedStatus2 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}AcceptedStatus8Choice | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}AcceptedStatusReason9 | 23 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}AcknowledgementReason7Code | 29 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ActiveCurrencyAndAmount_SimpleType | 35 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ActiveCurrencyAndAmount | 42 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ActiveCurrencyCode | 49 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}AnyBICDec2014Identifier | 54 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}BlockChainAddressWallet3 | 59 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CancelledReason8Choice | 66 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CancelledStatus12Choice | 72 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CancelledStatus5 | 78 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CancelledStatusReason11 | 84 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CancelledStatusReason6Code | 90 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CashAccountIdentification9Choice | 99 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CorporateActionEventType112Choice | 106 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CorporateActionEventType40Code | 112 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CorporateActionGeneralInformation197 | 181 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CorporateActionInstructionStatusAdviceV16 | 190 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CorporateActionNarrative10 | 202 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CorporateActionOption17Code | 208 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CorporateActionOption238 | 237 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CorporateActionOption41Choice | 257 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}CountryCode | 263 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}DTI2024Identifier | 268 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}DecimalNumber | 273 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Document | 279 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}DocumentIdentification33 | 284 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}DocumentIdentification3Choice | 290 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}DocumentIdentification9 | 296 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}DocumentNumber5Choice | 301 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Exact3NumericText | 308 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Exact4AlphaNumericText | 313 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ExternalFinancialInstrumentIdentificationType1Code | 318 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}FinancialInstrumentQuantity18Choice | 324 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}FinancialInstrumentQuantity33Choice | 330 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ForwardedStatus1 | 338 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}GenericIdentification30 | 344 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}GenericIdentification36 | 351 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}GenericIdentification78 | 358 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}IBAN2007Identifier | 364 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ISINOct2015Identifier | 369 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ISO20022MessageIdentificationText | 374 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ISODate | 379 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}IdentificationSource3Choice | 382 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ImpliedCurrencyAndAmount | 388 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}InstructionProcessingStatus60Choice | 395 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Max140Text | 409 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Max15Text | 415 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Max16Text | 421 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Max210Text | 427 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Max30DecimalNumber | 433 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Max34Text | 439 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Max350Text | 445 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Max35Text | 451 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Max70Text | 457 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}NoReasonCode | 463 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}NoSpecifiedReason1 | 468 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}OptionFeatures12Code | 473 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}OptionFeaturesFormat25Choice | 478 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}OptionNumber1Choice | 484 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}OptionNumber1Code | 490 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}OriginalAndCurrentQuantities1 | 495 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}OtherIdentification1 | 501 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}PartyIdentification127Choice | 508 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}PendingReason37Code | 514 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}PendingReason76Choice | 539 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}PendingStatus3 | 545 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}PendingStatus80Choice | 551 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}PendingStatusReason33 | 557 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ProprietaryQuantity8 | 563 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ProprietaryReason4 | 571 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ProprietaryStatusAndReason6 | 577 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ProtectInstruction2 | 583 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ProtectInstructionStatus3Code | 593 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ProtectTransactionType2Code | 600 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Quantity48Choice | 607 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}Quantity51Choice | 613 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ReceivedByIssuerOrOfferorStatus1 | 619 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}RejectedReason68Choice | 625 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}RejectedStatus15 | 631 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}RejectedStatus64Choice | 637 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}RejectedStatusReason63 | 643 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}RejectionReason89Code | 649 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ReturnedReason2Choice | 700 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ReturnedStatus1 | 706 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ReturnedStatus1Code | 712 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ReturnedStatus2Choice | 718 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ReturnedStatusReason2 | 724 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}SafekeepingPlace1Code | 730 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}SafekeepingPlace2Code | 738 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}SafekeepingPlaceFormat42Choice | 744 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}SafekeepingPlaceTypeAndIdentification1 | 753 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}SafekeepingPlaceTypeAndText6 | 759 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}SecurityIdentification19 | 765 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}ShortLong1Code | 772 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}SignedQuantityFormat11 | 778 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}SupplementaryData1 | 784 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}SupplementaryDataEnvelope1 | 790 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.034.001.16}YesNoIndicator | 795 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 25 |
| complexType | 62 |
| element | 167 |
| enumeration | 184 |
| extension | 1 |
| fractionDigits | 4 |
| maxLength | 9 |
| minInclusive | 2 |
| minLength | 9 |
| pattern | 9 |
| restriction | 39 |
| schema | 1 |
| sequence | 36 |
| simpleContent | 1 |
| simpleType | 39 |
| totalDigits | 4 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/b5c87e05eb0c59827c4a8f03.md) · [Message](index.md)
