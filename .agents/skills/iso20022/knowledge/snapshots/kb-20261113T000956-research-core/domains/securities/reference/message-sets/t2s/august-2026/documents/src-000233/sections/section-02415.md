---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.32 Transaction Type", "82.1.32.2 TradeTransactionCondition5Choice"]
file_pages: [3206]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.32.2 TradeTransactionCondition5Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3206 to 3206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3206

```text
82.1.32.2  TradeTransactionCondition5Choice
Definition: Choice of format for the trade transaction condition.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3206
Or}   Proprietary <Prtry> [1..1] ± 3207
82.1.32.2.1  Code <Cd>
Presence: [1..1]
Definition: Trade conditions expressed as an ISO 20022 code.
Datatype: "TradeTransactionCondition4Code" on page 3310
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
CWAR CumWarrant Indicates whether the trade is executed
cum warrant.
XWAR ExWarrant Indicates whether the trade is executed
ex warrant.
SPCU SpecialCumDividend Indicates whether the trade is executed
with a special cum
dividend, that is, buying after the ex date
and getting the dividend.
SPEX SpecialExDividend Indicates whether the trade is executed
with a special ex
dividend, that is, selling before the ex
date without the coupon.
GTDL GuaranteedDelivery Indicates whether the delivery of the
financial instrument on settlement date
is guaranteed.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3206 August 2026
```

