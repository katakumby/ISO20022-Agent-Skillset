---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.002.001.02"
message_family: "semt.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.002.001.02"
source_ids: ["src-000114"]
source_editions: ["2025-2026"]
---

# semt.002.001.02 structure

[src-000114](../../../../../raw-input/investment_funds/semt.002.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.002.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.002.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Account7 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AccountIdentification1 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AccountIdentification3 | 16 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AccountIdentificationAndPurpose | 23 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AccountIdentificationFormatChoice | 29 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ActiveCurrencyAndAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ActiveCurrencyAndAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ActiveCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ActiveOrHistoricCurrencyAnd13DecimalAmount | 62 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ActiveOrHistoricCurrencyAndAmount_SimpleType | 69 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ActiveOrHistoricCurrencyAndAmount | 76 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ActiveOrHistoricCurrencyCode | 83 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AdditionalBalanceInformation2 | 88 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AdditionalReference2 | 97 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AddressType2Code | 104 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AggregateBalanceInformation4 | 114 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AggregateBalancePerSafekeepingPlace3 | 134 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AlternateSecurityIdentification1 | 152 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}AnyBICIdentifier | 161 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}BalanceQuantity1Choice | 166 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}BaseOneRate | 172 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}BelgianIdentifier | 178 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}BloombergIdentifier | 181 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}CUSIPIdentifier | 187 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ConsolidatedTapeAssociationIdentifier | 190 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}CountryCode | 196 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}CustodyStatementOfHoldingsV02 | 201 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}DateAndDateTimeChoice | 215 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}DecimalNumber | 221 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}DistributionPolicy1Code | 227 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Document | 233 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}DutchIdentifier | 238 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}EuroclearClearstreamIdentifier | 241 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}EventFrequency1Code | 247 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Exact4AlphaNumericText | 264 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Extended350Code | 269 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Extension1 | 275 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}FinancialInstrument13 | 281 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}FinancialInstrumentQuantityChoice | 291 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ForeignExchangeTerms6 | 298 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}FormOfSecurity1Code | 307 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}FrequencyCodeAndDSSCode1Choice | 313 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}GenericIdentification1 | 319 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}GenericIdentification5 | 326 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}GenericIdentification6 | 333 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}GenericIdentification7 | 340 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ISINIdentifier | 346 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ISODate | 351 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ISODateTime | 354 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ImpliedCurrencyAndAmount | 357 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Intermediary11 | 364 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}InvestmentFundRole2Code | 374 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}LongPostalAddress1Choice | 387 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}MICIdentifier | 393 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Max140Text | 398 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Max16Text | 404 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Max350Text | 410 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Max35Text | 416 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Max5NumericText | 422 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Max70Text | 427 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Max8Text | 433 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}MessageIdentification1 | 439 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}NameAndAddress2 | 445 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}NameAndAddress5 | 451 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Number | 457 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Pagination | 463 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PartyIdentification1Choice | 469 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PartyIdentification2Choice | 476 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PartyIdentification3 | 483 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PercentageRate | 488 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PlusOrMinusIndicator | 494 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PostalAddress1 | 497 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PriceInformation2 | 509 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PriceRateOrAmountOrUnknownChoice | 522 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PriceSource | 529 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PriceSource1Code | 535 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PriceSourceFormatChoice | 542 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}PriceValueType2Code | 549 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}QUICKIdentifier | 555 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}QuantityAndAvailability | 558 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}RICIdentifier | 564 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SEDOLIdentifier | 570 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SafekeepingAccount2 | 573 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SafekeepingPlace1Code | 584 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SafekeepingPlaceAsCodeAndPartyIdentification | 592 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SafekeepingPlaceFormatChoice | 599 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SecuritiesAccountPurposeType1Code | 606 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SecuritiesBalanceType1Code | 616 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SecuritiesBalanceType2Code | 641 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SecurityIdentification3Choice | 651 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SicovamIdentifier | 670 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SimpleIdentificationInformation | 673 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}Statement7 | 678 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}StatementBasis1Code | 690 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}StatementBasisCodeAndDSSCodeChoice | 697 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}StatementUpdateTypeCode | 703 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}StatementUpdateTypeCodeAndDSSCodeChoice | 709 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}StructuredLongPostalAddress1 | 715 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SubAccountIdentification5 | 731 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SubBalanceInformation2 | 739 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}SubBalanceQuantity1Choice | 749 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}TickerIdentifier | 756 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}TotalValueInPageAndStatement | 762 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}TypeOfPrice11Code | 768 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}ValorenIdentifier | 784 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}WertpapierIdentifier | 787 |
| [type-0109](types/type-0109.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.002.001.02}YesNoIndicator | 790 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| attribute | 3 |
| choice | 20 |
| complexType | 54 |
| element | 207 |
| enumeration | 91 |
| extension | 3 |
| fractionDigits | 8 |
| maxLength | 12 |
| minInclusive | 4 |
| minLength | 12 |
| pattern | 8 |
| restriction | 54 |
| schema | 1 |
| sequence | 36 |
| simpleContent | 3 |
| simpleType | 54 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/bc8aeae36dfb05e29416972c.md) · [Message](index.md)
