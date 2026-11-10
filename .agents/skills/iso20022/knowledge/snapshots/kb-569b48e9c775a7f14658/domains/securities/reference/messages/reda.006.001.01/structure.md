---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.006.001.01"
message_family: "reda.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.006.001.01"
source_ids: ["src-000262"]
source_editions: ["june-2021"]
---

# reda.006.001.01 structure

[src-000262](../../../../../raw-input/target2securities_t2s/reda.006.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.006.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.006.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ActiveCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ActiveCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ActiveCurrencyAndAmount_SimpleType | 19 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ActiveCurrencyAndAmount | 26 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ActiveCurrencyCode | 33 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ActiveOrHistoricCurrencyAnd13DecimalAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}AddressType1Code | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}AddressType2Code | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}AmountOrPercentageRange1 | 73 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}AnyBICDec2014Identifier | 79 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Appearance1Code | 84 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Appearance3Choice | 96 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}AssignmentMethod1Code | 102 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}AssignmentMethod2Choice | 108 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}BaseOneRate | 114 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}BenchmarkCurve6 | 120 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}BenchmarkCurveName1Code | 130 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}BenchmarkCurveName7Choice | 142 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}CFIOct2015Identifier | 148 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}CalculationType1Code | 153 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}CalculationType3Choice | 190 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}CallType1Code | 196 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}CallType3Choice | 202 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ClassificationType2 | 208 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}CommonFinancialInstrumentAttributes10 | 215 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}CommunicationAddress3 | 271 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}CountryCode | 281 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}DateAndDateTime2Choice | 286 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}DateTimePeriod1 | 292 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}DateTimePeriod1Choice | 298 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}DateTimePeriod2 | 305 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Debt5 | 311 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}DecimalNumber | 392 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Derivative4 | 398 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}DistributionPolicy1Code | 404 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}DistributionPolicy2Choice | 410 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Document | 416 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Equity3 | 421 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Exact4AlphaNumericText | 430 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ExternalFinancialInstrumentIdentificationType1Code | 435 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ExternalFinancialInstrumentProductType1Code | 441 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}FinancialInstrument97 | 447 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}FinancialInstrumentForm2 | 455 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}FinancialInstrumentQuantity1Choice | 461 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}FormOfSecurity1Code | 468 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}FormOfSecurity8Choice | 474 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Frequency35Choice | 480 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Frequency5Code | 486 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Future4 | 500 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}GenericIdentification1 | 511 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}GenericIdentification13 | 518 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}GenericIdentification30 | 525 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}GenericIdentification36 | 532 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}GlobalNote1Code | 539 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}GlobalNote2Choice | 545 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ISIN2021Identifier | 551 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ISODate | 556 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ISODateTime | 559 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ISOYearMonth | 562 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}IdentificationSource3Choice | 565 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}ImpliedCurrencyAndAmount | 571 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InitialPhysicalForm1Code | 578 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InitialPhysicalForm2Code | 585 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InitialPhysicalForm3Choice | 591 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InitialPhysicalForm4Choice | 597 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InstrumentSubStructureType1Code | 603 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InstrumentSubStructureType2Choice | 627 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InterestType3Code | 633 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InvestorRestrictionType1Code | 643 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InvestorRestrictionType3Choice | 650 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InvestorType1Code | 656 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}InvestorType3Choice | 664 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Issuance5 | 670 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Jurisdiction1 | 686 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}LEIIdentifier | 692 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}LegalRestrictions1Code | 697 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}LegalRestrictions2Code | 704 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}LegalRestrictions4Choice | 713 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}LegalRestrictions5Choice | 719 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}MICIdentifier | 725 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}MaturityRedemptionType1Code | 730 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}MaturityRedemptionType3Choice | 741 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Max140Text | 747 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Max15NumericText | 753 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Max16Text | 758 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Max256Text | 764 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Max350Text | 770 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Max35Text | 776 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Max3NumericText | 782 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Max4AlphaNumericText | 787 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Max70Text | 794 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}MessageHeader1 | 800 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}NameAndAddress4 | 806 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}NameAndAddress5 | 812 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Number | 818 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Operation1Code | 824 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Operator1Code | 831 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Option15 | 840 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}OptionParty1Code | 860 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}OptionParty3Choice | 866 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}OptionStyle1Choice | 872 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}OptionStyle1Code | 878 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}OptionType1Code | 887 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}OptionType8Choice | 893 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Organisation38 | 899 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}OtherIdentification1 | 914 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PartyIdentification120Choice | 921 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PartyIdentification136 | 928 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PartyIdentification177Choice | 934 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PaymentDirectionIndicator | 940 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PercentageRate | 943 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PhoneNumber | 949 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PostalAddress1 | 954 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PostalAddress3 | 966 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PreferenceToIncome1Code | 974 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PreferenceToIncome5Choice | 980 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Price8 | 986 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PriceRateOrAmount3Choice | 993 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PriceValue1 | 999 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PriceValueType3Code | 1004 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PutType1Code | 1019 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}PutType3Choice | 1026 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}RateAndAmountFormat1Choice | 1032 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}RateOrAbsoluteValue1Choice | 1039 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}RateType12Code | 1045 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}RateType12FormatChoice | 1052 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}RestrictionType1Code | 1058 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecuritiesPaymentStatus1Code | 1067 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecuritiesPaymentStatus5Choice | 1074 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecuritiesTransactionType11Code | 1080 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecuritiesTransactionType31Choice | 1086 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecurityAttributes10 | 1092 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecurityCreationRequestV01 | 1099 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecurityIdentification39 | 1106 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecurityRestriction3 | 1113 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecurityRestrictionType2Choice | 1122 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecurityStatus2Code | 1128 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecurityStatus3Choice | 1135 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SecurityWithHoldingTax1 | 1141 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SettleStyle1Code | 1147 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SettleStyle2Choice | 1153 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SettlementInformation17 | 1159 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SettlementType1Code | 1168 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SettlementType3Choice | 1174 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SettlementUnitType1Code | 1180 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SettlementUnitType3Choice | 1186 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Standardisation1Code | 1192 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Standardisation3Choice | 1199 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SupplementaryData1 | 1205 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}SupplementaryDataEnvelope1 | 1211 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}TEFRARules1Code | 1216 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}TEFRARules3Choice | 1222 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Term1 | 1228 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}TimeUnit1Code | 1234 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}TimeUnit3Choice | 1245 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}TradeTransactionCondition2Code | 1251 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}TradeTransactionCondition7Choice | 1268 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}TradingParameters2 | 1274 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}TypeOfPrice1Code | 1286 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}UnderlyingAttributes4 | 1303 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}UnitOfMeasure7Choice | 1321 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}UnitOfMeasure9Code | 1327 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}UnitOrFaceAmount1Choice | 1381 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}Warrant4 | 1387 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}WarrantStyle1Code | 1395 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}WarrantStyle3Choice | 1402 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}YesNoIndicator | 1408 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.006.001.01}YieldCalculation6 | 1411 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 46 |
| complexType | 93 |
| element | 405 |
| enumeration | 276 |
| extension | 3 |
| fractionDigits | 8 |
| maxLength | 9 |
| minInclusive | 4 |
| minLength | 9 |
| pattern | 13 |
| restriction | 77 |
| schema | 1 |
| sequence | 44 |
| simpleContent | 3 |
| simpleType | 77 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
