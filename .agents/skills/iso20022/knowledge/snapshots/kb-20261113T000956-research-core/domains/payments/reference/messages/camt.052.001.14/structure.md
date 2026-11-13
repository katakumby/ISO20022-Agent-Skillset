---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.052.001.14"
message_family: "camt.052"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.052.001.14"
source_ids: ["src-000007"]
source_editions: ["2025-2026"]
---

# camt.052.001.14 structure

[src-000007](../../../../../raw-input/banktocustomer_cash_management/camt.052.001.14_0.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.052.001.14`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.052.001.14 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AccountInterest4 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AccountReport38 | 20 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AccountSchemeName1Choice | 40 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ActiveCurrencyAndAmount_SimpleType | 46 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ActiveCurrencyAndAmount | 53 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ActiveCurrencyCode | 60 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 65 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ActiveOrHistoricCurrencyAnd13DecimalAmount | 72 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ActiveOrHistoricCurrencyAndAmount_SimpleType | 79 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ActiveOrHistoricCurrencyAndAmount | 86 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ActiveOrHistoricCurrencyAndAmountRange2 | 93 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ActiveOrHistoricCurrencyCode | 100 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AddressType2Code | 105 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AddressType3Choice | 115 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AmountAndCurrencyExchange4 | 121 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AmountAndCurrencyExchangeDetails5 | 130 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AmountAndCurrencyExchangeDetails6 | 136 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AmountAndDirection35 | 143 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AmountRangeBoundary1 | 149 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AnyBICDec2014Identifier | 155 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AttendanceContext1Code | 160 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AuthenticationEntity1Code | 167 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}AuthenticationMethod1Code | 174 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BICFIDec2014Identifier | 189 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BalanceSubType1Choice | 194 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BalanceType10Choice | 200 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BalanceType13 | 206 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BankToCustomerAccountReportV14 | 212 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BankTransactionCodeStructure4 | 219 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BankTransactionCodeStructure5 | 225 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BankTransactionCodeStructure6 | 231 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BaseOneRate | 237 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BatchInformation2 | 243 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BranchAndFinancialInstitutionIdentification8 | 252 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}BranchData5 | 258 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CSCManagement1Code | 266 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardAggregated2 | 274 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardDataReading1Code | 283 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardEntry5 | 295 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardIndividualTransaction2 | 303 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardPaymentServiceType2Code | 319 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardSecurityInformation1 | 334 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardSequenceNumberRange1 | 340 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardTransaction18 | 346 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardTransaction3Choice | 354 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardholderAuthentication2 | 360 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CardholderVerificationCapability1Code | 366 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CashAccount40 | 382 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CashAccount43 | 391 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CashAccountType2Choice | 402 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CashAvailability1 | 408 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CashAvailabilityDate1Choice | 415 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CashBalance8 | 421 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CashDeposit1 | 431 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CategoryPurpose1Choice | 438 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ChargeBearerType1Code | 444 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ChargeIncludedIndicator | 452 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ChargeType3Choice | 455 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Charges15 | 461 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ChargesRecord8 | 467 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ClearingChannel2Code | 479 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ClearingSystemIdentification2Choice | 487 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ClearingSystemMemberIdentification2 | 493 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Contact13 | 499 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CopyDuplicate1Code | 516 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CorporateAction82 | 523 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CorporateActionEventType104Choice | 530 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CountryCode | 536 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CreditDebitCode | 541 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CreditLine3 | 547 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CreditLineType1Choice | 555 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CreditorReferenceInformation3 | 561 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CreditorReferenceType2Choice | 567 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CreditorReferenceType3 | 573 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}CurrencyExchange24 | 579 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DateAndDateTime2Choice | 590 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DateAndPlaceOfBirth1 | 596 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DateAndType1 | 604 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DateOrDateTimePeriod1Choice | 610 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DatePeriod2 | 616 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DateTimePeriod1 | 622 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DateType2Choice | 628 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DecimalNumber | 634 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DisplayCapabilities1 | 640 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Document | 647 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DocumentAdjustment1 | 652 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DocumentAmount1 | 660 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DocumentAmountType1Choice | 666 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DocumentLineIdentification1 | 672 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DocumentLineInformation2 | 679 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DocumentLineType1 | 686 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DocumentLineType1Choice | 692 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DocumentType1 | 698 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}DocumentType2Choice | 704 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}EntryDetails16 | 710 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}EntryStatus1Choice | 716 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}EntryTransaction16 | 722 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Exact1NumericText | 755 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Exact3NumericText | 760 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Exact4AlphaNumericText | 765 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalAccountIdentification1Code | 770 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalBalanceSubType1Code | 776 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalBalanceType1Code | 782 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalBankTransactionDomain1Code | 788 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalBankTransactionFamily1Code | 794 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalBankTransactionSubFamily1Code | 800 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalCardTransactionCategory1Code | 806 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalCashAccountType1Code | 812 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalCategoryPurpose1Code | 818 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalChargeType1Code | 824 |
| [type-0113](types/type-0113.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalClearingSystemIdentification1Code | 830 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalCorporateActionEventType1Code | 836 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalCreditLineType1Code | 842 |
| [type-0116](types/type-0116.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalCreditorReferenceType1Code | 848 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalDateType1Code | 854 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalDocumentAmountType1Code | 860 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalDocumentLineType1Code | 866 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalDocumentType1Code | 872 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalEntryStatus1Code | 878 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalFinancialInstitutionIdentification1Code | 884 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalFinancialInstrumentIdentificationType1Code | 890 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalGarnishmentType1Code | 896 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalLocalInstrument1Code | 902 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalOrganisationIdentification1Code | 908 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalPersonIdentification1Code | 914 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalProxyAccountType1Code | 920 |
| [type-0129](types/type-0129.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalPurpose1Code | 926 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalRePresentmentReason1Code | 932 |
| [type-0131](types/type-0131.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalReportingSource1Code | 938 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalReturnReason1Code | 944 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalServiceLevel1Code | 950 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ExternalTechnicalInputChannel1Code | 956 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}FinancialIdentificationSchemeName1Choice | 962 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}FinancialInstitutionIdentification23 | 968 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}FinancialInstrumentQuantity33Choice | 978 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}FromToAmountRange1 | 986 |
| [type-0139](types/type-0139.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Garnishment4 | 992 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GarnishmentType1 | 1004 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GarnishmentType1Choice | 1010 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GenericAccountIdentification1 | 1016 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GenericFinancialIdentification1 | 1023 |
| [type-0144](types/type-0144.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GenericIdentification1 | 1030 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GenericIdentification3 | 1037 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GenericIdentification30 | 1043 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GenericIdentification32 | 1050 |
| [type-0148](types/type-0148.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GenericOrganisationIdentification3 | 1058 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GenericPersonIdentification2 | 1065 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}GroupHeader116 | 1072 |
| [type-0151](types/type-0151.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}IBAN2007Identifier | 1082 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ISINOct2015Identifier | 1087 |
| [type-0153](types/type-0153.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ISO2ALanguageCode | 1092 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ISODate | 1097 |
| [type-0155](types/type-0155.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ISODateTime | 1100 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ISOYear | 1103 |
| [type-0157](types/type-0157.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ISOYearMonth | 1106 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}IdentificationSource3Choice | 1109 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ImpliedCurrencyAmountRange1Choice | 1115 |
| [type-0160](types/type-0160.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ImpliedCurrencyAndAmount | 1124 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}InterestRecord2 | 1131 |
| [type-0162](types/type-0162.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}InterestType1Choice | 1142 |
| [type-0163](types/type-0163.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}InterestType1Code | 1148 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}LEIIdentifier | 1154 |
| [type-0165](types/type-0165.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}LocalInstrument2Choice | 1159 |
| [type-0166](types/type-0166.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max1025Text | 1165 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max105Text | 1171 |
| [type-0168](types/type-0168.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max128Text | 1177 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max140Text | 1183 |
| [type-0170](types/type-0170.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max15NumericText | 1189 |
| [type-0171](types/type-0171.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max15PlusSignedNumericText | 1194 |
| [type-0172](types/type-0172.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max16Text | 1199 |
| [type-0173](types/type-0173.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max20000Text | 1205 |
| [type-0174](types/type-0174.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max2048Text | 1211 |
| [type-0175](types/type-0175.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max256Text | 1217 |
| [type-0176](types/type-0176.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max30DecimalNumber | 1223 |
| [type-0177](types/type-0177.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max34Text | 1229 |
| [type-0178](types/type-0178.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max350Text | 1235 |
| [type-0179](types/type-0179.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max35Text | 1241 |
| [type-0180](types/type-0180.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max3NumericText | 1247 |
| [type-0181](types/type-0181.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max4Text | 1252 |
| [type-0182](types/type-0182.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max500Text | 1258 |
| [type-0183](types/type-0183.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max5NumericText | 1264 |
| [type-0184](types/type-0184.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Max70Text | 1269 |
| [type-0185](types/type-0185.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}MessageIdentification2 | 1275 |
| [type-0186](types/type-0186.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Min2Max3NumericText | 1281 |
| [type-0187](types/type-0187.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Min3Max4NumericText | 1286 |
| [type-0188](types/type-0188.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Min8Max28NumericText | 1291 |
| [type-0189](types/type-0189.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}NameAndAddress18 | 1296 |
| [type-0190](types/type-0190.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}NamePrefix2Code | 1302 |
| [type-0191](types/type-0191.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}NonNegativeDecimalNumber | 1311 |
| [type-0192](types/type-0192.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Number | 1318 |
| [type-0193](types/type-0193.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}NumberAndSumOfTransactions1 | 1324 |
| [type-0194](types/type-0194.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}NumberAndSumOfTransactions4 | 1330 |
| [type-0195](types/type-0195.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}OnLineCapability1Code | 1337 |
| [type-0196](types/type-0196.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}OrganisationIdentification39 | 1344 |
| [type-0197](types/type-0197.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}OrganisationIdentificationSchemeName1Choice | 1351 |
| [type-0198](types/type-0198.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}OriginalAndCurrentQuantities1 | 1357 |
| [type-0199](types/type-0199.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}OriginalBusinessQuery1 | 1363 |
| [type-0200](types/type-0200.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}OtherContact1 | 1370 |
| [type-0201](types/type-0201.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}OtherIdentification1 | 1376 |
| [type-0202](types/type-0202.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}POIComponentType1Code | 1383 |
| [type-0203](types/type-0203.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Pagination1 | 1394 |
| [type-0204](types/type-0204.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Party50Choice | 1400 |
| [type-0205](types/type-0205.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Party52Choice | 1406 |
| [type-0206](types/type-0206.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PartyIdentification272 | 1412 |
| [type-0207](types/type-0207.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PartyType3Code | 1421 |
| [type-0208](types/type-0208.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PartyType4Code | 1432 |
| [type-0209](types/type-0209.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PaymentCard4 | 1442 |
| [type-0210](types/type-0210.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PaymentContext3 | 1450 |
| [type-0211](types/type-0211.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PaymentReturnReason8 | 1465 |
| [type-0212](types/type-0212.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PaymentTypeInformation27 | 1473 |
| [type-0213](types/type-0213.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PercentageRate | 1483 |
| [type-0214](types/type-0214.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PersonIdentification18 | 1489 |
| [type-0215](types/type-0215.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PersonIdentificationSchemeName1Choice | 1495 |
| [type-0216](types/type-0216.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PhoneNumber | 1501 |
| [type-0217](types/type-0217.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PlainCardData1 | 1506 |
| [type-0218](types/type-0218.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PointOfInteraction1 | 1517 |
| [type-0219](types/type-0219.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PointOfInteractionCapabilities1 | 1526 |
| [type-0220](types/type-0220.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PointOfInteractionComponent1 | 1535 |
| [type-0221](types/type-0221.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PositiveNumber | 1545 |
| [type-0222](types/type-0222.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PostalAddress27 | 1552 |
| [type-0223](types/type-0223.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PreferredContactMethod2Code | 1574 |
| [type-0224](types/type-0224.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Price7 | 1584 |
| [type-0225](types/type-0225.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PriceRateOrAmount3Choice | 1590 |
| [type-0226](types/type-0226.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}PriceValueType1Code | 1596 |
| [type-0227](types/type-0227.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Priority2Code | 1603 |
| [type-0228](types/type-0228.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Product2 | 1609 |
| [type-0229](types/type-0229.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ProprietaryAgent5 | 1620 |
| [type-0230](types/type-0230.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ProprietaryBankTransactionCodeStructure1 | 1626 |
| [type-0231](types/type-0231.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ProprietaryDate3 | 1632 |
| [type-0232](types/type-0232.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ProprietaryParty6 | 1638 |
| [type-0233](types/type-0233.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ProprietaryPrice2 | 1644 |
| [type-0234](types/type-0234.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ProprietaryQuantity1 | 1650 |
| [type-0235](types/type-0235.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ProprietaryReference1 | 1656 |
| [type-0236](types/type-0236.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ProxyAccountIdentification1 | 1662 |
| [type-0237](types/type-0237.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ProxyAccountType1Choice | 1668 |
| [type-0238](types/type-0238.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Purpose2Choice | 1674 |
| [type-0239](types/type-0239.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}Rate4 | 1680 |
| [type-0240](types/type-0240.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}RateType4Choice | 1686 |
| [type-0241](types/type-0241.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}References80Choice | 1692 |
| [type-0242](types/type-0242.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ReferredDocumentInformation8 | 1707 |
| [type-0243](types/type-0243.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}RemittanceAmount4 | 1715 |
| [type-0244](types/type-0244.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}RemittanceInformation26 | 1721 |
| [type-0245](types/type-0245.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}RemittanceLocation8 | 1727 |
| [type-0246](types/type-0246.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}RemittanceLocationData2 | 1733 |
| [type-0247](types/type-0247.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}RemittanceLocationMethod2Code | 1740 |
| [type-0248](types/type-0248.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ReportEntry16 | 1750 |
| [type-0249](types/type-0249.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ReportingSource1Choice | 1773 |
| [type-0250](types/type-0250.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ReturnReason5Choice | 1779 |
| [type-0251](types/type-0251.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}SecuritiesAccount19 | 1785 |
| [type-0252](types/type-0252.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}SecuritiesAttributes1 | 1792 |
| [type-0253](types/type-0253.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}SecurityIdentification19 | 1798 |
| [type-0254](types/type-0254.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}SequenceRange1 | 1805 |
| [type-0255](types/type-0255.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}SequenceRange1Choice | 1811 |
| [type-0256](types/type-0256.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}SequenceType3Code | 1820 |
| [type-0257](types/type-0257.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}ServiceLevel8Choice | 1829 |
| [type-0258](types/type-0258.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}StructuredRemittanceInformation22 | 1835 |
| [type-0259](types/type-0259.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}SupplementaryData1 | 1848 |
| [type-0260](types/type-0260.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}SupplementaryDataEnvelope1 | 1854 |
| [type-0261](types/type-0261.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxAmount3 | 1859 |
| [type-0262](types/type-0262.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxAuthorisation1 | 1867 |
| [type-0263](types/type-0263.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxCharges2 | 1873 |
| [type-0264](types/type-0264.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxData1 | 1880 |
| [type-0265](types/type-0265.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxParty1 | 1895 |
| [type-0266](types/type-0266.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxParty2 | 1902 |
| [type-0267](types/type-0267.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxPeriod3 | 1910 |
| [type-0268](types/type-0268.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxRecord3 | 1917 |
| [type-0269](types/type-0269.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxRecordDetails3 | 1930 |
| [type-0270](types/type-0270.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TaxRecordPeriod1Code | 1936 |
| [type-0271](types/type-0271.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TechnicalInputChannel1Choice | 1958 |
| [type-0272](types/type-0272.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TotalTransactions6 | 1964 |
| [type-0273](types/type-0273.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TotalsPerBankTransactionCode5 | 1972 |
| [type-0274](types/type-0274.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TrackData1 | 1985 |
| [type-0275](types/type-0275.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionAgents6 | 1991 |
| [type-0276](types/type-0276.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionAllocation2 | 2007 |
| [type-0277](types/type-0277.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionChannel1Code | 2017 |
| [type-0278](types/type-0278.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionDates3 | 2025 |
| [type-0279](types/type-0279.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionEnvironment1Code | 2037 |
| [type-0280](types/type-0280.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionIdentifier1 | 2044 |
| [type-0281](types/type-0281.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionInterest4 | 2050 |
| [type-0282](types/type-0282.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionParties12 | 2056 |
| [type-0283](types/type-0283.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionPrice4Choice | 2069 |
| [type-0284](types/type-0284.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionQuantities4Choice | 2075 |
| [type-0285](types/type-0285.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TransactionReferences10 | 2082 |
| [type-0286](types/type-0286.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}TrueFalseIndicator | 2102 |
| [type-0287](types/type-0287.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}UTIIdentifier | 2105 |
| [type-0288](types/type-0288.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}UUIDv4Identifier | 2110 |
| [type-0289](types/type-0289.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}UnitOfMeasure1Code | 2115 |
| [type-0290](types/type-0290.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}UserInterface2Code | 2154 |
| [type-0291](types/type-0291.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}YesNoIndicator | 2160 |
| [type-0292](types/type-0292.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.052.001.14}YieldedOrValueType1Choice | 2163 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 45 |
| complexType | 177 |
| element | 671 |
| enumeration | 185 |
| extension | 3 |
| fractionDigits | 11 |
| maxLength | 46 |
| minInclusive | 6 |
| minLength | 46 |
| pattern | 22 |
| restriction | 114 |
| schema | 1 |
| sequence | 129 |
| simpleContent | 3 |
| simpleType | 114 |
| totalDigits | 11 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/ebbd552838cfe21849732051.md) · [Message](index.md)
