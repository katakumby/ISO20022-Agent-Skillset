---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.020.001.09"
message_family: "sese.020"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.020.001.09"
source_ids: ["src-000211"]
source_editions: ["2025-2026"]
---

# sese.020.001.09 structure

[src-000211](../../../../../raw-input/settlement_and_reconciliation/sese.020.001.09.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.020.001.09`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.020.001.09 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ActiveCurrencyAndAmount_SimpleType | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ActiveCurrencyAndAmount | 12 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ActiveCurrencyCode | 19 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ActiveOrHistoricCurrencyAndAmount_SimpleType | 24 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ActiveOrHistoricCurrencyAndAmount | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ActiveOrHistoricCurrencyCode | 38 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}AddressType2Code | 43 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}AmountAndDirection51 | 53 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}AnyBICDec2014Identifier | 60 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}BlockChainAddressWallet3 | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}CancellationReason23 | 72 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}CancellationReason36Choice | 78 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}CancelledStatusReason16Code | 84 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}CashSettlementSystemPlace1Choice | 101 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}CountryCode | 108 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}CreditDebitCode | 113 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}DTI2024Identifier | 119 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}DateAndDateTime2Choice | 124 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}DateType3Code | 130 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}DecimalNumber | 135 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}DeliveryReceiptType2Code | 141 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}DigitalPaymentSettlement2 | 147 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Document | 154 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}DocumentNumber5Choice | 159 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Exact3NumericText | 166 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Exact4AlphaNumericText | 171 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ExternalFinancialInstrumentIdentificationType1Code | 176 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}FXCancellation3Choice | 182 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}FinancialInstrumentQuantity33Choice | 188 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}GenericDocumentIdentification4 | 196 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}GenericIdentification30 | 202 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}GenericIdentification36 | 209 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ISINOct2015Identifier | 216 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ISO20022MessageIdentificationText | 221 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ISODate | 226 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ISODateTime | 229 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}IdentificationSource3Choice | 232 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ImpliedCurrencyAndAmount | 238 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}LEIIdentifier | 245 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Max140Text | 250 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Max16Text | 256 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Max30DecimalNumber | 262 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Max350Text | 268 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Max35Text | 274 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Max70Text | 280 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}NameAndAddress5 | 286 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}OriginalAndCurrentQuantities1 | 292 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}OtherIdentification1 | 298 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}PartyIdentification120Choice | 305 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}PartyIdentification127Choice | 312 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}PartyIdentification134Choice | 318 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}PartyIdentification144 | 326 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}PartyIdentification149 | 332 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}PartyIdentification257Choice | 338 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}PartyIdentification314 | 346 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}PartyIdentificationAndAccount195 | 353 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}PostalAddress1 | 362 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}Quantity51Choice | 374 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}ReceiveDelivery1Code | 380 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}References45Choice | 386 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SecuritiesAccount19 | 394 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SecuritiesTransactionCancellationRequestV09 | 401 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SecurityIdentification19 | 417 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SettlementDate17Choice | 424 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SettlementDate4Code | 430 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SettlementDateCode7Choice | 435 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SettlementParties125 | 441 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SettlementTypeAndIdentification18 | 451 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SupplementaryData1 | 458 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}SupplementaryDataEnvelope1 | 464 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}TradeDate8Choice | 469 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}TradeDateCode3Choice | 475 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}TransactionDetails180 | 481 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.020.001.09}YesNoIndicator | 494 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 17 |
| complexType | 43 |
| element | 131 |
| enumeration | 25 |
| extension | 2 |
| fractionDigits | 5 |
| maxLength | 7 |
| minInclusive | 3 |
| minLength | 7 |
| pattern | 10 |
| restriction | 31 |
| schema | 1 |
| sequence | 24 |
| simpleContent | 2 |
| simpleType | 31 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
