---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04"]
file_pages: [4, 5, 6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2 head.001.001.04 BusinessApplicationHeaderV04

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 4 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
2 head.001.001.04
BusinessApplicationHeaderV04
2.1 MessageDefinition Functionality
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
```

## File page 5

```text
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
```

## File page 6

```text
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
```

