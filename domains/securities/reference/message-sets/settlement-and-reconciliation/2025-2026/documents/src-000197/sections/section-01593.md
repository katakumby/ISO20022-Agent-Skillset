---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.107 RejectionReason77Code"]
file_pages: [2127, 2128]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.107 RejectionReason77Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2127 to 2128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2127

```text
CodeName Name Definition
OTHR Other Other. See Narrative.
IEXE ReceivingDeliveringParty3 Unrecognised or invalid client of
delivering or receiving party 2.
INVE InvalidInvestorParty Unrecognised or invalid investor party.
May be used by an executing party to
reject an instruction for an investor (or
portfolio) for which it is not authorised to
act.
PLIS PlaceOfListing Unrecognised or invalid place of listing.
Used when the security identified is not
listed on the market supplied.
35.2.2.107  RejectionReason77Code
Definition: Specifies the reason why the request has a rejected or repair status.
Type: CodeSet
CodeName Name Definition
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
DSEC InvalidSecurity Unrecognised or invalid financial
instrument identification.
LATE MarketDeadlineMissed Received after market deadline.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
OTHR Other Other. See Narrative.
MISM InvalidRequest Statement/status advice request cannot
be executed. The message type
requested is not valid for the message
reference or statement period
concerned.
35.2.2.108  RepairReason4Code
Definition: Specifies the reason why the settlement instruction has a repair status.
Type: CodeSet
CodeName Name Definition
BATC ProcessingBatch Unrecognised or invalid processing
batch, that is, daytime/real-time while
only possible to settle in overnight batch.
CAEV CorporateAction Corporate action pending on the
financial instrument instructed.
CASH CashAccount Unrecognised or invalid cash account.
CASY ImpossibleCashSettlementSystem Impossible standing arrangements
override instruction for the cash
settlement system.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2127 March 2026
```

## File page 2128

```text
CodeName Name Definition
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
ICAG ReceivingDeliveringParty1 Participant of delivering or receiving
depository mismatch.
DEPT ReceivingDeliveringDepository Depository mismatch.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2128 March 2026
```

