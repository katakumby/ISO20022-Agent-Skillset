---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.3 InvestmentFundTransaction3", "66.1.26.3.6 MasterReference <MstrRef>"]
file_pages: [4723]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.3.6 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4723 to 4723.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4723

```text
Definition: Status of an investment fund transaction.
Datatype: "TransactionStatus1Code" on page 5378
CodeName Name Definition
RVSL Reversal Transaction has been reversed.
REBO Rebooked Transaction has been rebooked.
CANC Cancelled Transaction has been cancelled.
66.1.26.3.6  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
66.1.26.3.7  OrderReference <OrdrRef>
Presence: [0..1]
Definition: Unique identifier for an order, as assigned by the sell-side. The identifier must be unique
within a single trading day.
Datatype: "Max35Text" on page 5403
66.1.26.3.8  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of an order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
66.1.26.3.9  DealReference <DealRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for an order execution, as assigned by a confirming party.
Datatype: "Max35Text" on page 5403
66.1.26.3.10  LegIdentification <LegId>
Presence: [0..1]
Definition: Unique technical identifier for an instance of a leg within a switch.
Datatype: "Max35Text" on page 5403
66.1.26.3.11  LegExecutionIdentification <LegExctnId>
Presence: [0..1]
Definition: Unique identifier for an instance of a leg execution within a switch confirmation.
Datatype: "Max35Text" on page 5403
66.1.26.3.12  OrderDateTime <OrdrDtTm>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4723 May 2026
```

