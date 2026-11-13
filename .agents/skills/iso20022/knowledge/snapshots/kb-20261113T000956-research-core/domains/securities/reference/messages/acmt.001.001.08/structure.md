---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.001.001.08"
message_family: "acmt.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08"
source_ids: ["src-000098"]
source_editions: ["2025-2026"]
---

# acmt.001.001.08 structure

[src-000098](../../../../../raw-input/investment_funds/acmt.001.001.08.xsd); `urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Account23 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Account32 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountDesignation1Choice | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountIdentification4Choice | 23 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountIdentificationAndName5 | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountOpeningInstructionV08 | 35 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountOpeningType1Choice | 55 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountOpeningType1Code | 61 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountOwnershipType4Code | 67 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountParties12Choice | 89 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountParties17 | 97 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountSchemeName1Choice | 115 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountType2Choice | 121 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountUsageType2Choice | 127 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountUsageType2Code | 133 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountingStatus1Choice | 141 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AccountingStatus1Code | 147 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ActiveCurrencyAnd13DecimalAmount_SimpleType | 153 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ActiveCurrencyAnd13DecimalAmount | 160 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ActiveCurrencyAndAmount_SimpleType | 167 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ActiveCurrencyAndAmount | 174 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ActiveCurrencyCode | 181 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ActiveOrHistoricCurrencyCode | 186 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AdditionalReference13 | 191 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AdditiononalInformation13 | 198 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AddressType1Choice | 209 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AddressType1Code | 215 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AddressType2Choice | 221 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AddressType2Code | 227 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AlternateSecurityIdentification7 | 237 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AnyBICDec2014Identifier | 243 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}AustrianBankleitzahlIdentifier | 248 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}BICFIDec2014Identifier | 253 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}BelgianIdentifier | 258 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}BlockedHoldingDetails2 | 261 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}BlockedReason2Choice | 268 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}BlockedReason2Code | 274 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}BlockedStatusReason2 | 287 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}BlockedStatusReason2Choice | 295 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Bloomberg2Identifier | 301 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}BranchData4 | 306 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CHIPSParticipantIdentifier | 313 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CHIPSUniversalIdentifier | 318 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CRSForm1Choice | 323 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CRSFormType1Code | 329 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CRSSource1Choice | 341 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CRSSourceStatus1Code | 347 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CRSStatus1Code | 353 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CRSStatus3Choice | 371 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CRSStatus4 | 377 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CUSIPIdentifier | 384 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CanadianPaymentsARNIdentifier | 387 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CardType1Code | 392 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CashAccount204 | 398 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CashAccountType3Choice | 414 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CashAccountType5Code | 420 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CashSettlement3 | 429 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CertificateType2Code | 435 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CertificationType1Choice | 449 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Cheque4 | 455 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CitizenshipInformation2 | 460 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CivilStatus1Choice | 466 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CivilStatus1Code | 472 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ClearingSystemMemberIdentification4Choice | 483 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Collateral1Code | 506 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CommunicationAddress6 | 512 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CommunicationMethod1Code | 523 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CommunicationMethod3Choice | 532 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CompanyLink1Choice | 538 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CompanyLink1Code | 544 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ConductClassification1Code | 554 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ConsolidatedTapeAssociationIdentifier | 561 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ConsolidationType1Choice | 567 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ConsolidationType1Code | 573 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CountryAndResidentialStatusType2 | 579 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CountryCode | 585 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CreditDebit3Code | 590 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}CustomerConductClassification1Choice | 596 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DataBaseCheck1 | 602 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DateAndAmount1 | 608 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DateAndDateTime1Choice | 614 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DateTimePeriod2 | 620 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DeMinimus1Choice | 626 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DeMinimusApplicable1 | 632 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DeMinimusNotApplicable1 | 638 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DecimalNumber | 643 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DirectDebitMandate7 | 649 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DistributionPolicy1Code | 664 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Document | 670 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DocumentToSend4 | 675 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}DutchIdentifier | 682 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Eligible1Code | 685 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}EuroclearClearstreamIdentifier | 691 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}EventFrequency10Code | 697 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}EventFrequency1Code | 703 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}EventFrequency8Code | 720 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}EventFrequency9Code | 739 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Exact4AlphaNumericText | 757 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Extended350Code | 762 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ExtendedParty14 | 768 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Extension1 | 774 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ExtensiveBranchNetworkIdentifier | 780 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ExternalAccountIdentification1Code | 785 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FATCAForm1Choice | 791 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FATCAFormType1Code | 797 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FATCASource1Choice | 808 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FATCASourceStatus1Code | 814 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FATCAStatus1Code | 820 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FATCAStatus2 | 835 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FATCAStatus2Choice | 841 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FedwireRoutingNumberIdentifier | 847 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FinancialInstitutionIdentification11Choice | 852 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FinancialInstrument87 | 860 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FiscalYear1Choice | 879 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FormOfSecurity1Code | 885 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Frequency20Choice | 891 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FundCashAccount4Code | 897 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FundIntention1Code | 912 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}FundOwnership1Code | 918 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}GDPRData1 | 924 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}GDPRDataConsent1Choice | 931 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}GDPRDataConsent1Code | 937 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Gender1Code | 945 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}GenericAccountIdentification1 | 951 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}GenericIdentification1 | 958 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}GenericIdentification47 | 965 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}GenericIdentification82 | 972 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}GermanBankleitzahlIdentifier | 983 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}HighFrequencyTradingProfile1 | 988 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Holding1Code | 995 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}HongKongBankIdentifier | 1002 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}IBAN2007Identifier | 1007 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ISINOct2015Identifier | 1012 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ISODate | 1017 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ISODateTime | 1020 |
| [type-0137](types/type-0137.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ISOYearMonth | 1023 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}IdentificationSource1Choice | 1026 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}IncomePreference2Code | 1032 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}IndividualPerson29 | 1038 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}IndividualPerson37 | 1047 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InformationDistribution1Choice | 1072 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InformationDistribution2Code | 1078 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InitialAmount1Choice | 1085 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Insurance1Code | 1091 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InsuranceType2Choice | 1097 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Intermediary46 | 1103 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentAccount73 | 1115 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentAccountCategory1Choice | 1157 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentAccountCategory1Code | 1163 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentAccountOpening4 | 1169 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentAccountOwnershipInformation16 | 1178 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentFundOrder4 | 1214 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentFundRole6Code | 1220 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentFundRole7Code | 1242 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentFundTransactionType1Code | 1257 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestmentPlan17 | 1283 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestorProfile2 | 1305 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestorProfileStatus1Choice | 1314 |
| [type-0160](types/type-0160.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}InvestorProfileStatus1Code | 1320 |
| [type-0161](types/type-0161.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}IrishNSCIdentifier | 1334 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ItalianDomesticIdentifier | 1339 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}KYCCheckType1Choice | 1344 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}KnowYourCustomerCheckType1Code | 1350 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}LEIIdentifier | 1357 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}LanguageCode | 1362 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}LetterIntent1 | 1365 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}LevelOfControl1Choice | 1373 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}LevelOfControl1Code | 1379 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Liability1Choice | 1385 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Liability1Code | 1391 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}MICIdentifier | 1397 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}MailType1Choice | 1402 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}MailType1Code | 1408 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}MarketMakerProfile2 | 1415 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}MarketPracticeVersion1 | 1423 |
| [type-0177](types/type-0177.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max10Text | 1430 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max140Text | 1436 |
| [type-0179](types/type-0179.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max16Text | 1442 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max256Text | 1448 |
| [type-0181](types/type-0181.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max34Text | 1454 |
| [type-0182](types/type-0182.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max350Text | 1460 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max35Text | 1466 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max3Text | 1472 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max4AlphaNumericText | 1478 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Max70Text | 1485 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}MessageIdentification1 | 1491 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}MiFIDClassification1 | 1497 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}MoneyLaunderingCheck1Choice | 1503 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}MoneyLaunderingCheck1Code | 1509 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}NameAndAddress4 | 1519 |
| [type-0192](types/type-0192.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}NameAndAddress5 | 1525 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}NamePrefix1Choice | 1531 |
| [type-0194](types/type-0194.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}NamePrefix1Code | 1537 |
| [type-0195](types/type-0195.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}NationalityCode | 1545 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}NewIssueAllocation2 | 1548 |
| [type-0197](types/type-0197.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}NewZealandNCCIdentifier | 1555 |
| [type-0198](types/type-0198.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}NoReasonCode | 1560 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Notification2 | 1565 |
| [type-0200](types/type-0200.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Number | 1572 |
| [type-0201](types/type-0201.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}OperationalStatus1Code | 1578 |
| [type-0202](types/type-0202.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}OrderOriginatorEligibility1Code | 1584 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Organisation23 | 1591 |
| [type-0204](types/type-0204.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Organisation39 | 1598 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}OrganisationType1Choice | 1612 |
| [type-0206](types/type-0206.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}OrganisationType1Code | 1618 |
| [type-0207](types/type-0207.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}OtherIdentification3Choice | 1626 |
| [type-0208](types/type-0208.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}OwnershipBeneficiaryRate1 | 1632 |
| [type-0209](types/type-0209.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}OwnershipType2Choice | 1638 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Party47Choice | 1644 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PartyIdentification125Choice | 1650 |
| [type-0212](types/type-0212.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PartyIdentification177Choice | 1657 |
| [type-0213](types/type-0213.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PartyIdentificationType7Code | 1663 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PartyProfileInformation5 | 1685 |
| [type-0215](types/type-0215.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PartyRole1Code | 1703 |
| [type-0216](types/type-0216.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PartyRole2Choice | 1709 |
| [type-0217](types/type-0217.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PartyRole4Choice | 1715 |
| [type-0218](types/type-0218.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PartyRole5Choice | 1721 |
| [type-0219](types/type-0219.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PaymentCard29 | 1727 |
| [type-0220](types/type-0220.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PaymentInstrument17 | 1740 |
| [type-0221](types/type-0221.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PaymentInstrument19Choice | 1751 |
| [type-0222](types/type-0222.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PaymentInstrument24Choice | 1757 |
| [type-0223](types/type-0223.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PercentageBoundedRate | 1765 |
| [type-0224](types/type-0224.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PercentageRate | 1773 |
| [type-0225](types/type-0225.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PersonalInformation1 | 1779 |
| [type-0226](types/type-0226.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PhoneNumber | 1786 |
| [type-0227](types/type-0227.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PlanStatus1Code | 1791 |
| [type-0228](types/type-0228.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PlanStatus2Choice | 1798 |
| [type-0229](types/type-0229.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PoliticalExposureType2Choice | 1804 |
| [type-0230](types/type-0230.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PoliticalExposureType2Code | 1810 |
| [type-0231](types/type-0231.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PoliticallyExposedPerson1 | 1818 |
| [type-0232](types/type-0232.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PoliticallyExposedPersonStatus1Choice | 1824 |
| [type-0233](types/type-0233.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PoliticallyExposedPersonStatus1Code | 1830 |
| [type-0234](types/type-0234.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PortugueseNCCIdentifier | 1837 |
| [type-0235](types/type-0235.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PositionEffect3Code | 1842 |
| [type-0236](types/type-0236.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PostalAddress1 | 1848 |
| [type-0237](types/type-0237.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}PostalAddress21 | 1860 |
| [type-0238](types/type-0238.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ProfileType1Choice | 1882 |
| [type-0239](types/type-0239.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ProfileType1Code | 1888 |
| [type-0240](types/type-0240.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Provided1Code | 1896 |
| [type-0241](types/type-0241.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}QUICKIdentifier | 1902 |
| [type-0242](types/type-0242.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RICIdentifier | 1905 |
| [type-0243](types/type-0243.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Rank1Code | 1911 |
| [type-0244](types/type-0244.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Referred1Code | 1917 |
| [type-0245](types/type-0245.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ReferredAgent3 | 1924 |
| [type-0246](types/type-0246.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RegisteredShareholderName1Choice | 1930 |
| [type-0247](types/type-0247.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RegulatoryInformation1 | 1936 |
| [type-0248](types/type-0248.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Reinvestment4 | 1944 |
| [type-0249](types/type-0249.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}Repartition6 | 1951 |
| [type-0250](types/type-0250.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ResidentialStatus1Code | 1958 |
| [type-0251](types/type-0251.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RestrictionStatus1Choice | 1965 |
| [type-0252](types/type-0252.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RestrictionStatus1Code | 1971 |
| [type-0253](types/type-0253.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RiskLevel1Code | 1977 |
| [type-0254](types/type-0254.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RiskLevel2Choice | 1984 |
| [type-0255](types/type-0255.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RoundingDirection1Code | 1990 |
| [type-0256](types/type-0256.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RoundingParameters1 | 1998 |
| [type-0257](types/type-0257.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}RussianCentralBankIdentificationCodeIdentifier | 2004 |
| [type-0258](types/type-0258.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SEDOLIdentifier | 2009 |
| [type-0259](types/type-0259.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SecurityIdentification25Choice | 2012 |
| [type-0260](types/type-0260.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SettlementFrequency1Choice | 2031 |
| [type-0261](types/type-0261.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SettlementInstructionReason1Choice | 2037 |
| [type-0262](types/type-0262.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SettlementInstructionReason1Code | 2043 |
| [type-0263](types/type-0263.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SicovamIdentifier | 2061 |
| [type-0264](types/type-0264.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SimpleIdentificationInformation4 | 2064 |
| [type-0265](types/type-0265.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SmallNetworkIdentifier | 2069 |
| [type-0266](types/type-0266.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SouthAfricanNCCIdentifier | 2074 |
| [type-0267](types/type-0267.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SpanishDomesticInterbankingIdentifier | 2079 |
| [type-0268](types/type-0268.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}StatementFrequencyReason2Choice | 2084 |
| [type-0269](types/type-0269.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SwissBCIdentifier | 2090 |
| [type-0270](types/type-0270.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}SwissSICIdentifier | 2095 |
| [type-0271](types/type-0271.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}TaxExemptReason3Code | 2100 |
| [type-0272](types/type-0272.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}TaxExemptionReason2Choice | 2147 |
| [type-0273](types/type-0273.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}TaxReporting3 | 2153 |
| [type-0274](types/type-0274.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}TaxWithholdingMethod3Code | 2163 |
| [type-0275](types/type-0275.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ThirdPartyRights2 | 2176 |
| [type-0276](types/type-0276.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}TickerIdentifier | 2186 |
| [type-0277](types/type-0277.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}TransactionChannel2Code | 2192 |
| [type-0278](types/type-0278.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}TransactionChannelType1Choice | 2199 |
| [type-0279](types/type-0279.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}TransactionType5Choice | 2205 |
| [type-0280](types/type-0280.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}TreasuryProfile1 | 2211 |
| [type-0281](types/type-0281.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}UKDomesticSortCodeIdentifier | 2218 |
| [type-0282](types/type-0282.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}UnitsOrAmount1Choice | 2223 |
| [type-0283](types/type-0283.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}UnitsOrAmountOrPercentage1Choice | 2229 |
| [type-0284](types/type-0284.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}ValorenIdentifier | 2236 |
| [type-0285](types/type-0285.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}WertpapierIdentifier | 2239 |
| [type-0286](types/type-0286.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.001.001.08}YesNoIndicator | 2242 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 2 |
| choice | 71 |
| complexType | 146 |
| element | 600 |
| enumeration | 429 |
| extension | 2 |
| fractionDigits | 6 |
| maxInclusive | 1 |
| maxLength | 16 |
| minInclusive | 3 |
| minLength | 16 |
| pattern | 32 |
| restriction | 139 |
| schema | 1 |
| sequence | 73 |
| simpleContent | 2 |
| simpleType | 139 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/548f4245706e86bc41b2a7ee.md) · [Message](index.md)
