---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.003.001.08"
message_family: "acmt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08"
source_ids: ["src-000100"]
source_editions: ["2025-2026"]
---

# acmt.003.001.08 structure

[src-000100](../../../../../raw-input/investment_funds/acmt.003.001.08.xsd); `urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Account23 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Account32 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountDesignation1Choice | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountIdentification4Choice | 23 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountIdentificationAndName5 | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountModificationInstructionV08 | 35 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountOwner3Choice | 55 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountOwnershipType4Code | 61 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountParties13Choice | 83 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountParties18 | 91 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountSchemeName1Choice | 110 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountSelection3Choice | 116 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountStatusUpdateInstruction1 | 122 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountStatusUpdateInstruction1Choice | 128 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountStatusUpdateInstruction1Code | 134 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountStatusUpdateInstructionReason1 | 140 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountStatusUpdateInstructionReason1Choice | 146 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountStatusUpdateInstructionReason2Choice | 152 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountStatusUpdateRequestReason1Code | 158 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountType2Choice | 163 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountUsageType2Choice | 169 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountUsageType2Code | 175 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountingStatus1Choice | 183 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AccountingStatus1Code | 189 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ActiveCurrencyAnd13DecimalAmount_SimpleType | 195 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ActiveCurrencyAnd13DecimalAmount | 202 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ActiveCurrencyAndAmount_SimpleType | 209 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ActiveCurrencyAndAmount | 216 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ActiveCurrencyCode | 223 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ActiveOrHistoricCurrencyCode | 228 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AdditionalReference13 | 233 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AdditiononalInformation13 | 240 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AddressType1Choice | 251 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AddressType1Code | 257 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AddressType2Choice | 263 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AddressType2Code | 269 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AlternateSecurityIdentification7 | 279 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AnyBICDec2014Identifier | 285 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}AustrianBankleitzahlIdentifier | 290 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}BICFIDec2014Identifier | 295 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}BelgianIdentifier | 300 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}BlockedHoldingDetails2 | 303 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}BlockedReason2Choice | 310 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}BlockedReason2Code | 316 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}BlockedStatusReason2 | 329 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}BlockedStatusReason2Choice | 337 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Bloomberg2Identifier | 343 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}BranchData4 | 348 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CHIPSParticipantIdentifier | 355 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CHIPSUniversalIdentifier | 360 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CRSForm1Choice | 365 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CRSFormType1Code | 371 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CRSSource1Choice | 383 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CRSSourceStatus1Code | 389 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CRSStatus1Code | 395 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CRSStatus3Choice | 413 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CRSStatus4 | 419 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CUSIPIdentifier | 426 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CanadianPaymentsARNIdentifier | 429 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CardType1Code | 434 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CashAccount204 | 440 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CashAccountType3Choice | 456 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CashAccountType5Code | 462 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CashSettlement4 | 471 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CertificateType2Code | 478 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CertificationType1Choice | 492 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Cheque4 | 498 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CitizenshipInformation2 | 503 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CivilStatus1Choice | 509 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CivilStatus1Code | 515 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ClearingSystemMemberIdentification4Choice | 526 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Collateral1Code | 549 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CommunicationAddress6 | 555 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CommunicationMethod1Code | 566 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CommunicationMethod3Choice | 575 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CompanyLink1Choice | 581 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CompanyLink1Code | 587 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ConductClassification1Code | 597 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ConsolidatedTapeAssociationIdentifier | 604 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ConsolidationType1Choice | 610 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ConsolidationType1Code | 616 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CountryAndResidentialStatusType2 | 622 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CountryCode | 628 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CreditDebit3Code | 633 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}CustomerConductClassification1Choice | 639 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DataBaseCheck1 | 645 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DataModification1Code | 651 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DataModification2Code | 658 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DateAndAmount1 | 664 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DateAndDateTime1Choice | 670 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DateTimePeriod2 | 676 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DeMinimus1Choice | 682 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DeMinimusApplicable1 | 688 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DeMinimusNotApplicable1 | 694 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DecimalNumber | 699 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DirectDebitMandate7 | 705 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DistributionPolicy1Code | 720 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Document | 726 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DocumentToSend4 | 731 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}DutchIdentifier | 738 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Eligible1Code | 741 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}EuroclearClearstreamIdentifier | 747 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}EventFrequency10Code | 753 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}EventFrequency1Code | 759 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}EventFrequency8Code | 776 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}EventFrequency9Code | 795 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Exact4AlphaNumericText | 813 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Extended350Code | 818 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ExtendedParty15 | 824 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Extension1 | 830 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ExtensiveBranchNetworkIdentifier | 836 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ExternalAccountIdentification1Code | 841 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FATCAForm1Choice | 847 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FATCAFormType1Code | 853 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FATCASource1Choice | 864 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FATCASourceStatus1Code | 870 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FATCAStatus1Code | 876 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FATCAStatus2 | 891 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FATCAStatus2Choice | 897 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FedwireRoutingNumberIdentifier | 903 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FinancialInstitutionIdentification11Choice | 908 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FinancialInstrument55 | 916 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FinancialInstrument87 | 928 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FiscalYear1Choice | 947 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FormOfSecurity1Code | 953 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Frequency20Choice | 959 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FundCashAccount4Code | 965 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FundIntention1Code | 980 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}FundOwnership1Code | 986 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GDPRData1 | 992 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GDPRDataConsent1Choice | 999 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GDPRDataConsent1Code | 1005 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Gender1Code | 1013 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GenericAccountIdentification1 | 1019 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GenericIdentification1 | 1026 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GenericIdentification36 | 1033 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GenericIdentification47 | 1040 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GenericIdentification81 | 1047 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GenericIdentification82 | 1053 |
| [type-0141](types/type-0141.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}GermanBankleitzahlIdentifier | 1064 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}HighFrequencyTradingProfile1 | 1069 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Holding1Code | 1076 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}HongKongBankIdentifier | 1083 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}IBAN2007Identifier | 1088 |
| [type-0146](types/type-0146.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ISINOct2015Identifier | 1093 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ISODate | 1098 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ISODateTime | 1101 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ISOYearMonth | 1104 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}IdentificationSource1Choice | 1107 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}IncomePreference2Code | 1113 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}IndividualPerson29 | 1119 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}IndividualPerson35 | 1128 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}IndividualPerson38 | 1137 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}IndividualPersonIdentification3Choice | 1162 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InformationDistribution1Choice | 1168 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InformationDistribution2Code | 1174 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InitialAmount1Choice | 1181 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Insurance1Code | 1187 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InsuranceType2Choice | 1193 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Intermediary46 | 1199 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Intermediary47 | 1211 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentAccount75 | 1218 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentAccount76 | 1260 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentAccountCategory1Choice | 1272 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentAccountCategory1Code | 1278 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentAccountModification4 | 1284 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentAccountOwnershipInformation17 | 1293 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentFundRole6Code | 1329 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentFundRole7Code | 1351 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentFundTransactionType1Code | 1366 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestmentPlan16 | 1392 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestorProfile2 | 1414 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestorProfileStatus1Choice | 1423 |
| [type-0175](types/type-0175.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}InvestorProfileStatus1Code | 1429 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}IrishNSCIdentifier | 1443 |
| [type-0177](types/type-0177.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ItalianDomesticIdentifier | 1448 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}KYCCheckType1Choice | 1453 |
| [type-0179](types/type-0179.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}KnowYourCustomerCheckType1Code | 1459 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}LEIIdentifier | 1466 |
| [type-0181](types/type-0181.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}LanguageCode | 1471 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}LetterIntent1 | 1474 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}LevelOfControl1Choice | 1482 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}LevelOfControl1Code | 1488 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Liability1Choice | 1494 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Liability1Code | 1500 |
| [type-0187](types/type-0187.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}MICIdentifier | 1506 |
| [type-0188](types/type-0188.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}MailType1Choice | 1511 |
| [type-0189](types/type-0189.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}MailType1Code | 1517 |
| [type-0190](types/type-0190.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}MarketMakerProfile2 | 1524 |
| [type-0191](types/type-0191.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}MarketPracticeVersion1 | 1532 |
| [type-0192](types/type-0192.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max10Text | 1539 |
| [type-0193](types/type-0193.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max140Text | 1545 |
| [type-0194](types/type-0194.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max16Text | 1551 |
| [type-0195](types/type-0195.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max256Text | 1557 |
| [type-0196](types/type-0196.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max34Text | 1563 |
| [type-0197](types/type-0197.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max350Text | 1569 |
| [type-0198](types/type-0198.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max35Text | 1575 |
| [type-0199](types/type-0199.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max3Text | 1581 |
| [type-0200](types/type-0200.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max4AlphaNumericText | 1587 |
| [type-0201](types/type-0201.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Max70Text | 1594 |
| [type-0202](types/type-0202.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}MessageIdentification1 | 1600 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}MiFIDClassification1 | 1606 |
| [type-0204](types/type-0204.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope21 | 1612 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope27 | 1618 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope34 | 1624 |
| [type-0207](types/type-0207.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope39 | 1630 |
| [type-0208](types/type-0208.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope40 | 1636 |
| [type-0209](types/type-0209.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope41 | 1642 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope42 | 1648 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope43 | 1654 |
| [type-0212](types/type-0212.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope44 | 1660 |
| [type-0213](types/type-0213.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope45 | 1666 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ModificationScope46 | 1672 |
| [type-0215](types/type-0215.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}MoneyLaunderingCheck1Choice | 1678 |
| [type-0216](types/type-0216.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}MoneyLaunderingCheck1Code | 1684 |
| [type-0217](types/type-0217.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}NameAndAddress15 | 1694 |
| [type-0218](types/type-0218.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}NameAndAddress4 | 1700 |
| [type-0219](types/type-0219.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}NameAndAddress5 | 1706 |
| [type-0220](types/type-0220.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}NamePrefix1Choice | 1712 |
| [type-0221](types/type-0221.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}NamePrefix1Code | 1718 |
| [type-0222](types/type-0222.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}NationalityCode | 1726 |
| [type-0223](types/type-0223.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}NewIssueAllocation2 | 1729 |
| [type-0224](types/type-0224.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}NewZealandNCCIdentifier | 1736 |
| [type-0225](types/type-0225.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}NoReasonCode | 1741 |
| [type-0226](types/type-0226.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Notification2 | 1746 |
| [type-0227](types/type-0227.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Number | 1753 |
| [type-0228](types/type-0228.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}OperationalStatus1Code | 1759 |
| [type-0229](types/type-0229.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}OrderOriginatorEligibility1Code | 1765 |
| [type-0230](types/type-0230.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Organisation23 | 1772 |
| [type-0231](types/type-0231.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Organisation40 | 1779 |
| [type-0232](types/type-0232.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}OrganisationType1Choice | 1793 |
| [type-0233](types/type-0233.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}OrganisationType1Code | 1799 |
| [type-0234](types/type-0234.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}OtherIdentification3Choice | 1807 |
| [type-0235](types/type-0235.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}OwnershipBeneficiaryRate1 | 1813 |
| [type-0236](types/type-0236.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}OwnershipType2Choice | 1819 |
| [type-0237](types/type-0237.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Party48Choice | 1825 |
| [type-0238](types/type-0238.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyIdentification125Choice | 1831 |
| [type-0239](types/type-0239.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyIdentification177Choice | 1838 |
| [type-0240](types/type-0240.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyIdentification182Choice | 1844 |
| [type-0241](types/type-0241.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyIdentification220 | 1853 |
| [type-0242](types/type-0242.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyIdentificationType7Code | 1859 |
| [type-0243](types/type-0243.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyProfileInformation5 | 1881 |
| [type-0244](types/type-0244.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyRole1Code | 1899 |
| [type-0245](types/type-0245.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyRole2Choice | 1905 |
| [type-0246](types/type-0246.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyRole4Choice | 1911 |
| [type-0247](types/type-0247.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PartyRole5Choice | 1917 |
| [type-0248](types/type-0248.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PaymentCard29 | 1923 |
| [type-0249](types/type-0249.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PaymentInstrument17 | 1936 |
| [type-0250](types/type-0250.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PaymentInstrument19Choice | 1947 |
| [type-0251](types/type-0251.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PaymentInstrument24Choice | 1953 |
| [type-0252](types/type-0252.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PercentageBoundedRate | 1961 |
| [type-0253](types/type-0253.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PercentageRate | 1969 |
| [type-0254](types/type-0254.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PersonalInformation1 | 1975 |
| [type-0255](types/type-0255.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PhoneNumber | 1982 |
| [type-0256](types/type-0256.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PlanStatus1Code | 1987 |
| [type-0257](types/type-0257.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PlanStatus2Choice | 1994 |
| [type-0258](types/type-0258.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PoliticalExposureType2Choice | 2000 |
| [type-0259](types/type-0259.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PoliticalExposureType2Code | 2006 |
| [type-0260](types/type-0260.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PoliticallyExposedPerson1 | 2014 |
| [type-0261](types/type-0261.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PoliticallyExposedPersonStatus1Choice | 2020 |
| [type-0262](types/type-0262.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PoliticallyExposedPersonStatus1Code | 2026 |
| [type-0263](types/type-0263.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PortugueseNCCIdentifier | 2033 |
| [type-0264](types/type-0264.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PositionEffect3Code | 2038 |
| [type-0265](types/type-0265.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PostalAddress1 | 2044 |
| [type-0266](types/type-0266.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}PostalAddress21 | 2056 |
| [type-0267](types/type-0267.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ProfileType1Choice | 2078 |
| [type-0268](types/type-0268.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ProfileType1Code | 2084 |
| [type-0269](types/type-0269.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Provided1Code | 2092 |
| [type-0270](types/type-0270.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}QUICKIdentifier | 2098 |
| [type-0271](types/type-0271.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RICIdentifier | 2101 |
| [type-0272](types/type-0272.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Rank1Code | 2107 |
| [type-0273](types/type-0273.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Referred1Code | 2113 |
| [type-0274](types/type-0274.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ReferredAgent3 | 2120 |
| [type-0275](types/type-0275.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RegisteredShareholderName1Choice | 2126 |
| [type-0276](types/type-0276.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RegulatoryInformation1 | 2132 |
| [type-0277](types/type-0277.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Reinvestment4 | 2140 |
| [type-0278](types/type-0278.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}Repartition6 | 2147 |
| [type-0279](types/type-0279.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ResidentialStatus1Code | 2154 |
| [type-0280](types/type-0280.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RestrictionStatus1Choice | 2161 |
| [type-0281](types/type-0281.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RestrictionStatus1Code | 2167 |
| [type-0282](types/type-0282.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RiskLevel1Code | 2173 |
| [type-0283](types/type-0283.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RiskLevel2Choice | 2180 |
| [type-0284](types/type-0284.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RoundingDirection1Code | 2186 |
| [type-0285](types/type-0285.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RoundingParameters1 | 2194 |
| [type-0286](types/type-0286.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}RussianCentralBankIdentificationCodeIdentifier | 2200 |
| [type-0287](types/type-0287.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SEDOLIdentifier | 2205 |
| [type-0288](types/type-0288.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SecurityIdentification25Choice | 2208 |
| [type-0289](types/type-0289.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SettlementFrequency1Choice | 2227 |
| [type-0290](types/type-0290.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SettlementInstructionReason1Choice | 2233 |
| [type-0291](types/type-0291.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SettlementInstructionReason1Code | 2239 |
| [type-0292](types/type-0292.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SicovamIdentifier | 2257 |
| [type-0293](types/type-0293.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SimpleIdentificationInformation4 | 2260 |
| [type-0294](types/type-0294.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SmallNetworkIdentifier | 2265 |
| [type-0295](types/type-0295.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SouthAfricanNCCIdentifier | 2270 |
| [type-0296](types/type-0296.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SpanishDomesticInterbankingIdentifier | 2275 |
| [type-0297](types/type-0297.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}StatementFrequencyReason2Choice | 2280 |
| [type-0298](types/type-0298.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SwissBCIdentifier | 2286 |
| [type-0299](types/type-0299.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}SwissSICIdentifier | 2291 |
| [type-0300](types/type-0300.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}TaxExemptReason3Code | 2296 |
| [type-0301](types/type-0301.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}TaxExemptionReason2Choice | 2343 |
| [type-0302](types/type-0302.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}TaxReporting3 | 2349 |
| [type-0303](types/type-0303.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}TaxWithholdingMethod3Code | 2359 |
| [type-0304](types/type-0304.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ThirdPartyRights2 | 2372 |
| [type-0305](types/type-0305.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}TickerIdentifier | 2382 |
| [type-0306](types/type-0306.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}TransactionChannel2Code | 2388 |
| [type-0307](types/type-0307.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}TransactionChannelType1Choice | 2395 |
| [type-0308](types/type-0308.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}TransactionType5Choice | 2401 |
| [type-0309](types/type-0309.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}TreasuryProfile1 | 2407 |
| [type-0310](types/type-0310.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}UKDomesticSortCodeIdentifier | 2414 |
| [type-0311](types/type-0311.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}UnitsOrAmount1Choice | 2419 |
| [type-0312](types/type-0312.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}UnitsOrAmountOrPercentage1Choice | 2425 |
| [type-0313](types/type-0313.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}ValorenIdentifier | 2432 |
| [type-0314](types/type-0314.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}WertpapierIdentifier | 2435 |
| [type-0315](types/type-0315.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.003.001.08}YesNoIndicator | 2438 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 2 |
| choice | 77 |
| complexType | 172 |
| element | 674 |
| enumeration | 435 |
| extension | 2 |
| fractionDigits | 6 |
| maxInclusive | 1 |
| maxLength | 16 |
| minInclusive | 3 |
| minLength | 16 |
| pattern | 32 |
| restriction | 142 |
| schema | 1 |
| sequence | 93 |
| simpleContent | 2 |
| simpleType | 142 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
