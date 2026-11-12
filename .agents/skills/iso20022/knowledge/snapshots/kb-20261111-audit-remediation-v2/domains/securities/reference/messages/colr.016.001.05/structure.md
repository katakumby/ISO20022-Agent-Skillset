---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "colr.016.001.05"
message_family: "colr.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.016.001.05"
source_ids: ["src-000078"]
source_editions: []
---

# colr.016.001.05 structure

[src-000078](../../../../../raw-input/collateral_management_collateral_management/colr.016.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:colr.016.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:colr.016.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ActiveOrHistoricCurrencyCode | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Agreement4 | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}AgreementFramework1Choice | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}AgreementFramework1Code | 58 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}AnyBICDec2014Identifier | 67 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}BaseOneRate | 72 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}BlockChainAddressWallet3 | 78 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}BlockChainAddressWallet5 | 85 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CCPMemberType1Code | 92 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CashCollateral4 | 102 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Collateral53 | 115 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralAccount3 | 123 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralAccountIdentificationType3Choice | 130 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralAccountType1Code | 136 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralAmount1 | 145 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralAndExposureReportV05 | 154 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralAppliedExcess1Code | 164 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralDirection1Code | 170 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralOwnership3 | 176 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralType8Code | 182 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CollateralValuation13 | 199 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}CountryCode | 217 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}DateAndDateTime2Choice | 222 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}DateCode9Choice | 228 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}DateFormat14Choice | 234 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}DateType2Code | 240 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}DecimalNumber | 245 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}DepositType1Code | 251 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Document | 257 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}EventFrequency6Code | 262 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Exact4AlphaNumericText | 269 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ExposureType11Code | 274 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ExposureType13Code | 314 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ExternalFinancialInstrumentIdentificationType1Code | 363 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}FinancialInstrumentQuantity33Choice | 369 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}GenericIdentification30 | 377 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}GenericIdentification36 | 384 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}GenericIdentification78 | 391 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ISINOct2015Identifier | 397 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ISODate | 402 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ISODateTime | 405 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}IdentificationSource3Choice | 408 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ImpliedCurrencyAndAmount | 414 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}InterestComputationMethod2Code | 421 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Max140Text | 440 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Max16Text | 446 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Max30DecimalNumber | 452 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Max350Text | 458 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Max35Text | 464 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Max5NumericText | 470 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Max70Text | 475 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}NameAndAddress6 | 481 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Number | 487 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Obligation11 | 493 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}OtherCollateral10 | 505 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}OtherIdentification1 | 528 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}OtherTypeOfCollateral3 | 535 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Pagination1 | 541 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}PartyIdentification178Choice | 547 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}PartyIdentification242 | 554 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}PercentageRate | 560 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}PostalAddress2 | 566 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Price7 | 575 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}PriceRateOrAmount3Choice | 581 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}PriceValueType1Code | 587 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ReportParameters6 | 594 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ReturnExcessCash1 | 603 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ReturnExcessCash1Choice | 609 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ReturnExcessCash1Code | 615 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SafekeepingPlace1Code | 622 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SafekeepingPlace3Code | 630 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SafekeepingPlaceFormat29Choice | 635 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SafekeepingPlaceTypeAndIdentification1 | 643 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SafekeepingPlaceTypeAndText8 | 649 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SecuritiesAccount19 | 655 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SecuritiesCollateral13 | 662 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SecurityIdentification19 | 681 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SettlementStatus3Code | 688 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ShortLong1Code | 703 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}Summary3 | 709 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SummaryAmounts2 | 722 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SupplementaryData1 | 740 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}SupplementaryDataEnvelope1 | 746 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}ThresholdType1Code | 751 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}YesNoIndicator | 757 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.016.001.05}YieldedOrValueType1Choice | 760 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 12 |
| complexType | 48 |
| element | 195 |
| enumeration | 161 |
| extension | 2 |
| fractionDigits | 8 |
| maxLength | 6 |
| minInclusive | 3 |
| minLength | 6 |
| pattern | 7 |
| restriction | 43 |
| schema | 1 |
| sequence | 34 |
| simpleContent | 2 |
| simpleType | 43 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
