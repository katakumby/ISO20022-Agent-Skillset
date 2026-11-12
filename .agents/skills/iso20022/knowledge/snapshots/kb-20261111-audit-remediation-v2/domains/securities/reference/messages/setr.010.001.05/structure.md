---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.010.001.05"
message_family: "setr.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.010.001.05"
source_ids: ["src-000146"]
source_editions: ["2025-2026"]
---

# setr.010.001.05 structure

[src-000146](../../../../../raw-input/investment_funds/setr.010.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.010.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.010.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Account35 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}AccountIdentification82Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}AccountIdentificationAndName8 | 18 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}AccountSchemeName1Choice | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ActiveCurrencyAndAmount_SimpleType | 30 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ActiveCurrencyAndAmount | 37 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ActiveCurrencyCode | 44 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ActiveOrHistoricCurrencyAndAmount_SimpleType | 49 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ActiveOrHistoricCurrencyAndAmount | 56 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ActiveOrHistoricCurrencyCode | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}AdditionalReference10 | 68 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}AdditionalReference11 | 75 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}AddressType2Code | 82 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}AlternateSecurityIdentification7 | 92 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}AnyBICDec2014Identifier | 98 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}AustrianBankleitzahlIdentifier | 103 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}BICFIDec2014Identifier | 108 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}BaseOneRate | 113 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}BelgianIdentifier | 119 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}BeneficiaryCertificationCompletion1Code | 122 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}BlockChainAddressWallet14 | 129 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}BlockChainAddressWallet3 | 137 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Bloomberg2Identifier | 144 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}BranchData4 | 149 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CHIPSParticipantIdentifier | 156 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CHIPSUniversalIdentifier | 161 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CUSIPIdentifier | 166 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CanadianPaymentsARNIdentifier | 169 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CancellationRight1Choice | 174 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CancellationRight1Code | 180 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CardType1Code | 188 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ChargeBasis2Choice | 194 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ChargeOrCommissionDiscount1 | 200 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ChargeType10Choice | 207 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Cheque10 | 213 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ClearingSystemMemberIdentification2Choice | 221 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ConductClassification1Code | 248 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ConsolidatedTapeAssociationIdentifier | 255 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CopyInformation5 | 261 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CountryAndResidentialStatusType2 | 267 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CountryCode | 273 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CreditTransfer12 | 278 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}CustomerConductClassification1Choice | 295 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DTI2024Identifier | 301 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DateAndDateTime2Choice | 306 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DateFormat42Choice | 312 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DecimalNumber | 318 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DeliveringPartiesAndAccount24 | 324 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DeliveryReceiptType2Code | 332 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DigitalPaymentSettlement3 | 338 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DirectDebitMandate9 | 345 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DistributionPolicy1Code | 360 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Document | 366 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}DutchIdentifier | 371 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Equalisation1 | 374 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}EuroclearClearstreamIdentifier | 380 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Exact4AlphaNumericText | 386 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ExemptionReason1Choice | 391 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Extension1 | 397 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ExtensiveBranchNetworkIdentifier | 403 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ExternalAccountIdentification1Code | 408 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FedwireRoutingNumberIdentifier | 414 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Fee9 | 419 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FeeAndTax2 | 432 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FinancialAdvice1Code | 440 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FinancialInstitutionIdentification10Choice | 447 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FinancialInstitutionIdentification17 | 455 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FinancialInstrument107 | 461 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FinancialInstrumentIdentificationType1Code | 474 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FinancialInstrumentQuantity33Choice | 502 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FinancialInstrumentQuantity49Choice | 510 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ForeignExchangeTerms44 | 518 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FormOfSecurity1Code | 527 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FundCashAccount2Code | 533 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FundOrderType4Choice | 541 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FundOrderType5Code | 547 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FundOrderType8Code | 555 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}FundSettlementParameters22 | 567 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}GenericAccountIdentification1 | 579 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}GenericIdentification1 | 586 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}GenericIdentification164 | 593 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}GenericIdentification30 | 600 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}GenericIdentification47 | 607 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}GenericIdentification78 | 614 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}GermanBankleitzahlIdentifier | 620 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}HellenicBankIdentificationCodeIdentifier | 625 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}HongKongBankIdentifier | 630 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}IBAN2007Identifier | 635 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ISINOct2015Identifier | 640 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ISODate | 645 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ISODateTime | 648 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ISOYearMonth | 651 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}IdentificationSource1Choice | 654 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}IdentificationSource6Choice | 660 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ImpliedCurrencyAndAmount | 666 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}IncomePreference1Code | 673 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}IndianFinancialSystemCodeIdentifier | 679 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}IndividualPerson31 | 684 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Intermediary50 | 693 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}InvestmentAccount60 | 701 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}InvestmentAccount81 | 707 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}InvestmentAccountType1Choice | 719 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}InvestmentFundFee3Code | 725 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}InvestmentFundRole2Choice | 748 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}InvestmentFundRole2Code | 754 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}InvestmentFundsOrderBreakdown2 | 767 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}IrishNSCIdentifier | 773 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ItalianDomesticIdentifier | 778 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}LEIIdentifier | 783 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}MICIdentifier | 788 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Max140Text | 793 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Max16Text | 799 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Max30DecimalNumber | 805 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Max34Text | 811 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Max350Text | 817 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Max35Text | 823 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Max3Text | 829 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Max4AlphaNumericText | 835 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Max70Text | 842 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}MessageIdentification1 | 848 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}NameAndAddress4 | 854 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}NameAndAddress5 | 860 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}NegotiatedTrade1Code | 866 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}NewZealandNCCIdentifier | 873 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}OrderBreakdownType1Choice | 878 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}OrderOriginatorEligibility1Code | 884 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}OrderWaiver1 | 891 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}OrderWaiverReason1Code | 897 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}OrderWaiverReason3Choice | 906 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}OtherIdentification3Choice | 912 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}OtherIdentification8 | 918 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PartyIdentification125Choice | 925 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PartyIdentification139 | 932 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PartyIdentification262Choice | 938 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PartyIdentification339 | 946 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PartyIdentificationAndAccount235 | 952 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PartyIdentificationType7Code | 959 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PaymentCard34 | 981 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PaymentInstrument29Choice | 994 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PaymentTransaction180 | 1005 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PercentageRate | 1010 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PlaceOfTradeIdentification4Choice | 1016 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PolishNationalClearingCodeIdentifier | 1024 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PortugueseNCCIdentifier | 1029 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}PostalAddress1 | 1034 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ProprietaryQuantity8 | 1046 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}QUICKIdentifier | 1054 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Quantity48Choice | 1057 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}RICIdentifier | 1063 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ReceivingPartiesAndAccount24 | 1069 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ResidentialStatus1Code | 1077 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}RoundingDirection2Code | 1084 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}RussianCentralBankIdentificationCodeIdentifier | 1090 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SEDOLIdentifier | 1095 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SafekeepingPlace1Code | 1098 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SafekeepingPlace2Code | 1106 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SafekeepingPlaceFormat42Choice | 1112 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SafekeepingPlaceTypeAndIdentification1 | 1121 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SafekeepingPlaceTypeAndText6 | 1127 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SecurityIdentification46Choice | 1133 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SecurityIdentification50 | 1153 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Series1 | 1160 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SettlementTransactionCondition11Code | 1166 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SettlementTransactionCondition30Choice | 1171 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SicovamIdentifier | 1177 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SignatureType1Choice | 1180 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SignatureType2Code | 1186 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SmallNetworkIdentifier | 1194 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SourceOfCash1Choice | 1199 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SourceOfCash1Code | 1205 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SouthAfricanNCCIdentifier | 1224 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SpanishDomesticInterbankingIdentifier | 1229 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SubAccount6 | 1234 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SubscriptionMultipleOrder7 | 1242 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SubscriptionOrder17 | 1257 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SubscriptionOrderV05 | 1295 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SwissBCIdentifier | 1305 |
| [type-0179](types/type-0179.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}SwissSICIdentifier | 1310 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}Tax42 | 1315 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TaxAmountOrRate4Choice | 1326 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TaxBasis1Choice | 1332 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TaxCalculationInformation9 | 1338 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TaxExemptReason1Code | 1343 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TaxType17Code | 1376 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TaxType3Choice | 1398 |
| [type-0187](types/type-0187.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TaxationBasis2Code | 1404 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TaxationBasis5Code | 1410 |
| [type-0189](types/type-0189.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TickerIdentifier | 1419 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TradeTransactionCondition5Code | 1425 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TradeTransactionCondition8Choice | 1431 |
| [type-0192](types/type-0192.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TransactionChannel2Code | 1437 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}TransactionChannelType1Choice | 1444 |
| [type-0194](types/type-0194.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}UKDomesticSortCodeIdentifier | 1450 |
| [type-0195](types/type-0195.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}ValorenIdentifier | 1455 |
| [type-0196](types/type-0196.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}WaivingInstruction1Code | 1458 |
| [type-0197](types/type-0197.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}WaivingInstruction2Choice | 1464 |
| [type-0198](types/type-0198.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}WertpapierIdentifier | 1470 |
| [type-0199](types/type-0199.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.010.001.05}YesNoIndicator | 1473 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 2 |
| choice | 37 |
| complexType | 98 |
| element | 390 |
| enumeration | 218 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 13 |
| minInclusive | 3 |
| minLength | 13 |
| pattern | 35 |
| restriction | 100 |
| schema | 1 |
| sequence | 59 |
| simpleContent | 2 |
| simpleType | 100 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
