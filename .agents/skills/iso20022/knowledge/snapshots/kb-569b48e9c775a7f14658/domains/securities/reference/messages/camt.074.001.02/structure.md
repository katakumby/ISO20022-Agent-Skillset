---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "camt.074.001.02"
message_family: "camt.074"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.074.001.02"
source_ids: ["src-000247"]
source_editions: ["march-2024"]
---

# camt.074.001.02 structure

[src-000247](../../../../../raw-input/target2securities_t2s/camt.074.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.074.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.074.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ActiveOrHistoricCurrencyCode | 36 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}AddressType2Code | 41 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}AddressType3Choice | 51 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Amount2Choice | 57 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}AmountAndDirection5 | 63 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}AmountAndQuantityBreakdown1 | 69 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}AnyBICDec2014Identifier | 77 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}BICFIDec2014Identifier | 82 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}BranchAndFinancialInstitutionIdentification8 | 87 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}BranchData5 | 93 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}CashAccount40 | 101 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}CashAccountType2Choice | 110 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}CashBalanceType3Choice | 116 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}CashSubBalanceTypeAndQuantityBreakdown3 | 122 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ClearingSystemIdentification2Choice | 128 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ClearingSystemMemberIdentification2 | 134 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}CopyDuplicate1Code | 140 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}CountryCode | 147 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}CreditDebitCode | 152 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}DateAndDateTime2Choice | 158 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}DecimalNumber | 164 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Document | 170 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}DocumentIdentification51 | 175 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Exact4AlphaNumericText | 184 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Exact4NumericText | 189 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ExternalAccountIdentification1Code | 194 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ExternalBalanceType1Code | 200 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ExternalCashAccountType1Code | 206 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ExternalClearingSystemIdentification1Code | 212 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ExternalFinancialInstitutionIdentification1Code | 218 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ExternalProxyAccountType1Code | 224 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}FinancialIdentificationSchemeName1Choice | 230 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}FinancialInstitutionIdentification23 | 236 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}FinancialInstrumentQuantity1Choice | 246 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}GenericAccountIdentification1 | 253 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}GenericFinancialIdentification1 | 260 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}GenericIdentification30 | 267 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}GenericIdentification36 | 274 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}GenericIdentification37 | 281 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}IBAN2007Identifier | 287 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ISODate | 292 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ISODateTime | 295 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ImpliedCurrencyAndAmount | 298 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}IntraBalance5 | 305 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}IntraBalanceMovementCancellationRequestV02 | 316 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}LEIIdentifier | 327 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Max140Text | 332 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Max16Text | 338 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Max2048Text | 344 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Max34Text | 350 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Max350Text | 356 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Max35Text | 362 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}Max70Text | 368 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}NameAndAddress5 | 374 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}PartyIdentification120Choice | 380 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}PartyIdentification136 | 387 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}PostalAddress1 | 393 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}PostalAddress27 | 405 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}PriorityNumeric4Choice | 427 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ProxyAccountIdentification1 | 433 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}ProxyAccountType1Choice | 439 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}References14 | 445 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}SupplementaryData1 | 454 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}SupplementaryDataEnvelope1 | 460 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.074.001.02}SystemPartyIdentification8 | 465 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 13 |
| complexType | 40 |
| element | 131 |
| enumeration | 11 |
| extension | 1 |
| fractionDigits | 3 |
| maxLength | 13 |
| minInclusive | 2 |
| minLength | 13 |
| pattern | 9 |
| restriction | 30 |
| schema | 1 |
| sequence | 26 |
| simpleContent | 1 |
| simpleType | 30 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
