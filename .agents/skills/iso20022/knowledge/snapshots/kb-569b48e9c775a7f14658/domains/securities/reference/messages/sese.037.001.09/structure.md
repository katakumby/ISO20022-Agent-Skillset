---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.037.001.09"
message_family: "sese.037"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.037.001.09"
source_ids: ["src-000228"]
source_editions: ["2025-2026"]
---

# sese.037.001.09 structure

[src-000228](../../../../../raw-input/settlement_and_reconciliation/sese.037.001.09.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.037.001.09`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.037.001.09 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}AcknowledgedAcceptedStatus32Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}AcknowledgementReason20 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}AcknowledgementReason23Choice | 17 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}AcknowledgementReason9Code | 23 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ActiveCurrencyAndAmount_SimpleType | 28 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ActiveCurrencyAndAmount | 35 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ActiveCurrencyCode | 42 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 47 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ActiveOrHistoricCurrencyAnd13DecimalAmount | 54 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ActiveOrHistoricCurrencyAndAmount_SimpleType | 61 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ActiveOrHistoricCurrencyAndAmount | 68 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ActiveOrHistoricCurrencyCode | 75 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}AddressType2Code | 80 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}AlternatePartyIdentification7 | 90 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}AmountAndDirection44 | 97 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}AmountAndDirection52 | 105 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}AnyBICDec2014Identifier | 111 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}BaseOneRate | 116 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}BlockChainAddressWallet3 | 122 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}CFIOct2015Identifier | 129 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}CashSettlementSystemPlace1Choice | 134 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ClassificationType32Choice | 141 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}CountryCode | 147 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}CreditDebitCode | 152 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}DTI2024Identifier | 158 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}DateAndDateTime2Choice | 163 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}DateType3Code | 169 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}DecimalNumber | 174 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}DeliveryReceiptType2Code | 180 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}DigitalPaymentSettlement1 | 186 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Document | 193 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}EventFrequency3Code | 198 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Exact3NumericText | 207 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Exact4AlphaNumericText | 212 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Exact5NumericText | 217 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ExternalFinancialInstrumentIdentificationType1Code | 222 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}FinancialInstrumentAttributes111 | 228 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}FinancialInstrumentQuantity33Choice | 272 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ForeignExchangeTerms23 | 280 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}FormOfSecurity1Code | 288 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}FormOfSecurity6Choice | 294 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Frequency23Choice | 300 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}GenericIdentification1 | 306 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}GenericIdentification30 | 313 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}GenericIdentification36 | 320 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}GenericIdentification37 | 327 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ISINOct2015Identifier | 333 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ISODate | 338 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ISODateTime | 341 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}IdentificationSource3Choice | 344 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}IdentificationType42Choice | 350 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ImpliedCurrencyAndAmount | 356 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}InterestComputationMethod2Code | 363 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}InterestComputationMethodFormat4Choice | 382 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}LEIIdentifier | 388 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}MICIdentifier | 393 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}MarketIdentification3Choice | 398 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Max140Text | 404 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Max16Text | 410 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Max210Text | 416 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Max30DecimalNumber | 422 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Max350Text | 428 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Max35Text | 434 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Max3Number | 440 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Max5NumericText | 446 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Max70Text | 451 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}NameAndAddress5 | 457 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}NoReasonCode | 463 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Number22Choice | 468 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Number3Choice | 474 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}OptionStyle2Code | 480 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}OptionStyle8Choice | 486 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}OptionType1Code | 492 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}OptionType6Choice | 498 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}OtherAmounts29 | 504 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}OtherIdentification1 | 524 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}OtherParties39 | 531 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}OwnershipLegalRestrictions1Code | 538 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Pagination1 | 545 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyIdentification120Choice | 551 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyIdentification127Choice | 558 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyIdentification134Choice | 564 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyIdentification136 | 572 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyIdentification144 | 578 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyIdentification149 | 584 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyIdentification257Choice | 590 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyIdentification315 | 598 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyIdentificationAndAccount196 | 608 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PartyTextInformation1 | 620 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PendingFailingReason1Code | 627 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PendingProcessingReason14 | 632 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PendingProcessingReason16Choice | 638 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PendingProcessingStatus17Choice | 644 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PercentageRate | 650 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PortfolioTransferNotificationV09 | 656 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PortfolioTransferStatus2Choice | 666 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PostalAddress1 | 674 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Price7 | 686 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PriceRateOrAmount3Choice | 692 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PriceType4Choice | 698 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}PriceValueType1Code | 704 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ProprietaryReason4 | 711 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ProprietaryStatusAndReason6 | 717 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Quantity48 | 723 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Quantity83Choice | 731 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}QuantityBreakdown62 | 737 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}ReceiveDelivery1Code | 746 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Registration1Code | 752 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Registration9Choice | 758 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}RejectionReason37Choice | 764 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}RejectionReason49 | 770 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}RejectionReason55Code | 776 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}RejectionStatus30Choice | 788 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Reporting1Code | 794 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Reporting7Choice | 800 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Restriction5Choice | 806 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SecuritiesAccount19 | 812 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SecuritiesCertificate4 | 819 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SecuritiesPaymentStatus1Code | 826 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SecuritiesPaymentStatus5Choice | 833 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SecuritiesRTGS4Choice | 839 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SecuritiesTradeDetails154 | 845 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SecurityIdentification19 | 870 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SettlementDate17Choice | 877 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SettlementDate4Code | 883 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SettlementDateCode7Choice | 888 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SettlementDetails236 | 894 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SettlementParties128 | 905 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SettlementSystemMethod1Code | 915 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SettlementSystemMethod4Choice | 921 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SettlementTransactionCondition21Code | 927 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SettlementTransactionCondition47Choice | 945 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}Statement62 | 951 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}StatementUpdateType1Code | 961 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SupplementaryData1 | 967 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}SupplementaryDataEnvelope1 | 973 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}TaxCapacityParty4Choice | 978 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}TaxLiability1Code | 984 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}TradeDate8Choice | 990 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}TradeDateCode3Choice | 996 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}TypeOfIdentification1Code | 1002 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}TypeOfPrice14Code | 1013 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}TypeOfPrice29Choice | 1018 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}UpdateType15Choice | 1024 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}YesNoIndicator | 1030 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.037.001.09}YieldedOrValueType1Choice | 1033 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 43 |
| complexType | 88 |
| element | 303 |
| enumeration | 92 |
| extension | 3 |
| fractionDigits | 9 |
| maxLength | 7 |
| minInclusive | 4 |
| minLength | 7 |
| pattern | 13 |
| restriction | 58 |
| schema | 1 |
| sequence | 42 |
| simpleContent | 3 |
| simpleType | 58 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
