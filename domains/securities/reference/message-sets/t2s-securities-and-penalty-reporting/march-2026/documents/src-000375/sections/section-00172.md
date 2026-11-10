---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.9 RelatedTransaction <RltdTx>", "6.4.6.11.4.9.3 TransactionDetails <TxDtls>", "6.4.6.11.4.9.3.14 SettlementStatusFailing <SttlmStsFlng>", "6.4.6.11.4.9.3.14.2 Reason <Rsn>", "6.4.6.11.4.9.3.14.2.1 Code <Cd>"]
file_pages: [238, 239, 240]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.9.3.14.2.1 Code <Cd>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 238 to 240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 238

```text
Definition: Specifies the reason of the failing status.
Reason <Rsn> contains the following FailingReason13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  238
{Or     Code <Cd> [1..1] CodeSet 238
Or}     Proprietary <Prtry> [1..1] ± 241
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 242
6.4.6.11.4.9.3.14.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing status.
Code <Cd> contains one of the following FailingReason18Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 238
Or}   Proprietary <Prtry> [1..1] ± 241
6.4.6.11.4.9.3.14.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a failing settlement status.
Datatype: "FailingReason5Code" on page 507
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
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 238 March 2026
```

## File page 239

```text
CodeName Name Definition
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
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 239 March 2026
```

## File page 240

```text
CodeName Name Definition
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
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 240 March 2026
```

