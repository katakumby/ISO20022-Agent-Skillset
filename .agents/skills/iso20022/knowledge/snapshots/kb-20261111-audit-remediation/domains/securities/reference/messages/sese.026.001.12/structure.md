---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.026.001.12"
message_family: "sese.026"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.026.001.12"
source_ids: ["src-000217"]
source_editions: ["2025-2026"]
---

# sese.026.001.12 structure

[src-000217](../../../../../raw-input/settlement_and_reconciliation/sese.026.001.12.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.026.001.12`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.026.001.12 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ActiveOrHistoricCurrencyAndAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ActiveOrHistoricCurrencyAndAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}AdditionalParameters30 | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}AddressType2Code | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}AlternatePartyIdentification7 | 75 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}AmountAndDirection44 | 82 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}AmountAndDirection52 | 90 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}AmountAndDirection94 | 96 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}AnyBICDec2014Identifier | 109 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}AutoBorrowing1Code | 114 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}AutomaticBorrowing6Choice | 121 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}BICFIDec2014Identifier | 127 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}BaseOneRate | 132 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}BeneficialOwnership4Choice | 138 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}BlockChainAddressWallet3 | 144 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}BlockTrade1Code | 151 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}BlockTrade4Choice | 157 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CFIOct2015Identifier | 163 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CashAccountIdentification5Choice | 168 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CashAccountIdentification9Choice | 174 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CashParties42 | 181 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CashSettlementSystem3Code | 189 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CashSettlementSystem6Choice | 196 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CashSettlementSystemPlace1Choice | 202 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CentralCounterPartyEligibility4Choice | 209 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ClassificationType32Choice | 215 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Counterparty15Choice | 221 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CountryCode | 227 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}CreditDebitCode | 232 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}DTI2024Identifier | 238 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}DateAndDateTime2Choice | 243 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}DateType3Code | 249 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}DecimalNumber | 254 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}DeliveryReceiptType2Code | 260 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}DigitalPaymentSettlement1 | 266 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Document | 273 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Eligibility1Code | 278 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}EventFrequency3Code | 285 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Exact3NumericText | 294 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Exact4AlphaNumericText | 299 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Exact4NumericText | 304 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ExposureType15Code | 309 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ExposureType25Choice | 347 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ExternalFinancialInstrumentIdentificationType1Code | 353 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}FinancialInstrumentAttributes111 | 359 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}FinancialInstrumentQuantity33Choice | 403 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ForeignExchangeTerms23 | 411 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}FormOfSecurity1Code | 419 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}FormOfSecurity6Choice | 425 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Frequency23Choice | 431 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}GenericIdentification1 | 437 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}GenericIdentification30 | 444 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}GenericIdentification36 | 451 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}GenericIdentification37 | 458 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}GenericIdentification78 | 464 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}IBAN2007Identifier | 470 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ISINOct2015Identifier | 475 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ISODate | 480 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ISODateTime | 483 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}IdentificationSource3Choice | 486 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}IdentificationType42Choice | 492 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ImpliedCurrencyAndAmount | 498 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}InterestComputationMethod2Code | 505 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}InterestComputationMethodFormat4Choice | 524 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}InvestorCapacity4Choice | 530 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}LEIIdentifier | 536 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}LetterOfGuarantee4Choice | 541 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}MICIdentifier | 547 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}MarketClientSide1Code | 552 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}MarketClientSide6Choice | 558 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}MarketIdentification1Choice | 564 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}MarketIdentification3Choice | 570 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}MarketIdentification84 | 576 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}MarketType2Code | 582 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}MarketType8Choice | 591 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Max140Text | 597 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Max16Text | 603 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Max210Text | 609 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Max30DecimalNumber | 615 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Max34Text | 621 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Max350Text | 627 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Max35Text | 633 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Max3Number | 639 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Max70Text | 645 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}NameAndAddress5 | 651 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}NettingEligibility4Choice | 657 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Number22Choice | 663 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OpeningClosing1Code | 669 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OpeningClosing3Choice | 675 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OptionStyle2Code | 681 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OptionStyle8Choice | 687 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OptionType1Code | 693 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OptionType6Choice | 699 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OriginalAndCurrentQuantities1 | 705 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OriginatorRole2Code | 711 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OtherAmounts46 | 721 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OtherIdentification1 | 753 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OtherParties43 | 760 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}OwnershipLegalRestrictions1Code | 770 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartialSettlement2Code | 777 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentification120Choice | 783 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentification127Choice | 790 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentification133Choice | 796 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentification136 | 803 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentification144 | 809 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentification257Choice | 815 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentification315 | 823 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentificationAndAccount165 | 833 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentificationAndAccount196 | 842 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentificationAndAccount197 | 854 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentificationAndAccount198 | 866 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentificationAndAccount223 | 877 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyIdentificationAndAccount224 | 889 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyTextInformation1 | 901 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PartyTextInformation2 | 908 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PercentageRate | 914 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PlaceOfClearingIdentification2 | 920 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PlaceOfTradeIdentification1 | 926 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PostalAddress1 | 932 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PreConfirmation1Code | 944 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Price10 | 950 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Price7 | 956 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PriceRateOrAmount3Choice | 962 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PriceType4Choice | 968 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PriceValueType12Code | 974 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PriceValueType1Code | 982 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}PriorityNumeric4Choice | 989 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Quantity51Choice | 995 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Quantity83Choice | 1001 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}QuantityAndAccount115 | 1007 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}QuantityBreakdown63 | 1023 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}ReceiveDelivery1Code | 1033 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Registration1Code | 1039 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Registration9Choice | 1045 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}RegistrationParameters6 | 1051 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Reporting2Code | 1059 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Reporting6Choice | 1066 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}RepurchaseType22Choice | 1072 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}RepurchaseType9Code | 1078 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}Restriction5Choice | 1090 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SafeKeepingPlace5 | 1096 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SafekeepingPlace1Code | 1102 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SafekeepingPlace3Code | 1110 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SafekeepingPlaceFormat41Choice | 1115 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SafekeepingPlaceTypeAndIdentification1 | 1124 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SafekeepingPlaceTypeAndText8 | 1130 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecuritiesAccount19 | 1136 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecuritiesCertificate4 | 1143 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecuritiesPaymentStatus1Code | 1150 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecuritiesPaymentStatus5Choice | 1157 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecuritiesRTGS4Choice | 1163 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecuritiesSettlementTransactionReversalAdviceV12 | 1169 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecuritiesTradeDetails150 | 1191 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecuritiesTransactionType22Code | 1213 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecuritiesTransactionType46Choice | 1260 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SecurityIdentification19 | 1266 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementDate17Choice | 1273 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementDate18Choice | 1279 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementDate4Code | 1285 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementDateCode7Choice | 1290 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementDetails223 | 1296 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementParties126 | 1324 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementStandingInstructionDatabase1Code | 1334 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementStandingInstructionDatabase4Choice | 1341 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementSystemMethod1Code | 1347 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementSystemMethod4Choice | 1353 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementTransactionCondition17Code | 1359 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementTransactionCondition42Choice | 1388 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementTransactionCondition5Code | 1394 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlementTypeAndIdentification29 | 1402 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlingCapacity2Code | 1417 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SettlingCapacity7Choice | 1425 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}StandingSettlementInstruction20 | 1431 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SupplementaryData1 | 1440 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}SupplementaryDataEnvelope1 | 1446 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TaxCapacityParty4Choice | 1451 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TaxLiability1Code | 1457 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TradeDate8Choice | 1463 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TradeDateCode3Choice | 1469 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TradeOriginator3Choice | 1475 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TradeTransactionCondition4Code | 1481 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TradeTransactionCondition5Choice | 1507 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TypeOfIdentification1Code | 1513 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TypeOfPrice14Code | 1524 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}TypeOfPrice29Choice | 1529 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}UTIIdentifier | 1535 |
| [type-0194](types/type-0194.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}YesNoIndicator | 1540 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}YieldedOrValueType1Choice | 1543 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.026.001.12}YieldedOrValueType2Choice | 1549 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 61 |
| complexType | 119 |
| element | 463 |
| enumeration | 248 |
| extension | 3 |
| fractionDigits | 9 |
| maxLength | 8 |
| minInclusive | 4 |
| minLength | 8 |
| pattern | 15 |
| restriction | 76 |
| schema | 1 |
| sequence | 55 |
| simpleContent | 3 |
| simpleType | 76 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
