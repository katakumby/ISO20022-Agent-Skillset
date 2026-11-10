---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.1 SettlementStatus32Choice", "35.1.29.1.1 Pending <Pdg>", "35.1.29.1.1.1 NoSpecifiedReason <NoSpcfdRsn>"]
file_pages: [1862, 1863, 1864]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.1.1.1 NoSpecifiedReason <NoSpcfdRsn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1862 to 1864.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1862

```text
35.1.29.1.1.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.1.1.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the pending status.
Reason <Rsn> contains the following PendingReason32 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  1862
{Or     Code <Cd> [1..1] CodeSet 1862
Or}     Proprietary <Prtry> [1..1] ± 1865
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1866
35.1.29.1.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Code <Cd> contains one of the following PendingReason69Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1862
Or}   Proprietary <Prtry> [1..1] ± 1865
35.1.29.1.1.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Datatype: "PendingReason28Code" on page 2101
CodeName Name Definition
AWMO AwaitingMoney Financial instruments are delivered, but
still awaiting money from counterparty.
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. Processed
on best effort basis.
CAIS AwaitingSecurities Awaiting financial instruments from a
corporate action or other procedure, for
example, conversion, dematerialisation,
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1862 March 2026
```

## File page 1863

```text
CodeName Name Definition
exchange, registration, stamping,
splitting.
REFU InstructionRefusedOrNotRecognised Instruction has been refused or not
recognised and is represented
automatically.
AWSH AwaitingSecuritiesFromCounterparty Financial instruments have not yet been
received from the counterparty (if receive
against payment trade), the money has
been delivered.
PHSE PhysicalDeliveryDelay Settlement is physical. Financial
instruments are being delivered.
TAMM TradeAmendedInMarket Trade is being amended in the market.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
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
NMAS NoMatchingRequired Instruction has not been matched;
matching process is not required.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1863 March 2026
```

## File page 1864

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
FUTU AwaitingSettlementDate Awaiting settlement date. No settlement
problems to be reported.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1864 March 2026
```

