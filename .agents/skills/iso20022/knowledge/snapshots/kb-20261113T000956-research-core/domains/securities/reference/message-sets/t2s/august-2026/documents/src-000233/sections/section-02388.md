---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.30 Status", "82.1.30.37 PendingReason14"]
file_pages: [3176, 3177, 3178]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.30.37 PendingReason14

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3176 to 3178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3176

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.30.37  PendingReason14
Definition: Specifies the reason why the instruction or request has a pending status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3176
{Or     Code <Cd> [1..1] CodeSet 3176
Or}     Proprietary <Prtry> [1..1] ± 3179
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3179
82.1.30.37.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Code <Cd> contains one of the following PendingReason26Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3176
Or}   Proprietary <Prtry> [1..1] ± 3179
82.1.30.37.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending status.
Datatype: "PendingReason10Code" on page 3271
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3176 August 2026
```

## File page 3177

```text
CodeName Name Definition
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
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3177 August 2026
```

## File page 3178

```text
CodeName Name Definition
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
SBLO SecuritiesBlocked Financial instruments are blocked due
to, for example, a corporate action event,
realignment.
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3178 August 2026
```

