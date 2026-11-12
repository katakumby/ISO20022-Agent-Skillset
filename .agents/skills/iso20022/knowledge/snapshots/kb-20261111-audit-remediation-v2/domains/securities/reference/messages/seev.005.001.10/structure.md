---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "seev.005.001.10"
message_family: "seev.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.005.001.10"
source_ids: ["src-000192"]
source_editions: []
---

# seev.005.001.10 structure

[src-000192](../../../../../raw-input/securities_events_general_meeting_proxy_voting/seev.005.001.10.xsd); `urn:iso:std:iso:20022:tech:xsd:seev.005.001.10`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:seev.005.001.10 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Document | 4 |
| [type-0002](types/type-0002.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}AddressType2Code | 5 |
| [type-0003](types/type-0003.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}AnyBICDec2014Identifier | 15 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}CancelInstruction5 | 20 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}CountryCode | 26 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}DTI2024Identifier | 31 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}DateAndPlaceOfBirth2 | 36 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}DecimalNumber | 44 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Document | 50 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Exact4AlphaNumericText | 55 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}ExternalFinancialInstrumentIdentificationType1Code | 60 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}FinancialInstrumentQuantity46Choice | 66 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}GenericIdentification13 | 74 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}GenericIdentification30 | 81 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}GenericIdentification36 | 88 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}GenericIdentification78 | 95 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}HoldingBalance15 | 101 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}ISINOct2015Identifier | 108 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}ISODate | 113 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}ISODateTime | 116 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}IdentificationSource3Choice | 119 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}IdentificationType45Choice | 125 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}ImpliedCurrencyAndAmount | 131 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}LEIIdentifier | 138 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Max140Text | 143 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Max16Text | 149 |
| [type-0027](types/type-0027.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Max256Text | 155 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Max30DecimalNumber | 161 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Max350Text | 167 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Max35Text | 173 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Max4AlphaNumericText | 179 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Max50Text | 186 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Max70Text | 192 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}MeetingInstructionCancellationRequestV10 | 198 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}MeetingReference10 | 207 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}MeetingType4Code | 218 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}MeetingTypeClassification2Choice | 228 |
| [type-0038](types/type-0038.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}MeetingTypeClassification2Code | 234 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}NameAndAddress5 | 243 |
| [type-0040](types/type-0040.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}NamePrefix2Code | 249 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}NaturalPersonIdentification1 | 258 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}OtherIdentification1 | 264 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PartyIdentification129Choice | 271 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PartyIdentification198Choice | 279 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PartyIdentification221 | 288 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PartyIdentification231Choice | 295 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PartyIdentification238 | 301 |
| [type-0048](types/type-0048.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PartyIdentification246Choice | 310 |
| [type-0049](types/type-0049.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PartyIdentification250 | 316 |
| [type-0050](types/type-0050.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PartyIdentification269 | 326 |
| [type-0051](types/type-0051.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PersonName2 | 335 |
| [type-0052](types/type-0052.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PersonName3 | 341 |
| [type-0053](types/type-0053.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PostalAddress1 | 349 |
| [type-0054](types/type-0054.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}PostalAddress26 | 361 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}Quantity1Code | 374 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SafekeepingAccount18 | 379 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SafekeepingPlace1Code | 389 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SafekeepingPlace2Code | 397 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SafekeepingPlaceFormat42Choice | 403 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SafekeepingPlaceTypeAndIdentification1 | 412 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SafekeepingPlaceTypeAndText6 | 418 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SecuritiesEntryType2Code | 424 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SecurityIdentification19 | 443 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}ShortLong1Code | 450 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SignedQuantityFormat15 | 456 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SupplementaryData1 | 462 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}SupplementaryDataEnvelope1 | 468 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:seev.005.001.10}TypeOfIdentification4Code | 473 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| any | 1 |
| choice | 9 |
| complexType | 37 |
| element | 128 |
| enumeration | 55 |
| fractionDigits | 3 |
| maxLength | 9 |
| minInclusive | 1 |
| minLength | 9 |
| pattern | 7 |
| restriction | 30 |
| schema | 1 |
| sequence | 28 |
| simpleType | 30 |
| totalDigits | 3 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
