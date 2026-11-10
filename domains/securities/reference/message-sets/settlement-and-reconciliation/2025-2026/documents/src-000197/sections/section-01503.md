---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.78 RejectionStatus36Choice", "35.1.29.78.2 Reason <Rsn>", "35.1.29.78.2.1 Code <Cd>", "35.1.29.78.2.1.1 Code <Cd>"]
file_pages: [1996, 1997]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.78.2.1.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1996 to 1997.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1996

```text
Code <Cd> contains one of the following RejectionReason41Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1996
Or}   Proprietary <Prtry> [1..1] ± 1998
35.1.29.78.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason70Code" on page 2115
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1996 March 2026
```

## File page 1997

```text
CodeName Name Definition
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
SETR SettlementTransactionRejection Unrecognised or invalid settlement
transaction type.
SDUT LackOfStampDuty Required stamp duty information is
missing.
CADE TransactionCallDelay Unrecognised or invalid transaction call
delay.
FORF ForfeitAmount Unrecognised or invalid forfeit amount.
TERM ClosingDateTimeRejection Unrecognised or invalid closing date/
time.
VASU VariableRateSupportRejection Unrecognised or invalid variable rate
support (repurchase agreement).
REPA TerminationTransactionAmount Unrecognised or invalid termination
transaction amount.
REPO RepurchaseRate Unrecognised or invalid repurchase rate.
REPP PremiumAmount Unrecognised or invalid premium
amount.
RERT RepurchaseRateType Unrecognised or invalid repurchase rate
type.
RSPR SpreadRate Unrecognised or invalid spread rate.
ICAG ReceivingDeliveringParty1 Unrecognised or invalid participant of
delivering or receiving depository.
INPS PlaceOfSafekeeping Unrecognised, invalid or missing place of
safekeeping.
ICUS ReceivingDeliveringParty2 Unrecognised or invalid client of
delivering or receiving party 1.
DEPT ReceivingDeliveringDepository Unrecognised or invalid depository.
OTHR Other Other. See Narrative.
IEXE ReceivingDeliveringParty3 Unrecognised or invalid client of
delivering or receiving party 2.
INVE InvalidInvestorParty Unrecognised or invalid investor party.
May be used by an executing party to
reject an instruction for an investor (or
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1997 March 2026
```

