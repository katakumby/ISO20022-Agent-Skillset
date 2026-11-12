---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.013.001.07"
message_family: "semt.013"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.013.001.07"
source_ids: ["src-000201"]
source_editions: ["2025-2026"]
---

# semt.013.001.07 structure

[src-000201](../../../../../raw-input/settlement_and_reconciliation/semt.013.001.07.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.013.001.07`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.013.001.07 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ActiveOrHistoricCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ActiveOrHistoricCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}AnyBICDec2014Identifier | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}BaseOneRate | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}BlockChainAddressWallet3 | 35 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}CFIOct2015Identifier | 42 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ClassificationType32Choice | 47 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}CountryCode | 53 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}DTI2024Identifier | 58 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}DateAndDateTime2Choice | 63 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}DecimalNumber | 69 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Document | 75 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}DocumentNumber5Choice | 80 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}EventFrequency3Code | 87 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Exact3NumericText | 96 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Exact4AlphaNumericText | 101 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Exact4NumericText | 106 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ExternalFinancialInstrumentIdentificationType1Code | 111 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}FinancialInstrumentAttributes112 | 117 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}FinancialInstrumentQuantity33Choice | 162 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}FormOfSecurity1Code | 170 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}FormOfSecurity6Choice | 176 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Frequency23Choice | 182 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}GenericIdentification1 | 188 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}GenericIdentification30 | 195 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}GenericIdentification36 | 202 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}GenericIdentification37 | 209 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}GenericIdentification78 | 215 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ISINOct2015Identifier | 221 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ISO20022MessageIdentificationText | 226 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ISODate | 231 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ISODateTime | 234 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}IdentificationSource3Choice | 237 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ImpliedCurrencyAndAmount | 243 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}InterestComputationMethod2Code | 250 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}InterestComputationMethodFormat4Choice | 269 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}IntraPositionDetails58 | 275 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}IntraPositionMovementInstructionV07 | 286 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Linkages59 | 302 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}MICIdentifier | 310 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}MarketIdentification3Choice | 315 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Max140Text | 321 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Max16Text | 327 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Max30DecimalNumber | 333 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Max350Text | 339 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Max35Text | 345 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Max70Text | 351 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Number22Choice | 357 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}NumberCount1Choice | 363 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}OptionStyle2Code | 369 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}OptionStyle8Choice | 375 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}OptionType1Code | 381 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}OptionType6Choice | 387 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}OtherIdentification1 | 393 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}PartyIdentification127Choice | 400 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}PercentageRate | 406 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}Price7 | 412 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}PriceRateOrAmount3Choice | 418 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}PriceType4Choice | 424 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}PriceValueType1Code | 430 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}PriorityNumeric4Choice | 437 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ProcessingPosition3Code | 443 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}ProcessingPosition7Choice | 451 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}QuantityBreakdown60 | 457 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}QuantityBreakdown61 | 463 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}References41Choice | 470 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SafekeepingPlace1Code | 481 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SafekeepingPlace3Code | 489 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SafekeepingPlaceFormat41Choice | 494 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SafekeepingPlaceTypeAndIdentification1 | 503 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SafekeepingPlaceTypeAndText8 | 509 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SecuritiesAccount19 | 515 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SecuritiesBalanceType11Code | 522 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SecuritiesBalanceType6Choice | 554 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SecuritiesPaymentStatus1Code | 560 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SecuritiesPaymentStatus5Choice | 567 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SecuritiesSubBalanceTypeAndQuantityBreakdown5 | 573 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SecurityIdentification19 | 579 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SupplementaryData1 | 586 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}SupplementaryDataEnvelope1 | 592 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}TotalNumber1 | 597 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}YesNoIndicator | 603 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.013.001.07}YieldedOrValueType1Choice | 606 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 23 |
| complexType | 47 |
| element | 165 |
| enumeration | 69 |
| extension | 1 |
| fractionDigits | 6 |
| maxLength | 6 |
| minInclusive | 2 |
| minLength | 6 |
| pattern | 11 |
| restriction | 37 |
| schema | 1 |
| sequence | 23 |
| simpleContent | 1 |
| simpleType | 37 |
| totalDigits | 6 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
