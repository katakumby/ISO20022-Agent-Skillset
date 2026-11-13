---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pain.002.001.15"
message_family: "pain.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:pain.002.001.15"
source_ids: ["src-000177"]
source_editions: ["2025-2026"]
---

# pain.002.001.15 structure

[src-000177](../../../../../raw-input/payments_initiation/pain.002.001.15.xsd); `urn:iso:std:iso:20022:tech:xsd:pain.002.001.15`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pain.002.001.15 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}AddressType3Choice | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}AmendmentInformationDetails15 | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}AmountType4Choice | 87 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}AnyBICDec2014Identifier | 93 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}BICFIDec2014Identifier | 98 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}BaseOneRate | 103 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}BranchAndFinancialInstitutionIdentification8 | 109 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}BranchData5 | 115 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CashAccount40 | 123 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CashAccountType2Choice | 132 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CategoryPurpose1Choice | 138 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ChargeBearerType1Code | 144 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ChargeType3Choice | 152 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Charges16 | 158 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ClearingChannel2Code | 165 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ClearingSystemIdentification2Choice | 173 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ClearingSystemIdentification3Choice | 179 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ClearingSystemMemberIdentification2 | 185 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Contact13 | 191 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CountryCode | 208 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CreditDebitCode | 213 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CreditTransferMandateData1 | 219 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CreditorReferenceInformation3 | 232 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CreditorReferenceType2Choice | 238 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CreditorReferenceType3 | 244 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CurrencyExchange13 | 250 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}CustomerPaymentStatusReportV15 | 258 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DateAndDateTime2Choice | 266 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DateAndPlaceOfBirth1 | 272 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DateAndType1 | 280 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DatePeriod2 | 286 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DateType2Choice | 292 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DecimalNumber | 298 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Document | 304 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DocumentAdjustment1 | 309 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DocumentAmount1 | 317 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DocumentAmountType1Choice | 323 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DocumentLineIdentification1 | 329 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DocumentLineInformation2 | 336 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DocumentLineType1 | 343 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DocumentLineType1Choice | 349 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DocumentType1 | 355 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}DocumentType2Choice | 361 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}EquivalentAmount2 | 367 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Exact2NumericText | 373 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Exact4AlphaNumericText | 378 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalAccountIdentification1Code | 383 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalCashAccountType1Code | 389 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalCashClearingSystem1Code | 395 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalCategoryPurpose1Code | 401 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalChargeType1Code | 407 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalClearingSystemIdentification1Code | 413 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalCreditorReferenceType1Code | 419 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalDateType1Code | 425 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalDocumentAmountType1Code | 431 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalDocumentLineType1Code | 437 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalDocumentType1Code | 443 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalFinancialInstitutionIdentification1Code | 449 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalGarnishmentType1Code | 455 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalLocalInstrument1Code | 461 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalMandateSetupReason1Code | 467 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalOrganisationIdentification1Code | 473 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalPaymentGroupStatus1Code | 479 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalPaymentTransactionStatus1Code | 485 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalPersonIdentification1Code | 491 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalProxyAccountType1Code | 497 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalPurpose1Code | 503 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalServiceLevel1Code | 509 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ExternalStatusReason1Code | 515 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}FinancialIdentificationSchemeName1Choice | 521 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}FinancialInstitutionIdentification23 | 527 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Frequency36Choice | 537 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Frequency6Code | 544 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}FrequencyAndMoment1 | 557 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}FrequencyPeriod1 | 563 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Garnishment4 | 569 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}GarnishmentType1 | 581 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}GarnishmentType1Choice | 587 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}GenericAccountIdentification1 | 593 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}GenericFinancialIdentification1 | 600 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}GenericIdentification3 | 607 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}GenericIdentification30 | 613 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}GenericOrganisationIdentification3 | 620 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}GenericPersonIdentification2 | 627 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}GroupHeader128 | 634 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}IBAN2007Identifier | 644 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ISODate | 649 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ISODateTime | 652 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ISOYear | 655 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}LEIIdentifier | 658 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}LocalInstrument2Choice | 663 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}MandateClassification1Choice | 669 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}MandateClassification1Code | 675 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}MandateRelatedData5Choice | 682 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}MandateRelatedInformation16 | 688 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}MandateSetupReason1Choice | 702 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}MandateTypeInformation2 | 708 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max1025Text | 716 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max105Text | 722 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max10KBinary | 728 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max128Text | 734 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max140Text | 740 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max15NumericText | 746 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max16Text | 751 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max2048Text | 757 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max256Text | 763 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max34Text | 769 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max350Text | 775 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max35Text | 781 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max4Text | 787 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Max70Text | 793 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}NamePrefix2Code | 799 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Number | 808 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}NumberOfTransactionsPerStatus5 | 814 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}OrganisationIdentification39 | 821 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}OrganisationIdentificationSchemeName1Choice | 828 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}OriginalGroupHeader22 | 834 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}OriginalPaymentInstruction56 | 846 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}OriginalTransactionReference47 | 857 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}OtherContact1 | 883 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Party50Choice | 889 |
| [type-0132](types/type-0132.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Party52Choice | 895 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PartyIdentification272 | 901 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PaymentMethod4Code | 910 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PaymentTransaction178 | 918 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PaymentTypeInformation27 | 935 |
| [type-0137](types/type-0137.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PercentageRate | 945 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PersonIdentification18 | 951 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PersonIdentificationSchemeName1Choice | 957 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PhoneNumber | 963 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PostalAddress27 | 968 |
| [type-0142](types/type-0142.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}PreferredContactMethod2Code | 990 |
| [type-0143](types/type-0143.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Priority2Code | 1000 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ProxyAccountIdentification1 | 1006 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ProxyAccountType1Choice | 1012 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}Purpose2Choice | 1018 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ReferredDocumentInformation8 | 1024 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}RemittanceAmount4 | 1032 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}RemittanceInformation26 | 1038 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}SecuritiesAttributes1 | 1044 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}SequenceType3Code | 1050 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}ServiceLevel8Choice | 1059 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}SettlementInstruction15 | 1065 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}SettlementMethod1Code | 1078 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}StatusReason6Choice | 1086 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}StatusReasonInformation14 | 1092 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}StructuredRemittanceInformation22 | 1099 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}SupplementaryData1 | 1112 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}SupplementaryDataEnvelope1 | 1118 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TaxAmount3 | 1123 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TaxAuthorisation1 | 1131 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TaxData1 | 1137 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TaxParty1 | 1152 |
| [type-0164](types/type-0164.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TaxParty2 | 1159 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TaxPeriod3 | 1167 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TaxRecord3 | 1174 |
| [type-0167](types/type-0167.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TaxRecordDetails3 | 1187 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TaxRecordPeriod1Code | 1193 |
| [type-0169](types/type-0169.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TrackerData7 | 1215 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TrackerRecord5 | 1222 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}TrueFalseIndicator | 1230 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}UTIIdentifier | 1233 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.002.001.15}UUIDv4Identifier | 1238 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 30 |
| complexType | 100 |
| element | 377 |
| enumeration | 72 |
| extension | 2 |
| fractionDigits | 6 |
| maxLength | 36 |
| minInclusive | 2 |
| minLength | 36 |
| pattern | 13 |
| restriction | 72 |
| schema | 1 |
| sequence | 68 |
| simpleContent | 2 |
| simpleType | 72 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/d113a4312e464ec594fddc0e.md) · [Message](index.md)
