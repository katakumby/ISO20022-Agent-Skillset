---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.017.001.14"
message_family: "semt.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.017.001.14"
source_ids: ["src-000205"]
source_editions: ["2025-2026"]
---

# semt.017.001.14 structure

[src-000205](../../../../../raw-input/settlement_and_reconciliation/semt.017.001.14.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.017.001.14`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.017.001.14 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Account29 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}AccountIdentification26 | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 16 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ActiveOrHistoricCurrencyAnd13DecimalAmount | 23 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ActiveOrHistoricCurrencyAndAmount_SimpleType | 30 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ActiveOrHistoricCurrencyAndAmount | 37 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ActiveOrHistoricCurrencyCode | 44 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}AdditionalReference10 | 49 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}AddressType2Code | 56 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}AmountAndDirection21 | 66 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}AmountAndDirection3 | 72 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}AnyBICDec2014Identifier | 78 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}BalanceQuantity14Choice | 83 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}BeneficialOwnership4Choice | 89 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}BlockChainAddressWallet2 | 95 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}BlockChainAddressWallet3 | 102 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}BlockChainAddressWallet4 | 109 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}BlockTrade1Code | 117 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}BlockTrade4Choice | 123 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}CFIOct2015Identifier | 129 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}CashSettlementSystem3Code | 134 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}CashSettlementSystem6Choice | 141 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}CashSettlementSystemPlace1Choice | 147 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}CentralCounterPartyEligibility4Choice | 154 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ClosingBalance5 | 160 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ClosingBalance6Choice | 166 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}CorporateActionEventType110Choice | 172 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}CorporateActionEventType38Code | 178 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}CountryCode | 251 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}CreditDebitCode | 256 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}DTI2024Identifier | 262 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}DateAndDateTime2Choice | 267 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}DateTimePeriod1 | 273 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}DateType3Code | 279 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}DecimalNumber | 284 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}DeliveryReceiptType2Code | 290 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}DigitalPaymentSettlement2 | 296 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}DistributionPolicy1Code | 303 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Document | 309 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}EventFrequency4Code | 314 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Exact3NumericText | 324 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Exact4AlphaNumericText | 329 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Exact5NumericText | 334 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ExternalFinancialInstrumentIdentificationType1Code | 339 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}FinancialInstrument72 | 345 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}FinancialInstrumentDetails48 | 354 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}FinancialInstrumentDetails49 | 365 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}FinancialInstrumentQuantity33Choice | 376 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}FormOfSecurity1Code | 384 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Frequency25Choice | 390 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}GenericIdentification1 | 396 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}GenericIdentification3 | 403 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}GenericIdentification30 | 409 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}GenericIdentification36 | 416 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}GenericIdentification56 | 423 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}GenericIdentification78 | 431 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ISINOct2015Identifier | 437 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ISODate | 442 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ISODateTime | 445 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}IdentificationSource3Choice | 448 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ImpliedCurrencyAndAmount | 454 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Intermediary44 | 461 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}InvestmentFundRole2Code | 468 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}LEIIdentifier | 481 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}LetterOfGuarantee4Choice | 486 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MICIdentifier | 492 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketClientSide1Code | 497 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketClientSide6Choice | 503 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketIdentification1Choice | 509 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketIdentification5Choice | 515 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketIdentification84 | 521 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketIdentification98 | 527 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketType19Choice | 533 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketType2Code | 539 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketType8Choice | 548 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}MarketType9Code | 554 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Max140Text | 563 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Max16Text | 569 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Max30DecimalNumber | 575 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Max350Text | 581 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Max35Text | 587 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Max3Number | 593 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Max5NumericText | 599 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Max70Text | 604 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}NameAndAddress5 | 610 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}NettingEligibility4Choice | 616 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Number3Choice | 622 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}OpeningBalance5 | 628 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}OpeningBalance6Choice | 634 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}OriginalAndCurrentQuantities1 | 640 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}OtherIdentification1 | 646 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}OwnershipLegalRestrictions1Code | 653 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Pagination1 | 660 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PartyIdentification120Choice | 666 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PartyIdentification125Choice | 673 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PartyIdentification127Choice | 680 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PartyIdentification136 | 686 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PartyIdentification139 | 692 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PartyIdentification144 | 698 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PartyIdentification257Choice | 704 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PartyIdentification314 | 712 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PartyIdentificationAndAccount195 | 719 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PercentageRate | 728 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Period2 | 734 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Period7Choice | 740 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PlaceOfClearingIdentification2 | 746 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PlaceOfTradeIdentification1 | 752 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PostalAddress1 | 758 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PriceInformation30 | 770 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PriceRateOrAmountOrUnknown2Choice | 779 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PriceValueType1Code | 786 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}PurposeCode7Choice | 793 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Quantity51Choice | 799 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ReceiveDelivery1Code | 805 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Registration1Code | 811 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Registration9Choice | 817 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}RepurchaseType22Choice | 823 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}RepurchaseType9Code | 829 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Restriction5Choice | 841 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Role6Choice | 847 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SafeKeepingPlace5 | 854 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SafekeepingPlace1Code | 860 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SafekeepingPlace3Code | 868 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SafekeepingPlaceFormat41Choice | 873 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SafekeepingPlaceTypeAndIdentification1 | 882 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SafekeepingPlaceTypeAndText8 | 888 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecuritiesAccount19 | 894 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecuritiesAccount25 | 901 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecuritiesAccount36 | 908 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecuritiesAccountPurposeType1Code | 916 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecuritiesRTGS4Choice | 926 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecuritiesTransactionPostingReportV14 | 932 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecuritiesTransactionType27Code | 944 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecuritiesTransactionType48Choice | 994 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecurityClassificationType2Choice | 1000 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SecurityIdentification19 | 1006 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementDate17Choice | 1013 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementDate4Code | 1019 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementDateCode7Choice | 1024 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementDetails231 | 1030 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementOrCorporateActionEvent35Choice | 1051 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementParties125 | 1057 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementSystemMethod1Code | 1067 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementSystemMethod4Choice | 1073 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementTransactionCondition16Code | 1079 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementTransactionCondition41Choice | 1110 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlementTransactionCondition5Code | 1116 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlingCapacity2Code | 1124 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SettlingCapacity7Choice | 1132 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}ShortLong1Code | 1138 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SimpleIdentificationInformation4 | 1144 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Statement79 | 1149 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}StatementBasis2Code | 1162 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}StatementBasis8Choice | 1168 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}StatementUpdateType1Code | 1174 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SubAccountIdentification74 | 1180 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SupplementaryData1 | 1189 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}SupplementaryDataEnvelope1 | 1195 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TaxCapacityParty4Choice | 1200 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TaxLiability1Code | 1206 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TradeDate8Choice | 1212 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TradeDateCode3Choice | 1218 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Transaction165 | 1224 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}Transaction167 | 1248 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TransactionActivity1Code | 1272 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TransactionActivity3Choice | 1281 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TransactionDetails184 | 1287 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TransactionDetails186 | 1314 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TypeOfPrice17Code | 1341 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}TypeOfPrice48Choice | 1359 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}UTIIdentifier | 1365 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}UpdateType15Choice | 1370 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}YesNoIndicator | 1376 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.017.001.14}YieldedOrValueType1Choice | 1379 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 51 |
| complexType | 111 |
| element | 383 |
| enumeration | 256 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 6 |
| minInclusive | 3 |
| minLength | 6 |
| pattern | 13 |
| restriction | 63 |
| schema | 1 |
| sequence | 58 |
| simpleContent | 2 |
| simpleType | 63 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/47a12f6ce98904cdcd2e3e8b.md) · [Message](index.md)
