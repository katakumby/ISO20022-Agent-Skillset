---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.47 FailingReason4Code"]
file_pages: [2072, 2073, 2074]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.47 FailingReason4Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2072 to 2074.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2072

```text
35.2.2.47  FailingReason4Code
Definition: Specifies the reason the transaction/instruction is failing settlement. Settlement on the
instructed settlement date is no longer possible.
Type: CodeSet
CodeName Name Definition
AWMO AwaitingMoney Financial instruments are delivered, but
still awaiting money from counterparty.
BYIY BuyInProcedure Buy-in procedure has started on the
market (on your behalf if your instruction
is a receipt, by the counterparty if your
instruction is a delivery).
CLAT CounterpartyTooLateForSettlement Counterparty's instruction was too late
for settlement, that is the matching or
settlement problems was solved too late.
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. Processed
on best effort basis.
CANR CancellationConfirmationRequested Instruction was in suspense. Suspense
period is finished so your cancellation or
confirmation of instruction is required.
CAIS AwaitingSecurities Awaiting financial instruments from a
corporate action or other procedure, for
example, conversion, dematerialisation,
exchange, registration, stamping,
splitting.
OBJT UnderObjection Financial instruments are stolen, in
dispute, under objection etc.
AWSH AwaitingSecuritiesFromCounterparty Financial instruments have not yet been
received from the counterparty (if receive
against payment trade), the money has
been delivered.
PHSE PhysicalDeliveryDelay Settlement is physical. Financial
instruments are being delivered.
STCD ConfirmationDiscrepency Discrepancy in the settlement
confirmation.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
MLAT MoneySecuritiesTooLateForSettlement Covering money/financial instruments
were received too late for completing
settlement on a same day basis.
DOCC AwaitingDocumentsOrEndorsementsFromCoun
terparty
Awaiting documents or endorsements
from counterparty.
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
CHAS EnquirySent A chaser/enquiry has been sent.
NEWI NewIssues Financial instrument is a new issue and
not yet available/tradable.
CLAC CounterpartyInsufficientSecurities Insufficient deliverable financial
instruments in counterparty's account or
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2072 March 2026
```

## File page 2073

```text
CodeName Name Definition
counterparty does not hold financial
instruments.
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
GLOB GlobalFormSecurities Settlement cannot be executed; financial
instruments are in global form.
PREA YourInstructionOnHold Your instruction is a preadvice, that is,
for matching only.
PART TradeSettlesInPartials Trade will settle in partials.
NOFX NoForeignExchangeInstruction A foreign exchange instruction from you
is missing.
CMON CounterpartyInsufficientMoney Insufficient money in counterparty's
account.
YCOL CollateralShortage Insufficient collateral in your account to
execute the instruction.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
DEPO RefusedDepositForIssueOfDepositaryReceipts Deposit of shares for the issuing of
depositary receipts has been refused.
The allotment granted by the issuer is
exceeded by your transaction.
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
INCA IncomeAdjustementRequired Financial instruments require income
adjustment, for example, dividend or
interest.
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
LACK LackOfSecurities Insufficient financial instruments in your
account.
LALO SecuritiesLoanedOut Financial instruments are out on loan.
MONY InsufficientMoney Insufficient money in your account.
NCON ConfirmationNotReceived Confirmation of settlement has not yet
been received.
REFS NotInGoodOrder Delivery/receipt was refused because
physical financial instruments are not in
good order.
SDUT LackOfStampDutyInformation Stamp duty information is missing.
BATC ProcessingBatchDifference Processing batch differs in the
counterparty's instruction, for example,
daytime/real-time versus overnight.
CYCL AwaitingNextSettlementCycle Your instruction is confirmed in the local
market or is ready for settlement,
awaiting next settlement cycle.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2073 March 2026
```

## File page 2074

```text
CodeName Name Definition
SBLO SecuritiesBlocked Financial instruments are blocked due to
a corporate action event, realignment,
etc.
CPEC CounterpartyInReceivership Counterparty is in receivership (form of
bankruptcy where a court appointed
person - the receiver - manages the
affairs of the business).
MINO MinimumSettlementAmount Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
IAAD StatusReasonInvestigation Pending reason being investigated.
OTHR Other Other. See Narrative.
PHCK PhysicalSecuritiesVerification Physical financial instruments have been
received and are being checked for
authenticity.
BENO BeneficialOwnershipDisagreement Disagreement in beneficial ownership.
BOTH BothInstructionsOnHold Counterparty's instruction and your
instruction are on hold/frozen/ in a
preadvice mode.
CLHT ClearingHouseTrade Instructed settlement date does not
agree with the settlement date on the
clearing house trade, that is, a specific
type of trade in India.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
DISA NaturalDisaster Exceptional closing of all financial
institutions due to natural disaster, for
example, earthquake.
DKNY CounterpartyReturnedShares Counterparty has returned or refuses the
securities.
FROZ SecuritiesFrozenAtCSD Financial instruments are blocked at the
Central Security Depository (CSD)
following a corporate event.
LAAW AwaitingOtherTransaction Awaiting settlement of a purchase to
cover failing positions.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
LIQU InsufficientCentralBankLiquidity Central bank liquidity is insufficient.
PRCY CounterpartyInstructionOnHold Counterparty's instruction is a preadvice,
that is, for matching only.
REGT CertificatesRejected Certificates have been lodged with the
registrar but rejected due to incomplete
documentation or foreign ownership
limitation reached.
SETS SettlementSystemMethodModified Settlement system/method has been
modified at central securities depository
to allow settlement.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2074 March 2026
```

