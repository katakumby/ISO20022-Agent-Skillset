---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.004.001.05"
message_family: "setr.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.004.001.05"
source_ids: ["src-000140"]
source_editions: ["2025-2026"]
---

# setr.004.001.05 structure

[src-000140](../../../../../raw-input/investment_funds/setr.004.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.004.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.004.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Account35 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}AccountIdentification82Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}AccountIdentificationAndName8 | 18 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}AccountSchemeName1Choice | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ActiveCurrencyAndAmount_SimpleType | 30 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ActiveCurrencyAndAmount | 37 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ActiveCurrencyCode | 44 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ActiveOrHistoricCurrencyAndAmount_SimpleType | 49 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ActiveOrHistoricCurrencyAndAmount | 56 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ActiveOrHistoricCurrencyCode | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}AdditionalReference10 | 68 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}AdditionalReference11 | 75 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}AddressType2Code | 82 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}AlternateSecurityIdentification7 | 92 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}AnyBICDec2014Identifier | 98 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}AustrianBankleitzahlIdentifier | 103 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}BICFIDec2014Identifier | 108 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}BaseOneRate | 113 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}BelgianIdentifier | 119 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}BlockChainAddressWallet14 | 122 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}BlockChainAddressWallet3 | 130 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Bloomberg2Identifier | 137 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CHIPSParticipantIdentifier | 142 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CHIPSUniversalIdentifier | 147 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CUSIPIdentifier | 152 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CanadianPaymentsARNIdentifier | 155 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CancellationRight1Choice | 160 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CancellationRight1Code | 166 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ChargeBasis2Choice | 174 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ChargeOrCommissionDiscount1 | 180 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ChargeType10Choice | 187 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Cheque10 | 193 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ClearingSystemMemberIdentification2Choice | 201 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ConductClassification1Code | 228 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ConsolidatedTapeAssociationIdentifier | 235 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CopyInformation5 | 241 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CountryAndResidentialStatusType2 | 247 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CountryCode | 253 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CreditTransfer12 | 258 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}CustomerConductClassification1Choice | 275 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DTI2024Identifier | 281 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DateAndDateTime2Choice | 286 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DateFormat42Choice | 292 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DecimalNumber | 298 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DeliveringPartiesAndAccount24 | 304 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DeliveryParameters3 | 312 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DeliveryReceiptType2Code | 318 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DigitalPaymentSettlement3 | 324 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DistributionPolicy1Code | 331 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Document | 337 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}DutchIdentifier | 342 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Equalisation1 | 345 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}EuroclearClearstreamIdentifier | 351 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Exact4AlphaNumericText | 357 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ExemptionReason1Choice | 362 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Extension1 | 368 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ExtensiveBranchNetworkIdentifier | 374 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ExternalAccountIdentification1Code | 379 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FedwireRoutingNumberIdentifier | 385 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Fee9 | 390 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FeeAndTax2 | 403 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FinancialAdvice1Code | 411 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FinancialInstitutionIdentification10Choice | 418 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FinancialInstitutionIdentification17 | 426 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FinancialInstrument107 | 432 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FinancialInstrumentIdentificationType1Code | 445 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FinancialInstrumentQuantity33Choice | 473 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FinancialInstrumentQuantity48Choice | 481 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ForeignExchangeTerms44 | 490 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FormOfSecurity1Code | 499 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FundCashAccount2Code | 505 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FundOrderType4Choice | 513 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FundOrderType5Code | 519 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FundOrderType8Code | 527 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}FundSettlementParameters28 | 539 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}GenericAccountIdentification1 | 551 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}GenericIdentification1 | 558 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}GenericIdentification164 | 565 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}GenericIdentification30 | 572 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}GenericIdentification47 | 579 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}GenericIdentification78 | 586 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}GermanBankleitzahlIdentifier | 592 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}HellenicBankIdentificationCodeIdentifier | 597 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}HongKongBankIdentifier | 602 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}IBAN2007Identifier | 607 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ISINOct2015Identifier | 612 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ISODate | 617 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ISODateTime | 620 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ISOYearMonth | 623 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}IdentificationSource1Choice | 626 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}IdentificationSource6Choice | 632 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ImpliedCurrencyAndAmount | 638 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}IncomePreference1Code | 645 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}IndianFinancialSystemCodeIdentifier | 651 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}IndividualPerson32 | 656 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Intermediary49 | 664 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}InvestmentAccount60 | 673 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}InvestmentAccount81 | 679 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}InvestmentAccountType1Choice | 691 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}InvestmentFundFee3Code | 697 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}InvestmentFundRole2Choice | 720 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}InvestmentFundRole2Code | 726 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}InvestmentFundsOrderBreakdown2 | 739 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}IrishNSCIdentifier | 745 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ItalianDomesticIdentifier | 750 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}LEIIdentifier | 755 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}MICIdentifier | 760 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Max140Text | 765 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Max16Text | 771 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Max30DecimalNumber | 777 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Max34Text | 783 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Max350Text | 789 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Max35Text | 795 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Max4AlphaNumericText | 801 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Max70Text | 808 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}MessageIdentification1 | 814 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}NameAndAddress4 | 820 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}NameAndAddress5 | 826 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}NegotiatedTrade1Code | 832 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}NewZealandNCCIdentifier | 839 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}OrderBreakdownType1Choice | 844 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}OrderOriginatorEligibility1Code | 850 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}OrderWaiver1 | 857 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}OrderWaiverReason1Code | 863 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}OrderWaiverReason3Choice | 872 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}OtherIdentification3Choice | 878 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}OtherIdentification8 | 884 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PartyIdentification125Choice | 891 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PartyIdentification139 | 898 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PartyIdentification262Choice | 904 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PartyIdentification339 | 912 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PartyIdentificationAndAccount235 | 918 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PartyIdentificationType7Code | 925 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PaymentInstrument28Choice | 947 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PaymentTransaction167 | 956 |
| [type-0137](types/type-0137.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PercentageRate | 961 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PlaceOfTradeIdentification4Choice | 967 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PolishNationalClearingCodeIdentifier | 975 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PortugueseNCCIdentifier | 980 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}PostalAddress1 | 985 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ProprietaryQuantity8 | 997 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}QUICKIdentifier | 1005 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Quantity48Choice | 1008 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}RICIdentifier | 1014 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ReceivingPartiesAndAccount24 | 1020 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}RedemptionMultipleOrder07 | 1028 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}RedemptionOrder18 | 1043 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}RedemptionOrderV05 | 1079 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ResidentialStatus1Code | 1089 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}RoundingDirection2Code | 1096 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}RussianCentralBankIdentificationCodeIdentifier | 1102 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SEDOLIdentifier | 1107 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SafekeepingPlace1Code | 1110 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SafekeepingPlace2Code | 1118 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SafekeepingPlaceFormat42Choice | 1124 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SafekeepingPlaceTypeAndIdentification1 | 1133 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SafekeepingPlaceTypeAndText6 | 1139 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SecurityIdentification46Choice | 1145 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SecurityIdentification50 | 1165 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Series1 | 1172 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SettlementTransactionCondition11Code | 1178 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SettlementTransactionCondition30Choice | 1183 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SicovamIdentifier | 1189 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SignatureType1Choice | 1192 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SignatureType2Code | 1198 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SmallNetworkIdentifier | 1206 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SouthAfricanNCCIdentifier | 1211 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SpanishDomesticInterbankingIdentifier | 1216 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SubAccount6 | 1221 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SwissBCIdentifier | 1229 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}SwissSICIdentifier | 1234 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}Tax42 | 1239 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TaxAmountOrRate4Choice | 1250 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TaxBasis1Choice | 1256 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TaxCalculationInformation9 | 1262 |
| [type-0177](types/type-0177.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TaxExemptReason1Code | 1267 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TaxType17Code | 1300 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TaxType3Choice | 1322 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TaxationBasis2Code | 1328 |
| [type-0181](types/type-0181.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TaxationBasis5Code | 1334 |
| [type-0182](types/type-0182.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TickerIdentifier | 1343 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TradeTransactionCondition5Code | 1349 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TradeTransactionCondition8Choice | 1355 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TradingCapacity8Code | 1361 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TransactionChannel2Code | 1367 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}TransactionChannelType1Choice | 1374 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}UKDomesticSortCodeIdentifier | 1380 |
| [type-0189](types/type-0189.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}UKTaxGroupUnit1Code | 1385 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}ValorenIdentifier | 1391 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}WaivingInstruction1Code | 1394 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}WaivingInstruction2Choice | 1400 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}WertpapierIdentifier | 1406 |
| [type-0194](types/type-0194.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.004.001.05}YesNoIndicator | 1409 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 2 |
| choice | 36 |
| complexType | 95 |
| element | 364 |
| enumeration | 202 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 12 |
| minInclusive | 3 |
| minLength | 12 |
| pattern | 35 |
| restriction | 98 |
| schema | 1 |
| sequence | 57 |
| simpleContent | 2 |
| simpleType | 98 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/362771270fdc2f85a4f1aa99.md) · [Message](index.md)
