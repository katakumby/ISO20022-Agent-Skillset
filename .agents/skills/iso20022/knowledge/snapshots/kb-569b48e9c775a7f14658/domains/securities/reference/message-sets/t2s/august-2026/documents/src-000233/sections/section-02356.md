---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.11 Reason18Choice", "82.1.30.11.2 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [3143]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.11.2 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3143 to 3143.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3143

```text
Reason <Rsn> contains the following elements (see "ProprietaryReason4" on page 3139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
82.1.30.11.2  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 3265
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
82.1.30.12  PendingReason28Choice
Definition: Choice of format for the pending reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3143
Or}   Proprietary <Prtry> [1..1] ± 3144
82.1.30.12.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason code why the instruction or request is pending.
Datatype: "PendingReason6Code" on page 3279
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. Processed
on best effort basis.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
OTHR Other Other. See Narrative.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3143 August 2026
```

