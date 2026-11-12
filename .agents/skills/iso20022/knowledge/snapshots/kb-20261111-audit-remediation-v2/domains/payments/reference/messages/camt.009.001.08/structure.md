---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "camt.009.001.08"
message_family: "camt.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.009.001.08"
source_ids: ["src-000023"]
source_editions: ["2024-2025"]
---

# camt.009.001.08 structure

[src-000023](../../../../../raw-input/cash_management/camt.009.001.08.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.009.001.08`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.009.001.08 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ActiveAmountRange3Choice | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ActiveCurrencyAndAmountRange3 | 23 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ActiveCurrencyCode | 30 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}AddressType2Code | 35 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}AddressType3Choice | 45 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}AmountRangeBoundary1 | 51 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}BICFIDec2014Identifier | 57 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}BranchAndFinancialInstitutionIdentification8 | 62 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}BranchData5 | 68 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ClearingSystemIdentification2Choice | 76 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ClearingSystemMemberIdentification2 | 82 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}CountryCode | 88 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}CreditDebitCode | 93 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}DateAndPeriod2Choice | 99 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Document | 107 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Exact4AlphaNumericText | 112 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ExternalAccountIdentification1Code | 117 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ExternalClearingSystemIdentification1Code | 123 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ExternalEnquiryRequestType1Code | 129 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ExternalFinancialInstitutionIdentification1Code | 135 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ExternalMarketInfrastructure1Code | 141 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ExternalPaymentControlRequestType1Code | 147 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}FinancialIdentificationSchemeName1Choice | 153 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}FinancialInstitutionIdentification23 | 159 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}FromToAmountRange1 | 169 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}FromToPercentageRange1 | 175 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}GenericAccountIdentification1 | 181 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}GenericFinancialIdentification1 | 188 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}GenericIdentification1 | 195 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}GenericIdentification30 | 202 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}GetLimitV08 | 209 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}IBAN2007Identifier | 216 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ISODate | 221 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ISODateTime | 224 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ImpliedCurrencyAmountRange1Choice | 227 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ImpliedCurrencyAndAmount | 236 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}ImpliedCurrencyAndAmountRange1 | 243 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}LEIIdentifier | 249 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}LimitCriteria7 | 254 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}LimitCriteria7Choice | 261 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}LimitQuery5 | 267 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}LimitReturnCriteria2 | 273 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}LimitSearchCriteria7 | 281 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}LimitType1Choice | 296 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}LimitType3Code | 302 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}MarketInfrastructureIdentification1Choice | 321 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Max140Text | 327 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Max16Text | 333 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Max34Text | 339 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Max350Text | 345 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Max35Text | 351 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Max70Text | 357 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}MessageHeader9 | 363 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}PercentageRange1Choice | 370 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}PercentageRangeBoundary1 | 379 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}PercentageRate | 385 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}Period2 | 391 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}PostalAddress27 | 397 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}QueryType2Code | 419 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}RequestType4Choice | 427 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}RequestedIndicator | 434 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}SupplementaryData1 | 437 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}SupplementaryDataEnvelope1 | 443 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}SystemIdentification2Choice | 448 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.009.001.08}YesNoIndicator | 454 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 14 |
| complexType | 39 |
| element | 126 |
| enumeration | 27 |
| fractionDigits | 2 |
| maxLength | 12 |
| minInclusive | 1 |
| minLength | 12 |
| pattern | 6 |
| restriction | 28 |
| schema | 1 |
| sequence | 25 |
| simpleType | 28 |
| totalDigits | 2 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
