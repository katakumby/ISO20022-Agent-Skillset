---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.13 AcknowledgedAcceptedStatus32Choice", "35.1.29.13.2 Reason <Rsn>", "35.1.29.13.2.1 Code <Cd>"]
file_pages: [1895, 1896, 1897]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.13.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1895 to 1897.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1895

```text
35.1.29.13.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason provided for the status.
Code <Cd> contains one of the following elements (see "AcknowledgementReason23Choice" on
page 1958 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1958
Or}   Proprietary <Prtry> [1..1] ± 1958
35.1.29.13.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.14  PendingReason63Choice
Definition: Choice of format for the pending reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1895
Or}   Proprietary <Prtry> [1..1] ± 1898
35.1.29.14.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Datatype: "PendingReason24Code" on page 2098
CodeName Name Definition
AWMO AwaitingMoney Financial instruments are delivered, but
still awaiting money from counterparty.
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. Processed
on best effort basis.
CAIS AwaitingSecurities Awaiting financial instruments from a
corporate action or other procedure, for
example, conversion, dematerialisation,
exchange, registration, stamping,
splitting.
REFU InstructionRefusedOrNotRecognised Instruction has been refused or not
recognised and is represented
automatically.
AWSH AwaitingSecuritiesFromCounterparty Financial instruments have not yet been
received from the counterparty (if receive
against payment trade), the money has
been delivered.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1895 March 2026
```

## File page 1896

```text
CodeName Name Definition
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
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
INCA IncomeAdjustementRequired Financial instruments require income
adjustment, for example, dividend or
interest.
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1896 March 2026
```

## File page 1897

```text
CodeName Name Definition
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1897 March 2026
```

