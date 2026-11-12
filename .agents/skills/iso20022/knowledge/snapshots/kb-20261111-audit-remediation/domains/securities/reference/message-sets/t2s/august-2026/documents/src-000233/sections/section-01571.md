---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["48 reda.028.001.01 CollateralDataStatusAdviceV01", "48.4 Message Building Blocks", "48.4.1 MessageHeader <MsgHdr>", "48.4.1.1 MessageIdentification <MsgId>"]
file_pages: [2196]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 48.4.1.1 MessageIdentification <MsgId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2196 to 2196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2196

```text
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2196
   CreationDateTime <CreDtTm> [0..1] DateTime 2196
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2196
48.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 3328
48.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
48.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
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
48.4.2 StatusReason <StsRsn>
Presence: [0..1]
Definition: Specifies the reason for the status report.
Impacted by: C8 "StatusReasonRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities 2196 August 2026
```

