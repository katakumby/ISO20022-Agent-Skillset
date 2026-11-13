---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.003.001.12"
message_family: "pacs.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12"
source_ids: ["src-000166"]
source_editions: ["2025-2026"]
---

# pacs.003.001.12 structure

[src-000166](../../../../../raw-input/payments_clearing_and_settlement/pacs.003.001.12.xsd); `urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}AddressType3Choice | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}AmendmentInformationDetails15 | 71 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}AnyBICDec2014Identifier | 87 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Authorisation1Choice | 92 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Authorisation1Code | 98 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}BICFIDec2014Identifier | 106 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}BaseOneRate | 111 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}BatchBookingIndicator | 117 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}BranchAndFinancialInstitutionIdentification8 | 120 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}BranchData5 | 126 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}CashAccount40 | 134 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}CashAccountType2Choice | 143 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}CategoryPurpose1Choice | 149 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ChargeBearerType1Code | 155 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ChargeType3Choice | 163 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Charges16 | 169 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ClearingChannel2Code | 176 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ClearingSystemIdentification2Choice | 184 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ClearingSystemIdentification3Choice | 190 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ClearingSystemMemberIdentification2 | 196 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Contact13 | 202 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}CountryCode | 219 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}CreditDebitCode | 224 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}CreditorReferenceInformation3 | 230 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}CreditorReferenceType2Choice | 236 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}CreditorReferenceType3 | 242 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DateAndPlaceOfBirth1 | 248 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DateAndType1 | 256 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DatePeriod2 | 262 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DateType2Choice | 268 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DecimalNumber | 274 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DirectDebitTransaction12 | 280 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DirectDebitTransactionInformation35 | 288 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Document | 328 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DocumentAdjustment1 | 333 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DocumentAmount1 | 341 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DocumentAmountType1Choice | 347 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DocumentLineIdentification1 | 353 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DocumentLineInformation2 | 360 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DocumentLineType1 | 367 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DocumentLineType1Choice | 373 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DocumentType1 | 379 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}DocumentType2Choice | 385 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Exact2NumericText | 391 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Exact4AlphaNumericText | 396 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalAccountIdentification1Code | 401 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalCashAccountType1Code | 407 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalCashClearingSystem1Code | 413 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalCategoryPurpose1Code | 419 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalChargeType1Code | 425 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalClearingSystemIdentification1Code | 431 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalCreditorReferenceType1Code | 437 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalDateType1Code | 443 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalDocumentAmountType1Code | 449 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalDocumentLineType1Code | 455 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalDocumentType1Code | 461 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalFinancialInstitutionIdentification1Code | 467 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalGarnishmentType1Code | 473 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalLocalInstrument1Code | 479 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalMandateSetupReason1Code | 485 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalOrganisationIdentification1Code | 491 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalPersonIdentification1Code | 497 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalProxyAccountType1Code | 503 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalPurpose1Code | 509 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalRegulatoryReportingType1Code | 515 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ExternalServiceLevel1Code | 521 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}FIToFICustomerDirectDebitV12 | 527 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}FinancialIdentificationSchemeName1Choice | 534 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}FinancialInstitutionIdentification23 | 540 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Frequency36Choice | 550 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Frequency6Code | 557 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}FrequencyAndMoment1 | 570 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}FrequencyPeriod1 | 576 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Garnishment4 | 582 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}GarnishmentType1 | 594 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}GarnishmentType1Choice | 600 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}GenericAccountIdentification1 | 606 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}GenericFinancialIdentification1 | 613 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}GenericIdentification3 | 620 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}GenericIdentification30 | 626 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}GenericOrganisationIdentification3 | 633 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}GenericPersonIdentification2 | 640 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}GroupHeader125 | 647 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}IBAN2007Identifier | 663 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ISODate | 668 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ISODateTime | 671 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ISOYear | 674 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}LEIIdentifier | 677 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}LocalInstrument2Choice | 682 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}MandateRelatedInformation16 | 688 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}MandateSetupReason1Choice | 702 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max1025Text | 708 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max10Text | 714 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max128Text | 720 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max140Text | 726 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max15NumericText | 732 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max16Text | 737 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max2048Text | 743 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max256Text | 749 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max34Text | 755 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max350Text | 761 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max35Text | 767 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max4Text | 773 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Max70Text | 779 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}NameAndAddress18 | 785 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}NamePrefix2Code | 791 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Number | 800 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}OrganisationIdentification39 | 806 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}OrganisationIdentificationSchemeName1Choice | 813 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}OtherContact1 | 819 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Party52Choice | 825 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}PartyIdentification272 | 831 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}PaymentIdentification13 | 840 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}PaymentTypeInformation27 | 849 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}PercentageRate | 859 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}PersonIdentification18 | 865 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}PersonIdentificationSchemeName1Choice | 871 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}PhoneNumber | 877 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}PostalAddress27 | 882 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}PreferredContactMethod2Code | 904 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Priority2Code | 914 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Priority3Code | 920 |
| [type-0133](types/type-0133.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ProxyAccountIdentification1 | 927 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ProxyAccountType1Choice | 933 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}Purpose2Choice | 939 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ReferredDocumentInformation8 | 945 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}RegulatoryAuthority2 | 953 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}RegulatoryReporting10 | 959 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}RegulatoryReportingType1Choice | 966 |
| [type-0140](types/type-0140.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}RegulatoryReportingType1Code | 972 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}RemittanceAmount4 | 979 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}RemittanceInformation26 | 985 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}RemittanceLocation8 | 991 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}RemittanceLocationData2 | 997 |
| [type-0145](types/type-0145.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}RemittanceLocationMethod2Code | 1004 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}SecuritiesAttributes1 | 1014 |
| [type-0147](types/type-0147.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}SequenceType3Code | 1020 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}ServiceLevel8Choice | 1029 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}SettlementDateTimeIndication1 | 1035 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}SettlementInstruction14 | 1041 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}SettlementMethod2Code | 1048 |
| [type-0152](types/type-0152.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}StructuredRegulatoryReporting5 | 1055 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}StructuredRemittanceInformation22 | 1065 |
| [type-0154](types/type-0154.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}SupplementaryData1 | 1078 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}SupplementaryDataEnvelope1 | 1084 |
| [type-0156](types/type-0156.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TaxAmount3 | 1089 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TaxAuthorisation1 | 1097 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TaxData1 | 1103 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TaxParty1 | 1118 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TaxParty2 | 1125 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TaxPeriod3 | 1133 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TaxRecord3 | 1140 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TaxRecordDetails3 | 1153 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TaxRecordPeriod1Code | 1159 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}TrueFalseIndicator | 1181 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}UTIIdentifier | 1184 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12}UUIDv4Identifier | 1189 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 26 |
| complexType | 94 |
| element | 351 |
| enumeration | 80 |
| extension | 2 |
| fractionDigits | 6 |
| maxLength | 33 |
| minInclusive | 2 |
| minLength | 33 |
| pattern | 13 |
| restriction | 72 |
| schema | 1 |
| sequence | 66 |
| simpleContent | 2 |
| simpleType | 72 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/a3b7673bd71997151a80ef1f.md) · [Message](index.md)
