---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 camt.006.001.11 ReturnTransactionV11", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 BusinessReport <BizRpt>", "5.4.2.1.3 TransactionReport <TxRpt>", "5.4.2.1.3.2 TransactionOrError <TxOrErr>", "5.4.2.1.3.2.1 Transaction <Tx>", "5.4.2.1.3.2.1.4 Payment <Pmt>", "5.4.2.1.3.2.1.4.3 Status <Sts>", "5.4.2.1.3.2.1.4.3.3 Reason <Rsn>", "5.4.2.1.3.2.1.4.3.3.5 PendingSettlement <PdgSttlm>"]
file_pages: [289, 290]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.006.001.11"]
---

# 5.4.2.1.3.2.1.4.3.3.5 PendingSettlement <PdgSttlm>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 289 to 290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
5.4.2.1.3.2.1.4.3.3.5  PendingSettlement <PdgSttlm>
Presence: [1..1]
Definition: Reason why the payment status is pending (settlement).
Datatype: "PendingSettlement2Code" on page 867
CodeName Name Definition
AWMO AwaitingMoney Securities have been delivered, but the
settlement amount has not been
received from the counterparty.
CAIS AwaitingSecurities Awaiting securities from corporate action
issue or other procedures, for example,
conversion, dematerialisation, exchange,
registration, stamping, splitting, etc.
REFU InstructionRefusedOrNotRecognised Instruction that has been refused or not
recognised, and is represented
automatically.
AWSH AwaitingSharesFromCounterparty Securities have not yet been received
from the counterparty.
PHSE PhysicalDeliveryDelay Settlement is physical and securities are
being delivered.
TAMM TradeAmendedInMarket Trade is being amended in the market.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
DOCC AwaitingDocumentsOrEndorsementsFromCoun
terparty
Awaiting documents or endorsements
from the counterparty.
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
CHAS EnquirySent Chaser/enquiry sent to the agent or
depository.
NEWI NewIssues Securities are new issues and are not
yet available/tradable.
CLAC CounterpartyInsufficientSecurities Insufficient deliverable securities in the
counterparty's account, or counterparty
does not hold the securities.
MUNO MultipleSettlementAmount Securities quantity is not a multiple of an
existing settlement amount lot for the
instructed financial instrument.
GLOB GlobalFormSecurities Settlement cannot be executed as
securities are in global form.
PREA PreadviceInstructed Your instruction is a preadvice, that is,
matching only.
GUAD GuaranteedDeliveryIndicatorDifference Guaranteed delivery indicator differs in
the counterparty's instruction.
PART TradeSettlesInPartials Trade will settle in partials.
NMAS NoMatchingRequired Instruction has not been matched
because the matching process is not
required.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 289 February 2025
```

## File page 290

```text
CodeName Name Definition
CMON CounterpartyInsufficientMoney Insufficient money in the counterparty's
account.
YCOL CollateralShortage Not enough collateral in your account to
execute the transaction.
COLL SecuritiesPledgedAsCollateral Securities are not deliverable as they are
pledged as collateral.
DEPO RefusedDepositForIssueOfDepositaryReceipts Deposit of shares for the issuing of
depositary receipts has been refused.
The allotment for depositary receipts
granted by the issuer is exceeded by the
transaction.
FLIM MaximumForeignLimitReached Insufficient deliverable securities in your
account because the maximum foreign
limit has been reached.
NOFX NoForeignExchangeInstruction Foreign exchange instruction is missing.
INCA IncomeAdjustementRequired Securities require income adjustment, for
example, dividend or interest.
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
FUTU AwaitingSettlementDate Instruction is awaiting the settlement
date, and no settlement problems have
been reported.
LACK LackOfSecurities Insufficient deliverable securities in your
account.
LALO SecuritiesLoanedOut Insufficient deliverable securities in your
account because securities are loaned
out.
MONY InsufficientMoney Insufficient money in your account.
NCON ConfirmationNotReceived Settlement confirmation has not been
received.
REFS NotInGoodOrder Delivery/receipt has been refused
because the physical securities are not
in good order.
SDUT LackOfStampDutyInformation Instruction is pending as stamp duty
information is missing.
BATC ProcessingBatchDifference Processing batch differs in the
counterparty's instruction, for example,
day time/real time versus overnight.
CYCL AwaitingNextSettlementCycle Instruction is confirmed in the local
market or is ready for settlement,
awaiting the next settlement cycle.
SBLO SecuritiesBlocked Settlement is pending. The securities are
blocked due to, for example, a corporate
action event, re-alignment.
CPEC CounterpartyInReceivership Counterparty is in receivership, that is,
the form of bankruptcy where a court
appointed person, the receiver, manages
the affairs of the business.
Approved by the Payments SEG on 04 February 2025 camt.006.001.11 ReturnTransactionV11
Cash Management - Maintenance 2024 - 2025 290 February 2025
```

