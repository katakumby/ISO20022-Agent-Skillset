---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.16 Status", "17.1.16.14 RejectionOrRepairStatus40Choice", "17.1.16.14.2 Reason <Rsn>"]
file_pages: [441]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.16.14.2 Reason <Rsn>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 441 to 441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 441

```text
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
17.1.16.14.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the rejection or repair status.
Reason <Rsn> contains the following RejectionOrRepairReason34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  441
{Or     Code <Cd> [1..1] CodeSet 441
Or}     Proprietary <Prtry> [1..1] ± 442
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 442
17.1.16.14.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RejectionAndRepairReason34Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 441
Or}   Proprietary <Prtry> [1..1] ± 442
17.1.16.14.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason35Code" on page 491
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
441 March 2024
```

