---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.23 Price", "82.1.23.3 PriceType4Choice"]
file_pages: [3103]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.23.3 PriceType4Choice

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3103 to 3103.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3103

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
82.1.23.3  PriceType4Choice
Definition: Choice of price type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Market <Mkt> [1..1] ± 3103
Or}   Indicative <Indctv> [1..1] ± 3103
82.1.23.3.1  Market <Mkt>
Presence: [1..1]
Definition: Last reported price of a financial instrument in a market, determined by supply and demand.
Market <Mkt> contains the following elements (see "Price7" on page 3101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 3101
   Value <Val> [1..1] ± 3102
82.1.23.3.2  Indicative <Indctv>
Presence: [1..1]
Definition: Estimated price, for valuation purposes.
Indicative <Indctv> contains the following elements (see "Price7" on page 3101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 3101
   Value <Val> [1..1] ± 3102
82.1.23.4  TypeOfPrice29Choice
Definition: Choice of format for the type of price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3103
Or}   Proprietary <Prtry> [1..1] ± 3104
82.1.23.4.1  Code <Cd>
Presence: [1..1]
Definition: Type of price expressed as an ISO 20022 code.
Datatype: "TypeOfPrice14Code" on page 3314
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3103 August 2026
```

