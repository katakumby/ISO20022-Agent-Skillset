---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.040.001.06"
message_family: "sese.040"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.040.001.06"
source_ids: ["src-000231"]
source_editions: ["2025-2026"]
---

# sese.040.001.06 structure

[src-000231](../../../../../raw-input/settlement_and_reconciliation/sese.040.001.06.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.040.001.06`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.040.001.06 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ActiveOrHistoricCurrencyAndAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ActiveOrHistoricCurrencyAndAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ActiveOrHistoricCurrencyCode | 38 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}AddressType2Code | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}AmountAndDirection51 | 53 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}AnyBICDec2014Identifier | 60 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}BlockChainAddressWallet3 | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}CashSettlementSystemPlace1Choice | 72 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ConsentOrRejectionReason4Choice | 79 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ConsentReason4 | 85 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ConsentStatus4Choice | 91 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}CounterpartyResponseStatusReason1Code | 97 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}CountryCode | 104 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}CreditDebitCode | 109 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}DTI2024Identifier | 115 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}DateAndDateTime2Choice | 120 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}DateType3Code | 126 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}DateType4Code | 131 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}DecimalNumber | 137 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}DeliveryReceiptType2Code | 143 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}DigitalPaymentSettlement2 | 149 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Document | 156 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Exact4AlphaNumericText | 161 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ExternalFinancialInstrumentIdentificationType1Code | 166 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}FinancialInstrumentQuantity33Choice | 172 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}GenericIdentification30 | 180 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}GenericIdentification36 | 187 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ISINOct2015Identifier | 194 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ISODate | 199 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ISODateTime | 202 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}IdentificationSource3Choice | 205 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ImpliedCurrencyAndAmount | 211 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}LEIIdentifier | 218 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Max140Text | 223 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Max16Text | 229 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Max210Text | 235 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Max30DecimalNumber | 241 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Max350Text | 247 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Max35Text | 253 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Max70Text | 259 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}NameAndAddress5 | 265 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}NoReasonCode | 271 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}NoSpecifiedReason1 | 276 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}OriginalAndCurrentQuantities1 | 281 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}OtherIdentification1 | 287 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}PartyIdentification120Choice | 294 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}PartyIdentification134Choice | 301 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}PartyIdentification149 | 309 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}PartyIdentification257Choice | 315 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}PartyIdentification314 | 323 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}PartyIdentificationAndAccount195 | 330 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}PendingStatus20Choice | 339 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}PostalAddress1 | 345 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}Quantity51Choice | 357 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ReceiveDelivery1Code | 363 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}RejectionReason29 | 369 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}RejectionStatus20Choice | 375 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}ResponseStatus6Choice | 381 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}SecuritiesAccount19 | 388 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}SecuritiesSettlementTransactionCounterpartyResponseV06 | 395 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}SecurityIdentification19 | 403 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}SettlementDate19Choice | 410 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}SettlementDateCode8Choice | 416 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}SettlementParties125 | 422 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}SupplementaryData1 | 432 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}SupplementaryDataEnvelope1 | 438 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}TradeDate8Choice | 443 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}TradeDateCode3Choice | 449 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}TransactionDetails183 | 455 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.040.001.06}TransactionIdentification6 | 472 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 17 |
| complexType | 43 |
| element | 125 |
| enumeration | 19 |
| extension | 2 |
| fractionDigits | 5 |
| maxLength | 7 |
| minInclusive | 3 |
| minLength | 7 |
| pattern | 8 |
| restriction | 30 |
| schema | 1 |
| sequence | 24 |
| simpleContent | 2 |
| simpleType | 30 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
