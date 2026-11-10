---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["2 head.001.001.04 BusinessApplicationHeaderV04", "2.4 Message Building Blocks", "2.4.10 CopyDuplicate <CpyDplct>"]
file_pages: [15]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.04"]
---

# 2.4.10 CopyDuplicate <CpyDplct>

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 15 to 15.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 15

```text
Definition: Processing date and time indicated by the sender for the receiver of the business message.
This date may be different from the date and time provided in the CreationDate.
Usage: Market practice or bilateral agreement should specify how this element should be used.
Datatype: "ISODateTime" on page 54
2.4.10 CopyDuplicate <CpyDplct>
Presence: [0..1]
Definition: Indicates whether the message is a Copy, a Duplicate or a copy of a duplicate of a previously
sent ISO 20022 Message.
Datatype: "CopyDuplicate1Code" on page 51
CodeName Name Definition
CODU CopyDuplicate Message is being sent as a copy to a
party other than the account owner, for
information purposes and the message
is a duplicate of a message previously
sent.
COPY Copy Message is being sent as a copy to a
party other than the account owner, for
information purposes.
DUPL Duplicate Message is for information/confirmation
purposes. It is a duplicate of a message
previously sent.
2.4.11 PossibleDuplicate <PssblDplct>
Presence: [0..1]
Definition: Flag indicating if the Business Message exchanged between the MessagingEndpoints is
possibly a duplicate.
If the receiving MessagingEndpoint did not receive the original, then this Business Message should be
processed as if it were the original.
If the receiving MessagingEndpoint did receive the original, then it should perform necessary actions to
avoid processing this Business Message again.
This will guarantee business idempotent behaviour.
NOTE: this is named "PossResend" in FIX - this is an application level resend not a network level
retransmission.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 55):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 head.001.001.04 BusinessApplicationHeaderV04
Business Application Header - Version 4 15 March 2024
```

