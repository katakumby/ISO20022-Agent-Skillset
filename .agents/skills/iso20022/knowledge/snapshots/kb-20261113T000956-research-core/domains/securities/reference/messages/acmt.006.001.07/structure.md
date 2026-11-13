---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.006.001.07"
message_family: "acmt.006"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07"
source_ids: ["src-000102"]
source_editions: ["2025-2026"]
---

# acmt.006.001.07 structure

[src-000102](../../../../../raw-input/investment_funds/acmt.006.001.07.xsd); `urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}AcceptedStatusReason1Choice | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}AcceptedStatusReason1Code | 11 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Account23 | 17 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}AccountManagementStatus1Code | 23 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}AccountManagementStatusAndReason5 | 31 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}AccountManagementStatusReportV07 | 44 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}AccountStatus2 | 53 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}AdditionalReference13 | 65 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}AddressType2Code | 72 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}AnyBICDec2014Identifier | 82 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}BlockedReason2Choice | 87 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}BlockedReason2Code | 93 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}BlockedStatusReason2 | 106 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}BlockedStatusReason2Choice | 114 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ClosedStatusReason1 | 120 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ClosedStatusReason1Choice | 126 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ClosedStatusReason1Code | 132 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ClosedStatusReason2Choice | 138 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ClosurePendingStatusReason1 | 144 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ClosurePendingStatusReason1Choice | 150 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ClosurePendingStatusReason1Code | 156 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ClosurePendingStatusReason2Choice | 162 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}CountryCode | 168 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}DisabledReason2Code | 173 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}DisabledStatusReason1 | 188 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}DisabledStatusReason1Choice | 194 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}DisabledStatusReason2Choice | 200 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Document | 206 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}EnabledStatusReason1 | 211 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}EnabledStatusReason1Choice | 217 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}EnabledStatusReason1Code | 223 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}EnabledStatusReason2Choice | 228 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Exact4AlphaNumericText | 234 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Extension1 | 239 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}GenericIdentification1 | 245 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}GenericIdentification36 | 252 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}GenericIdentification47 | 259 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ISODate | 266 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ISODateTime | 269 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ISOYearMonth | 272 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}InvestmentFundTransactionType1Code | 275 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}MarketPracticeVersion1 | 301 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Max16Text | 308 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Max350Text | 314 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Max35Text | 320 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Max4AlphaNumericText | 326 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Max70Text | 333 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}MessageIdentification1 | 339 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}NameAndAddress5 | 345 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}NoReasonCode | 351 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}OtherAccountStatus1 | 356 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PartyIdentification125Choice | 362 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PendingOpeningStatusReason1 | 369 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PendingOpeningStatusReason1Choice | 375 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PendingOpeningStatusReason1Code | 381 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PendingOpeningStatusReason2Choice | 392 |
| [type-0058](types/type-0058.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PendingStatusReason14 | 398 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PendingStatusReason1Choice | 404 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PendingStatusReason1Code | 410 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PendingStatusReason2Choice | 420 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}PostalAddress1 | 426 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ProformaStatusReason1 | 438 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ProformaStatusReason1Choice | 444 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ProformaStatusReason1Code | 450 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}ProformaStatusReason2Choice | 456 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}RejectedReason16Choice | 462 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}RejectedStatusReason6Code | 468 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}RejectionReason31 | 474 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}Status25Choice | 480 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}TransactionType5Choice | 486 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.006.001.07}YesNoIndicator | 492 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| choice | 21 |
| complexType | 45 |
| element | 120 |
| enumeration | 77 |
| maxLength | 5 |
| minLength | 5 |
| pattern | 4 |
| restriction | 26 |
| schema | 1 |
| sequence | 24 |
| simpleType | 26 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/217a3d119d8a04619017675f.md) · [Message](index.md)
