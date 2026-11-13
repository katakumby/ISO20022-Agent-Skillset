---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "secl.004.001.04"
message_family: "secl.004"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.004.001.04"
source_ids: ["src-000058"]
source_editions: ["2025-2026"]
---

# secl.004.001.04 structure

[src-000058](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/secl.004.001.04.xsd); `urn:iso:std:iso:20022:tech:xsd:secl.004.001.04`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:secl.004.001.04 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ActiveOrHistoricCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ActiveOrHistoricCurrencyAndAmount_SimpleType | 19 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ActiveOrHistoricCurrencyAndAmount | 26 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ActiveOrHistoricCurrencyCode | 33 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}AddressType2Code | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}AlternatePartyIdentification4 | 48 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}AlternatePartyIdentification8 | 55 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}AmountAndDirection21 | 62 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}AnyBICDec2014Identifier | 68 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ClearingAccountType1Code | 73 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}CountryCode | 80 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}CreditDebitCode | 85 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}CurrencyCode | 91 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}DateAndDateTime2Choice | 96 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}DateCode20Choice | 102 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}DateFormat66Choice | 108 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}DateType1Code | 114 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}DecimalNumber | 119 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Document | 125 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}EventFrequency6Code | 130 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Exact4AlphaNumericText | 137 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Exact5NumericText | 142 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ExternalFinancialInstrumentIdentificationType1Code | 147 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}FinancialInstrumentQuantity1Choice | 153 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}GenericIdentification189 | 160 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}GenericIdentification30 | 166 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}GenericIdentification36 | 173 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ISINOct2015Identifier | 180 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ISODate | 185 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ISODateTime | 188 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}IdentificationSource3Choice | 191 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}IdentificationType43Choice | 197 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}IdentificationType6Choice | 203 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ImpliedCurrencyAndAmount | 209 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}MICIdentifier | 216 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}MarketIdentification1Choice | 221 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}MarketIdentification20 | 227 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}MarketIdentification84 | 233 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}MarketIdentification85 | 239 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}MarketType2Code | 245 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}MarketType5Code | 254 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}MarketType8Choice | 260 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}MarketType9Choice | 266 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Max140Text | 272 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Max16Text | 278 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Max350Text | 284 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Max35Text | 290 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Max5NumericText | 296 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Max70Text | 301 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}NameAndAddress13 | 307 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}NameAndAddress5 | 313 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}NameAndAddress6 | 319 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}NetPosition4 | 325 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}NetPositionV04 | 345 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}OtherIdentification1 | 355 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Pagination1 | 362 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PartyIdentification253Choice | 368 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PartyIdentification254Choice | 374 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PartyIdentification255Choice | 381 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PartyIdentification256Choice | 388 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PartyIdentificationAndAccount227 | 395 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PartyIdentificationAndAccount230 | 403 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PartyTextInformation1 | 412 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PercentageRate | 419 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PostalAddress1 | 425 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PostalAddress2 | 437 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PostalAddress8 | 446 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Price14 | 458 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PriceRateOrAmount3Choice | 464 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}PriceValueType7Code | 470 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ReceiveDelivery1Code | 487 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}ReportParameters7 | 493 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SafekeepingPlace1Code | 503 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SafekeepingPlace3Code | 511 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SafekeepingPlaceFormat43Choice | 516 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SafekeepingPlaceTypeAndAnyBICIdentifier4 | 524 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SafekeepingPlaceTypeAndText1 | 530 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SecuritiesAccount18 | 536 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SecuritiesAccount19 | 543 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SecurityIdentification48 | 550 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}Side1Code | 557 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}StatementUpdateType1Code | 574 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SupplementaryData1 | 580 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}SupplementaryDataEnvelope1 | 586 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}TradeLeg13 | 591 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}TradePosting1Code | 621 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}TradeType1Code | 627 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}TradingCapacity5Code | 637 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}TypeOfIdentification1Code | 644 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}TypeOfIdentification2Code | 655 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}UTIIdentifier | 664 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.004.001.04}YesNoIndicator | 669 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 16 |
| complexType | 51 |
| element | 177 |
| enumeration | 80 |
| extension | 2 |
| fractionDigits | 5 |
| maxLength | 6 |
| minInclusive | 3 |
| minLength | 6 |
| pattern | 10 |
| restriction | 42 |
| schema | 1 |
| sequence | 33 |
| simpleContent | 2 |
| simpleType | 42 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/0611bb025d91f8c3942f57d2.md) · [Message](index.md)
