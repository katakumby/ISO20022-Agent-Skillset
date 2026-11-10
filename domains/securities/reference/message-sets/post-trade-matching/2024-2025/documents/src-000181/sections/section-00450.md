---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.23 Rate", "7.1.23.1 RateName1", "7.1.23.1.1 Issuer <Issr>"]
file_pages: [516]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.23.1.1 Issuer <Issr>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 516 to 516.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 516

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [0..1] Text 516
   RateName <RateNm> [1..1] Text 516
7.1.23.1.1  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max8Text" on page 670
7.1.23.1.2  RateName <RateNm>
Presence: [1..1]
Definition: Rate Name specifies the reference rate or basis rate on which a variable rate is based (ex:
EONIA, EURIBOR, LIBOR, FEFUND, EURREPO).
Datatype: "Max35Text" on page 669
7.1.23.2  RateType35Choice
Definition: Choice between a code and or a data source scheme to determine the rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 516
Or}   Proprietary <Prtry> [1..1] ± 516
7.1.23.2.1  Code <Cd>
Presence: [1..1]
Definition: Rate expressed as an ISO 20022 code.
Datatype: "RateType1Code" on page 639
CodeName Name Definition
FIXE Fixed Rate is fixed.
FORF Forfeit No specific repurchase rate applies to
the transaction Repo, only a forfeit.
VARI Variable Rate is variable.
7.1.23.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Rate expressed as a proprietary code.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 516 February 2025
```

