---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.002.001.08"
message_family: "acmt.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08"
source_ids: ["src-000099"]
source_editions: ["2025-2026"]
---

# acmt.002.001.08 structure

[src-000099](../../../../../raw-input/investment_funds/acmt.002.001.08.xsd); `urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Account23 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Account32 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountDesignation1Choice | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountDetailsConfirmationV08 | 23 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountIdentification4Choice | 43 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountIdentificationAndName5 | 49 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountManagementConfirmation5 | 55 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountManagementType2Code | 64 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountOwnershipType4Code | 71 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountParties12Choice | 93 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountParties17 | 101 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountSchemeName1Choice | 119 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountStatus2 | 125 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountType2Choice | 137 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountUsageType2Choice | 143 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountUsageType2Code | 149 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountingStatus1Choice | 157 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AccountingStatus1Code | 163 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ActiveCurrencyAnd13DecimalAmount_SimpleType | 169 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ActiveCurrencyAnd13DecimalAmount | 176 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ActiveCurrencyAndAmount_SimpleType | 183 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ActiveCurrencyAndAmount | 190 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ActiveCurrencyCode | 197 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ActiveOrHistoricCurrencyCode | 202 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AdditionalReference13 | 207 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AdditiononalInformation13 | 214 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AddressType1Choice | 225 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AddressType1Code | 231 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AddressType2Choice | 237 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AddressType2Code | 243 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AlternateSecurityIdentification7 | 253 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AnyBICDec2014Identifier | 259 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}AustrianBankleitzahlIdentifier | 264 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}BICFIDec2014Identifier | 269 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}BelgianIdentifier | 274 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}BlockedHoldingDetails2 | 277 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}BlockedReason2Choice | 284 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}BlockedReason2Code | 290 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}BlockedStatusReason2 | 303 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}BlockedStatusReason2Choice | 311 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Bloomberg2Identifier | 317 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}BranchData4 | 322 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CHIPSParticipantIdentifier | 329 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CHIPSUniversalIdentifier | 334 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CRSForm1Choice | 339 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CRSFormType1Code | 345 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CRSSource1Choice | 357 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CRSSourceStatus1Code | 363 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CRSStatus1Code | 369 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CRSStatus3Choice | 387 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CRSStatus4 | 393 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CUSIPIdentifier | 400 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CanadianPaymentsARNIdentifier | 403 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CardType1Code | 408 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CashAccount204 | 414 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CashAccountType3Choice | 430 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CashAccountType5Code | 436 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CashSettlement3 | 445 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CertificateType2Code | 451 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CertificationType1Choice | 465 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Cheque4 | 471 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CitizenshipInformation2 | 476 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CivilStatus1Choice | 482 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CivilStatus1Code | 488 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ClearingSystemMemberIdentification4Choice | 499 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ClosedStatusReason1 | 522 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ClosedStatusReason1Choice | 528 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ClosedStatusReason1Code | 534 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ClosedStatusReason2Choice | 540 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ClosurePendingStatusReason1 | 546 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ClosurePendingStatusReason1Choice | 552 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ClosurePendingStatusReason1Code | 558 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ClosurePendingStatusReason2Choice | 564 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Collateral1Code | 570 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CommunicationAddress6 | 576 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CommunicationMethod1Code | 587 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CommunicationMethod3Choice | 596 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CompanyLink1Choice | 602 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CompanyLink1Code | 608 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ConductClassification1Code | 618 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ConfirmationType1Choice | 625 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ConsolidatedTapeAssociationIdentifier | 631 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ConsolidationType1Choice | 637 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ConsolidationType1Code | 643 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CountryAndResidentialStatusType2 | 649 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CountryCode | 655 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CreditDebit3Code | 660 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}CustomerConductClassification1Choice | 666 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DataBaseCheck1 | 672 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DateAndAmount1 | 678 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DateAndDateTime1Choice | 684 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DateTimePeriod2 | 690 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DeMinimus1Choice | 696 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DeMinimusApplicable1 | 702 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DeMinimusNotApplicable1 | 708 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DecimalNumber | 713 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DirectDebitMandate7 | 719 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DisabledReason2Code | 734 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DisabledStatusReason1 | 749 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DisabledStatusReason1Choice | 755 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DisabledStatusReason2Choice | 761 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DistributionPolicy1Code | 767 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Document | 773 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DocumentToSend4 | 778 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}DutchIdentifier | 785 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Eligible1Code | 788 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}EnabledStatusReason1 | 794 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}EnabledStatusReason1Choice | 800 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}EnabledStatusReason1Code | 806 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}EnabledStatusReason2Choice | 811 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}EuroclearClearstreamIdentifier | 817 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}EventFrequency10Code | 823 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}EventFrequency1Code | 829 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}EventFrequency8Code | 846 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}EventFrequency9Code | 865 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Exact4AlphaNumericText | 883 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Extended350Code | 888 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ExtendedParty14 | 894 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Extension1 | 900 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ExtensiveBranchNetworkIdentifier | 906 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ExternalAccountIdentification1Code | 911 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FATCAForm1Choice | 917 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FATCAFormType1Code | 923 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FATCASource1Choice | 934 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FATCASourceStatus1Code | 940 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FATCAStatus1Code | 946 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FATCAStatus2 | 961 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FATCAStatus2Choice | 967 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FedwireRoutingNumberIdentifier | 973 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FinancialInstitutionIdentification11Choice | 978 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FinancialInstrument87 | 986 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FiscalYear1Choice | 1005 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FormOfSecurity1Code | 1011 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Frequency20Choice | 1017 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FundCashAccount4Code | 1023 |
| [type-0137](types/type-0137.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FundIntention1Code | 1038 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}FundOwnership1Code | 1044 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}GDPRData1 | 1050 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}GDPRDataConsent1Choice | 1057 |
| [type-0141](types/type-0141.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}GDPRDataConsent1Code | 1063 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Gender1Code | 1071 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}GenericAccountIdentification1 | 1077 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}GenericIdentification1 | 1084 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}GenericIdentification36 | 1091 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}GenericIdentification47 | 1098 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}GenericIdentification82 | 1105 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}GermanBankleitzahlIdentifier | 1116 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}HighFrequencyTradingProfile1 | 1121 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Holding1Code | 1128 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}HongKongBankIdentifier | 1135 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}IBAN2007Identifier | 1140 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ISINOct2015Identifier | 1145 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ISODate | 1150 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ISODateTime | 1153 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ISOYearMonth | 1156 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}IdentificationSource1Choice | 1159 |
| [type-0158](types/type-0158.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}IncomePreference2Code | 1165 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}IndividualPerson29 | 1171 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}IndividualPerson37 | 1180 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InformationDistribution1Choice | 1205 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InformationDistribution2Code | 1211 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InitialAmount1Choice | 1218 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Insurance1Code | 1224 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InsuranceType2Choice | 1230 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Intermediary46 | 1236 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestmentAccount74 | 1248 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestmentAccountCategory1Choice | 1292 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestmentAccountCategory1Code | 1298 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestmentAccountOwnershipInformation16 | 1304 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestmentFundOrder4 | 1340 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestmentFundRole6Code | 1346 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestmentFundRole7Code | 1368 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestmentFundTransactionType1Code | 1383 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestmentPlan17 | 1409 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestorProfile2 | 1431 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestorProfileStatus1Choice | 1440 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}InvestorProfileStatus1Code | 1446 |
| [type-0179](types/type-0179.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}IrishNSCIdentifier | 1460 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ItalianDomesticIdentifier | 1465 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}KYCCheckType1Choice | 1470 |
| [type-0182](types/type-0182.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}KnowYourCustomerCheckType1Code | 1476 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}LEIIdentifier | 1483 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}LanguageCode | 1488 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}LetterIntent1 | 1491 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}LevelOfControl1Choice | 1499 |
| [type-0187](types/type-0187.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}LevelOfControl1Code | 1505 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Liability1Choice | 1511 |
| [type-0189](types/type-0189.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Liability1Code | 1517 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}MICIdentifier | 1523 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}MailType1Choice | 1528 |
| [type-0192](types/type-0192.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}MailType1Code | 1534 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}MarketMakerProfile2 | 1541 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}MarketPracticeVersion1 | 1549 |
| [type-0195](types/type-0195.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max10Text | 1556 |
| [type-0196](types/type-0196.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max140Text | 1562 |
| [type-0197](types/type-0197.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max16Text | 1568 |
| [type-0198](types/type-0198.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max256Text | 1574 |
| [type-0199](types/type-0199.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max34Text | 1580 |
| [type-0200](types/type-0200.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max350Text | 1586 |
| [type-0201](types/type-0201.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max35Text | 1592 |
| [type-0202](types/type-0202.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max3Text | 1598 |
| [type-0203](types/type-0203.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max4AlphaNumericText | 1604 |
| [type-0204](types/type-0204.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Max70Text | 1611 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}MessageIdentification1 | 1617 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}MiFIDClassification1 | 1623 |
| [type-0207](types/type-0207.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}MoneyLaunderingCheck1Choice | 1629 |
| [type-0208](types/type-0208.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}MoneyLaunderingCheck1Code | 1635 |
| [type-0209](types/type-0209.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}NameAndAddress4 | 1645 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}NameAndAddress5 | 1651 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}NamePrefix1Choice | 1657 |
| [type-0212](types/type-0212.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}NamePrefix1Code | 1663 |
| [type-0213](types/type-0213.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}NationalityCode | 1671 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}NewIssueAllocation2 | 1674 |
| [type-0215](types/type-0215.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}NewZealandNCCIdentifier | 1681 |
| [type-0216](types/type-0216.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}NoReasonCode | 1686 |
| [type-0217](types/type-0217.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Notification2 | 1691 |
| [type-0218](types/type-0218.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Number | 1698 |
| [type-0219](types/type-0219.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}OperationalStatus1Code | 1704 |
| [type-0220](types/type-0220.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}OrderOriginatorEligibility1Code | 1710 |
| [type-0221](types/type-0221.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Organisation23 | 1717 |
| [type-0222](types/type-0222.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Organisation39 | 1724 |
| [type-0223](types/type-0223.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}OrganisationType1Choice | 1738 |
| [type-0224](types/type-0224.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}OrganisationType1Code | 1744 |
| [type-0225](types/type-0225.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}OtherAccountStatus1 | 1752 |
| [type-0226](types/type-0226.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}OtherIdentification3Choice | 1758 |
| [type-0227](types/type-0227.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}OwnershipBeneficiaryRate1 | 1764 |
| [type-0228](types/type-0228.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}OwnershipType2Choice | 1770 |
| [type-0229](types/type-0229.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Party47Choice | 1776 |
| [type-0230](types/type-0230.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PartyIdentification125Choice | 1782 |
| [type-0231](types/type-0231.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PartyIdentification177Choice | 1789 |
| [type-0232](types/type-0232.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PartyIdentificationType7Code | 1795 |
| [type-0233](types/type-0233.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PartyProfileInformation5 | 1817 |
| [type-0234](types/type-0234.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PartyRole1Code | 1835 |
| [type-0235](types/type-0235.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PartyRole2Choice | 1841 |
| [type-0236](types/type-0236.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PartyRole4Choice | 1847 |
| [type-0237](types/type-0237.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PartyRole5Choice | 1853 |
| [type-0238](types/type-0238.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PaymentCard29 | 1859 |
| [type-0239](types/type-0239.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PaymentInstrument17 | 1872 |
| [type-0240](types/type-0240.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PaymentInstrument19Choice | 1883 |
| [type-0241](types/type-0241.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PaymentInstrument24Choice | 1889 |
| [type-0242](types/type-0242.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PendingOpeningStatusReason1 | 1897 |
| [type-0243](types/type-0243.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PendingOpeningStatusReason1Choice | 1903 |
| [type-0244](types/type-0244.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PendingOpeningStatusReason1Code | 1909 |
| [type-0245](types/type-0245.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PendingOpeningStatusReason2Choice | 1920 |
| [type-0246](types/type-0246.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PendingStatusReason14 | 1926 |
| [type-0247](types/type-0247.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PendingStatusReason1Choice | 1932 |
| [type-0248](types/type-0248.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PendingStatusReason1Code | 1938 |
| [type-0249](types/type-0249.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PendingStatusReason2Choice | 1948 |
| [type-0250](types/type-0250.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PercentageBoundedRate | 1954 |
| [type-0251](types/type-0251.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PercentageRate | 1962 |
| [type-0252](types/type-0252.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PersonalInformation1 | 1968 |
| [type-0253](types/type-0253.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PhoneNumber | 1975 |
| [type-0254](types/type-0254.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PlanStatus1Code | 1980 |
| [type-0255](types/type-0255.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PlanStatus2Choice | 1987 |
| [type-0256](types/type-0256.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PoliticalExposureType2Choice | 1993 |
| [type-0257](types/type-0257.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PoliticalExposureType2Code | 1999 |
| [type-0258](types/type-0258.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PoliticallyExposedPerson1 | 2007 |
| [type-0259](types/type-0259.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PoliticallyExposedPersonStatus1Choice | 2013 |
| [type-0260](types/type-0260.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PoliticallyExposedPersonStatus1Code | 2019 |
| [type-0261](types/type-0261.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PortugueseNCCIdentifier | 2026 |
| [type-0262](types/type-0262.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PositionEffect3Code | 2031 |
| [type-0263](types/type-0263.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PostalAddress1 | 2037 |
| [type-0264](types/type-0264.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}PostalAddress21 | 2049 |
| [type-0265](types/type-0265.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ProfileType1Choice | 2071 |
| [type-0266](types/type-0266.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ProfileType1Code | 2077 |
| [type-0267](types/type-0267.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ProformaStatusReason1 | 2085 |
| [type-0268](types/type-0268.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ProformaStatusReason1Choice | 2091 |
| [type-0269](types/type-0269.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ProformaStatusReason1Code | 2097 |
| [type-0270](types/type-0270.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ProformaStatusReason2Choice | 2103 |
| [type-0271](types/type-0271.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Provided1Code | 2109 |
| [type-0272](types/type-0272.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}QUICKIdentifier | 2115 |
| [type-0273](types/type-0273.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RICIdentifier | 2118 |
| [type-0274](types/type-0274.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Rank1Code | 2124 |
| [type-0275](types/type-0275.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Referred1Code | 2130 |
| [type-0276](types/type-0276.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ReferredAgent3 | 2137 |
| [type-0277](types/type-0277.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RegisteredShareholderName1Choice | 2143 |
| [type-0278](types/type-0278.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RegulatoryInformation1 | 2149 |
| [type-0279](types/type-0279.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Reinvestment4 | 2157 |
| [type-0280](types/type-0280.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}Repartition6 | 2164 |
| [type-0281](types/type-0281.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ResidentialStatus1Code | 2171 |
| [type-0282](types/type-0282.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RestrictionStatus1Choice | 2178 |
| [type-0283](types/type-0283.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RestrictionStatus1Code | 2184 |
| [type-0284](types/type-0284.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RiskLevel1Code | 2190 |
| [type-0285](types/type-0285.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RiskLevel2Choice | 2197 |
| [type-0286](types/type-0286.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RoundingDirection1Code | 2203 |
| [type-0287](types/type-0287.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RoundingParameters1 | 2211 |
| [type-0288](types/type-0288.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}RussianCentralBankIdentificationCodeIdentifier | 2217 |
| [type-0289](types/type-0289.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SEDOLIdentifier | 2222 |
| [type-0290](types/type-0290.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SecurityIdentification25Choice | 2225 |
| [type-0291](types/type-0291.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SettlementFrequency1Choice | 2244 |
| [type-0292](types/type-0292.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SettlementInstructionReason1Choice | 2250 |
| [type-0293](types/type-0293.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SettlementInstructionReason1Code | 2256 |
| [type-0294](types/type-0294.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SicovamIdentifier | 2274 |
| [type-0295](types/type-0295.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SimpleIdentificationInformation4 | 2277 |
| [type-0296](types/type-0296.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SmallNetworkIdentifier | 2282 |
| [type-0297](types/type-0297.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SouthAfricanNCCIdentifier | 2287 |
| [type-0298](types/type-0298.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SpanishDomesticInterbankingIdentifier | 2292 |
| [type-0299](types/type-0299.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}StatementFrequencyReason2Choice | 2297 |
| [type-0300](types/type-0300.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SwissBCIdentifier | 2303 |
| [type-0301](types/type-0301.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}SwissSICIdentifier | 2308 |
| [type-0302](types/type-0302.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}TaxExemptReason3Code | 2313 |
| [type-0303](types/type-0303.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}TaxExemptionReason2Choice | 2360 |
| [type-0304](types/type-0304.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}TaxReporting3 | 2366 |
| [type-0305](types/type-0305.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}TaxWithholdingMethod3Code | 2376 |
| [type-0306](types/type-0306.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ThirdPartyRights2 | 2389 |
| [type-0307](types/type-0307.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}TickerIdentifier | 2399 |
| [type-0308](types/type-0308.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}TransactionChannel2Code | 2405 |
| [type-0309](types/type-0309.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}TransactionChannelType1Choice | 2412 |
| [type-0310](types/type-0310.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}TransactionType5Choice | 2418 |
| [type-0311](types/type-0311.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}TreasuryProfile1 | 2424 |
| [type-0312](types/type-0312.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}UKDomesticSortCodeIdentifier | 2431 |
| [type-0313](types/type-0313.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}UnitsOrAmount1Choice | 2436 |
| [type-0314](types/type-0314.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}UnitsOrAmountOrPercentage1Choice | 2442 |
| [type-0315](types/type-0315.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}ValorenIdentifier | 2449 |
| [type-0316](types/type-0316.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}WertpapierIdentifier | 2452 |
| [type-0317](types/type-0317.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.002.001.08}YesNoIndicator | 2455 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 2 |
| choice | 85 |
| complexType | 170 |
| element | 657 |
| enumeration | 461 |
| extension | 2 |
| fractionDigits | 6 |
| maxInclusive | 1 |
| maxLength | 16 |
| minInclusive | 3 |
| minLength | 16 |
| pattern | 32 |
| restriction | 146 |
| schema | 1 |
| sequence | 83 |
| simpleContent | 2 |
| simpleType | 146 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
