---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "secl.005.001.02"
message_family: "secl.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.005.001.02"
source_ids: ["src-000059"]
source_editions: ["2025-2026"]
---

# secl.005.001.02 structure

[src-000059](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/secl.005.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:secl.005.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:secl.005.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ActiveOrHistoricCurrencyAndAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ActiveOrHistoricCurrencyAndAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ActiveOrHistoricCurrencyCode | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}AlternatePartyIdentification4 | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Amount2 | 50 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}AmountAndDirection20 | 56 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}AnyBICIdentifier | 62 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ClearingAccountType1Code | 67 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Collateral6 | 74 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}CollateralType1Code | 81 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}CountryCode | 89 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}CreditDebitCode | 94 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}CurrencyCode | 100 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}DateAndDateTimeChoice | 105 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Document | 113 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}EventFrequency6Code | 118 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Exact4AlphaNumericText | 125 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Exact5NumericText | 130 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ExternalFinancialInstrumentIdentificationType1Code | 135 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}GenericIdentification29 | 141 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}GenericIdentification30 | 148 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ISINIdentifier | 155 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ISODate | 160 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ISODateTime | 163 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}IdentificationSource3Choice | 166 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}IdentificationType6Choice | 174 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ImpliedCurrencyAndAmount | 182 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Margin3 | 189 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Margin4 | 196 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}MarginCalculation1 | 203 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}MarginCalculation2 | 211 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}MarginProduct1Code | 222 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}MarginProductType1Choice | 228 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}MarginReport2 | 236 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}MarginReportV02 | 246 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}MarginResult1Choice | 256 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}MarginType1Choice | 264 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}MarginType1Code | 272 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Max140Text | 287 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Max16Text | 293 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Max350Text | 299 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Max35Text | 305 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Max5NumericText | 311 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Max70Text | 316 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}NameAndAddress6 | 322 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}OtherIdentification1 | 328 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}Pagination | 335 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}PartyIdentification33Choice | 341 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}PartyIdentification35Choice | 350 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}PartyIdentificationAndAccount31 | 358 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}PartyTextInformation1 | 366 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}PostalAddress2 | 373 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ReportParameters3 | 382 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}SecuritiesAccount18 | 392 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}SecurityIdentification14 | 399 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}ShortLong1Code | 406 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}SupplementaryData1 | 412 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}SupplementaryDataEnvelope1 | 418 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}TotalVariationMargin1 | 423 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}TypeOfIdentification1Code | 429 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}VariationMargin3 | 440 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.005.001.02}YesNoIndicator | 451 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 8 |
| complexType | 36 |
| element | 106 |
| enumeration | 34 |
| extension | 2 |
| fractionDigits | 3 |
| maxLength | 6 |
| minInclusive | 3 |
| minLength | 6 |
| pattern | 9 |
| restriction | 29 |
| schema | 1 |
| sequence | 34 |
| simpleContent | 2 |
| simpleType | 29 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
