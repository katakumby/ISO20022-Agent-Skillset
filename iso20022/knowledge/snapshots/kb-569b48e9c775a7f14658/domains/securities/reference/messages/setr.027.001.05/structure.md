---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.027.001.05"
message_family: "setr.027"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.027.001.05"
source_ids: ["src-000184"]
source_editions: ["2024-2025"]
---

# setr.027.001.05 structure

[src-000184](../../../../../raw-input/post_trade_matching/setr.027.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.027.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.027.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AccountIdentification55Choice | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ActiveCurrencyAndAmount_SimpleType | 13 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ActiveCurrencyAndAmount | 20 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ActiveCurrencyCode | 27 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 32 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount | 39 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ActiveOrHistoricCurrencyAndAmount_SimpleType | 46 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ActiveOrHistoricCurrencyAndAmount | 53 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ActiveOrHistoricCurrencyCode | 60 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AddressType2Code | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Agreement5 | 75 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AlternatePartyIdentification10 | 86 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AlternatePartyIdentification8 | 93 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AmountAndDirection28 | 100 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AmountAndDirection29 | 111 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AmountAndDirection5 | 119 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AmountOrPercentageRange1 | 125 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AmountOrRate1Choice | 131 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AmountOrRate2Choice | 137 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AnyBICDec2014Identifier | 143 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Appearance1Code | 148 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AutoBorrowing1Code | 160 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}AutomaticBorrowing6Choice | 167 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BBANIdentifier | 173 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BICNonFIDec2014Identifier | 178 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BaseOneRate | 183 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BeneficialOwnership4Choice | 189 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BlockTrade1Code | 195 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BlockTrade4Choice | 201 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BorrowingReason1Code | 207 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BorrowingReason2Choice | 214 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BusinessProcessType1Code | 220 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}BusinessProcessType2Choice | 232 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CFIOct2015Identifier | 238 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CalculationType1Code | 243 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CallIn1Code | 280 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CashAccountIdentification5Choice | 287 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CashMarginOrder1Code | 293 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CashParties33 | 300 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CashSettlementSystem2Code | 309 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CashSettlementSystem4Choice | 315 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CentralCounterPartyEligibility4Choice | 321 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ChargeTaxBasis1Code | 327 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ChargeTaxBasisType2Choice | 333 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ClassificationType32Choice | 339 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Clearing5 | 345 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ClearingAccountType1Code | 351 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ClearingSide1Code | 358 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ClosingDate4Choice | 366 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ClosingType1Code | 372 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CollateralType3Code | 380 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CollateralType4Choice | 392 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Commission24 | 398 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CommissionType6Choice | 409 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CommissionType9Code | 415 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ConfirmationParties6 | 430 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ConfirmationPartyDetails10 | 448 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ConfirmationPartyDetails7 | 459 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ConfirmationPartyDetails8 | 469 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ConfirmationPartyDetails9 | 477 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CountryCode | 486 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CreditDebitCode | 491 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}CurrencyToBuyOrSell1Choice | 497 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Date3Choice | 503 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DateAndDateTime1Choice | 509 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DateAndDateTime2Choice | 515 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DateTimePeriod1 | 521 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DateTimePeriod1Choice | 527 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DateTimePeriod2 | 534 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DateType2Code | 540 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DateType3Code | 545 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DecimalNumber | 550 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DeliveryReceiptType2Code | 556 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DeliveryType2Code | 562 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Document | 570 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}DocumentNumber17Choice | 575 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}EUCapitalGain2Code | 582 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}EUCapitalGainType3Choice | 589 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Eligibility1Code | 595 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}EventFrequency3Code | 602 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Exact3NumericText | 611 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Exact4AlphaNumericText | 616 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Exact4NumericText | 621 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ExposureType18Choice | 626 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ExposureType3Code | 632 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ExternalFinancialInstrumentIdentificationType1Code | 666 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ExternalTradeTransactionCondition1Code | 672 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}FXStandingInstruction4Choice | 678 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}FinancialInstrumentAttributes124 | 684 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}FinancialInstrumentQuantity18Choice | 740 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}FinancialInstrumentQuantity1Choice | 746 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}FinancialInstrumentStipulations4 | 753 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ForeignExchangeTerms18 | 798 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}FormOfSecurity1Code | 806 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}FormOfSecurity6Choice | 812 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Frequency1Code | 818 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Frequency23Choice | 830 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}FutureAndOptionContractType1Code | 836 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}FutureOrOptionDetails3 | 843 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}GenericIdentification1 | 867 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}GenericIdentification30 | 874 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}GenericIdentification36 | 881 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}GenericIdentification37 | 888 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}GenericIdentification7 | 894 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}IBAN2007Identifier | 900 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ISINOct2015Identifier | 905 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ISO20022MessageIdentificationText | 910 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ISODate | 915 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ISODateTime | 918 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ISOYearMonth | 921 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}IdentificationReference15Choice | 924 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}IdentificationSource3Choice | 942 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}IdentificationType42Choice | 948 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}IdentificationType43Choice | 954 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ImpliedCurrencyAndAmount | 960 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}InterestComputationMethod1Code | 967 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}InterestComputationMethod2Code | 985 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}InterestComputationMethod3Choice | 1004 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}InterestComputationMethodFormat4Choice | 1010 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}InterestType2Code | 1016 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}InvestorCapacity4Choice | 1022 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}LegalFramework1Code | 1028 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}LendingTransactionMethod1Code | 1033 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}LendingTransactionMethod2Choice | 1039 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}LetterOfGuarantee4Choice | 1045 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Linkages76 | 1051 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MICIdentifier | 1057 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MarketClientSide1Code | 1062 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MarketClientSide6Choice | 1068 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MarketIdentification3Choice | 1074 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MarketIdentification93 | 1080 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MarketIdentification97 | 1086 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MarketType18Choice | 1092 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MarketType2Code | 1098 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MarketType6Code | 1107 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MarketType8Choice | 1114 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MatchingStatus1Code | 1120 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}MatchingStatus27Choice | 1126 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max140Text | 1132 |
| [type-0141](types/type-0141.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max16Text | 1138 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max256Text | 1144 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max34Text | 1150 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max350Text | 1156 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max35Text | 1162 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max3Number | 1168 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max3NumericText | 1174 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max4NumericText | 1179 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max70Text | 1184 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Max8Text | 1190 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}ModificationCancellationAllowed4Choice | 1196 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}NameAndAddress13 | 1202 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}NameAndAddress5 | 1208 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}NettingEligibility4Choice | 1214 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Number | 1220 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Number1Choice | 1226 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Number24Choice | 1232 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}NumberCount1Choice | 1238 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Operation1Code | 1244 |
| [type-0160](types/type-0160.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Operator1Code | 1251 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OptionRight1Code | 1260 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OptionRight2Choice | 1268 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OptionStyle10Choice | 1274 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OptionStyle4Code | 1280 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OptionType1Code | 1287 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OptionType6Choice | 1293 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Order24 | 1299 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OriginalAndCurrentQuantities1 | 1346 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OtherAmounts16 | 1352 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OtherIdentification1 | 1396 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OtherParties32 | 1403 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OtherPrices5 | 1412 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}OwnershipLegalRestrictions1Code | 1431 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartialFill4 | 1438 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentification116Choice | 1450 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentification117 | 1457 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentification117Choice | 1464 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentification118 | 1471 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentification127Choice | 1478 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentification245Choice | 1484 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentificationAndAccount148 | 1491 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentificationAndAccount149 | 1502 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentificationAndAccount150 | 1512 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentificationAndAccount151 | 1523 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentificationAndAccount152 | 1532 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentificationAndAccount154 | 1540 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyIdentificationAndAccount155 | 1550 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyTextInformation1 | 1558 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyTextInformation2 | 1565 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PartyTextInformation5 | 1571 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PercentageRate | 1577 |
| [type-0192](types/type-0192.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PlusOrMinusIndicator | 1583 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PositionEffect2Code | 1586 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PostalAddress1 | 1595 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PostalAddress8 | 1607 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Price14 | 1619 |
| [type-0197](types/type-0197.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PriceInformation28 | 1625 |
| [type-0198](types/type-0198.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PriceRateOrAmount3Choice | 1633 |
| [type-0199](types/type-0199.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PriceValueType7Code | 1639 |
| [type-0200](types/type-0200.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PriorityNumeric4Choice | 1656 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}PurposeCode9Choice | 1662 |
| [type-0202](types/type-0202.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Quantity6Choice | 1668 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}QuantityBreakdown76 | 1674 |
| [type-0204](types/type-0204.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}QuantityOrAmount2Choice | 1682 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Rate2 | 1688 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RateName1 | 1694 |
| [type-0207](types/type-0207.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RateOrAbsoluteValue1Choice | 1700 |
| [type-0208](types/type-0208.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RateOrName1Choice | 1706 |
| [type-0209](types/type-0209.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RateType1Code | 1712 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RateType35Choice | 1719 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Rating1 | 1725 |
| [type-0212](types/type-0212.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RatingValueIdentifier | 1732 |
| [type-0213](types/type-0213.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Registration1Code | 1735 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Registration9Choice | 1741 |
| [type-0215](types/type-0215.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RegistrationParameters3 | 1747 |
| [type-0216](types/type-0216.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RegulatoryStipulations1 | 1755 |
| [type-0217](types/type-0217.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Reporting2Code | 1761 |
| [type-0218](types/type-0218.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Reporting6Choice | 1768 |
| [type-0219](types/type-0219.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RepurchaseType22Choice | 1774 |
| [type-0220](types/type-0220.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}RepurchaseType9Code | 1780 |
| [type-0221](types/type-0221.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Restriction5Choice | 1792 |
| [type-0222](types/type-0222.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Revaluation3Choice | 1798 |
| [type-0223](types/type-0223.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Reversible1Code | 1804 |
| [type-0224](types/type-0224.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Reversible2Choice | 1811 |
| [type-0225](types/type-0225.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecuritiesAccount20 | 1817 |
| [type-0226](types/type-0226.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecuritiesAccount35 | 1824 |
| [type-0227](types/type-0227.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecuritiesAccountPurposeType1Code | 1831 |
| [type-0228](types/type-0228.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecuritiesCertificate3 | 1841 |
| [type-0229](types/type-0229.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecuritiesFinancing12 | 1848 |
| [type-0230](types/type-0230.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecuritiesLendingType1Code | 1892 |
| [type-0231](types/type-0231.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecuritiesLendingType2Choice | 1899 |
| [type-0232](types/type-0232.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecuritiesRTGS4Choice | 1905 |
| [type-0233](types/type-0233.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecuritiesTradeConfirmationV05 | 1911 |
| [type-0234](types/type-0234.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SecurityIdentification19 | 1937 |
| [type-0235](types/type-0235.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementDate16Choice | 1944 |
| [type-0236](types/type-0236.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementDate5Code | 1950 |
| [type-0237](types/type-0237.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementDateCode12Choice | 1967 |
| [type-0238](types/type-0238.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementDetails213 | 1973 |
| [type-0239](types/type-0239.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementInstructionGeneration1Code | 2007 |
| [type-0240](types/type-0240.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementInstructionGeneration2Choice | 2013 |
| [type-0241](types/type-0241.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementParties59 | 2019 |
| [type-0242](types/type-0242.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementStandingInstructionDatabase1Code | 2029 |
| [type-0243](types/type-0243.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementStandingInstructionDatabase4Choice | 2036 |
| [type-0244](types/type-0244.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementSystemMethod1Code | 2042 |
| [type-0245](types/type-0245.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementSystemMethod4Choice | 2048 |
| [type-0246](types/type-0246.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementTransactionCondition31Choice | 2054 |
| [type-0247](types/type-0247.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementTransactionCondition7Code | 2060 |
| [type-0248](types/type-0248.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementTransactionType3Choice | 2078 |
| [type-0249](types/type-0249.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlementTransactionType7Code | 2084 |
| [type-0250](types/type-0250.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlingCapacity1Code | 2122 |
| [type-0251](types/type-0251.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SettlingCapacity9Choice | 2129 |
| [type-0252](types/type-0252.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Side3Code | 2135 |
| [type-0253](types/type-0253.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SimpleIdentificationInformation2 | 2155 |
| [type-0254](types/type-0254.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SpreadRate1 | 2160 |
| [type-0255](types/type-0255.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}StandingSettlementInstruction13 | 2166 |
| [type-0256](types/type-0256.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SupplementaryData1 | 2174 |
| [type-0257](types/type-0257.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}SupplementaryDataEnvelope1 | 2180 |
| [type-0258](types/type-0258.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TaxCapacityParty4Choice | 2185 |
| [type-0259](types/type-0259.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TaxLiability1Code | 2191 |
| [type-0260](types/type-0260.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Term1 | 2197 |
| [type-0261](types/type-0261.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TotalNumber1 | 2203 |
| [type-0262](types/type-0262.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}Tracking4Choice | 2209 |
| [type-0263](types/type-0263.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradeDate7Choice | 2215 |
| [type-0264](types/type-0264.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradeDate8Choice | 2221 |
| [type-0265](types/type-0265.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradeDateCode3Choice | 2227 |
| [type-0266](types/type-0266.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradeRegulatoryConditions1Code | 2233 |
| [type-0267](types/type-0267.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradeTransactionCondition2Code | 2239 |
| [type-0268](types/type-0268.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradeTransactionCondition9Choice | 2256 |
| [type-0269](types/type-0269.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradeType3Code | 2262 |
| [type-0270](types/type-0270.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradeType4Choice | 2290 |
| [type-0271](types/type-0271.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradingCapacity4Code | 2296 |
| [type-0272](types/type-0272.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradingCapacity6Code | 2315 |
| [type-0273](types/type-0273.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradingDate1Code | 2326 |
| [type-0274](types/type-0274.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradingDateCode2Choice | 2331 |
| [type-0275](types/type-0275.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradingPartyCapacity3Choice | 2337 |
| [type-0276](types/type-0276.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TradingPartyCapacity4Choice | 2343 |
| [type-0277](types/type-0277.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TransactiontIdentification4 | 2349 |
| [type-0278](types/type-0278.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TwoLegTransactionDetails5 | 2354 |
| [type-0279](types/type-0279.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TwoLegTransactionType4Choice | 2369 |
| [type-0280](types/type-0280.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TypeOfIdentification1Code | 2375 |
| [type-0281](types/type-0281.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TypeOfIdentification2Code | 2386 |
| [type-0282](types/type-0282.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TypeOfPrice3Code | 2395 |
| [type-0283](types/type-0283.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}TypeOfPrice47Choice | 2406 |
| [type-0284](types/type-0284.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}UPICIdentifier | 2412 |
| [type-0285](types/type-0285.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}UTIIdentifier | 2417 |
| [type-0286](types/type-0286.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}UnderlyingFinancialInstrument7 | 2422 |
| [type-0287](types/type-0287.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}UnderlyingRatio2 | 2428 |
| [type-0288](types/type-0288.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}UnitOfMeasure1Code | 2435 |
| [type-0289](types/type-0289.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}YesNoIndicator | 2474 |
| [type-0290](types/type-0290.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.027.001.05}YieldCalculation7 | 2477 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 91 |
| complexType | 175 |
| element | 779 |
| enumeration | 484 |
| extension | 3 |
| fractionDigits | 9 |
| maxLength | 10 |
| minInclusive | 4 |
| minLength | 10 |
| pattern | 18 |
| restriction | 114 |
| schema | 1 |
| sequence | 81 |
| simpleContent | 3 |
| simpleType | 114 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
