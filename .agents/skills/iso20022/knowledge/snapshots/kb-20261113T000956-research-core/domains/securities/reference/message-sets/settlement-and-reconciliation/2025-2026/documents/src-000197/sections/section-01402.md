---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.4 RejectionStatus38Choice", "35.1.29.4.2 Reason <Rsn>", "35.1.29.4.2.1 Code <Cd>", "35.1.29.4.2.1.1 Code <Cd>"]
file_pages: [1875]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.4.2.1.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1875 to 1875.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1875

```text
Code <Cd> contains one of the following RejectionReason43Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1875
Or}   Proprietary <Prtry> [1..1] ± 1876
35.1.29.4.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Datatype: "RejectionReason73Code" on page 2119
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
Settlement And Reconciliation - Maintenance 2025 - 2026 1875 March 2026
```

