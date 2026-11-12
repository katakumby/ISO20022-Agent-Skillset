---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "colr.010.001.05"
message_family: "colr.010"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.010.001.05"
source_ids: ["src-000072"]
source_editions: []
---

# colr.010.001.05 structure

[src-000072](../../../../../raw-input/collateral_management_collateral_management/colr.010.001.05.xsd); `urn:iso:std:iso:20022:tech:xsd:colr.010.001.05`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:colr.010.001.05 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ActiveOrHistoricCurrencyAnd13DecimalAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Agreement4 | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}AgreementFramework1Choice | 74 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}AgreementFramework1Code | 80 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}AlternatePartyIdentification8 | 89 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}AnyBICDec2014Identifier | 96 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}BaseOneRate | 101 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}BlockChainAddressWallet3 | 107 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}BlockChainAddressWallet5 | 114 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CashCollateral3 | 121 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CashCollateral5 | 134 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CollateralAccount3 | 148 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CollateralAccountIdentificationType3Choice | 155 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CollateralAccountType1Code | 161 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CollateralOwnership4 | 170 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CollateralSubstitution7 | 176 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CollateralSubstitution8 | 188 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CollateralSubstitutionRequestV05 | 200 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CollateralSubstitutionSequence1Code | 210 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CollateralSubstitutionType1Code | 216 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ContactIdentification2 | 222 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}CountryCode | 233 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}DateAndDateTime2Choice | 238 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}DateCode9Choice | 244 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}DateFormat14Choice | 250 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}DateType2Code | 256 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}DecimalNumber | 261 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}DeliveringPartiesAndAccount19 | 267 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}DepositType1Code | 274 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Document | 280 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Exact4AlphaNumericText | 285 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ExposureType11Code | 290 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ExternalAccountIdentification1Code | 330 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ExternalFinancialInstrumentIdentificationType1Code | 336 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}FinancialInstrumentQuantity33Choice | 342 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}GenericAccountIdentification1 | 350 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}GenericIdentification30 | 357 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}GenericIdentification36 | 364 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}GenericIdentification78 | 371 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}IBAN2007Identifier | 377 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ISINOct2015Identifier | 382 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ISODate | 387 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ISODateTime | 390 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}IdentificationSource3Choice | 393 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}IdentificationType43Choice | 399 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ImpliedCurrencyAndAmount | 405 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Max140Text | 412 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Max16Text | 418 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Max256Text | 424 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Max30DecimalNumber | 430 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Max34Text | 436 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Max350Text | 442 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Max35Text | 448 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Max70Text | 454 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}NameAndAddress13 | 460 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}NameAndAddress5 | 466 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}NameAndAddress6 | 472 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}NamePrefix1Code | 478 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Obligation9 | 486 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}OtherCollateral11 | 498 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}OtherCollateral9 | 520 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}OtherIdentification1 | 541 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}OtherTypeOfCollateral3 | 548 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PartyIdentification178Choice | 554 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PartyIdentification239Choice | 561 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PartyIdentification240Choice | 568 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PartyIdentificationAndAccount200 | 575 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PartyIdentificationAndAccount201 | 586 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PartyTextInformation1 | 596 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PercentageRate | 603 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PhoneNumber | 609 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PostalAddress1 | 614 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PostalAddress2 | 626 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PostalAddress8 | 635 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Price7 | 647 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PriceRateOrAmount3Choice | 653 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}PriceValueType1Code | 659 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}ReceivingPartiesAndAccount19 | 666 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}Reference17 | 673 |
| [type-0089](types/type-0089.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SafekeepingPlace1Code | 679 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SafekeepingPlace3Code | 687 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SafekeepingPlaceFormat29Choice | 692 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SafekeepingPlaceTypeAndIdentification1 | 700 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SafekeepingPlaceTypeAndText8 | 706 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SecuritiesAccount19 | 712 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SecuritiesCollateral11 | 719 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SecuritiesCollateral12 | 738 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SecurityIdentification19 | 756 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SettlementDetails206 | 763 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SettlementParties36Choice | 770 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SubAccount5 | 776 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SupplementaryData1 | 783 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}SupplementaryDataEnvelope1 | 789 |
| [type-0103](types/type-0103.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}TypeOfIdentification2Code | 794 |
| [type-0104](types/type-0104.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}YesNoIndicator | 803 |
| [type-0105](types/type-0105.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.010.001.05}YieldedOrValueType1Choice | 806 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 17 |
| complexType | 64 |
| element | 269 |
| enumeration | 76 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 9 |
| minInclusive | 3 |
| minLength | 9 |
| pattern | 8 |
| restriction | 40 |
| schema | 1 |
| sequence | 45 |
| simpleContent | 2 |
| simpleType | 40 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
