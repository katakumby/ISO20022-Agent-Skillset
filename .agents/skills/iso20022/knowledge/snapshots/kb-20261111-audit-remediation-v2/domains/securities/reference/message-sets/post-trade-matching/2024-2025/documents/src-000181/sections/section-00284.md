---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.16 ProcessingDate <PrcgDt>"]
file_pages: [344]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.16 ProcessingDate <PrcgDt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 344 to 344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 344

```text
TradeDate <TradDt> contains one of the following elements (see "TradeDate7Choice" on page 267 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 267
Or}   Value <Val> [1..1]  267
{Or     Code <Cd> [1..1] CodeSet 267
Or}     Proprietary <Prtry> [1..1] ± 268
7.1.19.43.16  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Processing date of the trading session.
ProcessingDate <PrcgDt> contains one of the following elements (see "TradeDate7Choice" on
page 267 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 267
Or}   Value <Val> [1..1]  267
{Or     Code <Cd> [1..1] CodeSet 267
Or}     Proprietary <Prtry> [1..1] ± 268
7.1.19.43.17  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
SettlementDate <SttlmDt> contains one of the following elements (see "SettlementDate16Choice" on
page 264 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 265
Or}   Code <Cd> [1..1] ± 265
7.1.19.43.18  NAVDate <NAVDt>
Presence: [0..1]
Definition: Valuation point, or valuation date of the portfolio (underlying assets). This is also known as
price date.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 344 February 2025
```

