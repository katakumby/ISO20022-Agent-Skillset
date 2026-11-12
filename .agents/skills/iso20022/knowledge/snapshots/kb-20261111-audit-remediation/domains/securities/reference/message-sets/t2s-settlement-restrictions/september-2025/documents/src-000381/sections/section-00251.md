---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.28 RejectionOrRepairStatus40Choice", "9.1.21.28.2 Reason <Rsn>"]
file_pages: [297]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.28.2 Reason <Rsn>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 297 to 297.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 297

```text
9.1.21.28.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the rejection or repair status.
Reason <Rsn> contains the following RejectionOrRepairReason34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  297
{Or     Code <Cd> [1..1] CodeSet 297
Or}     Proprietary <Prtry> [1..1] ± 297
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 298
9.1.21.28.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RejectionAndRepairReason34Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 297
Or}   Proprietary <Prtry> [1..1] ± 297
9.1.21.28.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason35Code" on page 336
CodeName Name Definition
CASH CashAccount Unrecognised or invalid cash account.
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
LATE MarketDeadlineMissed Received after market deadline.
DDAT SettlementDateRejection Unrecognised or invalid settlement date.
NRGN NotFoundRejection Instruction could not be found.
OTHR Other Other. See Narrative.
INVM InvalidModificationRequest Invalid or unrecognized modification
request.
INVL InvalidLink Invalid or unrecognized link.
9.1.21.28.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 297 September 2025
```

