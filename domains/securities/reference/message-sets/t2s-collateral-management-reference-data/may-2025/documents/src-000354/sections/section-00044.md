---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["7 reda.044.001.01 EligibleCounterpartCSDStatusAdviceV01", "7.4 Message Building Blocks", "7.4.1 MessageHeader <MsgHdr>", "7.4.1.1 MessageIdentification <MsgId>"]
file_pages: [48]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.044.001.01"]
---

# 7.4.1.1 MessageIdentification <MsgId>

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 48 to 48.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 48

```text
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 48
   CreationDateTime <CreDtTm> [0..1] DateTime 48
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 48
7.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 83
7.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 80
7.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
Presence: [0..1]
Definition: Unique identification of the original instruction.
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 69 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 69
   MessageNameIdentification <MsgNmId> [0..1] Text 69
   CreationDateTime <CreDtTm> [0..1] DateTime 69
7.4.2 StatusReason <StsRsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Impacted by: C1 "StatusReasonRule"
Approved by the Securities SEG on 17 April 2025. reda.044.001.01
EligibleCounterpartCSDStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 48 May 2025
```

