---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.2 CodeSet", "9.2.2.38 RejectionReason35Code"]
file_pages: [336]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.2.38 RejectionReason35Code

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 336 to 336.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 336

```text
CodeName Name Definition
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
9.2.2.38  RejectionReason35Code
Definition: Specifies the reason why the instruction/cancellation request has a rejected status.
Type: CodeSet
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
9.2.2.39  RestrictionReference1Code
Definition: Specifies the restriction references to be applied to a transaction.
Type: CodeSet
Format
minLength 1
maxLength 4
CodeName Name Definition
ADDC AddCashRestrictionReference Addition of a cash restriction reference
representing a cash sub-balance to be
utilised within the settlement instruction
for the debiting or crediting of cash.
ADDS AddSecuritiesRestrictionReference Addition of a securities restriction
reference representing a securities sub-
position to be utilised within the
settlement instruction for the delivery or
receipt of securities.
REMC RemoveCashRestrictionReference Removal of a cash restriction reference,
already present within the settlement
instruction, representing a cash sub-
balance to be utilised within the
settlement instruction for the debiting or
crediting of cash.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 336 September 2025
```

