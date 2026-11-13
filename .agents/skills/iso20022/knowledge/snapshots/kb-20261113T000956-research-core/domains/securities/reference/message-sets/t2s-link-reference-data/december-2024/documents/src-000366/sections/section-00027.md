---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["4 reda.047.001.01 SecurityCSDLinkStatusAdviceV01", "4.4 Message Building Blocks", "4.4.2 SecurityCSDLinkStatus <SctyCSDLkSts>", "4.4.2.1 Status <Sts>"]
file_pages: [29]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.047.001.01"]
---

# 4.4.2.1 Status <Sts>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 29 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 29

```text
Constraints
• StatusReasonRule
If Status equals "Rejected" then StatusReason must be present.
4.4.2.1  Status <Sts>
Presence: [1..1]
Definition: Status of the party maintenance instruction.
Datatype: "Status6Code" on page 75
CodeName Name Definition
REJT Rejected Instruction has been rejected.
COMP Completed Processing has been completed.
QUED Queued Instruction is queued.
4.4.2.2  StatusReason <StsRsn>
Presence: [0..*]
Definition: Underlying reason related to the creation of a transaction.
StatusReason <StsRsn> contains the following StatusReasonInformation10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  29
{Or     Code <Cd> [1..1] CodeSet 29
Or}     Proprietary <Prtry> [1..1] Text 30
   AdditionalInformation <AddtlInf> [0..1] Text 30
4.4.2.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Reason <Rsn> contains one of the following StatusReason6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 29
Or}   Proprietary <Prtry> [1..1] Text 30
4.4.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalStatusReason1Code" on page 74
Approved by the Securities SEG on 21 November 2024. reda.047.001.01 SecurityCSDLinkStatusAdviceV01
Target2-Securities - Link Reference Data 29 December 2024
```

