---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "secl.010.001.04"
message_family: "secl.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:secl.010.001.04"
source_ids: ["src-000064"]
source_editions: ["2025-2026"]
---

# secl.010.001.04 structure

[src-000064](../../../../../raw-input/central_counterparty_clearing_ccp_clearing/secl.010.001.04.xsd); `urn:iso:std:iso:20022:tech:xsd:secl.010.001.04`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:secl.010.001.04 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}AccountIdentification26 | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ActiveCurrencyAndAmount_SimpleType | 10 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ActiveCurrencyAndAmount | 17 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ActiveCurrencyCode | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ActiveOrHistoricCurrencyAnd13DecimalAmount | 36 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ActiveOrHistoricCurrencyAndAmount_SimpleType | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ActiveOrHistoricCurrencyAndAmount | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ActiveOrHistoricCurrencyCode | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}AddressType2Code | 62 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}AlternatePartyIdentification4 | 72 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}AmountAndDirection27 | 79 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}AnyBICDec2014Identifier | 87 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}BaseOneRate | 92 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ClearingAccountType1Code | 98 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ContactIdentification2 | 105 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}CountryCode | 116 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}CreditDebitCode | 121 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}CurrencyCode | 127 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}DateAndDateTime2Choice | 132 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}DateCode20Choice | 138 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}DateFormat65Choice | 144 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}DateType1Code | 150 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}DecimalNumber | 155 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}DeliveringPartiesAndAccount21 | 161 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}DeliveringPartiesAndAccount22 | 169 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}DeliveryReceiptType2Code | 177 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Document | 183 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Exact4AlphaNumericText | 188 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ExternalFinancialInstrumentIdentificationType1Code | 193 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}FinancialInstrumentQuantity1Choice | 199 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ForeignExchangeTerms17 | 206 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}GenericIdentification189 | 214 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}GenericIdentification30 | 220 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}GenericIdentification36 | 227 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ISINOct2015Identifier | 234 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ISODate | 239 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ISODateTime | 242 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}IdentificationSource3Choice | 245 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}IdentificationType6Choice | 251 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ImpliedCurrencyAndAmount | 257 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}MICIdentifier | 264 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}MarketIdentification1Choice | 269 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}MarketIdentification84 | 275 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}MarketType2Code | 281 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}MarketType8Choice | 290 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Max140Text | 296 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Max16Text | 302 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Max256Text | 308 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Max350Text | 314 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Max35Text | 320 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Max5NumericText | 326 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Max70Text | 331 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}NameAndAddress5 | 337 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}NameAndAddress6 | 343 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}NamePrefix1Code | 349 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ObligationType1Choice | 357 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ObligationType1Code | 363 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}OtherIdentification1 | 370 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Pagination1 | 377 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PartyIdentification253Choice | 383 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PartyIdentification254Choice | 389 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PartyIdentification255Choice | 396 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PartyIdentificationAndAccount227 | 403 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PartyIdentificationAndAccount228 | 411 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PartyIdentificationAndAccount229 | 421 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PartyTextInformation1 | 431 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PercentageRate | 438 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PhoneNumber | 444 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PostalAddress1 | 449 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PostalAddress2 | 461 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Price14 | 470 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PriceRateOrAmount3Choice | 476 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}PriceValueType7Code | 482 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ReceiveDelivery1Code | 499 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ReceivingPartiesAndAccount21 | 505 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ReceivingPartiesAndAccount22 | 513 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Reference24 | 521 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}Report7 | 527 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}ReportParameters8 | 533 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SafekeepingPlace1Code | 539 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SafekeepingPlace3Code | 547 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SafekeepingPlaceFormat43Choice | 552 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SafekeepingPlaceTypeAndAnyBICIdentifier4 | 560 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SafekeepingPlaceTypeAndText1 | 566 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SecuritiesAccount18 | 572 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SecuritiesAccount19 | 579 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SecurityIdentification48 | 586 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SettlementObligation10 | 593 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SettlementObligation9 | 609 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SettlementObligationReportV04 | 628 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SettlementParties37Choice | 640 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SettlementParties38Choice | 646 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SimpleIdentificationInformation4 | 652 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SubAccount4 | 657 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SupplementaryData1 | 664 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}SupplementaryDataEnvelope1 | 670 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}TradeDate3Choice | 675 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}TradeLegNotificationIdentification1Choice | 681 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}TradingCapacity5Code | 687 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}TypeOfIdentification1Code | 694 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}UTIIdentifier | 705 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:secl.010.001.04}YesNoIndicator | 710 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 18 |
| complexType | 61 |
| element | 191 |
| enumeration | 56 |
| extension | 3 |
| fractionDigits | 7 |
| maxLength | 7 |
| minInclusive | 4 |
| minLength | 7 |
| pattern | 11 |
| restriction | 42 |
| schema | 1 |
| sequence | 40 |
| simpleContent | 3 |
| simpleType | 42 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/453c46b65e9a6b7b43376c73.md) · [Message](index.md)
