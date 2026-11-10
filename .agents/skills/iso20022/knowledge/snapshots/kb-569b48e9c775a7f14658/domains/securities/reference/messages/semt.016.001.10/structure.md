---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.016.001.10"
message_family: "semt.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.016.001.10"
source_ids: ["src-000204"]
source_editions: ["2025-2026"]
---

# semt.016.001.10 structure

[src-000204](../../../../../raw-input/settlement_and_reconciliation/semt.016.001.10.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.016.001.10`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.016.001.10 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ActiveOrHistoricCurrencyAndAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ActiveOrHistoricCurrencyAndAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}AmountAndDirection44 | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}AnyBICDec2014Identifier | 65 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}BaseOneRate | 70 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}BlockChainAddressWallet3 | 76 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}CFIOct2015Identifier | 83 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ClassificationType32Choice | 88 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}CorporateActionEventType110Choice | 94 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}CorporateActionEventType38Code | 100 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}CountryCode | 173 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}CreditDebitCode | 178 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}DTI2024Identifier | 184 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}DateAndDateTime2Choice | 189 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}DateTimePeriod1 | 195 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}DecimalNumber | 201 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Document | 207 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}EventFrequency3Code | 212 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}EventFrequency4Code | 221 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Exact3NumericText | 231 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Exact4AlphaNumericText | 236 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Exact5NumericText | 241 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ExternalFinancialInstrumentIdentificationType1Code | 246 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}FinancialInstrumentAttributes112 | 252 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}FinancialInstrumentDetails47 | 297 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}FinancialInstrumentQuantity33Choice | 304 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ForeignExchangeTerms23 | 312 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}FormOfSecurity1Code | 320 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}FormOfSecurity6Choice | 326 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Frequency23Choice | 332 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Frequency25Choice | 338 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}GenericIdentification1 | 344 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}GenericIdentification30 | 351 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}GenericIdentification36 | 358 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}GenericIdentification37 | 365 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}GenericIdentification78 | 371 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ISINOct2015Identifier | 377 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ISODate | 382 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ISODateTime | 385 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}IdentificationSource3Choice | 388 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}ImpliedCurrencyAndAmount | 394 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}InterestComputationMethod2Code | 401 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}InterestComputationMethodFormat4Choice | 420 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}IntraPositionDetails66 | 426 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}IntraPositionMovementDetails21 | 433 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}IntraPositionMovementPostingReportV10 | 450 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}MICIdentifier | 460 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}MarketIdentification3Choice | 465 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Max140Text | 471 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Max16Text | 477 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Max30DecimalNumber | 483 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Max350Text | 489 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Max35Text | 495 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Max5NumericText | 501 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Max70Text | 506 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Number22Choice | 512 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Number3Choice | 518 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}OptionStyle2Code | 524 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}OptionStyle8Choice | 530 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}OptionType1Code | 536 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}OptionType6Choice | 542 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}OtherIdentification1 | 548 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Pagination1 | 555 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}PartyIdentification127Choice | 561 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}PercentageRate | 567 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Period2 | 573 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Period7Choice | 579 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Price7 | 585 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}PriceRateOrAmount3Choice | 591 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}PriceType4Choice | 597 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}PriceValueType1Code | 603 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}QuantityBreakdown60 | 610 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}References72Choice | 616 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SafekeepingPlace1Code | 626 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SafekeepingPlace3Code | 634 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SafekeepingPlaceFormat41Choice | 639 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SafekeepingPlaceTypeAndIdentification1 | 648 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SafekeepingPlaceTypeAndText8 | 654 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SecuritiesAccount19 | 660 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SecuritiesBalanceType11Code | 667 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SecuritiesBalanceType6Choice | 699 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SecuritiesPaymentStatus1Code | 705 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SecuritiesPaymentStatus5Choice | 712 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SecurityIdentification19 | 718 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}Statement80 | 725 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}StatementUpdateType1Code | 736 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SupplementaryData1 | 742 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}SupplementaryDataEnvelope1 | 748 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}UpdateType15Choice | 753 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}YesNoIndicator | 759 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.016.001.10}YieldedOrValueType1Choice | 762 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 24 |
| complexType | 54 |
| element | 181 |
| enumeration | 144 |
| extension | 3 |
| fractionDigits | 8 |
| maxLength | 6 |
| minInclusive | 4 |
| minLength | 6 |
| pattern | 12 |
| restriction | 43 |
| schema | 1 |
| sequence | 27 |
| simpleContent | 3 |
| simpleType | 43 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
