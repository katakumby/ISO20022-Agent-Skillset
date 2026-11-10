---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "message-business"
message_id: "head.002.001.01"
message_family: "head.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:head.002.001.01"
source_ids: ["src-000349", "src-000261"]
source_editions: ["june-2024"]
source_locations: ["MDR §§2.1–2.4 pp4–8; §3 pp9–10", "XSD /xs:schema"]
message_sets: ["t2s-business-file-header"]
participants: ["bfh-file-sender", "bfh-file-receiver", "bfh-service-provider", "bfh-authorised-signatory", "bfh-system-user", "bfh-system-administrator"]
flows: ["bfh-file-exchange"]
limitations: ["The supplied MDR does not define a complete ordered business process or a source business-flow diagram.", "Historical nvlp.002 statement does not establish current external availability."]
---

# head.002.001.01 — file exchange purpose and rules

## Purpose and usage boundary

The BFH supplies information about file-exchange parties, content and structure. It identifies the sender, uniquely identifies the exchanged file, describes the message types (ISO 20022 definitions by default), and supplies receiver processing information such as message-instance counts. Its two building blocks are PayloadDescription and Payload. [src-000349](../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.1 p4.

The supplied June2024 publication limits head.002 to existing implementations such as the Eurosystem, says it will not be maintained, and directs new implementations toward its then-upcoming Business File Envelope nvlp.002. This is a statement of that publication; no supplied nvlp.002 schema or current product status is established. Missing nvlp.002 is not an XSD import failure. [src-000349](../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §§1.1–2.1 pp3–4.

## Participants

- [bfh-file-sender](../../participants/bfh-file-sender.md).
- [bfh-file-receiver](../../participants/bfh-file-receiver.md).
- [bfh-service-provider](../../participants/bfh-service-provider.md).
- [bfh-authorised-signatory](../../participants/bfh-authorised-signatory.md).
- [bfh-system-user](../../participants/bfh-system-user.md).
- [bfh-system-administrator](../../participants/bfh-system-administrator.md).

Roles are contextual. A system user represents an individual or application; its granted privileges determine available functions. The source does not distinguish those categories through an administrator attribute. [src-000349](../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.4.1.2.1 p7.

## Fields and source rules

| Field/context | Definition, condition or business rule | MDR locator |
| --- | --- | --- |
| PayloadDescription / PayloadData | Describes payload and identifies the exchanged instance. | §§2.4.1–2.4.1.1 pp5–6 |
| PayloadIdentifier | Unique file identifier assigned by sender. | §2.4.1.1.1 p6 |
| CreationDateAndTime | Date/time file was created by sender. | §2.4.1.1.2 p6 |
| PossibleDuplicateFlag | Possible duplicate of file between two business applications; if omitted, source business meaning is False. | §2.4.1.1.3 pp6–7 |
| ApplicationSpecifics | Optional block of business information necessary to the service provider. | §2.4.1.2 p7 |
| SystemUser | Optional static-data user account, representing individual or application and privileges. | §2.4.1.2.1 p7 |
| Signature | Optional digital signature of business entity authorised to sign the Business File. | §2.4.1.2.2 p7 |
| TotalNumberOfDocuments | Total message-instance count within the file; mandatory within present ApplicationSpecifics. | §2.2 p5; §2.4.1.2.3 p7 |
| PayloadType | Identifies type of payload. | §2.4.1.3 p8 |
| ManifestData | Repeats for each different item type, describing related items/attachments. | §2.4.1.4 p8 |
| DocumentType / NumberOfDocuments | Declared item type and instance count for that type; catalogue area examples include admi, camt, pacs, sese and semt. | §§2.4.1.4.1–2 p8 |
| Payload | Contains exchanged documents; permits any XML namespace with lax processing. Validate against an available uniquely determined declaration; otherwise absence of validation is permitted. | §2.4.2 p8 |

All source rows: [src-000349](../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.4 pp5–8. No reconciliation equation for total count versus manifest/payload counts is stated here; no additional rule is invented.

C1 OnlySignatureElement permits only the Signature root from XML Signature namespace. The source references XML Signature Syntax and Processing Second Edition (10 June2008). Keep this source business rule distinct from the XSD’s lax namespace wildcard. [src-000349](../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.3 p5; §2.4.1.2.2 p7.

The omitted PossibleDuplicateFlag has source-defined meaning False, while its optional XSD element declares no default attribute. The distinction matters for schema-only validators. [src-000261](../../../../raw-input/target2securities_t2s/head.002.001.01.xsd), /xs:schema/xs:complexType[@name="PayloadData2"]/xs:sequence/xs:element[@name="PssblDplctFlg"].

## Datatypes, full structure and evidence

[Complete exact XSD structure and 14 declarations](structure.md) supplies all ordering, cardinalities, wildcards and restrictions. [All 10 reviewed MDR tables, including four unruled format blocks](../../message-sets/t2s-business-file-header/june-2024/documents/src-000349/visual-coverage.md) includes Number(totalDigits18,fractionDigits0), Max140Text, Max256Text and Max35Text facets. ISODateTime permits date/time with UTC, offset or local representations; parties agree any fractional-second digit limit. [src-000349](../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §3.1 pp9–10.

The MDR p5 prints “Message root <Document> <Xchg>”; the supplied schema declares Xchg at /xs:schema/xs:element. The table wording is retained without inventing an extra Document wrapper. [src-000261](../../../../raw-input/target2securities_t2s/head.002.001.01.xsd), targetNamespace; /xs:schema/xs:element[@name="Xchg"].

[File-exchange responsibilities and source limitations](../../message-sets/t2s-business-file-header/june-2024/flows/file-exchange.md) is an explicitly explanatory ordering of field semantics. All10 source pages were rendered and inspected; no substantive source diagram exists. [BAH versus BFH scope](../../concepts/business-application-header-and-business-file-header.md).
