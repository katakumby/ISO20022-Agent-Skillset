---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.2 OtherPrices5", "7.1.22.2.6 NetDisclosed <NetDscld>"]
file_pages: [509]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.2.6 NetDisclosed <NetDscld>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 509 to 509.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 509

```text
7.1.22.2.6  NetDisclosed <NetDscld>
Presence: [0..1]
Definition: Price is net to the disclosed client.
NetDisclosed <NetDscld> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.7  NetUndisclosed <NetUdscld>
Presence: [0..1]
Definition: Price is net to the client undisclosed (used in the UK market).
NetUndisclosed <NetUdscld> contains the following elements (see "Price14" on page 512 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.8  NotionalGross <NtnlGrss>
Presence: [0..1]
Definition: Price is notional gross (used in the UK market).
NotionalGross <NtnlGrss> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.9  BenchmarkWeightedAverage <BchmkWghtdAvrg>
Presence: [0..1]
Definition: Price is weighted average price of the benchmark prices at the time of each partial fill.
BenchmarkWeightedAverage <BchmkWghtdAvrg> contains the following elements (see "Price14"
on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 509 February 2025
```

