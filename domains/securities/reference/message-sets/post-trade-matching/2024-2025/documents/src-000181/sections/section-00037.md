---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.20 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [56]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.20 QuantityBreakdown <QtyBrkdwn>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 56 to 56.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
ConfirmationQuantity <ConfQty> contains one of the following elements (see "Quantity6Choice" on
page 273 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 273
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 273
3.4.4.20  QuantityBreakdown <QtyBrkdwn>
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
3.4.4.21  GrossTradeAmount <GrssTradAmt>
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
3.4.4.22  DealPrice <DealPric>
Presence: [1..1]
Definition: Amount of money for which goods or services are offered, sold, or bought.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 56 February 2025
```

