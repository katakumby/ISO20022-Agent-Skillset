---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "4.4 Message Building Blocks", "4.4.1 MessageHeader <MsgHdr>", "4.4.1.2 CreationDateTime <CreDtTm>"]
file_pages: [28]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 4.4.1.2 CreationDateTime <CreDtTm>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 28 to 28.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 28

```text
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 78
4.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 75
4.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
Presence: [0..1]
Definition: Unique identification of the original instruction.
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 66 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 66
   MessageNameIdentification <MsgNmId> [0..1] Text 66
   CreationDateTime <CreDtTm> [0..1] DateTime 66
4.4.2 SecurityCSDLinkStatus <SctyCSDLkSts>
Presence: [1..1]
Definition: Represents the processing status.
Impacted by: C8 "StatusReasonRule"
SecurityCSDLinkStatus <SctyCSDLkSts> contains the following CSDLinkStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 29
   StatusReason <StsRsn> [0..*]  29
     Reason <Rsn> [1..1]  29
{Or       Code <Cd> [1..1] CodeSet 29
Or}       Proprietary <Prtry> [1..1] Text 30
     AdditionalInformation <AddtlInf> [0..1] Text 30
Approved by the Securities SEG on 21 November 2024. reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities - Link Reference Data 28 December 2024
```

