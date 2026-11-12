---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pain.001.001.13"
message_family: "pain.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:pain.001.001.13"
source_ids: ["src-000176"]
source_editions: ["2025-2026"]
---

# pain.001.001.13 structure

[src-000176](../../../../../raw-input/payments_initiation/pain.001.001.13.xsd); `urn:iso:std:iso:20022:tech:xsd:pain.001.001.13`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pain.001.001.13 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}AddressType3Choice | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}AdviceType1 | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}AdviceType1Choice | 77 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}AdviceType1Code | 83 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}AmountType4Choice | 89 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}AnyBICDec2014Identifier | 95 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Authorisation1Choice | 100 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Authorisation1Code | 106 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}BICFIDec2014Identifier | 114 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}BaseOneRate | 119 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}BatchBookingIndicator | 125 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}BranchAndFinancialInstitutionIdentification8 | 128 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}BranchData5 | 134 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CashAccount40 | 142 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CashAccountType2Choice | 151 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CategoryPurpose1Choice | 157 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ChargeBearerType1Code | 163 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Cheque19 | 171 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ChequeDelivery1Code | 187 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ChequeDeliveryMethod1Choice | 203 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ChequeType2Code | 209 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ClearingSystemIdentification2Choice | 218 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ClearingSystemMemberIdentification2 | 224 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Contact13 | 230 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CountryCode | 247 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CreditDebitCode | 252 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CreditTransferMandateData1 | 258 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CreditTransferTransaction76 | 271 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CreditorReferenceInformation3 | 302 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CreditorReferenceType2Choice | 308 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CreditorReferenceType3 | 314 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}CustomerCreditTransferInitiationV13 | 320 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DateAndDateTime2Choice | 327 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DateAndPlaceOfBirth1 | 333 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DateAndType1 | 341 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DatePeriod2 | 347 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DateType2Choice | 353 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DecimalNumber | 359 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Document | 365 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DocumentAdjustment1 | 370 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DocumentAmount1 | 378 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DocumentAmountType1Choice | 384 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DocumentLineIdentification1 | 390 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DocumentLineInformation2 | 397 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DocumentLineType1 | 404 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DocumentLineType1Choice | 410 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DocumentType1 | 416 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}DocumentType2Choice | 422 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}EquivalentAmount2 | 428 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Exact2NumericText | 434 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Exact4AlphaNumericText | 439 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExchangeRate1 | 444 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExchangeRateType1Code | 452 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalAccountIdentification1Code | 459 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalCashAccountType1Code | 465 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalCategoryPurpose1Code | 471 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalClearingSystemIdentification1Code | 477 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalCreditorAgentInstruction1Code | 483 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalCreditorReferenceType1Code | 489 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalDateType1Code | 495 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalDebtorAgentInstruction1Code | 501 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalDocumentAmountType1Code | 507 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalDocumentLineType1Code | 513 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalDocumentType1Code | 519 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalFinancialInstitutionIdentification1Code | 525 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalGarnishmentType1Code | 531 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalLocalInstrument1Code | 537 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalMandateSetupReason1Code | 543 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalOrganisationIdentification1Code | 549 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalPersonIdentification1Code | 555 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalProxyAccountType1Code | 561 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalPurpose1Code | 567 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalRegulatoryReportingType1Code | 573 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ExternalServiceLevel1Code | 579 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}FinancialIdentificationSchemeName1Choice | 585 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}FinancialInstitutionIdentification23 | 591 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Frequency36Choice | 601 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Frequency6Code | 608 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}FrequencyAndMoment1 | 621 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}FrequencyPeriod1 | 627 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Garnishment4 | 633 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}GarnishmentType1 | 645 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}GarnishmentType1Choice | 651 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}GenericAccountIdentification1 | 657 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}GenericFinancialIdentification1 | 664 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}GenericIdentification30 | 671 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}GenericOrganisationIdentification3 | 678 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}GenericPersonIdentification2 | 685 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}GroupHeader114 | 692 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}IBAN2007Identifier | 704 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ISODate | 709 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ISODateTime | 712 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ISOYear | 715 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}InstructionForCreditorAgent3 | 718 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}InstructionForDebtorAgent1 | 724 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}LEIIdentifier | 730 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}LocalInstrument2Choice | 735 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}MandateClassification1Choice | 741 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}MandateClassification1Code | 747 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}MandateSetupReason1Choice | 754 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}MandateTypeInformation2 | 760 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max10KBinary | 768 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max10Text | 774 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max128Text | 780 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max140Text | 786 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max15NumericText | 792 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max16Text | 797 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max2048Text | 803 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max256Text | 809 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max34Text | 815 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max350Text | 821 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max35Text | 827 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max4Text | 833 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Max70Text | 839 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}NameAndAddress18 | 845 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}NamePrefix2Code | 851 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Number | 860 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}OrganisationIdentification39 | 866 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}OrganisationIdentificationSchemeName1Choice | 873 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}OtherContact1 | 879 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Party52Choice | 885 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PartyIdentification272 | 891 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PaymentIdentification6 | 900 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PaymentInitiationSource1 | 907 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PaymentInstruction51 | 914 |
| [type-0136](types/type-0136.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PaymentMethod3Code | 937 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PaymentTypeInformation26 | 944 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PercentageRate | 952 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PersonIdentification18 | 958 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PersonIdentificationSchemeName1Choice | 964 |
| [type-0141](types/type-0141.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PhoneNumber | 970 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PostalAddress27 | 975 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}PreferredContactMethod2Code | 997 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Priority2Code | 1007 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ProxyAccountIdentification1 | 1013 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ProxyAccountType1Choice | 1019 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}Purpose2Choice | 1025 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ReferredDocumentInformation8 | 1031 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}RegulatoryAuthority2 | 1039 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}RegulatoryReporting10 | 1045 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}RegulatoryReportingType1Choice | 1052 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}RegulatoryReportingType1Code | 1058 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}RemittanceAmount4 | 1065 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}RemittanceInformation26 | 1071 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}RemittanceLocation8 | 1077 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}RemittanceLocationData2 | 1083 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}RemittanceLocationMethod2Code | 1090 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}SecuritiesAttributes1 | 1100 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}ServiceLevel8Choice | 1106 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}StructuredRegulatoryReporting5 | 1112 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}StructuredRemittanceInformation22 | 1122 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}SupplementaryData1 | 1135 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}SupplementaryDataEnvelope1 | 1141 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TaxAmount3 | 1146 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TaxAuthorisation1 | 1154 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TaxData1 | 1160 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TaxParty1 | 1175 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TaxParty2 | 1182 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TaxPeriod3 | 1190 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TaxRecord3 | 1197 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TaxRecordDetails3 | 1210 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TaxRecordPeriod1Code | 1216 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}TrueFalseIndicator | 1238 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}UTIIdentifier | 1241 |
| [type-0175](types/type-0175.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.001.001.13}UUIDv4Identifier | 1246 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 29 |
| complexType | 100 |
| element | 363 |
| enumeration | 93 |
| extension | 2 |
| fractionDigits | 6 |
| maxLength | 33 |
| minInclusive | 2 |
| minLength | 33 |
| pattern | 13 |
| restriction | 74 |
| schema | 1 |
| sequence | 69 |
| simpleContent | 2 |
| simpleType | 74 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
