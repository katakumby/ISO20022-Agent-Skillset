---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "camt.081.001.02"
message_family: "camt.081"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.081.001.02"
source_ids: ["src-000254"]
source_editions: ["march-2024"]
---

# camt.081.001.02 structure

[src-000254](../../../../../raw-input/target2securities_t2s/camt.081.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:camt.081.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:camt.081.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AcknowledgedAcceptedStatus21Choice | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AcknowledgementReason12Choice | 23 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AcknowledgementReason5Code | 29 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AcknowledgementReason9 | 42 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ActiveCurrencyAndAmount_SimpleType | 48 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ActiveCurrencyAndAmount | 55 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ActiveCurrencyCode | 62 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ActiveOrHistoricCurrencyCode | 67 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AddressType2Code | 72 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AddressType3Choice | 82 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Amount2Choice | 88 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AmountAndDirection5 | 94 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AmountAndQuantityBreakdown1 | 100 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}AnyBICDec2014Identifier | 108 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}BICFIDec2014Identifier | 113 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}BranchAndFinancialInstitutionIdentification8 | 118 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}BranchData5 | 124 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}CashAccount40 | 132 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}CashAccountType2Choice | 141 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}CashBalanceType3Choice | 147 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}CashSubBalanceTypeAndQuantityBreakdown3 | 153 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ClearingChannel2Code | 159 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ClearingSystemIdentification2Choice | 167 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ClearingSystemMemberIdentification2 | 173 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}CopyDuplicate1Code | 179 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}CountryCode | 186 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}CreditDebitCode | 191 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}DateAndDateTime2Choice | 197 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}DateTimePeriod1 | 203 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}DecimalNumber | 209 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}DeniedReason11 | 215 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}DeniedReason16Choice | 221 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}DeniedReason4Code | 227 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}DeniedStatus16Choice | 241 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Document | 247 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}DocumentIdentification51 | 252 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}DocumentNumber5Choice | 261 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ErrorHandling3Choice | 268 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ErrorHandling5 | 274 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}EventFrequency7Code | 280 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Exact3NumericText | 297 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Exact4AlphaNumericText | 302 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Exact4NumericText | 307 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Exact5NumericText | 312 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ExternalAccountIdentification1Code | 317 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ExternalBalanceType1Code | 323 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ExternalCashAccountType1Code | 329 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ExternalClearingSystemIdentification1Code | 335 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ExternalFinancialInstitutionIdentification1Code | 341 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ExternalProxyAccountType1Code | 347 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ExternalSystemErrorHandling1Code | 353 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}FinancialIdentificationSchemeName1Choice | 359 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}FinancialInstitutionIdentification23 | 365 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}FinancialInstrumentQuantity1Choice | 375 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Frequency22Choice | 382 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}GenericAccountIdentification1 | 388 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}GenericFinancialIdentification1 | 395 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}GenericIdentification30 | 402 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}GenericIdentification36 | 409 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}GenericIdentification37 | 416 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}IBAN2007Identifier | 422 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ISO20022MessageIdentificationText | 427 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ISODate | 432 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ISODateTime | 435 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ImpliedCurrencyAndAmount | 438 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}IntraBalance5 | 445 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}IntraBalanceModification7 | 456 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}IntraBalanceModification8 | 465 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}IntraBalanceMovementModificationReportV02 | 477 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}IntraBalanceOrOperationalError12Choice | 486 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}IntraBalanceReport5 | 492 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}LEIIdentifier | 505 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}LinkageType1Code | 510 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}LinkageType3Choice | 517 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Linkages57 | 523 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Max140Text | 531 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Max16Text | 537 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Max2048Text | 543 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Max210Text | 549 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Max34Text | 555 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Max350Text | 561 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Max35Text | 567 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Max5NumericText | 573 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Max70Text | 578 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}MovementResponseType1Code | 584 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}NameAndAddress5 | 590 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}NoReasonCode | 596 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Number3Choice | 601 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Pagination1 | 607 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PartyIdentification120Choice | 613 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PartyIdentification127Choice | 620 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PartyIdentification136 | 626 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PendingReason16 | 632 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PendingReason28Choice | 638 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PendingReason6Code | 644 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PendingStatus38Choice | 654 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Period2 | 660 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}Period7Choice | 666 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PostalAddress1 | 672 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PostalAddress27 | 684 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}PriorityNumeric4Choice | 706 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ProcessingPosition3Code | 712 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ProcessingPosition7Choice | 720 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ProcessingStatus71Choice | 726 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ProprietaryReason4 | 737 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ProprietaryStatusAndReason6 | 743 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ProxyAccountIdentification1 | 749 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}ProxyAccountType1Choice | 755 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}References14 | 761 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}References34Choice | 770 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}RejectionAndRepairReason33Choice | 781 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}RejectionAndRepairReason34Choice | 787 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}RejectionOrRepairReason33 | 793 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}RejectionOrRepairReason34 | 799 |
| [type-0118](types/type-0118.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}RejectionOrRepairStatus39Choice | 805 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}RejectionOrRepairStatus40Choice | 811 |
| [type-0120](types/type-0120.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}RejectionReason34Code | 817 |
| [type-0121](types/type-0121.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}RejectionReason35Code | 828 |
| [type-0122](types/type-0122.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}RequestDetails22 | 841 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}StatementUpdateType1Code | 852 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}SupplementaryData1 | 858 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}SupplementaryDataEnvelope1 | 864 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}SystemPartyIdentification8 | 869 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}UpdateType15Choice | 875 |
| [type-0128](types/type-0128.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:camt.081.001.02}YesNoIndicator | 881 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 1 |
| choice | 35 |
| complexType | 78 |
| element | 239 |
| enumeration | 81 |
| extension | 1 |
| fractionDigits | 3 |
| maxLength | 15 |
| minInclusive | 2 |
| minLength | 15 |
| pattern | 13 |
| restriction | 49 |
| schema | 1 |
| sequence | 42 |
| simpleContent | 1 |
| simpleType | 49 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
