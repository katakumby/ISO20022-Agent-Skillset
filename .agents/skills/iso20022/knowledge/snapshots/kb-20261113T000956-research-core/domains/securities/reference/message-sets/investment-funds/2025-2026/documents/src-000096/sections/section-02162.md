---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.3 OrderDateTime <OrdrDtTm>"]
file_pages: [3040]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.3 OrderDateTime <OrdrDtTm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3040 to 3040.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3040

```text
PlaceOfTrade <PlcOfTrad> contains one of the following elements (see
"PlaceOfTradeIdentification4Choice" on page 4808 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Country <Ctry> [1..1] CodeSet C12 4809
Or   Exchange <Xchg> [1..1] IdentifierSet 4809
Or   Party <Pty> [1..1] IdentifierSet C4 4809
Or}   OverTheCounter <OverTheCntr> [1..1] Text 4809
50.4.4.3  OrderDateTime <OrdrDtTm>
Presence: [0..1]
Definition: Date and time the order is placed by the investor or its agent.
Datatype: "ISODateTime" on page 5388
50.4.4.4  ExpiryDateTime <XpryDtTm>
Presence: [0..1]
Definition: Date on which the order expires.
ExpiryDateTime <XpryDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
50.4.4.5  RequestedFutureTradeDate <ReqdFutrTradDt>
Presence: [0..1]
Definition: Future date at which the investor requests the order to be executed. The specification of a
requested future trade date is not allowed in some markets. The date must be a date in the future.
Datatype: "ISODate" on page 5388
50.4.4.6  CancellationRight <CxlRght>
Presence: [0..1]
Definition: Cancellation right of the investor with respect to the investment fund order.
CancellationRight <CxlRght> contains one of the following elements (see "CancellationRight1Choice"
on page 4834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4834
Or}   Proprietary <Prtry> [1..1] ± 4834
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3040 May 2026
```

