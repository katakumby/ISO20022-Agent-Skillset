---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.008.001.14"
message_family: "pacs.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14"
source_ids: ["src-000169"]
source_editions: ["2025-2026"]
---

# pacs.008.001.14 structure

[src-000169](../../../../../raw-input/payments_clearing_and_settlement/pacs.008.001.14.xsd); `urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}AdditionalDateTime1 | 55 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}AddressType2Code | 62 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}AddressType3Choice | 72 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}AnyBICDec2014Identifier | 78 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}BICFIDec2014Identifier | 83 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}BaseOneRate | 88 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}BatchBookingIndicator | 94 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}BranchAndFinancialInstitutionIdentification8 | 97 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}BranchData5 | 103 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CashAccount40 | 111 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CashAccountType2Choice | 120 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CategoryPurpose1Choice | 126 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ChargeBearerType1Code | 132 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ChargeType3Choice | 140 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Charges16 | 146 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ClearingChannel2Code | 153 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ClearingSystemIdentification2Choice | 161 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ClearingSystemIdentification3Choice | 167 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ClearingSystemMemberIdentification2 | 173 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Contact13 | 179 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CountryCode | 196 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CreditDebitCode | 201 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CreditTransferMandateData1 | 207 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CreditTransferTransaction73 | 220 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CreditorReferenceInformation3 | 272 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CreditorReferenceType2Choice | 278 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CreditorReferenceType3 | 284 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CryptographicKey1Choice | 290 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}CurrencyExchange26 | 296 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DateAndPlaceOfBirth1 | 306 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DateAndType1 | 314 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DatePeriod2 | 320 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DateType2Choice | 326 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DecimalNumber | 332 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Document | 338 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DocumentAdjustment1 | 343 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DocumentAmount1 | 351 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DocumentAmountType1Choice | 357 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DocumentLineIdentification1 | 363 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DocumentLineInformation2 | 370 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DocumentLineType1 | 377 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DocumentLineType1Choice | 383 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DocumentType1 | 389 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}DocumentType2Choice | 395 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Exact2NumericText | 401 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Exact4AlphaNumericText | 406 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalAccountIdentification1Code | 411 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalCashAccountType1Code | 417 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalCashClearingSystem1Code | 423 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalCategoryPurpose1Code | 429 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalChargeType1Code | 435 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalClearingSystemIdentification1Code | 441 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalCreditorAgentInstruction1Code | 447 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalCreditorReferenceType1Code | 453 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalDateType1Code | 459 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalDocumentAmountType1Code | 465 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalDocumentLineType1Code | 471 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalDocumentType1Code | 477 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalFinancialInstitutionIdentification1Code | 483 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalGarnishmentType1Code | 489 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalLocalInstrument1Code | 495 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalMandateSetupReason1Code | 501 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalOrganisationIdentification1Code | 507 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalPersonIdentification1Code | 513 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalProxyAccountType1Code | 519 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalPurpose1Code | 525 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalRegulatoryReportingType1Code | 531 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ExternalServiceLevel1Code | 537 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}FIToFICustomerCreditTransferV14 | 543 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}FinancialIdentificationSchemeName1Choice | 550 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}FinancialInstitutionIdentification23 | 556 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Frequency36Choice | 566 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Frequency6Code | 573 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}FrequencyAndMoment1 | 586 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}FrequencyPeriod1 | 592 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Garnishment4 | 598 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}GarnishmentType1 | 610 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}GarnishmentType1Choice | 616 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}GenericAccountIdentification1 | 622 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}GenericFinancialIdentification1 | 629 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}GenericIdentification3 | 636 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}GenericIdentification30 | 642 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}GenericOrganisationIdentification3 | 649 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}GenericPersonIdentification2 | 656 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}GroupHeader131 | 663 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}HexBinaryText | 679 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}IBAN2007Identifier | 684 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ISODate | 689 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ISODateTime | 692 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ISOTime | 695 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ISOYear | 698 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Instruction4Code | 701 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}InstructionForCreditorAgent3 | 707 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}InstructionForNextAgent1 | 713 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}LEIIdentifier | 719 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}LocalInstrument2Choice | 724 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}MandateClassification1Choice | 730 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}MandateClassification1Code | 736 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}MandateSetupReason1Choice | 743 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}MandateTypeInformation2 | 749 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max10KBinary | 757 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max10Text | 763 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max128Text | 769 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max140Text | 775 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max15NumericText | 781 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max16Text | 786 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max2048Text | 792 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max256Text | 798 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max34Text | 804 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max350Text | 810 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max35Text | 816 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max4Text | 822 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Max70Text | 828 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}NameAndAddress18 | 834 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}NamePrefix2Code | 840 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Number | 849 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}OrganisationIdentification39 | 855 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}OrganisationIdentificationSchemeName1Choice | 862 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}OtherContact1 | 868 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Party52Choice | 874 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}PartyIdentification272 | 880 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}PaymentIdentification13 | 889 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}PaymentTypeInformation28 | 898 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}PercentageRate | 907 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}PersonIdentification18 | 913 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}PersonIdentificationSchemeName1Choice | 919 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}PhoneNumber | 925 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}PostalAddress27 | 930 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}PreferredContactMethod2Code | 952 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Priority2Code | 962 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Priority3Code | 968 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ProxyAccountIdentification1 | 975 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ProxyAccountType1Choice | 981 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}Purpose2Choice | 987 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ReferredDocumentInformation8 | 993 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}RegulatoryAuthority2 | 1001 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}RegulatoryReporting10 | 1007 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}RegulatoryReportingType1Choice | 1014 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}RegulatoryReportingType1Code | 1020 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}RemittanceAmount4 | 1027 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}RemittanceInformation26 | 1033 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}RemittanceLocation8 | 1039 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}RemittanceLocationData2 | 1045 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}RemittanceLocationMethod2Code | 1052 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}SHA256SignatureText | 1062 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}SecuritiesAttributes1 | 1067 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}ServiceLevel8Choice | 1073 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}SettlementDateTimeIndication1 | 1079 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}SettlementInstruction15 | 1085 |
| [type-0159](types/type-0159.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}SettlementMethod1Code | 1098 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}SettlementTimeRequest2 | 1106 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}StructuredRegulatoryReporting5 | 1114 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}StructuredRemittanceInformation22 | 1124 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}SupplementaryData1 | 1137 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}SupplementaryDataEnvelope1 | 1143 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TaxAmount3 | 1148 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TaxAuthorisation1 | 1156 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TaxData1 | 1162 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TaxParty1 | 1177 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TaxParty2 | 1184 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TaxPeriod3 | 1192 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TaxRecord3 | 1199 |
| [type-0172](types/type-0172.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TaxRecordDetails3 | 1212 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TaxRecordPeriod1Code | 1218 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}TrueFalseIndicator | 1240 |
| [type-0175](types/type-0175.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}UTIIdentifier | 1243 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14}UUIDv4Identifier | 1248 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 27 |
| complexType | 99 |
| element | 374 |
| enumeration | 77 |
| extension | 2 |
| fractionDigits | 6 |
| maxLength | 34 |
| minInclusive | 2 |
| minLength | 34 |
| pattern | 15 |
| restriction | 76 |
| schema | 1 |
| sequence | 70 |
| simpleContent | 2 |
| simpleType | 76 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
