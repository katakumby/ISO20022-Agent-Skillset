---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.2 FinancialInstrumentAttributes92", "82.1.13.2.34 ExercisePrice <ExrcPric>"]
file_pages: [2943]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.2.34 ExercisePrice <ExrcPric>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2943 to 2943.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2943

```text
82.1.13.2.34  ExercisePrice <ExrcPric>
Presence: [0..1]
Definition: Predetermined price at which the holder of a derivative will buy or sell the underlying
instrument.
ExercisePrice <ExrcPric> contains the following elements (see "Price7" on page 3101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 3101
   Value <Val> [1..1] ± 3102
82.1.13.2.35  SubscriptionPrice <SbcptPric>
Presence: [0..1]
Definition: Pre-determined price at which the holder of a right is entitled to buy the underlying
instrument.
SubscriptionPrice <SbcptPric> contains the following elements (see "Price7" on page 3101 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 3101
   Value <Val> [1..1] ± 3102
82.1.13.2.36  ConversionPrice <ConvsPric>
Presence: [0..1]
Definition: Price of one target security in the conversion.
ConversionPrice <ConvsPric> contains the following elements (see "Price7" on page 3101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 3101
   Value <Val> [1..1] ± 3102
82.1.13.2.37  StrikePrice <StrkPric>
Presence: [0..1]
Definition: Predetermined price at which the holder will have to buy or sell the underlying instrument.
StrikePrice <StrkPric> contains the following elements (see "Price7" on page 3101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 3101
   Value <Val> [1..1] ± 3102
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2943 August 2026
```

