---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Market", "7.1.18.5 MarketIdentification97", "7.1.18.5.2 Type <Tp>"]
file_pages: [285]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.5.2 Type <Tp>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 285 to 285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 285

```text
Identification <Id> contains one of the following elements (see "MarketIdentification3Choice" on
page 283 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 284
Or}   Description <Desc> [1..1] Text 284
7.1.18.5.2  Type <Tp>
Presence: [0..1]
Definition: Nature of a market in which transactions take place.
Type <Tp> contains one of the following elements (see "MarketType8Choice" on page 281 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 281
Or}   Proprietary <Prtry> [1..1] ± 281
7.1.19 Miscellaneous
7.1.19.1  Linkages76
Definition: Information related to a linked transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNumber <MsgNb> [0..1] ± C9 285
   Reference <Ref> [1..1] ± C7 286
7.1.19.1.1  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C9 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber17Choice"
on page 269 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 269
Or   LongNumber <LngNb> [1..1] Text 269
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 269
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 285 February 2025
```

