---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "setr.030.001.03"
message_family: "setr.030"
namespace: "urn:iso:std:iso:20022:tech:xsd:setr.030.001.03"
source_ids: ["src-000186"]
source_editions: ["2024-2025"]
---

# setr.030.001.03 structure

[src-000186](../../../../../raw-input/post_trade_matching/setr.030.001.03.xsd); `urn:iso:std:iso:20022:tech:xsd:setr.030.001.03`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:setr.030.001.03 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}AccountIdentification55Choice | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}AddressType2Code | 13 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}AffirmationStatus10Choice | 23 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}AffirmationStatus1Code | 29 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}AlternatePartyIdentification8 | 35 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}AnyBICDec2014Identifier | 42 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}BBANIdentifier | 47 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Clearing6 | 52 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}ClearingAccountType1Code | 58 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}ClearingSide1Code | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}ConfirmationParties8 | 73 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}ConfirmationPartyDetails12 | 83 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}ConfirmationPartyDetails14 | 93 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}ConfirmationPartyDetails15 | 104 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}CountryCode | 114 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Document | 119 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}DocumentNumber17Choice | 124 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Eligibility1Code | 131 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Exact3NumericText | 138 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Exact4AlphaNumericText | 143 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}GenericIdentification30 | 148 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}GenericIdentification36 | 155 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}IBAN2007Identifier | 162 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}ISO20022MessageIdentificationText | 167 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}IdentificationReference15Choice | 172 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}IdentificationType43Choice | 190 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}InvestorCapacity4Choice | 196 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Linkages76 | 202 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Max140Text | 208 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Max16Text | 214 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Max210Text | 220 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Max34Text | 226 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Max350Text | 232 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Max35Text | 238 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}Max70Text | 244 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}NameAndAddress13 | 250 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}PartyIdentification240Choice | 256 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}PartyIdentification243Choice | 263 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}PartyIdentificationAndAccount219 | 269 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}PartyTextInformation1 | 279 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}PartyTextInformation5 | 286 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}PostalAddress8 | 292 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}PurposeCode9Choice | 304 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}SecuritiesAccount20 | 310 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}SecuritiesAccount35 | 317 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}SecuritiesAccountPurposeType1Code | 324 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}SecuritiesTradeConfirmationResponseV03 | 334 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}SimpleIdentificationInformation2 | 344 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}StatusAndReason46 | 349 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}SupplementaryData1 | 356 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}SupplementaryDataEnvelope1 | 362 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}TradingCapacity4Code | 367 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}TradingCapacity6Code | 386 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}TradingPartyCapacity3Choice | 397 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}TradingPartyCapacity4Choice | 403 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}TransactiontIdentification4 | 409 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}TypeOfIdentification2Code | 414 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}UPICIdentifier | 423 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}UTIIdentifier | 428 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}UnaffirmedReason1Code | 433 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:setr.030.001.03}UnaffirmedReason3Choice | 438 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 12 |
| complexType | 35 |
| element | 120 |
| enumeration | 52 |
| maxLength | 7 |
| minLength | 7 |
| pattern | 9 |
| restriction | 26 |
| schema | 1 |
| sequence | 23 |
| simpleType | 26 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
