---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.011.001.10"
message_family: "sese.011"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.011.001.10"
source_ids: ["src-000130"]
source_editions: ["2025-2026"]
---

# sese.011.001.10 structure

[src-000130](../../../../../raw-input/investment_funds/sese.011.001.10.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.011.001.10`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.011.001.10 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Account34 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Account36 | 14 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}AccountIdentificationAndName9 | 26 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}AccountSchemeName1Choice | 34 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveCurrencyAnd13DecimalAmount_SimpleType | 40 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveCurrencyAnd13DecimalAmount | 47 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveCurrencyAndAmount_SimpleType | 54 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveCurrencyAndAmount | 61 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveCurrencyCode | 68 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 73 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount | 80 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveOrHistoricCurrencyAndAmount_SimpleType | 87 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveOrHistoricCurrencyAndAmount | 94 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ActiveOrHistoricCurrencyCode | 101 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}AdditionalInformation15 | 106 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}AdditionalReference10 | 112 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}AddressType2Code | 119 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}AlternateSecurityIdentification7 | 129 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}AnyBICDec2014Identifier | 135 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ApplicableRules1Choice | 140 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ApplicableRules1Code | 146 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}AustrianBankleitzahlIdentifier | 152 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}BICFIDec2014Identifier | 157 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}BelgianIdentifier | 162 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}BeneficiaryDrawdown2 | 165 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}BeneficiaryType1Choice | 174 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}BeneficiaryType1Code | 180 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}BenefitCrystallisationEvent2 | 187 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}BlockChainAddressWallet3 | 198 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Bloomberg2Identifier | 205 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}BranchData2 | 210 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CFIOct2015Identifier | 217 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CHIPSParticipantIdentifier | 222 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CHIPSUniversalIdentifier | 227 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CUSIPIdentifier | 232 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CanadianPaymentsARNIdentifier | 235 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CancellationPendingStatus7Choice | 240 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CancelledStatus13Choice | 247 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CancelledStatusReason3Code | 255 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Capped1 | 262 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CashAsset3 | 271 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CashAssetType1Choice | 279 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CashAssetType1Code | 285 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ChargeBasis2Choice | 291 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ChargeOrCommissionDiscount1 | 297 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ChargeType10Choice | 304 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Cheque12 | 310 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ClassificationType32Choice | 318 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ClearingSystemMemberIdentification2Choice | 324 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ClearingSystemMemberIdentification4Choice | 351 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ConsolidatedTapeAssociationIdentifier | 374 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ContactIdentification2 | 380 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Conversion4 | 391 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CountryCode | 399 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}CreditTransfer13 | 404 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}DTI2024Identifier | 420 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}DateFormat42Choice | 425 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}DecimalNumber | 431 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}DigitalPaymentSettlement3 | 437 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Document | 444 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Drawdown04 | 449 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Drawdown3 | 470 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}DrawdownType2Choice | 476 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}DrawdownType2Code | 482 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}DutchIdentifier | 489 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}EmploymentDetails1 | 492 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}EuroclearClearstreamIdentifier | 504 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Exact4AlphaNumericText | 510 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Extended350Code | 515 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Extension1 | 521 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ExtensiveBranchNetworkIdentifier | 527 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ExternalAccountIdentification1Code | 532 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FailedSettlementStatus2Choice | 538 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FedwireRoutingNumberIdentifier | 545 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Fee11 | 550 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FinancialInstitutionIdentification10Choice | 564 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FinancialInstitutionIdentification16 | 572 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FinancialInstitutionIdentification17 | 582 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FinancialInstrument101Choice | 588 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FinancialInstrumentIdentification6 | 595 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FinancialInstrumentIdentification7 | 603 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FinancialInstrumentIdentificationType1Code | 610 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}FinancialInstrumentQuantity33Choice | 638 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}GenericAccountIdentification1 | 646 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}GenericIdentification1 | 653 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}GenericIdentification30 | 660 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}GenericIdentification36 | 667 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}GenericIdentification47 | 674 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}GermanBankleitzahlIdentifier | 681 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}HellenicBankIdentificationCodeIdentifier | 686 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}HongKongBankIdentifier | 691 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}IBAN2007Identifier | 696 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ISINOct2015Identifier | 701 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ISODate | 706 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ISODateTime | 709 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ISOYearMonth | 712 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}IdentificationSource1Choice | 715 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}IdentificationSource6Choice | 721 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ImpliedCurrencyAndAmount | 727 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}InRepairStatus4Choice | 734 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}IndianFinancialSystemCodeIdentifier | 741 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Intermediary48 | 746 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}InvestmentFundFee3Code | 754 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}InvestmentFundRole8Code | 777 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}IrishNSCIdentifier | 795 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ItalianDomesticIdentifier | 800 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}LEIIdentifier | 805 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}MarketPracticeVersion1 | 810 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Max140Text | 817 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Max16Text | 823 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Max256Text | 829 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Max30DecimalNumber | 835 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Max34Text | 841 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Max350Text | 847 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Max35Text | 853 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Max4AlphaNumericText | 859 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Max70Text | 866 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}MessageIdentification1 | 872 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}NameAndAddress5 | 878 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}NamePrefix1Code | 884 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}NewZealandNCCIdentifier | 892 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}NoReasonCode | 897 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Number | 902 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}OtherAmount1 | 908 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}OtherAmountType1Choice | 914 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}OtherAmountType1Code | 920 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}OtherAsset2 | 926 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}OtherAsset2Choice | 936 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}OtherAsset2Code | 942 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}OtherIdentification8 | 951 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PartyIdentification125Choice | 958 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PartyIdentification132 | 965 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PartyIdentification139 | 974 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PaymentInstrument23 | 980 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PaymentInstrument31Choice | 988 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PendingSettlementStatus3Choice | 994 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PendingSettlementStatusReason2Code | 1002 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PercentageRate | 1043 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PersonIdentificationType7Code | 1049 |
| [type-0141](types/type-0141.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PhoneNumber | 1056 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PolishNationalClearingCodeIdentifier | 1061 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PortugueseNCCIdentifier | 1066 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PostalAddress1 | 1071 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PostalAddress6 | 1083 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PriceMethod1Code | 1097 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}PriceValue1 | 1103 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ProprietaryQuantity8 | 1108 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}QUICKIdentifier | 1116 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Quantity48Choice | 1119 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}RICIdentifier | 1125 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}References64Choice | 1131 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}RejectedReason45Choice | 1137 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}RejectedStatusReason13Code | 1143 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}RejectionReason56 | 1194 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ReversedStatus2Choice | 1200 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Role8Choice | 1207 |
| [type-0158](types/type-0158.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}RussianCentralBankIdentificationCodeIdentifier | 1213 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SEDOLIdentifier | 1218 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SecurityIdentification46Choice | 1221 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SecurityIdentification50 | 1241 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SicovamIdentifier | 1248 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SmallNetworkIdentifier | 1251 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SouthAfricanNCCIdentifier | 1256 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SpanishDomesticInterbankingIdentifier | 1261 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SubAccount5 | 1266 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SwissBCIdentifier | 1273 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}SwissSICIdentifier | 1278 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Tax35 | 1283 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxBasis1Choice | 1293 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxCalculationInformation10 | 1299 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxReference2 | 1305 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxReferenceType1Choice | 1311 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxType17Code | 1317 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxType3Choice | 1339 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxableIncomePerShareCalculated2Choice | 1345 |
| [type-0177](types/type-0177.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxableIncomePerShareCalculated2Code | 1351 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxationBasis2Code | 1358 |
| [type-0179](types/type-0179.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TaxationBasis5Code | 1364 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TickerIdentifier | 1373 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TotalFeesAndTaxes44 | 1379 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TransferInstructionStatus5 | 1390 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TransferInstructionStatusReportV10 | 1396 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TransferStatus5Choice | 1406 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TransferStatus6Code | 1419 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TransferStatusAndReason09 | 1431 |
| [type-0187](types/type-0187.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TransferStatusType2Code | 1462 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TransferStatusType3Choice | 1477 |
| [type-0189](types/type-0189.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TransferUnmatchedReason3Code | 1483 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TransferUnmatchedStatus4Choice | 1498 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TypeOfPrice10Code | 1506 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}TypeOfPrice46Choice | 1522 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}UKDomesticSortCodeIdentifier | 1528 |
| [type-0194](types/type-0194.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}UKTaxGroupUnit1Code | 1533 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Unit14 | 1539 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Unit15 | 1552 |
| [type-0197](types/type-0197.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}Unit1Choice | 1562 |
| [type-0198](types/type-0198.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}UnitPrice23 | 1568 |
| [type-0199](types/type-0199.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}ValorenIdentifier | 1579 |
| [type-0200](types/type-0200.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}WaivingInstruction1Code | 1582 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}WaivingInstruction2Choice | 1588 |
| [type-0202](types/type-0202.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}WertpapierIdentifier | 1594 |
| [type-0203](types/type-0203.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.011.001.10}YesNoIndicator | 1597 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 4 |
| choice | 41 |
| complexType | 105 |
| element | 450 |
| enumeration | 251 |
| extension | 4 |
| fractionDigits | 9 |
| maxLength | 14 |
| minInclusive | 5 |
| minLength | 14 |
| pattern | 36 |
| restriction | 97 |
| schema | 1 |
| sequence | 60 |
| simpleContent | 4 |
| simpleType | 97 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/381c0350a1d0471dd4e5c25e.md) · [Message](index.md)
