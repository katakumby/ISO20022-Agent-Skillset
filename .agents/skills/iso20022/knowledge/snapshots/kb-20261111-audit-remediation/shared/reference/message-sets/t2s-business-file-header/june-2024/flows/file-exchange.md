---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bfh-file-exchange"
source_ids: ["src-000349"]
source_edition: "June 2024"
source_locations: ["§2.1 p4; §§2.4.1–2.4.2 pp5–8"]
domains: ["shared"]
message_sets: ["t2s-business-file-header"]
message_ids: ["head.002.001.01"]
participants: ["bfh-file-sender", "bfh-file-receiver", "bfh-service-provider", "bfh-authorised-signatory", "bfh-system-user", "bfh-system-administrator"]
content_origin: "source-grounded-explanatory-sequence"
limitations: ["The MDR supplies field responsibilities, not a normative ordered process or source flow diagram."]
source_editions: ["june-2024"]
---

# Business File exchange context

## Purpose, trigger and preconditions

A sender exchanges a file containing documents with a receiving party. BFH identifies the file, describes its content/type/structure, and provides processing information such as counts. The publication limits head.002 to existing implementations; its statement about future nvlp.002 is historical supplied evidence. [src-000349](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.1 p4.

The sequence below is an explanatory ordering derived from the source-defined responsibilities and fields. The MDR does not specify a normative activity order, a trigger beyond the file exchange, or additional business preconditions.

## Participants

- [bfh-file-sender](../../../../participants/bfh-file-sender.md).
- [bfh-file-receiver](../../../../participants/bfh-file-receiver.md).
- [bfh-service-provider](../../../../participants/bfh-service-provider.md).
- [bfh-authorised-signatory](../../../../participants/bfh-authorised-signatory.md).
- [bfh-system-user](../../../../participants/bfh-system-user.md).
- [bfh-system-administrator](../../../../participants/bfh-system-administrator.md).

The system user and system administrator occur in the field narrative even though there is no source diagram. The user is a static-data account representing an individual or application, with functions governed by granted privileges; the administrator provides no attribute distinguishing individuals from applications. [src-000349](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.4.1.2.1 p7.

## Activities and responsibilities

| Explanatory step | Responsible role | Source-supported action/information | Message direction |
| --- | --- | --- | --- |
| 1 | File sender | Creates file; supplies unique PayloadIdentifier and CreationDateAndTime. | Local creation. |
| 2 | File sender | Describes payload type; optional ManifestData repeats for each different item type and gives its count. | Local description. |
| 3 (optional) | Service provider / system user context | ApplicationSpecifics carries required service business information, optional SystemUser, optional Signature and total instance count. SystemUser privileges govern available system functions. | No separate service-provider exchange specified. |
| 4 (optional) | Authorised signatory | Includes digital signature of the business entity authorised to sign the file. | No separate signing message specified. |
| 5 | File sender → file receiver | Exchanges file with BFH and documents; receiver obtains processing information including supplied counts. | File sender → file receiver; head.002.001.01 file context. |

[src-000349](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.1 p4; §§2.4.1.1–2.4.2 pp6–8.

## Alternatives, exceptions and outcomes

Payload and ManifestData may repeat zero or more times; ApplicationSpecifics is optional. If present, its total count is required by the structure. PossibleDuplicateFlag is optional and the MDR assigns omitted indicator the business default False. No duplicate-handling, cancellation, reversal, delivery acknowledgement or failure-response process is specified by this MDR. [src-000349](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`, §2.2 p5; §2.4.1.1.3 p7; §§2.4.1.2–2.4.2 pp7–8.

The file’s identity/content/processing information is available to the receiver. The source gives no explicit postcondition asserting delivery acceptance, processing completion or equality checks between counts and payloads. Those are not manufactured as business rules.

## Tables, schema and review

[All 10 reviewed source tables and diagram inventory](../documents/src-000349/visual-coverage.md) · [Exact XSD structure and 14 declarations](../../../../messages/head.002.001.01/structure.md) · [Purpose, rules and field usage](../../../../messages/head.002.001.01/business.md). No substantive source diagram exists in this MDR; this explanatory sequence is not labelled a source reconstruction.
