---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "sese.009.001.09"
message_family: "sese.009"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.009.001.09"
source_ids: ["src-000128"]
source_editions: ["2025-2026"]
---

# sese.009.001.09 structure

[src-000128](../../../../../raw-input/investment_funds/sese.009.001.09.xsd); `urn:iso:std:iso:20022:tech:xsd:sese.009.001.09`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:sese.009.001.09 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Account34 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Account36 | 14 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ActiveCurrencyCode | 26 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}AdditionalInformation15 | 31 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}AdditionalInformation25 | 37 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}AdditionalReference10 | 45 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}AddressType2Code | 52 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}AlternateSecurityIdentification7 | 62 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}AnyBICDec2014Identifier | 68 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}AustrianBankleitzahlIdentifier | 73 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}BelgianIdentifier | 78 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}BlockChainAddressWallet3 | 81 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Bloomberg2Identifier | 88 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}CFIOct2015Identifier | 93 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}CHIPSParticipantIdentifier | 98 |
| [type-0017](types/type-0017.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}CHIPSUniversalIdentifier | 103 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}CUSIPIdentifier | 108 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}CanadianPaymentsARNIdentifier | 111 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}CashAsset3 | 116 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}CashAssetType1Choice | 124 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}CashAssetType1Code | 130 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ClassificationType32Choice | 136 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ClearingSystemMemberIdentification2Choice | 142 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ConsolidatedTapeAssociationIdentifier | 169 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ContactIdentification2 | 175 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}CountryCode | 186 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}DTI2024Identifier | 191 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Document | 196 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}DutchIdentifier | 201 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}EuroclearClearstreamIdentifier | 204 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Exact4AlphaNumericText | 210 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Extension1 | 215 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ExtensiveBranchNetworkIdentifier | 221 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}FedwireRoutingNumberIdentifier | 226 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}FinancialInstrument101Choice | 231 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}FinancialInstrumentIdentification6 | 238 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}GenericIdentification1 | 246 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}GenericIdentification30 | 253 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}GenericIdentification36 | 260 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}GermanBankleitzahlIdentifier | 267 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}HellenicBankIdentificationCodeIdentifier | 272 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}HongKongBankIdentifier | 277 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ISINOct2015Identifier | 282 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ISODateTime | 287 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ISOYearMonth | 290 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}IdentificationSource1Choice | 293 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}IndianFinancialSystemCodeIdentifier | 299 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Intermediary48 | 304 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}InvestmentFundRole8Code | 312 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}IrishNSCIdentifier | 330 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ItalianDomesticIdentifier | 335 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}LEIIdentifier | 340 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}MarketPracticeVersion1 | 345 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Max140Text | 352 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Max16Text | 358 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Max256Text | 364 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Max350Text | 370 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Max35Text | 376 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Max70Text | 382 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}MessageAndBusinessReference14 | 388 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}MessageIdentification1 | 404 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}NameAndAddress5 | 410 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}NamePrefix1Code | 416 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}NewZealandNCCIdentifier | 424 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}OtherAsset2 | 429 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}OtherAsset2Choice | 439 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}OtherAsset2Code | 445 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}PartyIdentification125Choice | 454 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}PartyIdentification132 | 461 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}PartyIdentification139 | 470 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}PhoneNumber | 476 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}PolishNationalClearingCodeIdentifier | 481 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}PortugueseNCCIdentifier | 486 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}PostalAddress1 | 491 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}QUICKIdentifier | 503 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}RICIdentifier | 506 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}References68Choice | 512 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}RejectedReason33Choice | 518 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}RejectedStatusReason12Code | 524 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}RequestForTransferStatusReportV09 | 574 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}Role8Choice | 582 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}RussianCentralBankIdentificationCodeIdentifier | 588 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}SEDOLIdentifier | 593 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}SecurityIdentification46Choice | 596 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}SicovamIdentifier | 616 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}SmallNetworkIdentifier | 619 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}SouthAfricanNCCIdentifier | 624 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}SpanishDomesticInterbankingIdentifier | 629 |
| [type-0090](types/type-0090.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}SubAccount5 | 634 |
| [type-0091](types/type-0091.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}SwissBCIdentifier | 641 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}SwissSICIdentifier | 646 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}TickerIdentifier | 651 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}TypeOfRequest1Choice | 657 |
| [type-0095](types/type-0095.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}TypeOfRequest1Code | 663 |
| [type-0096](types/type-0096.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}UKDomesticSortCodeIdentifier | 669 |
| [type-0097](types/type-0097.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}ValorenIdentifier | 674 |
| [type-0098](types/type-0098.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:sese.009.001.09}WertpapierIdentifier | 677 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| choice | 12 |
| complexType | 38 |
| element | 167 |
| enumeration | 79 |
| maxLength | 10 |
| minLength | 10 |
| pattern | 32 |
| restriction | 59 |
| schema | 1 |
| sequence | 26 |
| simpleType | 59 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/60f0abefd8bc74409ebcc702.md) · [Message](index.md)
