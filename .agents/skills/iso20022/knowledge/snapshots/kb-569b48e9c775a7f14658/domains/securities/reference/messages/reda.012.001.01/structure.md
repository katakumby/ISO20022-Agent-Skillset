---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "reda.012.001.01"
message_family: "reda.012"
namespace: "urn:iso:std:iso:20022:tech:xsd:reda.012.001.01"
source_ids: ["src-000267"]
source_editions: ["june-2021"]
---

# reda.012.001.01 structure

[src-000267](../../../../../raw-input/target2securities_t2s/reda.012.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:reda.012.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:reda.012.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ActiveCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ActiveCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ActiveCurrencyAndAmount_SimpleType | 19 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ActiveCurrencyAndAmount | 26 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ActiveCurrencyCode | 33 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ActiveOrHistoricCurrencyAnd13DecimalAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}AddressType1Code | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}AddressType2Code | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}AmountOrPercentageRange1 | 73 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}AnyBICDec2014Identifier | 79 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Appearance1Code | 84 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Appearance3Choice | 96 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}AssignmentMethod1Code | 102 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}AssignmentMethod2Choice | 108 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}BaseOneRate | 114 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}BenchmarkCurve6 | 120 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}BenchmarkCurveName1Code | 130 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}BenchmarkCurveName7Choice | 142 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}BusinessError4 | 148 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}CFIOct2015Identifier | 154 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}CalculationType1Code | 159 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}CalculationType3Choice | 196 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}CallType1Code | 202 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}CallType3Choice | 208 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ClassificationType2 | 214 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}CommonFinancialInstrumentAttributes11 | 221 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}CommunicationAddress3 | 277 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}CountryCode | 287 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}DateAndDateTime2Choice | 292 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}DateTimePeriod1 | 298 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}DateTimePeriod1Choice | 304 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}DateTimePeriod2 | 311 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Debt5 | 317 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}DecimalNumber | 398 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Derivative4 | 404 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}DistributionPolicy1Code | 410 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}DistributionPolicy2Choice | 416 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Document | 422 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Equity3 | 427 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ErrorHandling3Choice | 436 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ErrorHandling5 | 442 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Exact4AlphaNumericText | 448 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ExternalFinancialInstrumentIdentificationType1Code | 453 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ExternalFinancialInstrumentProductType1Code | 459 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ExternalSystemErrorHandling1Code | 465 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}FinancialInstrument97 | 471 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}FinancialInstrumentForm2 | 479 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}FinancialInstrumentIdentificationValidity3 | 485 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}FinancialInstrumentName2 | 491 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}FinancialInstrumentQuantity1Choice | 498 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}FormOfSecurity1Code | 505 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}FormOfSecurity8Choice | 511 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Frequency35Choice | 517 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Frequency5Code | 523 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Future4 | 537 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}GenericIdentification1 | 548 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}GenericIdentification13 | 555 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}GenericIdentification30 | 562 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}GenericIdentification36 | 569 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}GlobalNote1Code | 576 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}GlobalNote2Choice | 582 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ISIN2021Identifier | 588 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ISODate | 593 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ISODateTime | 596 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ISOYearMonth | 599 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}IdentificationSource3Choice | 602 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}ImpliedCurrencyAndAmount | 608 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InitialPhysicalForm1Code | 615 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InitialPhysicalForm2Code | 622 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InitialPhysicalForm3Choice | 628 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InitialPhysicalForm4Choice | 634 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InstrumentSubStructureType1Code | 640 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InstrumentSubStructureType2Choice | 664 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InterestType3Code | 670 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InvestorRestrictionType1Code | 680 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InvestorRestrictionType3Choice | 687 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InvestorType1Code | 693 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}InvestorType3Choice | 701 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Issuance6 | 707 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}IssuanceAccount2 | 722 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Jurisdiction1 | 728 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}LEIIdentifier | 734 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}LegalRestrictions1Code | 739 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}LegalRestrictions2Code | 746 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}LegalRestrictions4Choice | 755 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}LegalRestrictions5Choice | 761 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}MICIdentifier | 767 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}MaturityRedemptionType1Code | 772 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}MaturityRedemptionType3Choice | 783 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max140Text | 789 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max15NumericText | 795 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max16Text | 800 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max256Text | 806 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max350Text | 812 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max35Text | 818 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max3NumericText | 824 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max4AlphaNumericText | 829 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max5NumericText | 836 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Max70Text | 841 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}MessageHeader12 | 847 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}NameAndAddress4 | 854 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}NameAndAddress5 | 860 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Number | 866 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Operation1Code | 872 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Operator1Code | 879 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Option15 | 888 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}OptionParty1Code | 908 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}OptionParty3Choice | 914 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}OptionStyle1Choice | 920 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}OptionStyle1Code | 926 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}OptionType1Code | 935 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}OptionType8Choice | 941 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Organisation38 | 947 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}OriginalBusinessInstruction1 | 962 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}OtherIdentification1 | 969 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Pagination1 | 976 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PartyIdentification120Choice | 982 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PartyIdentification136 | 989 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PartyIdentification177Choice | 995 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PaymentDirectionIndicator | 1001 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PercentageRate | 1004 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PhoneNumber | 1010 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PostalAddress1 | 1015 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PostalAddress3 | 1027 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PreferenceToIncome1Code | 1035 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PreferenceToIncome5Choice | 1041 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Price8 | 1047 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PriceRateOrAmount3Choice | 1054 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PriceValue1 | 1060 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PriceValueType3Code | 1065 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PutType1Code | 1080 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}PutType3Choice | 1087 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}RateAndAmountFormat1Choice | 1093 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}RateOrAbsoluteValue1Choice | 1100 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}RateType12Code | 1106 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}RateType12FormatChoice | 1113 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}RestrictionType1Code | 1119 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecuritiesAccount19 | 1128 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecuritiesPaymentStatus1Code | 1135 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecuritiesPaymentStatus5Choice | 1142 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecuritiesTransactionType11Code | 1148 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecuritiesTransactionType31Choice | 1154 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityAttributes11 | 1160 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityCSDLink7 | 1167 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityIdentification39 | 1178 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityOrBusinessError4Choice | 1185 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityOrOperationalError4Choice | 1191 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityReportV01 | 1197 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityRestriction3 | 1205 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityRestrictionType2Choice | 1214 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityStatus2Code | 1220 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityStatus3Choice | 1227 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SecurityWithHoldingTax1 | 1233 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SettleStyle1Code | 1239 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SettleStyle2Choice | 1245 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SettlementInformation17 | 1251 |
| [type-0160](types/type-0160.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SettlementType1Code | 1260 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SettlementType3Choice | 1266 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SettlementUnitType1Code | 1272 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SettlementUnitType3Choice | 1278 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Standardisation1Code | 1284 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Standardisation3Choice | 1291 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SupplementaryData1 | 1297 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SupplementaryDataEnvelope1 | 1303 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SystemPartyIdentification2Choice | 1308 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}SystemPartyIdentification8 | 1314 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}TEFRARules1Code | 1320 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}TEFRARules3Choice | 1326 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Term1 | 1332 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}TimeUnit1Code | 1338 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}TimeUnit3Choice | 1349 |
| [type-0175](types/type-0175.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}TradeTransactionCondition2Code | 1355 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}TradeTransactionCondition7Choice | 1372 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}TradingParameters2 | 1378 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}TypeOfPrice1Code | 1390 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}UnderlyingAttributes4 | 1407 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}UnitOfMeasure7Choice | 1425 |
| [type-0181](types/type-0181.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}UnitOfMeasure9Code | 1431 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}UnitOrFaceAmount1Choice | 1485 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}Warrant4 | 1491 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}WarrantStyle1Code | 1499 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}WarrantStyle3Choice | 1506 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}YesNoIndicator | 1512 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:reda.012.001.01}YieldCalculation6 | 1515 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 50 |
| complexType | 107 |
| element | 442 |
| enumeration | 276 |
| extension | 3 |
| fractionDigits | 8 |
| maxLength | 10 |
| minInclusive | 4 |
| minLength | 10 |
| pattern | 14 |
| restriction | 79 |
| schema | 1 |
| sequence | 54 |
| simpleContent | 3 |
| simpleType | 79 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
