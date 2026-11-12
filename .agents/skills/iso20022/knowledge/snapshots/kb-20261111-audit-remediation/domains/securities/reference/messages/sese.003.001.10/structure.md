---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.003.001.10"
message_family: "sese.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.003.001.10"
source_ids: ["src-000122"]
source_editions: ["2025-2026"]
---

# sese.003.001.10 structure

[src-000122](../../../../../raw-input/investment_funds/sese.003.001.10.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.003.001.10`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.003.001.10 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Account27 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Account38 | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveCurrencyAnd13DecimalAmount_SimpleType | 21 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveCurrencyAnd13DecimalAmount | 28 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveCurrencyAndAmount_SimpleType | 35 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveCurrencyAndAmount | 42 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveCurrencyCode | 49 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 54 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount | 61 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveOrHistoricCurrencyAndAmount_SimpleType | 68 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveOrHistoricCurrencyAndAmount | 75 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ActiveOrHistoricCurrencyCode | 82 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}AdditionalReference10 | 87 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}AdditionalReference11 | 94 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}AddressType2Code | 101 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}AlternatePartyIdentification7 | 111 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}AlternateSecurityIdentification7 | 118 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}AnyBICDec2014Identifier | 124 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}BaseOneRate | 129 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}BelgianIdentifier | 135 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}BeneficiaryCertificationCompletion1Code | 138 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}BlockChainAddressWallet3 | 145 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Bloomberg2Identifier | 152 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}BusinessFlowType1Code | 157 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}CUSIPIdentifier | 164 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ChargeBasis2Choice | 167 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ChargeBearer1Code | 173 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ChargeOrCommissionDiscount1 | 180 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ChargeOrCommissionDiscount2 | 187 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ChargePaymentMethod1Choice | 194 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ChargePaymentMethod1Code | 200 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ChargeType10Choice | 206 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ChargeType6Choice | 212 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ConsolidatedTapeAssociationIdentifier | 218 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ContactIdentification2 | 224 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}CopyInformation5 | 235 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}CountryCode | 241 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}DTI2024Identifier | 246 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}DateAndDateTime2Choice | 251 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}DecimalNumber | 257 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}DeliveryParameters4 | 263 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}DigitalPaymentSettlement3 | 270 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}DistributionPolicy1Code | 277 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Document | 283 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}DutchIdentifier | 288 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}EuroclearClearstreamIdentifier | 291 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Exact4AlphaNumericText | 297 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ExemptionReason1Choice | 302 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Extension1 | 308 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Fee11 | 314 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Fee7 | 328 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Fees2 | 338 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}FinancialInstrument116 | 344 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}FinancialInstrumentIdentificationType1Code | 356 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}FinancialInstrumentQuantity33Choice | 384 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ForeignExchangeTerms37 | 392 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}FormOfSecurity1Code | 403 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}FundSettlementParameters25 | 409 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}FundSettlementParameters26 | 417 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}GenericIdentification1 | 425 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}GenericIdentification27 | 432 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}GenericIdentification30 | 439 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}GenericIdentification36 | 446 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}GenericIdentification47 | 453 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}GenericIdentification78 | 460 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}HoldingsPlanType1Code | 466 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ISINOct2015Identifier | 473 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ISODate | 478 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ISODateTime | 481 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ISOYearMonth | 484 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}IdentificationSource1Choice | 487 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}IdentificationSource6Choice | 493 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}IdentificationType42Choice | 499 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ImpliedCurrencyAndAmount | 505 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}IncomePreference2Code | 512 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Intermediary43 | 518 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}InvestmentAccount82 | 526 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}InvestmentFundFee2Code | 544 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}InvestmentFundFee3Code | 555 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}InvestmentFundRole2Code | 578 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}LEIIdentifier | 591 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}MarketPracticeVersion1 | 596 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Max140Text | 603 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Max16Text | 609 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Max256Text | 615 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Max30DecimalNumber | 621 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Max350Text | 627 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Max35Text | 633 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Max4AlphaNumericText | 639 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Max70Text | 646 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}MessageIdentification1 | 652 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}NameAndAddress4 | 658 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}NameAndAddress5 | 664 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}NamePrefix1Code | 670 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Number | 678 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}OtherAmount1 | 684 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}OtherAmountType1Choice | 690 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}OtherAmountType1Code | 696 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}OtherIdentification8 | 702 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PartyIdentification123Choice | 709 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PartyIdentification125Choice | 716 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PartyIdentification139 | 723 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PartyIdentification257Choice | 729 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PartyIdentification315 | 737 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PartyIdentificationAndAccount194 | 747 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PartyTextInformation1 | 758 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PartyTextInformation6 | 765 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PercentageRate | 773 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PhoneNumber | 779 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PhysicalTransferType1Code | 784 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PostalAddress1 | 790 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PriceMethod1Code | 802 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}PriceValue1 | 808 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ProprietaryQuantity8 | 813 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}QUICKIdentifier | 821 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Quantity48Choice | 824 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}RICIdentifier | 830 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ReceiveInformation23 | 836 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Role4Choice | 860 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}RoundingDirection2Code | 866 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SEDOLIdentifier | 872 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SafekeepingPlace1Code | 875 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SafekeepingPlace2Code | 883 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SafekeepingPlaceFormat42Choice | 889 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SafekeepingPlaceTypeAndIdentification1 | 898 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SafekeepingPlaceTypeAndText6 | 904 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SecuritiesAccount19 | 910 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SecurityIdentification46Choice | 917 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SecurityIdentification50 | 937 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SettlementParties131 | 944 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SettlementTransactionCondition11Code | 954 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SettlementTransactionCondition30Choice | 959 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SicovamIdentifier | 965 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}StampDutyType2Code | 968 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}SubAccount5 | 974 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Tax35 | 981 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Tax38 | 991 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxBasis1Choice | 1003 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxCalculationInformation10 | 1009 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxCalculationInformation11 | 1015 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxExemptReason1Code | 1021 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxType16Code | 1054 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxType17Code | 1074 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxType1Choice | 1096 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxType3Choice | 1102 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxableIncomePerShareCalculated2Choice | 1108 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxableIncomePerShareCalculated2Code | 1114 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxationBasis2Code | 1121 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TaxationBasis5Code | 1127 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TickerIdentifier | 1136 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TotalFeesAndTaxes44 | 1142 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TradeTransactionCondition5Code | 1153 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TradeTransactionCondition8Choice | 1159 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Transfer38 | 1165 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TransferOutConfirmationV10 | 1195 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TransferReason1Choice | 1210 |
| [type-0158](types/type-0158.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TransferReason1Code | 1216 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TypeOfIdentification1Code | 1231 |
| [type-0160](types/type-0160.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TypeOfPrice10Code | 1242 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}TypeOfPrice46Choice | 1258 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}UKTaxGroupUnit1Code | 1264 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Unit14 | 1270 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}Unit1Choice | 1283 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}UnitPrice23 | 1289 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}ValorenIdentifier | 1300 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}WaivingInstruction1Code | 1303 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}WaivingInstruction2Choice | 1309 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}WertpapierIdentifier | 1315 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.003.001.10}YesNoIndicator | 1318 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 4 |
| choice | 28 |
| complexType | 92 |
| element | 368 |
| enumeration | 215 |
| extension | 4 |
| fractionDigits | 10 |
| maxLength | 11 |
| minInclusive | 5 |
| minLength | 11 |
| pattern | 11 |
| restriction | 77 |
| schema | 1 |
| sequence | 60 |
| simpleContent | 4 |
| simpleType | 77 |
| totalDigits | 10 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
