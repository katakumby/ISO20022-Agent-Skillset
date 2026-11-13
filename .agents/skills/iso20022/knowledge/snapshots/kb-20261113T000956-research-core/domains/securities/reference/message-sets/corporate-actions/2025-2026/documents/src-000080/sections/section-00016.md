---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "2.4 Message Building Blocks", "2.4.14 Related <Rltd>", "2.4.14.9 PossibleDuplicate <PssblDplct>"]
file_pages: [21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.02"]
---

# 2.4.14.9 PossibleDuplicate <PssblDplct>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 21 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
Datatype: "CopyDuplicate1Code" on page 1166
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
2.4.14.9  PossibleDuplicate <PssblDplct>
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
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
2.4.14.10  Priority <Prty>
Presence: [0..1]
Definition: Relative indication of the processing precedence of the message over a (set of) Business
Messages with assigned priorities.
Impacted by: C7 "ValidationByTable"
Datatype: "BusinessMessagePriorityCode" on page 1165
Approved by the Securities SEG on 27 January 2026 head.001.001.02 BusinessApplicationHeaderV02
Corporate Actions - Maintenance 2025 - 2026 21 February 2026
```

