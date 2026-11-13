---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "colr.007.001.06"
message_family: "colr.007"
namespace: "urn:iso:std:iso:20022:tech:xsd:colr.007.001.06"
source_ids: ["src-000069"]
source_editions: []
---

# colr.007.001.06 structure

[src-000069](../../../../../raw-input/collateral_management_collateral_management/colr.007.001.06.xsd); `urn:iso:std:iso:20022:tech:xsd:colr.007.001.06`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:colr.007.001.06 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}AccountIdentification4Choice | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}AccountSchemeName1Choice | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ActiveCurrencyAndAmount_SimpleType | 17 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ActiveCurrencyAndAmount | 24 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ActiveCurrencyCode | 31 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ActiveOrHistoricCurrencyAnd13DecimalAmount_SimpleType | 36 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ActiveOrHistoricCurrencyAnd13DecimalAmount | 43 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ActiveOrHistoricCurrencyCode | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}AddressType2Code | 55 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Agreement4 | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}AgreementFramework1Choice | 74 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}AgreementFramework1Code | 80 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}AlternatePartyIdentification8 | 89 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}AnyBICDec2014Identifier | 96 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}BaseOneRate | 101 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}BlockChainAddressWallet3 | 107 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}BlockChainAddressWallet5 | 114 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CashCollateral2 | 121 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CashCollateral3 | 135 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Collateral54 | 148 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Collateral55 | 159 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralAccount3 | 170 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralAccountIdentificationType3Choice | 177 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralAccountType1Code | 183 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralMovement12 | 192 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralMovement13 | 198 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralMovement6Choice | 204 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralOwnership4 | 210 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralProposal6Choice | 216 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralProposal7 | 222 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CollateralProposalV06 | 228 |
| [type-0033](types/type-0033.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ContactIdentification2 | 237 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}CountryCode | 248 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}DateAndDateTime2Choice | 253 |
| [type-0036](types/type-0036.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}DateCode9Choice | 259 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}DateFormat14Choice | 265 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}DateType2Code | 271 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}DecimalNumber | 276 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}DeliveringPartiesAndAccount19 | 282 |
| [type-0041](types/type-0041.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}DepositType1Code | 289 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Document | 295 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Exact4AlphaNumericText | 300 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ExposureType11Code | 305 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ExternalAccountIdentification1Code | 345 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ExternalFinancialInstrumentIdentificationType1Code | 351 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}FinancialInstrumentQuantity33Choice | 357 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}GenericAccountIdentification1 | 365 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}GenericIdentification30 | 372 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}GenericIdentification36 | 379 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}GenericIdentification78 | 386 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}IBAN2007Identifier | 392 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ISINOct2015Identifier | 397 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ISODate | 402 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ISODateTime | 405 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}IdentificationSource3Choice | 408 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}IdentificationType43Choice | 414 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ImpliedCurrencyAndAmount | 420 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Max140Text | 427 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Max16Text | 433 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Max256Text | 439 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Max30DecimalNumber | 445 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Max34Text | 451 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Max350Text | 457 |
| [type-0065](types/type-0065.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Max35Text | 463 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Max70Text | 469 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}NameAndAddress13 | 475 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}NameAndAddress5 | 481 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}NameAndAddress6 | 487 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}NamePrefix1Code | 493 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Obligation9 | 501 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}OtherCollateral9 | 513 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}OtherIdentification1 | 534 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}OtherTypeOfCollateral3 | 541 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PartyIdentification178Choice | 547 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PartyIdentification239Choice | 554 |
| [type-0077](types/type-0077.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PartyIdentification240Choice | 561 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PartyIdentificationAndAccount200 | 568 |
| [type-0079](types/type-0079.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PartyIdentificationAndAccount201 | 579 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PartyTextInformation1 | 589 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PercentageRate | 596 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PhoneNumber | 602 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PostalAddress1 | 607 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PostalAddress2 | 619 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PostalAddress8 | 628 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Price7 | 640 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PriceRateOrAmount3Choice | 646 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}PriceValueType1Code | 652 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}Proposal6 | 659 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ProposalType1Code | 665 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}ReceivingPartiesAndAccount19 | 671 |
| [type-0092](types/type-0092.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SafekeepingPlace1Code | 678 |
| [type-0093](types/type-0093.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SafekeepingPlace3Code | 686 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SafekeepingPlaceFormat29Choice | 691 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SafekeepingPlaceTypeAndIdentification1 | 699 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SafekeepingPlaceTypeAndText8 | 705 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SecuritiesAccount19 | 711 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SecuritiesCollateral10 | 718 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SecurityIdentification19 | 736 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SettlementDetails205 | 743 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SettlementParties35Choice | 750 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SubAccount5 | 756 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SupplementaryData1 | 763 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}SupplementaryDataEnvelope1 | 769 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}TypeOfIdentification2Code | 774 |
| [type-0106](types/type-0106.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}YesNoIndicator | 783 |
| [type-0107](types/type-0107.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:colr.007.001.06}YieldedOrValueType1Choice | 786 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| attribute | 2 |
| choice | 19 |
| complexType | 67 |
| element | 243 |
| enumeration | 74 |
| extension | 2 |
| fractionDigits | 7 |
| maxLength | 9 |
| minInclusive | 3 |
| minLength | 9 |
| pattern | 8 |
| restriction | 39 |
| schema | 1 |
| sequence | 46 |
| simpleContent | 2 |
| simpleType | 39 |
| totalDigits | 7 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/30ac4c8179733c0b8959d430.md) · [Message](index.md)
