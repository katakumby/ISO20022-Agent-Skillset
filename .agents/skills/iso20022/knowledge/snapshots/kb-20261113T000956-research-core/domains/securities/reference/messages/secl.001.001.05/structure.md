---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "secl.001.001.05"
message_family: "secl.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.001.001.05"
source_ids: ["src-000055"]
source_editions: ["2025-2026"]
---

# secl.001.001.05 structure

[src-000055](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/secl.001.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:secl.001.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:secl.001.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}AccountIdentification26 | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ActiveCurrencyAndAmount_SimpleType | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ActiveCurrencyAndAmount | 17 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ActiveCurrencyCode | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount | 36 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ActiveOrHistoricCurrencyAndAmount_SimpleType | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ActiveOrHistoricCurrencyAndAmount | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ActiveOrHistoricCurrencyCode | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}AddressType2Code | 62 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}AlternatePartyIdentification4 | 72 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}AlternatePartyIdentification8 | 79 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}AmountAndDirection21 | 86 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}AmountAndDirection27 | 92 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}AnyBICDec2014Identifier | 100 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}BaseOneRate | 105 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Clearing8 | 111 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ClearingAccountType1Code | 119 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ContactIdentification2 | 126 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}CountryCode | 137 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}CreditDebitCode | 142 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}CurrencyCode | 148 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}DateAndDateTime2Choice | 153 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}DateCode20Choice | 159 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}DateFormat66Choice | 165 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}DateType1Code | 171 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}DecimalNumber | 176 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}DeliveringPartiesAndAccount22 | 182 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Document | 190 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Exact4AlphaNumericText | 195 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ExternalFinancialInstrumentIdentificationType1Code | 200 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}FinancialInstrumentQuantity1Choice | 206 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ForeignExchangeTerms17 | 213 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}GenericIdentification189 | 221 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}GenericIdentification30 | 227 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}GenericIdentification36 | 234 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ISINOct2015Identifier | 241 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ISODate | 246 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ISODateTime | 249 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}IdentificationSource3Choice | 252 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}IdentificationType43Choice | 258 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}IdentificationType6Choice | 264 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ImpliedCurrencyAndAmount | 270 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}MICIdentifier | 277 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}MarketIdentification1Choice | 282 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}MarketIdentification84 | 288 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}MarketIdentification85 | 294 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}MarketType2Code | 300 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}MarketType5Code | 309 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}MarketType8Choice | 315 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}MarketType9Choice | 321 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Max140Text | 327 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Max16Text | 333 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Max256Text | 339 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Max350Text | 345 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Max35Text | 351 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Max70Text | 357 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}NameAndAddress13 | 363 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}NameAndAddress5 | 369 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}NameAndAddress6 | 375 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}NamePrefix1Code | 381 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}NettingEligible1Code | 389 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}NonGuaranteedTrade4 | 396 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}OtherIdentification1 | 404 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PartyIdentification253Choice | 411 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PartyIdentification254Choice | 417 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PartyIdentification255Choice | 424 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PartyIdentification256Choice | 431 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PartyIdentificationAndAccount227 | 438 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PartyIdentificationAndAccount229 | 446 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PartyIdentificationAndAccount230 | 456 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PartyTextInformation1 | 465 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PercentageRate | 472 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PhoneNumber | 478 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PostalAddress1 | 483 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PostalAddress2 | 495 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PostalAddress8 | 504 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Price14 | 516 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PriceRateOrAmount3Choice | 522 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}PriceValueType7Code | 528 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}ReceivingPartiesAndAccount22 | 545 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SafekeepingPlace1Code | 553 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SafekeepingPlace3Code | 561 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SafekeepingPlaceFormat43Choice | 566 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SafekeepingPlaceTypeAndAnyBICIdentifier4 | 574 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SafekeepingPlaceTypeAndText1 | 580 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SecuritiesAccount18 | 586 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SecuritiesAccount19 | 593 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SecurityIdentification48 | 600 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Settlement2 | 607 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Side1Code | 613 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SimpleIdentificationInformation4 | 630 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}Status5Code | 635 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SubAccount4 | 642 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SupplementaryData1 | 649 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}SupplementaryDataEnvelope1 | 655 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}TradeLeg14 | 660 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}TradeLegNotificationV05 | 694 |
| [type-0100](types/type-0100.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}TradePosting1Code | 706 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}TradeTransactionCondition4Code | 712 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}TradeTransactionCondition5Choice | 738 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}TradeType1Code | 744 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}TradingCapacity10Code | 754 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}TypeOfIdentification1Code | 762 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}TypeOfIdentification2Code | 773 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}UTIIdentifier | 782 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.001.001.05}YesNoIndicator | 787 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 17 |
| complexType | 61 |
| element | 203 |
| enumeration | 106 |
| extension | 3 |
| fractionDigits | 7 |
| maxLength | 7 |
| minInclusive | 4 |
| minLength | 7 |
| pattern | 10 |
| restriction | 46 |
| schema | 1 |
| sequence | 41 |
| simpleContent | 3 |
| simpleType | 46 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/a163dd5cb0e2ef7d17ce70d1.md) · [Message](index.md)
