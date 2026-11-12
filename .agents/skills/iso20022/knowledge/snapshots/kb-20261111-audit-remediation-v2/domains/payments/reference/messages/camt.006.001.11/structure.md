---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.006.001.11"
message_family: "camt.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.006.001.11"
source_ids: ["src-000020"]
source_editions: ["2024-2025"]
---

# camt.006.001.11 structure

[src-000020](../../../../../raw-input/cash_management/camt.006.001.11.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.006.001.11`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.006.001.11 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ActiveOrHistoricCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ActiveOrHistoricCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}AddressType3Choice | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Amount2Choice | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Amount3Choice | 77 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}AnyBICDec2014Identifier | 83 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}BICFIDec2014Identifier | 88 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}BranchAndFinancialInstitutionIdentification8 | 93 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}BranchData5 | 99 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}CancelledStatusReason1Code | 107 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}CashAccount43 | 114 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}CashAccountAndEntry5 | 125 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}CashAccountType2Choice | 131 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}CashEntry2 | 137 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ClearingSystemIdentification2Choice | 148 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ClearingSystemMemberIdentification2 | 154 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Contact13 | 160 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}CountryCode | 177 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}CreditDebitCode | 182 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}DateAndDateTime2Choice | 188 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}DateAndPlaceOfBirth1 | 194 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}DateTimePeriod1 | 202 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}DateTimePeriod1Choice | 208 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}DecimalNumber | 215 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Document | 221 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}EntryStatus1Code | 226 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}EntryTypeIdentifier | 233 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ErrorHandling3Choice | 238 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ErrorHandling5 | 244 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Exact4AlphaNumericText | 250 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalAccountIdentification1Code | 255 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalCashAccountType1Code | 261 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalClearingSystemIdentification1Code | 267 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalEnquiryRequestType1Code | 273 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalFinancialInstitutionIdentification1Code | 279 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalMarketInfrastructure1Code | 285 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalOrganisationIdentification1Code | 291 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalPaymentControlRequestType1Code | 297 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalPersonIdentification1Code | 303 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalProxyAccountType1Code | 309 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ExternalSystemErrorHandling1Code | 315 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}FinalStatus1Code | 321 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}FinancialIdentificationSchemeName1Choice | 329 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}FinancialInstitutionIdentification23 | 335 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}GenericAccountIdentification1 | 345 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}GenericFinancialIdentification1 | 352 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}GenericIdentification1 | 359 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}GenericIdentification30 | 366 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}GenericOrganisationIdentification3 | 373 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}GenericPersonIdentification2 | 380 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}IBAN2007Identifier | 387 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ISODate | 392 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ISODateTime | 395 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ImpliedCurrencyAndAmount | 398 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}LEIIdentifier | 405 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}LongPaymentIdentification4 | 410 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}MarketInfrastructureIdentification1Choice | 423 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max10Text | 429 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max128Text | 435 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max140Text | 441 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max15NumericText | 447 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max16Text | 452 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max20000Text | 458 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max2048Text | 464 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max256Text | 470 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max34Text | 476 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max350Text | 482 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max35Text | 488 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max3NumericText | 494 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max4AlphaNumericText | 499 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max4Text | 506 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max5NumericText | 512 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Max70Text | 517 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}MessageHeader8 | 523 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}NamePrefix2Code | 533 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Number | 542 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}NumberAndSumOfTransactions2 | 548 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}OrganisationIdentification39 | 556 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}OrganisationIdentificationSchemeName1Choice | 563 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}OriginalBusinessQuery1 | 569 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}OtherContact1 | 576 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Pagination1 | 582 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Party50Choice | 588 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Party52Choice | 594 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PartyIdentification272 | 600 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentCommon6 | 609 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentIdentification8Choice | 620 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentInstruction47 | 630 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentInstrument1Code | 650 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentOrigin1Choice | 664 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentStatus6 | 672 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentStatusCode6Choice | 679 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentStatusReason1Choice | 688 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentTransactionParty4 | 699 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentType3Code | 716 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PaymentType4Choice | 744 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PendingFailingSettlement1Code | 750 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PendingSettlement2Code | 799 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PendingStatus4Code | 842 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PersonIdentification18 | 863 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PersonIdentificationSchemeName1Choice | 869 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PhoneNumber | 875 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PostalAddress27 | 880 |
| [type-0112](types/type-0112.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}PreferredContactMethod2Code | 902 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Priority1Choice | 912 |
| [type-0114](types/type-0114.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Priority5Code | 918 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ProprietaryStatusJustification2 | 926 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ProxyAccountIdentification1 | 932 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ProxyAccountType1Choice | 938 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}QueueTransactionIdentification1 | 944 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}RequestType4Choice | 950 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ReturnTransactionV11 | 957 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}SecuritiesTransactionReferences1 | 964 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}ShortPaymentIdentification4 | 972 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}SupplementaryData1 | 980 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}SupplementaryDataEnvelope1 | 986 |
| [type-0125](types/type-0125.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}SuspendedStatusReason1Code | 991 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}System3 | 997 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Transaction159 | 1005 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}TransactionOrError6Choice | 1015 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}TransactionReport8 | 1021 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}TransactionReportOrError7Choice | 1027 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}Transactions11 | 1033 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}TrueFalseIndicator | 1040 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}UUIDv4Identifier | 1043 |
| [type-0134](types/type-0134.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}UnmatchedStatusReason1Code | 1048 |
| [type-0135](types/type-0135.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.006.001.11}YesNoIndicator | 1089 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 26 |
| complexType | 72 |
| element | 266 |
| enumeration | 207 |
| extension | 2 |
| fractionDigits | 5 |
| maxLength | 24 |
| minInclusive | 3 |
| minLength | 24 |
| pattern | 15 |
| restriction | 62 |
| schema | 1 |
| sequence | 44 |
| simpleContent | 2 |
| simpleType | 62 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
