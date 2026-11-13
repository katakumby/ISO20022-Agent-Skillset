---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "secl.002.001.05"
message_family: "secl.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.002.001.05"
source_ids: ["src-000056"]
source_editions: ["2025-2026"]
---

# secl.002.001.05 structure

[src-000056](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/secl.002.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:secl.002.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:secl.002.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}AccountIdentification26 | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ActiveCurrencyAndAmount_SimpleType | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ActiveCurrencyAndAmount | 17 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ActiveCurrencyCode | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount | 36 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ActiveOrHistoricCurrencyAndAmount_SimpleType | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ActiveOrHistoricCurrencyAndAmount | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ActiveOrHistoricCurrencyCode | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}AddressType2Code | 62 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}AlternatePartyIdentification4 | 72 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}AlternatePartyIdentification8 | 79 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}AmountAndDirection21 | 86 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}AmountAndDirection27 | 92 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}AnyBICDec2014Identifier | 100 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}BaseOneRate | 105 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}CancellationReason36Choice | 111 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}CancelledStatusReason16Code | 117 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Clearing8 | 134 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ClearingAccountType1Code | 142 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ContactIdentification2 | 149 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}CountryCode | 160 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}CreditDebitCode | 165 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}CurrencyCode | 171 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}DateAndDateTime2Choice | 176 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}DateCode20Choice | 182 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}DateFormat66Choice | 188 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}DateType1Code | 194 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}DecimalNumber | 199 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}DeliveringPartiesAndAccount22 | 205 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Document | 213 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Exact4AlphaNumericText | 218 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ExternalFinancialInstrumentIdentificationType1Code | 223 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}FinancialInstrumentQuantity1Choice | 229 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ForeignExchangeTerms17 | 236 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}GenericIdentification189 | 244 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}GenericIdentification30 | 250 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}GenericIdentification36 | 257 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ISINOct2015Identifier | 264 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ISODate | 269 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ISODateTime | 272 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}IdentificationSource3Choice | 275 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}IdentificationType43Choice | 281 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}IdentificationType6Choice | 287 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ImpliedCurrencyAndAmount | 293 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}MICIdentifier | 300 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}MarketIdentification1Choice | 305 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}MarketIdentification84 | 311 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}MarketIdentification85 | 317 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}MarketType2Code | 323 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}MarketType5Code | 332 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}MarketType8Choice | 338 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}MarketType9Choice | 344 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Max140Text | 350 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Max16Text | 356 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Max256Text | 362 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Max350Text | 368 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Max35Text | 374 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Max70Text | 380 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}NameAndAddress13 | 386 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}NameAndAddress5 | 392 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}NameAndAddress6 | 398 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}NamePrefix1Code | 404 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}NettingEligible1Code | 412 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}NonGuaranteedTrade4 | 419 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}OtherIdentification1 | 427 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PartyIdentification253Choice | 434 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PartyIdentification254Choice | 440 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PartyIdentification255Choice | 447 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PartyIdentification256Choice | 454 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PartyIdentificationAndAccount227 | 461 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PartyIdentificationAndAccount229 | 469 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PartyIdentificationAndAccount230 | 479 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PartyTextInformation1 | 488 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PercentageRate | 495 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PhoneNumber | 501 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PostalAddress1 | 506 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PostalAddress2 | 518 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PostalAddress8 | 527 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Price14 | 539 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PriceRateOrAmount3Choice | 545 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}PriceValueType7Code | 551 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}ReceivingPartiesAndAccount22 | 568 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SafekeepingPlace1Code | 576 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SafekeepingPlace3Code | 584 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SafekeepingPlaceFormat43Choice | 589 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SafekeepingPlaceTypeAndAnyBICIdentifier4 | 597 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SafekeepingPlaceTypeAndText1 | 603 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SecuritiesAccount18 | 609 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SecuritiesAccount19 | 616 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SecurityIdentification48 | 623 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Settlement2 | 630 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Side1Code | 636 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SimpleIdentificationInformation4 | 653 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}Status5Code | 658 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SubAccount4 | 665 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SupplementaryData1 | 672 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}SupplementaryDataEnvelope1 | 678 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}TradeLeg14 | 683 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}TradeLegNotificationCancellationV05 | 717 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}TradePosting1Code | 730 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}TradeTransactionCondition4Code | 736 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}TradeTransactionCondition5Choice | 762 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}TradeType1Code | 768 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}TradingCapacity10Code | 778 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}TypeOfIdentification1Code | 786 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}TypeOfIdentification2Code | 797 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}UTIIdentifier | 806 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.002.001.05}YesNoIndicator | 811 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 18 |
| complexType | 62 |
| element | 206 |
| enumeration | 117 |
| extension | 3 |
| fractionDigits | 7 |
| maxLength | 8 |
| minInclusive | 4 |
| minLength | 8 |
| pattern | 10 |
| restriction | 47 |
| schema | 1 |
| sequence | 41 |
| simpleContent | 3 |
| simpleType | 47 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/e3ed56f4c9e500c3b8b46e53.md) · [Message](index.md)
