---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.039.001.08"
message_family: "sese.039"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.039.001.08"
source_ids: ["src-000230"]
source_editions: ["2025-2026"]
---

# sese.039.001.08 structure

[src-000230](../../../../../raw-input/settlement_and_reconciliation/sese.039.001.08.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.039.001.08`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.039.001.08 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}AcknowledgedAcceptedStatus23Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}AcknowledgementReason11 | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}AcknowledgementReason14Choice | 17 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}AcknowledgementReason6Code | 23 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ActiveCurrencyAndAmount_SimpleType | 32 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ActiveCurrencyAndAmount | 39 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ActiveCurrencyCode | 46 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ActiveOrHistoricCurrencyAndAmount_SimpleType | 51 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ActiveOrHistoricCurrencyAndAmount | 58 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ActiveOrHistoricCurrencyCode | 65 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}AddressType2Code | 70 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}AmountAndDirection51 | 80 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}AnyBICDec2014Identifier | 87 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}BlockChainAddressWallet3 | 92 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}CashSettlementSystemPlace1Choice | 99 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}CountryCode | 106 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}CreditDebitCode | 111 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DTI2024Identifier | 117 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DateAndDateTime2Choice | 122 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DateType3Code | 128 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DateType4Code | 133 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DecimalNumber | 139 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DeliveryReceiptType2Code | 145 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DeniedReason10 | 151 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DeniedReason15Choice | 157 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DeniedReason6Code | 163 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DeniedStatus15Choice | 177 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}DigitalPaymentSettlement2 | 183 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Document | 190 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Exact4AlphaNumericText | 195 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ExternalFinancialInstrumentIdentificationType1Code | 200 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}FinancialInstrumentQuantity33Choice | 206 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}GenericIdentification30 | 214 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}GenericIdentification36 | 221 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ISINOct2015Identifier | 228 |
| [type-0037](types/type-0037.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ISODate | 233 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ISODateTime | 236 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}IdentificationSource3Choice | 239 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ImpliedCurrencyAndAmount | 245 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}LEIIdentifier | 252 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Max140Text | 257 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Max16Text | 263 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Max210Text | 269 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Max30DecimalNumber | 275 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Max350Text | 281 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Max35Text | 287 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Max70Text | 293 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ModificationProcessingStatus12Choice | 299 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ModificationReason4 | 310 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ModificationReason4Choice | 316 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ModificationStatus6Choice | 322 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ModifiedStatusReason1Code | 328 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}NameAndAddress5 | 334 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}NoReasonCode | 340 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}OriginalAndCurrentQuantities1 | 345 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}OtherIdentification1 | 351 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PartyIdentification120Choice | 358 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PartyIdentification127Choice | 365 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PartyIdentification134Choice | 371 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PartyIdentification144 | 379 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PartyIdentification149 | 385 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PartyIdentification257Choice | 391 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PartyIdentification314 | 399 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PartyIdentificationAndAccount195 | 406 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PendingProcessingReason20 | 415 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PendingProcessingReason22Choice | 421 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PendingProcessingReason8Code | 427 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PendingProcessingStatus23Choice | 439 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}PostalAddress1 | 445 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ProprietaryReason4 | 457 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ProprietaryStatusAndReason6 | 463 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}Quantity51Choice | 469 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}ReceiveDelivery1Code | 475 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}RejectionReason42Choice | 481 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}RejectionReason57 | 487 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}RejectionReason72Code | 493 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}RejectionStatus37Choice | 532 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}RepairReason10Choice | 538 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}RepairReason4Code | 544 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}RepairReason9 | 577 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}RepairStatus13Choice | 583 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}SecuritiesAccount19 | 589 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 | 596 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}SecurityIdentification19 | 608 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}SettlementDate19Choice | 615 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}SettlementDateCode8Choice | 621 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}SettlementParties125 | 627 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}SupplementaryData1 | 637 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}SupplementaryDataEnvelope1 | 643 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}TradeDate8Choice | 648 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}TradeDateCode3Choice | 654 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}TransactionDetails182 | 660 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.039.001.08}TransactionIdentifications33 | 675 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 26 |
| complexType | 58 |
| element | 163 |
| enumeration | 105 |
| extension | 2 |
| fractionDigits | 5 |
| maxLength | 7 |
| minInclusive | 3 |
| minLength | 7 |
| pattern | 8 |
| restriction | 35 |
| schema | 1 |
| sequence | 30 |
| simpleContent | 2 |
| simpleType | 35 |
| totalDigits | 5 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
