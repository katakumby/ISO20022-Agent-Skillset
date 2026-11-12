---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.11 RejectionOrRepairStatus44Choice", "35.1.29.11.2 Reason <Rsn>", "35.1.29.11.2.1 Code <Cd>"]
file_pages: [1893]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.11.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1893 to 1893.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1893

```text
Reason <Rsn> contains the following RejectionOrRepairReason39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1893
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1893
35.1.29.11.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Code <Cd> contains one of the following elements (see "RejectionAndRepairReason39Choice" on
page 2004 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2004
Or}   Proprietary <Prtry> [1..1] ± 2004
35.1.29.11.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.12  SettlementStatus19Choice
Definition: Choice of format for the settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1893
Or}   Proprietary <Prtry> [1..1] ± 1894
35.1.29.12.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of settlement of an instruction/financial instrument movement.
Datatype: "SecuritiesSettlementStatus2Code" on page 2143
CodeName Name Definition
PEND Pending Instruction is pending. Settlement at the
instructed settlement date is still
possible.
PENF Failing Instruction is failing. Settlement at the
instructed settlement date is no longer
possible.
USET Unsettled Instruction is unsettled.
SETT Settled Full settlement.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1893 March 2026
```

