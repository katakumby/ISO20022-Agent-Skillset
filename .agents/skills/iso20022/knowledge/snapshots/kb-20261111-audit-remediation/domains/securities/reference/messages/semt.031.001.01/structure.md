---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.031.001.01"
message_family: "semt.031"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.031.001.01"
source_ids: ["src-000314"]
source_editions: ["september-2025"]
---

# semt.031.001.01 structure

[src-000314](../../../../../raw-input/target2securities_t2s/semt.031.001.01.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.031.001.01`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.031.001.01 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}AcknowledgedAcceptedStatus21Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}AcknowledgementReason12Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}AcknowledgementReason5Code | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}AcknowledgementReason9 | 30 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ActiveCurrencyAndAmount_SimpleType | 36 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ActiveCurrencyAndAmount | 43 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ActiveCurrencyCode | 50 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ActiveOrHistoricCurrencyAndAmount_SimpleType | 55 |
| [type-0010](types/type-0010.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ActiveOrHistoricCurrencyAndAmount | 62 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ActiveOrHistoricCurrencyCode | 69 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}AddressType2Code | 74 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}AmountAndDirection51 | 84 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}AnyBICDec2014Identifier | 91 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}AutoBorrowing2Code | 96 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}AutomaticBorrowing7Choice | 104 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}CountryCode | 110 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}CreditDebitCode | 115 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}DateAndDateTime2Choice | 121 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}DateTimePeriod1 | 127 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}DateType3Code | 133 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}DecimalNumber | 138 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}DeniedReason11 | 144 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}DeniedReason16Choice | 150 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}DeniedReason4Code | 156 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}DeniedStatus16Choice | 170 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Document | 176 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}DocumentNumber5Choice | 181 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}EventFrequency7Code | 188 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Exact3NumericText | 205 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Exact4AlphaNumericText | 210 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Exact4NumericText | 215 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Exact5NumericText | 220 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ExternalFinancialInstrumentIdentificationType1Code | 225 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}FinancialInstrumentQuantity1Choice | 231 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Frequency22Choice | 238 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}GenericIdentification30 | 244 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}GenericIdentification36 | 251 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}GenericIdentification37 | 258 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}HoldIndicator6 | 264 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ISINOct2015Identifier | 270 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ISO20022MessageIdentificationText | 275 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ISODate | 280 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ISODateTime | 283 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}IdentificationSource3Choice | 286 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ImpliedCurrencyAndAmount | 292 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}IntraPosition6 | 299 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}LEIIdentifier | 310 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}LinkageType1Code | 315 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}LinkageType3Choice | 322 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Linkages57 | 328 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}MatchingDenied3Choice | 336 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}MatchingProcess1Code | 342 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Max140Text | 348 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Max16Text | 354 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Max210Text | 360 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Max350Text | 366 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Max35Text | 372 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Max52Text | 378 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Max5NumericText | 384 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Max70Text | 389 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}MovementResponseType1Code | 395 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}NameAndAddress5 | 401 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}NoReasonCode | 407 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Number3Choice | 412 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}OriginalAndCurrentQuantities1 | 418 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}OtherIdentification1 | 424 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Pagination1 | 431 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PartyIdentification120Choice | 437 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PartyIdentification122Choice | 444 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PartyIdentification127Choice | 451 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PartyIdentification136 | 457 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PartyIdentification148 | 463 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PartyIdentificationAndAccount170 | 470 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PendingReason16 | 478 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PendingReason28Choice | 484 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PendingReason6Code | 490 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PendingStatus38Choice | 500 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Period2 | 506 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Period7Choice | 512 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PostalAddress1 | 518 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}PriorityNumeric4Choice | 530 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ProcessingPosition3Code | 536 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ProcessingPosition7Choice | 544 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ProcessingStatus71Choice | 550 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ProprietaryReason4 | 561 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}ProprietaryStatusAndReason6 | 567 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Quantity6Choice | 573 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}QuantityBreakdown32 | 579 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}References32 | 586 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}References34Choice | 598 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Registration10Choice | 609 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}Registration2Code | 615 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RegistrationReason5 | 623 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RejectionAndRepairReason33Choice | 629 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RejectionAndRepairReason34Choice | 635 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RejectionOrRepairReason33 | 641 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RejectionOrRepairReason34 | 647 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RejectionOrRepairStatus39Choice | 653 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RejectionOrRepairStatus40Choice | 659 |
| [type-0101](types/type-0101.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RejectionReason34Code | 665 |
| [type-0102](types/type-0102.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RejectionReason35Code | 676 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RequestDetails33 | 689 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RestrictionIdentification1 | 706 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}RestrictionReference1Code | 712 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesAccount19 | 722 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesBalanceType11Code | 729 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesBalanceType6Choice | 761 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesModification2 | 767 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesModificationTransaction2 | 775 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesRTGS4Choice | 786 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesSettlementConditionsModificationRequestReportV01 | 792 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesSubBalanceTypeAndQuantityBreakdown3 | 800 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesTransactionReport5 | 806 |
| [type-0115](types/type-0115.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecuritiesTransactionType5Code | 819 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SecurityIdentification19 | 824 |
| [type-0117](types/type-0117.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SettlementDate17Choice | 831 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SettlementDate4Code | 837 |
| [type-0119](types/type-0119.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SettlementDateCode7Choice | 842 |
| [type-0120](types/type-0120.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SettlementOrIntraPosition3Choice | 848 |
| [type-0121](types/type-0121.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SettlementParties78 | 854 |
| [type-0122](types/type-0122.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SettlementTransactionCondition5Code | 864 |
| [type-0123](types/type-0123.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}StatementUpdateType1Code | 872 |
| [type-0124](types/type-0124.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SupplementaryData1 | 878 |
| [type-0125](types/type-0125.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SupplementaryDataEnvelope1 | 884 |
| [type-0126](types/type-0126.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}SystemPartyIdentification8 | 889 |
| [type-0127](types/type-0127.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}TradeDate8Choice | 895 |
| [type-0128](types/type-0128.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}TradeDateCode3Choice | 901 |
| [type-0129](types/type-0129.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}TransactionDetails126 | 907 |
| [type-0130](types/type-0130.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}UnilateralSplit3Choice | 918 |
| [type-0131](types/type-0131.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}UpdateType15Choice | 924 |
| [type-0132](types/type-0132.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.031.001.01}YesNoIndicator | 930 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 38 |
| complexType | 82 |
| element | 237 |
| enumeration | 123 |
| extension | 2 |
| fractionDigits | 4 |
| maxLength | 9 |
| minInclusive | 3 |
| minLength | 9 |
| pattern | 12 |
| restriction | 49 |
| schema | 1 |
| sequence | 42 |
| simpleContent | 2 |
| simpleType | 49 |
| totalDigits | 4 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
