---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.047.001.08"
message_family: "camt.047"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.047.001.08"
source_ids: ["src-000040"]
source_editions: ["2024-2025"]
---

# camt.047.001.08 structure

[src-000040](../../../../../raw-input/cash_management/camt.047.001.08.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.047.001.08`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.047.001.08 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}AddressType2Code | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}AddressType3Choice | 46 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Amount2Choice | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}BICFIDec2014Identifier | 58 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}BranchAndFinancialInstitutionIdentification8 | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}BranchData5 | 69 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ClearingSystemIdentification2Choice | 77 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ClearingSystemMemberIdentification2 | 83 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}CountryCode | 89 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}CurrentAndDefaultReservation6 | 94 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}DateAndDateTime2Choice | 100 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Document | 106 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ErrorHandling3Choice | 111 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ErrorHandling5 | 117 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Exact4AlphaNumericText | 123 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ExternalAccountIdentification1Code | 128 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ExternalClearingSystemIdentification1Code | 134 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ExternalEnquiryRequestType1Code | 140 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ExternalFinancialInstitutionIdentification1Code | 146 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ExternalMarketInfrastructure1Code | 152 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ExternalPaymentControlRequestType1Code | 158 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ExternalReservationType1Code | 164 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ExternalSystemErrorHandling1Code | 170 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}FinancialIdentificationSchemeName1Choice | 176 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}FinancialInstitutionIdentification23 | 182 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}GenericAccountIdentification1 | 192 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}GenericFinancialIdentification1 | 199 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}GenericIdentification1 | 206 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}GenericIdentification30 | 213 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}IBAN2007Identifier | 220 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ISODate | 225 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ISODateTime | 228 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ImpliedCurrencyAndAmount | 231 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}LEIIdentifier | 238 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}MarketInfrastructureIdentification1Choice | 243 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Max140Text | 249 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Max16Text | 255 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Max34Text | 261 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Max350Text | 267 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Max35Text | 273 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Max70Text | 279 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}MessageHeader7 | 285 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}OriginalBusinessQuery1 | 294 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}PostalAddress27 | 301 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}RequestType4Choice | 323 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}Reservation3 | 330 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ReservationIdentification4 | 337 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ReservationOrError11Choice | 346 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ReservationOrError9Choice | 352 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ReservationReport8 | 358 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ReservationStatus1Choice | 364 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ReservationStatus1Code | 370 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ReservationType2Choice | 379 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}ReturnReservationV08 | 385 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}SupplementaryData1 | 392 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}SupplementaryDataEnvelope1 | 398 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.047.001.08}SystemIdentification2Choice | 403 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 15 |
| complexType | 36 |
| element | 104 |
| enumeration | 11 |
| extension | 1 |
| fractionDigits | 2 |
| maxLength | 14 |
| minInclusive | 2 |
| minLength | 14 |
| pattern | 6 |
| restriction | 26 |
| schema | 1 |
| sequence | 20 |
| simpleContent | 1 |
| simpleType | 26 |
| totalDigits | 2 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
