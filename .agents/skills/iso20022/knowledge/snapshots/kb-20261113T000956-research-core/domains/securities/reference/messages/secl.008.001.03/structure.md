---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "secl.008.001.03"
message_family: "secl.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.008.001.03"
source_ids: ["src-000062"]
source_editions: ["2025-2026"]
---

# secl.008.001.03 structure

[src-000062](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/secl.008.001.03.xsd); `urn:iso:std:iso:20022:tech:xsd:secl.008.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:secl.008.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ActiveOrHistoricCurrencyAndAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ActiveOrHistoricCurrencyAndAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}AddressType2Code | 57 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}AlternatePartyIdentification4 | 67 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}AmountAndDirection27 | 74 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}AnyBICIdentifier | 82 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}BaseOneRate | 87 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}BuyIn3 | 93 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}BuyInResponseV03 | 103 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ClearingAccountType1Code | 111 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}CountryCode | 118 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}CreditDebitCode | 123 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}DecimalNumber | 129 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Document | 135 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Exact4AlphaNumericText | 140 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ExternalFinancialInstrumentIdentificationType1Code | 145 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}FinancialInstrumentQuantity1Choice | 151 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ForeignExchangeTerms17 | 158 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}GenericIdentification29 | 166 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}GenericIdentification30 | 173 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}GenericIdentification40 | 180 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}GenericIdentification58 | 187 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ISINIdentifier | 193 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ISODate | 198 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}IdentificationSource3Choice | 201 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}IdentificationType6Choice | 207 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}ImpliedCurrencyAndAmount | 213 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Max140Text | 220 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Max16Text | 226 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Max350Text | 232 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Max35Text | 238 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Max70Text | 244 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}NameAndAddress5 | 250 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}NameAndAddress6 | 256 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Number | 262 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}OtherIdentification1 | 268 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PartyIdentification33Choice | 275 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PartyIdentification34Choice | 282 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PartyIdentification35Choice | 289 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PartyIdentificationAndAccount31 | 295 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PartyTextInformation1 | 303 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PercentageRate | 310 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PostalAddress1 | 316 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PostalAddress2 | 328 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}Price4 | 337 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PriceRateOrAmountChoice | 343 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}PriceValueType7Code | 349 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SafekeepingPlace1Code | 366 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SafekeepingPlace3Code | 374 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SafekeepingPlaceFormat7Choice | 379 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SafekeepingPlaceTypeAndAnyBICIdentifier1 | 387 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SafekeepingPlaceTypeAndText1 | 393 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SecuritiesAccount18 | 399 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SecuritiesAccount19 | 406 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SecurityIdentification14 | 413 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SettlementObligation7 | 420 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SupplementaryData1 | 441 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}SupplementaryDataEnvelope1 | 447 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}TypeOfIdentification1Code | 452 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.008.001.03}YesNoIndicator | 463 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 8 |
| complexType | 37 |
| element | 116 |
| enumeration | 36 |
| extension | 3 |
| fractionDigits | 8 |
| maxLength | 6 |
| minInclusive | 4 |
| minLength | 6 |
| pattern | 6 |
| restriction | 29 |
| schema | 1 |
| sequence | 26 |
| simpleContent | 3 |
| simpleType | 29 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/71e6ff36a5ad07d41c657667.md) · [Message](index.md)
