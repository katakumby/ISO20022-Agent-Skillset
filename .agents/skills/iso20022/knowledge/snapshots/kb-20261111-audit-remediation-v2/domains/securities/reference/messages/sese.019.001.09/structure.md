---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.019.001.09"
message_family: "sese.019"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.019.001.09"
source_ids: ["src-000135"]
source_editions: ["2025-2026"]
---

# sese.019.001.09 structure

[src-000135](../../../../../raw-input/investment_funds/sese.019.001.09.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.019.001.09`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.019.001.09 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Account37 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AccountHoldingInformationRequestV09 | 16 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AccountOwnershipType6Code | 37 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ActiveCurrencyAnd13DecimalAmount_SimpleType | 62 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ActiveCurrencyAnd13DecimalAmount | 69 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ActiveCurrencyCode | 76 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ActiveOrHistoricCurrencyAndAmount_SimpleType | 81 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ActiveOrHistoricCurrencyAndAmount | 88 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ActiveOrHistoricCurrencyCode | 95 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AdditionalInformation15 | 100 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AdditionalReference10 | 106 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AdditionalReference11 | 113 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AddressType2Code | 120 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AlternatePartyIdentification7 | 130 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AlternateSecurityIdentification7 | 137 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AnyBICDec2014Identifier | 143 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}AustrianBankleitzahlIdentifier | 148 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}BelgianIdentifier | 153 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}BlockChainAddressWallet3 | 156 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Bloomberg2Identifier | 163 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}BusinessFlowDirectionType1Code | 168 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}CFIOct2015Identifier | 174 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}CHIPSParticipantIdentifier | 179 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}CHIPSUniversalIdentifier | 184 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}CUSIPIdentifier | 189 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}CanadianPaymentsARNIdentifier | 192 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}CashAsset2 | 197 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}CashAssetType1Choice | 204 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}CashAssetType1Code | 210 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ClassificationType32Choice | 216 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ClearingSystemMemberIdentification2Choice | 222 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ConsolidatedTapeAssociationIdentifier | 249 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}CountryCode | 255 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}DTI2024Identifier | 260 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}DateAndAmount2 | 265 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}DateAndDateTime2Choice | 271 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Document | 277 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}DutchIdentifier | 282 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}EuroclearClearstreamIdentifier | 285 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Exact4AlphaNumericText | 291 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Extension1 | 296 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ExtensiveBranchNetworkIdentifier | 302 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}FedwireRoutingNumberIdentifier | 307 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}FinancialInstrument104Choice | 312 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}FinancialInstrument111 | 319 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}FinancialInstrumentIdentification11 | 333 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}FundPortfolio9Choice | 341 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}FundSettlementParameters27 | 348 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}GenderCode | 357 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}GeneralInvestment2 | 363 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}GeneralInvestmentAccountType2Choice | 372 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}GeneralInvestmentAccountType2Code | 378 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}GenericIdentification1 | 384 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}GenericIdentification30 | 391 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}GenericIdentification36 | 398 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}GenericIdentification78 | 405 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}GermanBankleitzahlIdentifier | 411 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}HellenicBankIdentificationCodeIdentifier | 416 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}HolderType1Code | 421 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}HongKongBankIdentifier | 427 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ISINOct2015Identifier | 432 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ISODate | 437 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ISODateTime | 440 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ISOYear | 443 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ISOYearMonth | 446 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}IdentificationSource1Choice | 449 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}IdentificationType42Choice | 455 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}IndianFinancialSystemCodeIdentifier | 461 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}IndividualPerson8 | 466 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}InvestmentAccount69 | 478 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}IrishNSCIdentifier | 486 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ItalianDomesticIdentifier | 491 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}LEIIdentifier | 496 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}MarketPracticeVersion1 | 501 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Max140Text | 508 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Max16Text | 514 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Max350Text | 520 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Max35Text | 526 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Max70Text | 532 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}MessageIdentification1 | 538 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}NameAndAddress5 | 544 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}NamePrefix1Code | 550 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}NewZealandNCCIdentifier | 558 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Organisation36 | 563 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}OtherAsset2 | 576 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}OtherAsset2Choice | 586 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}OtherAsset2Code | 592 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyIdentification123Choice | 601 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyIdentification125Choice | 608 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyIdentification126Choice | 615 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyIdentification132 | 621 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyIdentification139 | 630 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyIdentification140 | 636 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyIdentification257Choice | 642 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyIdentification315 | 650 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyIdentificationAndAccount194 | 660 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyTextInformation1 | 671 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PartyTextInformation6 | 678 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}Pension6 | 686 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PensionPolicy1 | 697 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PensionSchemeType3Choice | 704 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PensionSchemeType3Code | 710 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PensionTransferScope1Choice | 734 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PensionTransferScope1Code | 740 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PersonIdentificationType7Code | 748 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PolishNationalClearingCodeIdentifier | 755 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PortfolioTransfer17 | 760 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PortugueseNCCIdentifier | 769 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PostalAddress1 | 774 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PreviousAll | 786 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}PreviousYear2Choice | 791 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}QUICKIdentifier | 797 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}RICIdentifier | 800 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}RussianCentralBankIdentificationCodeIdentifier | 806 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SEDOLIdentifier | 811 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SafekeepingPlace1Code | 814 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SafekeepingPlace2Code | 822 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SafekeepingPlaceFormat28Choice | 828 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SafekeepingPlaceTypeAndIdentification1 | 836 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SafekeepingPlaceTypeAndText6 | 842 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SecuritiesAccount19 | 848 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SecurityIdentification46Choice | 855 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SettlementParties131 | 875 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SettlementTransactionCondition11Code | 885 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SettlementTransactionCondition30Choice | 890 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SicovamIdentifier | 896 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SmallNetworkIdentifier | 899 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SouthAfricanNCCIdentifier | 904 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SpanishDomesticInterbankingIdentifier | 909 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SubAccount5 | 914 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SwissBCIdentifier | 921 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}SwissSICIdentifier | 926 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TaxEfficientProduct4 | 931 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TaxEfficientProductType2Choice | 939 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TaxEfficientProductType2Code | 945 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TaxReference1 | 962 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TaxReferenceParty1Choice | 969 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TaxReferenceType1Choice | 975 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TickerIdentifier | 981 |
| [type-0141](types/type-0141.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TradeTransactionCondition5Code | 987 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TradeTransactionCondition8Choice | 993 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}TypeOfIdentification1Code | 999 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}UKDomesticSortCodeIdentifier | 1010 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}ValorenIdentifier | 1015 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}WertpapierIdentifier | 1018 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.019.001.09}YesNoIndicator | 1021 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 2 |
| choice | 24 |
| complexType | 71 |
| element | 284 |
| enumeration | 102 |
| extension | 2 |
| fractionDigits | 2 |
| maxLength | 9 |
| minInclusive | 2 |
| minLength | 9 |
| pattern | 33 |
| restriction | 75 |
| schema | 1 |
| sequence | 45 |
| simpleContent | 2 |
| simpleType | 75 |
| totalDigits | 2 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
