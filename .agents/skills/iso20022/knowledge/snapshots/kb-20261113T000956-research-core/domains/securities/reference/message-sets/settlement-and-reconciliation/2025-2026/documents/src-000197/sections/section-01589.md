---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.102 RejectionReason72Code"]
file_pages: [2118]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.102 RejectionReason72Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2118 to 2118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2118

```text
CodeName Name Definition
LATE MarketDeadlineMissed Received after market deadline.
SAFE SafekeepingAccountRejection Unrecognised or invalid message
sender's safekeeping account.
NRGM NoMatch More than one instruction match the
criteria.
NRGN NotFoundRejection Instruction could not be found.
OTHR Other Other. See Narrative.
REFE ReferenceRejection Instruction has a reference identical to
another previously received instruction.
INVM InvalidModificationRequest Invalid or unrecognized modification
request.
INVL InvalidLink Invalid or unrecognized link.
35.2.2.102  RejectionReason72Code
Definition: Specifies the reason why the settlement instruction has a rejected status.
Type: CodeSet
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2118 March 2026
```

