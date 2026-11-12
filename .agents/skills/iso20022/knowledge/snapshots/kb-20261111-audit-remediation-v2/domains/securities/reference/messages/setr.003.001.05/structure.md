---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.003.001.05"
message_family: "setr.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.003.001.05"
source_ids: ["src-000139"]
source_editions: ["2025-2026"]
---

# setr.003.001.05 structure

[src-000139](../../../../../raw-input/investment_funds/setr.003.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.003.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.003.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Account35 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}AccountIdentification82Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}AccountIdentificationAndName8 | 18 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}AccountSchemeName1Choice | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ActiveCurrencyAnd13DecimalAmount_SimpleType | 30 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ActiveCurrencyAnd13DecimalAmount | 37 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ActiveCurrencyAndAmount_SimpleType | 44 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ActiveCurrencyAndAmount | 51 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ActiveCurrencyCode | 58 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ActiveOrHistoricCurrencyAndAmount_SimpleType | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ActiveOrHistoricCurrencyAndAmount | 70 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ActiveOrHistoricCurrencyCode | 77 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}AdditionalReference10 | 82 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}AdditionalReference11 | 89 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}AddressType2Code | 96 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}AlternateSecurityIdentification7 | 106 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}AnyBICDec2014Identifier | 112 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}AustrianBankleitzahlIdentifier | 117 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}BICFIDec2014Identifier | 122 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}BaseOneRate | 127 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}BelgianIdentifier | 133 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}BestExecution1Code | 136 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}BlockChainAddressWallet14 | 141 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}BlockChainAddressWallet3 | 149 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Bloomberg2Identifier | 156 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CHIPSParticipantIdentifier | 161 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CHIPSUniversalIdentifier | 166 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CUSIPIdentifier | 171 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CanadianPaymentsARNIdentifier | 174 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CancellationRight1Choice | 179 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CancellationRight1Code | 185 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ChargeBasis2Choice | 193 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ChargeOrCommissionDiscount1 | 199 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ChargeType10Choice | 206 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Cheque10 | 212 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ClearingSystemMemberIdentification2Choice | 220 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ConductClassification1Code | 247 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ConsolidatedTapeAssociationIdentifier | 254 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CopyInformation5 | 260 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CountryAndResidentialStatusType2 | 266 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CountryCode | 272 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CreditTransfer12 | 277 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}CustomerConductClassification1Choice | 294 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DTI2024Identifier | 300 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DateAndDateTime2Choice | 305 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DateFormat42Choice | 311 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DecimalNumber | 317 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DeliveringPartiesAndAccount24 | 323 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DeliveryParameters3 | 331 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DeliveryReceiptType2Code | 337 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DigitalPaymentSettlement3 | 343 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DistributionPolicy1Code | 350 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Document | 356 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}DutchIdentifier | 361 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}EUCapitalGain2Code | 364 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}EUCapitalGain3Choice | 371 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}EUDividendStatus1Code | 377 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}EUDividendStatusType2Choice | 384 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Equalisation1 | 390 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}EuroclearClearstreamIdentifier | 396 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Exact4AlphaNumericText | 402 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ExemptionReason1Choice | 407 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Extension1 | 413 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ExtensiveBranchNetworkIdentifier | 419 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ExternalAccountIdentification1Code | 424 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FedwireRoutingNumberIdentifier | 430 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Fee11 | 435 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FinancialAdvice1Code | 449 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FinancialInstitutionIdentification10Choice | 456 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FinancialInstitutionIdentification17 | 464 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FinancialInstrument107 | 470 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FinancialInstrumentIdentificationType1Code | 483 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FinancialInstrumentQuantity33Choice | 511 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ForeignExchangeTerms37 | 519 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FormOfSecurity1Code | 530 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FundCashAccount2Code | 536 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FundOrderType4Choice | 544 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FundOrderType5Code | 550 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FundOrderType8Code | 558 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}FundSettlementParameters22 | 570 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}GateHoldBack1Code | 582 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}GenericAccountIdentification1 | 588 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}GenericIdentification1 | 595 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}GenericIdentification164 | 602 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}GenericIdentification30 | 609 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}GenericIdentification47 | 616 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}GenericIdentification78 | 623 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}GermanBankleitzahlIdentifier | 629 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}HellenicBankIdentificationCodeIdentifier | 634 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}HoldBackInformation5 | 639 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}HongKongBankIdentifier | 650 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}IBAN2007Identifier | 655 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ISINOct2015Identifier | 660 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ISODate | 665 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ISODateTime | 668 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ISOYearMonth | 671 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}IdentificationSource1Choice | 674 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}IdentificationSource6Choice | 680 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ImpliedCurrencyAndAmount | 686 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}IncomePreference1Code | 693 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}IndianFinancialSystemCodeIdentifier | 699 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}IndividualPerson32 | 704 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}InformativeTax2 | 712 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Intermediary49 | 721 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}InvestmentAccount60 | 730 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}InvestmentAccount81 | 736 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}InvestmentAccountType1Choice | 748 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}InvestmentFundFee3Code | 754 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}InvestmentFundRole2Choice | 777 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}InvestmentFundRole2Code | 783 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}InvestmentFundsOrderBreakdown2 | 796 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}IrishNSCIdentifier | 802 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ItalianDomesticIdentifier | 807 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}LEIIdentifier | 812 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}LateReport1Code | 817 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}MICIdentifier | 823 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Max140Text | 828 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Max16Text | 834 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Max30DecimalNumber | 840 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Max34Text | 846 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Max350Text | 852 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Max35Text | 858 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Max4AlphaNumericText | 864 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Max70Text | 871 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}MessageIdentification1 | 877 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}NameAndAddress4 | 883 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}NameAndAddress5 | 889 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}NegotiatedTrade1Code | 895 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}NewZealandNCCIdentifier | 902 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Number | 907 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}OrderBreakdownType1Choice | 913 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}OrderOriginatorEligibility1Code | 919 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}OrderWaiver1 | 926 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}OrderWaiverReason1Code | 932 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}OrderWaiverReason3Choice | 941 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}OtherIdentification3Choice | 947 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}OtherIdentification8 | 953 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PartyIdentification125Choice | 960 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PartyIdentification139 | 967 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PartyIdentification262Choice | 973 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PartyIdentification339 | 981 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PartyIdentificationAndAccount235 | 987 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PartyIdentificationType7Code | 994 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PaymentInstrument28Choice | 1016 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PaymentTransaction167 | 1025 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PercentageRate | 1030 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PlaceOfTradeIdentification4Choice | 1036 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PolishNationalClearingCodeIdentifier | 1044 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PortugueseNCCIdentifier | 1049 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PostalAddress1 | 1054 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PriceMethod1Code | 1066 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}PriceValue1 | 1072 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ProfitAndLoss2Choice | 1077 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ProprietaryQuantity8 | 1083 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}QUICKIdentifier | 1091 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Quantity48Choice | 1094 |
| [type-0158](types/type-0158.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}RICIdentifier | 1100 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ReceivingPartiesAndAccount24 | 1106 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}RedemptionBulkExecution06 | 1114 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}RedemptionBulkOrderConfirmationV05 | 1131 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}RedemptionCompletion1Code | 1142 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}RedemptionExecution18 | 1148 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ResidentialStatus1Code | 1199 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}RoundingDirection2Code | 1206 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}RussianCentralBankIdentificationCodeIdentifier | 1212 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SEDOLIdentifier | 1217 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SafekeepingPlace1Code | 1220 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SafekeepingPlace2Code | 1228 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SafekeepingPlaceFormat42Choice | 1234 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SafekeepingPlaceTypeAndIdentification1 | 1243 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SafekeepingPlaceTypeAndText6 | 1249 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SecurityIdentification46Choice | 1255 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SecurityIdentification50 | 1275 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Series1 | 1282 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SettlementTransactionCondition11Code | 1288 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SettlementTransactionCondition30Choice | 1293 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SicovamIdentifier | 1299 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SignatureType1Choice | 1302 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SignatureType2Code | 1308 |
| [type-0181](types/type-0181.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SmallNetworkIdentifier | 1316 |
| [type-0182](types/type-0182.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SouthAfricanNCCIdentifier | 1321 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SpanishDomesticInterbankingIdentifier | 1326 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SubAccount6 | 1331 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SwissBCIdentifier | 1339 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}SwissSICIdentifier | 1344 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Tax35 | 1349 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Tax40 | 1359 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TaxBasis1Choice | 1371 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TaxCalculationInformation10 | 1377 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TaxExemptReason1Code | 1383 |
| [type-0192](types/type-0192.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TaxType17Code | 1416 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TaxType3Choice | 1438 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TaxableIncomePerShareCalculated2Choice | 1444 |
| [type-0195](types/type-0195.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TaxableIncomePerShareCalculated2Code | 1450 |
| [type-0196](types/type-0196.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TaxationBasis2Code | 1457 |
| [type-0197](types/type-0197.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TaxationBasis5Code | 1463 |
| [type-0198](types/type-0198.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TickerIdentifier | 1472 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TotalFeesAndTaxes45 | 1478 |
| [type-0200](types/type-0200.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TradeTransactionCondition5Code | 1489 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TradeTransactionCondition8Choice | 1495 |
| [type-0202](types/type-0202.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TradingCapacity8Code | 1501 |
| [type-0203](types/type-0203.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TransactionChannel2Code | 1507 |
| [type-0204](types/type-0204.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TransactionChannelType1Choice | 1514 |
| [type-0205](types/type-0205.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TypeOfPrice10Code | 1520 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}TypeOfPrice46Choice | 1536 |
| [type-0207](types/type-0207.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}UKDomesticSortCodeIdentifier | 1542 |
| [type-0208](types/type-0208.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}UKTaxGroupUnit1Code | 1547 |
| [type-0209](types/type-0209.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}Unit1Choice | 1553 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}UnitPrice22 | 1559 |
| [type-0211](types/type-0211.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}ValorenIdentifier | 1570 |
| [type-0212](types/type-0212.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}WaivingInstruction1Code | 1573 |
| [type-0213](types/type-0213.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}WaivingInstruction2Choice | 1579 |
| [type-0214](types/type-0214.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}WertpapierIdentifier | 1585 |
| [type-0215](types/type-0215.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.003.001.05}YesNoIndicator | 1588 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 3 |
| choice | 40 |
| complexType | 105 |
| element | 421 |
| enumeration | 232 |
| extension | 3 |
| fractionDigits | 9 |
| maxLength | 12 |
| minInclusive | 4 |
| minLength | 12 |
| pattern | 35 |
| restriction | 109 |
| schema | 1 |
| sequence | 62 |
| simpleContent | 3 |
| simpleType | 109 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
