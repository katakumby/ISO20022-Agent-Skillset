---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["67 reda.051.001.01 AccountLinkStatusAdviceV01", "67.4 Message Building Blocks", "67.4.2 AccountLinkStatus <AcctLkSts>"]
file_pages: [2384]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 67.4.2 AccountLinkStatus <AcctLkSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2384 to 2384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2384

```text
OriginalBusinessInstruction <OrgnlBizInstr> contains the following elements (see
"OriginalBusinessInstruction1" on page 3002 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3002
   MessageNameIdentification <MsgNmId> [0..1] Text 3002
   CreationDateTime <CreDtTm> [0..1] DateTime 3002
67.4.2 AccountLinkStatus <AcctLkSts>
Presence: [1..1]
Definition: Represents the processing status.
Impacted by: C6 "StatusReasonRule"
AccountLinkStatus <AcctLkSts> contains the following AccountLinkStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1] CodeSet 2384
   StatusReason <StsRsn> [0..*]  2384
     Reason <Rsn> [1..1]  2385
{Or       Code <Cd> [1..1] CodeSet 2385
Or}       Proprietary <Prtry> [1..1] Text 2385
     AdditionalInformation <AddtlInf> [0..1] Text 2385
Constraints
• StatusReasonRule
If Status equals "Rejected" then StatusReason must be present.
67.4.2.1  Status <Sts>
Presence: [1..1]
Definition: Status of the account link instruction.
Datatype: "Status6Code" on page 3305
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
67.4.2.2  StatusReason <StsRsn>
Presence: [0..*]
Definition: Underlying reason related to the creation of a transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities 2384 August 2026
```

