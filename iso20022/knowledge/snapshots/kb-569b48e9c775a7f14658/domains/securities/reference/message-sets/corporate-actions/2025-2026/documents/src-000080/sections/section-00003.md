---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [4, 5, 6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.02", "seev.031.001.16", "seev.032.001.09", "seev.033.001.14", "seev.034.001.16", "seev.035.001.17", "seev.036.001.17", "seev.037.001.17", "seev.038.001.09", "seev.039.001.13", "seev.040.001.13", "seev.041.001.15", "seev.042.001.14", "seev.044.001.13"]
---

# 1 Message Set Overview

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 4 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4

```text
1 Message Set Overview
Introduction
This document describes the Corporate Actions message set. It includes the new version of the
MessageDefinitions that have been added as part of the maintenance cycle 2025-2026 (See MCR
#269, 270) and approved by the Securities Standards Evaluation Group on 27 January 2026.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
head.001.001.02
BusinessApplicationHeaderV02
The Business Layer deals with Business Messages.
The behaviour of the Business Messages is fully
described by the Business Transaction and the
structure of the Business Messages is fully described
by the Message Definitions and related Message
Rules, Rules and Market Practices. All of which are
registered in the ISO 20022 Repository.
A single new Business Message (with its
accompagnying business application header) is
created - by the sending MessagingEndpoint - for each
business event; that is each interaction in a Business
Transaction. A Business Message adheres to the
following principles:
" A Business Message (and its business application
header) must not contain information about the
Message Transport System or the mechanics or
mechanism of message sending, transportation, or
receipt.
" A Business Message must be comprehensible
outside of the context of the Transport Message. That
is the Business Message must not require knowledge
of the Transport Message to be understood.
" A Business Message may contain headers, footers,
and envelopes that are meaningful for the business.
When present, they are treated as any other message
content, which means that they are considered part of
the Message Definition of the Business Message and
as such will be part of the ISO 20022 Repository.
" A Business Message refers to Business Actors by
their Name. Each instance of a Business Actor has one
Name. The Business Actor must not be referred to in
the Transport Layer.
Specific usage of this BusinessMessageHeader may
be defined by the relevant SEG.
seev.031.001.16
CorporateActionNotificationV16
The CorporateActionNotification message is sent by an
account servicer to an account owner or its designated
agent to notify details of a corporate action event and
optionally account information and preliminary
information about eligible balance and entitlements.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Corporate Actions - Maintenance 2025 - 2026 4 February 2026
```

## File page 5

```text
MessageDefinition Definition
It may also include possible elections or choices
available to the account owner. The account servicer
can initially send the CorporateActionNotification
message as a preliminary advice, subsequently
replaced by another CorporateActionNotification
message with complete or confirmed information.
It may also be sent to an account owner or its
designated agent, to remind of event details and/or of
missing or incomplete instructions for a corporate
action event.
seev.032.001.09
CorporateActionEventProcessingStatusAdviceV
09
An account servicer sends the
CorporateActionEventProcessingStatusAdvice
message to an account owner or its designated agent
to report processing status of a corporate action event.
The account servicer uses this message to provide a
reason as to why a corporate action event has not
been completed by the announced payment dates.
seev.033.001.14
CorporateActionInstructionV14
The CorporateActionInstruction message is sent by an
account owner to an account servicer to instruct
election on a corporate action event.
This message is used to provide the custodian with
instructions on how the account owner wishes to
proceed with a corporate action event. Instructions
include investment decisions regarding the exercise of
rights issues, the election of stock or cash when the
option is available, and decisions on the conversion or
tendering of securities.
seev.034.001.16
CorporateActionInstructionStatusAdviceV16
The CorporateActionInstructionStatusAdvice message
is sent by an account servicer to an account owner or
its designated agent, to report the status of a received
corporate action election instruction.
This message is used to advise the status, or a change
in status, of a corporate action-related transaction
previously instructed by, or executed on behalf of, the
account owner. This will include the acknowledgement/
rejection of a corporate action instruction.
seev.035.001.17
CorporateActionMovementPreliminaryAdviceV1
7
The CorporateActionMovementPreliminaryAdvice
message is sent by an account servicer to an account
owner or its designated agent:
- to advise about the eligible balance and entitlements
and,
- to pre-advise an upcoming posting or reversal of
securities and/or cash postings.
seev.036.001.17
CorporateActionMovementConfirmationV17
The CorporateActionMovementConfirmation message
is sent by an account servicer to an account owner or
its designated agent to confirm the posting of securities
or cash as a result of a corporate action event.
seev.037.001.17
CorporateActionMovementReversalAdviceV17
The CorporateActionMovementReversalAdvice
message is sent by an account servicer to an account
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Corporate Actions - Maintenance 2025 - 2026 5 February 2026
```

## File page 6

```text
MessageDefinition Definition
owner or its designated agent to reverse a previously
confirmed posting of securities or cash.
seev.038.001.09
CorporateActionNarrativeV09
The CorporateActionNarrative message is sent
between an account servicer and an account owner or
its designated agent to cater for such processes that
cannot be handled using messages such as the
CorporateActionNotification. It is not to be used for
event narrative as that should be included in the
CorporateActionNotification. Examples of when the
CorporateActionNarrative message may be used
include tax reclaims, restrictions, documentation
requirements. This message should only be used when
bilaterally agreed. This message is bi-directional.
seev.039.001.13
CorporateActionCancellationAdviceV13
The CorporateActionCancellationAdvice message is
sent by an account servicer to an account owner or its
designated agent to cancel a previously announced
corporate action event in case of error from the
account servicer or in case of withdrawal by the issuer.
seev.040.001.13
CorporateActionInstructionCancellationRequest
V13
The CorporateActionInstructionCancellationRequest
message is sent by an account owner to an account
servicer to request cancellation of a previously sent
corporate action election instruction.
seev.041.001.15
CorporateActionInstructionCancellationRequest
StatusAdviceV15
The
CorporateActionInstructionCancellationRequestStatus
Advice message is sent by an account servicer to an
account owner or its designated agent to report the
status of a previously received
CorporateActionInstructionCancellationRequest
message sent by the account owner. This will include
the acknowledgement/rejection of a request to cancel
an outstanding instruction.
seev.042.001.14
CorporateActionInstructionStatementReportV14
The CorporateActionInstructionStatementReport
message is sent by an account servicer to an account
owner or its designated agent to report balances at the
safekeeping account level for one or more corporate
action events or at the corporate action event level for
one or more safekeeping accounts.
seev.044.001.13
CorporateActionMovementPreliminaryAdviceCa
ncellationAdviceV13
The
CorporateActionMovementPreliminaryAdviceCancellati
onAdvice message is sent by an account servicer to an
account owner or its designated agent to cancel a
previously announced
CorporateActionMovementPreliminaryAdvice.
Approved by the Securities SEG on 27 January 2026 Message Set Overview
Corporate Actions - Maintenance 2025 - 2026 6 February 2026
```

