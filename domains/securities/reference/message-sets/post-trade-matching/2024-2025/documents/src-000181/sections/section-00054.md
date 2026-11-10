---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>", "3.4.6.43 ExercisePrice <ExrcPric>"]
file_pages: [75]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.6.43 ExercisePrice <ExrcPric>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 75 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 75

```text
3.4.6.43  ExercisePrice <ExrcPric>
Presence: [0..1]
Definition: Predetermined price at which the holder of a derivative will buy or sell the underlying
instrument.
ExercisePrice <ExrcPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
3.4.6.44  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Fixed price at which a new securities issue is being offered to the public.
SubscriptionPrice <SbcptPric> contains the following elements (see "Price14" on page 512 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
3.4.6.45  ConversionPrice <ConvsPric>
Presence: [0..1]
Definition: Price at which a given convertible security can be converted to common stock.
ConversionPrice <ConvsPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
3.4.6.46  TaxableIncomePerShare <TaxblIncmPerShr>
Presence: [0..1]
Definition: Amount included in the Net Asset Value(NAV) that corresponds to gains directly or indirectly
derived from interest payment, for example in the scope of the European Directive on taxation of
savings income in the form of interest payments.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 75 February 2025
```

