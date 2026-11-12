---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.49 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "46.4.5.10.49.2 Amount <Amt>"]
file_pages: [2472]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.49.2 Amount <Amt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2472 to 2472.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2472

```text
CodeName Name Definition
GATE Gating Gating of redemption proceeds.
HOLD HoldBack Hold back of redemption proceeds.
46.4.5.10.49.2  Amount <Amt>
Presence: [0..1]
Definition: Value of the redemption amount subject to gating or a hold back.
Impacted by: C3 "ActiveCurrency", C10 "CurrencyAmount"
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
46.4.5.10.49.3  ExpectedReleaseDate <XpctdRlsDt>
Presence: [0..1]
Definition: Date on which the gated amount or hold back amount is expected to be released.
Datatype: "ISODate" on page 5388
46.4.5.10.49.4  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: New identification of the security.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2472 May 2026
```

