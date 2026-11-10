---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Market", "7.1.18.3 MarketClientSide6Choice"]
file_pages: [283]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.3 MarketClientSide6Choice

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 283 to 283.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 283

```text
Type <Tp> contains one of the following elements (see "MarketType18Choice" on page 313 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 313
Or}   Proprietary <Prtry> [1..1] ± 313
7.1.18.3  MarketClientSide6Choice
Definition: Choice of format for the market/client side information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 283
Or}   Proprietary <Prtry> [1..1] ± 283
7.1.18.3.1  Code <Cd>
Presence: [1..1]
Definition: Market side or a client side information expressed as an ISO 20022 code.
Datatype: "MarketClientSide1Code" on page 635
CodeName Name Definition
CLNT ClientSide Instruction is for a client side transaction.
MAKT MarketSide Instruction is for a market side
transaction.
7.1.18.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Market side or a client side information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.18.4  MarketIdentification3Choice
Definition: Choice of market identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketIdentifierCode <MktIdrCd> [1..1] IdentifierSet 284
Or}   Description <Desc> [1..1] Text 284
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 283 February 2025
```

