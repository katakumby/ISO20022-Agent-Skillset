---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.109 RepairReason5Code"]
file_pages: [2129]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.109 RepairReason5Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2129 to 2129.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2129

```text
CodeName Name Definition
ICUS ReceivingDeliveringParty2 Client of delivering or receiving party 1
mismatch.
35.2.2.109  RepairReason5Code
Definition: Specifies the reason why the securities financing instruction has a repair status.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2129 March 2026
```

