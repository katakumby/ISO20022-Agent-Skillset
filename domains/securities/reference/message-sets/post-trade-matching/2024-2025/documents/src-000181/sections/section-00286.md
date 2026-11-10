---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.21 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [346]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.21 QuantityBreakdown <QtyBrkdwn>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 346 to 346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 346

```text
ConfirmationQuantity <ConfQty> contains one of the following elements (see "Quantity6Choice" on
page 273 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 273
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 273
7.1.19.43.21  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series, etc.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown76" on
page 519 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 519
   LotQuantity <LotQty> [0..1] ± 520
   LotDateTime <LotDtTm> [0..1] ± 520
   LotPrice <LotPric> [0..1] ± 520
7.1.19.43.22  GrossTradeAmount <GrssTradAmt>
Presence: [0..1]
Definition: Principal amount of a trade (price multiplied by quantity).
GrossTradeAmount <GrssTradAmt> contains the following elements (see "AmountAndDirection29"
on page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.19.43.23  DealPrice <DealPric>
Presence: [1..1]
Definition: Amount of money for which goods or services are offered, sold, or bought.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 346 February 2025
```

