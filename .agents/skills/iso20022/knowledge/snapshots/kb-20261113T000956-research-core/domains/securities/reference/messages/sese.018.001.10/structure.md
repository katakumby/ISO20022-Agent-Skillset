---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.018.001.10"
message_family: "sese.018"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.018.001.10"
source_ids: ["src-000134"]
source_editions: ["2025-2026"]
---

# sese.018.001.10 structure

[src-000134](../../../../../raw-input/investment_funds/sese.018.001.10.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.018.001.10`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.018.001.10 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Account27 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Account37 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AccountHoldingInformationV10 | 22 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AccountOwnershipType6Code | 43 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveCurrencyAnd13DecimalAmount_SimpleType | 68 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveCurrencyAnd13DecimalAmount | 75 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveCurrencyAndAmount_SimpleType | 82 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveCurrencyAndAmount | 89 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveCurrencyCode | 96 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 101 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount | 108 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveOrHistoricCurrencyAndAmount_SimpleType | 115 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveOrHistoricCurrencyAndAmount | 122 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ActiveOrHistoricCurrencyCode | 129 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AdditionalInformation15 | 134 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AdditionalReference10 | 140 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AdditionalReference11 | 147 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AddressType2Code | 154 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AlternatePartyIdentification7 | 164 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AlternateSecurityIdentification7 | 171 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AnyBICDec2014Identifier | 177 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}AustrianBankleitzahlIdentifier | 182 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}BelgianIdentifier | 187 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}BlockChainAddressWallet3 | 190 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Bloomberg2Identifier | 197 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}BonusWithdrawal2 | 202 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}BusinessFlowDirectionType1Code | 213 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}BusinessFlowType1Code | 219 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}CFIOct2015Identifier | 226 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}CHIPSParticipantIdentifier | 231 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}CHIPSUniversalIdentifier | 236 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}CUSIPIdentifier | 241 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}CanadianPaymentsARNIdentifier | 244 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}CashAsset2 | 249 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}CashAssetType1Choice | 256 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}CashAssetType1Code | 262 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ChargeBasis2Choice | 268 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ChargeOrCommissionDiscount1 | 274 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ChargeType10Choice | 281 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ClassificationType32Choice | 287 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ClearingSystemMemberIdentification2Choice | 293 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ConsolidatedTapeAssociationIdentifier | 320 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ContactIdentification2 | 326 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}CountryCode | 337 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Crystallisation2 | 342 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DTI2024Identifier | 352 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DateAndAmount2 | 357 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DateAndDateTime2Choice | 363 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DateQuarter1Choice | 369 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DecimalNumber | 375 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DigitalPaymentSettlement3 | 381 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Document | 388 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DrawdownStatus1Choice | 393 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DrawdownStatus1Code | 399 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DrawdownType2Choice | 406 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DrawdownType2Code | 412 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}DutchIdentifier | 419 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}EuroclearClearstreamIdentifier | 422 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Exact4AlphaNumericText | 428 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Extension1 | 433 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ExtensiveBranchNetworkIdentifier | 439 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}FedwireRoutingNumberIdentifier | 444 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Fee11 | 449 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}FinancialInstrument102Choice | 463 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}FinancialInstrument110 | 470 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}FinancialInstrumentIdentification8 | 495 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}FinancialInstrumentIdentification9 | 505 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}FinancialInstrumentIdentificationType1Code | 514 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}FinancialInstrumentQuantity33Choice | 542 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}FundPortfolio7Choice | 550 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}FundSettlementParameters24 | 557 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GenderCode | 567 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GeneralInvestment2 | 573 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GeneralInvestmentAccountType2Choice | 582 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GeneralInvestmentAccountType2Code | 588 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GenericIdentification1 | 594 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GenericIdentification30 | 601 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GenericIdentification36 | 608 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GenericIdentification47 | 615 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GenericIdentification78 | 622 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}GermanBankleitzahlIdentifier | 628 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}HellenicBankIdentificationCodeIdentifier | 633 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}HolderType1Code | 638 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}HongKongBankIdentifier | 644 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ISINOct2015Identifier | 649 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ISODate | 654 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ISODateTime | 657 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ISOYear | 660 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ISOYearMonth | 663 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}IdentificationSource1Choice | 666 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}IdentificationSource6Choice | 672 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}IdentificationType42Choice | 678 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ImpliedCurrencyAndAmount | 684 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}IndianFinancialSystemCodeIdentifier | 691 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}IndividualPerson8 | 696 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}InnovativeFinance1 | 708 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Intermediary43 | 714 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}InvestmentAccount69 | 722 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}InvestmentFundFee3Code | 730 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}InvestmentFundRole2Code | 753 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}IrishNSCIdentifier | 766 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ItalianDomesticIdentifier | 771 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}LEIIdentifier | 776 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}LumpSumType1Choice | 781 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}LumpSumType1Code | 787 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}MarketPracticeVersion1 | 794 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Max140Text | 801 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Max16Text | 807 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Max256Text | 813 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Max30DecimalNumber | 819 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Max350Text | 825 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Max35Text | 831 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Max4AlphaNumericText | 837 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Max70Text | 844 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}MessageIdentification1 | 850 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}MoneyPurchaseAnnualAllowance1 | 856 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}NameAndAddress5 | 862 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}NamePrefix1Code | 868 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}NewZealandNCCIdentifier | 876 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Number | 881 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Organisation36 | 887 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}OtherAmount1 | 900 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}OtherAmount3 | 906 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}OtherAmountType1Choice | 912 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}OtherAmountType1Code | 918 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}OtherAsset2 | 924 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}OtherAsset2Choice | 934 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}OtherAsset2Code | 940 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}OtherIdentification8 | 949 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyIdentification123Choice | 956 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyIdentification125Choice | 963 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyIdentification126Choice | 970 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyIdentification132 | 976 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyIdentification139 | 985 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyIdentification140 | 991 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyIdentification257Choice | 997 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyIdentification315 | 1005 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyIdentificationAndAccount194 | 1015 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyTextInformation1 | 1026 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PartyTextInformation6 | 1033 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Pension5 | 1041 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PensionOrder1 | 1073 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PensionOrderType1Choice | 1079 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PensionOrderType1Code | 1085 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PensionPolicy1 | 1091 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PensionSchemeType3Choice | 1098 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PensionSchemeType3Code | 1104 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PensionTransferScope1Choice | 1128 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PensionTransferScope1Code | 1134 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PercentageRate | 1142 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PersonIdentificationType7Code | 1148 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PhoneNumber | 1155 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PolishNationalClearingCodeIdentifier | 1160 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PortfolioTransfer16 | 1165 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PortfolioWithdrawalReason1Code | 1178 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PortugueseNCCIdentifier | 1183 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PostalAddress1 | 1188 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PreviousAll | 1200 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PreviousYear1Choice | 1205 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PreviousYear4 | 1211 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PriceMethod1Code | 1217 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}PriceValue1 | 1223 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ProprietaryQuantity8 | 1228 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}QUICKIdentifier | 1236 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Quantity48Choice | 1239 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Quantity53 | 1245 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}RICIdentifier | 1255 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ResidualCash1 | 1261 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Role4Choice | 1267 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}RussianCentralBankIdentificationCodeIdentifier | 1273 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SEDOLIdentifier | 1278 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SafekeepingPlace1Code | 1281 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SafekeepingPlace2Code | 1289 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SafekeepingPlaceFormat42Choice | 1295 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SafekeepingPlaceTypeAndIdentification1 | 1304 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SafekeepingPlaceTypeAndText6 | 1310 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SecuritiesAccount19 | 1316 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SecurityIdentification46Choice | 1323 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SecurityIdentification50 | 1343 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SettlementParties131 | 1350 |
| [type-0182](types/type-0182.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SettlementTransactionCondition11Code | 1360 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SettlementTransactionCondition30Choice | 1365 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SicovamIdentifier | 1371 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SmallNetworkIdentifier | 1374 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SouthAfricanNCCIdentifier | 1379 |
| [type-0187](types/type-0187.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SpanishDomesticInterbankingIdentifier | 1384 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SubAccount5 | 1389 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SubscriptionInformation2 | 1396 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SwissBCIdentifier | 1404 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}SwissSICIdentifier | 1409 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Tax35 | 1414 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Tax36 | 1424 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxBasis1Choice | 1430 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxCalculationInformation10 | 1436 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxEfficientProduct7 | 1442 |
| [type-0197](types/type-0197.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxEfficientProductType2Choice | 1469 |
| [type-0198](types/type-0198.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxEfficientProductType2Code | 1475 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxReference1 | 1492 |
| [type-0200](types/type-0200.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxReference2 | 1499 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxReferenceParty1Choice | 1505 |
| [type-0202](types/type-0202.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxReferenceType1Choice | 1511 |
| [type-0203](types/type-0203.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxType17Code | 1517 |
| [type-0204](types/type-0204.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxType3Choice | 1539 |
| [type-0205](types/type-0205.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxWrapperAmountType1Code | 1545 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxableIncomePerShareCalculated2Choice | 1551 |
| [type-0207](types/type-0207.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxableIncomePerShareCalculated2Code | 1557 |
| [type-0208](types/type-0208.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxationBasis2Code | 1564 |
| [type-0209](types/type-0209.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TaxationBasis5Code | 1570 |
| [type-0210](types/type-0210.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TickerIdentifier | 1579 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TotalFeesAndTaxes44 | 1585 |
| [type-0212](types/type-0212.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TradeTransactionCondition5Code | 1596 |
| [type-0213](types/type-0213.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TradeTransactionCondition8Choice | 1602 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TypeOfAmount1Choice | 1608 |
| [type-0215](types/type-0215.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TypeOfIdentification1Code | 1614 |
| [type-0216](types/type-0216.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TypeOfPrice10Code | 1625 |
| [type-0217](types/type-0217.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}TypeOfPrice46Choice | 1641 |
| [type-0218](types/type-0218.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}UKDomesticSortCodeIdentifier | 1647 |
| [type-0219](types/type-0219.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}UKTaxGroupUnit1Code | 1652 |
| [type-0220](types/type-0220.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Unit14 | 1658 |
| [type-0221](types/type-0221.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}Unit1Choice | 1671 |
| [type-0222](types/type-0222.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}UnitPrice23 | 1677 |
| [type-0223](types/type-0223.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}ValorenIdentifier | 1688 |
| [type-0224](types/type-0224.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}WaivingInstruction1Code | 1691 |
| [type-0225](types/type-0225.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}WaivingInstruction2Choice | 1697 |
| [type-0226](types/type-0226.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}WertpapierIdentifier | 1703 |
| [type-0227](types/type-0227.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}WithdrawalReason1Choice | 1706 |
| [type-0228](types/type-0228.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.018.001.10}YesNoIndicator | 1712 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 4 |
| choice | 44 |
| complexType | 123 |
| element | 505 |
| enumeration | 219 |
| extension | 4 |
| fractionDigits | 9 |
| maxLength | 11 |
| minInclusive | 5 |
| minLength | 11 |
| pattern | 35 |
| restriction | 104 |
| schema | 1 |
| sequence | 75 |
| simpleContent | 4 |
| simpleType | 104 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/f781f17b5ef5cdcfd8a9e470.md) · [Message](index.md)
