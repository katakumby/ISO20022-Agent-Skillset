---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.3 Status <Sts>", "5.4.2.1.3.2.1.4.3.3 Reason <Rsn>", "5.4.2.1.3.2.1.4.3.3.2 Cancelled <Canc>"]
file_pages: [286, 287, 288]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.3.3.2 Cancelled <Canc>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 286 to 288.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 286

```text
CodeName Name Definition
ICUS DisagreementReceivingOrDeliveringCustodian Incorrect delivering or receiving
custodian.
5.4.2.1.3.2.1.4.3.3.2  Cancelled <Canc>
Presence: [1..1]
Definition: Reason why the payment status is cancelled.
Datatype: "CancelledStatusReason1Code" on page 850
CodeName Name Definition
CANI CancelledByYourself Transaction is cancelled by yourself.
CANS CancelledBySystem Transaction is cancelled by the system.
CSUB CancelledByAgent Transaction is cancelled by the agent.
5.4.2.1.3.2.1.4.3.3.3  Suspended <Sspd>
Presence: [1..1]
Definition: Reason why the payment status is suspended.
Datatype: "SuspendedStatusReason1Code" on page 874
CodeName Name Definition
SUBY SuspendedByYourself Transaction/instruction is suspended
following your earlier suspension
instruction.
SUBS SuspendedBySystem Transaction/instruction is suspended
following a system suspension
instruction.
5.4.2.1.3.2.1.4.3.3.4  PendingFailingSettlement <PdgFlngSttlm>
Presence: [1..1]
Definition: Reason why the payment status is pending (failing settlement).
Datatype: "PendingFailingSettlement1Code" on page 865
CodeName Name Definition
AWMO AwaitingMoney Securities have been delivered, but the
money is still expected from the
counterparty.
AWSH AwaitingSecuritiesFromCounterparty Securities have not yet been received
from the counterparty. If the settlement
instruction was a received against
payment, the cash has been delivered.
LAAW AwaitingOtherTransaction Awaiting settlement of a linked 'buy'.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
CLAT CounterpartyTooLateForSettlement Counterparty's instruction was too late
for settlement, (that is, received too late,
matching, or settlement problems were
solved too late).
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 286 February 2025
```

## File page 287

```text
CodeName Name Definition
CERT WrongCertificateNumbers Certificate number error.
MINO MinimumSettlementAmount Securities quantity is lower than the
minimum existing settlement quantity for
the instructed financial instrument.
PHSE PhysicalDeliveryDelay Settlement is physical, and there is a
delay in the delivery of the securities.
SBLO SecuritiesBlocked Securities are blocked, for example,
because of a corporate action event or
re-alignment.
DKNY CounterpartyReturnedSecurities Counterparty has returned, refused, or
does not recognize the securities.
STCD ConfirmationDiscrepancy Discrepancy in the settlement
confirmation.
BENO BeneficialOwnershipDisagreement Disagreement over beneficial ownership.
LACK LackOfSecurities Insufficient deliverable securities in your
account.
LATE TooLateForSettlement Settlement instruction was too late for
settlement, that is, received too late,
matching, or settlement problems were
solved too late.
CANR CancellationConfirmationRequest Transaction suspended. Because the
suspension period is finished, the
cancellation or confirmation of
instructions is required.
MLAT MoneyTooLateForSettlement Payment for a buy of securities was
received after the cut-off time for
completing the settlement on a same
day basis.
OBJT UnderObjection Securities are stolen, in dispute, and
under objection.
DOCC AwaitingDocumentsOrEndorsementsFromCoun
terparty
Awaiting documents or endorsements
from the counterparty.
BLOC AccountBlocked Account is blocked, so no instruction can
settle.
CHAS EnquirySent Enquiry/chaser sent to the agent or
depository.
NEWI NewIssues Securities are new issues, and not yet
available/tradeable.
CLAC CounterpartyInsufficientSecurities Insufficient deliverable securities in the
counterparty's account, or counterparty
does not hold the securities.
PART TradeSettlesInPartials Trade will settle in partials.
CMON CounterpartyInsufficientMoney Insufficient money in counterparty's
account.
COLL SecuritiesPledgedAsCollateral Securities are not deliverable as they are
pledged as collateral.
DEPO RefusedDepositForIssueOfDepositaryReceipts Deposit of shares for the issuance of a
depositary receipt has been refused. The
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 287 February 2025
```

## File page 288

```text
CodeName Name Definition
allotment for depositary receipts granted
by the issuer would be exceeded by the
transaction.
FLIM MaximumForeignLimitReached Insufficient deliverable securities in your
account, as maximum foreign limit has
been reached.
NOFX NoForeignExchangeInstruction A foreign exchange instruction from you
is missing.
INCA IncomeAdjustementRequired Securities require income adjustment,
that is, dividend or interest.
LINK PendingLinkedInstruction Linked instruction is pending/failing.
BYIY BuyInProcedure A buy-in procedure has started on the
market, on your behalf, if your instruction
is a receipt, or on behalf of the
counterparty if the instruction is a
delivery.
CAIS AwaitingSecurities Awaiting securities from a corporate
action issue or other procedure(s), for
example, conversion, dematerialisation,
exchange, registration, stamping, and
splitting.
LALO SecuritiesLoanedOut Insufficient deliverable securities in your
account as securities are loaned out.
MONY InsufficientMoney Insufficient money in your account.
NCON ConfirmationNotReceived Settlement confirmation has not yet been
received.
YCOL CollateralShortage Not enough collateral in your account to
execute the instruction.
REFS NotInGoodOrder Delivery/receipt is refused because the
physical securities are not in good order.
SDUT LackOfStampDutyInformation Instruction is failing since stamp duty
information is missing.
CYCL AwaitingNextSettlementCycle Your instruction is confirmed in the local
market, but is ready for settlement at the
next settlement cycle.
BATC ProcessingBatchDifference Processing batch differs in the
counterparty's instruction, for example,
day time/real time vs overnight.
GUAD GuaranteedDeliveryIndicatorDifference Guaranteed delivery indicator differs in
the counterparty's instruction.
PREA PreadviceInstructed Instruction is a preadvice, that is,
matching only.
GLOB GlobalFormSecurities Securities are in global form.
CPEC CounterpartyInReceivership Counterparty is in receivership, that is, a
form of bankruptcy.
MUNO MultipleSettlementAmount Amount is not a multiple of an existing
settlement amount lot for the instructed
financial instrument.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 288 February 2025
```

