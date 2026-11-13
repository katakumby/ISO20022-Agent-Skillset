---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.5 Pending <Pdg>", "6.4.4.5.2 PendingReason <PdgRsn>", "6.4.4.5.2.2 Reason <Rsn>", "6.4.4.5.2.2.1 ReasonCode <RsnCd>"]
file_pages: [343]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.5.2.2.1 ReasonCode <RsnCd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 343 to 343.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 343

```text
Reason <Rsn> contains the following PendingStatusReason33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReasonCode <RsnCd> [1..1]  343
{Or     Code <Cd> [1..1] CodeSet 343
Or}     Proprietary <Prtry> [1..1] ± 344
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 344
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
6.4.4.5.2.2.1  ReasonCode <RsnCd>
Presence: [1..1]
Definition: Specifies the reason why the instruction's processing is pending.
ReasonCode <RsnCd> contains one of the following PendingReason76Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 343
Or}   Proprietary <Prtry> [1..1] ± 344
6.4.4.5.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Pending reason specified as a code.
Datatype: "PendingReason37Code" on page 1228
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
WCTF AwaitingCounterpartyResponse Allegement has been sent out to
counterparty. Waiting for their response.
BSTR BeforeInstructionPeriod Instruction is submitted before instruction
start date.
BUMM BuyerProtectionMismatch Counterparty disagreement on the
chosen corporate action outturn.
DQCS DisagreementOnCashAmount Unrecognised or invalid instructed cash
amount.
ECRD ElectionToCounterpartyResponseDeadlineMiss
ed
Received after the election to
counterparty response deadline.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 343 February 2026
```

