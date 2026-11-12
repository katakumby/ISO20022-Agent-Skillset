---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "payments"
message_id: "pacs.010.001.06"
message_family: "pacs.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06"
source_ids: ["src-000171"]
source_editions: ["2025-2026"]
---

# pacs.010.001.06 structure

[src-000171](../../../../../raw-input/payments_clearing_and_settlement/pacs.010.001.06.xsd); `urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ActiveOrHistoricCurrencyCode | 36 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}AddressType2Code | 41 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}AddressType3Choice | 51 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}BICFIDec2014Identifier | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}BatchBookingIndicator | 62 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}BranchAndFinancialInstitutionIdentification8 | 65 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}BranchData5 | 71 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}CashAccount40 | 79 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}CashAccountType2Choice | 88 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}CategoryPurpose1Choice | 94 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ClearingChannel2Code | 100 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ClearingSystemIdentification2Choice | 108 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ClearingSystemMemberIdentification2 | 114 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}CountryCode | 120 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}CreditTransferTransaction66 | 125 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}DecimalNumber | 151 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}DirectDebitTransactionInformation33 | 157 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Document | 176 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Exact4AlphaNumericText | 181 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalAccountIdentification1Code | 186 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalCashAccountType1Code | 192 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalCategoryPurpose1Code | 198 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalClearingSystemIdentification1Code | 204 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalCreditorAgentInstruction1Code | 210 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalFinancialInstitutionIdentification1Code | 216 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalLocalInstrument1Code | 222 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalProxyAccountType1Code | 228 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalPurpose1Code | 234 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ExternalServiceLevel1Code | 240 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}FinancialIdentificationSchemeName1Choice | 246 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}FinancialInstitutionDirectDebitV06 | 252 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}FinancialInstitutionIdentification23 | 259 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}GenericAccountIdentification1 | 269 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}GenericFinancialIdentification1 | 276 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}GenericIdentification30 | 283 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}GroupHeader119 | 290 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}IBAN2007Identifier | 300 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ISODate | 305 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ISODateTime | 308 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ISOTime | 311 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}InstructionForCreditorAgent3 | 314 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}LEIIdentifier | 320 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}LocalInstrument2Choice | 325 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Max140Text | 331 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Max15NumericText | 337 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Max16Text | 342 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Max2048Text | 348 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Max210Text | 354 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Max34Text | 360 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Max350Text | 366 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Max35Text | 372 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Max70Text | 378 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}PaymentIdentification13 | 384 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}PaymentTypeInformation28 | 393 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}PostalAddress27 | 402 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Priority2Code | 424 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Priority3Code | 430 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ProxyAccountIdentification1 | 437 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ProxyAccountType1Choice | 443 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}Purpose2Choice | 449 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}RemittanceInformation2 | 455 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}ServiceLevel8Choice | 460 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}SettlementDateTimeIndication1 | 466 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}SettlementTimeRequest2 | 472 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}SupplementaryData1 | 480 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}SupplementaryDataEnvelope1 | 486 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06}UUIDv4Identifier | 491 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 11 |
| complexType | 35 |
| element | 139 |
| enumeration | 15 |
| extension | 1 |
| fractionDigits | 2 |
| maxLength | 18 |
| minInclusive | 1 |
| minLength | 18 |
| pattern | 9 |
| restriction | 37 |
| schema | 1 |
| sequence | 23 |
| simpleContent | 1 |
| simpleType | 37 |
| totalDigits | 2 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
