---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.104 RejectionReason74Code"]
file_pages: [2121, 2122]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.104 RejectionReason74Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2121 to 2122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2121

```text
CodeName Name Definition
SETR SettlementTransactionRejection Unrecognised or invalid settlement
transaction type.
SDUT LackOfStampDuty Required stamp duty information is
missing.
INPS PlaceOfSafekeeping Unrecognised, invalid or missing place of
safekeeping.
OTHR Other Other. See Narrative.
ICUS ReceivingDeliveringParty2 Unrecognised or invalid client of
delivering or receiving party 1.
ICAG ReceivingDeliveringParty1 Unrecognised or invalid participant of
delivering or receiving depository.
DEPT ReceivingDeliveringDepository Unrecognised or invalid depository.
IEXE ReceivingDeliveringParty3 Unrecognised or invalid client of
delivering or receiving party 2.
INVB InvalidBalance Instruction aims at using an invalid
balance.
INVL InvalidLink Invalid or unrecognized link.
INVN InvalidLotNumber Invalid or unrecognized lot number.
VALR InvalidRule Account servicer validation rule rejection.
35.2.2.104  RejectionReason74Code
Definition: Unrecognised or invalid depository.
Type: CodeSet
CodeName Name Definition
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
LATE MarketDeadlineMissed Received after market deadline.
NRGN NotFoundRejection Instruction could not be found.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
NRGM NoMatch More than one instruction match the
criteria.
OTHR Other Other. See Narrative.
35.2.2.105  RejectionReason75Code
Definition: Specifies the reason why the settlement instruction has a rejected status.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2121 March 2026
```

## File page 2122

```text
CodeName Name Definition
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
DQUA QuantityRejection Unrecognised or invalid instructed
quantity.
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
LATE MarketDeadlineMissed Received after market deadline.
CASH CashAccount Unrecognised or invalid cash account.
DDEA DealPrice Unrecognised or invalid deal price.
DTRD TradeDate Unrecognised or invalid trade date or
requested trade date or future trade
date.
PLCE PlaceOfTrade Unrecognised or invalid place of trade.
RTGS ImpossibleToUseTheRTGSSystemInstructed Not possible to use the RTGS system
instructed (NRTG or YRTG).
NCRR SettlementAmountCurrencyRejection Unrecognised or invalid settlement
amount currency.
PHYS PhysicalSettlementImpossible Physical settlement is impossible for the
instructed financial instrument.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
DMON SettlementAmountRejection Unrecognised or invalid settlement
amount.
MINO MinimumSettlementQuantity Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
BATC ProcessingBatchRejection Unrecognised or invalid processing
batch, that is, daytime/real-time while
only possible to settle in overnight batch.
MUNO MultipleSettlementQuantity Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
TXST TaxStatusRejection Unrecognised or invalid tax status of the
securities instructed.
SETS SettlementSystemMethodRejection Unrecognised or invalid settlement
system/method instructed.
IIND CommonReferenceRejection Unrecognised, invalid or missing
common reference.
CAEV CorporateActionRejection Corporate action pending on the
financial instrument instructed.
CASY ImpossibleCashSettlementSystem Impossible standing arrangements
override instruction for the cash
settlement system.
DDAT SettlementDateRejection Unrecognised or invalid settlement date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2122 March 2026
```

