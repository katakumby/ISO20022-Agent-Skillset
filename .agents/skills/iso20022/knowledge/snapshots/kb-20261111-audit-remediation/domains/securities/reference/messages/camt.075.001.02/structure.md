---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "camt.075.001.02"
message_family: "camt.075"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.075.001.02"
source_ids: ["src-000248"]
source_editions: ["march-2024"]
---

# camt.075.001.02 structure

[src-000248](../../../../../raw-input/target2securities_t2s/camt.075.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.075.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.075.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AcknowledgedAcceptedStatus24Choice | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AcknowledgementReason12 | 23 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AcknowledgementReason15Choice | 29 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AcknowledgementReason3Code | 35 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ActiveCurrencyAndAmount_SimpleType | 42 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ActiveCurrencyAndAmount | 49 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ActiveCurrencyCode | 56 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ActiveOrHistoricCurrencyCode | 61 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AddressType2Code | 66 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AddressType3Choice | 76 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Amount2Choice | 82 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AmountAndDirection5 | 88 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AmountAndQuantityBreakdown1 | 94 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}AnyBICDec2014Identifier | 102 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}BICFIDec2014Identifier | 107 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}BranchAndFinancialInstitutionIdentification8 | 112 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}BranchData5 | 118 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CancellationReason10 | 126 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CancellationReason21Choice | 132 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CancellationStatus15Choice | 138 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CancelledStatusReason5Code | 144 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CashAccount40 | 150 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CashAccountType2Choice | 159 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CashBalanceType3Choice | 165 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CashSubBalanceTypeAndQuantityBreakdown3 | 171 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ClearingSystemIdentification2Choice | 177 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ClearingSystemMemberIdentification2 | 183 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CopyDuplicate1Code | 189 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CountryCode | 196 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}CreditDebitCode | 201 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}DateAndDateTime2Choice | 207 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}DecimalNumber | 213 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}DeniedReason11 | 219 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}DeniedReason16Choice | 225 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}DeniedReason4Code | 231 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}DeniedStatus16Choice | 245 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Document | 251 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}DocumentIdentification51 | 256 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Exact4AlphaNumericText | 265 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Exact4NumericText | 270 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ExternalAccountIdentification1Code | 275 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ExternalBalanceType1Code | 281 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ExternalCashAccountType1Code | 287 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ExternalClearingSystemIdentification1Code | 293 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ExternalFinancialInstitutionIdentification1Code | 299 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ExternalProxyAccountType1Code | 305 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}FinancialIdentificationSchemeName1Choice | 311 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}FinancialInstitutionIdentification23 | 317 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}FinancialInstrumentQuantity1Choice | 327 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}GenericAccountIdentification1 | 334 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}GenericFinancialIdentification1 | 341 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}GenericIdentification30 | 348 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}GenericIdentification36 | 355 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}GenericIdentification37 | 362 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}IBAN2007Identifier | 368 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ISODate | 373 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ISODateTime | 376 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ImpliedCurrencyAndAmount | 379 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}IntraBalance5 | 386 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}IntraBalanceMovementCancellationRequestStatusAdviceV02 | 397 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}LEIIdentifier | 410 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Max140Text | 415 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Max16Text | 421 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Max2048Text | 427 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Max210Text | 433 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Max34Text | 439 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Max350Text | 445 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Max35Text | 451 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}Max70Text | 457 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}NameAndAddress5 | 463 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}NoReasonCode | 469 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}PartyIdentification120Choice | 474 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}PartyIdentification136 | 481 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}PendingReason17 | 487 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}PendingReason30Choice | 493 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}PendingReason9Code | 499 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}PendingStatus39Choice | 511 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}PostalAddress1 | 517 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}PostalAddress27 | 529 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}PriorityNumeric4Choice | 551 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ProcessingStatus69Choice | 557 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ProprietaryReason4 | 568 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ProprietaryStatusAndReason6 | 574 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ProxyAccountIdentification1 | 580 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}ProxyAccountType1Choice | 586 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}References14 | 592 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}RejectionAndRepairReason33Choice | 601 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}RejectionOrRepairReason33 | 607 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}RejectionOrRepairStatus39Choice | 613 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}RejectionReason34Code | 619 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}SupplementaryData1 | 630 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}SupplementaryDataEnvelope1 | 636 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.075.001.02}SystemPartyIdentification8 | 641 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 24 |
| complexType | 58 |
| element | 174 |
| enumeration | 42 |
| extension | 1 |
| fractionDigits | 3 |
| maxLength | 14 |
| minInclusive | 2 |
| minLength | 14 |
| pattern | 9 |
| restriction | 37 |
| schema | 1 |
| sequence | 33 |
| simpleContent | 1 |
| simpleType | 37 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
