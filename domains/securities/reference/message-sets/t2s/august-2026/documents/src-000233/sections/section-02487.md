---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.172 TransactionActivity1Code"]
file_pages: [3311]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.172 TransactionActivity1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3311 to 3311.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3311

```text
CodeName Name Definition
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
BCRO ResultOption Result of option when set. (UK specific).
BCRP ResultRepo Result of repo when set (UK specific).
BCFD DeliveryForm Form of delivery, not for foreign
registration when unset (UK specific).
BCBL BoardLot Board lots, not set for odd lots (UK
specific).
BCBN BadName Bad names, not set for good names (UK
specific).
MAPR MarketPrice Trade was executed at market price.
NEGO NegotiatedTrade Trade for which the price is not the one
quoted but an improved one, that is, the
negotiated price.
NMPR NonMarketPrice Trade was executed outside of normal
market conditions, for example, in the
case of an iceberg order.
BCPD DeliverCountryIncorporation Place of delivery, in country of
incorporation when unset (UK specific).
82.2.2.172  TransactionActivity1Code
Definition: Specifies the type of activity to which this transaction relates.
Type: CodeSet
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3311 August 2026
```

