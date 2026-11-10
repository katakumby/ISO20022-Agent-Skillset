---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.12 FundCashOutBreakdown3", "66.1.28.12.3 NewAmountIndicator <NewAmtInd>"]
file_pages: [4828]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.12.3 NewAmountIndicator <NewAmtInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4828 to 4828.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4828

```text
UnitsNumber <UnitsNb> contains the following elements (see "FinancialInstrumentQuantity1" on
page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] Quantity 5142
66.1.28.12.3  NewAmountIndicator <NewAmtInd>
Presence: [0..1]
Definition: Indicates whether the cash flow is an item that did not appear on the previously sent report,
for example, because it was received close to cut-off time.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.12.4  InvestmentFundTransactionOutType <InvstmtFndTxOutTp>
Presence: [1..1]
Definition: Type of transaction that resulted in the cash-out movement, for example, redemption, switch-
out.
InvestmentFundTransactionOutType <InvstmtFndTxOutTp> contains one of the following
InvestmentFundTransactionOutType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4828
Or}   Proprietary <Prtry> [1..1] ± 4828
66.1.28.12.4.1  Code <Cd>
Presence: [1..1]
Definition: Transaction type expressed as a code.
Datatype: "InvestmentFundTransactionOutType1Code" on page 5325
CodeName Name Definition
REDM Redemption Transaction is a redemption of an
investment fund.
SWIO SwitchOut Transaction is a subscription leg of a
switch order execution.
INSP InSpecie Transaction is an InSpecie.
CROO CrossOut Transaction is a cross out.
66.1.28.12.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Transaction type expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4828 May 2026
```

