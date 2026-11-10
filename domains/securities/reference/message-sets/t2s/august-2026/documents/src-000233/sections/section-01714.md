---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["64 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "64.4 Message Building Blocks", "64.4.1 MessageHeader <MsgHdr>", "64.4.1.2 CreationDateTime <CreDtTm>"]
file_pages: [2362]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 64.4.1.2 CreationDateTime <CreDtTm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2362 to 2362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2362

```text
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 3328
64.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
64.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
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
64.4.2 SecurityCSDLinkStatus <SctyCSDLkSts>
Presence: [1..1]
Definition: Represents the processing status.
Impacted by: C8 "StatusReasonRule"
SecurityCSDLinkStatus <SctyCSDLkSts> contains the following CSDLinkStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 2363
   StatusReason <StsRsn> [0..*]  2363
     Reason <Rsn> [1..1]  2363
{Or       Code <Cd> [1..1] CodeSet 2363
Or}       Proprietary <Prtry> [1..1] Text 2364
     AdditionalInformation <AddtlInf> [0..1] Text 2364
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities 2362 August 2026
```

