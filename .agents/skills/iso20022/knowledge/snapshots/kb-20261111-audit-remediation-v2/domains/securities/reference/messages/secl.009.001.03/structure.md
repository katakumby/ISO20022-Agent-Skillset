---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "secl.009.001.03"
message_family: "secl.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.009.001.03"
source_ids: ["src-000063"]
source_editions: ["2025-2026"]
---

# secl.009.001.03 structure

[src-000063](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/secl.009.001.03.xsd); `urn:iso:std:iso:20022:tech:xsd:secl.009.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:secl.009.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ActiveOrHistoricCurrencyAndAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ActiveOrHistoricCurrencyAndAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}AddressType2Code | 57 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}AlternatePartyIdentification4 | 67 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}AmountAndDirection20 | 74 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}AmountAndDirection27 | 80 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}AnyBICIdentifier | 88 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}BaseOneRate | 93 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}BuyIn2 | 99 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}BuyInConfirmationV03 | 109 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}CashCompensation1 | 118 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ClearingAccountType1Code | 125 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}CountryCode | 132 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}CreditDebitCode | 137 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}DecimalNumber | 143 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Document | 149 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Exact4AlphaNumericText | 154 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ExternalFinancialInstrumentIdentificationType1Code | 159 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}FinancialInstrumentQuantity1Choice | 165 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ForeignExchangeTerms17 | 172 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}GenericIdentification29 | 180 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}GenericIdentification30 | 187 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}GenericIdentification40 | 194 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}GenericIdentification58 | 201 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ISINIdentifier | 207 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ISODate | 212 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}IdentificationSource3Choice | 215 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}IdentificationType6Choice | 221 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}ImpliedCurrencyAndAmount | 227 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Max140Text | 234 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Max16Text | 240 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Max350Text | 246 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Max35Text | 252 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Max70Text | 258 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}NameAndAddress5 | 264 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}NameAndAddress6 | 270 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}OtherIdentification1 | 276 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PartyIdentification33Choice | 283 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PartyIdentification34Choice | 290 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PartyIdentification35Choice | 297 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PartyIdentificationAndAccount31 | 303 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PartyTextInformation1 | 311 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PercentageRate | 318 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PostalAddress1 | 324 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PostalAddress2 | 336 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}Price4 | 345 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PriceRateOrAmountChoice | 351 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}PriceValueType7Code | 357 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SafekeepingPlace1Code | 374 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SafekeepingPlace3Code | 382 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SafekeepingPlaceFormat7Choice | 387 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SafekeepingPlaceTypeAndAnyBICIdentifier1 | 395 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SafekeepingPlaceTypeAndText1 | 401 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SecuritiesAccount18 | 407 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SecuritiesAccount19 | 414 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SecuritiesCompensation1 | 421 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SecurityIdentification14 | 428 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SettlementObligation7 | 435 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SupplementaryData1 | 456 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}SupplementaryDataEnvelope1 | 462 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.009.001.03}TypeOfIdentification1Code | 467 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 8 |
| complexType | 40 |
| element | 125 |
| enumeration | 36 |
| extension | 3 |
| fractionDigits | 7 |
| maxLength | 6 |
| minInclusive | 4 |
| minLength | 6 |
| pattern | 6 |
| restriction | 27 |
| schema | 1 |
| sequence | 29 |
| simpleContent | 3 |
| simpleType | 27 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
