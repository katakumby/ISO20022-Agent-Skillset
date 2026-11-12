---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.1 FinancialInstrumentAttributes111", "35.1.11.1.34 SubscriptionPrice <SbcptPric>"]
file_pages: [1454]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.1.34 SubscriptionPrice <SbcptPric>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1454 to 1454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1454

```text
35.1.11.1.34  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Pre-determined price at which the holder of a right is entitled to buy the underlying
instrument.
SubscriptionPrice <SbcptPric> contains the following elements (see "Price7" on page 1715 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1716
   Value <Val> [1..1] ± 1716
35.1.11.1.35  ConversionPrice <ConvsPric>
Presence: [0..1]
Definition: Price of one target security in the conversion.
ConversionPrice <ConvsPric> contains the following elements (see "Price7" on page 1715 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1716
   Value <Val> [1..1] ± 1716
35.1.11.1.36  StrikePrice <StrkPric>
Presence: [0..1]
Definition: Predetermined price at which the holder will have to buy or sell the underlying instrument.
StrikePrice <StrkPric> contains the following elements (see "Price7" on page 1715 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1716
   Value <Val> [1..1] ± 1716
35.1.11.1.37  MinimumNominalQuantity <MinNmnlQty>
Presence: [0..1]
Definition: Minimum nominal quantity of financial instrument.
Impacted by: C12 "DigitalTokenUnitUsageRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1454 March 2026
```

