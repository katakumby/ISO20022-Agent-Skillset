---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "message-business"
message_id: "head.001.001.04"
message_family: "head.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"
source_ids: ["src-000011", "src-000013"]
source_editions: ["Version 4 March 2024", "march-2024"]
source_locations: ["MDR §§2.1–2.4 pp4–25; §3 pp26–57", "XSD /xs:schema"]
message_sets: ["business-application-header"]
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint", "bah-copy-context-account-owner"]
limitations: ["External table validation and service/market-practice semantics are not established solely by XSD.", "MUG V3 historical scenario profile is separately qualified."]
---

# head.001.001.04 — business purpose and rules

## Purpose, usage and participants

A new Business Message with accompanying BAH is created by its sending MessagingEndpoint for each business event/interaction in a Business Transaction. Business Message behaviour is described by the Business Transaction; structure is described by Message Definitions, Message Rules, Rules and Market Practices. Specific BAH usage may be defined by the relevant SEG. [src-000011](../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf), §2.1 pp4–6.

BAH and its Business Message must not contain transport mechanics or depend on transport-message knowledge for interpretation. Business-meaningful headers/footers/envelopes remain message content. Business actors are referred to by Name in the business message, not the transport layer. From identifies the creator; To identifies the endpoint that ultimately processes it. These endpoints may differ from transport addresses. [src-000011](../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf), §2.1 p4; §2.4.2 p9; §2.4.3 p11.

- [bah-sending-messaging-endpoint](../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../participants/bah-receiving-messaging-endpoint.md).
- [bah-copy-context-account-owner](../../participants/bah-copy-context-account-owner.md).

## Field usage

| Building block | Source-supported meaning/condition | MDR locator |
| --- | --- | --- |
| CharacterSet | Character set of text-based Business Message elements; UnicodeChartsCode; table validation. | §2.4.1 p9 |
| From / To | Sending creator / ultimate processing endpoint; person/organisation or financial-institution identification choice. | §§2.4.2–3 pp9–13 |
| BusinessMessageIdentifier | Unambiguously identifies the Business Message to its creator. | §2.4.4 p13 |
| MessageDefinitionIdentifier | Identifier of the Message Definition associated with this instance. | §2.4.5 p13 |
| BusinessService | Agreed exchange rules; may identify a processing service/level. | §2.4.6 pp13–14 |
| MarketPractice | Rules agreed to restrict usage for STP; may extend message specification with extensions/supplementary data. Registry names the registration scheme; Identification identifies the practice within it, optionally including version/date or a URN. | §2.4.7 p14 |
| CreationDate | Date/time this Business Message header was created. | §2.4.8 p14 |
| BusinessProcessingDate | Sender-indicated receiver processing date/time; may differ from CreationDate; usage decided by market practice or bilateral agreement. | §2.4.9 pp14–15 |
| CopyDuplicate | COPY, DUPL or CODU per the complete source code table; Related required when this field is present. | §2.4.10 p15; C5 p8 |
| PossibleDuplicate | If original was not received, process as original; if original was received, take action to avoid processing again. Application-level resend, not network retransmission. | §2.4.11 p15 |
| Priority | Relative processing precedence over assigned priorities; semantics are user/service/implementation dependent. | §2.4.12 p16; §3.2.1.2 pp50–51 |
| Signature | Digital signature of entity authorised to sign this Business Message; W3C XML Signature context and OnlySignatureElement constraint. | §2.4.13 p16; C4 p8 |
| Related | Headers of messages to which this message relates; may be used for query replies, cancellation or amendment. | §2.4.14 pp16–25 |

All rows: [src-000011](../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf), §2.4 pp9–25. Copy or duplicate flags themselves do not define a settlement cancellation or movement reversal. Related can point to such contextual messages but does not prescribe their message family.

Related/CreationDate has an additional source usage condition: times must be normalized using the “Z” annotation (MDR §2.4.14.8, file/printed p23). This note belongs to the related-header CreationDate; the top-level CreationDate definition on p14 does not repeat it. Both use ISODateTime structurally, so preserve this as a scoped MDR usage condition, not an invented XSD facet. [src-000011](../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf), §§2.4.8 and 2.4.14.8, pp14 and23.

## All source-defined constraints

| ID | Constraint | Source meaning |
| --- | --- | --- |
| C1 | AnyBIC | Valid ISO 9362 registered Business identifier code for financial or non-financial institution; 8 or 11 contiguous characters. |
| C2 | BICFI | Valid registered financial-institution BIC; 8 or 11 contiguous characters. |
| C3 | Country | Check against United Nations country names / ISO 3166 Alpha-2 list. |
| C4 | OnlySignatureElement | Of the possible XML Signature namespace global roots, only Signature is permitted. |
| C5 | RelatedPresentWhenCopyDupl | Related contains relevant BusinessMessageHeader elements; when CopyDuplicate is present, Related[1] must be present. MessageDefinition-level rule. |
| C6 | ValidationByTable | Applies to CharacterSet; UnicodeChartsCode names Unicode blocks. No actual block enumeration is supplied in this MDR. |
| C7 | ValidationByTable | Applies to Priority; the relevant user community defines the meaning of its priority values. No universal priority enumeration is supplied here. |

[src-000011](../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf), §2.3 pp8–9; §3.2.1.2 pp50–51; §3.2.1.11 p53.

These source business/table-validation requirements remain separate from XSD syntax. For example, a matching BIC pattern does not establish registry validity, and the XSD does not replace contextual priority semantics or C5 business validation.

## Structures, tables and related context

[Complete exact XSD structure and 55 declarations](structure.md) contains all structural cardinalities, types and schema restrictions. [All 76 reviewed MDR tables, including 19 unruled facet blocks](../../message-sets/business-application-header/march-2024/documents/src-000011/visual-coverage.md) preserves source hierarchy and complete code definitions. The MDR contains no substantive source diagram.

The MDR p7 labels its structure “Message root <Document> <AppHdr>”; the supplied XSD declares AppHdr at /xs:schema/xs:element. That generic table wording is preserved and is not used to introduce an extra Document wrapper. [src-000013](../../../../raw-input/business_application_header/head.001.001.04.xsd), targetNamespace; /xs:schema/xs:element[@name="AppHdr"].

[Historical MUG usage scenarios and source diagrams](../../message-sets/business-application-header/2021-11-03-v3.0/flows/index.md) are guide-level context. Its packaging example uses V03; it is not silently an exact V04 implementation profile. [BAH versus BFH](../../concepts/business-application-header-and-business-file-header.md).
