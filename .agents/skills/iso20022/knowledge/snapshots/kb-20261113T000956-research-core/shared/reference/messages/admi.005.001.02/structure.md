---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "shared"
message_id: "admi.005.001.02"
message_family: "admi.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:admi.005.001.02"
source_ids: ["src-000237"]
source_editions: ["march-2024"]
---

# admi.005.001.02 structure

[src-000237](../../../../raw-input/target2securities_t2s/admi.005.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:admi.005.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:admi.005.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}AccountIdentificationSearchCriteria2Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}AccountSchemeName1Choice | 18 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}AddressType2Code | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}AddressType3Choice | 34 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}AnyBICDec2014Identifier | 40 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}BICFIDec2014Identifier | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}BalanceCounterparty1Code | 50 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}BalanceType11Choice | 56 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}BranchAndFinancialInstitutionIdentification8 | 62 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}BranchData5 | 68 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}CashBalance14 | 76 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ClearingSystemIdentification2Choice | 85 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ClearingSystemMemberIdentification2 | 91 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}CountryCode | 97 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}DateAndDateTimeSearch4Choice | 102 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}DatePeriod2 | 108 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}DatePeriodSearch1Choice | 114 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}DateTimePeriod1 | 123 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}DateTimePeriod1Choice | 129 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}DateTimeSearch2Choice | 136 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Document | 145 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}EventType1Choice | 150 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Exact4AlphaNumericText | 156 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ExternalAccountIdentification1Code | 161 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ExternalClearingSystemIdentification1Code | 167 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ExternalEnquiryRequestType1Code | 173 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ExternalFinancialInstitutionIdentification1Code | 179 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ExternalPaymentControlRequestType1Code | 185 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ExternalSystemBalanceType1Code | 191 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ExternalSystemEventType1Code | 197 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}FinancialIdentificationSchemeName1Choice | 203 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}FinancialInstitutionIdentification23 | 209 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}GenericAccountIdentification1 | 219 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}GenericFinancialIdentification1 | 226 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}GenericIdentification1 | 233 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}GenericIdentification30 | 240 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}GenericIdentification36 | 247 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}IBAN2007Identifier | 254 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ISODate | 259 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ISODateTime | 262 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}LEIIdentifier | 265 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Max140Text | 270 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Max16Text | 276 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Max34Text | 282 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Max350Text | 288 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Max35Text | 294 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Max4AlphaNumericText | 300 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}Max70Text | 307 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}MessageHeader7 | 313 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}NameAndAddress5 | 322 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}OriginalBusinessQuery1 | 328 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}PartyIdentification120Choice | 335 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}PartyIdentification136 | 342 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}PostalAddress1 | 348 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}PostalAddress27 | 360 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ReportQueryCriteria3 | 382 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ReportQueryRequestV02 | 388 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}ReportQuerySearchCriteria3 | 395 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}RequestType4Choice | 408 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}SupplementaryData1 | 415 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:admi.005.001.02}SupplementaryDataEnvelope1 | 421 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 14 |
| complexType | 38 |
| element | 132 |
| enumeration | 8 |
| maxLength | 14 |
| minLength | 14 |
| pattern | 7 |
| restriction | 24 |
| schema | 1 |
| sequence | 24 |
| simpleType | 24 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../evidence/archived/27838557c5ee2ef31b02fefa.md) · [Message](index.md)
