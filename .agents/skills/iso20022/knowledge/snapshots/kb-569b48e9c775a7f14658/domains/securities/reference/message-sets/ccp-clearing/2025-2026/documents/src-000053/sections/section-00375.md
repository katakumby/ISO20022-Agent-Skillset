---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.19 Transaction Type"]
file_pages: [468]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.19 Transaction Type

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 468 to 468.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 468

```text
Constraints
• Country
(Rule)
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
Error handling:
– Error severity: Fatal
– Error Code: D00004
– Error Text: Invalid Country Code.
12.1.19 Transaction Type
12.1.19.1  TradeTransactionCondition5Choice
Definition: Choice of format for the trade transaction condition.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 468
Or}   Proprietary <Prtry> [1..1] ± 469
12.1.19.1.1  Code <Cd>
Presence: [1..1]
Definition: Trade conditions expressed as an ISO 20022 code.
Datatype: TradeTransactionCondition4Code on page 484
CodeName Name Definition
CBNS CumBonus Indicates whether the trade is executed
cum bonus.
XBNS ExBonus Indicates whether the trade is executed
ex bonus.
CCPN CumCoupon Indicates whether the trade is executed
cum coupon.
XCPN ExCoupon Indicates whether the trade is executed
ex coupon.
CDIV CumDividend Indicates whether the trade is executed
cum dividend.
XDIV ExDividend Indicates whether the trade is executed
ex dividend.
CRTS CumRights Indicates whether the trade is executed
cum rights.
XRTS ExRights Indicates whether the trade is executed
ex rights.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 468
```

