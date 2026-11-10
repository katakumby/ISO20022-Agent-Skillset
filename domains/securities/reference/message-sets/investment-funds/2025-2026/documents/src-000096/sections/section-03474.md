---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.3 InvestmentFundTransaction3", "66.1.26.3.13 SettledTransactionIndicator <SttldTxInd>"]
file_pages: [4724]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.3.13 SettledTransactionIndicator <SttldTxInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4724 to 4724.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4724

```text
Definition: Date and time at which the order was placed by the investor.
Datatype: "ISODateTime" on page 5388
66.1.26.3.13  SettledTransactionIndicator <SttldTxInd>
Presence: [1..1]
Definition: Indicates whether the cash payment with respect to the executed order is settled.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.3.14  RegisteredTransactionIndicator <RegdTxInd>
Presence: [1..1]
Definition: Indicates whether the executed order has a registered status on the books of the transfer
agent.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.3.15  UnitsQuantity <UnitsQty>
Presence: [1..1]
Definition: Number of investment funds units.
UnitsQuantity <UnitsQty> contains the following elements (see "FinancialInstrumentQuantity1" on
page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.26.3.16  CreditDebit <CdtDbt>
Presence: [1..1]
Definition: Direction of the transaction being reported, ie, securities are received (credited) or delivered
(debited).
Datatype: "CreditDebitCode" on page 5291
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
66.1.26.3.17  Reversal <Rvsl>
Presence: [0..1]
Definition: Transaction being reported is a reversal of previously reported transaction.
Datatype: "ReversalCode" on page 5358
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4724 May 2026
```

