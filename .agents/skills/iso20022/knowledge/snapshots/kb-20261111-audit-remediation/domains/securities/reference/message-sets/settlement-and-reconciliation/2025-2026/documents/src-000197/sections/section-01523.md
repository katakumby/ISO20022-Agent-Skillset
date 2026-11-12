---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.93 PendingProcessingStatus22Choice", "35.1.29.93.2 Reason <Rsn>", "35.1.29.93.2.1 Code <Cd>", "35.1.29.93.2.1.1 Code <Cd>"]
file_pages: [2021]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.93.2.1.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2021 to 2021.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2021

```text
35.1.29.93.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Datatype: "PendingProcessingReason7Code" on page 2093
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
CDEL ConditionalDelivery Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditional
delivery rules in the market infrastructure
platform for conditional delivery.
CDAC ConditionalDeliveryAwaitingCancellation Awaiting cancellation of one of the party.
CDLR ConditionalDeliveryAwaitingRelease Instruction is in a hold/frozen/preadvice
mode. Market infrastructure platform is
awaiting release.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CVAL CSDValidation Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditions of
a restriction processing type in the
market infrastructure platform.
GLOB GlobalFormSecurities Settlement cannot be executed; financial
instruments are in global form.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
LIQU InsufficientCentralBankLiquidity Central bank liquidity is insufficient.
MONY InsufficientMoney Insufficient money in your account.
LACK LackOfSecurities Insufficient financial instruments in your
account.
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2021 March 2026
```

