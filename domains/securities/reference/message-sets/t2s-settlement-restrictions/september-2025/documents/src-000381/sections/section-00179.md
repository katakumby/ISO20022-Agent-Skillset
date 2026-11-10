---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.9 Financial Instrument", "9.1.9.2 FinancialInstrumentAttributes92", "9.1.9.2.34 ExercisePrice <ExrcPric>"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.9.2.34 ExercisePrice <ExrcPric>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

```text
9.1.9.2.34  ExercisePrice <ExrcPric>
Presence: [0..1]
Definition: Predetermined price at which the holder of a derivative will buy or sell the underlying
instrument.
ExercisePrice <ExrcPric> contains the following elements (see "Price7" on page 260 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 260
   Value <Val> [1..1] ± 261
9.1.9.2.35  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Pre-determined price at which the holder of a right is entitled to buy the underlying
instrument.
SubscriptionPrice <SbcptPric> contains the following elements (see "Price7" on page 260 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 260
   Value <Val> [1..1] ± 261
9.1.9.2.36  ConversionPrice <ConvsPric>
Presence: [0..1]
Definition: Price of one target security in the conversion.
ConversionPrice <ConvsPric> contains the following elements (see "Price7" on page 260 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 260
   Value <Val> [1..1] ± 261
9.1.9.2.37  StrikePrice <StrkPric>
Presence: [0..1]
Definition: Predetermined price at which the holder will have to buy or sell the underlying instrument.
StrikePrice <StrkPric> contains the following elements (see "Price7" on page 260 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 260
   Value <Val> [1..1] ± 261
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 218 September 2025
```

