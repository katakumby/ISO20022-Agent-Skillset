---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.004.001.07"
message_family: "reda.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.004.001.07"
source_ids: ["src-000111"]
source_editions: ["2025-2026"]
---

# reda.004.001.07 structure

[src-000111](../../../../../raw-input/investment_funds/reda.004.001.07.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.004.001.07`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.004.001.07 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}AccountIdentificationAndName7 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ActiveCurrencyAnd13DecimalAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ActiveCurrencyAnd13DecimalAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ActiveCurrencyAndAmount_SimpleType | 31 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ActiveCurrencyAndAmount | 38 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ActiveCurrencyCode | 45 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}AdditionalInformation15 | 50 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}AdditionalProductInformation3 | 56 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}AdditionalReference10 | 62 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}AddressType2Code | 69 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}AnnualChargePaymentType1Code | 79 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}AnyBICDec2014Identifier | 85 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}AssessmentOfValueRequiredUnderCOLLUKType1Code | 90 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}BusinessDayConvention1Code | 96 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}CFIOct2015Identifier | 102 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}CashAccount205 | 107 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}CashAccount206 | 114 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}CashAccountIdentification8Choice | 121 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ChargeType8Choice | 127 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ContactAttributes5 | 133 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ContactAttributes6 | 145 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}CostsAndCharges2 | 157 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}CountryCode | 164 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}DecimalNumber | 169 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}DistributionPolicy1Code | 175 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}DistributionStrategy1 | 181 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}DistributionStrategy1Choice | 190 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}DividendPolicy1Code | 196 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Document | 203 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}EMTDataReportingVFMUKType1Code | 208 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}EUSavingsDirective1Code | 213 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}EventFrequency5Code | 220 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}EventFrequency8Code | 234 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ExPostCostCalculationBasis1Choice | 253 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ExPostCostCalculationBasis1Code | 259 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Exact4AlphaNumericText | 265 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ExtendedParty13 | 270 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Extension1 | 276 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ExternalAccountIdentification1Code | 282 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ExternalFinancialInstrumentIdentificationType1Code | 288 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}FinancialInstrument96 | 294 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Forms1 | 326 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Frequency20Choice | 332 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}FundOrderType10Code | 338 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}FundOrderType5Choice | 347 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}FundParties1 | 353 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}FundPaymentType1Choice | 361 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}FundPaymentType1Code | 367 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}FundReferenceDataReport5 | 377 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}FundReferenceDataReportV07 | 408 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}GenericAccountIdentification1 | 417 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}GenericIdentification1 | 424 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}GenericIdentification3 | 431 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}GenericIdentification36 | 437 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}GenericIdentification47 | 444 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}GovernanceProcess1Choice | 451 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}GovernanceProcessType1Code | 457 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}HoldingTransferable1Code | 465 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}IBAN2007Identifier | 472 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ISINOct2015Identifier | 477 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ISODate | 482 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ISODateTime | 485 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ISOTime | 488 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ISOYearMonth | 491 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}IdentificationSource3Choice | 494 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}IndividualCostOrCharge2 | 500 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}IntendedOrActual2Code | 511 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestmentFundMiFIDFee2Code | 517 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestmentFundPlanType1Choice | 550 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestmentFundPlanType1Code | 556 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestmentNeed2Choice | 563 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestmentNeed2Code | 569 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestmentPlanCharacteristics1 | 576 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestmentRestrictions3 | 588 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestorKnowledge1 | 610 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestorRequirements4 | 619 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestorType2 | 633 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestorType2Code | 641 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestorType3Code | 648 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}InvestorType4Code | 656 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}LEIIdentifier | 664 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}LocalMarketAnnex6 | 669 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}LossBearing2 | 680 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}MainFundOrderDeskLocation1 | 690 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}MarketPracticeVersion1 | 696 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max140Text | 703 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max16Text | 709 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max1Number | 715 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max2048Text | 721 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max256Text | 727 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max34Text | 733 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max350Text | 739 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max35Text | 745 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max4AlphaNumericText | 751 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Max70Text | 758 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}MessageIdentification1 | 764 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}NameAndAddress5 | 770 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}NotionalOrUnitBased1Choice | 776 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}NotionalOrUnitBased1Code | 782 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Number | 788 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OrderDesk1 | 794 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OtherDistributionStrategy1 | 801 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OtherIdentification1 | 808 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OtherInvestmentNeed1 | 815 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OtherReviewRelatedToValueAndOrChargesUKType1Code | 822 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OtherTargetMarket1 | 828 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OtherTargetMarketInvestor1 | 834 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OtherTargetMarketInvestorKnowledge1 | 841 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OtherTargetMarketLossBearing1 | 848 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OtherTargetMarketRiskTolerance1 | 855 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OutcomeOfCOLLAssessmentOfValueUKType1Code | 862 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}OutcomeOfPRINValueAssessmentOrReviewUKType1Code | 868 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}PartyIdentification125Choice | 874 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}PartyIdentification139 | 881 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}PaymentInstrument16 | 887 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}PercentageRate | 894 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}Period15 | 900 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}PhoneNumber | 906 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}PlusOrMinusIndicator | 911 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}PostalAddress1 | 914 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}PriceMethod1Code | 926 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ProcessingCharacteristics10 | 932 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ProcessingCharacteristics11 | 952 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ProcessingCharacteristics12 | 972 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ProcessingCharacteristics9 | 992 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ProductStructure1Choice | 1011 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ProductStructure1Code | 1017 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}QuotationType1Choice | 1029 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}QuotationType1Code | 1035 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ReferToFundOrderDesk1Code | 1041 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}RiskLevel1Code | 1046 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}RiskTolerance1 | 1053 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}RoundingDirection2Code | 1063 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}SecurityClassificationType2Choice | 1069 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}SecurityIdentification40 | 1075 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}SecurityIdentification47 | 1082 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}SignatureType1Code | 1107 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}SustainabilityPreferences2Code | 1115 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TargetMarket1Choice | 1121 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TargetMarket1Code | 1127 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TargetMarket2Code | 1134 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TargetMarket3Choice | 1140 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TargetMarket3Code | 1147 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TargetMarket4 | 1153 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TargetMarket5Choice | 1164 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TimeFrame10 | 1170 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TimeFrame11 | 1178 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TimeFrame2Code | 1186 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TimeFrame7Choice | 1195 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TimeFrame8 | 1201 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TimeFrame8Choice | 1209 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TimeFrame9 | 1215 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TimeFrame9Choice | 1223 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}TimeHorizon2Choice | 1229 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}UTCOffset1 | 1235 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}UnitsOrAmount1Choice | 1241 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ValuationDealingProcessingCharacteristics3 | 1247 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}ValueForMoney1 | 1260 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.004.001.07}YesNoIndicator | 1272 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 2 |
| choice | 25 |
| complexType | 90 |
| element | 427 |
| enumeration | 158 |
| extension | 2 |
| fractionDigits | 6 |
| maxLength | 11 |
| minInclusive | 2 |
| minLength | 11 |
| pattern | 10 |
| restriction | 70 |
| schema | 1 |
| sequence | 63 |
| simpleContent | 2 |
| simpleType | 70 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/7a8b345d67d413021774c579.md) · [Message](index.md)
