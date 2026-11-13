---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.4 OrderDateTime <OrdrDtTm>"]
file_pages: [3288]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.4 OrderDateTime <OrdrDtTm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3288 to 3288.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3288

```text
52.4.5.4  OrderDateTime <OrdrDtTm>
Presence: [0..1]
Definition: Date and time at which the order was placed by the investor or its agent.
Datatype: "ISODateTime" on page 5388
52.4.5.5  ReceivedDateTime <RcvdDtTm>
Presence: [0..1]
Definition: Date and time the order was received by the executing party, for example, the transfer agent.
Datatype: "ISODateTime" on page 5388
52.4.5.6  RequestedFutureTradeDate <ReqdFutrTradDt>
Presence: [0..1]
Definition: Future date at which the investor requests the order to be executed.
The specification of a requested future trade date is not allowed in some markets. The date must be a
date in the future.
Datatype: "ISODate" on page 5388
52.4.5.7  CancellationRight <CxlRght>
Presence: [0..1]
Definition: Cancellation right of the investor with respect to the investment fund order.
CancellationRight <CxlRght> contains one of the following elements (see "CancellationRight1Choice"
on page 4834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4834
Or}   Proprietary <Prtry> [1..1] ± 4834
52.4.5.8  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [1..1]
Definition: Account impacted by the investment fund order execution.
Impacted by: C28 "OrderOriginatorEligibility2Rule"
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3288 May 2026
```

