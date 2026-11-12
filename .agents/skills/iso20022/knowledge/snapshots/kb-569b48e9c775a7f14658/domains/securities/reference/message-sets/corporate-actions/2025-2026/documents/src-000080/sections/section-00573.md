---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks", "13.4.4 InstructionCancellationRequestStatus <InstrCxlReqSts>", "13.4.4.3 Rejected <Rjctd>", "13.4.4.3.2 Reason <Rsn>", "13.4.4.3.2.1 ReasonCode <RsnCd>"]
file_pages: [744]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.4.4.3.2.1 ReasonCode <RsnCd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 744 to 744.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 744

```text
Reason <Rsn> contains the following RejectedStatusReason64 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1]  744
{Or     Code <Cd> [1..1] CodeSet 744
Or}     Proprietary <Prtry> [1..1] ± 745
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 745
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
13.4.4.3.2.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Specifies the reason why the instruction or instruction cancellation has been rejected.
ReasonCode <RsnCd> contains one of the following RejectedReason69Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 744
Or}   Proprietary <Prtry> [1..1] ± 745
13.4.4.3.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the reason why the instruction/cancellation request has a rejected
status.
Datatype: "RejectionReason90Code" on page 1239
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
INIR InstructionIrrevocable Instruction is irrevocable.
ULNK InvalidReference Linked reference is unknown.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
DCAN RejectedSinceAlreadyCancelled Cancellation request was rejected since
the instruction has already been
cancelled.
DPRG RejectedSinceInProgress Cancellation request has been rejected
because the instruction process is in
progress or has been processed.
REJA RejectedByIssuerAgent Instruction rejected by the issuer agent.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 744 February 2026
```

