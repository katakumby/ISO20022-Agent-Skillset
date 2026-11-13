---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pain.007.001.13"
message_family: "pain.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:pain.007.001.13"
source_ids: ["src-000178"]
source_editions: ["2025-2026"]
---

# pain.007.001.13 structure

[src-000178](../../../../../raw-input/payments_initiation/pain.007.001.13.xsd); `urn:iso:std:iso:20022:tech:xsd:pain.007.001.13`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pain.007.001.13 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}AddressType3Choice | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}AmendmentInformationDetails15 | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}AmountType4Choice | 87 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}AnyBICDec2014Identifier | 93 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Authorisation1Choice | 98 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Authorisation1Code | 104 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}BICFIDec2014Identifier | 112 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}BatchBookingIndicator | 117 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}BranchAndFinancialInstitutionIdentification8 | 120 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}BranchData5 | 126 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CashAccount40 | 134 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CashAccountType2Choice | 143 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CategoryPurpose1Choice | 149 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ChargeBearerType1Code | 155 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ClearingChannel2Code | 163 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ClearingSystemIdentification2Choice | 171 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ClearingSystemIdentification3Choice | 177 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ClearingSystemMemberIdentification2 | 183 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Contact13 | 189 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CountryCode | 206 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CreditDebitCode | 211 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CreditTransferMandateData1 | 217 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CreditorReferenceInformation3 | 230 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CreditorReferenceType2Choice | 236 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CreditorReferenceType3 | 242 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}CustomerPaymentReversalV13 | 248 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DateAndDateTime2Choice | 256 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DateAndPlaceOfBirth1 | 262 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DateAndType1 | 270 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DatePeriod2 | 276 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DateType2Choice | 282 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DecimalNumber | 288 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Document | 294 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DocumentAdjustment1 | 299 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DocumentAmount1 | 307 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DocumentAmountType1Choice | 313 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DocumentLineIdentification1 | 319 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DocumentLineInformation2 | 326 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DocumentLineType1 | 333 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DocumentLineType1Choice | 339 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DocumentType1 | 345 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}DocumentType2Choice | 351 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}EquivalentAmount2 | 357 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Exact2NumericText | 363 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Exact4AlphaNumericText | 368 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalAccountIdentification1Code | 373 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalCashAccountType1Code | 379 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalCashClearingSystem1Code | 385 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalCategoryPurpose1Code | 391 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalClearingSystemIdentification1Code | 397 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalCreditorReferenceType1Code | 403 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalDateType1Code | 409 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalDocumentAmountType1Code | 415 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalDocumentLineType1Code | 421 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalDocumentType1Code | 427 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalFinancialInstitutionIdentification1Code | 433 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalGarnishmentType1Code | 439 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalLocalInstrument1Code | 445 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalMandateSetupReason1Code | 451 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalOrganisationIdentification1Code | 457 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalPersonIdentification1Code | 463 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalProxyAccountType1Code | 469 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalPurpose1Code | 475 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalReversalReason1Code | 481 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ExternalServiceLevel1Code | 487 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}FinancialIdentificationSchemeName1Choice | 493 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}FinancialInstitutionIdentification23 | 499 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Frequency36Choice | 509 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Frequency6Code | 516 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}FrequencyAndMoment1 | 529 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}FrequencyPeriod1 | 535 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Garnishment4 | 541 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}GarnishmentType1 | 553 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}GarnishmentType1Choice | 559 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}GenericAccountIdentification1 | 565 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}GenericFinancialIdentification1 | 572 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}GenericIdentification30 | 579 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}GenericOrganisationIdentification3 | 586 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}GenericPersonIdentification2 | 593 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}GroupHeader124 | 600 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}IBAN2007Identifier | 614 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ISODate | 619 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ISODateTime | 622 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ISOYear | 625 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}LEIIdentifier | 628 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}LocalInstrument2Choice | 633 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}MandateClassification1Choice | 639 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}MandateClassification1Code | 645 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}MandateRelatedData5Choice | 652 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}MandateRelatedInformation16 | 658 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}MandateSetupReason1Choice | 672 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}MandateTypeInformation2 | 678 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max1025Text | 686 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max105Text | 692 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max10KBinary | 698 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max128Text | 704 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max140Text | 710 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max15NumericText | 716 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max16Text | 721 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max2048Text | 727 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max256Text | 733 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max34Text | 739 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max350Text | 745 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max35Text | 751 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max4Text | 757 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Max70Text | 763 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}NamePrefix2Code | 769 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Number | 778 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}OrganisationIdentification39 | 784 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}OrganisationIdentificationSchemeName1Choice | 791 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}OriginalGroupHeader20 | 797 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}OriginalPaymentInstruction53 | 805 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}OriginalTransactionReference47 | 817 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}OtherContact1 | 843 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Party50Choice | 849 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Party52Choice | 855 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PartyIdentification272 | 861 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PaymentMethod4Code | 870 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PaymentReversalReason10 | 878 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PaymentTransaction174 | 885 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PaymentTypeInformation27 | 899 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PercentageRate | 909 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PersonIdentification18 | 915 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PersonIdentificationSchemeName1Choice | 921 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PhoneNumber | 927 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PostalAddress27 | 932 |
| [type-0137](types/type-0137.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}PreferredContactMethod2Code | 954 |
| [type-0138](types/type-0138.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Priority2Code | 964 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ProxyAccountIdentification1 | 970 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ProxyAccountType1Choice | 976 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}Purpose2Choice | 982 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ReferredDocumentInformation8 | 988 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}RemittanceAmount4 | 996 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}RemittanceInformation26 | 1002 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ReversalReason4Choice | 1008 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}SecuritiesAttributes1 | 1014 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}SequenceType3Code | 1020 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}ServiceLevel8Choice | 1029 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}SettlementInstruction15 | 1035 |
| [type-0150](types/type-0150.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}SettlementMethod1Code | 1048 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}StructuredRemittanceInformation22 | 1056 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}SupplementaryData1 | 1069 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}SupplementaryDataEnvelope1 | 1075 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TaxAmount3 | 1080 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TaxAuthorisation1 | 1088 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TaxData1 | 1094 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TaxParty1 | 1109 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TaxParty2 | 1116 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TaxPeriod3 | 1124 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TaxRecord3 | 1131 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TaxRecordDetails3 | 1144 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TaxRecordPeriod1Code | 1150 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}TrueFalseIndicator | 1172 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}UTIIdentifier | 1175 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pain.007.001.13}UUIDv4Identifier | 1180 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 30 |
| complexType | 94 |
| element | 356 |
| enumeration | 76 |
| extension | 2 |
| fractionDigits | 5 |
| maxLength | 33 |
| minInclusive | 2 |
| minLength | 33 |
| pattern | 13 |
| restriction | 70 |
| schema | 1 |
| sequence | 62 |
| simpleContent | 2 |
| simpleType | 70 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/9af0c55a08ef8ef6e69a2fb9.md) · [Message](index.md)
