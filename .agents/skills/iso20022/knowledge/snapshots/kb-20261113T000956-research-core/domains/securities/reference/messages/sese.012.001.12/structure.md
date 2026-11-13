---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.012.001.12"
message_family: "sese.012"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.012.001.12"
source_ids: ["src-000131"]
source_editions: ["2025-2026"]
---

# sese.012.001.12 structure

[src-000131](../../../../../raw-input/investment_funds/sese.012.001.12.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.012.001.12`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.012.001.12 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Account27 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Account37 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AccountIdentificationAndName9 | 22 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AccountOwnershipType6Code | 30 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AccountSchemeName1Choice | 55 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ActiveCurrencyAnd13DecimalAmount_SimpleType | 61 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ActiveCurrencyAnd13DecimalAmount | 68 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ActiveCurrencyAndAmount_SimpleType | 75 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ActiveCurrencyAndAmount | 82 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ActiveCurrencyCode | 89 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ActiveOrHistoricCurrencyAndAmount_SimpleType | 94 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ActiveOrHistoricCurrencyAndAmount | 101 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ActiveOrHistoricCurrencyCode | 108 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AdditionalInformation15 | 113 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AdditionalReference10 | 119 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AdditionalReference11 | 126 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AddressType2Code | 133 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AllOtherCash1 | 143 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AlternatePartyIdentification7 | 149 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AlternateSecurityIdentification7 | 156 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AnyBICDec2014Identifier | 162 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}AustrianBankleitzahlIdentifier | 167 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}BICFIDec2014Identifier | 172 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}BelgianIdentifier | 177 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}BlockChainAddressWallet3 | 180 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Bloomberg2Identifier | 187 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}BranchData2 | 192 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}BusinessFlowType1Code | 199 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CFIOct2015Identifier | 206 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CHIPSParticipantIdentifier | 211 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CHIPSUniversalIdentifier | 216 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CUSIPIdentifier | 221 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CanadianPaymentsARNIdentifier | 224 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CashAll1 | 229 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CashAsset3 | 235 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CashAssetType1Choice | 243 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CashAssetType1Code | 249 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ChargeBasis2Choice | 255 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ChargeOrCommissionDiscount1 | 261 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ChargeType10Choice | 268 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ClassificationType32Choice | 274 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ClearingSystemMemberIdentification2Choice | 280 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ClearingSystemMemberIdentification4Choice | 307 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ConsolidatedTapeAssociationIdentifier | 330 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ContactIdentification2 | 336 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Conversion5 | 347 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CountryCode | 353 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}CreditTransfer13 | 358 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Crystallisation2 | 374 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}DTI2024Identifier | 384 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}DateAndAmount2 | 389 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}DateAndDateTime2Choice | 395 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}DateQuarter1Choice | 401 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}DecimalNumber | 407 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}DigitalPaymentSettlement3 | 413 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Document | 420 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}DutchIdentifier | 425 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}EuroclearClearstreamIdentifier | 428 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Exact4AlphaNumericText | 434 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Extension1 | 439 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ExtensiveBranchNetworkIdentifier | 445 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ExternalAccountIdentification1Code | 450 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FedwireRoutingNumberIdentifier | 456 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Fee11 | 461 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FinancialInstitutionIdentification16 | 475 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FinancialInstrument101Choice | 485 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FinancialInstrument108 | 492 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FinancialInstrumentIdentification6 | 524 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FinancialInstrumentIdentification7 | 532 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FinancialInstrumentIdentificationType1Code | 539 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FinancialInstrumentQuantity33Choice | 567 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FundPortfolio8Choice | 575 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}FundSettlementParameters24 | 582 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GenderCode | 592 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GeneralInvestment2 | 598 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GeneralInvestmentAccountType2Choice | 607 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GeneralInvestmentAccountType2Code | 613 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GenericAccountIdentification1 | 619 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GenericIdentification1 | 626 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GenericIdentification30 | 633 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GenericIdentification36 | 640 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GenericIdentification47 | 647 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GenericIdentification78 | 654 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}GermanBankleitzahlIdentifier | 660 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}HellenicBankIdentificationCodeIdentifier | 665 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}HolderType1Code | 670 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}HongKongBankIdentifier | 676 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}IBAN2007Identifier | 681 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ISINOct2015Identifier | 686 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ISODate | 691 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ISODateTime | 694 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ISOYear | 697 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ISOYearMonth | 700 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}IdentificationSource1Choice | 703 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}IdentificationSource6Choice | 709 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}IdentificationType42Choice | 715 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ImpliedCurrencyAndAmount | 721 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}IndianFinancialSystemCodeIdentifier | 728 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}IndividualPerson8 | 733 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Intermediary43 | 745 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}InvestmentAccount69 | 753 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}InvestmentFundFee3Code | 761 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}InvestmentFundRole2Code | 784 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}IrishNSCIdentifier | 797 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ItalianDomesticIdentifier | 802 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}LEIIdentifier | 807 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}MarketPracticeVersion1 | 812 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Max140Text | 819 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Max16Text | 825 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Max256Text | 831 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Max30DecimalNumber | 837 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Max34Text | 843 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Max350Text | 849 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Max35Text | 855 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Max4AlphaNumericText | 861 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Max70Text | 868 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}MessageIdentification1 | 874 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}NameAndAddress5 | 880 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}NamePrefix1Code | 886 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}NewZealandNCCIdentifier | 894 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Number | 899 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Organisation36 | 905 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}OtherAmount1 | 918 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}OtherAmountType1Choice | 924 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}OtherAmountType1Code | 930 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}OtherAsset2 | 936 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}OtherAsset2Choice | 946 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}OtherAsset2Code | 952 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}OtherIdentification8 | 961 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyIdentification123Choice | 968 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyIdentification125Choice | 975 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyIdentification126Choice | 982 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyIdentification132 | 988 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyIdentification139 | 997 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyIdentification140 | 1003 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyIdentification257Choice | 1009 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyIdentification315 | 1017 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyIdentificationAndAccount194 | 1027 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyTextInformation1 | 1038 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PartyTextInformation6 | 1045 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PaymentInstrument22 | 1053 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Pension6 | 1059 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PensionPolicy1 | 1070 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PensionSchemeType3Choice | 1077 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PensionSchemeType3Code | 1083 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PensionTransferScope1Choice | 1107 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PensionTransferScope1Code | 1113 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PercentageRate | 1121 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PersonIdentificationType7Code | 1127 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PhoneNumber | 1134 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PolishNationalClearingCodeIdentifier | 1139 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PortfolioTransfer14 | 1144 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PortfolioTransferInstructionV12 | 1159 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PortugueseNCCIdentifier | 1179 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PostalAddress1 | 1184 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PostalAddress6 | 1196 |
| [type-0158](types/type-0158.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PreviousAll | 1210 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PreviousYear1Choice | 1215 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PreviousYear4 | 1221 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PriceMethod1Code | 1227 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}PriceValue1 | 1233 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ProprietaryQuantity8 | 1238 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}QUICKIdentifier | 1246 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Quantity48Choice | 1249 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Quantity53 | 1255 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}RICIdentifier | 1265 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ResidualCash2 | 1271 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Role4Choice | 1277 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}RussianCentralBankIdentificationCodeIdentifier | 1283 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SEDOLIdentifier | 1288 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SafekeepingPlace1Code | 1291 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SafekeepingPlace2Code | 1299 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SafekeepingPlaceFormat42Choice | 1305 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SafekeepingPlaceTypeAndIdentification1 | 1314 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SafekeepingPlaceTypeAndText6 | 1320 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SecuritiesAccount19 | 1326 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SecurityIdentification46Choice | 1333 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SecurityIdentification50 | 1353 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SettlementParties131 | 1360 |
| [type-0181](types/type-0181.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SettlementTransactionCondition11Code | 1370 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SettlementTransactionCondition30Choice | 1375 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SicovamIdentifier | 1381 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SmallNetworkIdentifier | 1384 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SouthAfricanNCCIdentifier | 1389 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SpanishDomesticInterbankingIdentifier | 1394 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SubAccount5 | 1399 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SubscriptionInformation2 | 1406 |
| [type-0189](types/type-0189.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SwissBCIdentifier | 1414 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}SwissSICIdentifier | 1419 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Tax35 | 1424 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Tax36 | 1434 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxBasis1Choice | 1440 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxCalculationInformation10 | 1446 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxEfficientProduct6 | 1452 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxEfficientProductType2Choice | 1462 |
| [type-0197](types/type-0197.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxEfficientProductType2Code | 1468 |
| [type-0198](types/type-0198.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxReference1 | 1485 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxReferenceParty1Choice | 1492 |
| [type-0200](types/type-0200.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxReferenceType1Choice | 1498 |
| [type-0201](types/type-0201.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxType17Code | 1504 |
| [type-0202](types/type-0202.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxType3Choice | 1526 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxableIncomePerShareCalculated2Choice | 1532 |
| [type-0204](types/type-0204.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxableIncomePerShareCalculated2Code | 1538 |
| [type-0205](types/type-0205.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxationBasis2Code | 1545 |
| [type-0206](types/type-0206.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TaxationBasis5Code | 1551 |
| [type-0207](types/type-0207.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TickerIdentifier | 1560 |
| [type-0208](types/type-0208.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TotalFeesAndTaxes44 | 1566 |
| [type-0209](types/type-0209.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TradeTransactionCondition5Code | 1577 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TradeTransactionCondition8Choice | 1583 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TransferType2Choice | 1589 |
| [type-0212](types/type-0212.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TransferType4Code | 1595 |
| [type-0213](types/type-0213.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TypeOfIdentification1Code | 1603 |
| [type-0214](types/type-0214.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TypeOfPrice10Code | 1614 |
| [type-0215](types/type-0215.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}TypeOfPrice46Choice | 1630 |
| [type-0216](types/type-0216.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}UKDomesticSortCodeIdentifier | 1636 |
| [type-0217](types/type-0217.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}UKTaxGroupUnit1Code | 1641 |
| [type-0218](types/type-0218.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Unit14 | 1647 |
| [type-0219](types/type-0219.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}Unit1Choice | 1660 |
| [type-0220](types/type-0220.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}UnitPrice23 | 1666 |
| [type-0221](types/type-0221.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}ValorenIdentifier | 1677 |
| [type-0222](types/type-0222.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}WaivingInstruction1Code | 1680 |
| [type-0223](types/type-0223.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}WaivingInstruction2Choice | 1686 |
| [type-0224](types/type-0224.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}WertpapierIdentifier | 1692 |
| [type-0225](types/type-0225.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.012.001.12}YesNoIndicator | 1695 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 3 |
| choice | 41 |
| complexType | 123 |
| element | 512 |
| enumeration | 207 |
| extension | 3 |
| fractionDigits | 8 |
| maxLength | 13 |
| minInclusive | 4 |
| minLength | 13 |
| pattern | 37 |
| restriction | 101 |
| schema | 1 |
| sequence | 79 |
| simpleContent | 3 |
| simpleType | 101 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/9700f23280f02607e2e4aada.md) · [Message](index.md)
