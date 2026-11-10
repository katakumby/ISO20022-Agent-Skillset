---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "semt.021.001.09"
message_family: "semt.021"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.021.001.09"
source_ids: ["src-000209"]
source_editions: ["2025-2026"]
---

# semt.021.001.09 structure

[src-000209](../../../../../raw-input/settlement_and_reconciliation/semt.021.001.09.xsd); `urn:iso:std:iso:20022:tech:xsd:semt.021.001.09`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:semt.021.001.09 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}AcknowledgementReason12Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}AcknowledgementReason13Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}AcknowledgementReason5Code | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}AdditionalQueryParameters15 | 30 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}AffirmationStatus1Code | 37 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}AffirmationStatus8Choice | 43 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}AllocationSatus3Choice | 49 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}AllocationStatus1Code | 55 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}AnyBICDec2014Identifier | 61 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}BlockChainAddressWallet3 | 66 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}CancellationProcessingStatus1Code | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}CancellationProcessingStatus7Choice | 86 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}CancellationReason20Choice | 92 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}CancelledStatusReason12Code | 98 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}CorporateActionEventProcessingStatus1Code | 113 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}CorporateActionEventProcessingStatus3Choice | 120 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}CorporateActionEventStage2Code | 126 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}CorporateActionEventStage3Choice | 137 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}DateAndDateTime2Choice | 143 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}DateAndPeriod3Choice | 149 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}DateTimePeriod1 | 155 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}DeniedReason14Choice | 161 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}DeniedReason7Code | 167 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Document | 184 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}DocumentNumber13 | 189 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}DocumentNumber5Choice | 194 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}EventFrequency4Code | 201 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Exact3NumericText | 211 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Exact4AlphaNumericText | 216 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}ExternalFinancialInstrumentIdentificationType1Code | 221 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}FailingReason1Code | 227 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}FailingReason9Choice | 289 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Frequency25Choice | 295 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}GeneratedReason3Code | 301 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}GeneratedReasons5Choice | 312 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}GenericIdentification30 | 318 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}GenericIdentification36 | 325 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}ISINOct2015Identifier | 332 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}ISO20022MessageIdentificationText | 337 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}ISODate | 342 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}ISODateTime | 345 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}IdentificationSource3Choice | 348 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}InstructionProcessingStatus1Code | 354 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}InstructionProcessingStatus23Choice | 390 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}LEIIdentifier | 396 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}MatchingStatus1Code | 401 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}MatchingStatus27Choice | 407 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Max140Text | 413 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Max16Text | 419 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Max350Text | 425 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Max35Text | 431 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Max70Text | 437 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}OtherIdentification1 | 443 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PartyIdentification127Choice | 450 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PartyIdentification144 | 456 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PendingCancellationReasons6Choice | 462 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PendingProcessingReason20Choice | 468 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PendingProcessingReason6Code | 474 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PendingReason28Choice | 497 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PendingReason33Code | 503 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PendingReason34Code | 574 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PendingReason6Code | 582 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}PendingReason78Choice | 592 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Period2 | 598 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Period7Choice | 604 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Reason21Choice | 610 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}RegistrationProcessingStatus1Code | 627 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}RegistrationProcessingStatus3Choice | 633 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}RejectionReason45Choice | 639 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}RejectionReason76Code | 645 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}RepairReason11Choice | 728 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}RepairReason6Code | 734 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}ReplacementProcessingStatus1Code | 784 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}ReplacementProcessingStatus8Choice | 797 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}RepoCallAcknowledgementReason2Code | 803 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}RepoCallRequestStatus1Code | 810 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}RepoCallRequestStatus8Choice | 816 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}ResponseStatus1Code | 822 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}ResponseStatus5Choice | 830 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SecuritiesAccount19 | 836 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SecuritiesSettlementStatus2Code | 843 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SecuritiesStatementQueryV09 | 852 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SecuritiesStatementType1Code | 863 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SecurityIdentification19 | 869 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SettlementConditionModificationStatus1Code | 876 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SettlementConditionModificationStatus3Choice | 885 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SettlementStatus19Choice | 891 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Statement83 | 897 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}StatementBasis1Code | 906 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}StatementBasis7Choice | 913 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}StatementType5Choice | 919 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}StatementUpdateType1Code | 925 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}Status19Choice | 931 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SupplementaryData1 | 949 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}SupplementaryDataEnvelope1 | 955 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}UnmatchedReason14Code | 960 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}UnmatchedReason22Choice | 1017 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:semt.021.001.09}UpdateType15Choice | 1023 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 38 |
| complexType | 54 |
| element | 144 |
| enumeration | 472 |
| maxLength | 6 |
| minLength | 6 |
| pattern | 6 |
| restriction | 44 |
| schema | 1 |
| sequence | 16 |
| simpleType | 44 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
