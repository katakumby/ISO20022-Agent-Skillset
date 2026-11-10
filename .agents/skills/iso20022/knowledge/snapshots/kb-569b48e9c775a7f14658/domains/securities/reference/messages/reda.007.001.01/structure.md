---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.007.001.01"
message_family: "reda.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.007.001.01"
source_ids: ["src-000263"]
source_editions: ["june-2021"]
---

# reda.007.001.01 structure

[src-000263](../../../../../raw-input/target2securities_t2s/reda.007.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.007.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.007.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ActiveCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ActiveCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ActiveCurrencyAndAmount_SimpleType | 19 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ActiveCurrencyAndAmount | 26 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ActiveCurrencyCode | 33 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ActiveOrHistoricCurrencyAnd13DecimalAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}AddressType1Code | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}AddressType2Code | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}AmountOrPercentageRange1 | 73 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}AnyBICDec2014Identifier | 79 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Appearance1Code | 84 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Appearance3Choice | 96 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}AssignmentMethod1Code | 102 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}AssignmentMethod2Choice | 108 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}BaseOneRate | 114 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}BenchmarkCurve6 | 120 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}BenchmarkCurveName1Code | 130 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}BenchmarkCurveName7Choice | 142 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}CFIOct2015Identifier | 148 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}CalculationType1Code | 153 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}CalculationType3Choice | 190 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}CallType1Code | 196 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}CallType3Choice | 202 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ClassificationType2 | 208 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}CommonFinancialInstrumentAttributes12 | 215 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}CommunicationAddress3 | 272 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}CountryCode | 282 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}DateAndDateTime2Choice | 287 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}DateTimePeriod1 | 293 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}DateTimePeriod1Choice | 299 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}DateTimePeriod2 | 306 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Debt5 | 312 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}DecimalNumber | 393 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Derivative4 | 399 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}DistributionPolicy1Code | 405 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}DistributionPolicy2Choice | 411 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Document | 417 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Equity3 | 422 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Exact4AlphaNumericText | 431 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ExternalFinancialInstrumentIdentificationType1Code | 436 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ExternalFinancialInstrumentProductType1Code | 442 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ExternalSecuritiesUpdateReason1Code | 448 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}FinancialInstrument97 | 454 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}FinancialInstrumentForm2 | 462 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}FinancialInstrumentQuantity1Choice | 468 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}FormOfSecurity1Code | 475 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}FormOfSecurity8Choice | 481 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Frequency35Choice | 487 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Frequency5Code | 493 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Future4 | 507 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}GenericIdentification1 | 518 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}GenericIdentification13 | 525 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}GenericIdentification30 | 532 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}GenericIdentification36 | 539 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}GlobalNote1Code | 546 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}GlobalNote2Choice | 552 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ISIN2021Identifier | 558 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ISODate | 563 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ISODateTime | 566 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ISOYearMonth | 569 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}IdentificationSource3Choice | 572 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}ImpliedCurrencyAndAmount | 578 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InitialPhysicalForm1Code | 585 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InitialPhysicalForm2Code | 592 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InitialPhysicalForm3Choice | 598 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InitialPhysicalForm4Choice | 604 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InstrumentSubStructureType1Code | 610 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InstrumentSubStructureType2Choice | 634 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InterestType3Code | 640 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InvestorRestrictionType1Code | 650 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InvestorRestrictionType3Choice | 657 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InvestorType1Code | 663 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}InvestorType3Choice | 671 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Issuance5 | 677 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Jurisdiction1 | 693 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}LEIIdentifier | 699 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}LegalRestrictions1Code | 704 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}LegalRestrictions2Code | 711 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}LegalRestrictions4Choice | 720 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}LegalRestrictions5Choice | 726 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}MICIdentifier | 732 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}MaturityRedemptionType1Code | 737 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}MaturityRedemptionType3Choice | 748 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Max140Text | 754 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Max15NumericText | 760 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Max16Text | 765 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Max256Text | 771 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Max350Text | 777 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Max35Text | 783 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Max3NumericText | 789 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Max4AlphaNumericText | 794 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Max70Text | 801 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}MessageHeader1 | 807 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}NameAndAddress4 | 813 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}NameAndAddress5 | 819 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Number | 825 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Operation1Code | 831 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Operator1Code | 838 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Option15 | 847 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}OptionParty1Code | 867 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}OptionParty3Choice | 873 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}OptionStyle1Choice | 879 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}OptionStyle1Code | 885 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}OptionType1Code | 894 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}OptionType8Choice | 900 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Organisation38 | 906 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}OtherIdentification1 | 921 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PartyIdentification120Choice | 928 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PartyIdentification136 | 935 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PartyIdentification177Choice | 941 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PaymentDirectionIndicator | 947 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PercentageRate | 950 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PhoneNumber | 956 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PostalAddress1 | 961 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PostalAddress3 | 973 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PreferenceToIncome1Code | 981 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PreferenceToIncome5Choice | 987 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Price8 | 993 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PriceRateOrAmount3Choice | 1000 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PriceValue1 | 1006 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PriceValueType3Code | 1011 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PutType1Code | 1026 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}PutType3Choice | 1033 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}RateAndAmountFormat1Choice | 1039 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}RateOrAbsoluteValue1Choice | 1046 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}RateType12Code | 1052 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}RateType12FormatChoice | 1059 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}RestrictionType1Code | 1065 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecuritiesPaymentStatus1Code | 1074 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecuritiesPaymentStatus5Choice | 1081 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecuritiesTransactionType11Code | 1087 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecuritiesTransactionType31Choice | 1093 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecuritiesUpdateReason1Choice | 1099 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecurityAttributes12 | 1105 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecurityIdentification39 | 1112 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecurityMaintenanceRequestV01 | 1119 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecurityRestriction3 | 1128 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecurityRestrictionType2Choice | 1137 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecurityStatus2Code | 1143 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecurityStatus3Choice | 1150 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SecurityWithHoldingTax1 | 1156 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SettleStyle1Code | 1162 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SettleStyle2Choice | 1168 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SettlementInformation17 | 1174 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SettlementType1Code | 1183 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SettlementType3Choice | 1189 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SettlementUnitType1Code | 1195 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SettlementUnitType3Choice | 1201 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Standardisation1Code | 1207 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Standardisation3Choice | 1214 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SupplementaryData1 | 1220 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}SupplementaryDataEnvelope1 | 1226 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}TEFRARules1Code | 1231 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}TEFRARules3Choice | 1237 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Term1 | 1243 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}TimeUnit1Code | 1249 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}TimeUnit3Choice | 1260 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}TradeTransactionCondition2Code | 1266 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}TradeTransactionCondition7Choice | 1283 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}TradingParameters2 | 1289 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}TypeOfPrice1Code | 1301 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}UnderlyingAttributes4 | 1318 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}UnitOfMeasure7Choice | 1336 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}UnitOfMeasure9Code | 1342 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}UnitOrFaceAmount1Choice | 1396 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}UpdateType35Choice | 1402 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}UpdateType36Choice | 1409 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}Warrant4 | 1415 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}WarrantStyle1Code | 1423 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}WarrantStyle3Choice | 1430 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}YesNoIndicator | 1436 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.007.001.01}YieldCalculation6 | 1439 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 49 |
| complexType | 96 |
| element | 415 |
| enumeration | 276 |
| extension | 3 |
| fractionDigits | 8 |
| maxLength | 10 |
| minInclusive | 4 |
| minLength | 10 |
| pattern | 13 |
| restriction | 78 |
| schema | 1 |
| sequence | 44 |
| simpleContent | 3 |
| simpleType | 78 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
