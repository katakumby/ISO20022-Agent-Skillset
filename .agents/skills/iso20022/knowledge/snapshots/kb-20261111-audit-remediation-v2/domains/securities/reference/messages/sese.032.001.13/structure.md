---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.032.001.13"
message_family: "sese.032"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.032.001.13"
source_ids: ["src-000223"]
source_editions: ["2025-2026"]
---

# sese.032.001.13 structure

[src-000223](../../../../../raw-input/settlement_and_reconciliation/sese.032.001.13.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.032.001.13`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.032.001.13 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AcknowledgedAcceptedStatus21Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AcknowledgementReason12Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AcknowledgementReason5Code | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AcknowledgementReason9 | 30 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ActiveCurrencyAndAmount_SimpleType | 36 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ActiveCurrencyAndAmount | 43 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ActiveCurrencyCode | 50 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 55 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ActiveOrHistoricCurrencyAnd13DecimalAmount | 62 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ActiveOrHistoricCurrencyAndAmount_SimpleType | 69 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ActiveOrHistoricCurrencyAndAmount | 76 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ActiveOrHistoricCurrencyCode | 83 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AddressType2Code | 88 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AffirmationStatus1Code | 98 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AffirmationStatus8Choice | 104 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AlternatePartyIdentification7 | 110 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AmountAndDirection44 | 117 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AmountAndDirection94 | 125 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AnyBICDec2014Identifier | 138 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AutoBorrowing1Code | 143 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}AutomaticBorrowing6Choice | 150 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}BICFIDec2014Identifier | 156 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}BaseOneRate | 161 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}BeneficialOwnership4Choice | 167 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}BlockChainAddressWallet3 | 173 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}BlockTrade1Code | 180 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}BlockTrade4Choice | 186 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CFIOct2015Identifier | 192 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CashAccountIdentification5Choice | 197 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CashAccountIdentification9Choice | 203 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CashParties41 | 210 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CashSettlementSystem3Code | 219 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CashSettlementSystem6Choice | 226 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CashSettlementSystemPlace1Choice | 232 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CentralCounterPartyEligibility4Choice | 239 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ClassificationType32Choice | 245 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CountryCode | 251 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CreditDebitCode | 256 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}CurrencyToBuyOrSell1Choice | 262 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}DTI2024Identifier | 268 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}DateAndDateTime2Choice | 273 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}DateType3Code | 279 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}DecimalNumber | 284 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}DeliveryReceiptType2Code | 290 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}DeliveryReturn1Code | 296 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}DeliveryReturn3Choice | 307 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}DigitalPaymentSettlement1 | 313 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Document | 320 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}DocumentNumber5Choice | 325 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Eligibility1Code | 332 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}EventFrequency3Code | 339 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Exact3NumericText | 348 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Exact4AlphaNumericText | 353 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Exact4NumericText | 358 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ExposureType15Code | 363 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ExposureType25Choice | 401 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ExternalFinancialInstrumentIdentificationType1Code | 407 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}FXStandingInstruction4Choice | 413 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}FailingReason13 | 419 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}FailingReason18Choice | 425 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}FailingReason5Code | 431 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}FailingStatus15Choice | 499 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}FinancialInstrumentAttributes111 | 505 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}FinancialInstrumentQuantity33Choice | 549 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ForeignExchangeTerms23 | 557 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}FormOfSecurity1Code | 565 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}FormOfSecurity6Choice | 571 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Frequency23Choice | 577 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}GeneratedReason3Code | 583 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}GeneratedReason5 | 594 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}GeneratedReasons5Choice | 600 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}GenericIdentification1 | 606 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}GenericIdentification30 | 613 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}GenericIdentification36 | 620 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}GenericIdentification37 | 627 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}GenericIdentification78 | 633 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}HoldIndicator6 | 639 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}IBAN2007Identifier | 645 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ISINOct2015Identifier | 650 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ISO20022MessageIdentificationText | 655 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ISODate | 660 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ISODateTime | 663 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}IdentificationSource3Choice | 666 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}IdentificationType42Choice | 672 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ImpliedCurrencyAndAmount | 678 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}InterestComputationMethod2Code | 685 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}InterestComputationMethodFormat4Choice | 704 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}InvestorCapacity4Choice | 710 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}LEIIdentifier | 716 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}LetterOfGuarantee4Choice | 721 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Linkages81 | 727 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MICIdentifier | 736 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MarketClientSide1Code | 741 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MarketClientSide6Choice | 747 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MarketIdentification1Choice | 753 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MarketIdentification3Choice | 759 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MarketIdentification84 | 765 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MarketType2Code | 771 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MarketType8Choice | 780 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MatchingStatus1Code | 786 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MatchingStatus24Choice | 792 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}MatchingStatus27Choice | 799 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max140Text | 805 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max16Text | 811 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max210Text | 817 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max30DecimalNumber | 823 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max34Text | 829 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max350Text | 835 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max35Text | 841 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max3Number | 847 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max6NumericText | 853 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Max70Text | 858 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ModificationCancellationAllowed4Choice | 864 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}NameAndAddress5 | 870 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}NettingEligibility4Choice | 876 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}NoReasonCode | 882 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Number22Choice | 887 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}NumberCount2Choice | 893 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OpeningClosing1Code | 899 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OpeningClosing3Choice | 905 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OptionStyle2Code | 911 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OptionStyle8Choice | 917 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OptionType1Code | 923 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OptionType6Choice | 929 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OriginalAndCurrentQuantities1 | 935 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OriginatorRole2Code | 941 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OtherAmounts45 | 951 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OtherIdentification1 | 981 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OtherParties43 | 988 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}OwnershipLegalRestrictions1Code | 998 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PairedOrTurnedQuantity7Choice | 1005 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentification120Choice | 1011 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentification127Choice | 1018 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentification133Choice | 1024 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentification144 | 1031 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentification257Choice | 1037 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentification315 | 1045 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentificationAndAccount165 | 1055 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentificationAndAccount196 | 1064 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentificationAndAccount197 | 1076 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentificationAndAccount198 | 1088 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentificationAndAccount223 | 1099 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyIdentificationAndAccount224 | 1111 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyTextInformation1 | 1123 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PartyTextInformation2 | 1130 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingProcessingReason19 | 1136 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingProcessingReason21Choice | 1142 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingProcessingReason7Code | 1148 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingProcessingStatus22Choice | 1177 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingReason28Code | 1183 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingReason32 | 1249 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingReason32Code | 1255 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingReason35 | 1265 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingReason69Choice | 1271 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingReason77Choice | 1277 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingStatus73Choice | 1283 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PendingStatus81Choice | 1289 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PercentageRate | 1295 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PlaceOfClearingIdentification2 | 1301 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PlaceOfTradeIdentification1 | 1307 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PostalAddress1 | 1313 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Price10 | 1325 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Price7 | 1331 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PriceRateOrAmount3Choice | 1337 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PriceType4Choice | 1343 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PriceValueType12Code | 1349 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PriceValueType1Code | 1357 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}PriorityNumeric4Choice | 1364 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ProcessingPosition3Code | 1370 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ProcessingPosition7Choice | 1378 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ProcessingStatus104Choice | 1384 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ProprietaryReason4 | 1394 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ProprietaryStatusAndReason6 | 1400 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Quantity51Choice | 1406 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Quantity83Choice | 1412 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}QuantityAndAccount117 | 1418 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}QuantityBreakdown62 | 1430 |
| [type-0179](types/type-0179.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}ReceiveDelivery1Code | 1439 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}References86Choice | 1445 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Registration10Choice | 1457 |
| [type-0182](types/type-0182.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Registration1Code | 1463 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Registration2Code | 1469 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Registration9Choice | 1477 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}RegistrationParameters6 | 1483 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}RegistrationReason5 | 1491 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}RepairReason10Choice | 1497 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}RepairReason4Code | 1503 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}RepairReason8 | 1536 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}RepairStatus12Choice | 1542 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Reporting2Code | 1548 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Reporting6Choice | 1555 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}RepurchaseType10Code | 1561 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}RepurchaseType23Choice | 1572 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Restriction5Choice | 1578 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SafeKeepingPlace5 | 1584 |
| [type-0197](types/type-0197.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SafekeepingPlace1Code | 1590 |
| [type-0198](types/type-0198.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SafekeepingPlace3Code | 1598 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SafekeepingPlaceFormat41Choice | 1603 |
| [type-0200](types/type-0200.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SafekeepingPlaceTypeAndIdentification1 | 1612 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SafekeepingPlaceTypeAndText8 | 1618 |
| [type-0202](types/type-0202.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecuritiesAccount19 | 1624 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecuritiesCertificate4 | 1631 |
| [type-0204](types/type-0204.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecuritiesPaymentStatus1Code | 1638 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecuritiesPaymentStatus5Choice | 1645 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecuritiesRTGS4Choice | 1651 |
| [type-0207](types/type-0207.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecuritiesSettlementTransactionGenerationNotificationV13 | 1657 |
| [type-0208](types/type-0208.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecuritiesTradeDetails153 | 1680 |
| [type-0209](types/type-0209.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecuritiesTransactionType26Code | 1707 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecuritiesTransactionType44Choice | 1755 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SecurityIdentification19 | 1761 |
| [type-0212](types/type-0212.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementDate17Choice | 1768 |
| [type-0213](types/type-0213.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementDate4Code | 1774 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementDateCode7Choice | 1779 |
| [type-0215](types/type-0215.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementDetails225 | 1785 |
| [type-0216](types/type-0216.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementParties126 | 1819 |
| [type-0217](types/type-0217.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementStatus32Choice | 1829 |
| [type-0218](types/type-0218.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementSystemMethod1Code | 1836 |
| [type-0219](types/type-0219.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementSystemMethod4Choice | 1842 |
| [type-0220](types/type-0220.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementTransactionCondition19Code | 1848 |
| [type-0221](types/type-0221.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementTransactionCondition44Choice | 1876 |
| [type-0222](types/type-0222.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementTransactionCondition5Code | 1882 |
| [type-0223](types/type-0223.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlementTypeAndIdentification29 | 1890 |
| [type-0224](types/type-0224.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlingCapacity2Code | 1905 |
| [type-0225](types/type-0225.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SettlingCapacity7Choice | 1913 |
| [type-0226](types/type-0226.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}StatusAndReason50 | 1919 |
| [type-0227](types/type-0227.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SupplementaryData1 | 1927 |
| [type-0228](types/type-0228.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}SupplementaryDataEnvelope1 | 1933 |
| [type-0229](types/type-0229.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TaxCapacityParty4Choice | 1938 |
| [type-0230](types/type-0230.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TaxLiability1Code | 1944 |
| [type-0231](types/type-0231.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TotalNumber2 | 1950 |
| [type-0232](types/type-0232.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}Tracking4Choice | 1956 |
| [type-0233](types/type-0233.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TradeDate8Choice | 1962 |
| [type-0234](types/type-0234.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TradeDateCode3Choice | 1968 |
| [type-0235](types/type-0235.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TradeOriginator3Choice | 1974 |
| [type-0236](types/type-0236.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TradeTransactionCondition4Code | 1980 |
| [type-0237](types/type-0237.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TradeTransactionCondition5Choice | 2006 |
| [type-0238](types/type-0238.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TypeOfIdentification1Code | 2012 |
| [type-0239](types/type-0239.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TypeOfPrice14Code | 2023 |
| [type-0240](types/type-0240.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}TypeOfPrice29Choice | 2028 |
| [type-0241](types/type-0241.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}UTIIdentifier | 2034 |
| [type-0242](types/type-0242.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}UnmatchedReason11Code | 2039 |
| [type-0243](types/type-0243.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}UnmatchedReason15 | 2083 |
| [type-0244](types/type-0244.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}UnmatchedReason21Choice | 2089 |
| [type-0245](types/type-0245.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}UnmatchedStatus16Choice | 2095 |
| [type-0246](types/type-0246.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}YesNoIndicator | 2101 |
| [type-0247](types/type-0247.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}YieldedOrValueType1Choice | 2104 |
| [type-0248](types/type-0248.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.032.001.13}YieldedOrValueType2Choice | 2110 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 89 |
| complexType | 158 |
| element | 560 |
| enumeration | 502 |
| extension | 3 |
| fractionDigits | 9 |
| maxLength | 8 |
| minInclusive | 4 |
| minLength | 8 |
| pattern | 17 |
| restriction | 89 |
| schema | 1 |
| sequence | 66 |
| simpleContent | 3 |
| simpleType | 89 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
