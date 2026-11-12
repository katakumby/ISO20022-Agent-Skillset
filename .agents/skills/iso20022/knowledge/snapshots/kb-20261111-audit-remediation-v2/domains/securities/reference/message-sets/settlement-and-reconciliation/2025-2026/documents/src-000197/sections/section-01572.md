---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.70 PendingFailingReason1Code"]
file_pages: [2090, 2091]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.70 PendingFailingReason1Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2090 to 2091.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2090

```text
CodeName Name Definition
PAIN PartialSettlement Confirmation is for partial settlement.
Part of the transaction remains
unsettled.
PARC PartiallyConfirmed Confirmation is for partial settlement. No
additional settlement will take place.
35.2.2.70  PendingFailingReason1Code
Definition: Specifies the reason the transaction/instruction is pending or failing settlement. Settlement
on the instructed settlement date is still possible, status is pending. Settlement on the instructed
settlement date is no longer possible, status is failing.
Type: CodeSet
CodeName Name Definition
OTHR Other Other. See Narrative.
35.2.2.71  PendingProcessingReason3Code
Definition: Specifies the reason the transaction/instruction is failing settlement. Settlement on the
instructed settlement date is no longer possible.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. Processed
on best effort basis.
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
NEXT NextProcess Next process is launched. No processing
pending problems to be reported.
MINO MinimumSettlementAmount Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
OTHR Other Other. See Narrative.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
CERT WrongCertificatesNumbers Certificate number error.
35.2.2.72  PendingProcessingReason5Code
Definition: Specifies the reason the transaction/instruction is pending or failing settlement. Settlement
on the instructed settlement date is still possible, status is pending. Settlement on the instructed
settlement date is no longer possible, status is failing.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2090 March 2026
```

## File page 2091

```text
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
CERT WrongCertificatesNumbers Certificate number error.
NEXT NextProcess Next process is launched. No processing
pending problems to be reported.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2091 March 2026
```

