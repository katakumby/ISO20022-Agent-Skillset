---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.17 Market", "7.1.17.7 MarketType8Choice"]
file_pages: [359]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.17.7 MarketType8Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 359 to 359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 359

```text
Definition: Nature of a market in which transactions take place.
Type <Tp> contains one of the following elements (see "MarketType8Choice" on page 359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 359
Or}   Proprietary <Prtry> [1..1] ± 359
7.1.17.7  MarketType8Choice
Definition: Choice of format for the market type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 359
Or}   Proprietary <Prtry> [1..1] ± 359
7.1.17.7.1  Code <Cd>
Presence: [1..1]
Definition: Market type expressed as an ISO 20022 code.
Datatype: "MarketType2Code" on page 515
CodeName Name Definition
PRIM PrimaryMarket The place is a primary market.
SECM SecondaryMarket The place is a secondary market.
OTCO OverTheCounter The place is over the counter.
VARI Various Various places.
EXCH StockExchange The place is a stock exchange.
7.1.17.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 359 March 2026
```

