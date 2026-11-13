---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.21 RejectionOrRepairStatus39Choice", "82.1.30.21.2 Reason <Rsn>"]
file_pages: [3157]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.21.2 Reason <Rsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3157 to 3157.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3157

```text
82.1.30.21.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the rejection or repair status.
Reason <Rsn> contains the following RejectionOrRepairReason33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3157
{Or     Code <Cd> [1..1] CodeSet 3157
Or}     Proprietary <Prtry> [1..1] ± 3157
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3158
82.1.30.21.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RejectionAndRepairReason33Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3157
Or}   Proprietary <Prtry> [1..1] ± 3157
82.1.30.21.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason34Code" on page 3284
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
LATE MarketDeadlineMissed Received after market deadline.
CASH CashAccount Unrecognised or invalid cash account.
NRGM NoMatch More than one instruction match the
criteria.
NRGN NotFoundRejection Instruction could not be found.
OTHR Other Other. See Narrative.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
82.1.30.21.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3157 August 2026
```

