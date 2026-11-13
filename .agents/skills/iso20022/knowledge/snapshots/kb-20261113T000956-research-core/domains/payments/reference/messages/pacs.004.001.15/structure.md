---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.004.001.15"
message_family: "pacs.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15"
source_ids: ["src-000167"]
source_editions: ["2025-2026"]
---

# pacs.004.001.15 structure

[src-000167](../../../../../raw-input/payments_clearing_and_settlement/pacs.004.001.15.xsd); `urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}AddressType3Choice | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}AmendmentInformationDetails15 | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}AmountType4Choice | 87 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}AnyBICDec2014Identifier | 93 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Authorisation1Choice | 98 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Authorisation1Code | 104 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}BICFIDec2014Identifier | 112 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}BaseOneRate | 117 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}BatchBookingIndicator | 123 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}BranchAndFinancialInstitutionIdentification8 | 126 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}BranchData5 | 132 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CashAccount40 | 140 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CashAccountType2Choice | 149 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CategoryPurpose1Choice | 155 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ChargeBearerType1Code | 161 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ChargeType3Choice | 169 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Charges16 | 175 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ClearingChannel2Code | 182 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ClearingSystemIdentification2Choice | 190 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ClearingSystemIdentification3Choice | 196 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ClearingSystemMemberIdentification2 | 202 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Contact13 | 208 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CountryCode | 225 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CreditDebitCode | 230 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CreditTransferMandateData1 | 236 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CreditTransferTransaction72 | 249 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CreditTransferTransaction82 | 284 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CreditorReferenceInformation3 | 326 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CreditorReferenceType2Choice | 332 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CreditorReferenceType3 | 338 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CryptographicKey1Choice | 344 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}CurrencyExchange26 | 350 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DateAndDateTime2Choice | 360 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DateAndPlaceOfBirth1 | 366 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DateAndType1 | 374 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DatePeriod2 | 380 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DateType2Choice | 386 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DecimalNumber | 392 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Document | 398 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DocumentAdjustment1 | 403 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DocumentAmount1 | 411 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DocumentAmountType1Choice | 417 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DocumentLineIdentification1 | 423 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DocumentLineInformation2 | 430 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DocumentLineType1 | 437 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DocumentLineType1Choice | 443 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DocumentType1 | 449 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}DocumentType2Choice | 455 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}EquivalentAmount2 | 461 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Exact2NumericText | 467 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Exact4AlphaNumericText | 472 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalAccountIdentification1Code | 477 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalCashAccountType1Code | 483 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalCashClearingSystem1Code | 489 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalCategoryPurpose1Code | 495 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalChargeType1Code | 501 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalClearingSystemIdentification1Code | 507 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalCreditorAgentInstruction1Code | 513 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalCreditorReferenceType1Code | 519 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalDateType1Code | 525 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalDocumentAmountType1Code | 531 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalDocumentLineType1Code | 537 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalDocumentType1Code | 543 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalFinancialInstitutionIdentification1Code | 549 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalGarnishmentType1Code | 555 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalLocalInstrument1Code | 561 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalMandateSetupReason1Code | 567 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalOrganisationIdentification1Code | 573 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalPersonIdentification1Code | 579 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalProxyAccountType1Code | 585 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalPurpose1Code | 591 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalReturnReason1Code | 597 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ExternalServiceLevel1Code | 603 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}FinancialIdentificationSchemeName1Choice | 609 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}FinancialInstitutionIdentification23 | 615 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Frequency36Choice | 625 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Frequency6Code | 632 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}FrequencyAndMoment1 | 645 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}FrequencyPeriod1 | 651 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Garnishment4 | 657 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}GarnishmentType1 | 669 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}GarnishmentType1Choice | 675 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}GenericAccountIdentification1 | 681 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}GenericFinancialIdentification1 | 688 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}GenericIdentification3 | 695 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}GenericIdentification30 | 701 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}GenericOrganisationIdentification3 | 708 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}GenericPersonIdentification2 | 715 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}GroupHeader123 | 722 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}HexBinaryText | 739 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}IBAN2007Identifier | 744 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ISODate | 749 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ISODateTime | 752 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ISOTime | 755 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ISOYear | 758 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Instruction4Code | 761 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}InstructionForCreditorAgent3 | 767 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}InstructionForNextAgent1 | 773 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}LEIIdentifier | 779 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}LocalInstrument2Choice | 784 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}MandateClassification1Choice | 790 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}MandateClassification1Code | 796 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}MandateRelatedData5Choice | 803 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}MandateRelatedInformation16 | 809 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}MandateSetupReason1Choice | 823 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}MandateTypeInformation2 | 829 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max1025Text | 837 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max105Text | 843 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max10KBinary | 849 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max128Text | 855 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max140Text | 861 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max15NumericText | 867 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max16Text | 872 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max2048Text | 878 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max256Text | 884 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max34Text | 890 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max350Text | 896 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max35Text | 902 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max4Text | 908 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Max70Text | 914 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}NamePrefix2Code | 920 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Number | 929 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}OrganisationIdentification39 | 935 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}OrganisationIdentificationSchemeName1Choice | 942 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}OriginalGroupHeader19 | 948 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}OriginalGroupInformation33 | 956 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}OriginalTransactionReference45 | 963 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}OtherContact1 | 991 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Party50Choice | 997 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Party52Choice | 1003 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PartyIdentification272 | 1009 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PaymentIdentification13 | 1018 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PaymentMethod4Code | 1027 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PaymentReturnReason7 | 1035 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PaymentReturnV15 | 1042 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PaymentTransaction168 | 1050 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PaymentTypeInformation27 | 1082 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PaymentTypeInformation28 | 1092 |
| [type-0149](types/type-0149.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PercentageRate | 1101 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PersonIdentification18 | 1107 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PersonIdentificationSchemeName1Choice | 1113 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PhoneNumber | 1119 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PostalAddress27 | 1124 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}PreferredContactMethod2Code | 1146 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Priority2Code | 1156 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Priority3Code | 1162 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ProxyAccountIdentification1 | 1169 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ProxyAccountType1Choice | 1175 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}Purpose2Choice | 1181 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}References80Choice | 1187 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ReferredDocumentInformation8 | 1202 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}RemittanceAmount4 | 1210 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}RemittanceInformation2 | 1216 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}RemittanceInformation26 | 1221 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ReturnReason5Choice | 1227 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}SHA256SignatureText | 1233 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}SecuritiesAttributes1 | 1238 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}SequenceType3Code | 1244 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}ServiceLevel8Choice | 1253 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}SettlementDateTimeIndication1 | 1259 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}SettlementInstruction15 | 1265 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}SettlementMethod1Code | 1278 |
| [type-0173](types/type-0173.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}SettlementTimeRequest2 | 1286 |
| [type-0174](types/type-0174.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}StructuredRemittanceInformation22 | 1294 |
| [type-0175](types/type-0175.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}SupplementaryData1 | 1307 |
| [type-0176](types/type-0176.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}SupplementaryDataEnvelope1 | 1313 |
| [type-0177](types/type-0177.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TaxAmount3 | 1318 |
| [type-0178](types/type-0178.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TaxAuthorisation1 | 1326 |
| [type-0179](types/type-0179.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TaxData1 | 1332 |
| [type-0180](types/type-0180.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TaxParty1 | 1347 |
| [type-0181](types/type-0181.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TaxParty2 | 1354 |
| [type-0182](types/type-0182.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TaxPeriod3 | 1362 |
| [type-0183](types/type-0183.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TaxRecord3 | 1369 |
| [type-0184](types/type-0184.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TaxRecordDetails3 | 1382 |
| [type-0185](types/type-0185.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TaxRecordPeriod1Code | 1388 |
| [type-0186](types/type-0186.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TransactionAllocation2 | 1410 |
| [type-0187](types/type-0187.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TransactionParties11 | 1420 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}TrueFalseIndicator | 1447 |
| [type-0189](types/type-0189.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}UTIIdentifier | 1450 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.004.001.15}UUIDv4Identifier | 1455 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 33 |
| complexType | 111 |
| element | 519 |
| enumeration | 81 |
| extension | 2 |
| fractionDigits | 6 |
| maxLength | 35 |
| minInclusive | 2 |
| minLength | 35 |
| pattern | 15 |
| restriction | 78 |
| schema | 1 |
| sequence | 76 |
| simpleContent | 2 |
| simpleType | 78 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/48176637b5bdf90d9d201194.md) · [Message](index.md)
