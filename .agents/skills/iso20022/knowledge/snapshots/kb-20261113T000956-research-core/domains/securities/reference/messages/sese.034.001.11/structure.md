---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.034.001.11"
message_family: "sese.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.034.001.11"
source_ids: ["src-000225"]
source_editions: ["2025-2026"]
---

# sese.034.001.11 structure

[src-000225](../../../../../raw-input/settlement_and_reconciliation/sese.034.001.11.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.034.001.11`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.034.001.11 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AcknowledgedAcceptedStatus21Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AcknowledgedAcceptedStatus22Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AcknowledgementReason10 | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AcknowledgementReason12Choice | 23 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AcknowledgementReason13Choice | 29 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AcknowledgementReason5Code | 35 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AcknowledgementReason9 | 48 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ActiveCurrencyAndAmount_SimpleType | 54 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ActiveCurrencyAndAmount | 61 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ActiveCurrencyCode | 68 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ActiveOrHistoricCurrencyAndAmount_SimpleType | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ActiveOrHistoricCurrencyAndAmount | 80 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ActiveOrHistoricCurrencyCode | 87 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AddressType2Code | 92 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AlternatePartyIdentification7 | 102 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AmountAndDirection21 | 109 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AmountAndDirection51 | 115 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}AnyBICDec2014Identifier | 122 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}BeneficialOwnership4Choice | 127 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}BlockChainAddressWallet3 | 133 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}BlockTrade1Code | 140 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}BlockTrade4Choice | 146 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CancellationReason12 | 152 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CancellationReason23Choice | 158 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CancellationStatus16Choice | 164 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CancelledStatusReason9Code | 170 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CashSettlementSystem3Code | 183 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CashSettlementSystem6Choice | 190 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CashSettlementSystemPlace1Choice | 196 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CentralCounterPartyEligibility4Choice | 203 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CountryCode | 209 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}CreditDebitCode | 214 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DTI2024Identifier | 220 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DateAndDateTime2Choice | 225 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DateCode18Choice | 231 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DateType3Code | 237 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DateType4Code | 242 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DateType5Code | 248 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DecimalNumber | 253 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DeliveryReceiptType2Code | 259 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DeniedReason12 | 265 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DeniedReason17Choice | 271 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DeniedReason3Code | 277 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DeniedStatus17Choice | 286 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}DigitalPaymentSettlement2 | 292 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Document | 299 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Exact4AlphaNumericText | 304 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ExternalFinancialInstrumentIdentificationType1Code | 309 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}FailingReason2Code | 315 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}FailingReason8 | 381 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}FailingReason8Choice | 387 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}FailingStatus10Choice | 393 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}FinancialInstrumentQuantity33Choice | 399 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}GenericIdentification30 | 407 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}GenericIdentification36 | 414 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}GenericIdentification78 | 421 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ISINOct2015Identifier | 427 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ISODate | 432 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ISODateTime | 435 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}IdentificationSource3Choice | 438 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}IdentificationType42Choice | 444 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ImpliedCurrencyAndAmount | 450 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}LEIIdentifier | 457 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}MICIdentifier | 462 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}MarketClientSide1Code | 467 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}MarketClientSide6Choice | 473 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}MarketIdentification1Choice | 479 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}MarketIdentification84 | 485 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}MarketType2Code | 491 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}MarketType8Choice | 500 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}MatchingStatus26Choice | 506 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Max140Text | 513 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Max16Text | 519 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Max210Text | 525 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Max30DecimalNumber | 531 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Max350Text | 537 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Max35Text | 543 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Max70Text | 549 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Max8Text | 555 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}NameAndAddress5 | 561 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}NettingEligibility4Choice | 567 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}NoReasonCode | 573 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}OriginalAndCurrentQuantities1 | 578 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}OtherIdentification1 | 584 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}OwnershipLegalRestrictions1Code | 591 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PartyIdentification120Choice | 598 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PartyIdentification127Choice | 605 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PartyIdentification134Choice | 611 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PartyIdentification144 | 619 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PartyIdentification149 | 625 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PartyIdentification257Choice | 631 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PartyIdentification315 | 639 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PartyIdentificationAndAccount199 | 649 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PartyTextInformation1 | 661 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingProcessingReason18 | 668 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingProcessingReason20Choice | 674 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingProcessingReason6Code | 680 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingProcessingStatus21Choice | 703 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingReason18 | 709 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingReason1Code | 715 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingReason31Choice | 775 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingReason32Code | 781 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingReason35 | 791 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingReason77Choice | 797 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingStatus40Choice | 803 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PendingStatus81Choice | 809 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PercentageRate | 815 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PlaceOfTradeIdentification1 | 821 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PlusOrMinusIndicator | 827 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}PostalAddress1 | 830 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ProcessingStatus102Choice | 842 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ProprietaryReason4 | 855 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ProprietaryStatusAndReason6 | 861 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Quantity51Choice | 867 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Rate2 | 873 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RateName1 | 879 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RateOrName1Choice | 885 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RateType1Code | 891 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RateType35Choice | 898 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}ReceiveDelivery1Code | 904 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RejectionReason41Choice | 910 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RejectionReason60 | 916 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RejectionReason70Code | 922 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RejectionStatus36Choice | 968 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RepairReason10 | 974 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RepairReason12Choice | 980 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RepairReason5Code | 986 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RepairStatus14Choice | 1028 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RepoCallAcknowledgementReason2Code | 1034 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}RepoCallRequestStatus7Choice | 1041 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}Restriction5Choice | 1048 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SafeKeepingPlace5 | 1054 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SafekeepingPlace1Code | 1060 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SafekeepingPlace3Code | 1068 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SafekeepingPlaceFormat41Choice | 1073 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SafekeepingPlaceTypeAndIdentification1 | 1082 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SafekeepingPlaceTypeAndText8 | 1088 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SecuritiesAccount19 | 1094 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SecuritiesAccount22 | 1101 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SecuritiesFinancingStatusAdviceV11 | 1108 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SecuritiesFinancingTransactionDetails59 | 1120 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SecuritiesFinancingTransactionType2Code | 1163 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SecuritiesRTGS4Choice | 1173 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SecurityIdentification19 | 1179 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementDate19Choice | 1186 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementDateCode8Choice | 1192 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementDetails227 | 1198 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementParties127 | 1218 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementStatus18Choice | 1228 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementSystemMethod1Code | 1235 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementSystemMethod4Choice | 1241 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementTransactionCondition20Code | 1247 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementTransactionCondition45Choice | 1274 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlementTransactionCondition5Code | 1280 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlingCapacity2Code | 1288 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SettlingCapacity7Choice | 1296 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SupplementaryData1 | 1302 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}SupplementaryDataEnvelope1 | 1308 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}TaxCapacityParty4Choice | 1313 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}TaxLiability1Code | 1319 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}TerminationDate6Choice | 1325 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}TradeDate8Choice | 1331 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}TradeDateCode3Choice | 1337 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}TransactionIdentifications53 | 1343 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}TypeOfIdentification1Code | 1351 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}UTIIdentifier | 1362 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}UnmatchedReason13Code | 1367 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}UnmatchedReason17 | 1417 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}UnmatchedReason24Choice | 1423 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}UnmatchedStatus18Choice | 1429 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.034.001.11}YesNoIndicator | 1435 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 59 |
| complexType | 109 |
| element | 323 |
| enumeration | 383 |
| extension | 2 |
| fractionDigits | 6 |
| maxLength | 8 |
| minInclusive | 3 |
| minLength | 8 |
| pattern | 10 |
| restriction | 62 |
| schema | 1 |
| sequence | 48 |
| simpleContent | 2 |
| simpleType | 62 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/53e8b1e85e913c318635e8d2.md) · [Message](index.md)
