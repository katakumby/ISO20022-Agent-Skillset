---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.003.001.08"
message_family: "camt.003"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.003.001.08"
source_ids: ["src-000017"]
source_editions: ["2024-2025"]
---

# camt.003.001.08 structure

[src-000017](../../../../../raw-input/cash_management/camt.003.001.08.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.003.001.08`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.003.001.08 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}AccountCriteria4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}AccountCriteria8 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}AccountIdentification4Choice | 18 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}AccountIdentificationSearchCriteria2Choice | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}AccountQuery4 | 31 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}AccountSchemeName1Choice | 37 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ActiveOrHistoricCurrencyCode | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}AddressType2Code | 48 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}AddressType3Choice | 58 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}AnyBICDec2014Identifier | 64 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}BICFIDec2014Identifier | 69 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}BalanceCounterparty1Code | 74 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}BalanceType11Choice | 80 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}BranchAndFinancialInstitutionIdentification8 | 86 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}BranchData5 | 92 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}CashAccountReturnCriteria5 | 100 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}CashAccountSearchCriteria8 | 114 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}CashAccountType2Choice | 124 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}CashBalance14 | 130 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}CashBalanceReturnCriteria2 | 139 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ClearingSystemIdentification2Choice | 148 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ClearingSystemMemberIdentification2 | 154 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Contact13 | 160 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}CountryCode | 177 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}DateAndDateTimeSearch4Choice | 182 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}DateAndPlaceOfBirth1 | 188 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}DatePeriod2 | 196 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}DatePeriodSearch1Choice | 202 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}DateTimePeriod1 | 211 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}DateTimeSearch2Choice | 217 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Document | 226 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Exact4AlphaNumericText | 231 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ExternalAccountIdentification1Code | 236 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ExternalCashAccountType1Code | 242 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ExternalClearingSystemIdentification1Code | 248 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ExternalEnquiryRequestType1Code | 254 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ExternalFinancialInstitutionIdentification1Code | 260 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ExternalOrganisationIdentification1Code | 266 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ExternalPaymentControlRequestType1Code | 272 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ExternalPersonIdentification1Code | 278 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ExternalSystemBalanceType1Code | 284 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}FinancialIdentificationSchemeName1Choice | 290 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}FinancialInstitutionIdentification23 | 296 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}GenericAccountIdentification1 | 306 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}GenericFinancialIdentification1 | 313 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}GenericIdentification1 | 320 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}GenericIdentification30 | 327 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}GenericOrganisationIdentification3 | 334 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}GenericPersonIdentification2 | 341 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}GetAccountV08 | 348 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}IBAN2007Identifier | 355 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ISODate | 360 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}ISODateTime | 363 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}LEIIdentifier | 366 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max128Text | 371 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max140Text | 377 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max16Text | 383 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max2048Text | 389 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max256Text | 395 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max34Text | 401 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max350Text | 407 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max35Text | 413 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max4Text | 419 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Max70Text | 425 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}MessageHeader9 | 431 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}NamePrefix2Code | 438 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}OrganisationIdentification39 | 447 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}OrganisationIdentificationSchemeName1Choice | 454 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}OtherContact1 | 460 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}Party52Choice | 466 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}PartyIdentification272 | 472 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}PersonIdentification18 | 481 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}PersonIdentificationSchemeName1Choice | 487 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}PhoneNumber | 493 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}PostalAddress27 | 498 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}PreferredContactMethod2Code | 520 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}QueryType2Code | 530 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}RequestType4Choice | 538 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}RequestedIndicator | 545 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}SupplementaryData1 | 548 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.003.001.08}SupplementaryDataEnvelope1 | 554 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 16 |
| complexType | 46 |
| element | 164 |
| enumeration | 23 |
| maxLength | 19 |
| minLength | 19 |
| pattern | 8 |
| restriction | 35 |
| schema | 1 |
| sequence | 30 |
| simpleType | 35 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
