---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.025.001.02"
message_family: "acmt.025"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02"
source_ids: ["src-000235"]
source_editions: ["august-2026"]
---

# acmt.025.001.02 structure

[src-000235](../../../../../raw-input/target2securities_t2s/acmt.025.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Document | 18 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Document | 18 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}AccountIdentification4Choice | 19 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}AccountQueryListV02 | 39 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}AccountSchemeName1Choice | 96 |
| [type-0005](types/type-0005.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}AccountStatus3Code | 116 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ActiveCurrencyCode | 148 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}AddressType2Code | 157 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}AddressType3Choice | 201 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}AnyBICDec2014Identifier | 221 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}BICFIDec2014Identifier | 230 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}BranchAndFinancialInstitutionIdentification8 | 239 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}BranchData5 | 261 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}CashAccountType2Choice | 293 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ClearingSystemIdentification2Choice | 313 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ClearingSystemMemberIdentification2 | 333 |
| [type-0016](types/type-0016.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}CodeOrProprietary1Choice | 353 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}CommunicationFormat1Choice | 373 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}CommunicationMethod2Choice | 393 |
| [type-0019](types/type-0019.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}CommunicationMethod2Code | 413 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Contact13 | 451 |
| [type-0021](types/type-0021.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}CountryCode | 537 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}CustomerAccount10 | 546 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}CustomerAccountReturnCriteria1 | 710 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}DateAndPlaceOfBirth1 | 832 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}DatePeriod2 | 864 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}DatePeriodSearch1Choice | 884 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Document | 922 |
| [type-0028](types/type-0028.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Exact4AlphaNumericText | 927 |
| [type-0029](types/type-0029.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ExternalAccountIdentification1Code | 936 |
| [type-0030](types/type-0030.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ExternalCashAccountType1Code | 948 |
| [type-0031](types/type-0031.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ExternalClearingSystemIdentification1Code | 960 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ExternalCommunicationFormat1Code | 971 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ExternalFinancialInstitutionIdentification1Code | 983 |
| [type-0034](types/type-0034.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ExternalOrganisationIdentification1Code | 995 |
| [type-0035](types/type-0035.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ExternalPersonIdentification1Code | 1007 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ExternalProxyAccountType1Code | 1019 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}FinancialIdentificationSchemeName1Choice | 1030 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}FinancialInstitutionIdentification23 | 1050 |
| [type-0039](types/type-0039.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Frequency7Code | 1094 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}GenericAccountIdentification1 | 1156 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}GenericFinancialIdentification1 | 1182 |
| [type-0042](types/type-0042.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}GenericIdentification1 | 1208 |
| [type-0043](types/type-0043.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}GenericIdentification13 | 1234 |
| [type-0044](types/type-0044.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}GenericIdentification30 | 1260 |
| [type-0045](types/type-0045.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}GenericIdentification42 | 1286 |
| [type-0046](types/type-0046.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}GenericOrganisationIdentification3 | 1306 |
| [type-0047](types/type-0047.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}GenericPersonIdentification2 | 1332 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}IBAN2007Identifier | 1358 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ISODate | 1367 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ISODateTime | 1374 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ImpliedCurrencyAndAmount | 1387 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}LEIIdentifier | 1399 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max128Text | 1408 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max140Text | 1418 |
| [type-0055](types/type-0055.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max16Text | 1428 |
| [type-0056](types/type-0056.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max2048Text | 1438 |
| [type-0057](types/type-0057.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max256Text | 1448 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max34Text | 1458 |
| [type-0059](types/type-0059.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max350Text | 1468 |
| [type-0060](types/type-0060.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max35Text | 1478 |
| [type-0061](types/type-0061.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max4AlphaNumericText | 1488 |
| [type-0062](types/type-0062.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max4Text | 1499 |
| [type-0063](types/type-0063.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max5NumericText | 1509 |
| [type-0064](types/type-0064.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Max70Text | 1518 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}MessageIdentification1 | 1528 |
| [type-0066](types/type-0066.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}NamePrefix2Code | 1548 |
| [type-0067](types/type-0067.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Organisation42 | 1586 |
| [type-0068](types/type-0068.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}OrganisationIdentification39 | 1678 |
| [type-0069](types/type-0069.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}OrganisationIdentificationSchemeName1Choice | 1704 |
| [type-0070](types/type-0070.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}OtherContact1 | 1724 |
| [type-0071](types/type-0071.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Party52Choice | 1744 |
| [type-0072](types/type-0072.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}PartyAndSignature4 | 1764 |
| [type-0073](types/type-0073.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}PartyIdentification272 | 1784 |
| [type-0074](types/type-0074.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}PartyIdentification274 | 1822 |
| [type-0075](types/type-0075.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}PersonIdentification18 | 1860 |
| [type-0076](types/type-0076.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}PersonIdentificationSchemeName1Choice | 1880 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}PhoneNumber | 1900 |
| [type-0078](types/type-0078.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}PostalAddress27 | 1910 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}PreferredContactMethod2Code | 2026 |
| [type-0080](types/type-0080.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ProxyAccountIdentification1 | 2070 |
| [type-0081](types/type-0081.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}ProxyAccountType1Choice | 2090 |
| [type-0082](types/type-0082.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}References4 | 2110 |
| [type-0083](types/type-0083.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}Restriction1 | 2136 |
| [type-0084](types/type-0084.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}SkipPayload | 2162 |
| [type-0085](types/type-0085.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}StatementFrequencyAndForm1 | 2172 |
| [type-0086](types/type-0086.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}SupplementaryData1 | 2204 |
| [type-0087](types/type-0087.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}SupplementaryDataEnvelope1 | 2225 |
| [type-0088](types/type-0088.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.025.001.02}YesNoIndicator | 2234 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| annotation | 328 |
| any | 2 |
| choice | 14 |
| complexType | 49 |
| documentation | 656 |
| element | 209 |
| enumeration | 35 |
| fractionDigits | 1 |
| maxLength | 19 |
| minInclusive | 1 |
| minLength | 19 |
| pattern | 10 |
| restriction | 38 |
| schema | 1 |
| sequence | 35 |
| simpleType | 38 |
| totalDigits | 1 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/2a87eb8ef967dafd805ed274.md) · [Message](index.md)
