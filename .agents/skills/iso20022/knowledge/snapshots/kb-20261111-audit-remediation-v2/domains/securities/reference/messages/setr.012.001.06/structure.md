---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.012.001.06"
message_family: "setr.012"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.012.001.06"
source_ids: ["src-000148"]
source_editions: ["2025-2026"]
---

# setr.012.001.06 structure

[src-000148](../../../../../raw-input/investment_funds/setr.012.001.06.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.012.001.06`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.012.001.06 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Account35 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}AccountIdentification82Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}AccountIdentificationAndName8 | 18 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}AccountSchemeName1Choice | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ActiveCurrencyAnd13DecimalAmount_SimpleType | 30 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ActiveCurrencyAnd13DecimalAmount | 37 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ActiveCurrencyAndAmount_SimpleType | 44 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ActiveCurrencyAndAmount | 51 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ActiveCurrencyCode | 58 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ActiveOrHistoricCurrencyAndAmount_SimpleType | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ActiveOrHistoricCurrencyAndAmount | 70 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ActiveOrHistoricCurrencyCode | 77 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}AdditionalReference10 | 82 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}AdditionalReference11 | 89 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}AddressType2Code | 96 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}AlternateSecurityIdentification7 | 106 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}AnyBICDec2014Identifier | 112 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}AustrianBankleitzahlIdentifier | 117 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}BICFIDec2014Identifier | 122 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}BaseOneRate | 127 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}BelgianIdentifier | 133 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}BestExecution1Code | 136 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}BlockChainAddressWallet14 | 141 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}BlockChainAddressWallet3 | 149 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Bloomberg2Identifier | 156 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}BranchData4 | 161 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CHIPSParticipantIdentifier | 168 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CHIPSUniversalIdentifier | 173 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CUSIPIdentifier | 178 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CanadianPaymentsARNIdentifier | 181 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CancellationRight1Choice | 186 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CancellationRight1Code | 192 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CardType1Code | 200 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ChargeBasis2Choice | 206 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ChargeOrCommissionDiscount1 | 212 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ChargeType10Choice | 219 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Cheque10 | 225 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ClearingSystemMemberIdentification2Choice | 233 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ConductClassification1Code | 260 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ConsolidatedTapeAssociationIdentifier | 267 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CopyInformation5 | 273 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CountryAndResidentialStatusType2 | 279 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CountryCode | 285 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CreditTransfer12 | 290 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}CustomerConductClassification1Choice | 307 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DTI2024Identifier | 313 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DateAndDateTime2Choice | 318 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DateFormat42Choice | 324 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DecimalNumber | 330 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DeliveringPartiesAndAccount24 | 336 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DeliveryParameters3 | 344 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DeliveryReceiptType2Code | 350 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DigitalPaymentSettlement3 | 356 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DirectDebitMandate9 | 363 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DistributionPolicy1Code | 378 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Document | 384 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}DutchIdentifier | 389 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}EUCapitalGain2Code | 392 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}EUCapitalGain3Choice | 399 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}EUDividendStatus1Code | 405 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}EUDividendStatusType2Choice | 412 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Equalisation4 | 418 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}EqualisationMethodologyType1Code | 430 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}EuroclearClearstreamIdentifier | 437 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Exact4AlphaNumericText | 443 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ExemptionReason1Choice | 448 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Extension1 | 454 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ExtensiveBranchNetworkIdentifier | 460 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ExternalAccountIdentification1Code | 465 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FedwireRoutingNumberIdentifier | 471 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Fee11 | 476 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FinancialAdvice1Code | 490 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FinancialInstitutionIdentification10Choice | 497 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FinancialInstitutionIdentification17 | 505 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FinancialInstrument107 | 511 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FinancialInstrumentIdentificationType1Code | 524 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FinancialInstrumentQuantity33Choice | 552 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ForeignExchangeTerms37 | 560 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FormOfSecurity1Code | 571 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FundCashAccount2Code | 577 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FundOrderType4Choice | 585 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FundOrderType5Code | 591 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FundOrderType8Code | 599 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}FundSettlementParameters28 | 611 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}GenericAccountIdentification1 | 623 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}GenericIdentification1 | 630 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}GenericIdentification164 | 637 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}GenericIdentification30 | 644 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}GenericIdentification47 | 651 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}GenericIdentification78 | 658 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}GermanBankleitzahlIdentifier | 664 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}HellenicBankIdentificationCodeIdentifier | 669 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}HongKongBankIdentifier | 674 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}IBAN2007Identifier | 679 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ISINOct2015Identifier | 684 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ISODate | 689 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ISODateTime | 692 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ISOYearMonth | 695 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}IdentificationSource1Choice | 698 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}IdentificationSource6Choice | 704 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ImpliedCurrencyAndAmount | 710 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}IncomePreference1Code | 717 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}IndianFinancialSystemCodeIdentifier | 723 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}IndividualPerson32 | 728 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}InformativeTax2 | 736 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Intermediary49 | 745 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}InvestmentAccount60 | 754 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}InvestmentAccount81 | 760 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}InvestmentAccountType1Choice | 772 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}InvestmentFundFee3Code | 778 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}InvestmentFundRole2Choice | 801 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}InvestmentFundRole2Code | 807 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}InvestmentFundsOrderBreakdown2 | 820 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}IrishNSCIdentifier | 826 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ItalianDomesticIdentifier | 831 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}LEIIdentifier | 836 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}LateReport1Code | 841 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}MICIdentifier | 847 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Max140Text | 852 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Max16Text | 858 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Max30DecimalNumber | 864 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Max34Text | 870 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Max350Text | 876 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Max35Text | 882 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Max3Text | 888 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Max4AlphaNumericText | 894 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Max70Text | 901 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}MessageIdentification1 | 907 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}NameAndAddress4 | 913 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}NameAndAddress5 | 919 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}NegotiatedTrade1Code | 925 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}NewZealandNCCIdentifier | 932 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Number | 937 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}OrderBreakdownType1Choice | 943 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}OrderOriginatorEligibility1Code | 949 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}OrderWaiver1 | 956 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}OrderWaiverReason1Code | 962 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}OrderWaiverReason3Choice | 971 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}OtherIdentification3Choice | 977 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}OtherIdentification8 | 983 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PartyIdentification125Choice | 990 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PartyIdentification139 | 997 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PartyIdentification262Choice | 1003 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PartyIdentification339 | 1011 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PartyIdentificationAndAccount235 | 1017 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PartyIdentificationType7Code | 1024 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PaymentCard34 | 1046 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PaymentInstrument29Choice | 1059 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PaymentTransaction180 | 1070 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PercentageRate | 1075 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PlaceOfTradeIdentification4Choice | 1081 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PolishNationalClearingCodeIdentifier | 1089 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PortugueseNCCIdentifier | 1094 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PostalAddress1 | 1099 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PriceMethod1Code | 1111 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}PriceValue1 | 1117 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ProfitAndLoss2Choice | 1122 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ProprietaryQuantity8 | 1128 |
| [type-0160](types/type-0160.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}QUICKIdentifier | 1136 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Quantity48Choice | 1139 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}RICIdentifier | 1145 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ReceivingPartiesAndAccount24 | 1151 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ResidentialStatus1Code | 1159 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}RoundingDirection2Code | 1166 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}RussianCentralBankIdentificationCodeIdentifier | 1172 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SEDOLIdentifier | 1177 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SafekeepingPlace1Code | 1180 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SafekeepingPlace2Code | 1188 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SafekeepingPlaceFormat42Choice | 1194 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SafekeepingPlaceTypeAndIdentification1 | 1203 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SafekeepingPlaceTypeAndText6 | 1209 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SecurityIdentification46Choice | 1215 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SecurityIdentification50 | 1235 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Series1 | 1242 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SettlementTransactionCondition11Code | 1248 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SettlementTransactionCondition30Choice | 1253 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SicovamIdentifier | 1259 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SignatureType1Choice | 1262 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SignatureType2Code | 1268 |
| [type-0181](types/type-0181.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SmallNetworkIdentifier | 1276 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SourceOfCash1Choice | 1281 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SourceOfCash1Code | 1287 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SouthAfricanNCCIdentifier | 1306 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SpanishDomesticInterbankingIdentifier | 1311 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SubAccount6 | 1316 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SubscriptionExecution16 | 1324 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SubscriptionMultipleExecution7 | 1378 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SubscriptionOrderConfirmationV06 | 1394 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SwissBCIdentifier | 1405 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}SwissSICIdentifier | 1410 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Tax35 | 1415 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Tax40 | 1425 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TaxBasis1Choice | 1437 |
| [type-0195](types/type-0195.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TaxCalculationInformation10 | 1443 |
| [type-0196](types/type-0196.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TaxExemptReason1Code | 1449 |
| [type-0197](types/type-0197.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TaxType17Code | 1482 |
| [type-0198](types/type-0198.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TaxType3Choice | 1504 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TaxableIncomePerShareCalculated2Choice | 1510 |
| [type-0200](types/type-0200.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TaxableIncomePerShareCalculated2Code | 1516 |
| [type-0201](types/type-0201.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TaxationBasis2Code | 1523 |
| [type-0202](types/type-0202.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TaxationBasis5Code | 1529 |
| [type-0203](types/type-0203.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TickerIdentifier | 1538 |
| [type-0204](types/type-0204.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TotalFeesAndTaxes45 | 1544 |
| [type-0205](types/type-0205.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TradeTransactionCondition5Code | 1555 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TradeTransactionCondition8Choice | 1561 |
| [type-0207](types/type-0207.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TradingCapacity8Code | 1567 |
| [type-0208](types/type-0208.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TransactionChannel2Code | 1573 |
| [type-0209](types/type-0209.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TransactionChannelType1Choice | 1580 |
| [type-0210](types/type-0210.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TypeOfPrice10Code | 1586 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}TypeOfPrice46Choice | 1602 |
| [type-0212](types/type-0212.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}UKDomesticSortCodeIdentifier | 1608 |
| [type-0213](types/type-0213.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}Unit1Choice | 1613 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}UnitPrice22 | 1619 |
| [type-0215](types/type-0215.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}ValorenIdentifier | 1630 |
| [type-0216](types/type-0216.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}WaivingInstruction1Code | 1633 |
| [type-0217](types/type-0217.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}WaivingInstruction2Choice | 1639 |
| [type-0218](types/type-0218.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}WertpapierIdentifier | 1645 |
| [type-0219](types/type-0219.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.012.001.06}YesNoIndicator | 1648 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 3 |
| choice | 41 |
| complexType | 108 |
| element | 449 |
| enumeration | 246 |
| extension | 3 |
| fractionDigits | 9 |
| maxLength | 13 |
| minInclusive | 4 |
| minLength | 13 |
| pattern | 35 |
| restriction | 110 |
| schema | 1 |
| sequence | 64 |
| simpleContent | 3 |
| simpleType | 110 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
