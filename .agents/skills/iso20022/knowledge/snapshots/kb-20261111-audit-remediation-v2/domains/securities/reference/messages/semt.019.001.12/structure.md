---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.019.001.12"
message_family: "semt.019"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.019.001.12"
source_ids: ["src-000207"]
source_editions: ["2025-2026"]
---

# semt.019.001.12 structure

[src-000207](../../../../../raw-input/settlement_and_reconciliation/semt.019.001.12.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.019.001.12`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.019.001.12 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ActiveOrHistoricCurrencyAnd13DecimalAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ActiveOrHistoricCurrencyAndAmount_SimpleType | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ActiveOrHistoricCurrencyAndAmount | 45 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ActiveOrHistoricCurrencyCode | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}AddressType2Code | 57 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}AllegementStatus1Code | 67 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}AllegementStatus3Choice | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}AlternatePartyIdentification7 | 79 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}AmountAndDirection21 | 86 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}AmountAndDirection47 | 92 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}AmountAndDirection88 | 99 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}AnyBICDec2014Identifier | 108 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}BaseOneRate | 113 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}BeneficialOwnership4Choice | 119 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}BlockChainAddressWallet3 | 125 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}CFIOct2015Identifier | 132 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}CashAccountIdentification9Choice | 137 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}CashSettlementSystem3Code | 144 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}CashSettlementSystem6Choice | 151 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}CashSettlementSystemPlace1Choice | 157 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ClassificationType32Choice | 164 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}CountryCode | 170 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}CreditDebitCode | 175 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}DTI2024Identifier | 181 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}DateAndDateTime2Choice | 186 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}DateCode18Choice | 192 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}DateType3Code | 198 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}DateType5Code | 203 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}DecimalNumber | 208 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}DeliveryReceiptType2Code | 214 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}DigitalPaymentSettlement1 | 220 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Document | 227 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}EventFrequency3Code | 232 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}EventFrequency4Code | 241 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Exact3NumericText | 251 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Exact4AlphaNumericText | 256 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Exact5NumericText | 261 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ExternalFinancialInstrumentIdentificationType1Code | 266 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}FinancialInstrumentAttributes111 | 272 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}FinancialInstrumentQuantity33Choice | 316 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ForeignExchangeTerms23 | 324 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}FormOfSecurity1Code | 332 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}FormOfSecurity6Choice | 338 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Frequency23Choice | 344 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Frequency25Choice | 350 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}GenericIdentification1 | 356 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}GenericIdentification30 | 363 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}GenericIdentification36 | 370 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}GenericIdentification37 | 377 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}GenericIdentification78 | 383 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}IBAN2007Identifier | 389 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ISINOct2015Identifier | 394 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ISODate | 399 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ISODateTime | 402 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}IdentificationSource3Choice | 405 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}IdentificationType42Choice | 411 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ImpliedCurrencyAndAmount | 417 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}InterestComputationMethod2Code | 424 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}InterestComputationMethodFormat4Choice | 443 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}LEIIdentifier | 449 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}LegalFramework1Code | 454 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}LegalFramework3Choice | 459 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}MICIdentifier | 465 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}MarketClientSide1Code | 470 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}MarketClientSide6Choice | 476 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}MarketIdentification1Choice | 482 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}MarketIdentification3Choice | 488 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}MarketIdentification84 | 494 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}MarketType2Code | 500 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}MarketType8Choice | 509 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max140Text | 515 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max16Text | 521 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max210Text | 527 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max30DecimalNumber | 533 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max34Text | 539 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max350Text | 545 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max35Text | 551 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max3Number | 557 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max5NumericText | 563 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max70Text | 568 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Max8Text | 574 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}NameAndAddress5 | 580 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Number22Choice | 586 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Number3Choice | 592 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}OptionStyle2Code | 598 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}OptionStyle8Choice | 604 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}OptionType1Code | 610 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}OptionType6Choice | 616 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}OtherAmounts32 | 622 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}OtherIdentification1 | 637 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}OtherParties34 | 644 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Pagination1 | 653 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyIdentification120Choice | 659 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyIdentification127Choice | 666 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyIdentification134Choice | 672 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyIdentification136 | 680 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyIdentification144 | 686 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyIdentification149 | 692 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyIdentification257Choice | 698 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyIdentification315 | 706 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyIdentificationAndAccount196 | 716 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PartyTextInformation1 | 728 |
| [type-0108](types/type-0108.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PercentageRate | 735 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PlaceOfClearingIdentification2 | 741 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PlaceOfTradeIdentification1 | 747 |
| [type-0111](types/type-0111.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PlusOrMinusIndicator | 753 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PostalAddress1 | 756 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Price10 | 768 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Price7 | 774 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PriceRateOrAmount3Choice | 780 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PriceType4Choice | 786 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PriceValueType12Code | 792 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}PriceValueType1Code | 800 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Quantity83Choice | 807 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}QuantityAndAccount114 | 813 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}QuantityBreakdown62 | 822 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Rate2 | 831 |
| [type-0123](types/type-0123.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}RateName1 | 837 |
| [type-0124](types/type-0124.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}RateType1Code | 843 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}RateType35Choice | 850 |
| [type-0126](types/type-0126.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}ReceiveDelivery1Code | 856 |
| [type-0127](types/type-0127.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Registration1Code | 862 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Registration9Choice | 868 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}RepurchaseType13Choice | 874 |
| [type-0130](types/type-0130.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}RepurchaseType6Code | 880 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SafeKeepingPlace5 | 887 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SafekeepingPlace1Code | 893 |
| [type-0133](types/type-0133.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SafekeepingPlace3Code | 901 |
| [type-0134](types/type-0134.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SafekeepingPlaceFormat41Choice | 906 |
| [type-0135](types/type-0135.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SafekeepingPlaceTypeAndIdentification1 | 915 |
| [type-0136](types/type-0136.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SafekeepingPlaceTypeAndText8 | 921 |
| [type-0137](types/type-0137.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecuritiesAccount19 | 927 |
| [type-0138](types/type-0138.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecuritiesFinancingTransactionDetails54 | 934 |
| [type-0139](types/type-0139.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecuritiesPaymentStatus1Code | 952 |
| [type-0140](types/type-0140.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecuritiesPaymentStatus5Choice | 959 |
| [type-0141](types/type-0141.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecuritiesRTGS4Choice | 965 |
| [type-0142](types/type-0142.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecuritiesSettlementTransactionAllegementReportV12 | 971 |
| [type-0143](types/type-0143.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecuritiesTradeDetails152 | 981 |
| [type-0144](types/type-0144.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecuritiesTransactionType24Code | 1018 |
| [type-0145](types/type-0145.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecuritiesTransactionType45Choice | 1059 |
| [type-0146](types/type-0146.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SecurityIdentification19 | 1065 |
| [type-0147](types/type-0147.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SettlementDate17Choice | 1072 |
| [type-0148](types/type-0148.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SettlementDate4Code | 1078 |
| [type-0149](types/type-0149.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SettlementDateCode7Choice | 1083 |
| [type-0150](types/type-0150.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SettlementDetails234 | 1089 |
| [type-0151](types/type-0151.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SettlementParties126 | 1104 |
| [type-0152](types/type-0152.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SettlementTransactionCondition22Code | 1114 |
| [type-0153](types/type-0153.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SettlementTransactionCondition46Choice | 1126 |
| [type-0154](types/type-0154.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SettlementTransactionCondition5Code | 1132 |
| [type-0155](types/type-0155.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}Statement63 | 1140 |
| [type-0156](types/type-0156.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}StatementUpdateType1Code | 1151 |
| [type-0157](types/type-0157.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SupplementaryData1 | 1157 |
| [type-0158](types/type-0158.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}SupplementaryDataEnvelope1 | 1163 |
| [type-0159](types/type-0159.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}TerminationDate6Choice | 1168 |
| [type-0160](types/type-0160.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}TradeDate8Choice | 1174 |
| [type-0161](types/type-0161.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}TradeDateCode3Choice | 1180 |
| [type-0162](types/type-0162.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}TradeTransactionCondition4Code | 1186 |
| [type-0163](types/type-0163.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}TradeTransactionCondition5Choice | 1212 |
| [type-0164](types/type-0164.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}TypeOfIdentification1Code | 1218 |
| [type-0165](types/type-0165.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}TypeOfPrice14Code | 1229 |
| [type-0166](types/type-0166.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}TypeOfPrice29Choice | 1234 |
| [type-0167](types/type-0167.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}UTIIdentifier | 1240 |
| [type-0168](types/type-0168.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}UpdateType15Choice | 1245 |
| [type-0169](types/type-0169.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}YesNoIndicator | 1251 |
| [type-0170](types/type-0170.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}YieldedOrValueType1Choice | 1254 |
| [type-0171](types/type-0171.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.019.001.12}YieldedOrValueType2Choice | 1260 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 3 |
| choice | 49 |
| complexType | 100 |
| element | 357 |
| enumeration | 164 |
| extension | 3 |
| fractionDigits | 9 |
| maxLength | 9 |
| minInclusive | 4 |
| minLength | 9 |
| pattern | 15 |
| restriction | 70 |
| schema | 1 |
| sequence | 48 |
| simpleContent | 3 |
| simpleType | 70 |
| totalDigits | 9 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
