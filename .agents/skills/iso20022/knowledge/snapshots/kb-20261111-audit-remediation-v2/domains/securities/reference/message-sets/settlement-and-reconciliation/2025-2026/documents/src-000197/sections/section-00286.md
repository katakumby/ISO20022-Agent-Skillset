---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.4 Message Building Blocks", "12.4.6 AdditionalQueryParameters <AddtlQryParams>", "12.4.6.2 Reason <Rsn>", "12.4.6.2.9 PendingProcessingReason <PdgPrcgRsn>", "12.4.6.2.9.1 Code <Cd>"]
file_pages: [428]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.4.6.2.9.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 428 to 428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 428

```text
PendingProcessingReason <PdgPrcgRsn> contains one of the following
PendingProcessingReason20Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 428
Or}   Proprietary <Prtry> [1..1] ± 429
12.4.6.2.9.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Datatype: "PendingProcessingReason6Code" on page 2092
CodeName Name Definition
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
CAIS AwaitingSecurities Awaiting financial instruments from a
corporate action or other procedure, for
example, conversion, dematerialisation,
exchange, registration, stamping,
splitting.
YCOL CollateralShortage Insufficient collateral in your account to
execute the instruction.
GLOB GlobalFormSecurities Settlement cannot be executed; financial
instruments are in global form.
LIQU InsufficientCentralBankLiquidity Central bank liquidity is insufficient.
MONY InsufficientMoney Insufficient money in your account.
LACK LackOfSecurities Insufficient financial instruments in your
account.
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
MINO MinimumSettlementAmount Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
NEXT NextProcess Next process is launched. No processing
pending problems to be reported.
NOFX NoForeignExchangeInstruction A foreign exchange instruction from you
is missing.
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 428 March 2026
```

