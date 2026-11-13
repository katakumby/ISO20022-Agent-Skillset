---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.038.001.11"
message_family: "sese.038"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.038.001.11"
source_ids: ["src-000229"]
source_editions: ["2025-2026"]
---

# sese.038.001.11 structure

[src-000229](../../../../../raw-input/settlement_and_reconciliation/sese.038.001.11.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.038.001.11`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.038.001.11 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ActiveOrHistoricCurrencyAndAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ActiveOrHistoricCurrencyAndAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}AddressType2Code | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}AffirmationStatus1Code | 67 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}AffirmationStatus8Choice | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}AlternatePartyIdentification7 | 79 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}AmountAndDirection44 | 86 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}AmountAndDirection51 | 94 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}AmountAndDirection95 | 101 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}AnyBICDec2014Identifier | 114 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}BICFIDec2014Identifier | 119 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}BaseOneRate | 124 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}BeneficialOwnership4Choice | 130 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}BlockChainAddressWallet3 | 136 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CFIOct2015Identifier | 143 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CashAccountIdentification5Choice | 148 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CashAccountIdentification9Choice | 154 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CashParties41 | 161 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CashSettlementSystem3Code | 170 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CashSettlementSystem6Choice | 177 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CashSettlementSystemPlace1Choice | 183 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CentralCounterPartyEligibility4Choice | 190 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ClassificationType32Choice | 196 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Counterparty15Choice | 202 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CountryCode | 208 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CreditDebitCode | 213 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}CurrencyToBuyOrSell1Choice | 219 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DTI2024Identifier | 225 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DateAndDateTime2Choice | 230 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DateType3Code | 236 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DecimalNumber | 241 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DeliveryReceiptType2Code | 247 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DeliveryReturn1Code | 253 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DeliveryReturn3Choice | 264 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DigitalPaymentSettlement1 | 270 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DigitalPaymentSettlement2 | 277 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Document | 284 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}DocumentNumber5Choice | 289 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Eligibility1Code | 296 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}EventFrequency3Code | 303 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Exact3NumericText | 312 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Exact4AlphaNumericText | 317 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ExposureType15Code | 322 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ExposureType25Choice | 360 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ExternalFinancialInstrumentIdentificationType1Code | 366 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}FXStandingInstruction4Choice | 372 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}FinancialInstrumentAttributes111 | 378 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}FinancialInstrumentQuantity33Choice | 422 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ForeignExchangeTerms23 | 430 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}FormOfSecurity1Code | 438 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}FormOfSecurity6Choice | 444 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Frequency23Choice | 450 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}GenericIdentification1 | 456 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}GenericIdentification30 | 463 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}GenericIdentification36 | 470 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}GenericIdentification37 | 477 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}GenericIdentification78 | 483 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}IBAN2007Identifier | 489 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ISINOct2015Identifier | 494 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ISO20022MessageIdentificationText | 499 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ISODate | 504 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ISODateTime | 507 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}IdentificationSource3Choice | 510 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}IdentificationType42Choice | 516 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ImpliedCurrencyAndAmount | 522 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}InterestComputationMethod2Code | 529 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}InterestComputationMethodFormat4Choice | 548 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}InvestorCapacity4Choice | 554 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}LEIIdentifier | 560 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}LetterOfGuarantee4Choice | 565 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Linkages40 | 571 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Linkages80 | 576 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MICIdentifier | 584 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MarketClientSide1Code | 589 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MarketClientSide6Choice | 595 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MarketIdentification1Choice | 601 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MarketIdentification3Choice | 607 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MarketIdentification84 | 613 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MarketType2Code | 619 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MarketType8Choice | 628 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MatchingStatus1Code | 634 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}MatchingStatus27Choice | 640 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Max140Text | 646 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Max16Text | 652 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Max210Text | 658 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Max30DecimalNumber | 664 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Max34Text | 670 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Max350Text | 676 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Max35Text | 682 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Max3Number | 688 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Max70Text | 694 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ModificationCancellationAllowed4Choice | 700 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}NameAndAddress5 | 706 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}NettingEligibility4Choice | 712 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Number22Choice | 718 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OpeningClosing1Code | 724 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OpeningClosing3Choice | 730 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OptionStyle2Code | 736 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OptionStyle8Choice | 742 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OptionType1Code | 748 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OptionType6Choice | 754 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OriginalAndCurrentQuantities1 | 760 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OriginatorRole2Code | 766 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OtherAmounts39 | 776 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OtherIdentification1 | 805 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OtherParties43 | 812 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}OwnershipLegalRestrictions1Code | 822 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PairedOrTurnedQuantity7Choice | 829 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification120Choice | 835 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification127Choice | 842 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification133Choice | 848 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification134Choice | 855 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification136 | 863 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification144 | 869 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification149 | 875 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification257Choice | 881 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification314 | 889 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentification315 | 896 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentificationAndAccount165 | 906 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentificationAndAccount195 | 915 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentificationAndAccount196 | 924 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentificationAndAccount197 | 936 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentificationAndAccount198 | 948 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentificationAndAccount223 | 959 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyIdentificationAndAccount224 | 971 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyTextInformation1 | 983 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PartyTextInformation2 | 990 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PercentageRate | 996 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PlaceOfClearingIdentification2 | 1002 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PlaceOfTradeIdentification1 | 1008 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PostalAddress1 | 1014 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Price10 | 1026 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Price7 | 1032 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PriceRateOrAmount3Choice | 1038 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PriceType4Choice | 1044 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PriceValueType12Code | 1050 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}PriceValueType1Code | 1058 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ProcessingPosition3Code | 1065 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ProcessingPosition7Choice | 1073 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Quantity51Choice | 1079 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Quantity83Choice | 1085 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}QuantityAndAccount113 | 1091 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}QuantityAndAccount118 | 1103 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}QuantityBreakdown62 | 1112 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}ReceiveDelivery1Code | 1121 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}References47Choice | 1127 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Registration1Code | 1136 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Registration9Choice | 1142 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}RegistrationParameters6 | 1148 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Reporting2Code | 1156 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Reporting6Choice | 1163 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Restriction5Choice | 1169 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SafeKeepingPlace5 | 1175 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SafekeepingPlace1Code | 1181 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SafekeepingPlace3Code | 1189 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SafekeepingPlaceFormat41Choice | 1194 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SafekeepingPlaceTypeAndIdentification1 | 1203 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SafekeepingPlaceTypeAndText8 | 1209 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesAccount19 | 1215 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesCertificate4 | 1222 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesPaymentStatus1Code | 1229 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesPaymentStatus5Choice | 1236 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesSettlementTransactionDetails59 | 1242 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesSettlementTransactionDetails60 | 1262 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesSettlementTransactionDetails61 | 1282 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesSettlementTransactionModificationRequestV11 | 1303 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesTradeDetails146 | 1309 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesTradeDetails147 | 1333 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesTransactionType28Code | 1358 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecuritiesTransactionType59Choice | 1406 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SecurityIdentification19 | 1412 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementDate17Choice | 1419 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementDate4Code | 1425 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementDateCode7Choice | 1430 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementDetails230 | 1436 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementParties125 | 1462 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementParties126 | 1472 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementParties98 | 1482 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementStandingInstructionDatabase1Code | 1490 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementStandingInstructionDatabase4Choice | 1497 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementTransactionCondition17Code | 1503 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementTransactionCondition42Choice | 1532 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementTypeAndAdditionalParameters13 | 1538 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementTypeAndAdditionalParameters14 | 1545 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlementTypeAndIdentification18 | 1554 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlingCapacity2Code | 1561 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SettlingCapacity7Choice | 1569 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}StandingSettlementInstruction20 | 1575 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SupplementaryData1 | 1584 |
| [type-0197](types/type-0197.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}SupplementaryDataEnvelope1 | 1590 |
| [type-0198](types/type-0198.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TaxCapacityParty4Choice | 1595 |
| [type-0199](types/type-0199.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TaxLiability1Code | 1601 |
| [type-0200](types/type-0200.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}Tracking4Choice | 1607 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TradeDate8Choice | 1613 |
| [type-0202](types/type-0202.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TradeDateCode3Choice | 1619 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TradeOriginator3Choice | 1625 |
| [type-0204](types/type-0204.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TradeTransactionCondition4Code | 1631 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TradeTransactionCondition5Choice | 1657 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TransactionDetails180 | 1663 |
| [type-0207](types/type-0207.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TransactionDetails181 | 1676 |
| [type-0208](types/type-0208.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TypeOfIdentification1Code | 1689 |
| [type-0209](types/type-0209.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TypeOfPrice14Code | 1700 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}TypeOfPrice29Choice | 1705 |
| [type-0211](types/type-0211.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}UTIIdentifier | 1711 |
| [type-0212](types/type-0212.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}UpdateType40Choice | 1716 |
| [type-0213](types/type-0213.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}YesNoIndicator | 1723 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}YieldedOrValueType1Choice | 1726 |
| [type-0215](types/type-0215.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.038.001.11}YieldedOrValueType2Choice | 1732 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 67 |
| complexType | 141 |
| element | 577 |
| enumeration | 241 |
| extension | 3 |
| fractionDigits | 9 |
| maxLength | 8 |
| minInclusive | 4 |
| minLength | 8 |
| pattern | 15 |
| restriction | 73 |
| schema | 1 |
| sequence | 71 |
| simpleContent | 3 |
| simpleType | 73 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/c739dc7cc7ac2eef926ca62c.md) · [Message](index.md)
