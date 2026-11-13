---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.005.001.02"
message_family: "semt.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.005.001.02"
source_ids: ["src-000117"]
source_editions: ["2025-2026"]
---

# semt.005.001.02 structure

[src-000117](../../../../../raw-input/investment_funds/semt.005.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.005.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.005.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Account7 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AccountIdentification1 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AccountIdentification3 | 16 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AccountIdentificationAndPurpose | 23 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AccountIdentificationFormatChoice | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AccountingStatementOfHoldings2 | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AccountingStatementOfHoldingsCancellationV02 | 48 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ActiveCurrencyAndAmount_SimpleType | 57 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ActiveCurrencyAndAmount | 64 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ActiveCurrencyCode | 71 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 76 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ActiveOrHistoricCurrencyAnd13DecimalAmount | 83 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ActiveOrHistoricCurrencyAndAmount_SimpleType | 90 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ActiveOrHistoricCurrencyAndAmount | 97 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ActiveOrHistoricCurrencyCode | 104 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AdditionalBalanceInformation2 | 109 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AdditionalReference2 | 118 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AddressType2Code | 125 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AggregateBalanceInformation3 | 135 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AggregateBalancePerSafekeepingPlace4 | 153 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AlternateSecurityIdentification1 | 169 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}AnyBICIdentifier | 178 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}BalanceQuantity1Choice | 183 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}BaseOneRate | 191 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}BelgianIdentifier | 197 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}BloombergIdentifier | 200 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}CUSIPIdentifier | 206 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ConsolidatedTapeAssociationIdentifier | 209 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}CountryCode | 215 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}DateAndDateTimeChoice | 220 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}DecimalNumber | 228 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}DistributionPolicy1Code | 234 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Document | 240 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}DutchIdentifier | 245 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}EuroclearClearstreamIdentifier | 248 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}EventFrequency1Code | 254 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Exact4AlphaNumericText | 271 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Extended350Code | 276 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Extension1 | 282 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}FinancialInstrument13 | 288 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}FinancialInstrumentQuantityChoice | 298 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ForeignExchangeTerms6 | 307 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}FormOfSecurity1Code | 316 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}FrequencyCodeAndDSSCode1Choice | 322 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}GenericIdentification1 | 330 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}GenericIdentification5 | 337 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}GenericIdentification6 | 344 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}GenericIdentification7 | 351 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ISINIdentifier | 357 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ISODate | 362 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ISODateTime | 365 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ImpliedCurrencyAndAmount | 368 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Intermediary11 | 375 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}InvestmentFundRole2Code | 385 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}LongPostalAddress1Choice | 398 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}MICIdentifier | 406 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Max140Text | 411 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Max16Text | 417 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Max350Text | 423 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Max35Text | 429 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Max5NumericText | 435 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Max70Text | 440 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Max8Text | 446 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}MessageIdentification1 | 452 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}NameAndAddress2 | 458 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}NameAndAddress5 | 464 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Number | 470 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Pagination | 476 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PartyIdentification1Choice | 482 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PartyIdentification2Choice | 491 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PartyIdentification3 | 500 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PercentageRate | 505 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PlusOrMinusIndicator | 511 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PostalAddress1 | 514 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PriceInformation2 | 526 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PriceRateOrAmountOrUnknownChoice | 539 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PriceSource | 548 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PriceSource1Code | 554 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PriceSourceFormatChoice | 561 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}PriceValueType2Code | 570 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}QUICKIdentifier | 576 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}QuantityAndAvailability | 579 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}RICIdentifier | 585 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SEDOLIdentifier | 591 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SafekeepingAccount2 | 594 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SafekeepingPlace1Code | 605 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SafekeepingPlaceAsCodeAndPartyIdentification | 613 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SafekeepingPlaceFormatChoice | 620 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SecuritiesAccountPurposeType1Code | 629 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SecuritiesBalanceType1Code | 639 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SecuritiesBalanceType2Code | 664 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SecurityIdentification3Choice | 674 |
| [type-0094](types/type-0094.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SicovamIdentifier | 695 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SimpleIdentificationInformation | 698 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}Statement6 | 703 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}StatementBasis1Code | 716 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}StatementBasisCodeAndDSSCodeChoice | 723 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}StatementUpdateTypeCode | 731 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}StatementUpdateTypeCodeAndDSSCodeChoice | 737 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}StructuredLongPostalAddress1 | 745 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SubAccountIdentification3 | 761 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SubBalanceInformation2 | 769 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}SubBalanceQuantity1Choice | 779 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}TickerIdentifier | 788 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}TotalValueInPageAndStatement | 794 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}TypeOfPrice11Code | 800 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}ValorenIdentifier | 816 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}WertpapierIdentifier | 819 |
| [type-0110](types/type-0110.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.005.001.02}YesNoIndicator | 822 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 3 |
| choice | 20 |
| complexType | 55 |
| element | 205 |
| enumeration | 91 |
| extension | 3 |
| fractionDigits | 8 |
| maxLength | 12 |
| minInclusive | 4 |
| minLength | 12 |
| pattern | 8 |
| restriction | 54 |
| schema | 1 |
| sequence | 52 |
| simpleContent | 3 |
| simpleType | 54 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/13327b249de3ff7407778863.md) · [Message](index.md)
