---
template: false
document_kind: "message-mdr-evidence"
review_status: "needs-review"
domain: "shared"
message_id: "head.001.001.04"
message_family: "head.001"
namespace: "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"
source_ids: ["src-000011"]
source_locations: [{"source_id": "src-000011", "heading": "2 head.001.001.04 BusinessApplicationHeaderV04", "file_pages": [4, 25]}]
limitations: ["PDF text and candidate tables require visual reconciliation; business-role mapping is not inferred from XML names.", "Separate publication statements are retained without version-comparison or silent conflict resolution."]
source_editions: ["Version 4 March 2024"]
---

# head.001.001.04 MDR business evidence

The following supplied publications explicitly define this exact message identifier. Functionality text is retained with page locators; detailed definitions, rules, tables and figures remain in focused source sections. This page does not substitute one message version for another.

## src-000011 — 2 head.001.001.04 BusinessApplicationHeaderV04

[src-000011](../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md); file pp4–25; publication Version 4 March 2024. Printed labels are retained in the page text; these locators use one-based file pages.

### Purpose, usage, participant roles and structure outline

**src-000011, 2 head.001.001.04 BusinessApplicationHeaderV04, Functionality, file p4.**

The Business Layer deals with Business Messages. The behaviour of the Business Messages is fully
described by the Business Transaction and the structure of the Business Messages is fully described by
the Message Definitions and related Message Rules, Rules and Market Practices. All of which are
registered in the ISO 20022 Repository.
A single new Business Message (with its accompagnying business application header) is created - by
the sending MessagingEndpoint - for each business event; that is each interaction in a Business
Transaction. A Business Message adheres to the following principles:
" A Business Message (and its business application header) must not contain information about the
Message Transport System or the mechanics or mechanism of message sending, transportation, or
receipt.
" A Business Message must be comprehensible outside of the context of the Transport Message. That
is the Business Message must not require knowledge of the Transport Message to be understood.
" A Business Message may contain headers, footers, and envelopes that are meaningful for the
business. When present, they are treated as any other message content, which means that they are
considered part of the Message Definition of the Business Message and as such will be part of the ISO
20022 Repository.
" A Business Message refers to Business Actors by their Name. Each instance of a Business Actor has
one Name. The Business Actor must not be referred to in the Transport Layer.
Specific usage of this BusinessMessageHeader may be defined by the relevant SEG.
Outline
The BusinessApplicationHeaderV04 MessageDefinition is composed of 14 MessageBuildingBlocks:
A. CharacterSet
Contains the character set of the text-based elements used in the Business Message.
B. From
The sending MessagingEndpoint that has created this Business Message for the receiving
MessagingEndpoint that will process this Business Message.
Note the sending MessagingEndpoint might be different from the sending address potentially
contained in the transport header (as defined in the transport layer).
C. To
The MessagingEndpoint designated by the sending MessagingEndpoint to be the recipient who will
ultimately process this Business Message.
Note the receiving MessagingEndpoint might be different from the receiving address potentially
contained in the transport header (as defined in the transport layer).
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 4 March 2024

**src-000011, 2 head.001.001.04 BusinessApplicationHeaderV04, Functionality, file p5.**

D. BusinessMessageIdentifier
Unambiguously identifies the Business Message to the MessagingEndpoint that has created the
Business Message.
E. MessageDefinitionIdentifier
The Message Definition Identifier of the Business Message instance with which this Business
Application Header instance is associated.
F. BusinessService
Specifies the business service agreed between the two MessagingEndpoints under which rules this
Business Message is exchanged.
To be used when there is a choice of processing services or processing service levels.
Example:
"marketx.hvps.01" and "marketx.xbdr.01" might be used to indicate that the associated messages
are subject to different processing levels for domestic high value payments versus cross-border
payments within the same market practice.
G. MarketPractice
Specifies the market practice to which the message conforms. The market practices are a set of
rules agreed between parties that restricts the usage of the messages in order to achieve better
STP (Straight Through Processing) rates.
A market practice specification may also extend the underlying message specification by using
extensions or supplementary data of this underlying message.
H. CreationDate
Date and time when this Business Message (header) was created.
I. BusinessProcessingDate
Processing date and time indicated by the sender for the receiver of the business message. This
date may be different from the date and time provided in the CreationDate.
Usage: Market practice or bilateral agreement should specify how this element should be used.
J. CopyDuplicate
Indicates whether the message is a Copy, a Duplicate or a copy of a duplicate of a previously sent
ISO 20022 Message.
K. PossibleDuplicate
Flag indicating if the Business Message exchanged between the MessagingEndpoints is possibly a
duplicate.
If the receiving MessagingEndpoint did not receive the original, then this Business Message should
be processed as if it were the original.
If the receiving MessagingEndpoint did receive the original, then it should perform necessary
actions to avoid processing this Business Message again.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 5 March 2024

