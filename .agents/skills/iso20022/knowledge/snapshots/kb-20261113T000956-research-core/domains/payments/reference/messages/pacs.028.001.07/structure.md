---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.028.001.07"
message_family: "pacs.028"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07"
source_ids: ["src-000172"]
source_editions: ["2025-2026"]
---

# pacs.028.001.07 structure

[src-000172](../../../../../raw-input/payments_clearing_and_settlement/pacs.028.001.07.xsd); `urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}AddressType3Choice | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}AmendmentInformationDetails15 | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}AmountType4Choice | 87 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}AnyBICDec2014Identifier | 93 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}BICFIDec2014Identifier | 98 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}BranchAndFinancialInstitutionIdentification8 | 103 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}BranchData5 | 109 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}CashAccount40 | 117 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}CashAccountType2Choice | 126 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}CategoryPurpose1Choice | 132 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ClearingChannel2Code | 138 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ClearingSystemIdentification2Choice | 146 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ClearingSystemIdentification3Choice | 152 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ClearingSystemMemberIdentification2 | 158 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Contact13 | 164 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}CountryCode | 181 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}CreditDebitCode | 186 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}CreditTransferMandateData1 | 192 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}CreditorReferenceInformation3 | 205 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}CreditorReferenceType2Choice | 211 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}CreditorReferenceType3 | 217 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DateAndDateTime2Choice | 223 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DateAndPlaceOfBirth1 | 229 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DateAndType1 | 237 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DatePeriod2 | 243 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DateType2Choice | 249 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DecimalNumber | 255 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Document | 261 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DocumentAdjustment1 | 266 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DocumentAmount1 | 274 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DocumentAmountType1Choice | 280 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DocumentLineIdentification1 | 286 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DocumentLineInformation2 | 293 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DocumentLineType1 | 300 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DocumentLineType1Choice | 306 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DocumentType1 | 312 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}DocumentType2Choice | 318 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}EquivalentAmount2 | 324 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Exact2NumericText | 330 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Exact4AlphaNumericText | 335 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalAccountIdentification1Code | 340 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalCashAccountType1Code | 346 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalCashClearingSystem1Code | 352 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalCategoryPurpose1Code | 358 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalClearingSystemIdentification1Code | 364 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalCreditorReferenceType1Code | 370 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalDateType1Code | 376 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalDocumentAmountType1Code | 382 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalDocumentLineType1Code | 388 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalDocumentType1Code | 394 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalFinancialInstitutionIdentification1Code | 400 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalGarnishmentType1Code | 406 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalLocalInstrument1Code | 412 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalMandateSetupReason1Code | 418 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalOrganisationIdentification1Code | 424 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalPersonIdentification1Code | 430 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalProxyAccountType1Code | 436 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalPurpose1Code | 442 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ExternalServiceLevel1Code | 448 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}FIToFIPaymentStatusRequestV07 | 454 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}FinancialIdentificationSchemeName1Choice | 462 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}FinancialInstitutionIdentification23 | 468 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Frequency36Choice | 478 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Frequency6Code | 485 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}FrequencyAndMoment1 | 498 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}FrequencyPeriod1 | 504 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Garnishment4 | 510 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}GarnishmentType1 | 522 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}GarnishmentType1Choice | 528 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}GenericAccountIdentification1 | 534 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}GenericFinancialIdentification1 | 541 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}GenericIdentification30 | 548 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}GenericOrganisationIdentification3 | 555 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}GenericPersonIdentification2 | 562 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}GroupHeader109 | 569 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}IBAN2007Identifier | 577 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ISODate | 582 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ISODateTime | 585 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ISOYear | 588 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}LEIIdentifier | 591 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}LocalInstrument2Choice | 596 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}MandateClassification1Choice | 602 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}MandateClassification1Code | 608 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}MandateRelatedData5Choice | 615 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}MandateRelatedInformation16 | 621 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}MandateSetupReason1Choice | 635 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}MandateTypeInformation2 | 641 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max1025Text | 649 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max10KBinary | 655 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max128Text | 661 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max140Text | 667 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max15NumericText | 673 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max16Text | 678 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max2048Text | 684 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max256Text | 690 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max34Text | 696 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max350Text | 702 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max35Text | 708 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max4Text | 714 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Max70Text | 720 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}NamePrefix2Code | 726 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Number | 735 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}OrganisationIdentification39 | 741 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}OrganisationIdentificationSchemeName1Choice | 748 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}OriginalGroupInformation27 | 754 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}OriginalGroupInformation33 | 763 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}OriginalTransactionReference47 | 770 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}OtherContact1 | 796 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Party50Choice | 802 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Party52Choice | 808 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PartyIdentification272 | 814 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PaymentMethod4Code | 823 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PaymentTransaction171 | 831 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PaymentTypeInformation27 | 847 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PercentageRate | 857 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PersonIdentification18 | 863 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PersonIdentificationSchemeName1Choice | 869 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PhoneNumber | 875 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PostalAddress27 | 880 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}PreferredContactMethod2Code | 902 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Priority2Code | 912 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ProxyAccountIdentification1 | 918 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ProxyAccountType1Choice | 924 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}Purpose2Choice | 930 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ReferredDocumentInformation8 | 936 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}RemittanceAmount4 | 944 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}RemittanceInformation26 | 950 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}SecuritiesAttributes1 | 956 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}SequenceType3Code | 962 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}ServiceLevel8Choice | 971 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}SettlementInstruction15 | 977 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}SettlementMethod1Code | 990 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}StructuredRemittanceInformation22 | 998 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}SupplementaryData1 | 1011 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}SupplementaryDataEnvelope1 | 1017 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TaxAmount3 | 1022 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TaxAuthorisation1 | 1030 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TaxData1 | 1036 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TaxParty1 | 1051 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TaxParty2 | 1058 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TaxPeriod3 | 1066 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TaxRecord3 | 1073 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TaxRecordDetails3 | 1086 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TaxRecordPeriod1Code | 1092 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}TrueFalseIndicator | 1114 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}UTIIdentifier | 1117 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07}UUIDv4Identifier | 1122 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 28 |
| complexType | 91 |
| element | 341 |
| enumeration | 68 |
| extension | 2 |
| fractionDigits | 5 |
| maxLength | 31 |
| minInclusive | 2 |
| minLength | 31 |
| pattern | 13 |
| restriction | 65 |
| schema | 1 |
| sequence | 61 |
| simpleContent | 2 |
| simpleType | 65 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/8f4e81e39e533c64b1bb34ac.md) · [Message](index.md)
