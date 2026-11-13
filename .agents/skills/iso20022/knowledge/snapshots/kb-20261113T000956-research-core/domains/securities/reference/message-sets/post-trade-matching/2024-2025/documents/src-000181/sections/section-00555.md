---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.60 RepairReason7Code"]
file_pages: [642, 643]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.60 RepairReason7Code

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 642 to 643.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 642

```text
CodeName Name Definition
DFLT MissingDefaultOption One option must be marked as the
default.
FAIL FailedValidation Validation of the advice/instruction/
request failed.
INDT InvalidDetails Message details specified in the
instruction/request are inconsistent with
those that were specified in the relating
original message.
OTHR Other Other. See Narrative.
DEPT ReceivingDeliveringDepository Unrecognised or invalid depository.
ICUS ReceivingDeliveringParty2 Unrecognised or invalid client of
delivering or receiving party 1.
ICAG ReceivingDeliveringParty1 Unrecognised or invalid participant of
delivering or receiving depository.
7.2.2.60  RepairReason7Code
Definition: Specifies the reason why the instruction is in repair.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
BATC ProcessingBatch Unrecognised or invalid processing
batch, that is, daytime/real-time while
only possible to settle in overnight batch.
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 642 February 2025
```

## File page 643

```text
CodeName Name Definition
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
PHYS PhysicalSettlementImpossible Physical settlement is impossible for the
instructed financial instrument.
PLCE PlaceOfTrade Unrecognised or invalid place of trade.
CTRA ClosingTransactionAmount Unrecognised or invalid closing
transaction amount.
REPO RepurchaseRate Unrecognised or invalid repurchase rate.
REPP PremiumAmount Unrecognised or invalid premium
amount.
RERT RepurchaseRateType Unrecognised or invalid repurchase rate
type.
RSPR SpreadRate Unrecognised or invalid spread rate.
RTGS ImpossibleToUseTheRTGSSystemInstructed Impossible to use the RTGS system
instructed (NRTG or YRTG).
SAFE SafekeepingAccount Unrecognised or invalid message
sender's safekeeping account.
SETR SettlementTransaction Unrecognised or invalid settlement
transaction type.
SETS SettlementSystemMethod Unrecognised or invalid settlement
system/method instructed.
TERM ClosingDateTime Unrecognised or invalid closing date/
time.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 643 February 2025
```

