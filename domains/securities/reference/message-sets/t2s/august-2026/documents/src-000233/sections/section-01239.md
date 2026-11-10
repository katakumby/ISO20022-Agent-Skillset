---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["29 reda.008.001.01 SecurityCreationStatusAdviceV01", "29.4 Message Building Blocks", "29.4.1 MessageHeader <MsgHdr>"]
file_pages: [1755]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.008.001.01"]
---

# 29.4.1 MessageHeader <MsgHdr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1755 to 1755.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1755

```text
29.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 1755
   CreationDateTime <CreDtTm> [0..1] DateTime 1755
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 1755
29.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 3328
29.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
29.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
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
29.4.2 FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Identification of the financial instrument.
Impacted by: C2 "DescriptionPresenceRule", C3 "DescriptionUsageRule", C4 "ISINGuideline", C5
"ISINPresenceRule", C6 "OtherIdentificationPresenceRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.008.001.01 SecurityCreationStatusAdviceV01
Target2-Securities 1755 August 2026
```

