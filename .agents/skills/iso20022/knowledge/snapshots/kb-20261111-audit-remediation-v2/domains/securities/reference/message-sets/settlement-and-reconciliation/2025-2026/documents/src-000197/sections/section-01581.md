---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.82 PendingReason34Code"]
file_pages: [2109]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.82 PendingReason34Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2109 to 2109.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2109

```text
CodeName Name Definition
AUTH SentToTaxAuthorities Tax reclaim has been sent to the tax
authorities.
SETS SettlementSystemMethodModified Settlement system/method has been
modified at central securities depository
to allow settlement.
IAAD StatusReasonInvestigation Pending reason being investigated.
PRSY SystemOnHold Transaction was put on hold/frozen by
the system.
TAMM TradeAmendedInMarket Trade is being amended in the market.
PART TradeSettlesInPartials Trade will settle in partials.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
VLDA ValidForTaxAuthorities For tax reclaim, the event is pending, the
tax reclaim is valid for the tax authorities.
PREA YourInstructionOnHold Your instruction is a preadvice, that is,
for matching only.
35.2.2.82  PendingReason34Code
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
OTHR Other Other. See Narrative.
DQUA QuantityDisagreement Quantity of financial instruments does
not match.
35.2.2.83  PendingReason35Code
Definition: Specifies the reason why a cancellation request sent for the related instruction is pending.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
CONF AwaitingConfirmation Awaiting confirmation from the
counterparty.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2109 March 2026
```

