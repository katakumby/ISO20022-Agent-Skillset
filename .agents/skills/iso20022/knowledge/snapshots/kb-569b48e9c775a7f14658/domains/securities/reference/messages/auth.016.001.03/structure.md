---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "auth.016.001.03"
message_family: "auth.016"
namespace: "urn:iso:std:iso:20022:tech:xsd:auth.016.001.03"
source_ids: ["src-000323"]
source_editions: ["2025"]
---

# auth.016.001.03 structure

[src-000323](../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/auth.016.001.03.xsd); `urn:iso:std:iso:20022:tech:xsd:auth.016.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:auth.016.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ActiveCurrencyAnd13DecimalAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ActiveCurrencyAnd13DecimalAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ActiveOrHistoricCurrencyAndAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ActiveOrHistoricCurrencyAndAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ActiveOrHistoricCurrencyCode | 38 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}AmountAndDirection53 | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}AmountAndDirection61 | 49 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}AssetClassAttributes1 | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}AssetClassAttributes1Choice | 61 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}BasketDescription3 | 68 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}BenchmarkCurveName2Code | 74 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}BenchmarkCurveName5Choice | 104 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}CFIOct2015Identifier | 110 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}CancelledStatusReason15Code | 115 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}CountryCode | 121 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}DTI2021Identifier | 126 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}DebtInstrument4 | 131 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}DecimalNumber | 136 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}DerivativeForeignExchange2 | 142 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}DerivativeInstrument6 | 147 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}DerivativeInterest2 | 159 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}DigitalTokenAmount2 | 164 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Document | 171 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ExecutingParty1Choice | 176 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ExternalAuthorityExchangeReason1Code | 183 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ExternalFinancialInstrumentIdentificationType1Code | 189 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ExternalPersonIdentification1Code | 195 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}FinancialInstrument58 | 201 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}FinancialInstrumentAttributes5Choice | 207 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}FinancialInstrumentIdentification6Choice | 214 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}FinancialInstrumentIdentification7Choice | 220 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}FinancialInstrumentQuantity25Choice | 226 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}FinancialInstrumentReportingTransactionReportV03 | 233 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}FloatingInterestRate8 | 239 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}GenericPersonIdentification1 | 245 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ISINOct2015Identifier | 252 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ISODate | 257 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ISODateTime | 260 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}IdentificationSource3Choice | 263 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ImpliedCurrencyAndAmount | 269 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}InterestRateContractTerm2 | 276 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}InternalPartyRole1Code | 282 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}InvestmentParty1Choice | 287 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}LEIIdentifier | 293 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}MICIdentifier | 298 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max140Text | 303 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max16Text | 309 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max25Text | 315 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max30DecimalNumber | 321 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max30Text | 327 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max350Text | 332 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max35Text | 338 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max3Number | 344 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max50Text | 350 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Max52Text | 356 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}NoReasonCode | 362 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}NonNegativeDecimalNumber | 367 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}OptionStyle7Code | 374 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}OptionType2Code | 383 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}OtherIdentification1 | 390 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PartyIdentification76 | 397 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PartyIdentification79 | 403 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PercentageRate | 409 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PersonIdentification10 | 415 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PersonIdentification12 | 423 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PersonIdentificationSchemeName1Choice | 429 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PersonOrOrganisation1Choice | 435 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PersonOrOrganisation2Choice | 443 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PhysicalTransferType4Code | 449 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PlusOrMinusIndicator | 456 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}PriceStatus1Code | 459 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}RateBasis1Code | 465 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}RecordTechnicalData2 | 473 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}RecordTechnicalData5 | 479 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}RegulatoryTradingCapacity1Code | 485 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ReportingTransactionType3Choice | 492 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ReportingWaiverType1Code | 499 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}ReportingWaiverType3Code | 509 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransaction3 | 526 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionIndicator2 | 542 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionPrice1 | 551 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionPrice22Choice | 557 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionPrice2Choice | 564 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionPrice4Choice | 572 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionPrice6 | 578 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionPrice7 | 585 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionReport2 | 591 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionReport7 | 600 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecuritiesTransactionTransmission2 | 618 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecurityIdentification19 | 625 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecurityInstrumentDescription22 | 632 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SecurityInstrumentDescription23 | 639 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}Side5Code | 648 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SupplementaryData1 | 656 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SupplementaryDataEnvelope1 | 662 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}SwapLegIdentification2 | 667 |
| [type-0099](types/type-0099.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}TrueFalseIndicator | 673 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}UnderlyingIdentification2Choice | 676 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:auth.016.001.03}VariationType1Code | 682 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 17 |
| complexType | 55 |
| element | 157 |
| enumeration | 75 |
| extension | 2 |
| fractionDigits | 8 |
| maxLength | 11 |
| minInclusive | 4 |
| minLength | 10 |
| pattern | 8 |
| restriction | 45 |
| schema | 1 |
| sequence | 36 |
| simpleContent | 2 |
| simpleType | 45 |
| totalDigits | 8 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
