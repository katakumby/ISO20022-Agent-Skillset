---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.28 AccountStatusUpdateInstruction1"]
file_pages: [5206]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.28 AccountStatusUpdateInstruction1

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5206 to 5206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5206

```text
Definition: Reason for the status.
Datatype: "Max350Text" on page 5403
66.1.45.28  AccountStatusUpdateInstruction1
Definition: Instruction for a change to an account status and reason for the change.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UpdateInstruction <UpdInstr> [1..1]  5206
{Or     Code <Cd> [1..1] CodeSet 5206
Or}     Proprietary <Prtry> [1..1] ± 5207
   UpdateInstructionReason <UpdInstrRsn> [0..1]  5207
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5207
Or}     Reason <Rsn> [1..*]  C27 5207
       Code <Cd> [0..1]  5208
{Or         Code <Cd> [1..1] CodeSet 5208
Or}         Proprietary <Prtry> [1..1] ± 5208
       AdditionalInformation <AddtlInf> [0..1] Text 5209
66.1.45.28.1  UpdateInstruction <UpdInstr>
Presence: [1..1]
Definition: Type of status change instructed for the account status.
UpdateInstruction <UpdInstr> contains one of the following
AccountStatusUpdateInstruction1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5206
Or}   Proprietary <Prtry> [1..1] ± 5207
66.1.45.28.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of change to the account status expressed as a code.
Datatype: "AccountStatusUpdateInstruction1Code" on page 5275
CodeName Name Definition
CLOS Close Account is to be closed.
REAC Reactive Account is to be reactivated, any
previous instruction to close the account
is rescinded.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5206 May 2026
```

