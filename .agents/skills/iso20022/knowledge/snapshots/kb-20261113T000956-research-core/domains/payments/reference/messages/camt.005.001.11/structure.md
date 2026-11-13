---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.005.001.11"
message_family: "camt.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.005.001.11"
source_ids: ["src-000019"]
source_editions: ["2024-2025"]
---

# camt.005.001.11 structure

[src-000019](../../../../../raw-input/cash_management/camt.005.001.11.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.005.001.11`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.005.001.11 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}AccountCashEntryReturnCriteria3 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}AccountIdentification4Choice | 17 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}AccountIdentificationSearchCriteria2Choice | 23 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}AccountSchemeName1Choice | 30 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ActiveAmountRange3Choice | 36 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ActiveCurrencyAndAmountRange3 | 42 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ActiveCurrencyCode | 49 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ActiveOrHistoricAmountRange2Choice | 54 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ActiveOrHistoricCurrencyAndAmountRange2 | 60 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ActiveOrHistoricCurrencyCode | 67 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}AddressType2Code | 72 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}AddressType3Choice | 82 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}AmountRangeBoundary1 | 88 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}AnyBICDec2014Identifier | 94 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}BICFIDec2014Identifier | 99 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}BranchAndFinancialInstitutionIdentification8 | 104 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}BranchData5 | 110 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}CashAccountEntrySearch8 | 118 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}CashPaymentStatus2Code | 130 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ClearingSystemIdentification2Choice | 136 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ClearingSystemIdentification3Choice | 142 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ClearingSystemMemberIdentification2 | 148 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Contact13 | 154 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}CountryCode | 171 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}CreditDebitCode | 176 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}DateAndDateTimeSearch3Choice | 182 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}DateAndPlaceOfBirth1 | 188 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}DatePeriod2 | 196 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}DatePeriodSearch1Choice | 202 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}DateTimePeriod1 | 211 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}DateTimePeriod1Choice | 217 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Document | 224 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}EntryStatus1Code | 229 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}EntryTypeIdentifier | 236 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Exact4AlphaNumericText | 241 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ExternalAccountIdentification1Code | 246 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ExternalCashClearingSystem1Code | 252 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ExternalClearingSystemIdentification1Code | 258 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ExternalEnquiryRequestType1Code | 264 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ExternalFinancialInstitutionIdentification1Code | 270 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ExternalOrganisationIdentification1Code | 276 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ExternalPaymentControlRequestType1Code | 282 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ExternalPersonIdentification1Code | 288 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}FinalStatusCode | 294 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}FinancialIdentificationSchemeName1Choice | 302 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}FinancialInstitutionIdentification23 | 308 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}FromToAmountRange1 | 318 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}GenericAccountIdentification1 | 324 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}GenericFinancialIdentification1 | 331 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}GenericIdentification1 | 338 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}GenericIdentification30 | 345 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}GenericOrganisationIdentification3 | 352 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}GenericPersonIdentification2 | 359 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}GetTransactionV11 | 366 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}IBAN2007Identifier | 373 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ISODate | 378 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ISODateTime | 381 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ImpliedCurrencyAmountRange1Choice | 384 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ImpliedCurrencyAndAmount | 393 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ImpliedCurrencyAndAmountRange1 | 400 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Instruction1Code | 406 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}InstructionStatusReturnCriteria1 | 413 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}InstructionStatusSearch5 | 420 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}LEIIdentifier | 427 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}LongPaymentIdentification4 | 432 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max128Text | 445 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max140Text | 451 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max16Text | 457 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max2048Text | 463 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max256Text | 469 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max34Text | 475 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max350Text | 481 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max35Text | 487 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max3NumericText | 493 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max4AlphaNumericText | 498 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max4Text | 505 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Max70Text | 511 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}MessageHeader9 | 517 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}NamePrefix2Code | 524 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}OrganisationIdentification39 | 533 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}OrganisationIdentificationSchemeName1Choice | 540 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}OtherContact1 | 546 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Party50Choice | 552 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Party52Choice | 558 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PartyIdentification272 | 564 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PaymentIdentification8Choice | 573 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PaymentInstrument1Code | 583 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PaymentOrigin1Choice | 597 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PaymentReturnCriteria4 | 605 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PaymentSearch10 | 633 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PaymentStatusCodeSearch2Choice | 656 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PaymentTransactionParty4 | 663 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PaymentType3Code | 680 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PaymentType4Choice | 708 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PendingStatus4Code | 714 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PersonIdentification18 | 735 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PersonIdentificationSchemeName1Choice | 741 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PhoneNumber | 747 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PostalAddress27 | 752 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}PreferredContactMethod2Code | 774 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Priority1Choice | 784 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}Priority5Code | 790 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}QueryType2Code | 798 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}QueueTransactionIdentification1 | 806 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ReportIndicator1Code | 812 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}RequestType4Choice | 818 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}RequestedIndicator | 825 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}ShortPaymentIdentification4 | 828 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}SupplementaryData1 | 836 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}SupplementaryDataEnvelope1 | 842 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}SystemReturnCriteria2 | 847 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}SystemSearch5 | 855 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}TransactionCriteria11 | 863 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}TransactionCriteria8Choice | 871 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}TransactionQuery8 | 877 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}TransactionReturnCriteria5 | 883 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}TransactionSearchCriteria11 | 891 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}UUIDv4Identifier | 899 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.005.001.11}YesNoIndicator | 904 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 24 |
| complexType | 69 |
| element | 284 |
| enumeration | 92 |
| fractionDigits | 1 |
| maxLength | 19 |
| minInclusive | 1 |
| minLength | 19 |
| pattern | 13 |
| restriction | 50 |
| schema | 1 |
| sequence | 45 |
| simpleType | 50 |
| totalDigits | 1 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/5690f991aa6cec4573690ad2.md) · [Message](index.md)
