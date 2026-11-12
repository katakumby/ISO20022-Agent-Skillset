---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.009.001.13"
message_family: "pacs.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13"
source_ids: ["src-000170"]
source_editions: ["2025-2026"]
---

# pacs.009.001.13 structure

[src-000170](../../../../../raw-input/payments_clearing_and_settlement/pacs.009.001.13.xsd); `urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}AddressType3Choice | 65 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}AnyBICDec2014Identifier | 71 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}BICFIDec2014Identifier | 76 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}BatchBookingIndicator | 81 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}BranchAndFinancialInstitutionIdentification8 | 84 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}BranchData5 | 90 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CashAccount40 | 98 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CashAccountType2Choice | 107 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CategoryPurpose1Choice | 113 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ClearingChannel2Code | 119 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ClearingSystemIdentification2Choice | 127 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ClearingSystemIdentification3Choice | 133 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ClearingSystemMemberIdentification2 | 139 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Contact13 | 145 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CountryCode | 162 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CreditDebitCode | 167 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CreditTransferTransaction72 | 173 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CreditTransferTransaction79 | 208 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CreditTransferTransaction80 | 254 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CreditorReferenceInformation3 | 297 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CreditorReferenceType2Choice | 303 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CreditorReferenceType3 | 309 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}CryptographicKey1Choice | 315 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DateAndPlaceOfBirth1 | 321 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DateAndType1 | 329 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DatePeriod2 | 335 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DateType2Choice | 341 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DecimalNumber | 347 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Document | 353 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DocumentAdjustment1 | 358 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DocumentAmount1 | 366 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DocumentAmountType1Choice | 372 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DocumentLineIdentification1 | 378 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DocumentLineInformation2 | 385 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DocumentLineType1 | 392 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DocumentLineType1Choice | 398 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DocumentType1 | 404 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}DocumentType2Choice | 410 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Exact4AlphaNumericText | 416 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalAccountIdentification1Code | 421 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalCashAccountType1Code | 427 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalCashClearingSystem1Code | 433 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalCategoryPurpose1Code | 439 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalClearingSystemIdentification1Code | 445 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalCreditorAgentInstruction1Code | 451 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalCreditorReferenceType1Code | 457 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalDateType1Code | 463 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalDocumentAmountType1Code | 469 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalDocumentLineType1Code | 475 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalDocumentType1Code | 481 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalFinancialInstitutionIdentification1Code | 487 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalGarnishmentType1Code | 493 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalLocalInstrument1Code | 499 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalOrganisationIdentification1Code | 505 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalPersonIdentification1Code | 511 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalProxyAccountType1Code | 517 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalPurpose1Code | 523 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalRegulatoryReportingType1Code | 529 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ExternalServiceLevel1Code | 535 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}FinancialIdentificationSchemeName1Choice | 541 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}FinancialInstitutionCreditTransferV13 | 547 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}FinancialInstitutionIdentification23 | 554 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Garnishment4 | 564 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}GarnishmentType1 | 576 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}GarnishmentType1Choice | 582 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}GenericAccountIdentification1 | 588 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}GenericFinancialIdentification1 | 595 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}GenericIdentification30 | 602 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}GenericOrganisationIdentification3 | 609 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}GenericPersonIdentification2 | 616 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}GroupHeader131 | 623 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}HexBinaryText | 639 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}IBAN2007Identifier | 644 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ISODate | 649 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ISODateTime | 652 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ISOTime | 655 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ISOYear | 658 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Instruction4Code | 661 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}InstructionForCreditorAgent3 | 667 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}InstructionForNextAgent1 | 673 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}LEIIdentifier | 679 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}LocalInstrument2Choice | 684 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max10Text | 690 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max128Text | 696 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max140Text | 702 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max15NumericText | 708 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max16Text | 713 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max2048Text | 719 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max256Text | 725 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max34Text | 731 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max350Text | 737 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max35Text | 743 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max4Text | 749 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Max70Text | 755 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}NamePrefix2Code | 761 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Number | 770 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}OrganisationIdentification39 | 776 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}OrganisationIdentificationSchemeName1Choice | 783 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}OtherContact1 | 789 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Party52Choice | 795 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}PartyIdentification272 | 801 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}PaymentIdentification13 | 810 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}PaymentTypeInformation28 | 819 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}PercentageRate | 828 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}PersonIdentification18 | 834 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}PersonIdentificationSchemeName1Choice | 840 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}PhoneNumber | 846 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}PostalAddress27 | 851 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}PreferredContactMethod2Code | 873 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Priority2Code | 883 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Priority3Code | 889 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ProxyAccountIdentification1 | 896 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ProxyAccountType1Choice | 902 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}Purpose2Choice | 908 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}References80Choice | 914 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ReferredDocumentInformation8 | 929 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}RegulatoryAuthority2 | 937 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}RegulatoryReporting10 | 943 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}RegulatoryReportingType1Choice | 950 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}RegulatoryReportingType1Code | 956 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}RemittanceAmount4 | 963 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}RemittanceInformation2 | 969 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}RemittanceInformation26 | 974 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}SHA256SignatureText | 980 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}SecuritiesAttributes1 | 985 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}ServiceLevel8Choice | 991 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}SettlementDateTimeIndication1 | 997 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}SettlementInstruction15 | 1003 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}SettlementMethod1Code | 1016 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}SettlementTimeRequest2 | 1024 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}StructuredRegulatoryReporting5 | 1032 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}StructuredRemittanceInformation22 | 1042 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}SupplementaryData1 | 1055 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}SupplementaryDataEnvelope1 | 1061 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TaxAmount3 | 1066 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TaxAuthorisation1 | 1074 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TaxData1 | 1080 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TaxParty1 | 1095 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TaxParty2 | 1102 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TaxPeriod3 | 1110 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TaxRecord3 | 1117 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TaxRecordDetails3 | 1130 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TaxRecordPeriod1Code | 1136 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TransactionAllocation2 | 1158 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}TrueFalseIndicator | 1168 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}UTIIdentifier | 1171 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13}UUIDv4Identifier | 1176 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 24 |
| complexType | 89 |
| element | 409 |
| enumeration | 55 |
| extension | 2 |
| fractionDigits | 5 |
| maxLength | 31 |
| minInclusive | 2 |
| minLength | 31 |
| pattern | 14 |
| restriction | 67 |
| schema | 1 |
| sequence | 63 |
| simpleContent | 2 |
| simpleType | 67 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
