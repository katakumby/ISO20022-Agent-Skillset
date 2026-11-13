---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.110 RepairReason6Code"]
file_pages: [2130, 2131]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.110 RepairReason6Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2130 to 2131.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2130

```text
CodeName Name Definition
SETR SettlementTransaction Unrecognised or invalid settlement
transaction type.
SETS SettlementSystemMethod Unrecognised or invalid settlement
system/method instructed.
TXST TaxStatus Unrecognised or invalid tax status of the
securities instructed.
INPS PlaceOfSafekeeping Unrecognised, invalid or missing Place
of Safekeeping.
SDUT StampDuty Required stamp duty information is
missing.
OTHR Other Other. See Narrative.
IEXE ReceivingDeliveringParty3 Client of delivering or receiving party 2
mismatch.
ICAG ReceivingDeliveringParty1 Participant of delivering or receiving
depository mismatch.
DEPT ReceivingDeliveringDepository Depository mismatch.
ICUS ReceivingDeliveringParty2 Client of delivering or receiving party 1
mismatch.
REPA TerminationTransactionAmount Unrecognised or invalid termination
transaction amount.
CADE TransactionCallDelay Unrecognised or invalid transaction call
delay.
RERT RepurchaseRateType Unrecognised or invalid repurchase rate
type.
RSPR SpreadRate Unrecognised or invalid spread rate.
VASU VariableRateSupport Unrecognised or invalid variable rate
support (repurchase agreement).
REPO RepurchaseRate Unrecognised or invalid repurchase rate.
REPP PremiumAmount Unrecognised or invalid premium
amount.
TERM ClosingDateTime Unrecognised or invalid closing date/
time.
FORF ForfeitAmount Unrecognised or invalid forfeit amount.
35.2.2.110  RepairReason6Code
Definition: Specifies the reason why the securities financing instruction has a repair status.
Type: CodeSet
CodeName Name Definition
BATC ProcessingBatch Unrecognised or invalid processing
batch, that is, daytime/real-time while
only possible to settle in overnight batch.
CAEV CorporateAction Corporate action pending on the
financial instrument instructed.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2130 March 2026
```

## File page 2131

```text
CodeName Name Definition
CASH CashAccount Unrecognised or invalid cash account.
CASY ImpossibleCashSettlementSystem Impossible standing arrangements
override instruction for the cash
settlement system.
DDAT SettlementDate Unrecognised or invalid settlement date.
DDEA DealPrice Unrecognised or invalid deal price.
DMON SettlementAmount Unrecognised or invalid settlement
amount.
DQUA Quantity Unrecognised or invalid settlement
quantity.
DSEC Security Unrecognised or invalid financial
instrument identification.
DTRD TradeDate Unrecognised or invalid trade date.
IIND CommonReference Unrecognised, invalid or missing
common reference.
MINO MinimumSettlementQuantity Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
MUNO MultipleSettlementQuantity Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
NCRR SettlementAmountCurrency Unrecognised or invalid settlement
amount currency.
PHYS PhysicalSettlementImpossible Physical settlement is impossible for the
instructed financial instrument.
PLCE PlaceOfTrade Unrecognised or invalid place of trade.
REFE Reference Instruction has a reference identical to
another previously received instruction.
RTGS ImpossibleToUseTheRTGSSystemInstructed Impossible to use the RTGS system
instructed (NRTG or YRTG).
SAFE SafekeepingAccount Unrecognised or invalid message
sender's safekeeping account.
SETR SettlementTransaction Unrecognised or invalid settlement
transaction type.
SETS SettlementSystemMethod Unrecognised or invalid settlement
system/method instructed.
TXST TaxStatus Unrecognised or invalid tax status of the
securities instructed.
INPS PlaceOfSafekeeping Unrecognised, invalid or missing Place
of Safekeeping.
SDUT StampDuty Required stamp duty information is
missing.
OTHR Other Other. See Narrative.
IEXE ReceivingDeliveringParty3 Client of delivering or receiving party 2
mismatch.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2131 March 2026
```

