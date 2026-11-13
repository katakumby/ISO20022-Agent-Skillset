---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.26 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "55.4.5.19.26.2 Amount <Amt>"]
file_pages: [3924]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.26.2 Amount <Amt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3924 to 3924.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3924

```text
CodeName Name Definition
GATE Gating Gating of redemption proceeds.
HOLD HoldBack Hold back of redemption proceeds.
55.4.5.19.26.2  Amount <Amt>
Presence: [0..1]
Definition: Value of the redemption amount subject to gating or a hold back.
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
55.4.5.19.26.3  ExpectedReleaseDate <XpctdRlsDt>
Presence: [0..1]
Definition: Date on which the gated amount or hold back amount is expected to be released.
Datatype: "ISODate" on page 5388
55.4.5.19.26.4  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: New identification of the security.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3924 May 2026
```

