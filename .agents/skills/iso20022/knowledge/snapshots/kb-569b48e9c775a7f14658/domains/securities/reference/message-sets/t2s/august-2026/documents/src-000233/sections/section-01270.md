---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.1 MessageHeader <MsgHdr>"]
file_pages: [1803]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.1 MessageHeader <MsgHdr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1803 to 1803.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1803

```text
32.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Point to point reference elements, as assigned by the instructing party, to unambiguously
identify the report message.
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 1803
   CreationDateTime <CreDtTm> [0..1] DateTime 1803
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 1803
32.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 3328
32.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
32.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
Presence: [0..1]
Definition: Unique identification of the original instruction.
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 3002 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3002
   MessageNameIdentification <MsgNmId> [0..1] Text 3002
   CreationDateTime <CreDtTm> [0..1] DateTime 3002
32.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Provides details on the page number of the message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1803 August 2026
```

