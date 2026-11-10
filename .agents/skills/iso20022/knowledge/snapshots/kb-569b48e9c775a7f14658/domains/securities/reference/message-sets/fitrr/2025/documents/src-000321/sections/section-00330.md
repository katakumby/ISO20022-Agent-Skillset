---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.9 FinancialInstrument <FinInstrm>", "22.1.13.2.9.3 Other <Othr>", "22.1.13.2.9.3.3 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "22.1.13.2.9.3.3.3 UnderlyingInstrument <UndrlygInstrm>"]
file_pages: [384]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.9.3.3.3 UnderlyingInstrument <UndrlygInstrm>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 384 to 384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 384

```text
For a future or option on an index, the amount per index point.
Impacted by: C9 "MultiplierRule"
Datatype: "NonNegativeDecimalNumber" on page 453
Constraints
• MultiplierRule
Price Multiplier must not be zero.
22.1.13.2.9.3.3.3  UnderlyingInstrument <UndrlygInstrm>
Presence: [1..1]
Definition: Choice to specify the type(s) of underlying instrument(s) that make up the financial
instrument.
UnderlyingInstrument <UndrlygInstrm> contains one of the following
UnderlyingIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Swap <Swp> [1..1]  C13 384
     SwapIn <SwpIn> [0..1] ± 384
     SwapOut <SwpOut> [0..1] ± 385
Or}   Other <Othr> [1..1] ± 385
22.1.13.2.9.3.3.3.1  Swap <Swp>
Presence: [1..1]
Definition: Underlying of a swap transaction.
Impacted by: C13 "SwapInOrSwapOutRule"
Swap <Swp> contains the following SwapLegIdentification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SwapIn <SwpIn> [0..1] ± 384
   SwapOut <SwpOut> [0..1] ± 385
Constraints
• SwapInOrSwapOutRule
SwapIn or SwapOut must be present or both.
Following Must be True
    /SwapIn Must be present
 Or    /SwapOut Must be present
22.1.13.2.9.3.3.3.1.1  SwapIn <SwpIn>
Presence: [0..1]
Definition: Instrument received by the buyer.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
384 July 2025
```

