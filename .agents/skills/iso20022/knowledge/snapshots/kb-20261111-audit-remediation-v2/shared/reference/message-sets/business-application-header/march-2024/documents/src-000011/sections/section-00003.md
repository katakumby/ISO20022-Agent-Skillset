---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["1 Message Set Overview"]
file_pages: [3]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 1 Message Set Overview

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 3 to 3.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3

```text
1 Message Set Overview
Introduction
TThis document describes the Business Application Header, which includes the changes that have
been implemented as part of the maintenance cycle 2023-2024 (See MCR #234) and approved by the
Cross-SEG Harmonisation Group on 20 February 2024.
1.1 List of MessageDefinitions
The following table lists all MessageDefinitions described in this book.
MessageDefinition Definition
head.001.001.04
BusinessApplicationHeaderV04
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
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Set Overview
Business Application Header - Version 4 3 March 2024
```

