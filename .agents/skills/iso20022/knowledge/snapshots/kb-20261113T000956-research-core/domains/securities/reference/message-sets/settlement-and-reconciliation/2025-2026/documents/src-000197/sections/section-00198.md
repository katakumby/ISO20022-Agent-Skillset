---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "9.4 Message Building Blocks", "9.4.6 Status <Sts>", "9.4.6.1 StatusAndReason <StsAndRsn>", "9.4.6.1.5 InstructionProcessingStatus <InstrPrcgSts>", "9.4.6.1.5.1 PendingProcessing <PdgPrcg>", "9.4.6.1.5.1.2 Reason <Rsn>", "9.4.6.1.5.1.2.1 Code <Cd>", "9.4.6.1.5.1.2.1.1 Code <Cd>"]
file_pages: [298]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.018.001.15"]
---

# 9.4.6.1.5.1.2.1.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 298 to 298.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 298

```text
9.4.6.1.5.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Datatype: "PendingProcessingReason5Code" on page 0
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CAIS AwaitingSecurities Awaiting financial instruments from a
corporate action or other procedure, for
example, conversion, dematerialisation,
exchange, registration, stamping,
splitting.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
GLOB GlobalFormSecurities Settlement cannot be executed; financial
instruments are in global form.
PREA YourInstructionOnHold Your instruction is a preadvice, that is,
for matching only.
YCOL CollateralShortage Insufficient collateral in your account to
execute the instruction.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
NOFX NoForeignExchangeInstruction A foreign exchange instruction from you
is missing.
LACK LackOfSecurities Insufficient financial instruments in your
account.
LALO SecuritiesLoanedOut Financial instruments are out on loan.
MONY InsufficientMoney Insufficient money in your account.
MINO MinimumSettlementAmount Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
OTHR Other Other. See Narrative.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
LIQU InsufficientCentralBankLiquidity Central bank liquidity is insufficient.
Approved by the Securities SEG on 27 January 2026 semt.018.001.15
SecuritiesTransactionPendingReportV15
Settlement And Reconciliation - Maintenance 2025 - 2026 298 March 2026
```

