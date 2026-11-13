---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.035.001.13"
message_family: "sese.035"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.035.001.13"
source_ids: ["src-000226"]
source_editions: ["2025-2026"]
---

# sese.035.001.13 structure

[src-000226](../../../../../raw-input/settlement_and_reconciliation/sese.035.001.13.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.035.001.13`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.035.001.13 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ActiveOrHistoricCurrencyAndAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ActiveOrHistoricCurrencyAndAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AdditionalParameters24 | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AddressType2Code | 64 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AlternatePartyIdentification7 | 74 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AmountAndDirection21 | 81 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AmountAndDirection44 | 87 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AmountAndDirection5 | 95 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AmountAndDirection94 | 101 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AnyBICDec2014Identifier | 114 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AutoBorrowing1Code | 119 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}AutomaticBorrowing6Choice | 126 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}BICFIDec2014Identifier | 132 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}BaseOneRate | 137 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}BeneficialOwnership4Choice | 143 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}BlockChainAddressWallet3 | 149 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}BlockTrade1Code | 156 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}BlockTrade4Choice | 162 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CFIOct2015Identifier | 168 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CashAccountIdentification5Choice | 173 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CashAccountIdentification9Choice | 179 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CashParties41 | 186 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CashSettlementSystem3Code | 195 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CashSettlementSystem6Choice | 202 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CashSettlementSystemPlace1Choice | 208 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CentralCounterPartyEligibility4Choice | 215 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ClassificationType32Choice | 221 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Counterparty15Choice | 227 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CountryCode | 233 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}CreditDebitCode | 238 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}DTI2024Identifier | 244 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}DateAndDateTime2Choice | 249 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}DateCode18Choice | 255 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}DateType3Code | 261 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}DateType5Code | 266 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}DecimalNumber | 271 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}DeliveryReceiptType2Code | 277 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}DigitalPaymentSettlement1 | 283 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Document | 290 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Eligibility1Code | 295 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}EventFrequency3Code | 302 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Exact3NumericText | 311 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Exact4AlphaNumericText | 316 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Exact4NumericText | 321 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ExternalFinancialInstrumentIdentificationType1Code | 326 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}FinancialInstrumentAttributes111 | 332 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}FinancialInstrumentQuantity33Choice | 376 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ForeignExchangeTerms23 | 384 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}FormOfSecurity1Code | 392 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}FormOfSecurity6Choice | 398 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Frequency23Choice | 404 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}GenericIdentification1 | 410 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}GenericIdentification30 | 417 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}GenericIdentification36 | 424 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}GenericIdentification37 | 431 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}GenericIdentification78 | 437 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}IBAN2007Identifier | 443 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ISINOct2015Identifier | 448 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ISODate | 453 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ISODateTime | 456 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}IdentificationSource3Choice | 459 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}IdentificationType42Choice | 465 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ImpliedCurrencyAndAmount | 471 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}InterestComputationMethod2Code | 478 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}InterestComputationMethodFormat4Choice | 497 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}InvestorCapacity4Choice | 503 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}LEIIdentifier | 509 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}LegalFramework1Code | 514 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}LegalFramework3Choice | 519 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}MICIdentifier | 525 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}MarketClientSide1Code | 530 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}MarketClientSide6Choice | 536 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}MarketIdentification1Choice | 542 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}MarketIdentification3Choice | 548 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}MarketIdentification84 | 554 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}MarketType2Code | 560 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}MarketType8Choice | 569 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Max140Text | 575 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Max16Text | 581 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Max30DecimalNumber | 587 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Max34Text | 593 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Max350Text | 599 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Max35Text | 605 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Max3Number | 611 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Max70Text | 617 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Max8Text | 623 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}NameAndAddress5 | 629 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}NettingEligibility4Choice | 635 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Number22Choice | 641 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OptionStyle2Code | 647 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OptionStyle8Choice | 653 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OptionType1Code | 659 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OptionType6Choice | 665 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OriginalAndCurrentQuantities1 | 671 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OriginatorRole2Code | 677 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OtherAmounts47 | 687 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OtherIdentification1 | 717 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OtherParties43 | 724 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}OwnershipLegalRestrictions1Code | 734 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartialSettlement2Code | 741 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentification120Choice | 747 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentification127Choice | 754 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentification133Choice | 760 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentification136 | 767 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentification144 | 773 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentification257Choice | 779 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentification315 | 787 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentificationAndAccount165 | 797 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentificationAndAccount196 | 806 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentificationAndAccount197 | 818 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentificationAndAccount198 | 830 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentificationAndAccount223 | 841 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyIdentificationAndAccount224 | 853 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyTextInformation1 | 865 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PartyTextInformation2 | 872 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PercentageRate | 878 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PlaceOfClearingIdentification2 | 884 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PlaceOfTradeIdentification1 | 890 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PlusOrMinusIndicator | 896 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PostalAddress1 | 899 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PreConfirmation1Code | 911 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Price10 | 917 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Price7 | 923 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PriceRateOrAmount3Choice | 929 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PriceType4Choice | 935 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PriceValueType12Code | 941 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PriceValueType1Code | 949 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}PriorityNumeric4Choice | 956 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Quantity51Choice | 962 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Quantity83Choice | 968 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}QuantityAndAccount120 | 974 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Rate2 | 988 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}RateName1 | 994 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}RateOrName1Choice | 1000 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}RateType1Code | 1006 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}RateType35Choice | 1013 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}ReceiveDelivery1Code | 1019 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Reporting2Code | 1025 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Reporting6Choice | 1032 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}Restriction5Choice | 1038 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}RevaluationIndicator3Choice | 1044 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SafeKeepingPlace5 | 1050 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SafekeepingPlace1Code | 1056 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SafekeepingPlace3Code | 1064 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SafekeepingPlaceFormat41Choice | 1069 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SafekeepingPlaceTypeAndIdentification1 | 1078 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SafekeepingPlaceTypeAndText8 | 1084 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SecuritiesAccount19 | 1090 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SecuritiesFinancingConfirmationV13 | 1097 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SecuritiesFinancingTransactionDetails56 | 1118 |
| [type-0158](types/type-0158.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SecuritiesFinancingTransactionType2Code | 1151 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SecuritiesPaymentStatus1Code | 1161 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SecuritiesPaymentStatus5Choice | 1168 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SecuritiesRTGS4Choice | 1174 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SecuritiesTradeDetails115 | 1180 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SecurityIdentification19 | 1197 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementDate17Choice | 1204 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementDate18Choice | 1210 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementDate4Code | 1216 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementDateCode7Choice | 1221 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementDetails228 | 1227 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementParties126 | 1248 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementStandingInstructionDatabase1Code | 1258 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementStandingInstructionDatabase4Choice | 1265 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementSystemMethod1Code | 1271 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementSystemMethod4Choice | 1277 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementTransactionCondition20Code | 1283 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementTransactionCondition45Choice | 1310 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlementTransactionCondition5Code | 1316 |
| [type-0177](types/type-0177.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlingCapacity2Code | 1324 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SettlingCapacity7Choice | 1332 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}StandingSettlementInstruction20 | 1338 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SupplementaryData1 | 1347 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}SupplementaryDataEnvelope1 | 1353 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TaxCapacityParty4Choice | 1358 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TaxLiability1Code | 1364 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TerminationDate6Choice | 1370 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TradeDate8Choice | 1376 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TradeDateCode3Choice | 1382 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TradeOriginator3Choice | 1388 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TradeTransactionCondition4Code | 1394 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TradeTransactionCondition5Choice | 1420 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TransactionTypeAndAdditionalParameters22 | 1426 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}TypeOfIdentification1Code | 1439 |
| [type-0192](types/type-0192.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}UTIIdentifier | 1450 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}YesNoIndicator | 1455 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}YieldedOrValueType1Choice | 1458 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.035.001.13}YieldedOrValueType2Choice | 1464 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 60 |
| complexType | 119 |
| element | 464 |
| enumeration | 167 |
| extension | 3 |
| fractionDigits | 9 |
| maxLength | 8 |
| minInclusive | 4 |
| minLength | 8 |
| pattern | 15 |
| restriction | 75 |
| schema | 1 |
| sequence | 56 |
| simpleContent | 3 |
| simpleType | 75 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/efe6fd05d06808590f182ce1.md) · [Message](index.md)
