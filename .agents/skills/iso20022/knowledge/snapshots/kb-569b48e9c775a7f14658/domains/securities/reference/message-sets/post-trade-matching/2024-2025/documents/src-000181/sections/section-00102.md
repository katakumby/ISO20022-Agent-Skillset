---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.20 TwoLegTransactionDetails <TwoLegTxDtls>", "3.4.20.9 ClosingSettlementAmount <ClsgSttlmAmt>"]
file_pages: [134]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.20.9 ClosingSettlementAmount <ClsgSttlmAmt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 134 to 134.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 134

```text
ClosingDate <ClsgDt> contains one of the following elements (see "ClosingDate4Choice" on page 263
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 263
Or}   Code <Cd> [1..1]  264
{Or     Code <Cd> [1..1] CodeSet 264
Or}     Proprietary <Prtry> [1..1] ± 264
3.4.20.9  ClosingSettlementAmount <ClsgSttlmAmt>
Presence: [0..1]
Definition: Total amount of money to be paid or received in exchange for the securities. The amount
includes the principal with any commissions and fees or accrued interest.
ClosingSettlementAmount <ClsgSttlmAmt> contains the following elements (see
"AmountAndDirection5" on page 227 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C9 227
   CreditDebit <CdtDbt> [0..1] CodeSet 228
3.4.20.10  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Processing date of the trading session.
ProcessingDate <PrcgDt> contains one of the following elements (see "TradeDate7Choice" on
page 267 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 267
Or}   Value <Val> [1..1]  267
{Or     Code <Cd> [1..1] CodeSet 267
Or}     Proprietary <Prtry> [1..1] ± 268
3.4.20.11  TwoLegTransactionType <TwoLegTxTp>
Presence: [0..1]
Definition: Specifies the type of the second leg transaction.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 134 February 2025
```

