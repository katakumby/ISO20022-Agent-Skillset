---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.4 Message Building Blocks", "12.4.6 AdditionalQueryParameters <AddtlQryParams>", "12.4.6.2 Reason <Rsn>", "12.4.6.2.5 DeniedReason <DndRsn>"]
file_pages: [423, 424, 425, 426]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.4.6.2.5 DeniedReason <DndRsn>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 423 to 426.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 423

```text
GeneratedReason <GnrtdRsn> contains one of the following elements (see
"GeneratedReasons5Choice" on page 1970 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1970
Or}   Proprietary <Prtry> [1..1] ± 1970
12.4.6.2.5  DeniedReason <DndRsn>
Presence: [0..1]
Definition: Specifies the reason why the request was denied.
DeniedReason <DndRsn> contains one of the following elements (see "DeniedReason14Choice" on
page 1978 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1978
Or}   Proprietary <Prtry> [1..1] ± 1979
12.4.6.2.6  AcknowledgedAcceptedReason <AckdAccptdRsn>
Presence: [0..1]
Definition: Specifies additional information about the processed instruction.
AcknowledgedAcceptedReason <AckdAccptdRsn> contains one of the following elements (see
"AcknowledgementReason12Choice" on page 1935 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1936
Or}   Proprietary <Prtry> [1..1] ± 1936
12.4.6.2.7  PendingReason <PdgRsn>
Presence: [0..1]
Definition: Specifies the reason why the instruction has a pending status.
PendingReason <PdgRsn> contains one of the following PendingReason78Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 423
Or}   Proprietary <Prtry> [1..1] ± 427
12.4.6.2.7.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Datatype: "PendingReason33Code" on page 2105
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 423 March 2026
```

## File page 424

```text
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
documentation or foreign ownership
limitation reached.
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 424 March 2026
```

## File page 425

```text
CodeName Name Definition
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
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 425 March 2026
```

## File page 426

```text
CodeName Name Definition
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
AUTH SentToTaxAuthorities Tax reclaim has been sent to the tax
authorities.
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 426 March 2026
```

