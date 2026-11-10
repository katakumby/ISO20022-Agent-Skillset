---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["7 reda.051.001.01 AccountLinkStatusAdviceV01", "7.4 Message Building Blocks", "7.4.2 AccountLinkStatus <AcctLkSts>"]
file_pages: [50]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 7.4.2 AccountLinkStatus <AcctLkSts>

Source: [src-000366](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 50 to 50.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 50

```text
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 66 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 66
   MessageNameIdentification <MsgNmId> [0..1] Text 66
   CreationDateTime <CreDtTm> [0..1] DateTime 66
7.4.2 AccountLinkStatus <AcctLkSts>
Presence: [1..1]
Definition: Represents the processing status.
Impacted by: C6 "StatusReasonRule"
AccountLinkStatus <AcctLkSts> contains the following AccountLinkStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 50
   StatusReason <StsRsn> [0..*]  50
     Reason <Rsn> [1..1]  51
{Or       Code <Cd> [1..1] CodeSet 51
Or}       Proprietary <Prtry> [1..1] Text 51
     AdditionalInformation <AddtlInf> [0..1] Text 51
Constraints
• StatusReasonRule
If Status equals "Rejected" then StatusReason must be present.
7.4.2.1  Status <Sts>
Presence: [1..1]
Definition: Status of the account link instruction.
Datatype: "Status6Code" on page 75
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
7.4.2.2  StatusReason <StsRsn>
Presence: [0..*]
Definition: Underlying reason related to the creation of a transaction.
Approved by the Securities SEG on 21 November 2024. reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities - Link Reference Data 50 December 2024
```

