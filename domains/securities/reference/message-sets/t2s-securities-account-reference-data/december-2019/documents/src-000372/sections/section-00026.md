---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["4 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "4.4 Message Building Blocks", "4.4.1 MessageHeader <MsgHdr>", "4.4.1.1 MessageIdentification <MsgId>"]
file_pages: [28]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.020.001.01"]
---

# 4.4.1.1 MessageIdentification <MsgId>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 28 to 28.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 28

```text
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 28
   CreationDateTime <CreDtTm> [0..1] DateTime 28
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 28
4.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 100
4.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 97
4.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
Presence: [0..1]
Definition: Unique identification of the original instruction.
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 82 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 82
   MessageNameIdentification <MsgNmId> [0..1] Text 83
   CreationDateTime <CreDtTm> [0..1] DateTime 83
4.4.2 SecuritiesAccountStatus <SctiesAcctSts>
Presence: [1..1]
Definition: Status of the securities account involved in the originating message.
Impacted by: C1 "PresenceRule", C2 "StatusReasonRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities - Securities Account Reference Data 28 December 2019
```

