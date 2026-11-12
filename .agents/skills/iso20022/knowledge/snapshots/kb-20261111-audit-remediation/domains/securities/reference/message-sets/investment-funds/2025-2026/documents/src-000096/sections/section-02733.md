---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.12 CancellationRight <CxlRght>"]
file_pages: [3855]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.12 CancellationRight <CxlRght>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3855 to 3855.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3855

```text
Constraints
• OrderOriginatorEligibility1Rule
OrderOriginatorEligibility may only be present if Role is either UCL1 (UnderlyingClient1) or UCL2
(UnderlyingClient2).
55.4.5.12  CancellationRight <CxlRght>
Presence: [0..1]
Definition: Cancellation right of the investor with respect to the investment fund order.
CancellationRight <CxlRght> contains one of the following elements (see "CancellationRight1Choice"
on page 4834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4834
Or}   Proprietary <Prtry> [1..1] ± 4834
55.4.5.13  RequestedFutureTradeDate <ReqdFutrTradDt>
Presence: [0..1]
Definition: Future date at which the investor requests the order to be executed.
The specification of a requested future trade date is not allowed in some markets. The date must be a
date in the future.
Datatype: "ISODate" on page 5388
55.4.5.14  SettlementAmount <SttlmAmt>
Presence: [0..1]
Definition: Total amount of money paid /to be paid or received in exchange for the financial instrument
in the individual order.
Impacted by: C2 "ActiveCurrency", C8 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
55.4.5.15  CashSettlementDate <CshSttlmDt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3855 May 2026
```

