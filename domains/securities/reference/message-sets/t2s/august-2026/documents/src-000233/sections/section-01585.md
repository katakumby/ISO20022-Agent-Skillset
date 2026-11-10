---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["50 reda.030.001.01 SecurityDeletionStatusAdviceV01", "50.4 Message Building Blocks", "50.4.1 MessageHeader <MsgHdr>"]
file_pages: [2210]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.030.001.01"]
---

# 50.4.1 MessageHeader <MsgHdr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2210 to 2210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2210

```text
50.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2210
   CreationDateTime <CreDtTm> [0..1] DateTime 2210
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2210
50.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 3328
50.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
50.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
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
50.4.2 FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Identification of the financial instrument.
Impacted by: C2 "DescriptionPresenceRule", C3 "DescriptionUsageRule", C4 "ISINGuideline", C5
"ISINPresenceRule", C6 "OtherIdentificationPresenceRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.030.001.01 SecurityDeletionStatusAdviceV01
Target2-Securities 2210 August 2026
```

