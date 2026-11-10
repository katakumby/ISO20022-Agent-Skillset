---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.007.001.14"
message_family: "pacs.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14"
source_ids: ["src-000168"]
source_editions: ["2025-2026"]
---

# pacs.007.001.14 structure

[src-000168](../../../../../raw-input/payments_clearing_and_settlement/pacs.007.001.14.xsd); `urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}AddressType3Choice | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}AmendmentInformationDetails15 | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}AmountType4Choice | 87 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}AnyBICDec2014Identifier | 93 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Authorisation1Choice | 98 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Authorisation1Code | 104 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}BICFIDec2014Identifier | 112 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}BaseOneRate | 117 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}BatchBookingIndicator | 123 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}BranchAndFinancialInstitutionIdentification8 | 126 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}BranchData5 | 132 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}CashAccount40 | 140 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}CashAccountType2Choice | 149 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}CategoryPurpose1Choice | 155 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ChargeBearerType1Code | 161 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ChargeType3Choice | 169 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Charges16 | 175 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ClearingChannel2Code | 182 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ClearingSystemIdentification2Choice | 190 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ClearingSystemIdentification3Choice | 196 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ClearingSystemMemberIdentification2 | 202 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Contact13 | 208 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}CountryCode | 225 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}CreditDebitCode | 230 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}CreditTransferMandateData1 | 236 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}CreditorReferenceInformation3 | 249 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}CreditorReferenceType2Choice | 255 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}CreditorReferenceType3 | 261 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DateAndDateTime2Choice | 267 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DateAndPlaceOfBirth1 | 273 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DateAndType1 | 281 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DatePeriod2 | 287 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DateType2Choice | 293 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DecimalNumber | 299 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Document | 305 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DocumentAdjustment1 | 310 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DocumentAmount1 | 318 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DocumentAmountType1Choice | 324 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DocumentLineIdentification1 | 330 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DocumentLineInformation2 | 337 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DocumentLineType1 | 344 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DocumentLineType1Choice | 350 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DocumentType1 | 356 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}DocumentType2Choice | 362 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}EquivalentAmount2 | 368 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Exact2NumericText | 374 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Exact4AlphaNumericText | 379 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalAccountIdentification1Code | 384 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalCashAccountType1Code | 390 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalCashClearingSystem1Code | 396 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalCategoryPurpose1Code | 402 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalChargeType1Code | 408 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalClearingSystemIdentification1Code | 414 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalCreditorReferenceType1Code | 420 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalDateType1Code | 426 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalDocumentAmountType1Code | 432 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalDocumentLineType1Code | 438 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalDocumentType1Code | 444 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalFinancialInstitutionIdentification1Code | 450 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalGarnishmentType1Code | 456 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalLocalInstrument1Code | 462 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalMandateSetupReason1Code | 468 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalOrganisationIdentification1Code | 474 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalPersonIdentification1Code | 480 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalProxyAccountType1Code | 486 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalPurpose1Code | 492 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalReversalReason1Code | 498 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ExternalServiceLevel1Code | 504 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}FIToFIPaymentReversalV14 | 510 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}FinancialIdentificationSchemeName1Choice | 518 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}FinancialInstitutionIdentification23 | 524 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Frequency36Choice | 534 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Frequency6Code | 541 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}FrequencyAndMoment1 | 554 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}FrequencyPeriod1 | 560 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Garnishment4 | 566 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}GarnishmentType1 | 578 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}GarnishmentType1Choice | 584 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}GenericAccountIdentification1 | 590 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}GenericFinancialIdentification1 | 597 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}GenericIdentification3 | 604 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}GenericIdentification30 | 610 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}GenericOrganisationIdentification3 | 617 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}GenericPersonIdentification2 | 624 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}GroupHeader127 | 631 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}IBAN2007Identifier | 647 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ISODate | 652 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ISODateTime | 655 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ISOYear | 658 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}LEIIdentifier | 661 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}LocalInstrument2Choice | 666 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}MandateClassification1Choice | 672 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}MandateClassification1Code | 678 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}MandateRelatedData5Choice | 685 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}MandateRelatedInformation16 | 691 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}MandateSetupReason1Choice | 705 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}MandateTypeInformation2 | 711 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max1025Text | 719 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max105Text | 725 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max10KBinary | 731 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max128Text | 737 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max140Text | 743 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max15NumericText | 749 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max16Text | 754 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max2048Text | 760 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max256Text | 766 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max34Text | 772 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max350Text | 778 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max35Text | 784 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max4Text | 790 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Max70Text | 796 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}NamePrefix2Code | 802 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Number | 811 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}OrganisationIdentification39 | 817 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}OrganisationIdentificationSchemeName1Choice | 824 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}OriginalGroupHeader20 | 830 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}OriginalGroupInformation33 | 838 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}OriginalTransactionReference47 | 845 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}OtherContact1 | 871 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Party50Choice | 877 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Party52Choice | 883 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PartyIdentification272 | 889 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PaymentMethod4Code | 898 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PaymentReversalReason10 | 906 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PaymentTransaction182 | 913 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PaymentTypeInformation27 | 939 |
| [type-0137](types/type-0137.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PercentageRate | 949 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PersonIdentification18 | 955 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PersonIdentificationSchemeName1Choice | 961 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PhoneNumber | 967 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PostalAddress27 | 972 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}PreferredContactMethod2Code | 994 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Priority2Code | 1004 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Priority3Code | 1010 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ProxyAccountIdentification1 | 1017 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ProxyAccountType1Choice | 1023 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}Purpose2Choice | 1029 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ReferredDocumentInformation8 | 1035 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}RemittanceAmount4 | 1043 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}RemittanceInformation26 | 1049 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ReversalReason4Choice | 1055 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}SecuritiesAttributes1 | 1061 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}SequenceType3Code | 1067 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}ServiceLevel8Choice | 1076 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}SettlementDateTimeIndication1 | 1082 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}SettlementInstruction15 | 1088 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}SettlementMethod1Code | 1101 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}StructuredRemittanceInformation22 | 1109 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}SupplementaryData1 | 1122 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}SupplementaryDataEnvelope1 | 1128 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TaxAmount3 | 1133 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TaxAuthorisation1 | 1141 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TaxData1 | 1147 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TaxParty1 | 1162 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TaxParty2 | 1169 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TaxPeriod3 | 1177 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TaxRecord3 | 1184 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TaxRecordDetails3 | 1197 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TaxRecordPeriod1Code | 1203 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}TrueFalseIndicator | 1225 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}UTIIdentifier | 1228 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.007.001.14}UUIDv4Identifier | 1233 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 31 |
| complexType | 98 |
| element | 374 |
| enumeration | 79 |
| extension | 2 |
| fractionDigits | 6 |
| maxLength | 34 |
| minInclusive | 2 |
| minLength | 34 |
| pattern | 13 |
| restriction | 73 |
| schema | 1 |
| sequence | 65 |
| simpleContent | 2 |
| simpleType | 73 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