**src-000011, 2 head.001.001.04 BusinessApplicationHeaderV04, Functionality, file p6.**

This will guarantee business idempotent behaviour.
NOTE: this is named "PossResend" in FIX - this is an application level resend not a network level
retransmission.
L. Priority
Relative indication of the processing precedence of the message over a (set of) Business
Messages with assigned priorities.
M. Signature
Contains the digital signature of the Business Entity authorised to sign this Business Message.
N. Related
Specifies the Business Application Header(s) of the Business Message(s) to which this Business
Message relates.
Can be used when replying to a query; can also be used when canceling or amending.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 6 March 2024

### Detailed rules, components, tables and diagrams

[Source section and coverage index](../../message-sets/business-application-header/march-2024/documents/src-000011/index.md) provides the exact document outline and extraction inventory for this message range. Source tables and drawings are retained there with their own review dispositions.

| Focused section | File pages |
| --- | --- |
| [2 head.001.001.04 BusinessApplicationHeaderV04](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00004.md) | 4–6 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.2 Structure](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00005.md) | 7–7 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.3 Constraints](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00006.md) | 8–8 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00007.md) | 9–9 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.2 From &lt;Fr&gt; / 2.4.2.2 FinancialInstitutionIdentification &lt;FIId&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00008.md) | 10–10 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.3 To &lt;To&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00009.md) | 11–11 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.3 To &lt;To&gt; / 2.4.3.2 FinancialInstitutionIdentification &lt;FIId&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00010.md) | 12–12 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.4 BusinessMessageIdentifier &lt;BizMsgIdr&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00011.md) | 13–13 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.7 MarketPractice &lt;MktPrctc&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00012.md) | 14–14 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.10 CopyDuplicate &lt;CpyDplct&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00013.md) | 15–15 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.12 Priority &lt;Prty&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00014.md) | 16–16 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.14 Related &lt;Rltd&gt; / 2.4.14.1 CharacterSet &lt;CharSet&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00015.md) | 17–17 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.14 Related &lt;Rltd&gt; / 2.4.14.2 From &lt;Fr&gt; / 2.4.14.2.1 OrganisationIdentification &lt;OrgId&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00016.md) | 18–18 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.14 Related &lt;Rltd&gt; / 2.4.14.2 From &lt;Fr&gt; / 2.4.14.2.2 FinancialInstitutionIdentification &lt;FIId&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00017.md) | 19–19 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.14 Related &lt;Rltd&gt; / 2.4.14.3 To &lt;To&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00018.md) | 20–20 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.14 Related &lt;Rltd&gt; / 2.4.14.3 To &lt;To&gt; / 2.4.14.3.2 FinancialInstitutionIdentification &lt;FIId&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00019.md) | 21–21 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.14 Related &lt;Rltd&gt; / 2.4.14.4 BusinessMessageIdentifier &lt;BizMsgIdr&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00020.md) | 22–22 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.14 Related &lt;Rltd&gt; / 2.4.14.7 MarketPractice &lt;MktPrctc&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00021.md) | 23–23 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.14 Related &lt;Rltd&gt; / 2.4.14.10 CopyDuplicate &lt;CpyDplct&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00022.md) | 24–24 |
| [2 head.001.001.04 BusinessApplicationHeaderV04 / 2.4 Message Building Blocks / 2.4.14 Related &lt;Rltd&gt; / 2.4.14.12 Priority &lt;Prty&gt;](../../message-sets/business-application-header/march-2024/documents/src-000011/sections/section-00023.md) | 25–25 |

## Scoped participants and related business flows

| Reference | Kind | Source |
| --- | --- | --- |
| [bah-authorised-signatory](../../participants/bah-authorised-signatory.md) | participant | src-000012 |
| [bah-business-intermediary](../../participants/bah-business-intermediary.md) | participant | src-000012 |
| [bah-copy-context-account-owner](../../participants/bah-copy-context-account-owner.md) | participant | src-000011 |
| [bah-receiving-messaging-endpoint](../../participants/bah-receiving-messaging-endpoint.md) | participant | src-000011, src-000012 |
| [bah-sending-messaging-endpoint](../../participants/bah-sending-messaging-endpoint.md) | participant | src-000011, src-000012 |
| [bah-signature-verifier](../../participants/bah-signature-verifier.md) | participant | src-000012 |
| [bah-technical-forwarder](../../participants/bah-technical-forwarder.md) | participant | src-000012 |

[Canonical message](index.md) · [Schema structure](structure.md) · [Known gaps](../../../../tracking/issues.md)
