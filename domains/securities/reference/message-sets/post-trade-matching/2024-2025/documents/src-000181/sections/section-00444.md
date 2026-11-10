---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.2 OtherPrices5", "7.1.22.2.10 AllMarketsWeightedAverage <AllMktsWghtdAvrg>"]
file_pages: [510]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.2.10 AllMarketsWeightedAverage <AllMktsWghtdAvrg>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 510 to 510.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 510

```text
7.1.22.2.10  AllMarketsWeightedAverage <AllMktsWghtdAvrg>
Presence: [0..1]
Definition: Price is weighted average price of all market executions during the completion of the order.
AllMarketsWeightedAverage <AllMktsWghtdAvrg> contains the following elements (see "Price14"
on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.11  Benchmark <Bchmk>
Presence: [0..1]
Definition: Price is a benchmark price relating to the current partial fills (eg, last trade tick from market).
Benchmark <Bchmk> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.12  OtherPrice <OthrPric>
Presence: [0..1]
Definition: Type of price that is not defined explicitly.
OtherPrice <OthrPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.13  IndexPrice <IndxPric>
Presence: [0..1]
Definition: Price of securities representing a particular market or a portion of it.
IndexPrice <IndxPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.14  ReportedPrice <RptdPric>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 510 February 2025
```

