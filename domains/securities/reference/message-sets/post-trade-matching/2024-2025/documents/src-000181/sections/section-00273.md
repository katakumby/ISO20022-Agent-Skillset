---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.37 BlockTrade4Choice"]
file_pages: [331]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.37 BlockTrade4Choice

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 331 to 331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
Datatype: "ActiveCurrencyCode" on page 613
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.1.19.37  BlockTrade4Choice
Definition: Choice of format for the block trade information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 331
Or}   Proprietary <Prtry> [1..1] ± 331
7.1.19.37.1  Code <Cd>
Presence: [1..1]
Definition: Block parent or child information expressed as an ISO 20022 code.
Datatype: "BlockTrade1Code" on page 615
CodeName Name Definition
BLPA Parent Transaction is a block trade parent.
BLCH Child Transaction is a block trade child.
7.1.19.37.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Block parent or child information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.38  RateOrName1Choice
Definition: Choice between a percentage rate or a rate name.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 331 February 2025
```

