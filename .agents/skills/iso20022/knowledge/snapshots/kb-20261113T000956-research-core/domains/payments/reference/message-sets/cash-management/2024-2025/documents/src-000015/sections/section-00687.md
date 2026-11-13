---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.44 PendingSettlement2Code"]
file_pages: [867, 868]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.44 PendingSettlement2Code

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 867 to 868.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 867

```text
CodeName Name Definition
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
37.2.2.44  PendingSettlement2Code
Definition: Specifies the reason the transaction/instruction is pending settlement, that is, pending
delivery or receipt of the financial instrument. Settlement on the instructed settlement date is still
possible.
Type: CodeSet
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
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 867 February 2025
```

## File page 868

```text
CodeName Name Definition
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
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 868 February 2025
```

