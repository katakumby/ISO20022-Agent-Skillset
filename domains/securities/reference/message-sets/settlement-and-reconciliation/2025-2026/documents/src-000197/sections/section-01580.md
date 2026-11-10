---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.80 PendingReason32Code"]
file_pages: [2105, 2106, 2107, 2108]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.80 PendingReason32Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2105 to 2108.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2105

```text
CodeName Name Definition
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
PART TradeSettlesInPartials Trade will settle in partials.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
FUTU AwaitingSettlementDate Awaiting settlement date. No settlement
problems to be reported.
LACK LackOfSecurities Insufficient financial instruments in your
account.
SBLO SecuritiesBlocked Financial instruments are blocked due to
a corporate action event, realignment,
etc.
OTHR Other Other. See Narrative.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
35.2.2.80  PendingReason32Code
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
OTHR Other Other. See Narrative.
35.2.2.81  PendingReason33Code
Definition: Specifies the reason the transaction/instruction is pending or failing settlement. Settlement
on the instructed settlement date is still possible, status is pending. Settlement on the instructed
settlement date is no longer possible, status is failing.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2105 March 2026
```

## File page 2106

```text
Type: CodeSet
CodeName Name Definition
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
DOCC AwaitingDocumentsOrEndorsementsFromCoun
terparty
Awaiting documents or endorsements
from counterparty.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
AWMO AwaitingMoney Financial instruments are delivered, but
still awaiting money from counterparty.
CYCL AwaitingNextSettlementCycle Your instruction is confirmed in the local
market or is ready for settlement,
awaiting next settlement cycle.
LAAW AwaitingOtherTransaction Awaiting settlement of a purchase to
cover failing positions.
CAIS AwaitingSecurities Awaiting financial instruments from a
corporate action or other procedure, for
example, conversion, dematerialisation,
exchange, registration, stamping,
splitting.
AWSH AwaitingSecuritiesFromCounterparty Financial instruments have not yet been
received from the counterparty (if receive
against payment trade), the money has
been delivered.
FUTU AwaitingSettlementDate Awaiting settlement date. No settlement
problems to be reported.
BENO BeneficialOwnershipDisagreement Disagreement in beneficial ownership.
BOTH BothInstructionsOnHold Counterparty's instruction and your
instruction are on hold/frozen/ in a
preadvice mode.
IPNC CancelNotPossible Instruction has been processed and
cannot be cancelled.
CDCY ConditionalCurrency Execution is conditional to the execution
of a process linked to the currency of the
transaction.
YCOL CollateralShortage Insufficient collateral in your account to
execute the instruction.
CLHT ClearingHouseTrade Instructed settlement date does not
agree with the settlement date on the
clearing house trade, that is, a specific
type of trade in India.
REGT CertificatesRejected Certificates have been lodged with the
registrar but rejected due to incomplete
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2106 March 2026
```

## File page 2107

```text
CodeName Name Definition
documentation or foreign ownership
limitation reached.
CDRE ConditionalRealignement Execution is conditional to the execution
of a process of realignment at the issuer
CSD.
CDRG ConditionalRegistrar Execution is conditional to the execution
of a process at the registrar.
NCON ConfirmationNotReceived Confirmation of settlement has not yet
been received.
CPEC CounterpartyInReceivership Counterparty is in receivership (form of
bankruptcy where a court appointed
person - the receiver - manages the
affairs of the business).
PRCY CounterpartyInstructionOnHold Counterparty's instruction is a preadvice,
that is, for matching only.
CMON CounterpartyInsufficientMoney Insufficient money in counterparty's
account.
CLAC CounterpartyInsufficientSecurities Insufficient deliverable financial
instruments in counterparty's account or
counterparty does not hold financial
instruments.
DKNY CounterpartyReturnedShares Counterparty has returned or refuses the
securities.
CHAS EnquirySent A chaser/enquiry has been sent.
GLOB GlobalFormSecurities Settlement cannot be executed; financial
instruments are in global form.
INCA IncomeAdjustementRequired Financial instruments require income
adjustment, for example, dividend or
interest.
REFU InstructionRefusedOrNotRecognised Instruction has been refused or not
recognised and is represented
automatically.
LIQU InsufficientCentralBankLiquidity Central bank liquidity is insufficient.
MONY InsufficientMoney Insufficient money in your account.
LACK LackOfSecurities Insufficient financial instruments in your
account.
SDUT LackOfStampDutyInformation Stamp duty information is missing.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
MINO MinimumSettlementAmount Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
MCER MissingCertification Awaiting receipt of adequate
certification.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2107 March 2026
```

## File page 2108

```text
CodeName Name Definition
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
DISA NaturalDisaster Exceptional closing of all financial
institutions due to natural disaster, for
example, earthquake.
NEWI NewIssues Financial instrument is a new issue and
not yet available/tradable.
NOFX NoForeignExchangeInstruction A foreign exchange instruction from you
is missing.
NMAS NoMatchingRequired Instruction has not been matched;
matching process is not required.
NPAY NoPayment Payment has not been made by issuer.
NSEC NotDelivered Financial instruments have not been
delivered by the issuer.
REFS NotInGoodOrder Delivery/receipt was refused because
physical financial instruments are not in
good order.
OTHR Other Other. See Narrative.
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
PENR PendingReceipt The instruction is pending receipt of
securities, for example, from a purchase,
loan etc.
PHSE PhysicalDeliveryDelay Settlement is physical. Financial
instruments are being delivered.
PHCK PhysicalSecuritiesVerification Physical financial instruments have been
received and are being checked for
authenticity.
BATC ProcessingBatchDifference Processing batch differs in the
counterparty's instruction, for example,
daytime/real-time versus overnight.
DQUA QuantityDisagreement Quantity of financial instruments does
not match.
DEPO RefusedDepositForIssueOfDepositaryReceipts Deposit of shares for the issuing of
depositary receipts has been refused.
The allotment granted by the issuer is
exceeded by your transaction.
SBLO SecuritiesBlocked Financial instruments are blocked due
to, for example, a corporate action event,
realignment.
FROZ SecuritiesFrozenAtCSD Financial instruments are blocked at the
Central Security Depository (CSD)
following a corporate event.
LALO SecuritiesLoanedOut Financial instruments are out on loan.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2108 March 2026
```

