---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.40 Linkages59", "35.1.16.40.2 MessageNumber <MsgNb>"]
file_pages: [1575]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.40.2 MessageNumber <MsgNb>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1575 to 1575.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1575

```text
Constraints
• WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and which
must be executed together. Even if one single transactions/instructions/notifications can not be
executed, then all the other transactions/instructions/notifications must also be kept pending.
Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/instructions/
notifications.
35.1.16.40.2  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C20 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber5Choice"
on page 1444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 1444
Or   LongNumber <LngNb> [1..1] Text 1445
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 1445
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
35.1.16.40.3  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1575 March 2026
```

