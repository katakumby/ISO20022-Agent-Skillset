---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.6 FinancialInstrumentAttributes <FinInstrmAttrbts>", "3.4.6.39 WarrantAttachedOnDelivery <WarrtAttchdOnDlvry>"]
file_pages: [74]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.6.39 WarrantAttachedOnDelivery <WarrtAttchdOnDlvry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 74 to 74.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 74

```text
Definition: Indicates whether the holder has the right to ask for redemption of the security prior to final
maturity. Also called RedeemableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.6.39  WarrantAttachedOnDelivery <WarrtAttchdOnDlvry>
Presence: [0..1]
Definition: Indicates whether the warrants on a financial instrument (which has been traded cum
warrants) will be attached on delivery.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.6.40  OddCouponIndicator <OddCpnInd>
Presence: [0..1]
Definition: Indicates whether the payment of the coupon (interest) on an interest bearing instrument is
off the normal schedule.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.6.41  RedemptionYieldImpact <RedYldImpct>
Presence: [0..1]
Definition: Indicates whether, in the case of a debt security subject to redemption before maturity, such
redemption could have an impact on the yield.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
3.4.6.42  YieldVariance <YldVar>
Presence: [0..1]
Definition: Indicates whether the actual yield of an asset-backed security may vary according to the rate
at which the underlying receivables or other financial assets are prepaid.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 74 February 2025
```

