---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.29 Transaction Type", "7.1.29.1 SettlementTransactionCondition31Choice", "7.1.29.1.2 Proprietary <Prtry>"]
file_pages: [606]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.29.1.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 606 to 606.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 606

```text
CodeName Name Definition
UNEX Unexposed Delivery cannot be performed until
money is received.
7.1.29.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement conditions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.29.2  TradeTransactionCondition9Choice
Definition: Choice of format for the trade transaction condition.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 606
Or}   Proprietary <Prtry> [1..1] ± 606
7.1.29.2.1  Code <Cd>
Presence: [1..1]
Definition: Trade conditions expressed in a coded form as published in an external list.
Datatype: "ExternalTradeTransactionCondition1Code" on page 627
7.1.29.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade conditions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 606 February 2025
```

