---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.026.001.02"
message_family: "acmt.026"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02"
source_ids: ["src-000236"]
source_editions: ["august-2026"]
---

# acmt.026.001.02 structure

[src-000236](../../../../../raw-input/target2securities_t2s/acmt.026.001.02.xsd); `urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Document | 18 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Document | 18 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AccountContract3 | 19 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AccountForAction1 | 63 |
| [type-0004](types/type-0004.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AccountIdentification4Choice | 83 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AccountListReportV02 | 103 |
| [type-0006](types/type-0006.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AccountReport34 | 147 |
| [type-0007](types/type-0007.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AccountReportOrError4Choice | 215 |
| [type-0008](types/type-0008.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AccountSchemeName1Choice | 235 |
| [type-0009](types/type-0009.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AccountStatus3Code | 255 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ActiveCurrencyAndAmount_SimpleType | 287 |
| [type-0011](types/type-0011.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ActiveCurrencyAndAmount | 294 |
| [type-0012](types/type-0012.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ActiveCurrencyCode | 310 |
| [type-0013](types/type-0013.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ActiveOrHistoricCurrencyCode | 319 |
| [type-0014](types/type-0014.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AddressType2Code | 328 |
| [type-0015](types/type-0015.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AddressType3Choice | 372 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}AnyBICDec2014Identifier | 392 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Authorisation2 | 401 |
| [type-0018](types/type-0018.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}BICFIDec2014Identifier | 427 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}BankTransactionCodeStructure4 | 436 |
| [type-0020](types/type-0020.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}BankTransactionCodeStructure5 | 458 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}BankTransactionCodeStructure6 | 478 |
| [type-0022](types/type-0022.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}BranchAndFinancialInstitutionIdentification8 | 498 |
| [type-0023](types/type-0023.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}BranchData5 | 520 |
| [type-0024](types/type-0024.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}CashAccount40 | 552 |
| [type-0025](types/type-0025.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}CashAccountType2Choice | 595 |
| [type-0026](types/type-0026.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Channel2Choice | 615 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ClearingSystemIdentification2Choice | 635 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ClearingSystemMemberIdentification2 | 655 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}CodeOrProprietary1Choice | 675 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}CommunicationFormat1Choice | 695 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}CommunicationMethod2Choice | 715 |
| [type-0032](types/type-0032.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}CommunicationMethod2Code | 735 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}CommunicationMethod3Code | 773 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Contact13 | 817 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ContractDocument1 | 903 |
| [type-0036](types/type-0036.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}CountryCode | 929 |
| [type-0037](types/type-0037.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}CustomerAccount8 | 938 |
| [type-0038](types/type-0038.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}DateAndPlaceOfBirth1 | 1048 |
| [type-0039](types/type-0039.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Document | 1080 |
| [type-0040](types/type-0040.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ErrorHandling3Choice | 1085 |
| [type-0041](types/type-0041.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ErrorHandling5 | 1105 |
| [type-0042](types/type-0042.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Exact4AlphaNumericText | 1125 |
| [type-0043](types/type-0043.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalAccountIdentification1Code | 1134 |
| [type-0044](types/type-0044.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalBankTransactionDomain1Code | 1146 |
| [type-0045](types/type-0045.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalBankTransactionFamily1Code | 1157 |
| [type-0046](types/type-0046.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalBankTransactionSubFamily1Code | 1168 |
| [type-0047](types/type-0047.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalCashAccountType1Code | 1179 |
| [type-0048](types/type-0048.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalClearingSystemIdentification1Code | 1191 |
| [type-0049](types/type-0049.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalCommunicationFormat1Code | 1202 |
| [type-0050](types/type-0050.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalFinancialInstitutionIdentification1Code | 1214 |
| [type-0051](types/type-0051.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalOrganisationIdentification1Code | 1226 |
| [type-0052](types/type-0052.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalPersonIdentification1Code | 1238 |
| [type-0053](types/type-0053.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalProxyAccountType1Code | 1250 |
| [type-0054](types/type-0054.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ExternalSystemErrorHandling1Code | 1261 |
| [type-0055](types/type-0055.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}FinancialIdentificationSchemeName1Choice | 1272 |
| [type-0056](types/type-0056.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}FinancialInstitutionIdentification23 | 1292 |
| [type-0057](types/type-0057.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}FixedAmountOrUnlimited1Choice | 1336 |
| [type-0058](types/type-0058.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Frequency7Code | 1356 |
| [type-0059](types/type-0059.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}GenericAccountIdentification1 | 1418 |
| [type-0060](types/type-0060.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}GenericFinancialIdentification1 | 1444 |
| [type-0061](types/type-0061.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}GenericIdentification1 | 1470 |
| [type-0062](types/type-0062.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}GenericIdentification13 | 1496 |
| [type-0063](types/type-0063.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}GenericIdentification30 | 1522 |
| [type-0064](types/type-0064.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}GenericOrganisationIdentification3 | 1548 |
| [type-0065](types/type-0065.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}GenericPersonIdentification2 | 1574 |
| [type-0066](types/type-0066.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Group6 | 1600 |
| [type-0067](types/type-0067.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}IBAN2007Identifier | 1620 |
| [type-0068](types/type-0068.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ISODate | 1629 |
| [type-0069](types/type-0069.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ISODateTime | 1636 |
| [type-0070](types/type-0070.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ImpliedCurrencyAndAmount | 1649 |
| [type-0071](types/type-0071.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}LEIIdentifier | 1661 |
| [type-0072](types/type-0072.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max10KBinary | 1670 |
| [type-0073](types/type-0073.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max128Text | 1680 |
| [type-0074](types/type-0074.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max140Text | 1690 |
| [type-0075](types/type-0075.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max15PlusSignedNumericText | 1700 |
| [type-0076](types/type-0076.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max16Text | 1709 |
| [type-0077](types/type-0077.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max2048Text | 1719 |
| [type-0078](types/type-0078.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max256Text | 1729 |
| [type-0079](types/type-0079.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max34Text | 1739 |
| [type-0080](types/type-0080.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max350Text | 1749 |
| [type-0081](types/type-0081.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max35Text | 1759 |
| [type-0082](types/type-0082.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max3NumericText | 1769 |
| [type-0083](types/type-0083.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max4AlphaNumericText | 1778 |
| [type-0084](types/type-0084.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max4Text | 1789 |
| [type-0085](types/type-0085.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max5NumericText | 1799 |
| [type-0086](types/type-0086.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max6Text | 1808 |
| [type-0087](types/type-0087.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Max70Text | 1818 |
| [type-0088](types/type-0088.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}MaximumAmountByPeriod1 | 1828 |
| [type-0089](types/type-0089.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}MessageIdentification1 | 1848 |
| [type-0090](types/type-0090.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}NamePrefix2Code | 1868 |
| [type-0091](types/type-0091.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}OperationMandate7 | 1906 |
| [type-0092](types/type-0092.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Organisation42 | 1962 |
| [type-0093](types/type-0093.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}OrganisationIdentification39 | 2054 |
| [type-0094](types/type-0094.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}OrganisationIdentificationSchemeName1Choice | 2080 |
| [type-0095](types/type-0095.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}OtherContact1 | 2100 |
| [type-0096](types/type-0096.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Party52Choice | 2120 |
| [type-0097](types/type-0097.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PartyAndAuthorisation7 | 2140 |
| [type-0098](types/type-0098.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PartyAndCertificate6 | 2166 |
| [type-0099](types/type-0099.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PartyAndSignature4 | 2186 |
| [type-0100](types/type-0100.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PartyIdentification272 | 2206 |
| [type-0101](types/type-0101.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PartyIdentification274 | 2244 |
| [type-0102](types/type-0102.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PartyOrGroup3Choice | 2282 |
| [type-0103](types/type-0103.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PersonIdentification18 | 2302 |
| [type-0104](types/type-0104.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PersonIdentificationSchemeName1Choice | 2322 |
| [type-0105](types/type-0105.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PhoneNumber | 2342 |
| [type-0106](types/type-0106.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PostalAddress27 | 2352 |
| [type-0107](types/type-0107.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}PreferredContactMethod2Code | 2468 |
| [type-0108](types/type-0108.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ProprietaryBankTransactionCodeStructure1 | 2512 |
| [type-0109](types/type-0109.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ProxyAccountIdentification1 | 2532 |
| [type-0110](types/type-0110.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}ProxyAccountType1Choice | 2552 |
| [type-0111](types/type-0111.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}References5 | 2572 |
| [type-0112](types/type-0112.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Restriction1 | 2616 |
| [type-0113](types/type-0113.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}SkipPayload | 2642 |
| [type-0114](types/type-0114.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}StatementFrequencyAndForm1 | 2652 |
| [type-0115](types/type-0115.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}SupplementaryData1 | 2684 |
| [type-0116](types/type-0116.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}SupplementaryDataEnvelope1 | 2705 |
| [type-0117](types/type-0117.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}Unlimited9Text | 2714 |
| [type-0118](types/type-0118.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}UseCases1Code | 2724 |
| [type-0119](types/type-0119.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.026.001.02}YesNoIndicator | 2756 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| annotation | 399 |
| any | 2 |
| attribute | 1 |
| choice | 18 |
| complexType | 67 |
| documentation | 798 |
| element | 239 |
| enumeration | 45 |
| extension | 1 |
| fractionDigits | 2 |
| length | 1 |
| maxLength | 25 |
| minInclusive | 2 |
| minLength | 25 |
| pattern | 14 |
| restriction | 51 |
| schema | 1 |
| sequence | 48 |
| simpleContent | 1 |
| simpleType | 51 |
| totalDigits | 2 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](schema-coverage.json) · [Message](index.md)
