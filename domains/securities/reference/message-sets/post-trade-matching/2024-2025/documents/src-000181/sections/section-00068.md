---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.7 UnderlyingFinancialInstrument <UndrlygFinInstrm>", "3.4.7.2 Attributes <Attrbts>", "3.4.7.2.44 SubscriptionPrice <SbcptPric>"]
file_pages: [92]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.7.2.44 SubscriptionPrice <SbcptPric>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 92 to 92.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 92

```text
3.4.7.2.44  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Fixed price at which a new securities issue is being offered to the public.
SubscriptionPrice <SbcptPric> contains the following elements (see "Price14" on page 512 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
3.4.7.2.45  ConversionPrice <ConvsPric>
Presence: [0..1]
Definition: Price at which a given convertible security can be converted to common stock.
ConversionPrice <ConvsPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
3.4.7.2.46  TaxableIncomePerShare <TaxblIncmPerShr>
Presence: [0..1]
Definition: Amount included in the Net Asset Value(NAV) that corresponds to gains directly or indirectly
derived from interest payment, for example in the scope of the European Directive on taxation of
savings income in the form of interest payments.
TaxableIncomePerShare <TaxblIncmPerShr> contains the following elements (see "Price14" on
page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
3.4.7.2.47  MinimumNominalQuantity <MinNmnlQty>
Presence: [0..1]
Definition: Indicates the minimum tradable quantity of a security.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 92 February 2025
```

