---
template: false
document_kind: "message-structure"
review_status: "needs-review"
domain: "securities"
message_id: "acmt.005.001.06"
message_family: "acmt.005"
namespace: "urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06"
source_ids: ["src-000101"]
source_editions: ["2025-2026"]
---

# acmt.005.001.06 structure

[src-000101](../../../../../raw-input/investment_funds/acmt.005.001.06.xsd); `urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06`, `/xs:schema`, line 1.

## Namespace and roots

| Property | Source value |
| --- | --- |
| elementFormDefault | qualified |
| targetNamespace | urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06 |

| Root | Type | Line |
| --- | --- | --- |
| Document | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Document | 4 |

## Dependencies

No xs:import, xs:include, xs:redefine or xs:override declaration occurs in the supplied schema. External code-type names remain references to separately published vocabularies, not XSD imports.

## Effective schema defaults

Unless explicitly overridden, local particle minOccurs/maxOccurs are 1, element nillable is false, attribute use is optional, and wildcard processContents is strict. Element and attribute qualification follows the schema defaults above, or the XSD unqualified default if omitted. Individual type pages distinguish literal attributes from these effective defaults.

## Complete declaration and type index

| Page | Kind | QName / anonymous path | Source line |
| --- | --- | --- | --- |
| [type-0001](types/type-0001.md) | element | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Document | 4 |
| [type-0002](types/type-0002.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Account23 | 5 |
| [type-0003](types/type-0003.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}AccountManagementMessageReference5 | 11 |
| [type-0004](types/type-0004.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}AccountManagementType3Code | 20 |
| [type-0005](types/type-0005.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}AdditionalReference13 | 28 |
| [type-0006](types/type-0006.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}AddressType2Code | 35 |
| [type-0007](types/type-0007.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}AnyBICDec2014Identifier | 45 |
| [type-0008](types/type-0008.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}CountryCode | 50 |
| [type-0009](types/type-0009.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Document | 55 |
| [type-0010](types/type-0010.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Exact4AlphaNumericText | 60 |
| [type-0011](types/type-0011.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}GenderCode | 65 |
| [type-0012](types/type-0012.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}GenericIdentification1 | 71 |
| [type-0013](types/type-0013.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}GenericIdentification47 | 78 |
| [type-0014](types/type-0014.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}GenericIdentification81 | 85 |
| [type-0015](types/type-0015.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}ISODate | 91 |
| [type-0016](types/type-0016.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}ISODateTime | 94 |
| [type-0017](types/type-0017.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}IndividualPerson30 | 97 |
| [type-0018](types/type-0018.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}IndividualPersonIdentification2Choice | 106 |
| [type-0019](types/type-0019.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}InvestmentAccount77 | 112 |
| [type-0020](types/type-0020.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}LEIIdentifier | 121 |
| [type-0021](types/type-0021.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}LinkedMessage5Choice | 126 |
| [type-0022](types/type-0022.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Max16Text | 132 |
| [type-0023](types/type-0023.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Max350Text | 138 |
| [type-0024](types/type-0024.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Max35Text | 144 |
| [type-0025](types/type-0025.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Max4AlphaNumericText | 150 |
| [type-0026](types/type-0026.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}Max70Text | 157 |
| [type-0027](types/type-0027.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}MessageIdentification1 | 163 |
| [type-0028](types/type-0028.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}NameAndAddress5 | 169 |
| [type-0029](types/type-0029.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}OtherIdentification3Choice | 175 |
| [type-0030](types/type-0030.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}OwnerIdentification3Choice | 181 |
| [type-0031](types/type-0031.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}PartyIdentification125Choice | 187 |
| [type-0032](types/type-0032.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}PartyIdentification139 | 194 |
| [type-0033](types/type-0033.md) | simpleType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}PartyIdentificationType7Code | 200 |
| [type-0034](types/type-0034.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}PostalAddress1 | 222 |
| [type-0035](types/type-0035.md) | complexType | {urn:iso:std:iso:20022:tech:xsd:acmt.005.001.06}RequestForAccountManagementStatusReportV06 | 234 |

## Coverage

| Construct | Supplied count |
| --- | --- |
| choice | 5 |
| complexType | 19 |
| element | 57 |
| enumeration | 30 |
| maxLength | 5 |
| minLength | 5 |
| pattern | 5 |
| restriction | 15 |
| schema | 1 |
| sequence | 14 |
| simpleType | 15 |

Compilation: **pass**. All supplied declarations compile locally; no network schema retrieval was performed.

[Machine-readable declaration coverage](../../../../../evidence/archived/a59e63edfed6a8081b539c2a.md) · [Message](index.md)
