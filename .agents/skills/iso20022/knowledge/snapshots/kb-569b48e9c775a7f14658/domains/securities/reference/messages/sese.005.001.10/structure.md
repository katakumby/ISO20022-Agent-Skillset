---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.005.001.10"
message_family: "sese.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.005.001.10"
source_ids: ["src-000124"]
source_editions: ["2025-2026"]
---

# sese.005.001.10 structure

[src-000124](../../../../../raw-input/investment_funds/sese.005.001.10.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.005.001.10`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.005.001.10 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Account27 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Account38 | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveCurrencyAnd13DecimalAmount_SimpleType | 21 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveCurrencyAnd13DecimalAmount | 28 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveCurrencyAndAmount_SimpleType | 35 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveCurrencyAndAmount | 42 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveCurrencyCode | 49 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 54 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount | 61 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveOrHistoricCurrencyAndAmount_SimpleType | 68 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveOrHistoricCurrencyAndAmount | 75 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ActiveOrHistoricCurrencyCode | 82 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}AdditionalReference10 | 87 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}AdditionalReference11 | 94 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}AddressType2Code | 101 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}AlternatePartyIdentification7 | 111 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}AlternateSecurityIdentification7 | 118 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}AnyBICDec2014Identifier | 124 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}BaseOneRate | 129 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}BelgianIdentifier | 135 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}BeneficiaryCertificationCompletion1Code | 138 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}BlockChainAddressWallet3 | 145 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Bloomberg2Identifier | 152 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}BusinessFlowType1Code | 157 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}CUSIPIdentifier | 164 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ChargeBasis2Choice | 167 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ChargeBearer1Code | 173 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ChargeOrCommissionDiscount1 | 180 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ChargeOrCommissionDiscount2 | 187 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ChargePaymentMethod1Choice | 194 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ChargePaymentMethod1Code | 200 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ChargeType10Choice | 206 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ChargeType6Choice | 212 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ConsolidatedTapeAssociationIdentifier | 218 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ContactIdentification2 | 224 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}CopyInformation5 | 235 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}CountryCode | 241 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}DTI2024Identifier | 246 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}DateAndDateTime2Choice | 251 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}DateFormat1Choice | 257 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}DecimalNumber | 264 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}DeliverInformation22 | 270 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}DeliveryParameters4 | 293 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}DigitalPaymentSettlement3 | 300 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}DistributionPolicy1Code | 307 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Document | 313 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}DutchIdentifier | 318 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}EuroclearClearstreamIdentifier | 321 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Exact4AlphaNumericText | 327 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ExemptionReason1Choice | 332 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Extension1 | 338 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Fee11 | 344 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Fee7 | 358 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Fees2 | 368 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}FinancialInstrument116 | 374 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}FinancialInstrumentIdentificationType1Code | 386 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}FinancialInstrumentQuantity33Choice | 414 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ForeignExchangeTerms37 | 422 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}FormOfSecurity1Code | 433 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}FundSettlementParameters25 | 439 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}FundSettlementParameters26 | 447 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}GenericIdentification1 | 455 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}GenericIdentification27 | 462 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}GenericIdentification30 | 469 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}GenericIdentification36 | 476 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}GenericIdentification47 | 483 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}GenericIdentification78 | 490 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}HoldingsPlanType1Code | 496 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ISINOct2015Identifier | 503 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ISODate | 508 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ISODateTime | 511 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ISOYearMonth | 514 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}IdentificationSource1Choice | 517 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}IdentificationSource6Choice | 523 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}IdentificationType42Choice | 529 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ImpliedCurrencyAndAmount | 535 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}IncomePreference2Code | 542 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Intermediary43 | 548 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}InvestmentAccount83 | 556 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}InvestmentFundFee2Code | 574 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}InvestmentFundFee3Code | 585 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}InvestmentFundRole2Code | 608 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}LEIIdentifier | 621 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}MarketPracticeVersion1 | 626 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Max140Text | 633 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Max16Text | 639 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Max256Text | 645 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Max30DecimalNumber | 651 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Max350Text | 657 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Max35Text | 663 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Max4AlphaNumericText | 669 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Max70Text | 676 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}MessageIdentification1 | 682 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}NameAndAddress4 | 688 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}NameAndAddress5 | 694 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}NamePrefix1Code | 700 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Number | 708 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}OtherAmount1 | 714 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}OtherAmountType1Choice | 720 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}OtherAmountType1Code | 726 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}OtherIdentification8 | 732 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PartyIdentification123Choice | 739 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PartyIdentification125Choice | 746 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PartyIdentification139 | 753 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PartyIdentification257Choice | 759 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PartyIdentification315 | 767 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PartyIdentificationAndAccount194 | 777 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PartyTextInformation1 | 788 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PartyTextInformation6 | 795 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PercentageRate | 803 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PhoneNumber | 809 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PhysicalTransferType1Code | 814 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PostalAddress1 | 820 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PriceMethod1Code | 832 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}PriceValue1 | 838 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ProprietaryQuantity8 | 843 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}QUICKIdentifier | 851 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Quantity48Choice | 854 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Quantity82Choice | 860 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}RICIdentifier | 866 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Role4Choice | 872 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}RoundingDirection2Code | 878 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SEDOLIdentifier | 884 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SafekeepingPlace1Code | 887 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SafekeepingPlace2Code | 895 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SafekeepingPlaceFormat42Choice | 901 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SafekeepingPlaceTypeAndIdentification1 | 910 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SafekeepingPlaceTypeAndText6 | 916 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SecuritiesAccount19 | 922 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SecurityIdentification46Choice | 929 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SecurityIdentification50 | 949 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SettlementDate1Code | 956 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SettlementParties131 | 963 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SettlementTransactionCondition11Code | 973 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SettlementTransactionCondition30Choice | 978 |
| [type-0137](types/type-0137.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SicovamIdentifier | 984 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}StampDutyType2Code | 987 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}SubAccount5 | 993 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Tax35 | 1000 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Tax38 | 1010 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxBasis1Choice | 1022 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxCalculationInformation10 | 1028 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxCalculationInformation11 | 1034 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxExemptReason1Code | 1040 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxType16Code | 1073 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxType17Code | 1093 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxType1Choice | 1115 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxType3Choice | 1121 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxableIncomePerShareCalculated2Choice | 1127 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxableIncomePerShareCalculated2Code | 1133 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxationBasis2Code | 1140 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TaxationBasis5Code | 1146 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TickerIdentifier | 1155 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TotalFeesAndTaxes44 | 1161 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TradeTransactionCondition5Code | 1172 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TradeTransactionCondition8Choice | 1178 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Transfer39 | 1184 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TransferInFunction1Code | 1207 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TransferInInstructionV10 | 1213 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TransferReason1Choice | 1229 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TransferReason1Code | 1235 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TypeOfIdentification1Code | 1250 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TypeOfPrice10Code | 1261 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}TypeOfPrice46Choice | 1277 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}UKTaxGroupUnit1Code | 1283 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Unit14 | 1289 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}Unit1Choice | 1302 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}UnitPrice23 | 1308 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}ValorenIdentifier | 1319 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}WaivingInstruction1Code | 1322 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}WaivingInstruction2Choice | 1328 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}WertpapierIdentifier | 1334 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.005.001.10}YesNoIndicator | 1337 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 4 |
| choice | 30 |
| complexType | 94 |
| element | 366 |
| enumeration | 220 |
| extension | 4 |
| fractionDigits | 10 |
| maxLength | 11 |
| minInclusive | 5 |
| minLength | 11 |
| pattern | 11 |
| restriction | 79 |
| schema | 1 |
| sequence | 60 |
| simpleContent | 4 |
| simpleType | 79 |
| totalDigits | 10 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
