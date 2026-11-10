---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.14 RejectionOrRepairStatus39Choice", "9.1.21.14.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [284]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.14.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 284 to 284.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 284

```text
9.1.21.14.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
9.1.21.14.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the rejection or repair status.
Reason <Rsn> contains the following RejectionOrRepairReason33 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  284
{Or     Code <Cd> [1..1] CodeSet 284
Or}     Proprietary <Prtry> [1..1] ± 285
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 285
9.1.21.14.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following RejectionAndRepairReason33Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 284
Or}   Proprietary <Prtry> [1..1] ± 285
9.1.21.14.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason34Code" on page 335
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
LATE MarketDeadlineMissed Received after market deadline.
CASH CashAccount Unrecognised or invalid cash account.
NRGM NoMatch More than one instruction match the
criteria.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 284 September 2025
```

