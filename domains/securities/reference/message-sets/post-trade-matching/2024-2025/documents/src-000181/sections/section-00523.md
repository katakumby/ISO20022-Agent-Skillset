---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.14 InstructionProcessingReason4Choice", "7.1.28.14.1 Reason <Rsn>"]
file_pages: [600, 601]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.14.1 Reason <Rsn>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 600 to 601.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 600

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..*]  600
     Code <Cd> [1..1]  600
{Or       Code <Cd> [1..1] CodeSet 600
Or}       Proprietary <Prtry> [1..1] ± 602
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 602
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 603
7.1.28.14.1  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the InRepairStatus.
Reason <Rsn> contains the following RepairReason14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  600
{Or     Code <Cd> [1..1] CodeSet 600
Or}     Proprietary <Prtry> [1..1] ± 602
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 602
7.1.28.14.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction is in repair.
Code <Cd> contains one of the following RepairReason19Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 600
Or}   Proprietary <Prtry> [1..1] ± 602
7.1.28.14.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RepairReason7Code" on page 642
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
BATC ProcessingBatch Unrecognised or invalid processing
batch, that is, daytime/real-time while
only possible to settle in overnight batch.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 600 February 2025
```

## File page 601

```text
CodeName Name Definition
BUSE TypeOfOrderRepair Unrecognised or invalid type of order.
CADE TransactionCallDelay Unrecognised or invalid transaction call
delay.
CASH CashAccount Unrecognised or invalid cash account.
CASY ImpossibleCashSettlementSystem Impossible standing arrangements
override instruction for the cash
settlement system.
COMC CommercializationContractRepair Unrecognized or invalid
commercialization contract.
DDAT SettlementDate Unrecognised or invalid settlement date.
DDEA DealPrice Unrecognised or invalid deal price.
DEPT ReceivingDeliveringDepository Depository mismatch.
DMON SettlementAmount Unrecognised or invalid settlement
amount.
DQUA Quantity Unrecognised or invalid settlement
quantity.
DSEC Security Unrecognised or invalid financial
instrument identification.
DTRD TradeDate Unrecognised or invalid trade date.
FEEE FeeCommissionRepair Unrecognised or invalid fee or
commission.
FORF ForfeitAmount Unrecognised or invalid forfeit amount.
ICAG ReceivingDeliveringParty1 Participant of delivering or receiving
depository mismatch.
ICUS ReceivingDeliveringParty2 Client of delivering or receiving party 1
mismatch.
IEXE ReceivingDeliveringParty3 Client of delivering or receiving party 2
mismatch.
IIND CommonReference Unrecognised, invalid or missing
common reference.
INNA NarrativeInformationRepair Unrecognised or invalid service level
agreement pre-agreed narrative
information.
LEOG LetterOfGuaranteeIndicator Unrecognised or invalid letter of
guarantee indicator instructed.
NARR NarrativeReason See narrative field for reason.
NCRR SettlementAmountCurrency Unrecognised or invalid settlement
amount currency.
NRGM NoMatch Cancellation request is in repair since
more than one instruction match to the
cancellation criteria.
NRGN NotFound Cancellation request is in repair since
the instruction could not be found.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 601 February 2025
```

