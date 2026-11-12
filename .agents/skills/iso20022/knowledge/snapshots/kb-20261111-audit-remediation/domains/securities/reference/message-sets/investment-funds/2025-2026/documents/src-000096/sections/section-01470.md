---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.47 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "43.4.5.9.47.2 Amount <Amt>"]
file_pages: [2049]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.47.2 Amount <Amt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2049 to 2049.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2049

```text
CodeName Name Definition
GATE Gating Gating of redemption proceeds.
HOLD HoldBack Hold back of redemption proceeds.
43.4.5.9.47.2  Amount <Amt>
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
43.4.5.9.47.3  ExpectedReleaseDate <XpctdRlsDt>
Presence: [0..1]
Definition: Date on which the gated amount or hold back amount is expected to be released.
Datatype: "ISODate" on page 5388
43.4.5.9.47.4  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: New identification of the security.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2049 May 2026
```

