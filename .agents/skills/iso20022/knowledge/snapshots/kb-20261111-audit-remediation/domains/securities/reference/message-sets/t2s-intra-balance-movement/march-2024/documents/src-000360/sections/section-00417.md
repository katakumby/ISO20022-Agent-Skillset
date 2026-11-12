---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.2 Message Datatypes", "17.2.2 CodeSet", "17.2.2.35 SecuritiesSettlementStatus1Code"]
file_pages: [492]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.2.2.35 SecuritiesSettlementStatus1Code

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 492 to 492.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 492

```text
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
17.2.2.35  SecuritiesSettlementStatus1Code
Definition: Provides the status of settlement of an instruction.
Type: CodeSet
CodeName Name Definition
PEND Pending Instruction is pending. Settlement at the
instructed settlement date is still
possible.
PENF Failing Instruction is failing. Settlement at the
instructed settlement date is no longer
possible.
17.2.2.36  StatementUpdateType1Code
Definition: Specifies the nature of a statement update, for example, it is a complete statement.
Type: CodeSet
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
17.2.2.37  TransactionProcessingStatus3Code
Definition: Provides the processing status of a transaction (at account servicer level).
Type: CodeSet
CodeName Name Definition
CAND Cancelled Instruction has been cancelled.
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted for further processing by the
account servicer.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
492 March 2024
```

